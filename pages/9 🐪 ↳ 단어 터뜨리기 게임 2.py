import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="단어 뜻 터뜨리기 게임",
    page_icon="💥",
    layout="wide"
)

st.title("💥 단어 뜻 터뜨리기 게임")
st.caption("위에서 떨어지는 영어 단어의 한국어 뜻을 입력하면 단어가 터집니다!")

# -----------------------------
# 단어 + 한국어 뜻 목록
# -----------------------------
word_data = [
    {"word": "cat", "meanings": ["고양이"]},
    {"word": "dog", "meanings": ["개"]},
    {"word": "sun", "meanings": ["태양", "해"]},
    {"word": "run", "meanings": ["달리다", "뛰다"]},
    {"word": "sit", "meanings": ["앉다"]},
    {"word": "big", "meanings": ["큰", "크다"]},
    {"word": "red", "meanings": ["빨간", "빨간색"]},
    {"word": "pen", "meanings": ["펜"]},
    {"word": "box", "meanings": ["상자"]},
    {"word": "cup", "meanings": ["컵"]},
    {"word": "fish", "meanings": ["물고기", "생선"]},
    {"word": "book", "meanings": ["책"]},
    {"word": "milk", "meanings": ["우유"]},
    {"word": "jump", "meanings": ["점프하다", "뛰다", "뛰어오르다"]},
    {"word": "bed", "meanings": ["침대"]},
    {"word": "apple", "meanings": ["사과"]},
    {"word": "banana", "meanings": ["바나나"]},
    {"word": "happy", "meanings": ["행복한", "기쁜"]},
    {"word": "sad", "meanings": ["슬픈"]},
    {"word": "school", "meanings": ["학교"]},
    {"word": "teacher", "meanings": ["선생님", "교사"]},
    {"word": "student", "meanings": ["학생"]},
    {"word": "water", "meanings": ["물"]},
    {"word": "chair", "meanings": ["의자"]},
    {"word": "desk", "meanings": ["책상"]},
    {"word": "phone", "meanings": ["전화기", "휴대폰", "폰"]},
    {"word": "music", "meanings": ["음악"]},
    {"word": "pizza", "meanings": ["피자"]},
    {"word": "green", "meanings": ["초록색", "초록", "녹색"]},
    {"word": "blue", "meanings": ["파란색", "파랑", "푸른"]},
]

# -----------------------------
# 조절 옵션
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
    max_value=len(word_data),
    value=15
)

batch_count = st.slider(
    "🌧️ 한 번에 떨어지는 단어 개수",
    min_value=1,
    max_value=5,
    value=2
)

show_hint = st.checkbox(
    "💡 뜻 힌트 보기",
    value=False
)

selected_words = word_data[:word_count]
word_data_js = json.dumps(selected_words, ensure_ascii=False)
show_hint_js = "true" if show_hint else "false"

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
        height: 660px;
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
        z-index: 5;
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
        z-index: 20;
        background: rgba(255,255,255,0.94);
        padding: 12px 18px;
        border-radius: 20px;
        font-size: 19px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        max-width: 55%;
        line-height: 1.4;
    }}

    #scoreBox {{
        position: absolute;
        top: 15px;
        right: 20px;
        z-index: 20;
        background: rgba(255,255,255,0.94);
        padding: 12px 18px;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}

    #inputPanel {{
        position: absolute;
        bottom: 22px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 30;
        width: 86%;
        background: rgba(255,255,255,0.95);
        border: 3px solid #bfdbfe;
        border-radius: 28px;
        padding: 18px 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
        box-sizing: border-box;
        text-align: center;
    }}

    #answerInput {{
        width: 68%;
        padding: 14px 18px;
        border-radius: 999px;
        border: 2px solid #93c5fd;
        font-size: 22px;
        font-weight: bold;
        outline: none;
        text-align: center;
    }}

    #answerInput:focus {{
        border-color: #ec4899;
        box-shadow: 0 0 0 4px rgba(236,72,153,0.15);
    }}

    #submitBtn {{
        margin-left: 10px;
        padding: 14px 24px;
        border: none;
        border-radius: 999px;
        font-size: 21px;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #ff7eb3, #ffb86c);
        box-shadow: 0 6px 14px rgba(0,0,0,0.18);
    }}

    #startBtn {{
        margin-left: 10px;
        padding: 14px 24px;
        border: none;
        border-radius: 999px;
        font-size: 21px;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #60a5fa, #34d399);
        box-shadow: 0 6px 14px rgba(0,0,0,0.18);
    }}

    #hintBox {{
        margin-top: 10px;
        font-size: 17px;
        font-weight: bold;
        color: #475569;
        min-height: 24px;
    }}

    .effect {{
        position: absolute;
        font-size: 42px;
        pointer-events: none;
        animation: floatUp 0.7s forwards;
        z-index: 40;
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

    @media (max-width: 700px) {{
        #gameArea {{
            height: 620px;
            border-radius: 22px;
        }}

        .word {{
            font-size: 24px;
            padding: 11px 18px;
        }}

        #status {{
            font-size: 15px;
            max-width: 52%;
            padding: 9px 12px;
            top: 10px;
            left: 10px;
        }}

        #scoreBox {{
            font-size: 16px;
            padding: 9px 12px;
            top: 10px;
            right: 10px;
        }}

        #inputPanel {{
            width: 94%;
            padding: 14px 12px;
            bottom: 14px;
        }}

        #answerInput {{
            width: 58%;
            font-size: 18px;
            padding: 12px 14px;
        }}

        #submitBtn, #startBtn {{
            font-size: 16px;
            padding: 12px 14px;
            margin-left: 4px;
        }}

        #hintBox {{
            font-size: 14px;
        }}
    }}
