import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Lyrics Training: Let It Go",
    page_icon="❄️",
    layout="wide"
)

# =========================
# 고급 CSS 디자인 (인터랙티브 요소 강조)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } 
    .title-box {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    /* 가사 영역 스타일 */
    .lyrics-container {
        background-color: #1e293b;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #38bdf8;
        line-height: 2.5;
        font-size: 1.3rem;
        font-family: 'Nanum Gothic', sans-serif;
    }
    /* 현재 읽는 구절 강조색 */
    .current-line {
        background-color: rgba(56, 189, 248, 0.2);
        border-left: 4px solid #38bdf8;
        padding-left: 10px;
        display: block;
    }
    .choice-label {
        color: #fbbf24;
        font-weight: bold;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Direct Click Training</h1><p>노래를 들으며 가사 속 버튼을 눌러 정답을 바로 고르세요!</p></div>', unsafe_allow_html=True)

# =========================
# 메인 레이아웃 (영상 | 인터랙티브 가사)
# =========================
col_v, col_l = st.columns([1, 1.2])

with col_v:
    st.subheader("🎬 Watch & Listen")
    st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    
    st.divider()
    # 학습 가이드 및 결과 확인
    st.info("💡 가사 옆의 선택 버튼을 클릭하면 즉시 정답 여부가 확인됩니다.")
    
    # 점수 계산용 세션 상태 초기화
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = set()

    st.metric("My Score", f"{st.session_state.score} / 5")
    if st.session_state.score == 5:
        st.balloons()
        st.success("1절의 핵심 단어를 모두 맞혔습니다!")

with col_l:
    st.subheader("📜 Interactive Lyrics")
    
    # 가사를 섹션별로 나누어 배치하고, 버튼을 가사 줄에 직접 통합
    with st.container():
        # 1번 문항
        st.write("The snow glows white on the...")
        c1_1, c1_2, c1_3 = st.columns([0.1, 0.4, 0.5])
        with c1_2:
            q1 = st.selectbox("1. mountain / fountain", ["-선택-", "mountain", "fountain"], key="q1", label_visibility="collapsed")
            if q1 == "mountain" and "q1" not in st.session_state.answered:
                st.session_state.score += 1
                st.session_state.answered.add("q1")
        st.markdown("<span class="current-line">...tonight, Not a footprint to be seen.</span>", unsafe_allow_html=True)
        
        st.write("A kingdom of...")
        c2_1, c2_2, c2_3 = st.columns([0.1, 0.4, 0.5])
        with c2_2:
            q2 = st.selectbox("2. isolation / imagination", ["-선택-", "isolation", "imagination"], key="q2", label_visibility="collapsed")
            if q2 == "isolation" and "q2" not in st.session_state.answered:
                st.session_state.score += 1
                st.session_state.answered.add("q2")
        st.write("And it looks like I'm the queen.")
        
        st.write("The wind is howling like this...")
        c3_1, c3_2, c3_3 = st.columns([0.1, 0.4, 0.5])
        with c3_2:
            q3 = st.selectbox("3. swirling / swinging", ["-선택-", "swirling", "swinging"], key="q3", label_visibility="collapsed")
            if q3 == "swirling" and "q3" not in st.session_state.answered:
                st.session_state.score += 1
                st.session_state.answered.add("q3")
        st.write("storm inside. Couldn't keep it in, heaven knows I tried.")

        st.write("---")
        st.write("Don't let them in, don't let them see...")
        
        c4_1, c4_2, c4_3 = st.columns([0.1, 0.4, 0.5])
        with c4_2:
            q4 = st.selectbox("4. conceal / reveal", ["-선택-", "conceal", "reveal"], key="q4", label_visibility="collapsed")
            if q4 == "conceal" and "q4" not in st.session_state.answered:
                st.session_state.score += 1
                st.session_state.answered.add("q4")
        st.write("don't feel, don't let them know. Well, now they know!")

        st.write("Let it go, let it go. Can't hold it back...")
        c5_1, c5_2, c5_3 = st.columns([0.1, 0.4, 0.5])
        with c5_2:
            q5 = st.selectbox("5. anymore / anyhow", ["-선택-", "anymore", "anyhow"], key="q5", label_visibility="collapsed")
            if q5 == "anymore" and "q5" not in st.session_state.answered:
                st.session_state.score += 1
                st.session_state.answered.add("q5")
        st.write("Let it go, let it go. Turn away and slam the door!")
