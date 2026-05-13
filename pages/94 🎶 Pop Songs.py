import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Lyrics Training with Subtitles",
    page_icon="❄️",
    layout="wide"
)

# =========================
# CSS 디자인 (자막 가독성 강화)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } 
    .lyrics-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #38bdf8;
        margin-bottom: 20px;
    }
    .korean-sub {
        color: #94a3b8;
        font-size: 0.95rem;
        font-family: 'Nanum Gothic', sans-serif;
        margin-top: 5px;
    }
    .english-line {
        font-size: 1.2rem;
        font-weight: bold;
        color: #f1f5f9;
    }
    .stop-sign {
        color: #ef4444;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# 세션 상태 (진행 단계 관리)
# =========================
if 'step' not in st.session_state:
    st.session_state.step = 1[cite: 1]

# =========================
# 메인 레이아웃
# =========================
col_v, col_l = st.columns([1, 1.2])

with col_v:
    st.markdown("### 🎬 1. Watch Video")
    st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    st.info("💡 노래를 들으며 오른쪽에서 정답을 고르세요. 정답을 맞춰야 다음 자막이 나옵니다.")
    
    st.divider()
    st.metric("Progress", f"Step {st.session_state.step} / 5")

with col_l:
    st.markdown("### 📜 2. Interactive Subtitles")

    # 단계별 가사, 자막, 문제 구성
    
    # --- STEP 1 ---
    if st.session_state.step >= 1:
        with st.container():
            st.markdown('<div class="english-line">The snow glows white on the... tonight</div>', unsafe_allow_html=True)
            st.markdown('<div class="korean-sub">오늘 밤 산에는 하얀 눈이 빛나고</div>', unsafe_allow_html=True)
            if st.session_state.step == 1:
                ans1 = st.radio("1. 들리는 단어를 고르세요:", ["mountain", "fountain"], index=None, horizontal=True, key="q1")
                if ans1 == "mountain":
                    if st.button("정답! 다음 문장 보기"):
                        st.session_state.step = 2
                        st.rerun()
            else:
                st.success("Selected: mountain")

    # --- STEP 2 ---
    if st.session_state.step >= 2:
        st.divider()
        with st.container():
            st.markdown('<div class="english-line">A kingdom of... and it looks like I\'m the queen</div>', unsafe_allow_html=True)
            st.markdown('<div class="korean-sub">고립된 왕국, 그리고 내가 이곳의 여왕이 된 것 같아</div>', unsafe_allow_html=True)
            if st.session_state.step == 2:
                ans2 = st.radio("2. 들리는 단어를 고르세요:", ["isolation", "imagination"], index=None, horizontal=True, key="q2")
                if ans2 == "isolation":
                    if st.button("정답! 다음 문장 보기"):
                        st.session_state.step = 3
                        st.rerun()
            else:
                st.success("Selected: isolation")

    # --- STEP 3 ---
    if st.session_state.step >= 3:
        st.divider()
        with st.container():
            st.markdown('<div class="english-line">The wind is howling like this... storm inside</div>', unsafe_allow_html=True)
            st.markdown('<div class="korean-sub">바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고 있어</div>', unsafe_allow_html=True)
            if st.session_state.step == 3:
                ans3 = st.radio("3. 들리는 단어를 고르세요:", ["swirling", "swinging"], index=None, horizontal=True, key="q3")
                if ans3 == "swirling":
                    if st.button("정답! 다음 문장 보기"):
                        st.session_state.step = 4
                        st.rerun()
            else:
                st.success("Selected: swirling")

    # --- STEP 4 ---
    if st.session_state.step >= 4:
        st.divider()
        with st.container():
            st.markdown('<div class="english-line">...don\'t let them know. Well, now they know!</div>', unsafe_allow_html=True)
            st.markdown('<div class="korean-sub">그들이 알게 하지 마. 그런데 이제 그들이 알아버렸어!</div>', unsafe_allow_html=True)
            if st.session_state.step == 4:
                ans4 = st.radio("4. 들리는 단어를 고르세요:", ["conceal", "reveal"], index=None, horizontal=True, key="q4")
                if ans4 == "conceal":
                    if st.button("정답! 다음 문장 보기"):
                        st.session_state.step = 5
                        st.rerun()
            else:
                st.success("Selected: conceal")

    # --- STEP 5 ---
    if st.session_state.step >= 5:
        st.divider()
        with st.container():
            st.markdown('<div class="english-line">Let it go, let it go. Can\'t hold it back...</div>', unsafe_allow_html=True)
            st.markdown('<div class="korean-sub">다 잊어, 다 잊어. 더 이상은 견딜 수 없어</div>', unsafe_allow_html=True)
            if st.session_state.step == 5:
                ans5 = st.radio("5. 들리는 단어를 고르세요:", ["anymore", "anyhow"], index=None, horizontal=True, key="q5")
                if ans5 == "anymore":
                    st.balloons()
                    st.success("Perfect! 1절 학습 완료!")
                    if st.button("다시 도전하기"):
                        st.session_state.step = 1
                        st.rerun()
