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
    page_title="Survival English 500 Test",
    page_icon="🛟",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 44px;
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
        background: linear-gradient(135deg, #ecfeff 0%, #fef3c7 50%, #fce7f3 100%);
        border-radius: 26px;
        padding: 26px 30px;
        margin-bottom: 26px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
    }

    .hero-title {
        font-size: 26px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .hero-text {
        font-size: 16px;
        color: #374151;
        line-height: 1.8;
    }

    .question-card {
        background: white;
        border-radius: 28px;
        padding: 34px 36px;
        margin-bottom: 24px;
        border: 1px solid #dbeafe;
        box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    }

    .progress-badge {
        display: inline-block;
        background: #dbeafe;
        color: #1d4ed8;
        padding: 8px 15px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 900;
        margin-bottom: 18px;
    }

    .theme-badge {
        display: inline-block;
        background: #fce7f3;
        color: #be185d;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 900;
        margin-left: 8px;
        margin-bottom: 18px;
    }

    .emoji-box {
        font-size: 78px;
        margin-bottom: 8px;
    }

    .korean-meaning {
        font-size: 42px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 16px;
    }

    .instruction {
        font-size: 18px;
        color: #4b5563;
        font-weight: 700;
        margin-bottom: 18px;
    }

    .result-correct {
        background: #dcfce7;
        color: #166534;
        border-radius: 20px;
        padding: 18px 20px;
        font-size: 22px;
        font-weight: 900;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .result-wrong {
        background: #fee2e2;
        color: #991b1b;
        border-radius: 20px;
        padding: 18px 20px;
        font-size: 22px;
        font-weight: 900;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .answer-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 18px 20px;
        margin-top: 12px;
        margin-bottom: 18px;
    }

    .answer-word {
        font-size: 34px;
        font-weight: 900;
        color: #111827;
    }

    .answer-meaning {
        font-size: 18px;
        font-weight: 800;
        color: #475569;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 28px;
        padding: 30px 34px;
        margin-bottom: 26px;
        border: 1px solid #bbf7d0;
        box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    }

    .score-title {
        font-size: 38px;
        font-weight: 900;
        color: #14532d;
        margin-bottom: 10px;
    }

    .score-text {
        font-size: 19px;
        font-weight: 800;
        color: #374151;
        line-height: 1.8;
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
        min-width: 44px;
        background: #fef3c7;
        color: #92400e;
        border-radius: 999px;
        padding: 5px 10px;
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

    .review-user {
        font-size: 15px;
        font-weight: 700;
        color: #6b7280;
    }

    .correct-mark {
        color: #15803d;
        font-weight: 900;
    }

    .wrong-mark {
        color: #b91c1c;
        font-weight: 900;
    }

    div[data-testid="stRadio"] > label {
        font-weight: 900;
        color: #374151;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        border: 1px solid #d1d5db;
        padding: 0.55rem 1.2rem;
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
st.markdown("<div class='main-title'>🛟 Survival English 500 Test</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>이모지와 한국어 뜻을 보고 알맞은 영어 단어를 고르는 50문제 테스트입니다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🎧 테스트 방법</div>
        <div class="hero-text">
            • 문제는 <b>이모지 + 한국어 뜻</b>으로 나옵니다.<br>
            • 알맞은 <b>영어 단어</b>를 고르세요.<br>
            • 한 문제씩 풀고, 제출 후 <b>정답 발음</b>을 들을 수 있습니다.<br>
            • 총 <b>50문제</b>이며, 테마는 섞여서 랜덤으로 나옵니다.<br>
            • 마지막에 <b>점수와 오답 기록</b>을 확인할 수 있습니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS 함수
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
def audio_button(label, text, height=54):
    audio_bytes = make_tts_audio(text)
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    audio_id = f"audio_{uuid.uuid4().hex}"
    play_btn_id = f"play_btn_{uuid.uuid4().hex}"
    stop_btn_id = f"stop_btn_{uuid.uuid4().hex}"
    player_id = f"player_{uuid.uuid4().hex}"
    status_id = f"status_{uuid.uuid4().hex}"

    safe_label = json.dumps(label)
    safe_player_id = json.dumps(player_id)

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; gap:10px; height:46px;">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #dcfce7, #dbeafe);
                border: 1px solid #bbf7d0;
                border-radius: 999px;
                padding: 8px 14px;
                font-weight: 800;
                font-size: 14px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.06);
                white-space: nowrap;
            ">
                {label}
            </button>

            <button id="{stop_btn_id}" style="
                background: #fff7ed;
                border: 1px solid #fed7aa;
                border-radius: 999px;
                padding: 8px 14px;
                font-weight: 800;
                font-size: 14px;
                color: #9a3412;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.04);
                white-space: nowrap;
            ">
                ⏹ 중지
            </button>

            <span id="{status_id}" style="
                font-size: 13px;
                color: #075985;
                font-weight: 700;
                white-space: nowrap;
            "></span>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");
            const playerId = {safe_player_id};
            const labelText = {safe_label};

            const channel = new BroadcastChannel("survival_test_audio_channel");

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

all_word_texts = [item["word"] for item in all_words]

# =========================
# 세션 초기화
# =========================
def start_new_test():
    questions = random.sample(all_words, 50)

    st.session_state.test_questions = questions
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.submitted = False
    st.session_state.selected_answer = None
    st.session_state.test_started = True
    st.session_state.test_finished = False

    # 문제별 보기 고정
    st.session_state.options_by_question = []

    for q in questions:
        distractors = [w for w in all_word_texts if w != q["word"]]
        wrongs = random.sample(distractors, 3)
        options = [q["word"]] + wrongs
        random.shuffle(options)
        st.session_state.options_by_question.append(options)


if "test_started" not in st.session_state:
    st.session_state.test_started = False

if "test_finished" not in st.session_state:
    st.session_state.test_finished = False

# =========================
# 시작 화면
# =========================
if not st.session_state.test_started:
    st.markdown("### 🧪 테스트를 시작해 봅시다")
    st.write("총 50문제가 랜덤으로 출제됩니다. 한 문제씩 풀고 정답 발음을 확인할 수 있습니다.")

    if st.button("🚀 50문제 테스트 시작하기"):
        start_new_test()
        st.rerun()

# =========================
# 테스트 진행 화면
# =========================
elif st.session_state.test_started and not st.session_state.test_finished:
    questions = st.session_state.test_questions
    idx = st.session_state.current_index
    q = questions[idx]
    options = st.session_state.options_by_question[idx]

    st.markdown('<div class="question-card">', unsafe_allow_html=True)

    st.markdown(
        f"""
        <span class="progress-badge">{idx + 1} / 50</span>
        <span class="theme-badge">{q['theme']}</span>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<div class='emoji-box'>{q['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='korean-meaning'>{q['meaning']}</div>", unsafe_allow_html=True)
    st.markdown("<div class='instruction'>알맞은 영어 단어를 고르세요.</div>", unsafe_allow_html=True)

    selected = st.radio(
        "보기",
        options,
        index=None,
        key=f"question_{idx}"
    )

    st.session_state.selected_answer = selected

    if not st.session_state.submitted:
        if st.button("✅ 제출하기", key=f"submit_{idx}"):
            if selected is None:
                st.warning("답을 먼저 선택해 주세요.")
            else:
                is_correct = selected == q["word"]

                if is_correct:
                    st.session_state.score += 1

                st.session_state.answers.append({
                    "number": idx + 1,
                    "theme": q["theme"],
                    "emoji": q["emoji"],
                    "meaning": q["meaning"],
                    "correct_word": q["word"],
                    "user_answer": selected,
                    "is_correct": is_correct
                })

                st.session_state.submitted = True
                st.rerun()

    else:
        last = st.session_state.answers[-1]

        if last["is_correct"]:
            st.markdown("<div class='result-correct'>🎉 정답입니다!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-wrong'>🍊 아쉬워요. 다시 확인해 봅시다.</div>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="answer-box">
                <div class="answer-word">{q['emoji']} {q['word']}</div>
                <div class="answer-meaning">{q['meaning']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        audio_button("🔊 정답 발음 듣기", q["word"])

        col1, col2 = st.columns([1, 4])

        with col1:
            if idx < 49:
                if st.button("➡️ 다음 문제", key=f"next_{idx}"):
                    st.session_state.current_index += 1
                    st.session_state.submitted = False
                    st.session_state.selected_answer = None
                    st.rerun()
            else:
                if st.button("🏁 결과 보기", key="finish_test"):
                    st.session_state.test_finished = True
                    st.rerun()

        with col2:
            st.markdown(
                f"현재 점수: **{st.session_state.score} / {idx + 1}점**"
            )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 결과 화면
# =========================
else:
    score = st.session_state.score
    total = 50
    percent = round(score / total * 100, 1)

    if score >= 45:
        message = "🌟 훌륭합니다! 생존 영어 단어를 아주 잘 알고 있습니다."
    elif score >= 35:
        message = "👍 좋습니다! 조금만 더 복습하면 안정적입니다."
    elif score >= 25:
        message = "🌱 괜찮습니다. 틀린 단어 위주로 다시 연습해 봅시다."
    else:
        message = "🛟 아직 시작 단계입니다. 발음 듣기와 단어 복습을 반복해 봅시다."

    st.markdown(
        f"""
        <div class="score-box">
            <div class="score-title">🏆 최종 점수: {score} / {total}점</div>
            <div class="score-text">
                정답률: {percent}%<br>
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🔄 다시 50문제 풀기"):
            start_new_test()
            st.rerun()

    with col2:
        if st.button("🧹 처음 화면으로"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("### 📋 전체 기록")

    for item in st.session_state.answers:
        mark = "✅" if item["is_correct"] else "❌"
        mark_class = "correct-mark" if item["is_correct"] else "wrong-mark"

        st.markdown('<div class="review-card">', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="review-line">
                <div class="review-num">{item['number']}</div>
                <div class="review-emoji">{item['emoji']}</div>
                <div class="review-ko">{item['meaning']}</div>
                <div class="review-en">{item['correct_word']}</div>
                <div class="{mark_class}">{mark}</div>
                <div class="review-user">내 답: {item['user_answer']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
