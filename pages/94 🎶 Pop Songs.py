import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Frozen: Let It Go Class",
    page_icon="❄️",
    layout="wide"
)

# =========================
# 디자인 설정 (고대비 라이트 모드)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; } 
    .title-box {
        background-color: #f0f9ff;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #0ea5e9;
        text-align: center;
        margin-bottom: 25px;
    }
    .title-box h1 { color: #0369a1 !important; margin: 0; }
    
    /* 질문 텍스트 강조 */
    .q-label {
        font-size: 1.2rem;
        font-weight: 800;
        color: #0f172a;
        margin-top: 15px;
        display: block;
    }
    
    /* 가사 영역 스타일 */
    .lyrics-row {
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid #f1f5f9;
    }
    .eng-line { font-size: 1.3rem; font-weight: 700; color: #1e3a8a; line-height: 1.4; }
    .kor-sub { font-size: 1.1rem; color: #475569; margin-top: 4px; font-weight: 500; }
    
    /* 탭 디자인 */
    .stTabs [data-baseweb="tab"] { font-size: 1.1rem; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Listening & Full Lyrics</h1></div>', unsafe_allow_html=True)

# =========================
# 데이터: 전체 가사 (1절 + 코러스)
# =========================
full_lyrics = [
    ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
    ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
    ("A kingdom of isolation", "고립된 이 왕국에서"),
    ("And it looks like I'm the queen", "내가 이곳의 여왕이 된 것 같아"),
    ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
    ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내가 노력했다는 걸 알 거야"),
    ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
    ("Be the good girl you always have to be", "언제나 그랬듯 착한 소녀가 되어야 해"),
    ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
    ("Well, now they know!", "그런데 이제 그들이 알아버렸어!"),
    ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
    ("Can't hold it back anymore", "더 이상 참을 수 없어"),
    ("Let it go, let it go", "다 잊어, 다 던져버려"),
    ("Turn away and slam the door!", "뒤돌아서 문을 쾅 닫아버릴 거야"),
    ("I don't care what they're going to say", "남들이 무슨 말을 하든 상관없어"),
    ("Let the storm rage on", "폭풍아 계속 몰아쳐라"),
    ("The cold never bothered me anyway", "추위는 더 이상 나를 괴롭히지 못하니까")
]

# =========================
# 탭 구성
# =========================
tab1, tab2 = st.tabs(["🎧 STEP 1. 영상 보고 문제 풀기", "📜 STEP 2. 전체 가사 해석"])

# -------------------------
# STEP 1: 리스닝 집중형
# -------------------------
with tab1:
    col_v, col_q = st.columns([1.2, 1])
    
    with col_v:
        st.subheader("🎬 영상을 보며 잘 들어보세요")
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")

    with col_q:
        st.subheader("👂 Listening Check")
        
        st.markdown('<span class="q-label">1. The snow glows white on the...</span>', unsafe_allow_html=True)
        a1 = st.radio("Q1", ["mountain", "fountain"], index=None, horizontal=True, key="step1_q1", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">2. A kingdom of...</span>', unsafe_allow_html=True)
        a2 = st.radio("Q2", ["isolation", "imagination"], index=None, horizontal=True, key="step1_q2", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">3. Conceal, don\'t feel, don\'t let them...</span>', unsafe_allow_html=True)
        a3 = st.radio("Q3", ["know", "go"], index=None, horizontal=True, key="step1_q3", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">4. Can\'t hold it back...</span>', unsafe_allow_html=True)
        a4 = st.radio("Q4", ["anymore", "anyhow"], index=None, horizontal=True, key="step1_q4", label_visibility="collapsed")
        
        st.divider()
        if a1 == "mountain" and a2 == "isolation" and a3 == "know" and a4 == "anymore":
            st.success("✅ 모두 맞히셨습니다! 리스닝 완료!")
            st.balloons()
        elif a1 or a2 or a3 or a4:
            st.info("들리는 단어를 선택하면 실시간으로 정답 여부가 확인됩니다.")

# -------------------------
# STEP 2: 전체 가사 및 영상 동시 제공
# -------------------------
with tab2:
    st.subheader("📜 1절 전체 가사 및 해석")
    
    col_v2, col_l2 = st.columns([1, 1.2])
    
    with col_v2:
        # 가사를 보면서 영상을 다시 확인할 수 있도록 상단 고정
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.info("💡 가사와 해석을 읽으며 노래의 의미를 깊이 있게 파악해 보세요.")
        
        # 추가 이해 문제 (선택 사항)
        st.write("")
        st.markdown('<span class="q-label">주인공 엘사의 심경 변화는?</span>', unsafe_allow_html=True)
        st.write("처음에는 두려워하며 숨기려 했지만(Conceal), 결국 자신의 힘을 받아들이고 자유로워지기로(Let it go) 결심합니다.")

    with col_l2:
        # 가사 리스트 출력
        for eng, kor in full_lyrics:
            st.markdown(f"""
            <div class="lyrics-row">
                <div class="eng-line">{eng}</div>
                <div class="kor-sub">{kor}</div>
            </div>
            """, unsafe_allow_html=True)
