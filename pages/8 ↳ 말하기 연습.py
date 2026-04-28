import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="문장 구조 말하기 문제", page_icon="🎤", layout="centered")

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
        background: linear-gradient(135deg, #fff7ed 0%, #fffdf7 50%, #eef7ff 100%);
        padding: 32px 28px;
        border-radius: 30px;
        margin-bottom: 26px;
        box-shadow: 0 10px 26px rgba(80, 80, 120, 0.12);
        text-align: center;
        border: 1.5px solid #fed7aa;
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
        font-size: 36px;
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
        <h1>🎤 문장 구조 말하기 문제</h1>
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
    {
        "category": "🌱 Be동사",
        "korean": "나는 학생이다.",
        "sentence": "I am a student."
    },
    {
        "category": "🌱 Be동사",
        "korean": "그녀는 행복하다.",
        "sentence": "She is happy."
    },
    {
        "category": "🌱 Be동사",
        "korean": "그는 친절하다.",
        "sentence": "He is kind."
    },
    {
        "category": "🌱 Be동사",
        "korean": "그들은 바쁘다.",
        "sentence": "They are busy."
    },
    {
        "category": "🌱 Be동사",
        "korean": "우리는 학생들이다.",
        "sentence": "We are students."
    },

    {
        "category": "🏃 현재진행형",
        "korean": "나는 점심을 먹고 있다.",
        "sentence": "I am eating lunch."
    },
    {
        "category": "🏃 현재진행형",
        "korean": "그녀는 책을 읽고 있다.",
        "sentence": "She is reading a book."
    },
    {
        "category": "🏃 현재진행형",
        "korean": "그들은 축구를 하고 있다.",
        "sentence": "They are playing soccer."
    },
    {
        "category": "🏃 현재진행형",
        "korean": "그는 음악을 듣고 있다.",
        "sentence": "He is listening to music."
    },
    {
        "category": "🏃 현재진행형",
        "korean": "우리는 영어를 공부하고 있다.",
        "sentence": "We are studying English."
    },

    {
        "category": "🚀 미래형 will",
        "korean": "나는 영어를 공부할 것이다.",
        "sentence": "I will study English."
    },
    {
        "category": "🚀 미래형 will",
        "korean": "그녀는 나에게 전화할 것이다.",
        "sentence": "She will call me."
    },
    {
        "category": "🚀 미래형 will",
        "korean": "우리는 부산에 갈 것이다.",
        "sentence": "We will go to Busan."
    },
    {
        "category": "🚀 미래형 will",
        "korean": "그는 축구를 할 것이다.",
        "sentence": "He will play soccer."
    },

    {
        "category": "🚀 미래형 be going to",
        "korean": "나는 영어를 공부할 예정이다.",
        "sentence": "I am going to study English."
    },
    {
        "category": "🚀 미래형 be going to",
        "korean": "그녀는 나에게 전화할 예정이다.",
        "sentence": "She is going to call me."
    },
    {
        "category": "🚀 미래형 be going to",
        "korean": "우리는 부산에 갈 예정이다.",
        "sentence": "We are going to go to Busan."
    },
    {
        "category": "🚀 미래형 be going to",
        "korean": "그들은 축구를 할 예정이다.",
        "sentence": "They are going to play soccer."
    },

    {
        "category": "🕰️ 과거형",
        "korean": "나는 어제 축구를 했다.",
        "sentence": "I played soccer yesterday."
    },
    {
        "category": "🕰️ 과거형",
        "korean": "그녀는 학교에 걸어갔다.",
        "sentence": "She walked to school."
    },
    {
        "category": "🕰️ 과거형",
        "korean": "우리는 방을 청소했다.",
        "sentence": "We cleaned the room."
    },
    {
        "category": "🕰️ 과거형",
        "korean": "나는 어제 점심을 먹었다.",
        "sentence": "I ate lunch yesterday."
    },
    {
        "category": "🕰️ 과거형",
        "korean": "그는 학교에 갔다.",
        "sentence": "He went to school."
    },

    {
        "category": "❌ 부정문",
        "korean": "나는 학생이 아니다.",
        "sentence": "I am not a student."
    },
    {
        "category": "❌ 부정문",
        "korean": "그녀는 행복하지 않다.",
        "sentence": "She is not happy."
    },
    {
        "category": "❌ 부정문",
        "korean": "그들은 바쁘지 않다.",
        "sentence": "They are not busy."
    },
    {
        "category": "❌ 부정문",
        "korean": "나는 커피를 좋아하지 않는다.",
        "sentence": "I do not like coffee."
    },
    {
        "category": "❌ 부정문",
        "korean": "그는 축구를 하지 않는다.",
        "sentence": "He does not play soccer."
    },
    {
        "category": "❌ 부정문",
        "korean": "그들은 어제 학교에 가지 않았다.",
        "sentence": "They did not go to school yesterday."
    },

    {
        "category": "❓ 의문문",
        "korean": "너는 학생이니?",
        "sentence": "Are you a student?"
    },
    {
        "category": "❓ 의문문",
        "korean": "그녀는 행복하니?",
        "sentence": "Is she happy?"
    },
    {
        "category": "❓ 의문문",
        "korean": "그들은 교실에 있니?",
        "sentence": "Are they in the classroom?"
    },
    {
        "category": "❓ 의문문",
        "korean": "너는 커피를 좋아하니?",
        "sentence": "Do you like coffee?"
    },
    {
        "category": "❓ 의문문",
        "korean": "그는 축구를 하니?",
        "sentence": "Does he play soccer?"
    },
    {
        "category": "❓ 의문문",
        "korean": "그들은 어제 학교에 갔니?",
        "sentence": "Did they go to school yesterday?"
    },

    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 무엇을 좋아하니?",
        "sentence": "What do you like?"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 언제 일어나니?",
        "sentence": "When do you get up?"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 어디에 사니?",
        "sentence": "Where do you live?"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 왜 행복하니?",
        "sentence": "Why are you happy?"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 어떻게 학교에 가니?",
        "sentence": "How do you go to school?"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "그는 누구니?",
        "sentence": "Who is he?"
    },
]


# =========================================================
# 선택 영역
# =========================================================
categories = ["전체"] + sorted(list(set([q["category"] for q in speaking_questions])))

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
