import streamlit as st
import streamlit.components.v1 as components
import json

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Mole Speaking Game",
    page_icon="🕳️",
    layout="centered"
)

st.title("🕳️ Phonics Mole Speaking Game")
st.caption("단어 두더지가 튀어나오면 영어로 말해 보세요. 맞히면 팡! 하고 터집니다.")

# =========================
# 단어 데이터
# =========================
word_sets = {
    "짧은 모음": [
        "cat", "bat", "hat", "bed", "egg",
        "sit", "pig", "hot", "cup", "bus",
        "fox", "dog", "sun", "jam", "van"
    ],
    "긴 모음": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope",
        "see", "tree", "goat", "rain", "day"
    ],
    "Blends": [
        "black", "brown", "clock", "crab", "drum",
        "flag", "frog", "green", "spoon", "star",
        "blue", "grass", "snake", "smile", "train"
    ],
    "Digraphs": [
        "chair", "ship", "three", "this", "phone",
        "whale", "duck", "shop", "cheese", "photo",
        "fish", "chick", "thin", "thank", "white"
    ],
    "Vowel Teams": [
        "rain", "day", "see", "eat", "boat",
        "snow", "cow", "house", "coin", "boy",
        "road", "team", "seed", "toy", "out"
    ],
    "R-Controlled": [
        "car", "star", "her", "bird", "girl",
        "corn", "fork", "turn", "burn", "teacher",
        "park", "farm", "short", "shirt", "tiger"
    ],
    "Silent e": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope",
        "lake", "time", "nose", "line", "game"
    ],
}

# =========================
# 게임 설정
# =========================
st.markdown("### 🎲 게임 설정")

category = st.selectbox(
    "단어 세트 선택",
    list(word_sets.keys())
)

col1, col2 = st.columns(2)

with col1:
    mole_count = st.slider(
        "한 번에 나오는 두더지 수",
        min_value=1,
        max_value=5,
        value=3,
        step=1
    )

    show_time = st.slider(
        "두더지가 나와 있는 시간",
        min_value=2,
        max_value=8,
        value=5,
        step=1
    )

with col2:
    target_score = st.slider(
        "목표 점수",
        min_value=5,
        max_value=50,
        value=15,
        step=5
    )

    lives = st.slider(
        "기회",
        min_value=3,
        max_value=10,
        value=5,
        step=1
    )

pass_ratio = st.slider(
    "정답 인정 기준",
    min_value=50,
    max_value=100,
    value=70,
    step=5,
    help="낮을수록 발음을 더 너그럽게 인정합니다."
)

words = word_sets[category]

# =========================
# 안내 박스
# =========================
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #fff7ed, #eef7ff);
        border: 2px solid #fed7aa;
        border-radius: 22px;
        padding: 18px 20px;
        margin: 16px 0 22px 0;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        font-size: 18px;
        line-height: 1.7;
    ">
        🕳️ <b>두더지 단어가 튀어나오면 바로 영어로 말하세요.</b><br>
        🎤 맞게 인식되면 단어가 <b>팡!</b> 하고 터지고 점수가 올라갑니다.<br>
        📱 폰에서는 Chrome으로 접속하고 마이크 권한을 허용해 주세요.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# HTML 게임 데이터
# =========================
game_data = {
    "words": words,
    "moleCount": mole_count,
    "showTime": show_time,
    "targetScore": target_score,
    "lives": lives,
    "passRatio": pass_ratio / 100
}

game_json = json.dumps(game_data, ensure_ascii=False)

