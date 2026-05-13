import streamlit as st
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Pop Song Listening",
    page_icon="🎵",
    layout="wide"
)

# =========================
# 디자인 (CSS)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff7ed 0%, #fefce8 45%, #ecfdf5 100%);
}
.title-box {
    background: linear-gradient(135deg, #f59e0b, #22c55e);
    padding: 26px;
    border-radius: 26px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
.card {
    background: white;
    padding: 22px;
    border-radius: 22px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 5px 14px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}
.lyrics-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #f59e0b;
    font-family: 'Courier New', Courier, monospace;
    line-height: 1.6;
    margin-bottom: 20px;
    white-space: pre-wrap;
}
.expression {
    background: #ecfdf5;
    padding: 13px 15px;
    border-radius: 14px;
    margin-bottom: 10px;
    border-left: 6px solid #22c55e;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 제목
# =========================
st.markdown("""
<div class="title-box">
    <h1>🎵 Can You Feel the Love Tonight</h1>
    <h3>Pop Song Listening Activity</h3>
</div>
""", unsafe_allow_html=True)

# =========================
# 자료 설정 (가사 1절 반영)
# =========================
video_url = "https://www.youtube.com/watch?v=25QyCxVkXwQ" # 라이온킹 OST 공식 링크 예시

# 1절 가사를 그대로 넣었습니다.
song_excerpt = """There's a calm surrender 
To the rush of day
When the heat of a rolling wave 
Can be turned away

An enchanted moment 
And it sees me through
It's enough for this restless warrior 
Just to be with you"""

# =========================
# 탭 구성
# =========================
tab_video, tab_activity, tab_expression, tab_reflection = st.tabs([
    "🎬 동영상 & 가사",
    "🎧 Listening Activity",
    "📘 Key Expressions",
    "✍️ Reflection"
])

# =========================
# 1. 동영상 & 가사 확인
# =========================
with tab_video:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("## 🎬 Watch and Listen")
        if video_url.startswith("http"):
            st.video(video_url)
        else:
            st.info("유튜브 링크를 확인해주세요.")

    with col2:
        st.markdown("## 📜 Lyrics (Verse 1)")
        st.markdown(f'<div class="lyrics-box">{song_excerpt}</div>', unsafe_allow_html=True)
        st.info("위 가사를 읽으며 노래를 들어보세요!")

# =========================
# 2. Listening Activity
# =========================
with tab_activity:
    st.markdown("## 🎧 Listening Activity")

    st.markdown("""
    <div class="card">
    노래 가사와 내용을 떠올리며 알맞은 단어를 고르세요.
    </div>
    """, unsafe_allow_html=True)

    # A. Choose the Correct Word
    st.markdown("### A. Choose the Correct Word")

    q1 = st.radio(
        "1. The song begins with a feeling of quiet __________ (calm surrender).",
        ["peace", "anger", "noise", "fear"],
        key="q1"
    )

    q2 = st.radio(
        "2. The speaker feels an enchanted __________.",
        ["air", "bag", "moment", "phone"],
        key="q2"
    )

    q3 = st.radio(
        "3. The mood of the song is mostly __________.",
        ["romantic", "scary", "funny", "angry"],
        key="q3"
    )

    q4 = st.radio(
        "4. The song talks about love and strong __________.",
        ["feelings", "machines", "tests", "numbers"],
        key="q4"
    )

    q5 = st.radio(
        "5. For the 'restless warrior', it is enough just to be with __________.",
        ["you", "them", "food", "money"],
        key="q5"
    )

    if st.button("A 정답 확인"):
        score = 0
        answers = {
            "q1": ("peace", q1),
            "q2": ("moment", q2),
            "q3": ("romantic", q3),
            "q4": ("feelings", q4),
            "q5": ("you", q5)
        }

        for key, (answer, user_answer) in answers.items():
            if answer == user_answer:
                score += 1

        st.markdown(f"### 점수: {score} / 5")
        if score == 5:
            st.balloons()
            st.success("완벽합니다! 가사를 아주 잘 이해했네요!")
        elif score >= 3:
            st.info("좋습니다. 가사를 다시 한 번 읽어볼까요?")
        else:
            st.warning("노래를 다시 듣고 도전해 봅시다.")

    st.markdown("---")

    # B. Fill in the Blanks
    st.markdown("### B. Fill in the Blanks")
    st.markdown("""
    <div class="card">
    1절 가사에 나온 단어를 골라 빈칸을 채우세요.<br><br>
    <b>[ surrender / rush / enchanted / warrior / moment ]</b>
    </div>
    """, unsafe_allow_html=True)

    b1 = st.text_input("1. There's a calm __________.", key="b1")
    b2 = st.text_input("2. To the __________ of day.", key="b2")
    b3 = st.text_input("3. An __________ moment.", key="b3")
    b4 = st.text_input("4. It's enough for this restless __________.", key="b4")

    if st.button("B 정답 확인"):
        score_b = 0
        correct_b = ["surrender", "rush", "enchanted", "warrior"]
        user_b = [b1, b2, b3, b4]
        
        for i, (ans, user) in enumerate(zip(correct_b, user_b)):
            if user.strip().lower() == ans:
                score_b += 1
                st.success(f"{i+1}번 정답!")
            else:
                st.error(f"{i+1}번 정답: {ans}")

# =========================
# 3. Key Expressions
# =========================
with tab_expression:
    st.markdown("## 📘 Key Expressions")
    expressions = {
        "Calm surrender": "차분한 굴복(평온하게 받아들임)",
        "Rush of day": "낮의 분주함",
        "Enchanted moment": "마법에 걸린 듯한(황홀한) 순간",
        "Restless warrior": "쉼 없는(마음이 불안한) 전사",
        "See me through": "어려움을 헤쳐나가게 해주다"
    }

    for word, meaning in expressions.items():
        st.markdown(
            f'<div class="expression"><b>{word}</b> : {meaning}</div>',
            unsafe_allow_html=True
        )

# =========================
# 4. Reflection
# =========================
with tab_reflection:
    st.markdown("## ✍️ Reflection Writing")
    st.markdown('<div class="card">이 노래의 가사를 읽고 느낀 점을 적어 보세요.</div>', unsafe_allow_html=True)

    reflection = st.text_area(
        "What did you feel from this song?",
        placeholder="I felt calm and warm. / 가사가 너무 아름다워요.",
        height=150
    )

    if st.button("피드백 받기"):
        text = reflection.strip()
        if text == "":
            st.warning("먼저 답을 적어 주세요.")
        else:
            korean_count = sum(1 for ch in text if "가" <= ch <= "힣")
            english_count = sum(1 for ch in text if ch.lower() in "abcdefghijklmnopqrstuvwxyz")

            if korean_count > english_count:
                st.markdown("### 영어로 바꾸면")
                st.success("The lyrics about the 'enchanted moment' were very beautiful. I felt a sense of peace.")
            else:
                st.markdown("### 다듬은 영어")
                st.success("I really liked the part about the 'calm surrender.' It made me feel relaxed and warm.")
