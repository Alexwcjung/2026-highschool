import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="문장 구조 말하기 문제", page_icon="🎤", layout="centered")

st.subheader("🎤 문장 구조 말하기 문제")

st.markdown(
    """
    <div style="
        background:linear-gradient(135deg,#fff7ed,#ffffff);
        border-radius:28px;
        padding:28px;
        margin:18px 0;
        box-shadow:0 8px 22px rgba(0,0,0,0.07);
        border:1.5px solid #fed7aa;
    ">
        <h3 style="color:#c2410c;">🎤 문장을 듣고 따라 말하기</h3>
        <p style="font-size:20px; line-height:1.7;">
            아래 문장을 보고, 먼저 <b>원어민 발음</b>을 들어 보세요.<br>
            그다음 직접 문장을 읽고 녹음해서 자신의 발음을 확인해 봅시다.
        </p>
        <div style="
            background:rgba(255,255,255,0.85);
            padding:18px 20px;
            border-radius:22px;
            font-size:25px;
            font-weight:900;
            text-align:center;
            margin-top:16px;
            color:#c2410c;
        ">
            듣기 → 따라 말하기 → 내 발음 확인하기
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("사용 방법: ① 문장 선택 → ② 원어민 발음 듣기 → ③ 직접 말하기 → ④ 녹음한 내 목소리 다시 듣기")


def make_tts_audio(text):
    tts = gTTS(text=text, lang="en", tld="com")
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp


speaking_questions = [
    {
        "category": "🌱 Be동사",
        "korean": "나는 학생이다.",
        "sentence": "I am a student.",
        "hint": "I + am + a student"
    },
    {
        "category": "🌱 Be동사",
        "korean": "그녀는 행복하다.",
        "sentence": "She is happy.",
        "hint": "She + is + happy"
    },
    {
        "category": "🌱 Be동사",
        "korean": "그들은 바쁘다.",
        "sentence": "They are busy.",
        "hint": "They + are + busy"
    },
    {
        "category": "🏃 현재진행형",
        "korean": "나는 점심을 먹고 있다.",
        "sentence": "I am eating lunch.",
        "hint": "am + eating"
    },
    {
        "category": "🏃 현재진행형",
        "korean": "그녀는 책을 읽고 있다.",
        "sentence": "She is reading a book.",
        "hint": "is + reading"
    },
    {
        "category": "🏃 현재진행형",
        "korean": "그들은 축구를 하고 있다.",
        "sentence": "They are playing soccer.",
        "hint": "are + playing"
    },
    {
        "category": "🚀 미래형 will",
        "korean": "나는 영어를 공부할 것이다.",
        "sentence": "I will study English.",
        "hint": "will + study"
    },
    {
        "category": "🚀 미래형 will",
        "korean": "그녀는 나에게 전화할 것이다.",
        "sentence": "She will call me.",
        "hint": "will + call"
    },
    {
        "category": "🚀 미래형 be going to",
        "korean": "나는 영어를 공부할 예정이다.",
        "sentence": "I am going to study English.",
        "hint": "am going to + study"
    },
    {
        "category": "🚀 미래형 be going to",
        "korean": "우리는 부산에 갈 예정이다.",
        "sentence": "We are going to go to Busan.",
        "hint": "are going to + go"
    },
    {
        "category": "🕰️ 과거형",
        "korean": "나는 어제 축구를 했다.",
        "sentence": "I played soccer yesterday.",
        "hint": "played + yesterday"
    },
    {
        "category": "🕰️ 과거형",
        "korean": "그녀는 학교에 걸어갔다.",
        "sentence": "She walked to school.",
        "hint": "walked"
    },
    {
        "category": "❌ 부정문",
        "korean": "나는 학생이 아니다.",
        "sentence": "I am not a student.",
        "hint": "am not"
    },
    {
        "category": "❌ 부정문",
        "korean": "나는 커피를 좋아하지 않는다.",
        "sentence": "I do not like coffee.",
        "hint": "do not + like"
    },
    {
        "category": "❓ 의문문",
        "korean": "너는 학생이니?",
        "sentence": "Are you a student?",
        "hint": "Are + you"
    },
    {
        "category": "❓ 의문문",
        "korean": "너는 커피를 좋아하니?",
        "sentence": "Do you like coffee?",
        "hint": "Do + you + like"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 무엇을 좋아하니?",
        "sentence": "What do you like?",
        "hint": "What + do you like"
    },
    {
        "category": "🕵️ 의문사 의문문",
        "korean": "너는 어떻게 학교에 가니?",
        "sentence": "How do you go to school?",
        "hint": "How + do you go"
    },
]

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
    f"{i + 1}. {q['korean']}  →  {q['sentence']}"
    for i, q in enumerate(filtered_questions)
]

selected_label = st.selectbox(
    "연습할 문장을 고르세요.",
    question_labels
)

selected_index = question_labels.index(selected_label)
current_q = filtered_questions[selected_index]

st.markdown("---")

st.markdown(
    f"""
    <div style="
        background:linear-gradient(135deg,#ffffff,#fff7ed);
        border-radius:28px;
        padding:28px;
        margin:18px 0;
        box-shadow:0 8px 22px rgba(0,0,0,0.07);
        border:1.5px solid #fed7aa;
        text-align:center;
    ">
        <p style="font-size:19px; color:#9a3412; font-weight:800; margin-bottom:8px;">
            {current_q["category"]}
        </p>
        <p style="font-size:22px; color:#374151; margin-bottom:10px;">
            한국어 뜻
        </p>
        <h2 style="font-size:30px; color:#111827; margin:8px 0 22px 0;">
            {current_q["korean"]}
        </h2>
        <p style="font-size:22px; color:#374151; margin-bottom:10px;">
            영어 문장
        </p>
        <h1 style="font-size:36px; color:#ea580c; margin:8px 0;">
            {current_q["sentence"]}
        </h1>
        <p style="font-size:18px; color:#6b7280; margin-top:18px;">
            힌트: <b>{current_q["hint"]}</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 🔊 1. 원어민 발음 듣기")

if st.button("🔊 원어민 발음 듣기"):
    audio = make_tts_audio(current_q["sentence"])
    st.audio(audio, format="audio/mp3")

st.markdown("---")

st.markdown("### 🎙️ 2. 직접 말하고 녹음하기")

st.markdown(
    """
    <div style="
        background:linear-gradient(135deg,#ffffff,#fbfdff);
        border-radius:24px;
        padding:22px 24px;
        margin:14px 0;
        box-shadow:0 5px 16px rgba(0,0,0,0.055);
        border:1.5px solid #edf2ff;
    ">
        <p style="font-size:20px; line-height:1.75; color:#374151;">
            위 문장을 보고 직접 말해 보세요.<br>
            녹음한 뒤, 자신의 발음을 다시 들어 보며 원어민 발음과 비교합니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

recorded_audio = st.audio_input("🎙️ 여기를 눌러 문장을 직접 말해 보세요.")

if recorded_audio:
    st.success("녹음이 완료되었습니다! 아래에서 자신의 발음을 다시 들어 보세요.")
    st.audio(recorded_audio)

st.markdown("---")

st.markdown("### ✅ 3. 발음 자기 점검")

st.markdown(
    """
    <div style="
        background:linear-gradient(135deg,#ffffff,#fbfdff);
        border-radius:24px;
        padding:22px 24px;
        margin:14px 0;
        box-shadow:0 5px 16px rgba(0,0,0,0.055);
        border:1.5px solid #edf2ff;
    ">
        <p style="font-size:20px;"><b>아래 항목을 스스로 확인해 봅시다.</b></p>
        <p style="font-size:20px;">① 문장을 끝까지 말했나요?</p>
        <p style="font-size:20px;">② 중요한 단어를 또렷하게 말했나요?</p>
        <p style="font-size:20px;">③ 원어민 발음과 비슷한 리듬으로 말했나요?</p>
        <p style="font-size:20px;">④ 너무 빠르거나 너무 느리지 않았나요?</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    check1 = st.checkbox("끝까지 말함")
with col2:
    check2 = st.checkbox("또렷하게 말함")
with col3:
    check3 = st.checkbox("리듬 자연스러움")
with col4:
    check4 = st.checkbox("속도 적절함")

checked_count = sum([check1, check2, check3, check4])

if checked_count == 4:
    st.success("훌륭합니다! 자신 있게 말했어요 🎉")
    st.balloons()
elif checked_count >= 2:
    st.info("좋아요! 원어민 발음을 한 번 더 듣고 다시 말해 봅시다.")
elif checked_count >= 1:
    st.warning("괜찮아요. 천천히 한 단어씩 다시 말해 봅시다.")
else:
    st.caption("체크박스를 눌러 자신의 발음을 점검해 보세요.")
