import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Phonics Speaking Mole Game",
    page_icon="🐹",
    layout="wide"
)

# =========================
# 파닉스 단어 세트
# =========================
PHONICS_WORD_SETS = {
    "짧은 모음": [
        "cat", "bat", "map", "hat", "bed", "red", "pen", "sit", "pig", "fish",
        "hot", "dog", "box", "cup", "sun", "run", "bus", "bug"
    ],
    "긴 모음": [
        "cake", "name", "rain", "day", "tree", "see", "bike", "kite",
        "home", "boat", "cube", "music"
    ],
    "자음 이어 읽기": [
        "black", "brown", "clock", "crab", "frog", "green", "plane",
        "snake", "spoon", "star", "tree", "smile"
    ],
    "두 글자 한 소리": [
        "chair", "ship", "three", "this", "phone", "duck", "whale",
        "chick", "shell", "thin"
    ],
    "모음 두 글자 소리": [
        "rain", "day", "see", "eat", "boat", "snow", "cow", "house",
        "coin", "boy"
    ],
    "자음 예외": [
        "city", "cent", "cycle", "gem", "giant", "gym", "knee",
        "write", "lamb", "exam"
    ]
}

# =========================
# 상단 화면
# =========================
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #fff1f2 0%, #eef2ff 50%, #ecfeff 100%);
        border-radius: 30px;
        padding: 32px;
        margin-bottom: 24px;
        text-align: center;
        border: 1px solid #fbcfe8;
        box-shadow: 0 10px 24px rgba(0,0,0,0.08);
    ">
        <div style="font-size: 42px; font-weight: 900; color: #334155;">
            🐹🔨 파닉스 말하기 두더지 게임
        </div>
        <div style="font-size: 18px; color: #64748b; line-height: 1.8; margin-top: 10px;">
            단어 두더지가 튀어나오면, 그 단어를 영어로 말해 보세요.<br>
            발음이 인식되면 두더지가 사라지고 점수가 올라갑니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

selected_set = st.selectbox(
    "연습할 파닉스 영역을 선택하세요",
    list(PHONICS_WORD_SETS.keys())
)

words = PHONICS_WORD_SETS[selected_set]
words_js_array = "[" + ",".join([f'"{w}"' for w in words]) + "]"

