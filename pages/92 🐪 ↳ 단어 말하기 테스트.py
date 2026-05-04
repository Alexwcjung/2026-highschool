import streamlit as st
from gtts import gTTS
import io
import random
import base64
import uuid
import json
import streamlit.components.v1 as components

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Survival English 500 Speaking Mission",
    page_icon="🗣️",
    layout="wide"
)

TOTAL_QUESTIONS = 100

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 46px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 4px;
    }

    .sub-title {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 24px;
    }

    .hero-box {
        background: linear-gradient(135deg, #ecfeff 0%, #fef3c7 48%, #fce7f3 100%);
        border-radius: 30px;
        padding: 28px 32px;
        margin-bottom: 26px;
        box-shadow: 0 10px 28px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.9);
    }

    .hero-title {
        font-size: 27px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .hero-text {
        font-size: 16px;
        color: #374151;
        line-height: 1.8;
    }

    .mission-card {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 34px;
        padding: 38px 40px;
        margin-bottom: 24px;
        border: 1px solid #dbeafe;
        box-shadow: 0 12px 30px rgba(15,23,42,0.08);
        text-align: center;
    }

    .top-badges {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 16px;
    }

    .question-number-badge {
        display: inline-block;
        background: linear-gradient(135deg, #0ea5e9, #6366f1);
        color: white;
        padding: 10px 18px;
        border-radius: 999px;
        font-size: 17px;
        font-weight: 900;
        box-shadow: 0 4px 12px rgba(14,165,233,0.25);
    }

    .progress-badge {
        display: inline-block;
        background: #dbeafe;
        color: #1d4ed8;
        padding: 9px 16px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 900;
    }

    .theme-badge {
        display: inline-block;
        background: #fce7f3;
        color: #be185d;
        padding: 9px 15px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 900;
    }

    .mini-score-row {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 10px;
        margin-bottom: 18px;
    }

    .mini-score-good {
        background: #dcfce7;
        color: #166534;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 900;
    }

    .mini-score-practice {
        background: #fff7ed;
        color: #9a3412;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 900;
    }

    .emoji-circle {
        width: 150px;
        height: 150px;
        border-radius: 999px;
        background: linear-gradient(135deg, #fef9c3, #dbeafe, #fce7f3);
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 18px auto 12px auto;
        box-shadow: inset 0 0 0 8px rgba(255,255,255,0.65), 0 8px 20px rgba(0,0,0,0.08);
    }

    .emoji-box {
        font-size: 84px;
        line-height: 1;
    }

    .meaning-box {
        font-size: 48px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 18px;
    }

    .speak-guide {
        font-size: 20px;
        font-weight: 800;
        color: #374151;
        margin-top: 16px;
        margin-bottom: 16px;
    }

    .hidden-word {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 22px;
        padding: 18px 20px;
        margin: 16px auto 20px auto;
        max-width: 520px;
    }

    .english-word {
        font-size: 40px;
        font-weight: 900;
        color: #111827;
    }

    .english-caption {
        font-size: 15px;
        font-weight: 700;
        color: #64748b;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 30px;
        padding: 32px 36px;
        margin-bottom: 26px;
        border: 1px solid #bbf7d0;
        box-shadow: 0 10px 28px rgba(0,0,0,0.08);
    }

    .score-title {
        font-size: 40px;
        font-weight: 900;
        color: #14532d;
        margin-bottom: 10px;
    }

    .score-text {
        font-size: 20px;
        font-weight: 800;
        color: #374151;
        line-height: 1.8;
    }

    .result-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(180px, 1fr));
        gap: 16px;
        margin-top: 18px;
        margin-bottom: 18px;
    }

    .result-mini-card {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(255,255,255,0.9);
        border-radius: 22px;
        padding: 18px 20px;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    }

    .result-number {
        font-size: 38px;
        font-weight: 900;
        color: #111827;
    }

    .result-label {
        font-size: 16px;
        font-weight: 900;
        color: #475569;
    }

    .review-card {
        background: white;
        border-radius: 18px;
        padding: 14px 16px;
        margin-bottom: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }

    .review-line {
        display: flex;
        align-items: center;
        gap: 16px;
        flex-wrap: wrap;
    }

    .review-num {
        min-width: 54px;
        background: #fef3c7;
        color: #92400e;
        border-radius: 999px;
        padding: 6px 11px;
        font-weight: 900;
        text-align: center;
    }

    .review-emoji {
        font-size: 28px;
        min-width: 34px;
    }

    .review-ko {
        font-size: 20px;
        font-weight: 900;
        min-width: 110px;
    }

    .review-en {
        font-size: 22px;
        font-weight: 900;
        color: #111827;
        min-width: 130px;
    }

    .review-status {
        font-size: 16px;
        font-weight: 900;
        color: #374151;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        border: 1px solid #d1d5db;
        padding: 0.68rem 1.25rem;
        font-size: 16px;
        white-space: nowrap;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
    }

    .stButton > button:hover {
        border-color: #0ea5e9;
        color: #0ea5e9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 제목
# =========================
st.markdown("<div class='main-title'>🗣️ Survival English 500 Speaking Mission</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>이모지와 한국어 뜻을 보고, 영어 발음을 듣고, 직접 따라 말하는 100문제 자기진단 미션입니다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="hero-box">
        <div class="hero-title">🎧 말하기 미션 방법</div>
        <div class="hero-text">
            • 문제는 <b>이모지 + 한국어 뜻</b>으로 나옵니다.<br>
            • <b>정답 발음 듣기</b>를 누르고 영어 단어를 따라 말해 보세요.<br>
            • 말한 뒤 <b>잘 말했어요</b> 또는 <b>연습이 더 필요해요</b>를 선택합니다.<br>
            • 총 <b>{TOTAL_QUESTIONS}문제</b>가 랜덤으로 출제됩니다.<br>
            • 마지막에 <b>잘 말한 단어 / 연습이 필요한 단어</b> 기록을 확인합니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS
# =========================
@st.cache_data
def make_tts_audio(text, lang="en", tld="com"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


# =========================
# 발음 버튼
# =========================
def audio_button(label, text, height=58):
    audio_bytes = make_tts_audio(text)
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    audio_id = f"audio_{uuid.uuid4().hex}"
    play_btn_id = f"play_btn_{uuid.uuid4().hex}"
    stop_btn_id = f"stop_btn_{uuid.uuid4().hex}"
    status_id = f"status_{uuid.uuid4().hex}"
    player_id = f"player_{uuid.uuid4().hex}"

    safe_label = json.dumps(label)
    safe_player_id = json.dumps(player_id)

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; justify-content:center; gap:12px; height:50px;">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #dcfce7, #dbeafe);
                border: 1px solid #bbf7d0;
                border-radius: 999px;
                padding: 9px 17px;
                font-weight: 900;
                font-size: 15px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                white-space: nowrap;
            ">
                {label}
            </button>

            <button id="{stop_btn_id}" style="
                background: #fff7ed;
                border: 1px solid #fed7aa;
                border-radius: 999px;
                padding: 9px 17px;
                font-weight: 900;
                font-size: 15px;
                color: #9a3412;
                cursor: pointer;
                box-shadow: 0 2px 6px rgba(0,0,0,0.04);
                white-space: nowrap;
            ">
                ⏹ 중지
            </button>

            <span id="{status_id}" style="
                font-size: 13px;
                color: #075985;
                font-weight: 800;
                white-space: nowrap;
            "></span>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");
            const playerId = {safe_player_id};
            const labelText = {safe_label};

            const channel = new BroadcastChannel("survival_speaking_audio_channel");

            function stopAudio(showMessage = false) {{
                audio.pause();
                audio.currentTime = 0;
                playBtn.disabled = false;
                playBtn.innerText = labelText;

                if (showMessage) {{
                    status.innerText = "중지됨";
                }} else {{
                    status.innerText = "";
                }}
            }}

            channel.onmessage = function(event) {{
                if (!event.data) return;
                if (event.data.type === "STOP_OTHERS" && event.data.playerId !== playerId) {{
                    stopAudio(false);
                }}
            }};

            playBtn.addEventListener("click", function() {{
                channel.postMessage({{
                    type: "STOP_OTHERS",
                    playerId: playerId
                }});

                stopAudio(false);
                playBtn.disabled = true;
                playBtn.innerText = "재생 중";
                status.innerText = "듣는 중";

                audio.play().then(() => {{
                    status.innerText = "듣는 중";
                }}).catch((error) => {{
                    status.innerText = "다시 클릭";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }});
            }});

            audio.addEventListener("ended", function() {{
                playBtn.disabled = false;
                playBtn.innerText = labelText;
                status.innerText = "완료";
            }});

            stopBtn.addEventListener("click", function() {{
                stopAudio(true);
            }});
            </script>
        </div>
        """,
        height=height
    )


# =========================
# Survival English 500 단어 데이터
# =========================
word_themes = {
    "🧍 나와 사람": [
        {"word": "I", "meaning": "나", "emoji": "🙋"},
        {"word": "you", "meaning": "너, 당신", "emoji": "👉"},
        {"word": "he", "meaning": "그", "emoji": "👦"},
        {"word": "she", "meaning": "그녀", "emoji": "👧"},
        {"word": "we", "meaning": "우리", "emoji": "👥"},
        {"word": "they", "meaning": "그들", "emoji": "👥"},
        {"word": "friend", "meaning": "친구", "emoji": "🤝"},
        {"word": "teacher", "meaning": "선생님", "emoji": "👩‍🏫"},
        {"word": "student", "meaning": "학생", "emoji": "🧑‍🎓"},
        {"word": "classmate", "meaning": "반 친구", "emoji": "👫"},
        {"word": "family", "meaning": "가족", "emoji": "👨‍👩‍👧"},
        {"word": "father", "meaning": "아버지", "emoji": "👨"},
        {"word": "mother", "meaning": "어머니", "emoji": "👩"},
        {"word": "brother", "meaning": "형제, 남자 형제", "emoji": "👦"},
        {"word": "sister", "meaning": "자매, 여자 형제", "emoji": "👧"},
        {"word": "name", "meaning": "이름", "emoji": "🏷️"},
        {"word": "person", "meaning": "사람", "emoji": "🧍"},
        {"word": "man", "meaning": "남자", "emoji": "👨"},
        {"word": "woman", "meaning": "여자", "emoji": "👩"},
        {"word": "child", "meaning": "아이", "emoji": "🧒"},
    ],

    "🏃 기본 동작": [
        {"word": "go", "meaning": "가다", "emoji": "➡️"},
        {"word": "come", "meaning": "오다", "emoji": "⬅️"},
        {"word": "walk", "meaning": "걷다", "emoji": "🚶"},
        {"word": "run", "meaning": "달리다", "emoji": "🏃"},
        {"word": "sit", "meaning": "앉다", "emoji": "🪑"},
        {"word": "stand", "meaning": "서다", "emoji": "🧍"},
        {"word": "stop", "meaning": "멈추다", "emoji": "🛑"},
        {"word": "start", "meaning": "시작하다", "emoji": "▶️"},
        {"word": "open", "meaning": "열다", "emoji": "📖"},
        {"word": "close", "meaning": "닫다", "emoji": "📕"},
        {"word": "eat", "meaning": "먹다", "emoji": "🍽️"},
        {"word": "drink", "meaning": "마시다", "emoji": "🥤"},
        {"word": "sleep", "meaning": "자다", "emoji": "😴"},
        {"word": "study", "meaning": "공부하다", "emoji": "📚"},
        {"word": "read", "meaning": "읽다", "emoji": "📖"},
        {"word": "write", "meaning": "쓰다", "emoji": "✏️"},
        {"word": "listen", "meaning": "듣다", "emoji": "👂"},
        {"word": "speak", "meaning": "말하다", "emoji": "🗣️"},
        {"word": "help", "meaning": "돕다", "emoji": "🆘"},
        {"word": "wait", "meaning": "기다리다", "emoji": "⏳"},
    ],

    "💖 감정·몸 상태": [
        {"word": "happy", "meaning": "행복한", "emoji": "😊"},
        {"word": "sad", "meaning": "슬픈", "emoji": "😢"},
        {"word": "angry", "meaning": "화난", "emoji": "😡"},
        {"word": "tired", "meaning": "피곤한", "emoji": "🥱"},
        {"word": "hungry", "meaning": "배고픈", "emoji": "😋"},
        {"word": "thirsty", "meaning": "목마른", "emoji": "💧"},
        {"word": "sick", "meaning": "아픈", "emoji": "🤒"},
        {"word": "okay", "meaning": "괜찮은", "emoji": "👌"},
        {"word": "fine", "meaning": "괜찮은", "emoji": "🙂"},
        {"word": "cold", "meaning": "추운, 차가운", "emoji": "🥶"},
        {"word": "hot", "meaning": "더운, 뜨거운", "emoji": "🥵"},
        {"word": "pain", "meaning": "통증", "emoji": "🤕"},
        {"word": "headache", "meaning": "두통", "emoji": "🤯"},
        {"word": "stomachache", "meaning": "복통", "emoji": "🤢"},
        {"word": "fever", "meaning": "열", "emoji": "🌡️"},
        {"word": "hurt", "meaning": "아프다, 다치다", "emoji": "🩹"},
        {"word": "good", "meaning": "좋은", "emoji": "👍"},
        {"word": "bad", "meaning": "나쁜", "emoji": "👎"},
        {"word": "worried", "meaning": "걱정하는", "emoji": "😟"},
        {"word": "scared", "meaning": "무서워하는", "emoji": "😨"},
    ],

    "🍎 음식·물": [
        {"word": "food", "meaning": "음식", "emoji": "🍽️"},
        {"word": "water", "meaning": "물", "emoji": "💧"},
        {"word": "rice", "meaning": "밥, 쌀", "emoji": "🍚"},
        {"word": "bread", "meaning": "빵", "emoji": "🍞"},
        {"word": "milk", "meaning": "우유", "emoji": "🥛"},
        {"word": "juice", "meaning": "주스", "emoji": "🧃"},
        {"word": "coffee", "meaning": "커피", "emoji": "☕"},
        {"word": "tea", "meaning": "차", "emoji": "🍵"},
        {"word": "apple", "meaning": "사과", "emoji": "🍎"},
        {"word": "banana", "meaning": "바나나", "emoji": "🍌"},
        {"word": "egg", "meaning": "달걀", "emoji": "🥚"},
        {"word": "meat", "meaning": "고기", "emoji": "🥩"},
        {"word": "chicken", "meaning": "닭고기, 닭", "emoji": "🍗"},
        {"word": "fish", "meaning": "생선, 물고기", "emoji": "🐟"},
        {"word": "breakfast", "meaning": "아침 식사", "emoji": "🍳"},
        {"word": "lunch", "meaning": "점심 식사", "emoji": "🍱"},
        {"word": "dinner", "meaning": "저녁 식사", "emoji": "🍽️"},
        {"word": "snack", "meaning": "간식", "emoji": "🍪"},
        {"word": "medicine", "meaning": "약", "emoji": "💊"},
        {"word": "hospital", "meaning": "병원", "emoji": "🏥"},
    ],

    "🚗 장소·이동": [
        {"word": "home", "meaning": "집", "emoji": "🏠"},
        {"word": "school", "meaning": "학교", "emoji": "🏫"},
        {"word": "classroom", "meaning": "교실", "emoji": "🧑‍🏫"},
        {"word": "bathroom", "meaning": "화장실", "emoji": "🚻"},
        {"word": "hospital", "meaning": "병원", "emoji": "🏥"},
        {"word": "store", "meaning": "가게", "emoji": "🏪"},
        {"word": "station", "meaning": "역", "emoji": "🚉"},
        {"word": "bus", "meaning": "버스", "emoji": "🚌"},
        {"word": "car", "meaning": "자동차", "emoji": "🚗"},
        {"word": "taxi", "meaning": "택시", "emoji": "🚕"},
        {"word": "train", "meaning": "기차", "emoji": "🚆"},
        {"word": "bike", "meaning": "자전거", "emoji": "🚲"},
        {"word": "road", "meaning": "도로", "emoji": "🛣️"},
        {"word": "street", "meaning": "거리", "emoji": "🏙️"},
        {"word": "here", "meaning": "여기", "emoji": "📍"},
        {"word": "there", "meaning": "거기", "emoji": "📌"},
        {"word": "near", "meaning": "가까운", "emoji": "📍"},
        {"word": "far", "meaning": "먼", "emoji": "🧭"},
        {"word": "left", "meaning": "왼쪽", "emoji": "⬅️"},
        {"word": "right", "meaning": "오른쪽, 맞는", "emoji": "➡️"},
    ],

    "⏰ 시간·숫자": [
        {"word": "time", "meaning": "시간", "emoji": "⏰"},
        {"word": "now", "meaning": "지금", "emoji": "🕒"},
        {"word": "today", "meaning": "오늘", "emoji": "📅"},
        {"word": "tomorrow", "meaning": "내일", "emoji": "➡️"},
        {"word": "yesterday", "meaning": "어제", "emoji": "⬅️"},
        {"word": "morning", "meaning": "아침", "emoji": "🌅"},
        {"word": "afternoon", "meaning": "오후", "emoji": "☀️"},
        {"word": "evening", "meaning": "저녁", "emoji": "🌆"},
        {"word": "night", "meaning": "밤", "emoji": "🌙"},
        {"word": "early", "meaning": "이른", "emoji": "🐓"},
        {"word": "late", "meaning": "늦은", "emoji": "🌃"},
        {"word": "one", "meaning": "하나", "emoji": "1️⃣"},
        {"word": "two", "meaning": "둘", "emoji": "2️⃣"},
        {"word": "three", "meaning": "셋", "emoji": "3️⃣"},
        {"word": "four", "meaning": "넷", "emoji": "4️⃣"},
        {"word": "five", "meaning": "다섯", "emoji": "5️⃣"},
        {"word": "six", "meaning": "여섯", "emoji": "6️⃣"},
        {"word": "seven", "meaning": "일곱", "emoji": "7️⃣"},
        {"word": "eight", "meaning": "여덟", "emoji": "8️⃣"},
        {"word": "ten", "meaning": "열", "emoji": "🔟"},
    ],

    "🎒 물건·돈": [
        {"word": "bag", "meaning": "가방", "emoji": "🎒"},
        {"word": "phone", "meaning": "전화기", "emoji": "📱"},
        {"word": "book", "meaning": "책", "emoji": "📘"},
        {"word": "notebook", "meaning": "공책", "emoji": "📓"},
        {"word": "pen", "meaning": "펜", "emoji": "🖊️"},
        {"word": "pencil", "meaning": "연필", "emoji": "✏️"},
        {"word": "desk", "meaning": "책상", "emoji": "🪑"},
        {"word": "chair", "meaning": "의자", "emoji": "🪑"},
        {"word": "door", "meaning": "문", "emoji": "🚪"},
        {"word": "window", "meaning": "창문", "emoji": "🪟"},
        {"word": "key", "meaning": "열쇠", "emoji": "🔑"},
        {"word": "money", "meaning": "돈", "emoji": "💰"},
        {"word": "card", "meaning": "카드", "emoji": "💳"},
        {"word": "ticket", "meaning": "표, 티켓", "emoji": "🎫"},
        {"word": "clothes", "meaning": "옷", "emoji": "👕"},
        {"word": "shoes", "meaning": "신발", "emoji": "👟"},
        {"word": "hat", "meaning": "모자", "emoji": "🧢"},
        {"word": "watch", "meaning": "시계", "emoji": "⌚"},
        {"word": "cup", "meaning": "컵", "emoji": "🥤"},
        {"word": "bottle", "meaning": "병", "emoji": "🍼"},
    ],

    "🆘 도움 요청": [
        {"word": "help", "meaning": "도움, 돕다", "emoji": "🆘"},
        {"word": "please", "meaning": "부디, 제발", "emoji": "🙏"},
        {"word": "sorry", "meaning": "미안합니다", "emoji": "🙇"},
        {"word": "excuse me", "meaning": "실례합니다", "emoji": "🙋"},
        {"word": "again", "meaning": "다시", "emoji": "🔁"},
        {"word": "slowly", "meaning": "천천히", "emoji": "🐢"},
        {"word": "understand", "meaning": "이해하다", "emoji": "💡"},
        {"word": "question", "meaning": "질문", "emoji": "❓"},
        {"word": "problem", "meaning": "문제", "emoji": "⚠️"},
        {"word": "need", "meaning": "필요하다", "emoji": "📌"},
        {"word": "want", "meaning": "원하다", "emoji": "🙋"},
        {"word": "know", "meaning": "알다", "emoji": "🧠"},
        {"word": "say", "meaning": "말하다", "emoji": "💬"},
        {"word": "tell", "meaning": "말하다, 알려주다", "emoji": "🗣️"},
        {"word": "ask", "meaning": "묻다", "emoji": "❓"},
        {"word": "answer", "meaning": "대답, 답", "emoji": "✅"},
        {"word": "repeat", "meaning": "반복하다", "emoji": "🔁"},
        {"word": "speak", "meaning": "말하다", "emoji": "🗣️"},
        {"word": "look", "meaning": "보다", "emoji": "👀"},
        {"word": "listen", "meaning": "듣다", "emoji": "👂"},
    ],
}

# =========================
# 전체 단어 목록 만들기
# =========================
all_words = []
for theme, words in word_themes.items():
    for item in words:
        new_item = item.copy()
        new_item["theme"] = theme
        all_words.append(new_item)

# =========================
# 테스트 시작
# =========================
def start_new_mission():
    question_count = min(TOTAL_QUESTIONS, len(all_words))
    questions = random.sample(all_words, question_count)

    st.session_state.questions = questions
    st.session_state.total_questions = question_count
    st.session_state.current_index = 0
    st.session_state.records = []
    st.session_state.mission_started = True
    st.session_state.mission_finished = False


if "mission_started" not in st.session_state:
    st.session_state.mission_started = False

if "mission_finished" not in st.session_state:
    st.session_state.mission_finished = False

# =========================
# 시작 화면
# =========================
if not st.session_state.mission_started:
    st.markdown("### 🚀 말하기 미션 시작")
    st.write(f"총 {TOTAL_QUESTIONS}개의 단어가 랜덤으로 나옵니다. 듣고 따라 말한 뒤 자기진단을 해 보세요.")

    if st.button(f"🗣️ {TOTAL_QUESTIONS}개 말하기 미션 시작하기"):
        start_new_mission()
        st.rerun()

# =========================
# 미션 진행 화면
# =========================
elif st.session_state.mission_started and not st.session_state.mission_finished:
    idx = st.session_state.current_index
    q = st.session_state.questions[idx]
    total = st.session_state.total_questions

    good_now = sum(1 for r in st.session_state.records if r["status"] == "잘 말했어요")
    practice_now = sum(1 for r in st.session_state.records if r["status"] == "연습이 더 필요해요")

    progress_value = (idx + 1) / total

    st.progress(progress_value)

    st.markdown('<div class="mission-card">', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="top-badges">
            <span class="question-number-badge">문제 {idx + 1}번</span>
            <span class="progress-badge">{idx + 1} / {total}</span>
            <span class="theme-badge">{q['theme']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="mini-score-row">
            <span class="mini-score-good">😊 잘 말했어요 {good_now}개</span>
            <span class="mini-score-practice">🔁 연습 필요 {practice_now}개</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="emoji-circle">
            <div class="emoji-box">{q['emoji']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<div class='meaning-box'>{q['meaning']}</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="speak-guide">
            발음을 듣고, 큰 소리로 따라 말해 보세요.
        </div>
        """,
        unsafe_allow_html=True
    )

    audio_button("🔊 정답 발음 듣기", q["word"])

    with st.expander("👀 영어 단어 확인하기"):
        st.markdown(
            f"""
            <div class="hidden-word">
                <div class="english-caption">정답 영어 단어</div>
                <div class="english-word">{q['word']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 자기 진단")

    def save_record(status):
        st.session_state.records.append({
            "number": idx + 1,
            "theme": q["theme"],
            "emoji": q["emoji"],
            "meaning": q["meaning"],
            "word": q["word"],
            "status": status
        })

        if idx < total - 1:
            st.session_state.current_index += 1
        else:
            st.session_state.mission_finished = True

        st.rerun()

    left_space, btn1_col, btn2_col, right_space = st.columns([2.8, 1.2, 1.2, 2.8], gap="small")

    with btn1_col:
        if st.button("😊 잘 말했어요", key=f"good_{idx}", use_container_width=True):
            save_record("잘 말했어요")

    with btn2_col:
        if st.button("🔁 연습이 더 필요해요", key=f"practice_{idx}", use_container_width=True):
            save_record("연습이 더 필요해요")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 결과 화면
# =========================
else:
    records = st.session_state.records
    total = st.session_state.total_questions

    good_count = sum(1 for r in records if r["status"] == "잘 말했어요")
    practice_count = sum(1 for r in records if r["status"] == "연습이 더 필요해요")
    percent = round(good_count / total * 100, 1)

    st.markdown(
        f"""
        <div class="score-box">
            <div class="score-title">🏆 말하기 미션 결과</div>
            <div class="score-text">
                총 말하기 단어: {total}개<br>
                정답처럼 말한 비율: {percent}%
            </div>

            <div class="result-grid">
                <div class="result-mini-card">
                    <div class="result-number">😊 {good_count}</div>
                    <div class="result-label">잘 말했어요</div>
                </div>
                <div class="result-mini-card">
                    <div class="result-number">🔁 {practice_count}</div>
                    <div class="result-label">연습이 더 필요해요</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if good_count >= int(total * 0.8):
        st.success("🌟 훌륭합니다! 오늘 말하기 미션을 아주 잘 해냈습니다.")
    elif good_count >= int(total * 0.5):
        st.info("👍 좋습니다! 연습이 필요한 단어만 다시 반복하면 됩니다.")
    else:
        st.warning("🌱 괜찮습니다. 오늘은 입으로 영어를 꺼내 본 것 자체가 큰 성공입니다.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"🔄 다시 {TOTAL_QUESTIONS}개 말하기"):
            start_new_mission()
            st.rerun()

    with col2:
        if st.button("🧹 처음 화면으로"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("### 📋 전체 기록")

    for item in records:
        if item["status"] == "잘 말했어요":
            status_icon = "😊"
        else:
            status_icon = "🔁"

        st.markdown('<div class="review-card">', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="review-line">
                <div class="review-num">{item['number']}번</div>
                <div class="review-emoji">{item['emoji']}</div>
                <div class="review-ko">{item['meaning']}</div>
                <div class="review-en">{item['word']}</div>
                <div class="review-status">{status_icon} {item['status']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
