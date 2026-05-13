import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Frozen: English Class",
    page_icon="❄️",
    layout="wide"
)

# =========================
# 고급 CSS 디자인
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } 
    .title-box {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 30px;
    }
    .lyrics-preview {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
        font-family: 'Courier New', monospace;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    .eng-line { font-weight: bold; color: #f1f5f9; }
    .kor-sub { color: #94a3b8; font-size: 0.9rem; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Frozen: Let It Go Class</h1></div>', unsafe_allow_html=True)

# =========================
# 탭 구성 (Step 1 & Step 2)
# =========================
tab1, tab2 = st.tabs(["📖 Step 1. Reading & Quiz", "🎧 Step 2. Watching & Listening"])

# -------------------------
# Step 1: 배경 지식 및 독해
# -------------------------
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Lyrics Preview")
        st.markdown("""
        <div class="lyrics-preview">
            <div class="eng-line">The snow glows white on the mountain tonight</div>
            <div class="kor-sub">오늘 밤 산에는 하얀 눈이 빛나고</div>
            <div class="eng-line">A kingdom of isolation, and it looks like I'm the queen</div>
            <div class="kor-sub">고립된 왕국, 그리고 내가 이곳의 여왕인 것 같아</div>
            <div class="eng-line">The wind is howling like this swirling storm inside</div>
            <div class="kor-sub">바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고 있어</div>
            <div class="eng-line">Conceal, don't feel, don't let them know</div>
            <div class="kor-sub">숨기고, 느끼지 마, 그들이 알게 하지 마</div>
            <div class="eng-line">Well, now they know!</div>
            <div class="kor-sub">그런데 이제 그들이 알아버렸어!</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("❓ Comprehension Quiz")
        
        q1 = st.selectbox("1. 이 노래의 제목은 무엇인가요?", ["-선택-", "Into the Unknown", "Let It Go", "Do You Want to Build a Snowman?"])
        q2 = st.selectbox("2. 이 가사에서 느껴지는 전체적인 분위기는?", ["-선택-", "평화롭고 행복함", "답답하고 고립된 느낌", "지루하고 평범함"])
        q3 = st.selectbox("3. 가사 속 'I(주인공)'는 누구일까요?", ["-선택-", "안나 (Anna)", "올라프 (Olaf)", "엘사 (Elsa)"])
        
        if st.button("Check Answers"):
            if q1 == "Let It Go" and q2 == "답답하고 고립된 느낌" and q3 == "엘사 (Elsa)":
                st.success("참 잘했습니다! 이제 Step 2로 이동하여 노래를 들어봅시다.")
                st.balloons()
            else:
                st.error("다시 한 번 생각해보세요!")

# -------------------------
# Step 2: 영상 시청 및 단어 선택
# -------------------------
with tab2:
    st.subheader("🎬 Watch & Choose")
    v_col, l_col = st.columns([1.2, 1])
    
    with v_col:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.info("💡 영상을 보며 가사에 맞는 단어를 골라보세요.")

    with l_col:
        # 실시간 리스닝 퀴즈 (3문제로 축소)
        st.write("---")
        st.markdown("**[1] The snow glows white on the...**")
        ans1 = st.segmented_control("Choice 1", ["mountain", "fountain"], key="step2_q1", label_visibility="collapsed")
        
        st.write("**[2] A kingdom of...**")
        ans2 = st.segmented_control("Choice 2", ["isolation", "imagination"], key="step2_q2", label_visibility="collapsed")
        
        st.write("**[3] The wind is howling like this... storm inside**")
        ans3 = st.segmented_control("Choice 3", ["swirling", "swinging"], key="step2_q3", label_visibility="collapsed")
        
        st.write("---")
        if ans1 and ans2 and ans3:
            if ans1 == "mountain" and ans2 == "isolation" and ans3 == "swirling":
                st.success("정답을 모두 맞히셨습니다! 완벽한 리스닝이었어요! ❄️")
            else:
                st.warning("틀린 단어가 있는 것 같아요. 다시 들어볼까요?")
