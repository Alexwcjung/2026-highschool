import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="기초 문법 확장 말하기 문제", page_icon="🎤", layout="centered")

# =========================================================
# 디자인 CSS
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #fffdfc;
    }

    .title-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #fff7ed 50%, #f7fee7 100%);
        padding: 32px 28px;
        border-radius: 30px;
        margin-bottom: 26px;
        box-shadow: 0 10px 26px rgba(80, 80, 120, 0.12);
        text-align: center;
        border: 1.5px solid #e0f2fe;
    }

    .title-box h1 {
        color: #334155;
        margin-bottom: 10px;
        font-size: 36px;
        font-weight: 900;
    }

    .title-box p {
        color: #64748b;
        font-size: 19px;
        margin: 0;
        line-height: 1.7;
    }

    .guide-card {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 24px;
        padding: 22px 24px;
        margin: 16px 0 24px 0;
        box-shadow: 0 5px 16px rgba(0,0,0,0.055);
        border: 1.5px solid #edf2ff;
    }

    .guide-card p {
        font-size: 20px;
        line-height: 1.75;
        color: #374151;
        margin: 0;
    }

    .practice-card {
        background: linear-gradient(135deg, #ffffff, #fff7ed);
        border-radius: 30px;
        padding: 34px 28px;
        margin: 20px 0;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        border: 1.5px solid #fed7aa;
        text-align: center;
    }

    .practice-card .category {
        font-size: 19px;
        color: #9a3412;
        font-weight: 900;
        margin-bottom: 14px;
    }

    .practice-card .label {
        font-size: 21px;
        color: #475569;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .practice-card .korean {
        font-size: 34px;
        color: #111827;
        font-weight: 900;
        margin: 14px 0;
        line-height: 1.45;
    }

    .answer-card {
        background: linear-gradient(135deg, #eef7ff, #ffffff);
        border-radius: 26px;
        padding: 28px 24px;
        margin: 20px 0;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
        border: 1.5px solid #dbeafe;
        text-align: center;
    }

    .answer-card p {
        font-size: 21px;
        color: #475569;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .answer-card h2 {
        color: #2563eb;
        font-size: 34px;
        font-weight: 900;
        margin: 8px 0;
        line-height: 1.35;
    }

    div[data-testid="stAlert"] {
        border-radius: 18px;
        font-size: 18px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        padding: 0.45rem 1.1rem;
        border: 1.5px solid #d9e7ff;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        color: #2563eb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 제목
# =========================================================
st.markdown(
    """
    <div class="title-box">
        <h1>🎤 기초 문법 확장 말하기 문제</h1>
        <p>한국어 문장을 보고 영어로 먼저 말해 본 뒤, 정답과 원어민 발음을 확인해 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("사용 방법: ① 문법 선택 → ② 한국어 문장 보고 영어로 말하기 → ③ 정답 보기 → ④ 원어민 발음 듣기")

st.markdown(
    """
    <div class="guide-card">
        <p>
            처음에는 <b>영어 정답이 보이지 않습니다.</b><br>
            한국어 문장만 보고 먼저 영어로 말해 본 뒤, <b>정답 보기</b>를 눌러 확인하세요.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# TTS 함수
# =========================================================
def make_tts_audio(text):
    tts = gTTS(text=text, lang="en", tld="com")
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp


# =========================================================
# 말하기 문제
# =========================================================
speaking_questions = [
    # can
    {
        "category": "💪 can 조동사",
        "korean": "나는 수영할 수 있다.",
        "sentence": "I can swim."
    },
    {
        "category": "💪 can 조동사",
        "korean": "그녀는 노래할 수 있다.",
        "sentence": "She can sing."
    },
    {
        "category": "💪 can 조동사",
        "korean": "그들은 축구를 할 수 있다.",
        "sentence": "They can play soccer."
    },
    {
        "category": "💪 can 조동사",
        "korean": "나는 수영할 수 없다.",
        "sentence": "I cannot swim."
    },
    {
        "category": "💪 can 조동사",
        "korean": "너는 수영할 수 있니?",
        "sentence": "Can you swim?"
    },
    {
        "category": "💪 can 조동사",
        "korean": "그녀는 피아노를 칠 수 있니?",
        "sentence": "Can she play the piano?"
    },

    # 명령문
    {
        "category": "📢 명령문",
        "korean": "문을 열어라.",
        "sentence": "Open the door."
    },
    {
        "category": "📢 명령문",
        "korean": "주의 깊게 들어라.",
        "sentence": "Listen carefully."
    },
    {
        "category": "📢 명령문",
        "korean": "일어서라.",
        "sentence": "Stand up."
    },
    {
        "category": "📢 명령문",
        "korean": "교실에서 뛰지 마라.",
        "sentence": "Don't run in the classroom."
    },
    {
        "category": "📢 명령문",
        "korean": "이것을 만지지 마라.",
        "sentence": "Don't touch this."
    },
    {
        "category": "📢 명령문",
        "korean": "늦지 마라.",
        "sentence": "Don't be late."
    },

    # There is / There are
    {
        "category": "📍 There is / are",
        "korean": "책상 위에 책 한 권이 있다.",
        "sentence": "There is a book on the desk."
    },
    {
        "category": "📍 There is / are",
        "korean": "교실에 학생 한 명이 있다.",
        "sentence": "There is a student in the classroom."
    },
    {
        "category": "📍 There is / are",
        "korean": "탁자 아래에 개 한 마리가 있다.",
        "sentence": "There is a dog under the table."
    },
    {
        "category": "📍 There is / are",
        "korean": "책상 위에 책 두 권이 있다.",
        "sentence": "There are two books on the desk."
    },
    {
        "category": "📍 There is / are",
        "korean": "교실에 학생 세 명이 있다.",
        "sentence": "There are three students in the classroom."
    },
    {
        "category": "📍 There is / are",
        "korean": "거리에 많은 자동차들이 있다.",
        "sentence": "There are many cars on the street."
    },

    # 전치사
    {
        "category": "🧭 전치사",
        "korean": "고양이는 상자 안에 있다.",
        "sentence": "The cat is in the box."
    },
    {
        "category": "🧭 전치사",
        "korean": "책은 책상 위에 있다.",
        "sentence": "The book is on the desk."
    },
    {
        "category": "🧭 전치사",
        "korean": "공은 의자 아래에 있다.",
        "sentence": "The ball is under the chair."
    },
    {
        "category": "🧭 전치사",
        "korean": "학교는 공원 옆에 있다.",
        "sentence": "The school is next to the park."
    },
    {
        "category": "🧭 전치사",
        "korean": "개는 문 뒤에 있다.",
        "sentence": "The dog is behind the door."
    },
    {
        "category": "🧭 전치사",
        "korean": "버스 정류장은 학교 앞에 있다.",
        "sentence": "The bus stop is in front of the school."
    },

    # want
    {
        "category": "💭 want",
        "korean": "나는 물을 원한다.",
        "sentence": "I want water."
    },
    {
        "category": "💭 want",
        "korean": "너는 피자를 원한다.",
        "sentence": "You want pizza."
    },
    {
        "category": "💭 want",
        "korean": "그들은 새 휴대전화를 원한다.",
        "sentence": "They want a new phone."
    },
    {
        "category": "💭 want",
        "korean": "그는 물을 원한다.",
        "sentence": "He wants water."
    },
    {
        "category": "💭 want",
        "korean": "그녀는 자전거를 원한다.",
        "sentence": "She wants a bike."
    },
    {
        "category": "💭 want",
        "korean": "내 남동생은 피자를 원한다.",
        "sentence": "My brother wants pizza."
    },

    # want to
    {
        "category": "🚀 want to",
        "korean": "나는 먹고 싶다.",
        "sentence": "I want to eat."
    },
    {
        "category": "🚀 want to",
        "korean": "나는 집에 가고 싶다.",
        "sentence": "I want to go home."
    },
    {
        "category": "🚀 want to",
        "korean": "우리는 축구를 하고 싶다.",
        "sentence": "We want to play soccer."
    },
    {
        "category": "🚀 want to",
        "korean": "그들은 영어를 공부하고 싶다.",
        "sentence": "They want to study English."
    },
    {
        "category": "🚀 want to",
        "korean": "그는 축구를 하고 싶다.",
        "sentence": "He wants to play soccer."
    },
    {
        "category": "🚀 want to",
        "korean": "그녀는 노래하고 싶다.",
        "sentence": "She wants to sing."
    },
    {
        "category": "🚀 want to",
        "korean": "내 여동생은 TV를 보고 싶다.",
        "sentence": "My sister wants to watch TV."
    },
    {
        "category": "🚀 want to",
        "korean": "나는 물을 마시고 싶다.",
        "sentence": "I want to drink water."
    },
    {
        "category": "🚀 want to",
        "korean": "그녀는 자전거를 타고 싶다.",
        "sentence": "She wants to ride a bike."
    },

    # have / has
    {
        "category": "🎒 have / has",
        "korean": "나는 자전거를 가지고 있다.",
        "sentence": "I have a bike."
    },
    {
        "category": "🎒 have / has",
        "korean": "너는 휴대전화를 가지고 있다.",
        "sentence": "You have a phone."
    },
    {
        "category": "🎒 have / has",
        "korean": "우리는 많은 책을 가지고 있다.",
        "sentence": "We have many books."
    },
    {
        "category": "🎒 have / has",
        "korean": "그들은 개 한 마리를 가지고 있다.",
        "sentence": "They have a dog."
    },
    {
        "category": "🎒 have / has",
        "korean": "그는 자전거를 가지고 있다.",
        "sentence": "He has a bike."
    },
    {
        "category": "🎒 have / has",
        "korean": "그녀는 개 한 마리를 가지고 있다.",
        "sentence": "She has a dog."
    },
    {
        "category": "🎒 have / has",
        "korean": "내 친구는 새 휴대전화를 가지고 있다.",
        "sentence": "My friend has a new phone."
    },
    {
        "category": "🎒 have / has",
        "korean": "그 학교는 체육관을 가지고 있다.",
        "sentence": "The school has a gym."
    },

    # 문장 연결하기 - because
    {
        "category": "🔗 because",
        "korean": "나는 영어를 좋아한다. 왜냐하면 재미있기 때문이다.",
        "sentence": "I like English because it is fun."
    },
    {
        "category": "🔗 because",
        "korean": "그녀는 행복하다. 왜냐하면 개를 가지고 있기 때문이다.",
        "sentence": "She is happy because she has a dog."
    },
    {
        "category": "🔗 because",
        "korean": "나는 물을 원한다. 왜냐하면 목이 마르기 때문이다.",
        "sentence": "I want water because I am thirsty."
    },

    # 문장 연결하기 - so
    {
        "category": "🔗 so",
        "korean": "나는 배고프다. 그래서 피자를 원한다.",
        "sentence": "I am hungry, so I want pizza."
    },
    {
        "category": "🔗 so",
        "korean": "날씨가 춥다. 그래서 나는 재킷을 입는다.",
        "sentence": "It is cold, so I wear a jacket."
    },
    {
        "category": "🔗 so",
        "korean": "그는 피곤하다. 그래서 집에 간다.",
        "sentence": "He is tired, so he goes home."
    },

    # 문장 연결하기 - but
    {
        "category": "🔗 but",
        "korean": "나는 축구를 좋아한다. 하지만 야구는 좋아하지 않는다.",
        "sentence": "I like soccer, but I don't like baseball."
    },
    {
        "category": "🔗 but",
        "korean": "그녀는 노래할 수 있다. 하지만 춤은 출 수 없다.",
        "sentence": "She can sing, but she can't dance."
    },
    {
        "category": "🔗 but",
        "korean": "나는 자전거를 가지고 있다. 하지만 자동차는 가지고 있지 않다.",
        "sentence": "I have a bike, but I don't have a car."
    },

    # 문장 연결하기 - if
    {
        "category": "🔗 if",
        "korean": "만약 비가 오면, 나는 집에 있을 것이다.",
        "sentence": "If it rains, I will stay home."
    },
    {
        "category": "🔗 if",
        "korean": "만약 내가 배고프면, 나는 피자를 먹을 것이다.",
        "sentence": "If I am hungry, I will eat pizza."
    },
    {
        "category": "🔗 if",
        "korean": "만약 네가 도움이 필요하면, 내가 도와줄 수 있다.",
        "sentence": "If you need help, I can help you."
    },
]


# =========================================================
# 선택 영역
# =========================================================
categories = ["전체"] + list(dict.fromkeys([q["category"] for q in speaking_questions]))

selected_category = st.selectbox(
    "연습할 문법을 고르세요.",
    categories
)

if selected_category == "전체":
    filtered_questions = speaking_questions
else:
    filtered_questions = [
        q for q in speaking_questions
        if q["category"] == selected_category
    ]

question_labels = [
    f"{i + 1}. {q['korean']}"
    for i, q in enumerate(filtered_questions)
]

selected_label = st.selectbox(
    "연습할 문제를 고르세요.",
    question_labels
)

selected_index = question_labels.index(selected_label)
current_q = filtered_questions[selected_index]

# 문제를 바꾸면 정답 다시 숨기기
question_key = current_q["category"] + current_q["korean"]

if "last_question_key" not in st.session_state:
    st.session_state.last_question_key = question_key

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if st.session_state.last_question_key != question_key:
    st.session_state.show_answer = False
    st.session_state.last_question_key = question_key

st.markdown("---")


# =========================================================
# 문제 카드: 한국어만 제시
# =========================================================
st.markdown(
    f"""
    <div class="practice-card">
        <p class="category">{current_q["category"]}</p>
        <p class="label">한국어 문장</p>
        <div class="korean">{current_q["korean"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="guide-card">
        <p>
            위 한국어 문장을 보고 <b>영어로 먼저 말해 보세요.</b><br>
            말한 뒤에 아래의 <b>정답 보기</b> 버튼을 눌러 확인합니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 정답 보기 + 원어민 발음
# =========================================================
if st.button("✅ 정답 보기"):
    st.session_state.show_answer = True

if st.session_state.show_answer:
    st.markdown(
        f"""
        <div class="answer-card">
            <p>정답 문장</p>
            <h2>{current_q["sentence"]}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🔊 원어민 발음")

    audio = make_tts_audio(current_q["sentence"])
    st.audio(audio, format="audio/mp3")

st.markdown("---")


# =========================================================
# 버튼
# =========================================================
col1, col2 = st.columns(2)

with col1:
    if st.button("🙈 정답 가리기"):
        st.session_state.show_answer = False
        st.rerun()

with col2:
    if st.button("🔄 다시 연습하기"):
        st.session_state.show_answer = False
        st.rerun()
