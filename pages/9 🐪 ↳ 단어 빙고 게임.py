import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Speaking Falling Words",
    page_icon="💥",
    layout="wide"
)

# =========================
# 단어 데이터
# =========================
word_groups = {
    "🌱 사람·학교·동작": [
        "person", "man", "woman", "child", "baby", "boy", "girl", "friend", "family", "parent",
        "father", "mother", "brother", "sister", "son", "daughter", "teacher", "student", "classmate", "neighbor",
        "customer", "worker", "driver", "doctor", "nurse", "owner", "guest", "team", "member",
        "school", "class", "classroom", "lesson", "homework", "test", "exam", "quiz", "question", "answer",
        "book", "notebook", "paper", "pen", "pencil", "desk", "chair", "board", "page", "word",
        "sentence", "story", "language", "English", "Korean", "grade", "score", "rule", "practice", "study",
        "go", "come", "walk", "run", "sit", "stand", "stop", "start", "open", "close",
        "make", "do", "have", "get", "take", "give", "put", "bring", "use", "find",
        "keep", "leave", "move", "turn", "wait", "help", "try", "need", "want", "like",
    ],

    "💖 감정·상태": [
        "happy", "sad", "angry", "tired", "hungry", "thirsty", "excited", "bored", "afraid", "worried",
        "proud", "kind", "nice", "brave", "honest", "friendly", "quiet", "shy", "smart", "strong",
        "weak", "careful", "lazy", "busy", "ready", "sorry", "thankful", "lonely", "nervous", "calm",
        "good", "bad", "big", "small", "long", "short", "new", "old", "young", "high",
        "low", "fast", "slow", "easy", "hard", "right", "wrong", "same", "different", "important",
        "beautiful", "clean", "dirty", "full", "empty", "free", "safe", "dangerous", "true", "false",
    ],

    "🍎 음식·장소·이동": [
        "food", "rice", "bread", "water", "milk", "juice", "coffee", "tea", "apple", "banana",
        "egg", "meat", "fish", "chicken", "vegetable", "fruit", "breakfast", "lunch", "dinner", "snack",
        "healthy", "sick", "pain", "headache", "medicine", "hospital", "exercise", "sleep", "rest", "wash",
        "home", "house", "room", "kitchen", "bathroom", "door", "window", "city", "town", "country",
        "street", "road", "park", "store", "market", "station", "bus", "car", "bike", "train",
        "plane", "ship", "map", "place", "here", "there", "left", "right", "near", "far",
    ],

    "🌤️ 자연·동물": [
        "sun", "moon", "star", "sky", "cloud", "rain", "snow", "wind", "weather", "air",
        "water", "fire", "tree", "flower", "grass", "mountain", "river", "sea", "beach", "forest",
        "earth", "ground", "rock", "hill", "lake", "island", "cold", "hot", "warm", "cool",
        "dog", "cat", "bird", "fish", "horse", "cow", "pig", "sheep", "goat", "chicken",
        "duck", "rabbit", "mouse", "monkey", "lion", "tiger", "bear", "wolf", "fox", "deer",
        "elephant", "giraffe", "zebra", "snake", "frog", "turtle", "whale", "dolphin", "shark", "penguin",
    ],

    "⏰ 시간·물건·생각": [
        "time", "day", "week", "month", "year", "today", "tomorrow", "yesterday", "morning", "afternoon",
        "evening", "night", "hour", "minute", "second", "early", "late", "now", "before", "after",
        "first", "last", "one", "two", "three", "four", "five", "many", "much", "few",
        "thing", "bag", "box", "cup", "bottle", "phone", "computer", "camera", "key", "money",
        "card", "ticket", "clothes", "shirt", "pants", "shoes", "hat", "watch", "table", "bed",
        "light", "picture", "music", "game", "ball", "tool", "knife", "spoon", "fork", "plate",
        "think", "know", "understand", "remember", "forget", "say", "tell", "speak", "talk", "ask",
        "answer", "call", "listen", "hear", "read", "write", "learn", "teach", "mean", "feel",
        "believe", "hope", "choose", "decide", "explain", "show", "share", "agree", "worry", "thank",
    ],
}

# =========================
# 화면 제목
# =========================
st.markdown("## 💥 Speaking Falling Words")
st.caption("위에서 내려오는 단어를 폰으로 말하면 단어가 펑! 터집니다.")

col1, col2, col3 = st.columns(3)

with col1:
    selected_group = st.selectbox("단어 묶음 선택", list(word_groups.keys()))

with col2:
    speed = st.selectbox(
        "단어 내려오는 속도",
        ["느리게", "보통", "빠르게"],
        index=1
    )

with col3:
    spawn_speed = st.selectbox(
        "단어 나오는 간격",
        ["천천히", "보통", "많이"],
        index=1
    )

words = word_groups[selected_group]

speed_map = {
    "느리게": 10,
    "보통": 8,
    "빠르게": 6
}

spawn_map = {
    "천천히": 2200,
    "보통": 1600,
    "많이": 1000
}

