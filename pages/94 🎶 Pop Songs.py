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
# 가독성 극대화 디자인 (White 테마)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; } 
    .main-title {
        background-color: #f0f9ff;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #0ea5e9;
        text-align: center;
        margin-bottom: 25px;
        color: #0369a1;
    }
    .info-box {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        line-height: 1.7;
        margin-bottom: 20px;
    }
    .q-label {
        font-size: 1.15rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
        display: block;
    }
    .eng-line { font-size: 1.25rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 1.05rem; color: #475569; margin-bottom: 18px; font-weight: 500; }
    .highlight { color: #0284c7; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"><h1>❄️ Let It Go: Understanding & Lyrics</h1></div>', unsafe_allow_html=True)

# =========================
# 탭 구성
# =========================
tab1, tab2 = st.tabs(["📋 STEP 1. 도입 및 이해", "🎧 STEP 2. 전체 가사 듣기"])

# -------------------------
# STEP 1: 영상 & 줄거리 & 사전 퀴즈
# -------------------------
with tab1:
    col_v, col_q = st.columns([1.2, 1])
    
    with col_v:
        st.subheader("🎬 Introduction Video")
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        
        st.subheader("📖 줄거리 및 배경")
        st.markdown("""
        <div class="info-box">
            <b>[엘사의 상황]</b><br>
            태어날 때부터 신비로운 얼음 마법을 가진 엘사는 자신의 능력이 타인에게 해를 끼칠까 봐 평생을 숨기며 살아왔습니다. 하지만 대관식 날, 능력이 세상에 드러나 버리고 그녀는 사람들을 피해 눈 덮인 산으로 도망칩니다.<br><br>
            <b>[심경의 변화]</b><br>
            처음에는 비밀이 밝혀진 것에 대한 <span class="highlight">두려움과 고립감</span>을 느끼지만, 아무도 없는 산속에서 비로소 자신의 마법을 마음껏 펼치며 억눌렸던 감정으로부터 <span class="highlight">자유와 해방감</span>을 만끽하기 시작합니다.
        </div>
        """, unsafe_allow_html=True)

    with col_q:
        st.subheader("❓ 사전 이해도 체크")
        
        with st.container():
            st.markdown('<span class="q-label">1. 이 노래의 제목은 무엇인가요?</span>', unsafe_allow_html=True)
            cq1 = st.radio("title", ["Let It Go", "Do You Want to Build a Snowman?", "For the First Time in Forever"], index=None, key="pre_q1", label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">2. 노래 초반, 산으로 도망친 엘사의 심경은?</span>', unsafe_allow_html=True)
            cq2 = st.radio("mood", ["기쁘고 신남", "답답하고 고독함", "화가 나고 복수하고 싶음"], index=None, key="pre_q2", label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">3. 가사 중 "Conceal, don\'t feel"의 뜻은?</span>', unsafe_allow_html=True)
            cq3 = st.radio("meaning", ["감추고, 느끼지 마", "드러내고, 즐겨봐", "친구와 함께해"], index=None, key="pre_q3", label_visibility="collapsed")
            
            st.write("")
            st.markdown('<span class="q-label">4. 이 노래의 주인공인 여왕의 이름은?</span>', unsafe_allow_html=True)
            cq4 = st.radio("who", ["안나 (Anna)", "엘사 (Elsa)", "올라프 (Olaf)"], index=None, key="pre_q4", label_visibility="collapsed")

        if st.button("정답 확인하기", type="primary"):
            if cq1 == "Let It Go" and cq2 == "답답하고 고독함" and cq3 == "감추고, 느끼지 마" and cq4 == "엘사 (Elsa)":
                st.success("✅ 완벽합니다! 이제 가사를 자세히 들어볼 준비가 되었습니다.")
                st.balloons()
            else:
                st.error("다시 한번 확인해 보세요!")

# -------------------------
# STEP 2: 전체 가사 리스닝 (1절 코러스 전부)
# -------------------------
with tab2:
    st.subheader("📜 1절 전체 가사 (English & Korean)")
    st.info("💡 영상을 재생하고 가사를 눈으로 따라가며 해석을 확인하세요.")
    
    # 1절 가사 전체 데이터
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
    
    col_v2, col_l2 = st.columns([1, 1.2])
    
    with col_v2:
        # 가사와 함께 볼 수 있도록 영상 재배치
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.write("")
        st.warning("⚠️ **학습 포인트**: 가사 중 **'Conceal'**과 **'Let it go'**의 상반된 감정을 비교해 보세요.")

    with col_l2:
        # 가사 출력
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="eng-line">{eng}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kor-sub">{kor}</div>', unsafe_allow_html=True)
