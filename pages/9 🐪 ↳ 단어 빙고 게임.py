import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Speaking Word Pop Game",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 말하면 단어가 터지는 파닉스 게임")
st.caption("폰에서 마이크를 허용하고, 떨어지는 단어를 말하면 단어가 터집니다!")

words = [
    "cat", "dog", "sun", "run", "sit",
    "big", "red", "pen", "box", "cup",
    "fish", "book", "milk", "jump", "bed"
]

speed = st.slider(
    "🚀 단어 떨어지는 속도 조절",
    min_value=1,
    max_value=10,
    value=4
)

word_list_js = str(words)

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
        background: linear-gradient(180deg, #e0f7ff, #fff7d6);
    }}

    #gameArea {{
        position: relative;
        width: 100%;
        height: 620px;
        overflow: hidden;
        border-radius: 25px;
        background: linear-gradient(180deg, #b3ecff, #fff5cc);
        border: 4px solid #ffffff;
    }}

    .word {{
        position: absolute;
        top: -70px;
        padding: 14px 24px;
        font-size: 30px;
        font-weight: bold;
        color: #333;
        background: white;
        border-radius: 999px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
        transition: transform 0.2s, opacity 0.2s;
        white-space: nowrap;
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
            transform: scale(1.7) rotate(10deg);
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
        background: rgba(255,255,255,0.9);
        padding: 12px 18px;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
    }}

    #scoreBox {{
        position: absolute;
        top: 15px;
        right: 20px;
        z-index: 10;
        background: rgba(255,255,255,0.9);
        padding: 12px 18px;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
    }}

    #startBtn {{
        position: absolute;
        bottom: 25px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 20;
        font-size: 24px;
        font-weight: bold;
        padding: 16px 34px;
        border: none;
        border-radius: 999px;
        background: #ff7eb3;
        color: white;
        box-shadow: 0 8px 18px rgba(0,0,0,0.25);
    }}

    #startBtn:active {{
        transform: translateX(-50%) scale(0.95);
    }}

    .effect {{
        position: absolute;
        font-size: 38px;
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

// Streamlit 슬라이더 값
let fallSpeed = {speed};

// 속도 계산
// 숫자가 클수록 더 빠르게
let baseSpeed = 0.6 + fallSpeed * 0.35;

// 단어 겹침 방지용 레인
const laneCount = 5;
let laneBusy = Array(laneCount).fill(false);

function getLaneX(laneIndex) {{
    const areaWidth = gameArea.clientWidth;
    const laneWidth = areaWidth / laneCount;
    const randomOffset = Math.random() * Math.max(10, laneWidth - 130);
    return laneIndex * laneWidth + randomOffset;
}}

function getFreeLane() {{
    let freeLanes = [];

    for (let i = 0; i < laneCount; i++) {{
        if (!laneBusy[i]) {{
            freeLanes.push(i);
        }}
    }}

    // 빈 레인이 없으면 랜덤 레인 사용
    // 하지만 생성 간격이 있어서 실제로는 거의 안 겹침
    if (freeLanes.length === 0) {{
        return Math.floor(Math.random() * laneCount);
    }}

    return freeLanes[Math.floor(Math.random() * freeLanes.length)];
}}

function createWord() {{
    if (!gameStarted) return;

    const wordText = words[Math.floor(Math.random() * words.length)];
    const wordDiv = document.createElement("div");

    const lane = getFreeLane();
    laneBusy[lane] = true;

    wordDiv.className = "word";
    wordDiv.innerText = wordText;
    wordDiv.dataset.word = wordText.toLowerCase();
    wordDiv.dataset.lane = lane;
    wordDiv.style.left = getLaneX(lane) + "px";
    wordDiv.style.top = "-70px";

    gameArea.appendChild(wordDiv);

    activeWords.push({{
        element: wordDiv,
        word: wordText.toLowerCase(),
        y: -70,
        speed: baseSpeed + Math.random() * 0.8,
        lane: lane
    }});

    // 일정 시간 후 해당 레인 다시 사용 가능
    setTimeout(() => {{
        laneBusy[lane] = false;
    }}, 1500);
}}

function moveWords() {{
    for (let i = activeWords.length - 1; i >= 0; i--) {{
        let item = activeWords[i];
        item.y += item.speed;
        item.element.style.top = item.y + "px";

        if (item.y > gameArea.clientHeight + 80) {{
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
    const effects = ["💥", "✨", "🎉", "⭐", "👏"];
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
            recognition.start();
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
    // 속도가 빠를수록 너무 많이 생기지 않게 약간 조절
    setInterval(createWord, 1300);
}});

moveWords();
</script>
</body>
</html>
"""

components.html(html_code, height=680)
