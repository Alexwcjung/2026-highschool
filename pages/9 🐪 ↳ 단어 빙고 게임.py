import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Speaking Word Pop Game",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 말하면 단어가 터지는 영어 단어 게임")
st.caption("폰에서 마이크를 허용하고, 떨어지는 단어를 말하면 단어가 터집니다!")

# -----------------------------
# 단어 목록
# -----------------------------
all_words = [
    "cat", "dog", "sun", "run", "sit",
    "big", "red", "pen", "box", "cup",
    "fish", "book", "milk", "jump", "bed",
    "apple", "banana", "happy", "sad", "school",
    "teacher", "student", "water", "chair", "desk",
    "phone", "music", "pizza", "green", "blue"
]

# -----------------------------
# 조절 옵션 유지
# -----------------------------
speed = st.slider(
    "🚀 떨어지는 속도",
    min_value=1,
    max_value=10,
    value=4
)

word_count = st.slider(
    "📚 사용할 단어 개수",
    min_value=5,
    max_value=len(all_words),
    value=15
)

batch_count = st.slider(
    "🌧️ 한 번에 떨어지는 단어 개수",
    min_value=1,
    max_value=5,
    value=2
)

selected_words = all_words[:word_count]
word_list_js = str(selected_words)

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    body {{
        margin: 0;
        overflow: hidden;
        font-family: Arial, sans-serif;
        background: linear-gradient(180deg, #dff7ff, #fff7d6);
    }}

    #gameArea {{
        position: relative;
        width: 100%;
        height: 620px;
        overflow: hidden;
        border-radius: 28px;
        background: linear-gradient(180deg, #aeefff 0%, #fff4bd 100%);
        border: 5px solid white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }}

    .word {{
        position: absolute;
        top: -80px;
        padding: 14px 24px;
        font-size: 30px;
        font-weight: bold;
        color: #333;
        background: white;
        border-radius: 999px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
        transition: transform 0.2s, opacity 0.2s;
        white-space: nowrap;
        border: 3px solid #ffd6ea;
    }}

    .pop {{
        animation: pop 0.35s forwards;
    }}

    @keyframes pop {{
        0% {{
            transform: scale(1);
            opacity: 1;
        }}
        50% {{
            transform: scale(1.8) rotate(10deg);
            opacity: 0.8;
        }}
        100% {{
            transform: scale(0);
            opacity: 0;
        }}
    }}

    #status {{
        position: absolute;
        top: 15px;
        left: 20px;
        z-index: 10;
        background: rgba(255,255,255,0.92);
        padding: 12px 18px;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}

    #scoreBox {{
        position: absolute;
        top: 15px;
        right: 20px;
        z-index: 10;
        background: rgba(255,255,255,0.92);
        padding: 12px 18px;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}

    #startBtn {{
        position: absolute;
        bottom: 25px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 20;
        font-size: 24px;
        font-weight: bold;
        padding: 16px 36px;
        border: none;
        border-radius: 999px;
        background: linear-gradient(135deg, #ff7eb3, #ffb86c);
        color: white;
        box-shadow: 0 8px 18px rgba(0,0,0,0.25);
    }}

    #startBtn:active {{
        transform: translateX(-50%) scale(0.95);
    }}

    .effect {{
        position: absolute;
        font-size: 40px;
        pointer-events: none;
        animation: floatUp 0.7s forwards;
        z-index: 30;
    }}

    @keyframes floatUp {{
        0% {{
            opacity: 1;
            transform: translateY(0) scale(1);
        }}
        100% {{
            opacity: 0;
            transform: translateY(-60px) scale(1.5);
        }}
    }}
</style>
</head>

<body>
<div id="gameArea">
    <div id="status">🎙️ 마이크 대기 중</div>
    <div id="scoreBox">점수: <span id="score">0</span></div>
    <button id="startBtn">🎤 게임 시작</button>
</div>

<script>
const words = {word_list_js};
const gameArea = document.getElementById("gameArea");
const statusBox = document.getElementById("status");
const scoreSpan = document.getElementById("score");
const startBtn = document.getElementById("startBtn");

let activeWords = [];
let score = 0;
let gameStarted = false;

let fallSpeed = {speed};
let batchCount = {batch_count};

// 속도 조절
let baseSpeed = 0.45 + fallSpeed * 0.28;

// 단어 겹침 방지용 레인
const laneCount = 6;
let laneBusy = Array(laneCount).fill(false);

function getLaneX(laneIndex) {{
    const areaWidth = gameArea.clientWidth;
    const laneWidth = areaWidth / laneCount;

    // 단어 폭을 고려해서 레인 안쪽에 배치
    const minPadding = 8;
    const maxOffset = Math.max(10, laneWidth - 130);
    const randomOffset = minPadding + Math.random() * maxOffset;

    return laneIndex * laneWidth + randomOffset;
}}