</style>
</head>

<body>
<div id="gameArea">
    <div id="status">🎮 게임 시작을 누르세요</div>
    <div id="scoreBox">점수: <span id="score">0</span></div>

    <div id="inputPanel">
        <input id="answerInput" type="text" placeholder="한국어 뜻 입력 예: 고양이" autocomplete="off">
        <button id="submitBtn">💥 제출</button>
        <button id="startBtn">▶️ 시작</button>
        <div id="hintBox"></div>
    </div>
</div>

<script>
const wordData = {word_data_js};
const showHint = {show_hint_js};

const gameArea = document.getElementById("gameArea");
const statusBox = document.getElementById("status");
const scoreSpan = document.getElementById("score");
const answerInput = document.getElementById("answerInput");
const submitBtn = document.getElementById("submitBtn");
const startBtn = document.getElementById("startBtn");
const hintBox = document.getElementById("hintBox");

let activeWords = [];
let score = 0;
let gameStarted = false;
let createInterval = null;

let fallSpeed = {speed};
let batchCount = {batch_count};

// 속도 조절: 숫자가 클수록 빠름
let baseSpeed = 0.12 + fallSpeed * 0.08;

// 단어 겹침 방지용 레인
const laneCount = 6;
let laneBusy = Array(laneCount).fill(false);

function normalizeKorean(text) {{
    return text
        .toLowerCase()
        .replace(/\\s+/g, "")
        .replace(/[.,!?~]/g, "")
        .trim();
}}

function getLaneX(laneIndex) {{
    const areaWidth = gameArea.clientWidth;
    const laneWidth = areaWidth / laneCount;
    const maxOffset = Math.max(5, laneWidth - 120);
    const randomOffset = 6 + Math.random() * maxOffset;
    return laneIndex * laneWidth + randomOffset;
}}

function getFreeLane() {{
    let freeLanes = [];

    for (let i = 0; i < laneCount; i++) {{
        if (!laneBusy[i]) {{
            freeLanes.push(i);
        }}
    }}

    if (freeLanes.length === 0) {{
        return null;
    }}

    return freeLanes[Math.floor(Math.random() * freeLanes.length)];
}}

function createOneWord() {{
    if (!gameStarted) return;

    const lane = getFreeLane();
    if (lane === null) return;

    laneBusy[lane] = true;

    const item = wordData[Math.floor(Math.random() * wordData.length)];
    const wordDiv = document.createElement("div");

    wordDiv.className = "word";
    wordDiv.innerText = item.word;
    wordDiv.dataset.word = item.word;
    wordDiv.style.left = getLaneX(lane) + "px";
    wordDiv.style.top = "-80px";

    gameArea.appendChild(wordDiv);

    activeWords.push({{
        element: wordDiv,
        word: item.word,
        meanings: item.meanings,
        y: -80,
        speed: baseSpeed + Math.random() * 0.15,
        lane: lane
    }});

    setTimeout(() => {{
        laneBusy[lane] = false;
    }}, 1900);
}}

function createWordsBatch() {{
    if (!gameStarted) return;

    for (let i = 0; i < batchCount; i++) {{
        setTimeout(() => {{
            createOneWord();
        }}, i * 220);
    }}
}}

function moveWords() {{
    for (let i = activeWords.length - 1; i >= 0; i--) {{
        let item = activeWords[i];
        item.y += item.speed;
        item.element.style.top = item.y + "px";

        if (item.y > gameArea.clientHeight - 120) {{
            item.element.remove();
            activeWords.splice(i, 1);
        }}
    }}

    updateHint();
    requestAnimationFrame(moveWords);
}}

function checkAnswer() {{
    if (!gameStarted) return;

    const userAnswer = normalizeKorean(answerInput.value);

    if (!userAnswer) {{
        statusBox.innerText = "✏️ 한국어 뜻을 입력하세요!";
        return;
    }}

    for (let i = activeWords.length - 1; i >= 0; i--) {{
        let item = activeWords[i];

        let correct = item.meanings.some(m => normalizeKorean(m) === userAnswer);

        if (correct) {{
            popWord(item, i);
            answerInput.value = "";
            return;
        }}
    }}

    statusBox.innerText = "🤔 아직 맞는 단어가 없어요: " + answerInput.value;
    answerInput.select();
}}

function popWord(item, index) {{
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

    activeWords.splice(index, 1);
    score++;
    scoreSpan.innerText = score;

    statusBox.innerText = "✅ 정답! " + item.word + " = " + item.meanings[0];
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

function updateHint() {{
    if (!showHint || !gameStarted) {{
        hintBox.innerText = "";
        return;
    }}

    if (activeWords.length === 0) {{
        hintBox.innerText = "";
        return;
    }}

    const sample = activeWords[activeWords.length - 1];
    const firstMeaning = sample.meanings[0];
    hintBox.innerText = "💡 힌트: 화면의 한 단어 뜻은 '" + firstMeaning[0] + "'로 시작합니다.";
}}

function startGame() {{
    if (gameStarted) return;

    gameStarted = true;
    score = 0;
    activeWords = [];
    scoreSpan.innerText = score;
    statusBox.innerText = "✏️ 떨어지는 단어의 한국어 뜻을 입력하세요!";

    answerInput.focus();

    createInterval = setInterval(createWordsBatch, 1300);
}}

submitBtn.addEventListener("click", checkAnswer);

answerInput.addEventListener("keydown", function(event) {{
    if (event.key === "Enter") {{
        checkAnswer();
    }}
}});

startBtn.addEventListener("click", startGame);

moveWords();
</script>
</body>
</html>
"""

components.html(html_code, height=730)