# =========================
# HTML / JS 게임
# =========================
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: #fffdfb;
    }}

    .game-wrap {{
        max-width: 1100px;
        margin: 0 auto;
        padding: 20px;
    }}

    .control-box {{
        background: linear-gradient(135deg, #fff7ed 0%, #fffbeb 100%);
        border: 1px solid #fed7aa;
        border-radius: 24px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }}

    .title {{
        font-size: 28px;
        font-weight: 900;
        color: #c2410c;
        margin-bottom: 10px;
    }}

    .desc {{
        font-size: 16px;
        color: #7c2d12;
        line-height: 1.7;
        margin-bottom: 15px;
    }}

    .btn {{
        border: none;
        border-radius: 999px;
        padding: 13px 24px;
        margin: 5px;
        font-size: 17px;
        font-weight: 900;
        cursor: pointer;
        background: #f97316;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }}

    .btn:hover {{
        background: #ea580c;
    }}

    .btn-stop {{
        background: #64748b;
    }}

    .btn-stop:hover {{
        background: #475569;
    }}

    .status-box {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 14px;
        margin-bottom: 20px;
    }}

    .status-card {{
        background: white;
        border-radius: 20px;
        padding: 16px;
        text-align: center;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}

    .status-label {{
        font-size: 14px;
        color: #64748b;
        font-weight: 800;
        margin-bottom: 6px;
    }}

    .status-value {{
        font-size: 24px;
        color: #111827;
        font-weight: 900;
    }}

    .board {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 22px;
        margin-top: 20px;
    }}

    .hole {{
        position: relative;
        height: 190px;
        background: linear-gradient(180deg, #d9f99d 0%, #86efac 55%, #4ade80 100%);
        border-radius: 28px;
        overflow: hidden;
        box-shadow: inset 0 -12px 0 rgba(22, 101, 52, 0.18), 0 8px 18px rgba(0,0,0,0.08);
        border: 2px solid #bbf7d0;
    }}

    .ground-hole {{
        position: absolute;
        bottom: 18px;
        left: 50%;
        transform: translateX(-50%);
        width: 72%;
        height: 42px;
        background: #78350f;
        border-radius: 50%;
        box-shadow: inset 0 8px 15px rgba(0,0,0,0.45);
        z-index: 1;
    }}

    .mole {{
        position: absolute;
        left: 50%;
        bottom: -120px;
        transform: translateX(-50%);
        width: 150px;
        height: 135px;
        background: linear-gradient(135deg, #92400e 0%, #b45309 100%);
        border-radius: 50% 50% 35% 35%;
        z-index: 2;
        transition: bottom 0.35s ease;
        text-align: center;
        color: white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.18);
    }}

    .mole.show {{
        bottom: 34px;
        animation: pop 0.45s ease;
    }}

    @keyframes pop {{
        0% {{ transform: translateX(-50%) scale(0.75); }}
        60% {{ transform: translateX(-50%) scale(1.08); }}
        100% {{ transform: translateX(-50%) scale(1); }}
    }}

    .mole.hit {{
        animation: hit 0.45s ease forwards;
    }}

    @keyframes hit {{
        0% {{ transform: translateX(-50%) scale(1); opacity: 1; }}
        50% {{ transform: translateX(-50%) scale(1.2) rotate(8deg); opacity: 0.8; }}
        100% {{ transform: translateX(-50%) scale(0.3); opacity: 0; bottom: -130px; }}
    }}

    .face {{
        font-size: 34px;
        margin-top: 12px;
    }}

    .word {{
        font-size: 25px;
        font-weight: 900;
        margin-top: 4px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.25);
    }}

    .heard-box {{
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1px solid #bfdbfe;
        border-radius: 22px;
        padding: 18px;
        margin-top: 22px;
        text-align: center;
    }}

    .heard-title {{
        font-size: 16px;
        font-weight: 900;
        color: #1d4ed8;
        margin-bottom: 8px;
    }}

    .heard-text {{
        font-size: 26px;
        font-weight: 900;
        color: #111827;
    }}

    .message {{
        margin-top: 18px;
        padding: 16px;
        border-radius: 18px;
        font-size: 22px;
        font-weight: 900;
        text-align: center;
    }}

    .good {{
        background: #dcfce7;
        color: #166534;
    }}

    .bad {{
        background: #fee2e2;
        color: #991b1b;
    }}

    .tip {{
        margin-top: 20px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 18px;
        color: #475569;
        line-height: 1.7;
        font-size: 15px;
    }}

    @media (max-width: 800px) {{
        .board {{
            grid-template-columns: repeat(2, 1fr);
        }}
        .status-box {{
            grid-template-columns: 1fr;
        }}
    }}
</style>
</head>

<body>
<div class="game-wrap">

    <div class="control-box">
        <div class="title">🐹 단어가 튀어나오면 말해서 잡기!</div>
        <div class="desc">
            마이크 시작을 누른 뒤, 화면에 나온 단어를 영어로 말하세요.<br>
            발음이 맞게 인식되면 두더지가 사라지고 점수가 올라갑니다.
        </div>
        <button class="btn" onclick="startGame()">🎙️ 마이크 시작 / 게임 시작</button>
        <button class="btn btn-stop" onclick="stopGame()">⏹️ 정지</button>
        <button class="btn btn-stop" onclick="resetGame()">🔄 다시 시작</button>
    </div>

    <div class="status-box">
        <div class="status-card">
            <div class="status-label">점수</div>
            <div class="status-value" id="score">0</div>
        </div>
        <div class="status-card">
            <div class="status-label">현재 목표 단어</div>
            <div class="status-value" id="targetWord">-</div>
        </div>
        <div class="status-card">
            <div class="status-label">마이크 상태</div>
            <div class="status-value" id="micStatus">대기</div>
        </div>
    </div>

    <div class="board">
        <div class="hole"><div class="mole" id="mole0"><div class="face">🐹</div><div class="word"></div></div><div class="ground-hole"></div></div>
        <div class="hole"><div class="mole" id="mole1"><div class="face">🐹</div><div class="word"></div></div><div class="ground-hole"></div></div>
        <div class="hole"><div class="mole" id="mole2"><div class="face">🐹</div><div class="word"></div></div><div class="ground-hole"></div></div>
        <div class="hole"><div class="mole" id="mole3"><div class="face">🐹</div><div class="word"></div></div><div class="ground-hole"></div></div>
        <div class="hole"><div class="mole" id="mole4"><div class="face">🐹</div><div class="word"></div></div><div class="ground-hole"></div></div>
        <div class="hole"><div class="mole" id="mole5"><div class="face">🐹</div><div class="word"></div></div><div class="ground-hole"></div></div>
    </div>

    <div class="heard-box">
        <div class="heard-title">🎧 인식된 발음</div>
        <div class="heard-text" id="heardText">아직 인식된 말이 없습니다.</div>
    </div>

    <div id="message"></div>

    <div class="tip">
        💡 <b>사용 팁</b><br>
        • Chrome 브라우저에서 가장 잘 작동합니다.<br>
        • 처음 실행할 때 마이크 허용을 눌러야 합니다.<br>
        • 조용한 환경에서 학생이 단어를 또박또박 말하면 인식률이 좋아집니다.<br>
        • 휴대폰에서는 주소창 왼쪽 자물쇠 또는 사이트 설정에서 마이크 허용을 확인하세요.
    </div>

</div>

<script>
const WORDS = {words_js_array};

let score = 0;
let currentTarget = "";
let currentMoleIndex = -1;
let gameTimer = null;
let recognition = null;
let isRunning = false;

const moleCount = 6;

function randomChoice(arr) {{
    return arr[Math.floor(Math.random() * arr.length)];
}}

function clearMoles() {{
    for (let i = 0; i < moleCount; i++) {{
        const mole = document.getElementById("mole" + i);
        mole.classList.remove("show");
        mole.classList.remove("hit");
        mole.querySelector(".word").innerText = "";
    }}
}}

function popMole() {{
    clearMoles();

    currentTarget = randomChoice(WORDS);
    currentMoleIndex = Math.floor(Math.random() * moleCount);

    const mole = document.getElementById("mole" + currentMoleIndex);
    mole.querySelector(".word").innerText = currentTarget;
    mole.classList.add("show");

    document.getElementById("targetWord").innerText = currentTarget;

    speakWord(currentTarget);
}}

function speakWord(word) {{
    try {{
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = "en-US";
        utterance.rate = 0.85;
        speechSynthesis.speak(utterance);
    }} catch (e) {{}}
}}

function normalizeText(text) {{
    return text
        .toLowerCase()
        .replace(/[^a-z ]/g, "")
        .trim();
}}

function checkAnswer(spokenText) {{
    const heard = normalizeText(spokenText);
    const target = normalizeText(currentTarget);

    document.getElementById("heardText").innerText = spokenText;

    if (!target) return;

    const words = heard.split(" ");

    if (heard === target || words.includes(target)) {{
        hitMole();
    }} else {{
        showMessage("😅 '" + spokenText + "'로 들렸어요. 다시 말해 보세요!", "bad");
    }}
}}

function hitMole() {{
    const mole = document.getElementById("mole" + currentMoleIndex);
    mole.classList.remove("show");
    mole.classList.add("hit");

    score += 1;
    document.getElementById("score").innerText = score;

    showMessage("🎉 정답! '" + currentTarget + "' 두더지를 잡았어요!", "good");

    setTimeout(() => {{
        if (isRunning) {{
            popMole();
        }}
    }}, 900);
}}

function showMessage(text, type) {{
    const message = document.getElementById("message");
    message.innerHTML = '<div class="message ' + type + '">' + text + '</div>';
}}

function startGame() {{
    if (isRunning) return;

    isRunning = true;
    document.getElementById("micStatus").innerText = "듣는 중";

    popMole();
    startRecognition();

    gameTimer = setInterval(() => {{
        if (isRunning) {{
            popMole();
        }}
    }}, 5500);
}}

function stopGame() {{
    isRunning = false;
    document.getElementById("micStatus").innerText = "정지";
    clearInterval(gameTimer);

    if (recognition) {{
        recognition.stop();
    }}
}}

function resetGame() {{
    stopGame();
    score = 0;
    currentTarget = "";
    currentMoleIndex = -1;

    document.getElementById("score").innerText = "0";
    document.getElementById("targetWord").innerText = "-";
    document.getElementById("heardText").innerText = "아직 인식된 말이 없습니다.";
    document.getElementById("message").innerHTML = "";
    clearMoles();
}}

function startRecognition() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {{
        document.getElementById("micStatus").innerText = "지원 안 됨";
        showMessage("이 브라우저는 음성 인식을 지원하지 않습니다. Chrome을 사용해 주세요.", "bad");
        return;
    }}

    recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = true;
    recognition.interimResults = false;

    recognition.onstart = function() {{
        document.getElementById("micStatus").innerText = "듣는 중";
    }};

    recognition.onresult = function(event) {{
        const last = event.results.length - 1;
        const spokenText = event.results[last][0].transcript;
        checkAnswer(spokenText);
    }};

    recognition.onerror = function(event) {{
        document.getElementById("micStatus").innerText = "오류";
        showMessage("마이크 오류가 났습니다: " + event.error, "bad");
    }};

    recognition.onend = function() {{
        if (isRunning) {{
            try {{
                recognition.start();
            }} catch (e) {{}}
        }}
    }};

    try {{
        recognition.start();
    }} catch (e) {{}}
}}
</script>
</body>
</html>
"""

components.html(html_code, height=950, scrolling=True)