fall_seconds = speed_map[speed]
spawn_interval = spawn_map[spawn_speed]

words_json = json.dumps(words)

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
        padding: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(180deg, #fdf2f8 0%, #eff6ff 50%, #f0fdf4 100%);
    }}

    .game-wrap {{
        width: 100%;
        height: 760px;
        border-radius: 28px;
        overflow: hidden;
        position: relative;
        background: linear-gradient(180deg, #dbeafe 0%, #fce7f3 55%, #fff7ed 100%);
        border: 4px solid #f9a8d4;
        box-shadow: 0 12px 30px rgba(0,0,0,0.12);
    }}

    .top-panel {{
        position: absolute;
        top: 14px;
        left: 14px;
        right: 14px;
        z-index: 20;
        display: flex;
        gap: 10px;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
    }}

    .score-box {{
        background: rgba(255,255,255,0.92);
        border-radius: 999px;
        padding: 10px 16px;
        font-weight: 900;
        font-size: 16px;
        color: #1e293b;
        border: 2px solid #e0e7ff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }}

    .btn {{
        border: none;
        border-radius: 999px;
        padding: 12px 18px;
        font-size: 16px;
        font-weight: 900;
        color: white;
        cursor: pointer;
        box-shadow: 0 5px 14px rgba(0,0,0,0.15);
    }}

    .start-btn {{
        background: linear-gradient(135deg, #ec4899, #8b5cf6);
    }}

    .stop-btn {{
        background: linear-gradient(135deg, #64748b, #334155);
    }}

    .reset-btn {{
        background: linear-gradient(135deg, #f97316, #ef4444);
    }}

    .guide {{
        position: absolute;
        top: 84px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10;
        background: rgba(255,255,255,0.9);
        border-radius: 24px;
        padding: 12px 22px;
        font-size: 18px;
        font-weight: 900;
        color: #be185d;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }}

    .recognized {{
        position: absolute;
        bottom: 16px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 20;
        width: 86%;
        background: rgba(255,255,255,0.94);
        border-radius: 22px;
        padding: 14px 16px;
        text-align: center;
        font-size: 17px;
        font-weight: 900;
        color: #334155;
        border: 2px solid #bfdbfe;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}

    .word {{
        position: absolute;
        top: -70px;
        padding: 12px 22px;
        border-radius: 999px;
        background: white;
        color: #be185d;
        font-size: 28px;
        font-weight: 1000;
        border: 3px solid #f9a8d4;
        box-shadow: 0 7px 18px rgba(0,0,0,0.15);
        animation-name: fall;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
        z-index: 5;
        white-space: nowrap;
    }}

    @keyframes fall {{
        from {{
            transform: translateY(0);
        }}
        to {{
            transform: translateY(860px);
        }}
    }}

    .pop {{
        animation: pop 0.45s ease-out forwards !important;
        background: linear-gradient(135deg, #fef3c7, #fecaca, #ddd6fe);
        border: 4px solid #ef4444;
        color: #dc2626;
        z-index: 30;
    }}

    @keyframes pop {{
        0% {{
            transform: scale(1);
            opacity: 1;
        }}
        45% {{
            transform: scale(1.8) rotate(8deg);
            opacity: 1;
        }}
        100% {{
            transform: scale(0);
            opacity: 0;
        }}
    }}

    .boom {{
        position: absolute;
        font-size: 42px;
        font-weight: 1000;
        color: #dc2626;
        animation: boom 0.65s ease-out forwards;
        z-index: 40;
        pointer-events: none;
    }}

    @keyframes boom {{
        0% {{
            transform: scale(0.4);
            opacity: 0;
        }}
        40% {{
            transform: scale(1.4);
            opacity: 1;
        }}
        100% {{
            transform: scale(2.1);
            opacity: 0;
        }}
    }}

    .mobile-note {{
        position: absolute;
        bottom: 72px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 20;
        background: rgba(255,247,237,0.95);
        color: #9a3412;
        border: 2px solid #fdba74;
        border-radius: 18px;
        padding: 10px 14px;
        font-size: 14px;
        font-weight: 800;
        text-align: center;
        width: 82%;
    }}
</style>
</head>

<body>

<div class="game-wrap" id="game">
    <div class="top-panel">
        <div class="score-box">⭐ 점수: <span id="score">0</span></div>
        <div class="score-box">💥 터뜨린 단어: <span id="hit">0</span></div>
        <div class="score-box">😅 놓친 단어: <span id="miss">0</span></div>

        <button class="btn start-btn" onclick="startGame()">🎙️ 시작</button>
        <button class="btn stop-btn" onclick="stopGame()">⏸️ 멈춤</button>
        <button class="btn reset-btn" onclick="resetGame()">🔄 다시</button>
    </div>

    <div class="guide" id="guide">
        🎤 시작을 누르고, 내려오는 영어 단어를 말하세요!
    </div>

    <div class="mobile-note">
        📱 폰에서는 마이크 권한을 허용해야 합니다. Chrome에서 가장 잘 작동합니다.
    </div>

    <div class="recognized" id="recognized">
        🗣️ 인식된 말: 아직 없음
    </div>
</div>

<script>
const WORDS = {words_json};
const FALL_SECONDS = {fall_seconds};
const SPAWN_INTERVAL = {spawn_interval};

let game = document.getElementById("game");
let scoreEl = document.getElementById("score");
let hitEl = document.getElementById("hit");
let missEl = document.getElementById("miss");
let recognizedEl = document.getElementById("recognized");
let guideEl = document.getElementById("guide");

let score = 0;
let hit = 0;
let miss = 0;

let running = false;
let spawnTimer = null;
let recognition = null;
let wordId = 0;

function randomWord() {{
    return WORDS[Math.floor(Math.random() * WORDS.length)];
}}

function normalize(text) {{
    return text
        .toLowerCase()
        .replace(/[^a-z\\s]/g, "")
        .trim();
}}

function createWord() {{
    if (!running) return;

    const wordText = randomWord();
    const word = document.createElement("div");

    word.className = "word";
    word.innerText = wordText;
    word.dataset.word = normalize(wordText);
    word.dataset.id = wordId++;

    const left = Math.random() * 78 + 4;
    word.style.left = left + "%";
    word.style.animationDuration = FALL_SECONDS + "s";

    word.addEventListener("animationend", function() {{
        if (word.parentNode && !word.classList.contains("pop")) {{
            miss += 1;
            missEl.innerText = miss;
            word.remove();
        }}
    }});

    game.appendChild(word);
}}

function popWord(wordElement) {{
    if (!wordElement || wordElement.classList.contains("pop")) return;

    const rect = wordElement.getBoundingClientRect();
    const gameRect = game.getBoundingClientRect();

    const boom = document.createElement("div");
    boom.className = "boom";
    boom.innerText = "💥";
    boom.style.left = (rect.left - gameRect.left + rect.width / 2 - 20) + "px";
    boom.style.top = (rect.top - gameRect.top - 10) + "px";

    game.appendChild(boom);

    setTimeout(() => {{
        if (boom.parentNode) boom.remove();
    }}, 650);

    wordElement.classList.add("pop");

    score += 10;
    hit += 1;

    scoreEl.innerText = score;
    hitEl.innerText = hit;

    setTimeout(() => {{
        if (wordElement.parentNode) wordElement.remove();
    }}, 450);
}}

function checkSpeech(transcript) {{
    const cleanText = normalize(transcript);
    const spokenWords = cleanText.split(/\\s+/);

    recognizedEl.innerText = "🗣️ 인식된 말: " + cleanText;

    const fallingWords = document.querySelectorAll(".word:not(.pop)");

    for (let wordElement of fallingWords) {{
        const target = wordElement.dataset.word;

        if (cleanText === target || spokenWords.includes(target)) {{
            popWord(wordElement);
            guideEl.innerText = "✅ 정답! " + target + " 펑!";
            return;
        }}
    }}

    guideEl.innerText = "🤔 인식은 됐지만, 내려오는 단어와 맞지 않아요.";
}}

function startSpeechRecognition() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {{
        guideEl.innerText = "이 브라우저는 음성 인식을 지원하지 않습니다. Chrome을 사용해 주세요.";
        return;
    }}

    recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = true;
    recognition.interimResults = false;

    recognition.onresult = function(event) {{
        for (let i = event.resultIndex; i < event.results.length; i++) {{
            if (event.results[i].isFinal) {{
                const transcript = event.results[i][0].transcript;
                checkSpeech(transcript);
            }}
        }}
    }};

    recognition.onerror = function(event) {{
        guideEl.innerText = "🎤 마이크 인식 오류가 났습니다. 다시 시작을 눌러 주세요.";
    }};

    recognition.onend = function() {{
        if (running) {{
            try {{
                recognition.start();
            }} catch (e) {{}}
        }}
    }};

    try {{
        recognition.start();
    }} catch (e) {{}}
}}

function startGame() {{
    if (running) return;

    running = true;
    guideEl.innerText = "🎤 내려오는 단어를 크게 말하세요!";

    createWord();
    spawnTimer = setInterval(createWord, SPAWN_INTERVAL);

    startSpeechRecognition();
}}

function stopGame() {{
    running = false;
    guideEl.innerText = "⏸️ 게임이 멈췄습니다.";

    if (spawnTimer) {{
        clearInterval(spawnTimer);
        spawnTimer = null;
    }}

    if (recognition) {{
        try {{
            recognition.stop();
        }} catch (e) {{}}
    }}
}}

function resetGame() {{
    stopGame();

    score = 0;
    hit = 0;
    miss = 0;

    scoreEl.innerText = score;
    hitEl.innerText = hit;
    missEl.innerText = miss;

    const words = document.querySelectorAll(".word, .boom");
    words.forEach(w => w.remove());

    recognizedEl.innerText = "🗣️ 인식된 말: 아직 없음";
    guideEl.innerText = "🎤 시작을 누르고, 내려오는 영어 단어를 말하세요!";
}}
</script>

</body>
</html>
"""

components.html(html_code, height=800, scrolling=False)
