import streamlit as st

# =========================
# 1. 기본 설정 및 디자인
# =========================
st.set_page_config(page_title="Frozen English Class", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    /* 전체 배경 및 텍스트 가독성 강화 */
    .stApp { background-color: #ffffff; color: #1e293b; }
    
    /* 제목 박스 */
    .title-box {
        background-color: #f0f9ff;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #0ea5e9;
        text-align: center;
        margin-bottom: 25px;
    }
    .title-box h1 { color: #0369a1 !important; margin: 0; }
    
    /* 줄거리 및 정보 박스 */
    .info-box {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        line-height: 1.7;
    }
    
    /* 가사 카드 스타일 */
    .eng-line { font-size: 1.3rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 1.1rem; color: #64748b; margin-bottom: 15px; }
    
    /* 질문 라벨 */
    .q-label { font-size: 1.2rem; font-weight: 800; color: #0f172a; display: block; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화 (카드 게임용)
if 'user_cards' not in st.session_state:
    st.session_state.user_cards = []

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Story & Lyrics Game</h1></div>', unsafe_allow_html=True)

# =========================
# 2. 탭 구성
# =========================
tab1, tab2 = st.tabs(["📖 STEP 1. 어떤 내용인가요?", "🎧 STEP 2. 노래 들으며 카드 맞추기"])

# -------------------------
# STEP 1: 영상 시청 및 배경 지식 이해
# -------------------------
with tab1:
    col_v1, col_q1 = st.columns([1.2, 1])
    
    with col_v1:
        st.subheader("🎬 먼저 영상을 시청하세요")
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        
        st.markdown("### 📖 엘사의 상황과 심경")
        st.markdown("""
        <div class="info-box">
            엘사는 마법 비밀을 들킨 후 혼자 눈산으로 도망칩니다. 처음에는 <b>외로움(Isolation)</b>을 느끼지만, 
            곧 남의 시선을 신경 쓰지 않고 자신의 마법을 펼치며 <b>자유(Freedom)</b>를 느낍니다.
        </div>
        """, unsafe_allow_html=True)

    with col_q1:
        st.subheader("❓ 퀴즈로 확인하기")
        st.markdown('<span class="q-label">1. 이 노래의 제목은 무엇인가요?</span>', unsafe_allow_html=True)
        q1 = st.selectbox("q1", ["-선택-", "Let It Go", "Into the Unknown"], label_visibility="collapsed")
        
        st.write("")
        st.markdown('<span class="q-label">2. 노래의 주인공은 누구인가요?</span>', unsafe_allow_html=True)
        q2 = st.selectbox("q2", ["-선택-", "안나 (Anna)", "엘사 (Elsa)"], label_visibility="collapsed")
        
        st.write("")
        st.markdown('<span class="q-label">3. 주인공의 기분은 어떻게 변했나요?</span>', unsafe_allow_html=True)
        q3 = st.selectbox("q3", ["-선택-", "슬픔에서 화남으로", "답답함에서 자유로움으로"], label_visibility="collapsed")
        
        if st.button("정답 확인", type="primary"):
            if q1 == "Let It Go" and q2 == "엘사 (Elsa)" and q3 == "답답함에서 자유로움으로":
                st.success("참 잘했습니다! 이제 노래 가사를 배우러 갈까요?")
                st.balloons()
            else:
                st.error("다시 한 번 생각해보세요!")

# -------------------------
# STEP 2: 전체 가사 & 실시간 카드 게임
# -------------------------
with tab2:
    st.subheader("📜 전체 가사 공부 & 🧩 카드 게임")
    st.write("영상을 다시 재생하고, 들리는 순서대로 아래 가사 버튼을 클릭하세요!")
    
    col_v2, col_l2 = st.columns([1, 1.2])
    
    with col_v2:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        
        st.divider()
        st.markdown("### 🧩 가사 순서 맞추기 게임")
        
        # 카드 게임 데이터
        scrambled = [
            "Don't let them in, don't let them see",
            "A kingdom of isolation",
            "Let it go, let it go!",
            "The snow glows white on the mountain"
        ]
        correct_ans = [
            "The snow glows white on the mountain",
            "A kingdom of isolation",
            "Don't let them in, don't let them see",
            "Let it go, let it go!"
        ]

        # 카드 버튼들
        c1, c2 = st.columns(2)
        for i, card in enumerate(scrambled):
            if (c1 if i % 2 == 0 else c2).button(card, key=f"card_{i}", use_container_width=True):
                if card not in st.session_state.user_cards:
                    st.session_state.user_cards.append(card)

        # 쌓인 카드 표시 및 정답 체크
        if st.session_state.user_cards:
            st.write("---")
            st.markdown("**[내가 선택한 순서]**")
            for idx, item in enumerate(st.session_state.user_cards):
                st.info(f"{idx+1}. {item}")
            
            if len(st.session_state.user_cards) == len(correct_ans):
                if st.session_state.user_cards == correct_ans:
                    st.balloons()
                    st.success("축하합니다! 순서를 완벽하게 맞혔어요!")
                else:
                    st.error("순서가 틀렸어요. 다시 시도해볼까요?")
                
                if st.button("게임 초기화"):
                    st.session_state.user_cards = []
                    st.rerun()

    with col_l2:
        st.markdown("### 📖 1절 전체 가사와 뜻")
        # 1절 전체 가사 데이터
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
            ("Turn away and slam the door!", "뒤돌아서 문을 쾅 닫아버릴 거야")
        ]
        
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="eng-line">{eng}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kor-sub">{kor}</div>', unsafe_allow_html=True)