# =========================
# 두더지 게임 HTML
# =========================
game_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: transparent;
    }}

    .game-wrap {{
        width: 100%;
        min-height: 690px;
        background: linear-gradient(180deg, #dbeafe 0%, #dcfce7 55%, #fef9c3 100%);
        border-radius: 28px;
        border: 4px solid #93c5fd;
        box-shadow: 0 10px 28px rgba(0,0,0,0.14);
        padding: 20px;
        box-sizing: border-box;
        position: relative;
        overflow: hidden;
    }}

    .top-bar {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-bottom: 16px;
    }}

    .score-card {{
        background: linear-gradient(135deg, #fff7ed, #fef3c7);
        border-radius: 20px;
        padding: 13px 8px;
        text-align: center;
        font-size: 19px;
        font-weight: 900;
        border: 3px solid #fed7aa;
        box-shadow: 0 5px 12px rgba(0,0,0,0.10);
        color: #334155;
        line-height: 1.35;
    }}

    .message-box {{
        background: linear-gradient(135deg, #fef3c7, #fed7aa);
        border: 4px solid #fb923c;
        border-radius: 24px;
        padding: 14px;
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        color: #7c2d12;
        margin-bottom: 16px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.14);
        min-height: 34px;
        line-height: 1.35;
    }}

    .field {{
        position: relative;
        width: 100%;
        height: 410px;
        background: linear-gradient(180deg, #bbf7d0 0%, #86efac 100%);
        border-radius: 28px;
        border: 4px solid rgba(255,255,255,0.85);
        overflow: hidden;
        box-shadow: inset 0 8px 18px rgba(0,0,0,0.08);
    }}

    .hole {{
        position: absolute;
        width: 165px;
        height: 58px;
        background: #6b3f2a;
        border-radius: 50%;
        box-shadow: inset 0 8px 13px rgba(0,0,0,0.38);
        z-index: 1;
    }}

    .hole1 {{ left: 8%; top: 74%; }}
    .hole2 {{ left: 39%; top: 74%; }}
    .hole3 {{ left: 70%; top: 74%; }}
    .hole4 {{ left: 21%; top: 45%; }}
    .hole5 {{ left: 57%; top: 45%; }}

    .mole {{
        position: absolute;
        width: 175px;
        min-height: 110px;
        background: linear-gradient(135deg, #ffffff, #fff7ed);
        border: 4px solid #fb923c;
        border-radius: 32px;
        box-shadow: 0 10px 22px rgba(0,0,0,0.20);
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-size: 36px;
        font-weight: 900;
        color: #111827;
        transform: translateY(80px) scale(0.7);
        opacity: 0;
        transition: all 0.23s ease;
        z-index: 5;
        padding: 8px;
        box-sizing: border-box;
        word-break: keep-all;
    }}

    .mole.show {{
        transform: translateY(0) scale(1);
        opacity: 1;
    }}

    .mole.pop {{
        animation: pop 0.45s forwards;
    }}

    @keyframes pop {{
        0% {{
            transform: scale(1);
            opacity: 1;
        }}
        50% {{
            transform: scale(1.5) rotate(5deg);
            opacity: 0.9;
        }}
        100% {{
            transform: scale(0);
            opacity: 0;
        }}
    }}

    .control-row {{
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 22px;
    }}

    .btn {{
        border: none;
        border-radius: 999px;
        padding: 13px 26px;
        font-size: 21px;
        font-weight: 900;
        color: white;
        background: linear-gradient(135deg, #ff7eb3, #ffb86c);
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
    }}

    .sub-btn {{
        background: linear-gradient(135deg, #60a5fa, #93c5fd);
    }}

    .btn:active {{
        transform: scale(0.96);
    }}

    .recognized {{
        margin-top: 16px;
        text-align: center;
        font-size: 19px;
        font-weight: 900;
        color: #475569;
        min-height: 32px;
        line-height: 1.5;
    }}

    .effect {{
        position: absolute;
        font-size: 42px;
        animation: floatUp 0.75s forwards;
        pointer-events: none;
        z-index: 30;
    }}

    @keyframes floatUp {{
        0% {{
            opacity: 1;
            transform: translateY(0) scale(1);
        }}
        100% {{
            opacity: 0;
            transform: translateY(-70px) scale(1.6);
        }}
    }}

    @media (max-width: 700px) {{
        .game-wrap {{
            padding: 10px;
            min-height: 640px;
            border-radius: 22px;
            border-width: 3px;
        }}

        .top-bar {{
            grid-template-columns: repeat(4, 1fr);
            gap: 5px;
            margin-bottom: 10px;
        }}

        .score-card {{
            font-size: 13px;
            padding: 8px 4px;
            border-radius: 14px;
            border-width: 2px;
            line-height: 1.3;
        }}

        .message-box {{
            font-size: 17px;
            padding: 10px 8px;
            border-radius: 18px;
            margin-bottom: 10px;
            border-width: 3px;
            min-height: 30px;
        }}

        .field {{
            height: 330px;
            border-radius: 20px;
            border-width: 3px;
        }}

        .hole {{
            width: 94px;
            height: 35px;
        }}

        .hole1 {{ left: 4%; top: 76%; }}
        .hole2 {{ left: 36%; top: 76%; }}
        .hole3 {{ left: 68%; top: 76%; }}
        .hole4 {{ left: 20%; top: 47%; }}
        .hole5 {{ left: 52%; top: 47%; }}

        .mole {{
            width: 98px;
            min-height: 74px;
            font-size: 22px;
            border-radius: 19px;
            border-width: 3px;
            padding: 5px;
        }}

        .control-row {{
            gap: 6px;
            margin-top: 15px;
        }}

        .btn {{
            font-size: 15px;
            padding: 10px 12px;
        }}

        .recognized {{
            font-size: 15px;
            margin-top: 12px;
        }}

        .effect {{
            font-size: 34px;
        }}
    }}
</style>
</head>

<body>
<div class="game-wrap">
    <div class="top-bar">
        <div class="score-card">⭐ 점수<br><span id="score">0</span></div>
        <div class="score-card">❤️ 기회<br><span id="lives">0</span></div>
        <div class="score-card">🎯 목표<br><span id="target">0</span></div>
        <div class="score-card">⏱️ 시간<br><span id="timeLeft">0</span>초</div>
    </div>

    <div id="message" class="message-box">
        게임 시작을 누르면 두더지 단어가 튀어나옵니다!
    </div>

    <div class="field" id="field">
        <div class="hole hole1"></div>
        <div class="hole hole2"></div>
        <div class="hole hole3"></div>
        <div class="hole hole4"></div>
        <div class="hole hole5"></div>
    </div>

    <div class="control-row">
        <button class="btn" onclick="startGame()">🎤 게임 시작</button>
        <button class="btn sub-btn" onclick="nextRound()">➡️ 다음 단어</button>
        <button class="btn sub-btn" onclick="resetGame()">🔄 다시 시작</button>
    </div>

    <div id="recognized" class="recognized">
        마이크 권한을 허용하고, 보이는 단어 중 하나를 말해 보세요.
    </div>
</div>

<script>
const config = {game_json};

let words = config.words;
let moleCount = config.moleCount;
let showTime = config.showTime;
let targetScore = config.targetScore;
let maxLives = config.lives;
let passRatio = config.passRatio;

let score = 0;
let lives = maxLives;
let gameStarted = false;
let activeMoles = [];
let usedWords = [];
let recognition = null;
let timer = null;
let timeLeft = showTime;
let roundLocked = false;

const field = document.getElementById("field");
const scoreBox = document.getElementById("score");
const livesBox = document.getElementById("lives");
const targetBox = document.getElementById("target");
const timeLeftBox = document.getElementById("timeLeft");
const messageBox = document.getElementById("message");
const recognizedBox = document.getElementById("recognized");

targetBox.innerText = targetScore;
livesBox.innerText = lives;
timeLeftBox.innerText = showTime;

const isMobile = window.innerWidth <= 700;

const positions = isMobile ? [
    {{left: "4%", top: "54%"}},
    {{left: "36%", top: "54%"}},
    {{left: "68%", top: "54%"}},
    {{left: "20%", top: "25%"}},
    {{left: "52%", top: "25%"}}
] : [
    {{left: "8%", top: "50%"}},
    {{left: "39%", top: "50%"}},
    {{left: "70%", top: "50%"}},
    {{left: "21%", top: "21%"}},
    {{left: "57%", top: "21%"}}
];

function normalizeText(text) {{
    return text
        .toLowerCase()
        .replace(/[.,!?]/g, "")
        .replace(/\\s+/g, " ")
        .trim();
}}

function shuffle(array) {{
    for (let i = array.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }}
    return array;
}}

function getRandomWord() {{
    let remaining = words.filter(w => !usedWords.includes(w));

    if (remaining.length === 0) {{
        usedWords = [];
        remaining = [...words];
    }}

    const word = remaining[Math.floor(Math.random() * remaining.length)];
    usedWords.push(word);
    return word;
}}

function similarityCheck(spoken, target) {{
    let s = normalizeText(spoken);
    let t = normalizeText(target);

    if (s === t) return true;

    let spokenWords = s.split(" ");
    if (spokenWords.includes(t)) return true;

    let matched = 0;
    for (let i = 0; i < Math.min(s.length, t.length); i++) {{
        if (s[i] === t[i]) matched++;
    }}

    let ratio = matched / t.length;
    return ratio >= passRatio;
}}

function clearMoles() {{
    activeMoles.forEach(m => {{
        if (m.element) m.element.remove();
    }});
    activeMoles = [];
}}

function createMoles() {{
    clearMoles();

    let selectedPositions = shuffle([...positions]).slice(0, moleCount);

    selectedPositions.forEach((pos, index) => {{
        const word = getRandomWord();

        const mole = document.createElement("div");
        mole.className = "mole";
        mole.innerText = word;
        mole.style.left = pos.left;
        mole.style.top = pos.top;
        mole.dataset.word = word;

        field.appendChild(mole);

        activeMoles.push({{
            word: word,
            element: mole,
            popped: false
        }});

        setTimeout(() => {{
            mole.classList.add("show");
        }}, 120 + index * 100);
    }});
}}

function startTimer() {{
    clearInterval(timer);
    timeLeft = showTime;
    timeLeftBox.innerText = timeLeft;

    timer = setInterval(() => {{
        timeLeft--;
        timeLeftBox.innerText = timeLeft;

        if (timeLeft <= 0) {{
            clearInterval(timer);

            if (!roundLocked) {{
                lives--;
                livesBox.innerText = lives;

                if (lives <= 0) {{
                    endGame(false);
                    return;
                }}

                messageBox.innerText = "😢 시간 끝! 단어를 놓쳤어요.";
                nextRoundDelay(800);
            }}
        }}
    }}, 1000);
}}

function nextRound() {{
    if (!gameStarted) return;

    roundLocked = false;
    messageBox.innerText = "🎧 듣는 중... 보이는 단어를 말해 보세요!";
    createMoles();
    startTimer();
}}

function nextRoundDelay(ms) {{
    setTimeout(() => {{
        nextRound();
    }}, ms);
}}

function showEffects() {{
    const icons = ["💥", "✨", "🎉", "⭐", "👏", "🌟"];

    for (let i = 0; i < 12; i++) {{
        const e = document.createElement("div");
        e.className = "effect";
        e.innerText = icons[Math.floor(Math.random() * icons.length)];
        e.style.left = Math.random() * 80 + 10 + "%";
        e.style.top = Math.random() * 50 + 15 + "%";
        field.appendChild(e);

        setTimeout(() => {{
            e.remove();
        }}, 800);
    }}
}}

function popMole(moleObj) {{
    if (moleObj.popped) return;

    moleObj.popped = true;
    moleObj.element.classList.add("pop");

    score++;
    scoreBox.innerText = score;

    messageBox.innerText = "💥 BOOM! '" + moleObj.word + "' 터졌다!";
    showEffects();

    setTimeout(() => {{
        if (moleObj.element) moleObj.element.remove();
    }}, 420);

    activeMoles = activeMoles.filter(m => !m.popped);

    if (score >= targetScore) {{
        endGame(true);
        return;
    }}

    if (activeMoles.length === 0) {{
        clearInterval(timer);
        nextRoundDelay(650);
    }}
}}

function checkSpeech(transcript) {{
    if (!gameStarted || roundLocked) return;

    recognizedBox.innerText = "🗣️ 인식: " + transcript;

    for (let m of activeMoles) {{
        if (similarityCheck(transcript, m.word)) {{
            popMole(m);
            return;
        }}
    }}
}}

function startRecognition() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {{
        recognizedBox.innerText = "❌ 이 브라우저는 음성 인식을 지원하지 않습니다. Chrome으로 접속해 주세요.";
        return false;
    }}

    recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onstart = function() {{
        recognizedBox.innerText = "🎧 마이크가 듣고 있습니다.";
    }};

    recognition.onresult = function(event) {{
        let transcript = "";

        for (let i = event.resultIndex; i < event.results.length; i++) {{
            transcript += event.results[i][0].transcript;
        }}

        checkSpeech(transcript);
    }};

    recognition.onerror = function(event) {{
        recognizedBox.innerText = "⚠️ 마이크 오류: " + event.error;
    }};

    recognition.onend = function() {{
        if (gameStarted) {{
            try {{
                recognition.start();
            }} catch(e) {{}}
        }}
    }};

    try {{
        recognition.start();
        return true;
    }} catch(e) {{
        recognizedBox.innerText = "⚠️ 마이크를 다시 시작해 주세요.";
        return false;
    }}
}}

function startGame() {{
    if (gameStarted) return;

    score = 0;
    lives = maxLives;
    usedWords = [];
    activeMoles = [];
    roundLocked = false;

    scoreBox.innerText = score;
    livesBox.innerText = lives;
    timeLeftBox.innerText = showTime;

    gameStarted = true;

    const ok = startRecognition();
    if (!ok) {{
        gameStarted = false;
        return;
    }}

    messageBox.innerText = "🎮 게임 시작! 튀어나온 단어를 말해 보세요!";
    nextRound();
}}

function resetGame() {{
    gameStarted = false;
    clearInterval(timer);
    clearMoles();

    if (recognition) {{
        try {{
            recognition.stop();
        }} catch(e) {{}}
    }}

    score = 0;
    lives = maxLives;
    usedWords = [];
    roundLocked = false;

    scoreBox.innerText = score;
    livesBox.innerText = lives;
    timeLeftBox.innerText = showTime;
    messageBox.innerText = "게임 시작을 누르면 두더지 단어가 튀어나옵니다!";
    recognizedBox.innerText = "마이크 권한을 허용하고, 보이는 단어 중 하나를 말해 보세요.";
}}

function endGame(success) {{
    gameStarted = false;
    clearInterval(timer);
    clearMoles();

    if (recognition) {{
        try {{
            recognition.stop();
        }} catch(e) {{}}
    }}

    if (success) {{
        messageBox.innerText = "🎉 목표 점수 달성! 훌륭합니다!";
        recognizedBox.innerText = "최종 점수: " + score + "점";
    }} else {{
        messageBox.innerText = "💥 Game Over! 다시 도전해 봅시다.";
        recognizedBox.innerText = "최종 점수: " + score + "점";
    }}
}}
</script>
</body>
</html>
"""

components.html(game_html, height=700)