function getFreeLane() {{
    let freeLanes = [];

    for (let i = 0; i < laneCount; i++) {{
        if (!laneBusy[i]) {{
            freeLanes.push(i);
        }}
    }}

    // 모든 레인이 사용 중이면 생성하지 않음
    if (freeLanes.length === 0) {{
        return null;
    }}

    return freeLanes[Math.floor(Math.random() * freeLanes.length)];
}}

function createOneWord() {{
    if (!gameStarted) return;

    const lane = getFreeLane();

    // 빈 레인이 없으면 이번 단어는 건너뜀
    if (lane === null) return;

    laneBusy[lane] = true;

    const wordText = words[Math.floor(Math.random() * words.length)];
    const wordDiv = document.createElement("div");

    wordDiv.className = "word";
    wordDiv.innerText = wordText;
    wordDiv.dataset.word = wordText.toLowerCase();
    wordDiv.dataset.lane = lane;
    wordDiv.style.left = getLaneX(lane) + "px";
    wordDiv.style.top = "-80px";

    gameArea.appendChild(wordDiv);

    activeWords.push({{
        element: wordDiv,
        word: wordText.toLowerCase(),
        y: -80,
        speed: baseSpeed + Math.random() * 0.5,
        lane: lane
    }});

    // 일정 시간 후 같은 레인에 새 단어 생성 가능
    // 이 시간이 길수록 덜 겹침
    setTimeout(() => {{
        laneBusy[lane] = false;
    }}, 1700);
}}

function createWordsBatch() {{
    if (!gameStarted) return;

    for (let i = 0; i < batchCount; i++) {{
        setTimeout(() => {{
            createOneWord();
        }}, i * 180);
    }}
}}

function moveWords() {{
    for (let i = activeWords.length - 1; i >= 0; i--) {{
        let item = activeWords[i];
        item.y += item.speed;
        item.element.style.top = item.y + "px";

        if (item.y > gameArea.clientHeight + 90) {{
            item.element.remove();
            activeWords.splice(i, 1);
        }}
    }}

    requestAnimationFrame(moveWords);
}}

function popWord(spokenText) {{
    spokenText = spokenText.toLowerCase().trim();

    for (let i = activeWords.length - 1; i >= 0; i--) {{
        let item = activeWords[i];

        if (spokenText.includes(item.word)) {{
            const rect = item.element.getBoundingClientRect();
            const parentRect = gameArea.getBoundingClientRect();

            showEffect(
                rect.left - parentRect.left,
                rect.top - parentRect.top
            );

            item.element.classList.add("pop");

            setTimeout(() => {{
                if (item.element) item.element.remove();
            }}, 300);

            activeWords.splice(i, 1);
            score++;
            scoreSpan.innerText = score;
            break;
        }}
    }}
}}

function showEffect(x, y) {{
    const effects = ["💥", "✨", "🎉", "⭐", "👏", "🌟"];
    const effect = document.createElement("div");
    effect.className = "effect";
    effect.innerText = effects[Math.floor(Math.random() * effects.length)];
    effect.style.left = x + "px";
    effect.style.top = y + "px";
    gameArea.appendChild(effect);

    setTimeout(() => {{
        effect.remove();
    }}, 700);
}}

function startSpeechRecognition() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {{
        statusBox.innerText = "❌ 이 브라우저는 음성 인식을 지원하지 않습니다";
        return;
    }}

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onstart = function() {{
        statusBox.innerText = "🎧 듣는 중...";
    }};

    recognition.onresult = function(event) {{
        let transcript = "";

        for (let i = event.resultIndex; i < event.results.length; i++) {{
            transcript += event.results[i][0].transcript;
        }}

        statusBox.innerText = "🗣️ " + transcript;
        popWord(transcript);
    }};

    recognition.onerror = function(event) {{
        statusBox.innerText = "⚠️ 마이크 오류: " + event.error;
    }};

    recognition.onend = function() {{
        if (gameStarted) {{
            try {{
                recognition.start();
            }} catch(e) {{}}
        }}
    }};

    recognition.start();
}}

startBtn.addEventListener("click", function() {{
    gameStarted = true;
    startBtn.style.display = "none";
    score = 0;
    scoreSpan.innerText = score;

    startSpeechRecognition();

    // 단어 생성 간격
    // 숫자를 줄이면 더 자주 나옴
    setInterval(createWordsBatch, 1300);
}});

moveWords();
</script>
</body>
</html>
"""

components.html(html_code, height=700)
