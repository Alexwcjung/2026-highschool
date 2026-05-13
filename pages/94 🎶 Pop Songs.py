import streamlit as st

# =========================
# 1. 기본 설정 및 디자인 요소
# =========================
st.set_page_config(page_title="Frozen English Class", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f0f9ff; padding: 20px; border-radius: 15px;
        border: 2px solid #0ea5e9; text-align: center; color: #0369a1; margin-bottom: 25px;
    }
    .info-box {
        background-color: #f8fafc; padding: 20px; border-radius: 12px;
        border: 1px solid #e2e8f0; line-height: 1.8; margin-bottom: 20px;
    }
    .lyrics-container {
        padding: 10px 20px;
        border-left: 4px solid #38bdf8;
        margin-bottom: 10px;
        background-color: #f1f5f9;
        border-radius: 0 10px 10px 0;
    }
    .eng-line { font-size: 1.15rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.95rem; color: #64748b; }
    .q-label { font-size: 1.05rem; font-weight: 800; color: #0f172a; display: block; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화 (문제용)
if 'q1_cards' not in st.session_state: st.session_state.q1_cards = []
if 'q2_cards' not in st.session_state: st.session_state.q2_cards = []
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []

st.markdown('<div class="main-title"><h1>❄️ Frozen: Let It Go Interactive Class</h1></div>', unsafe_allow_html=True)

# =========================
# 2. 탭 구성
# =========================
tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 영화 배경", "📖 STEP 2. 가사 학습", "🧩 STEP 3. 가사 완성 챌린지"])

# -------------------------
# STEP 1: 영화 배경
# -------------------------
with tab1:
    col_vid, col_txt = st.columns(2)
    with col_vid:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    with col_txt:
        st.markdown("""
        <div class="info-box">
            <h3>🏰 아렌델과 엘사의 이야기</h3>
            엘사는 태어날 때부터 모든 것을 얼리는 마법을 가졌지만, 사고를 막기 위해 평생 마법을 숨기며 살아왔습니다. 
            하지만 대관식 날 마법이 들통나자 산으로 도망치게 되죠. <b>'Let It Go'</b>는 더 이상 숨지 않고 자신을 찾겠다는 선언입니다.
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# STEP 2: 가사 학습 (영상 추가 & 전체 가사)
# -------------------------
with tab2:
    st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    st.divider()
    
    col_quiz, col_lyrics = st.columns([1, 2])
    with col_quiz:
        st.markdown("### 💡 내용 이해 퀴즈")
        ans1 = st.radio("1. 엘사가 현재 머무는 곳은?", ["번잡한 도시", "고립된 눈 덮인 산", "안나의 방"], index=None)
        ans2 = st.radio("2. 'Conceal, don't feel'의 의미는?", ["숨기고 느끼지 마라", "당당하게 드러내라", "슬퍼하지 마라"], index=None)
        if st.button("정답 확인"):
            if ans1 == "고립된 눈 덮인 산" and ans2 == "숨기고 느끼지 마라": st.success("정답입니다!")
            else: st.error("다시 확인해보세요!")

    with col_lyrics:
        full_lyrics = [
            ("The snow glows white on the mountain tonight", "오늘 밤 산에 내린 눈은 하얗게 빛나고"),
            ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
            ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
            ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"),
            ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"),
            ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"),
            ("Be the good girl you always have to be", "늘 그래왔던 것처럼 착한 소녀가 되어야 해"),
            ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 말고, 그들이 모르게 해"),
            ("Well, now they know!", "그런데 이제 그들이 알아버렸어!"),
            ("Let it go, let it go", "다 잊어, 다 내려놓자"),
            ("Can't hold it back anymore", "더는 억누를 수 없어"),
            ("Let it go, let it go", "다 잊어, 이제 자유야"),
            ("Turn away and slam the door!", "돌아서서 문을 쾅 닫아버려"),
            ("I don't care what they're going to say", "사람들이 뭐라 하든 상관없어"),
            ("Let the storm rage on", "폭풍아 계속 휘몰아쳐라"),
            ("The cold never bothered me anyway", "추위는 더 이상 나를 괴롭히지 못하니까")
        ]
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

# -------------------------
# STEP 3: 가사 완성 챌린지 (더 많은 문제 & 1절 전체)
# -------------------------
with tab3:
    st.subheader("🧩 1절 가사 순서 맞추기 끝판왕")
    st.write("버튼을 순서대로 눌러 가사를 완성하세요.")
    
    # --- 문제 1: 도입부 (Verse 1) ---
    st.markdown("#### 1. 노래의 시작 부분을 완성하세요")
    q1_correct = ["The snow glows white", "Not a footprint to be seen", "A kingdom of isolation", "I'm the queen"]
    q1_scrambled = sorted(q1_correct)
    
    cols1 = st.columns(4)
    for i, word in enumerate(q1_scrambled):
        if cols1[i].button(word, key=f"q1_{i}"): st.session_state.q1_cards.append(word)
    
    st.write("선택한 순서:", " → ".join(st.session_state.q1_cards))
    if len(st.session_state.q1_cards) == 4:
        if st.session_state.q1_cards == q1_correct: st.success("Good!")
        else: 
            st.error("틀렸습니다.")
            if st.button("다시 하기", key="r1"): st.session_state.q1_cards = []; st.rerun()

    st.divider()

    # --- 문제 2: 갈등 (Pre-Chorus) ---
    st.markdown("#### 2. 엘사의 내적 갈등 부분")
    q2_correct = ["Don't let them in", "Be the good girl", "Conceal, don't feel", "Well, now they know!"]
    q2_scrambled = ["Be the good girl", "Well, now they know!", "Don't let them in", "Conceal, don't feel"]
    
    cols2 = st.columns(4)
    for i, word in enumerate(q2_scrambled):
        if cols2[i].button(word, key=f"q2_{i}"): st.session_state.q2_cards.append(word)
    
    st.write("선택한 순서:", " → ".join(st.session_state.q2_cards))
    if len(st.session_state.q2_cards) == 4:
        if st.session_state.q2_cards == q2_correct: st.success("Great!")
        else: 
            st.error("다시 생각해보세요.")
            if st.button("다시 하기", key="r2"): st.session_state.q2_cards = []; st.rerun()

    st.divider()

    # --- 문제 3: 1절 후렴구 전체 (Full Chorus) ---
    st.markdown("#### 3. 1절 후렴구 전체를 완성하세요 (고난도)")
    q3_correct = [
        "Let it go, let it go", 
        "Can't hold it back anymore", 
        "Turn away and slam the door!", 
        "I don't care what they're going to say", 
        "Let the storm rage on", 
        "The cold never bothered me anyway"
    ]
    q3_scrambled = [
        "Let the storm rage on",
        "Let it go, let it go",
        "The cold never bothered me anyway",
        "Turn away and slam the door!",
        "Can't hold it back anymore",
        "I don't care what they're going to say"
    ]
    
    cols3 = st.columns(3)
    cols4 = st.columns(3)
    for i, word in enumerate(q3_scrambled):
        target_col = cols3[i] if i < 3 else cols4[i-3]
        if target_col.button(word, key=f"q3_{i}", use_container_width=True): 
            st.session_state.q3_cards.append(word)
    
    st.write("선택한 순서:")
    for idx, line in enumerate(st.session_state.q3_cards):
        st.caption(f"{idx+1}: {line}")

    if len(st.session_state.q3_cards) == 6:
        if st.session_state.q3_cards == q3_correct:
            st.balloons()
            st.success("대단합니다! 1절을 완벽하게 마스터하셨어요!")
        else:
            st.error("순서가 조금 틀렸네요. 가사를 다시 확인해보세요!")
            if st.button("다시 하기", key="r3"): st.session_state.q3_cards = []; st.rerun()
