import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="생존 문장 말하기 훈련",
    page_icon="🎙️",
    layout="wide"
)

# =========================================================
# 데이터
# =========================================================
PRACTICE_ITEMS = [{'cat': '🙋 내 상태 말하기', 'ko': '나는 배고파.', 'blank': 'I am ______.', 'answer': 'I am hungry.', 'hint': 'hungry', 'emoji': '🍽️'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 목말라.', 'blank': 'I am ______.', 'answer': 'I am thirsty.', 'hint': 'thirsty', 'emoji': '💧'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 피곤해.', 'blank': 'I am ______.', 'answer': 'I am tired.', 'hint': 'tired', 'emoji': '😴'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 아파.', 'blank': 'I am ______.', 'answer': 'I am sick.', 'hint': 'sick', 'emoji': '🤒'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 괜찮아.', 'blank': 'I am ______.', 'answer': 'I am okay.', 'hint': 'okay', 'emoji': '🙂'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 추워.', 'blank': 'I am ______.', 'answer': 'I am cold.', 'hint': 'cold', 'emoji': '🥶'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 걱정돼.', 'blank': 'I am ______.', 'answer': 'I am worried.', 'hint': 'worried', 'emoji': '😟'}, {'cat': '🙋 내 상태 말하기', 'ko': '나는 무서워.', 'blank': 'I am ______.', 'answer': 'I am scared.', 'hint': 'scared', 'emoji': '😨'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 물이 필요해.', 'blank': 'I need ______.', 'answer': 'I need water.', 'hint': 'water', 'emoji': '💧'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 음식이 필요해.', 'blank': 'I need ______.', 'answer': 'I need food.', 'hint': 'food', 'emoji': '🍽️'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 도움이 필요해.', 'blank': 'I need ______.', 'answer': 'I need help.', 'hint': 'help', 'emoji': '🆘'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 약이 필요해.', 'blank': 'I need ______.', 'answer': 'I need medicine.', 'hint': 'medicine', 'emoji': '💊'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 병원이 필요해.', 'blank': 'I need a ______.', 'answer': 'I need a hospital.', 'hint': 'hospital', 'emoji': '🏥'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 택시가 필요해.', 'blank': 'I need a ______.', 'answer': 'I need a taxi.', 'hint': 'taxi', 'emoji': '🚕'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 표가 필요해.', 'blank': 'I need a ______.', 'answer': 'I need a ticket.', 'hint': 'ticket', 'emoji': '🎫'}, {'cat': '🆘 필요한 것 말하기', 'ko': '나는 열쇠가 필요해.', 'blank': 'I need a ______.', 'answer': 'I need a key.', 'hint': 'key', 'emoji': '🔑'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 음식을 원해.', 'blank': 'I want ______.', 'answer': 'I want food.', 'hint': 'food', 'emoji': '🍽️'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 물을 원해.', 'blank': 'I want ______.', 'answer': 'I want water.', 'hint': 'water', 'emoji': '💧'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 밥을 원해.', 'blank': 'I want ______.', 'answer': 'I want rice.', 'hint': 'rice', 'emoji': '🍚'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 빵을 원해.', 'blank': 'I want ______.', 'answer': 'I want bread.', 'hint': 'bread', 'emoji': '🍞'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 우유를 원해.', 'blank': 'I want ______.', 'answer': 'I want milk.', 'hint': 'milk', 'emoji': '🥛'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 주스를 원해.', 'blank': 'I want ______.', 'answer': 'I want juice.', 'hint': 'juice', 'emoji': '🧃'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 커피를 원해.', 'blank': 'I want ______.', 'answer': 'I want coffee.', 'hint': 'coffee', 'emoji': '☕'}, {'cat': '💭 원하는 것 말하기', 'ko': '나는 간식을 원해.', 'blank': 'I want a ______.', 'answer': 'I want a snack.', 'hint': 'snack', 'emoji': '🍪'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 먹고 있어.', 'blank': 'I am ______.', 'answer': 'I am eating.', 'hint': 'eating', 'emoji': '🍽️'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 마시고 있어.', 'blank': 'I am ______.', 'answer': 'I am drinking.', 'hint': 'drinking', 'emoji': '🥤'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 기다리고 있어.', 'blank': 'I am ______.', 'answer': 'I am waiting.', 'hint': 'waiting', 'emoji': '⏳'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 공부하고 있어.', 'blank': 'I am ______.', 'answer': 'I am studying.', 'hint': 'studying', 'emoji': '📚'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 읽고 있어.', 'blank': 'I am ______.', 'answer': 'I am reading.', 'hint': 'reading', 'emoji': '📖'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 쓰고 있어.', 'blank': 'I am ______.', 'answer': 'I am writing.', 'hint': 'writing', 'emoji': '✏️'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 걷고 있어.', 'blank': 'I am ______.', 'answer': 'I am walking.', 'hint': 'walking', 'emoji': '🚶'}, {'cat': '🏃 지금 하는 일 말하기', 'ko': '나는 듣고 있어.', 'blank': 'I am ______.', 'answer': 'I am listening.', 'hint': 'listening', 'emoji': '👂'}, {'cat': '🚀 앞으로 할 일 말하기', 'ko': '나는 집에 갈 거야.', 'blank': 'I will ______ home.', 'answer': 'I will go home.', 'hint': 'go', 'emoji': '🏠'}, {'cat': '🚀 앞으로 할 일 말하기', 'ko': '나는 기다릴 거야.', 'blank': 'I will ______.', 'answer': 'I will wait.', 'hint': 'wait', 'emoji': '⏳'}, {'cat': '🚀 앞으로 할 일 말하기', 'ko': '나는 너를 도와줄 거야.', 'blank': 'I will ______ you.', 'answer': 'I will help you.', 'hint': 'help', 'emoji': '🤝'}, {'cat': '🚀 앞으로 할 일 말하기', 'ko': '나는 영어를 공부할 거야.', 'blank': 'I will ______ English.', 'answer': 'I will study English.', 'hint': 'study', 'emoji': '📚'}, {'cat': '🚀 앞으로 할 일 말하기', 'ko': '나는 점심을 먹을 거야.', 'blank': 'I will ______ lunch.', 'answer': 'I will eat lunch.', 'hint': 'eat', 'emoji': '🍱'}, {'cat': '🚀 앞으로 할 일 말하기', 'ko': '나는 물을 마실 거야.', 'blank': 'I will ______ water.', 'answer': 'I will drink water.', 'hint': 'drink', 'emoji': '💧'}, {'cat': '❌ 아니라고 말하기', 'ko': '나는 아프지 않아.', 'blank': 'I am not ______.', 'answer': 'I am not sick.', 'hint': 'sick', 'emoji': '🙂'}, {'cat': '❌ 아니라고 말하기', 'ko': '나는 배고프지 않아.', 'blank': 'I am not ______.', 'answer': 'I am not hungry.', 'hint': 'hungry', 'emoji': '🙅🍽️'}, {'cat': '❌ 아니라고 말하기', 'ko': '나는 괜찮지 않아.', 'blank': 'I am not ______.', 'answer': 'I am not okay.', 'hint': 'okay', 'emoji': '😟'}, {'cat': '❌ 아니라고 말하기', 'ko': '나는 몰라.', 'blank': 'I do not ______.', 'answer': 'I do not know.', 'hint': 'know', 'emoji': '🤷'}, {'cat': '❌ 아니라고 말하기', 'ko': '나는 이해하지 못해.', 'blank': 'I do not ______.', 'answer': 'I do not understand.', 'hint': 'understand', 'emoji': '❓'}, {'cat': '❌ 아니라고 말하기', 'ko': '나는 그것을 원하지 않아.', 'blank': 'I do not ______ it.', 'answer': 'I do not want it.', 'hint': 'want', 'emoji': '🙅'}, {'cat': '❓ 간단히 물어보기', 'ko': '괜찮니?', 'blank': 'Are you ______?', 'answer': 'Are you okay?', 'hint': 'okay', 'emoji': '🙂'}, {'cat': '❓ 간단히 물어보기', 'ko': '아프니?', 'blank': 'Are you ______?', 'answer': 'Are you sick?', 'hint': 'sick', 'emoji': '🤒'}, {'cat': '❓ 간단히 물어보기', 'ko': '배고프니?', 'blank': 'Are you ______?', 'answer': 'Are you hungry?', 'hint': 'hungry', 'emoji': '🍽️'}, {'cat': '❓ 간단히 물어보기', 'ko': '목마르니?', 'blank': 'Are you ______?', 'answer': 'Are you thirsty?', 'hint': 'thirsty', 'emoji': '💧'}, {'cat': '❓ 간단히 물어보기', 'ko': '도움이 필요하니?', 'blank': 'Do you need ______?', 'answer': 'Do you need help?', 'hint': 'help', 'emoji': '🆘'}, {'cat': '❓ 간단히 물어보기', 'ko': '물이 필요하니?', 'blank': 'Do you need ______?', 'answer': 'Do you need water?', 'hint': 'water', 'emoji': '💧'}, {'cat': '🕵️ 필요한 정보 묻기', 'ko': '화장실은 어디에 있나요?', 'blank': 'Where is the ______?', 'answer': 'Where is the bathroom?', 'hint': 'bathroom', 'emoji': '🚻'}, {'cat': '🕵️ 필요한 정보 묻기', 'ko': '병원은 어디에 있나요?', 'blank': 'Where is the ______?', 'answer': 'Where is the hospital?', 'hint': 'hospital', 'emoji': '🏥'}, {'cat': '🕵️ 필요한 정보 묻기', 'ko': '가게는 어디에 있나요?', 'blank': 'Where is the ______?', 'answer': 'Where is the store?', 'hint': 'store', 'emoji': '🏪'}, {'cat': '🕵️ 필요한 정보 묻기', 'ko': '역은 어디에 있나요?', 'blank': 'Where is the ______?', 'answer': 'Where is the station?', 'hint': 'station', 'emoji': '🚉'}, {'cat': '🕵️ 필요한 정보 묻기', 'ko': '지금 몇 시인가요?', 'blank': 'What ______ is it?', 'answer': 'What time is it?', 'hint': 'time', 'emoji': '⏰'}, {'cat': '🕵️ 필요한 정보 묻기', 'ko': '이름이 무엇인가요?', 'blank': 'What is your ______?', 'answer': 'What is your name?', 'hint': 'name', 'emoji': '🏷️'}]


# =========================================================
# 디자인
# =========================================================
st.markdown(
    """
    <style>
    .main-title-box {
        background: linear-gradient(135deg, #eff6ff 0%, #fff7ed 50%, #fdf2f8 100%);
        border: 1.5px solid #dbeafe;
        border-radius: 30px;
        padding: 28px 30px;
        margin-bottom: 22px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
    }

    .main-title-box h1 {
        margin: 0 0 10px 0;
        color: #0f172a;
        font-size: 38px;
        font-weight: 900;
    }

    .main-title-box p {
        margin: 0;
        color: #475569;
        font-size: 18px;
        line-height: 1.7;
        font-weight: 700;
    }

    .guide-box {
        background: white;
        border: 1.5px solid #e0f2fe;
        border-radius: 24px;
        padding: 18px 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.045);
        color: #334155;
        font-size: 17px;
        line-height: 1.7;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="main-title-box">
        <h1>🎙️ 생존 단어 160개로 문장 말하기</h1>
        <p>
            한국어 상황과 이모지를 보고, 빈칸에 들어갈 말을 떠올린 뒤 <b>문장 전체를 영어로 말해 보세요.</b><br>
            힌트는 정답 단어의 앞 두 글자만 보여 줍니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="guide-box">
        <b>활동 순서</b><br>
        1. 한국어 상황과 이모지를 봅니다. → 2. 영어 빈칸 문장을 봅니다. → 3. 필요하면 앞 두 글자 힌트를 봅니다.<br>
        4. 마이크 버튼을 누르고 <b>문장 전체</b>를 말합니다. → 5. 문장 전체가 맞게 인식되면 정답으로 인정됩니다.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 말하기 훈련 컴포넌트
# =========================================================
def speaking_practice_component(items):
    items_json = json.dumps(items, ensure_ascii=False)

    html = r"""
    <div id="speaking-app" style="
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #fff7ed 50%, #fdf2f8 100%);
        border: 1.5px solid #dbeafe;
        border-radius: 30px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    ">
        <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-bottom:18px;">
            <label style="font-weight:900; color:#334155;">문장 구조 선택</label>
            <select id="categorySelect" style="
                padding: 10px 14px;
                border-radius: 999px;
                border: 1.5px solid #bae6fd;
                font-size: 15px;
                font-weight: 800;
                color: #0f172a;
                background: white;
            "></select>

            <button id="randomBtn" style="
                border: 1.5px solid #c7d2fe;
                background: white;
                color: #3730a3;
                border-radius: 999px;
                padding: 10px 15px;
                font-weight: 900;
                cursor: pointer;
            ">🎲 랜덤</button>

            <button id="resetBtn" style="
                border: 1.5px solid #fed7aa;
                background: #fff7ed;
                color: #9a3412;
                border-radius: 999px;
                padding: 10px 15px;
                font-weight: 900;
                cursor: pointer;
            ">🔄 점수 초기화</button>
        </div>

        <div style="
            background:white;
            border-radius:26px;
            padding:24px;
            border:1.5px solid #e0f2fe;
            box-shadow:0 5px 16px rgba(0,0,0,0.055);
        ">
            <div style="display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; margin-bottom:14px;">
                <div id="categoryLabel" style="
                    display:inline-block;
                    background:#eef6ff;
                    color:#1d4ed8;
                    border-radius:999px;
                    padding:8px 14px;
                    font-size:15px;
                    font-weight:900;
                    border:1px solid #bfdbfe;
                "></div>

                <div id="scoreLabel" style="
                    display:inline-block;
                    background:#f0fdf4;
                    color:#166534;
                    border-radius:999px;
                    padding:8px 14px;
                    font-size:15px;
                    font-weight:900;
                    border:1px solid #bbf7d0;
                ">0 / 0</div>
            </div>

            <div style="
                font-size: 30px;
                font-weight: 900;
                color: #111827;
                line-height: 1.45;
                margin-bottom: 18px;
            " id="koPrompt">
                한국어 상황
            </div>

            <div style="
                background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
                border: 1.5px solid #dbeafe;
                border-radius: 22px;
                padding: 22px 20px;
                margin-bottom: 18px;
                font-size: 34px;
                font-weight: 900;
                color: #0f172a;
                line-height: 1.5;
            " id="blankSentence">
                I am ______.
            </div>

            <div id="hintBox" style="
                display:none;
                background:#fffbeb;
                border:1.5px solid #fde68a;
                color:#92400e;
                border-radius:18px;
                padding:14px 16px;
                margin-bottom:16px;
                font-size:22px;
                font-weight:900;
            "></div>

            <div id="answerBox" style="
                display:none;
                background:#ecfdf5;
                border:1.5px solid #bbf7d0;
                color:#166534;
                border-radius:18px;
                padding:14px 16px;
                margin-bottom:16px;
                font-size:22px;
                font-weight:900;
            "></div>

            <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-bottom:16px;">
                <button id="hintBtn" style="
                    border:1.5px solid #fde68a;
                    background:#fffbeb;
                    color:#92400e;
                    border-radius:999px;
                    padding:11px 16px;
                    font-weight:900;
                    cursor:pointer;
                ">💡 앞 두 글자 힌트</button>

                <button id="listenBtn" style="
                    border:1.5px solid #bfdbfe;
                    background:#eff6ff;
                    color:#1d4ed8;
                    border-radius:999px;
                    padding:11px 16px;
                    font-weight:900;
                    cursor:pointer;
                ">🔊 정답 듣기</button>

                <button id="answerBtn" style="
                    border:1.5px solid #bbf7d0;
                    background:#f0fdf4;
                    color:#166534;
                    border-radius:999px;
                    padding:11px 16px;
                    font-weight:900;
                    cursor:pointer;
                ">👀 정답 보기</button>

                <button id="micBtn" style="
                    border:1.5px solid #fecaca;
                    background:#fff1f2;
                    color:#be123c;
                    border-radius:999px;
                    padding:11px 18px;
                    font-weight:900;
                    cursor:pointer;
                    font-size:16px;
                ">🎙️ 말하기 시작</button>

                <button id="nextBtn" style="
                    border:1.5px solid #c7d2fe;
                    background:#eef2ff;
                    color:#3730a3;
                    border-radius:999px;
                    padding:11px 18px;
                    font-weight:900;
                    cursor:pointer;
                    font-size:16px;
                ">➡️ 다음 문제</button>
            </div>

            <div style="
                background:#f8fafc;
                border:1.5px solid #e2e8f0;
                border-radius:18px;
                padding:14px 16px;
                margin-bottom:14px;
                min-height:54px;
            ">
                <div style="font-size:13px; color:#64748b; font-weight:900; margin-bottom:5px;">인식된 문장</div>
                <div id="transcriptBox" style="font-size:22px; font-weight:900; color:#334155;">아직 말하지 않았습니다.</div>
            </div>

            <div id="resultBox" style="
                background:#f1f5f9;
                border:1.5px solid #e2e8f0;
                border-radius:18px;
                padding:14px 16px;
                font-size:20px;
                font-weight:900;
                color:#334155;
            ">
                마이크 버튼을 누르고 문장 전체를 말해 보세요. I'm, don't 같은 자연스러운 축약형은 괜찮습니다.
            </div>
        </div>

        <div style="
            margin-top:14px;
            color:#64748b;
            font-size:13px;
            line-height:1.6;
            font-weight:700;
        ">
            ※ Chrome 계열 브라우저에서 음성 인식이 가장 잘 작동합니다.<br>
            ※ 마이크 권한 요청이 나오면 허용을 눌러 주세요.
        </div>
    </div>

    <script>
    const ITEMS = __ITEMS_JSON__;

    let currentList = [];
    let currentIndex = 0;
    let currentItem = null;
    let score = 0;
    let attempts = 0;
    let alreadyCorrect = false;

    const categorySelect = document.getElementById("categorySelect");
    const randomBtn = document.getElementById("randomBtn");
    const resetBtn = document.getElementById("resetBtn");
    const categoryLabel = document.getElementById("categoryLabel");
    const scoreLabel = document.getElementById("scoreLabel");
    const koPrompt = document.getElementById("koPrompt");
    const blankSentence = document.getElementById("blankSentence");
    const hintBox = document.getElementById("hintBox");
    const answerBox = document.getElementById("answerBox");
    const hintBtn = document.getElementById("hintBtn");
    const listenBtn = document.getElementById("listenBtn");
    const answerBtn = document.getElementById("answerBtn");
    const micBtn = document.getElementById("micBtn");
    const nextBtn = document.getElementById("nextBtn");
    const transcriptBox = document.getElementById("transcriptBox");
    const resultBox = document.getElementById("resultBox");

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition = null;

    function uniqueCategories() {
        const cats = ["전체"];
        ITEMS.forEach(item => {
            if (!cats.includes(item.cat)) cats.push(item.cat);
        });
        return cats;
    }

    function initCategories() {
        const cats = uniqueCategories();
        categorySelect.innerHTML = "";
        cats.forEach(cat => {
            const option = document.createElement("option");
            option.value = cat;
            option.innerText = cat;
            categorySelect.appendChild(option);
        });
    }

    function getFilteredItems() {
        const selected = categorySelect.value;
        if (selected === "전체") return ITEMS.slice();
        return ITEMS.filter(item => item.cat === selected);
    }

    function shuffleArray(arr) {
        const copied = arr.slice();
        for (let i = copied.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copied[i], copied[j]] = [copied[j], copied[i]];
        }
        return copied;
    }

    function makeTwoLetterHint(answerWord) {
        if (!answerWord) return "";

        return answerWord.split(" ").map(word => {
            const clean = word.trim();
            if (clean.length <= 2) return clean;
            return clean.slice(0, 2) + "_".repeat(clean.length - 2);
        }).join(" ");
    }

    function normalizeText(text) {
        return text
            .toLowerCase()
            // 축약형을 먼저 풀어 줌
            .replace(/\bi'm\b/g, "i am")
            .replace(/\bim\b/g, "i am")
            .replace(/\byou're\b/g, "you are")
            .replace(/\bhe's\b/g, "he is")
            .replace(/\bshe's\b/g, "she is")
            .replace(/\bit's\b/g, "it is")
            .replace(/\bwe're\b/g, "we are")
            .replace(/\bthey're\b/g, "they are")
            .replace(/\bdon't\b/g, "do not")
            .replace(/\bdoesn't\b/g, "does not")
            .replace(/\bdidn't\b/g, "did not")
            .replace(/\bcan't\b/g, "cannot")
            .replace(/\bcant\b/g, "cannot")
            .replace(/\bi'll\b/g, "i will")
            .replace(/\byou'll\b/g, "you will")
            .replace(/\bhe'll\b/g, "he will")
            .replace(/\bshe'll\b/g, "she will")
            .replace(/[.,!?;:'"’‘“”]/g, "")
            .replace(/\s+/g, " ")
            .trim();
    }

    function wordsOnly(text) {
        return normalizeText(text)
            .split(" ")
            .filter(w => w.length > 0);
    }

    function editDistance(a, b) {
        const dp = Array.from({ length: a.length + 1 }, () => Array(b.length + 1).fill(0));

        for (let i = 0; i <= a.length; i++) dp[i][0] = i;
        for (let j = 0; j <= b.length; j++) dp[0][j] = j;

        for (let i = 1; i <= a.length; i++) {
            for (let j = 1; j <= b.length; j++) {
                const cost = a[i - 1] === b[j - 1] ? 0 : 1;
                dp[i][j] = Math.min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + cost
                );
            }
        }

        return dp[a.length][b.length];
    }

    function isCloseEnough(spoken, answer) {
        const s = normalizeText(spoken);
        const a = normalizeText(answer);

        if (!s || !a) return false;

        const sWords = wordsOnly(s);
        const aWords = wordsOnly(a);

        // 1) 축약형을 푼 뒤 완전 일치하면 정답
        // 예: "I'm hungry" → "I am hungry"
        if (s === a) return true;

        // 2) 음성 인식이 정답 앞뒤에 짧은 말을 붙이는 경우만 허용
        // 예: "um i am hungry" / "i am hungry please"
        if (sWords.length <= aWords.length + 2) {
            for (let i = 0; i <= sWords.length - aWords.length; i++) {
                const slice = sWords.slice(i, i + aWords.length).join(" ");
                if (slice === a) return true;
            }
        }

        // 3) 핵심 정답 단어는 반드시 들어가야 함
        // 빈칸 정답 단어 currentItem.hint가 빠지면 오답
        const keyWords = normalizeText(currentItem.hint || "").split(" ").filter(w => w.length > 0);
        const hasAllKeyWords = keyWords.every(w => sWords.includes(w));
        if (!hasAllKeyWords) return false;

        // 4) 정답 단어 수와 말한 단어 수가 너무 다르면 오답
        // 예: "water"만 말했는데 "I need water" 정답 처리되는 것 방지
        if (sWords.length < aWords.length) return false;
        if (sWords.length > aWords.length + 2) return false;

        // 5) 정답 문장의 각 단어가 순서대로 거의 들어 있는지 확인
        // 핵심 단어는 위에서 이미 확인했고, i/am/do 같은 짧은 기능어는 약간만 허용
        let matchedCount = 0;
        let searchStart = 0;

        for (const aw of aWords) {
            let foundIndex = -1;

            for (let i = searchStart; i < sWords.length; i++) {
                if (sWords[i] === aw) {
                    foundIndex = i;
                    break;
                }
            }

            if (foundIndex !== -1) {
                matchedCount += 1;
                searchStart = foundIndex + 1;
            }
        }

        // 짧은 문장은 거의 완전 일치해야 함
        if (aWords.length <= 3) {
            return matchedCount === aWords.length;
        }

        // 긴 문장도 한 단어 이상 빠지면 오답에 가깝게 처리
        return matchedCount >= aWords.length - 1;
    }

    function isCorrectSpeech(spoken, answer) {
        return isCloseEnough(spoken, answer);
    }

    function updateScore() {
        scoreLabel.innerText = score + " / " + attempts;
    }

    function loadQuestion(index = 0) {
        if (currentList.length === 0) {
            currentList = getFilteredItems();
        }

        if (index >= currentList.length) index = 0;
        if (index < 0) index = currentList.length - 1;

        currentIndex = index;
        currentItem = currentList[currentIndex];
        alreadyCorrect = false;

        categoryLabel.innerText = currentItem.cat + " · " + (currentIndex + 1) + " / " + currentList.length;
        const emoji = currentItem.emoji || "🛟";
        koPrompt.innerHTML =
            "<span style='font-size:42px; margin-right:10px; vertical-align:middle;'>" + emoji + "</span>" +
            "<span style='vertical-align:middle;'>" + currentItem.ko + "</span>";
        blankSentence.innerText = currentItem.blank;
        hintBox.style.display = "none";
        answerBox.style.display = "none";
        hintBox.innerText = "";
        answerBox.innerText = "";
        transcriptBox.innerText = "아직 말하지 않았습니다.";
        resultBox.innerText = "마이크 버튼을 누르고 문장 전체를 말해 보세요. I'm, don't 같은 자연스러운 축약형은 괜찮습니다.";
        resultBox.style.background = "#f1f5f9";
        resultBox.style.borderColor = "#e2e8f0";
        resultBox.style.color = "#334155";
    }

    function speak(text) {
        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "en-US";
        utterance.rate = 0.82;
        utterance.pitch = 1.05;

        const voices = window.speechSynthesis.getVoices();
        const preferred = voices.find(v =>
            v.lang && v.lang.toLowerCase().startsWith("en") &&
            /(samantha|jenny|aria|zira|google us english|karen|victoria|female)/i.test(v.name)
        );
        if (preferred) utterance.voice = preferred;

        window.speechSynthesis.speak(utterance);
    }

    function checkSpeech(spokenText) {
        attempts += 1;

        if (isCorrectSpeech(spokenText, currentItem.answer)) {
            if (!alreadyCorrect) {
                score += 1;
                alreadyCorrect = true;
            }

            resultBox.innerHTML = "✅ 정답입니다!<br><span style='font-size:17px;'>잘 말했어요: " + currentItem.answer + "</span>";
            resultBox.style.background = "#ecfdf5";
            resultBox.style.borderColor = "#bbf7d0";
            resultBox.style.color = "#166534";

            speak(currentItem.answer);
        } else {
            resultBox.innerHTML =
                "🍊 문장 전체가 정확히 맞아야 해요. 다시 말해 보세요.<br>" +
                "<span style='font-size:17px;'>목표 문장: " + currentItem.answer + "</span>";
            resultBox.style.background = "#fff7ed";
            resultBox.style.borderColor = "#fed7aa";
            resultBox.style.color = "#9a3412";
        }

        updateScore();
    }

    function startRecognition() {
        if (!SpeechRecognition) {
            resultBox.innerText = "이 브라우저에서는 음성 인식을 사용할 수 없습니다. Chrome에서 실행해 보세요.";
            resultBox.style.background = "#fef2f2";
            resultBox.style.borderColor = "#fecaca";
            resultBox.style.color = "#991b1b";
            return;
        }

        window.speechSynthesis.cancel();

        recognition = new SpeechRecognition();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.continuous = false;
        recognition.maxAlternatives = 3;

        micBtn.innerText = "🎙️ 듣는 중...";
        resultBox.innerText = "지금 말해 보세요.";
        resultBox.style.background = "#eff6ff";
        resultBox.style.borderColor = "#bfdbfe";
        resultBox.style.color = "#1d4ed8";

        recognition.onresult = function(event) {
            let bestTranscript = "";
            let matched = false;

            for (let i = 0; i < event.results[0].length; i++) {
                const transcript = event.results[0][i].transcript;
                if (i === 0) bestTranscript = transcript;

                if (isCorrectSpeech(transcript, currentItem.answer)) {
                    bestTranscript = transcript;
                    matched = true;
                    break;
                }
            }

            transcriptBox.innerText = bestTranscript;
            checkSpeech(bestTranscript);
        };

        recognition.onerror = function(event) {
            resultBox.innerText = "음성 인식 오류가 났습니다. 다시 눌러 주세요.";
            resultBox.style.background = "#fef2f2";
            resultBox.style.borderColor = "#fecaca";
            resultBox.style.color = "#991b1b";
            micBtn.innerText = "🎙️ 말하기 시작";
        };

        recognition.onend = function() {
            micBtn.innerText = "🎙️ 말하기 시작";
        };

        recognition.start();
    }

    categorySelect.addEventListener("change", function() {
        currentList = getFilteredItems();
        currentIndex = 0;
        loadQuestion(0);
    });

    randomBtn.addEventListener("click", function() {
        currentList = shuffleArray(getFilteredItems());
        loadQuestion(0);
    });

    resetBtn.addEventListener("click", function() {
        score = 0;
        attempts = 0;
        alreadyCorrect = false;
        updateScore();
        resultBox.innerText = "점수를 초기화했습니다.";
    });

    hintBtn.addEventListener("click", function() {
        hintBox.style.display = "block";
        hintBox.innerText = "힌트: " + makeTwoLetterHint(currentItem.hint);
    });

    listenBtn.addEventListener("click", function() {
        speak(currentItem.answer);
    });

    answerBtn.addEventListener("click", function() {
        answerBox.style.display = "block";
        answerBox.innerText = "정답: " + currentItem.answer;
    });

    micBtn.addEventListener("click", startRecognition);

    nextBtn.addEventListener("click", function() {
        loadQuestion(currentIndex + 1);
    });

    initCategories();
    currentList = getFilteredItems();
    updateScore();
    loadQuestion(0);
    </script>
    """

    html = html.replace("__ITEMS_JSON__", items_json)
    components.html(html, height=760)


speaking_practice_component(PRACTICE_ITEMS)
