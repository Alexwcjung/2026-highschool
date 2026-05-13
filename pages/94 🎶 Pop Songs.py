import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Pop Song Listening Activity",
    page_icon="🎵",
    layout="wide"
)

# =========================
# CSS 디자인 (탭, 음영, 레이아웃)
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #f8fafc;
}
.title-box {
    background: linear-gradient(135deg, #f59e0b, #22c55e);
    padding: 25px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.lyrics-container {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    line-height: 2.2;
    font-size: 1.1rem;
    color: #1e293b;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}
.highlight-blank {
    background-color: #fef08a; /* 노란색 음영 */
    padding: 2px 10px;
    border-radius: 6px;
    font-weight: bold;
    color: #c2410c;
    border-bottom: 2px solid #f59e0b;
    margin: 0 2px;
}
.expression-card {
    background: #ecfdf5;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    border-left: 5px solid #10b981;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>🎵 Can You Feel the Love Tonight</h1><p>노래를 들으며 노란 음영 속 빈칸의 정답을 맞춰보세요!</p></div>', unsafe_allow_html=True)

# =========================
# 탭 구성[cite: 1]
# =========================
tab_activity, tab_expression, tab_reflection = st.tabs([
    "🎧 Listening Activity",
    "📘 Key Expressions",
    "✍️ Reflection"
])

# =========================
# 1. Listening Activity (영상 + 가사 퀴즈 병렬 배치)[cite: 1]
# =========================
with tab_activity:
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("🎬 Watch & Listen")
        video_url = "https://www.youtube.com/watch?v=25QyCxVkXwQ"
        st.video(video_url)
        st.info("💡 왼쪽 영상을 재생하고, 오른쪽 가사의 흐름(1~5번)을 따라가며 답을 골라보세요.")

    with col2:
        st.subheader("📜 Lyrics & Quiz")
        # 가사 전체 반영 및 주요 지점 음영/번호 처리[cite: 1]
        lyrics_html = """
        <div class="lyrics-container">
            There's a calm <span class="highlight-blank">( 1 )</span><br>
            To the rush of day<br>
            When the heat of the rolling <span class="highlight-blank">( 2 )</span><br>
            Can be turned away<br><br>
            And enchanted moment<br>
            And it sees me through<br>
            It's enough for this restless <span class="highlight-blank">( 3 )</span><br>
            Just to be with you<br><br>
            And can you feel the love tonight?<br>
            It is where we are<br>
            It's enough for this wide-eyed <span class="highlight-blank">( 4 )</span><br>
            That we got this far<br><br>
            ... (중략) ...<br><br>
            It's enough to make kings and <span class="highlight-blank">( 5 )</span><br>
            Believe the very best
        </div>
        """
        st.markdown(lyrics_html, unsafe_allow_html=True)
        
        st.write("---")
        
        # 1~5번 퀴즈 (들리는 대로 고르기)[cite: 1]
        st.markdown("### 🎧 빈칸 채우기 (1~3번 중 선택)")
        
        q1 = st.selectbox("1번: There's a calm...", ["--- 선택 ---", "1. surrender", "2. sunshine", "3. sudden"], key="l1")
        q2 = st.selectbox("2번: ...rolling...", ["--- 선택 ---", "1. wood", "2. world", "3. wave"], key="l2")
        q3 = st.selectbox("3번: ...restless...", ["--- 선택 ---", "1. warrior", "2. winner", "3. worrier"], key="l3")
        q4 = st.selectbox("4번: ...wide-eyed...", ["--- 선택 ---", "1. wanderer", "2. wonder", "3. winter"], key="l4")
        q5 = st.selectbox("5번: ...kings and...", ["--- 선택 ---", "1. vacation", "2. vagabonds", "3. victory"], key="l5")

        if st.button("정답 확인하기", use_container_width=True):
            score = 0
            if "surrender" in q1: score += 1
            if "world" in q2: score += 1
            if "worrier" in q3: score += 1
            if "wanderer" in q4: score += 1
            if "vagabonds" in q5: score += 1
            
            if score == 5:
                st.balloons()
                st.success(f"Perfect! {score}/5 다 맞혔어요!")
            else:
                st.warning(f"다시 들어볼까요? 현재 점수: {score}/5")

# =========================
# 2. Key Expressions[cite: 1]
# =========================
with tab_expression:
    st.subheader("📘 핵심 표현 익히기")
    expressions = {
        "Surrender": "내맡김, 항복 (여기선 평온한 수용)",
        "Restless worrier": "쉴 새 없이 걱정하는 사람",
        "Wide-eyed wanderer": "눈을 크게 뜨고 방랑하는 사람",
        "Vagabonds": "방랑자, 부랑자",
        "Believe the very best": "최선(가장 좋은 것)을 믿다"
    }
    for word, mean in expressions.items():
        st.markdown(f'<div class="expression-card"><b>{word}</b>: {mean}</div>', unsafe_allow_html=True)

# =========================
# 3. Reflection[cite: 1]
# =========================
with tab_reflection:
    st.subheader("✍️ 오늘의 소감")
    user_input = st.text_area("노래를 듣고 가장 마음에 들었던 가사나 느낌을 적어보세요.")
    if st.button("제출하기"):
        if user_input:
            st.success("소중한 소감 감사합니다!")
        else:
            st.warning("내용을 입력해주세요.")
