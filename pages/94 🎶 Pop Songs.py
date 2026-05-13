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
# 고대비 라이트 테마 디자인 (가독성 수정)
# =========================
st.markdown("""
<style>
    /* 배경 및 기본 글자색 (밝게) */
    .stApp { background-color: #ffffff; color: #1e293b; } 
    
    /* 제목 박스 */
    .title-box {
        background-color: #f0f9ff;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #0ea5e9;
        text-align: center;
        margin-bottom: 30px;
    }
    .title-box h1 { color: #0369a1 !important; }
    
    /* 문제 및 가사 카드 (선명하게) */
    .content-card {
        background-color: #f8fafc;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    
    /* 강조 텍스트 */
    .q-label {
        font-size: 1.2rem;
        font-weight: 800;
        color: #0f172a; /* 짙은 검정색 */
        margin-bottom: 10px;
        display: block;
    }
    
    /* 가사 해석 스타일 */
    .eng-line { font-size: 1.3rem; font-weight: 700; color: #1e3a8a; } /* 진한 파랑 */
    .kor-sub { font-size: 1.1rem; color: #475569; margin-bottom: 15px; font-weight: 500; }
    
    /* 탭 메뉴 글자색 수정 */
    .stTabs [data-baseweb="tab"] { color: #64748b; font-weight: 600; }
    .stTabs [aria-selected="true"] { color: #0284c7 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Listening & Understanding</h1><p style="color:#0369a1;">글자를 더 선명하고 보기 편하게 수정했습니다.</p></div>', unsafe_allow_html=True)

# =========================
# 탭 구성
# =========================
tab1, tab2, tab3 = st.tabs(["🎧 STEP 1. 듣기 연습", "📖 STEP 2. 내용 이해", "📜 STEP 3. 전체 가사"])

# -------------------------
# Step 1: 리스닝 (영상 + 선택지)
# -------------------------
with tab1:
    col_v, col_q = st.columns([1.2, 1])
    
    with col_v:
        st.subheader("🎬 영상을 재생하세요")
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")

    with col_q:
        st.subheader("👂 들리는 단어 선택")
        
        with st.container():
            st.markdown('<span class="q-label">1. The snow glows white on the...</span>', unsafe_allow_html=True)
            a1 = st.radio("Q1", ["mountain", "fountain"], index=None, horizontal=True, key="l_q1", label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">2. A kingdom of...</span>', unsafe_allow_html=True)
            a2 = st.radio("Q2", ["isolation", "imagination"], index=None, horizontal=True, key="l_q2", label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">3. Conceal, don\'t feel, don\'t let them...</span>', unsafe_allow_html=True)
            a3 = st.radio("Q3", ["know", "go"], index=None, horizontal=True, key="l_q3", label_visibility="collapsed")
            
        st.divider()
        if a1 == "mountain" and a2 == "isolation" and a3 == "know":
            st.success("✅ 정답입니다! 리스닝 실력이 훌륭하네요.")
        elif a1 or a2 or a3:
            st.info("단어를 선택하면 정답 확인이 가능합니다.")

# -------------------------
# Step 2: 내용 이해 (3지 선다)
# -------------------------
with tab2:
    st.subheader("❓ 주요 내용 퀴즈")
    
    with st.container():
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<span class="q-label">1. 이 노래의 제목은?</span>', unsafe_allow_html=True)
            cq1 = st.selectbox("Q1_Title", ["-선택-", "Into the Unknown", "Let It Go", "Frozen"], label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">2. 노래의 분위기는 어떤가요?</span>', unsafe_allow_html=True)
            cq2 = st.selectbox("Q2_Mood", ["-선택-", "매우 신나고 경쾌함", "고립되고 답답한 느낌", "평화롭고 고요함"], label_visibility="collapsed")
        
        with c2:
            st.markdown('<span class="q-label">3. 주인공은 누구인가요?</span>', unsafe_allow_html=True)
            cq3 = st.selectbox("Q3_Who", ["-선택-", "안나", "엘사", "올라프"], label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">4. 주인공의 현재 심정은?</span>', unsafe_allow_html=True)
            cq4 = st.selectbox("Q4_Feel", ["-선택-", "자신을 숨기고 싶어함", "이제 자유롭고 싶어함", "친구를 그리워함"], label_visibility="collapsed")
            
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("정답 제출하기", type="primary"):
        if cq1 == "Let It Go" and cq2 == "고립되고 답답한 느낌" and cq3 == "엘사" and cq4 == "이제 자유롭고 싶어함":
            st.balloons()
            st.success("🎉 완벽합니다! 모든 문제를 맞히셨어요!")
        else:
            st.error("다시 한 번 가사를 떠올리며 풀어보세요.")

# -------------------------
# Step 3: 전체 가사 (가독성 중점)
# -------------------------
with tab3:
    st.subheader("📜 전체 가사 및 해석")
    
    lyrics = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
        ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
        ("A kingdom of isolation", "고립된 이 왕국에서"),
        ("And it looks like I'm the queen", "내가 이곳의 여왕이 된 것 같아"),
        ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
        ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
        ("Well, now they know!", "그런데 이제 그들이 알아버렸어!"),
        ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
        ("Can't hold it back anymore", "더 이상 참을 수 없어")
    ]
    
    for eng, kor in lyrics:
        st.markdown(f'<div class="eng-line">{eng}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="kor-sub">{kor}</div>', unsafe_allow_html=True)
