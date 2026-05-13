import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(page_title="Frozen English Class", page_icon="❄️", layout="wide")

# =========================
# 고대비 라이트 디자인 (가독성 중점)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title { background-color: #f0f9ff; padding: 20px; border-radius: 15px; border: 2px solid #0ea5e9; text-align: center; color: #0369a1; margin-bottom: 25px; }
    .card-button { background-color: #e0f2fe; padding: 15px; border-radius: 10px; border: 2px solid #0ea5e9; text-align: center; font-weight: bold; cursor: pointer; margin: 5px; }
    .lyrics-display { background-color: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #cbd5e1; min-height: 200px; font-size: 1.2rem; }
    .eng-text { font-size: 1.3rem; font-weight: 700; color: #1e3a8a; }
    .kor-text { font-size: 1.1rem; color: #64748b; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"><h1>❄️ Let It Go: Listening Game</h1></div>', unsafe_allow_html=True)

# 세션 상태 초기화 (카드 순서 저장용)
if 'user_cards' not in st.session_state:
    st.session_state.user_cards = []

# -------------------------
# 탭 구성
# -------------------------
tab1, tab2 = st.tabs(["📺 STEP 1. 배경 & 전체 가사", "🧩 STEP 2. 가사 카드 맞추기"])

# -------------------------
# STEP 1: 영상 + 전체 가사 (동시 제공)
# -------------------------
with tab1:
    col_v, col_l = st.columns([1, 1.2])
    with col_v:
        st.subheader("🎬 엘사의 이야기")
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.info("비밀을 들켜버린 엘사가 눈산으로 도망쳐 자유를 찾는 내용입니다.")
        
    with col_l:
        st.subheader("📜 전체 가사와 뜻")
        lyrics = [
            ("The snow glows white on the mountain", "오늘 밤 산에는 하얀 눈이 빛나고"),
            ("A kingdom of isolation", "고립된 이 왕국에서"),
            ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
            ("Let it go, let it go!", "다 잊어, 이제 다 잊어!")
        ]
        for eng, kor in lyrics:
            st.markdown(f'<div class="eng-text">{eng}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kor-text">{kor}</div>', unsafe_allow_html=True)

# -------------------------
# STEP 2: 실시간 카드 게임 (들으면서 클릭 가능)
# -------------------------
with tab2:
    st.subheader("🧩 가사 카드 쌓기 게임")
    st.write("노래를 들으며 들리는 가사를 순서대로 클릭하세요!")
    
    # 섞인 카드들
    scrambled = [
        "Don't let them in, don't let them see",
        "A kingdom of isolation",
        "Let it go, let it go!",
        "The snow glows white on the mountain"
    ]
    
    # 정답
    ans = [
        "The snow glows white on the mountain",
        "A kingdom of isolation",
        "Don't let them in, don't let them see",
        "Let it go, let it go!"
    ]

    # 카드 버튼 레이아웃
    cols = st.columns(2)
    for i, card in enumerate(scrambled):
        if cols[i % 2].button(card, key=f"btn_{i}", use_container_width=True):
            if card not in st.session_state.user_cards:
                st.session_state.user_cards.append(card)

    st.write("---")
    st.markdown("### 📥 내가 쌓은 가사 카드:")
    
    if st.session_state.user_cards:
        for idx, item in enumerate(st.session_state.user_cards):
            st.info(f"{idx+1}번: {item}")
        
        # 정답 확인
        if len(st.session_state.user_cards) == len(ans):
            if st.session_state.user_cards == ans:
                st.balloons()
                st.success("🎉 완벽한 순서입니다! 정말 잘 들으셨네요!")
            else:
                st.error("순서가 조금 틀린 것 같아요. 다시 들어볼까요?")
            
            if st.button("다시 하기"):
                st.session_state.user_cards = []
                st.rerun()
    else:
        st.write("위의 버튼을 눌러 카드를 쌓아보세요.")
