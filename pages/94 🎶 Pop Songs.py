import streamlit as st

# =========================
# 1. 기본 설정 및 디자인 요소
# =========================
st.set_page_config(page_title="Frozen English Class", page_icon="❄️", layout="wide")

st.markdown("""
<style>
    /* 가독성 높은 라이트 테마 */
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f0f9ff; padding: 20px; border-radius: 15px;
        border: 2px solid #0ea5e9; text-align: center; color: #0369a1; margin-bottom: 25px;
    }
    .info-box {
        background-color: #f8fafc; padding: 20px; border-radius: 12px;
        border: 1px solid #e2e8f0; line-height: 1.8; margin-bottom: 20px;
    }
    /* 가사 스타일 */
    .lyrics-container {
        padding: 10px 20px;
        border-left: 4px solid #e2e8f0;
        margin-bottom: 10px;
    }
    .eng-line { font-size: 1.2rem; font-weight: 700; color: #1e3a8a; margin-bottom: 2px; }
    .kor-sub { font-size: 1rem; color: #64748b; margin-bottom: 12px; }
    
    /* 퀴즈 라벨 */
    .q-label { font-size: 1.05rem; font-weight: 800; color: #0f172a; display: block; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화 (카드 게임용)
if 'q1_cards' not in st.session_state:
    st.session_state.q1_cards = []
if 'q2_cards' not in st.session_state:
    st.session_state.q2_cards = []

st.markdown('<div class="main-title"><h1>❄️ Frozen: Let It Go Interactive Class</h1></div>', unsafe_allow_html=True)

# =========================
# 2. 탭 구성
# =========================
tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 영화 배경 알기", "📖 STEP 2. 가사 듣기 & 이해", "🧩 STEP 3. 후렴구 순서 맞추기"])

# -------------------------
# STEP 1: 영상 & 상세 배경 설명 (영상을 절반 크기로 옆에 배치)
# -------------------------
with tab1:
    st.subheader("❄️ '겨울왕국(Frozen)' 배경 알아보기")

    # ▶ 영상을 왼쪽 절반, 텍스트를 오른쪽 절반에 배치
    col_video, col_txt = st.columns([1, 1])

    with col_video:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.info("🏰 **아렌델 왕국 (Arendelle)**\n\n북유럽의 노르웨이를 모델로 한 아름다운 항구 도시입니다. 평화롭지만 마법을 두려워하는 전통이 있는 곳이죠.")

    with col_txt:
        st.markdown("""
        <div class="info-box">
            <b>1. 엘사의 비밀</b><br>
            주인공 엘사는 모든 것을 얼려버리는 마법을 가지고 태어났습니다. 부모님은 엘사에게 마법을 숨기라고 가르쳤죠. "숨기고, 느끼지 마(Conceal, don't feel)."가 그녀의 규칙이었습니다.<br><br>
            <b>2. 대관식 날의 사건</b><br>
            여왕이 되는 날, 엘사는 마법을 들키고 맙니다. 사람들은 겁을 먹었고, 엘사는 북쪽 얼음 산으로 도망칩니다.<br><br>
            <b>3. 'Let It Go'의 의미</b><br>
            산 정상에서 엘사는 더 이상 능력을 숨기지 않기로 결심합니다. <b>억눌렸던 삶을 놓아버리고(Let it go), 진짜 나를 찾는 해방감</b>을 노래합니다.
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# STEP 2: 가사 전체 노출 & 왼쪽 퀴즈
# -------------------------
with tab2:
    st.subheader("📖 가사 전체 보기 및 이해도 체크")
    
    col_quiz, col_lyrics = st.columns([1, 2])
    
    with col_quiz:
        st.markdown("### 💡 이해도 퀴즈")
        
        st.markdown('<span class="q-label">1. 노래 초반, 엘사의 감정은?</span>', unsafe_allow_html=True)
        ans1 = st.radio("a1", ["신나고 자유로움", "외롭고 답답함", "화가 남"], index=None, key="q2_1", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">2. "Well, now they know!"의 심정은?</span>', unsafe_allow_html=True)
        ans2 = st.radio("a2", ["들켜서 회피", "차라리 속 시원함", "다시 숨고 싶음"], index=None, key="q2_2", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">3. "isolation"의 뜻은?</span>', unsafe_allow_html=True)
        ans3 = st.radio("a3", ["축제", "혼자 있음(고립)", "마법"], index=None, key="q2_3", label_visibility="collapsed")

        if st.button("정답 확인하기", type="primary"):
            if ans1 == "외롭고 답답함" and ans2 == "차라리 속 시원함" and ans3 == "혼자 있음(고립)":
                st.success("🎉 정답입니다! 엘사의 마음을 잘 읽으셨네요.")
                st.balloons()
            else:
                st.error("오답이 있습니다. 다시 생각해보세요!")

    with col_lyrics:
        st.markdown("### ❄️ 전체 가사 (Full Lyrics)")

        # ▶ 전체 가사 리스트 (스크롤 없이 전부 표시)
        full_lyrics = [
            ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
            ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
            ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서, 내가 이곳의 여왕인 것 같아"),
            ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
            ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내가 노력했다는 걸 알 거야"),
            ("Don't let them in, don't let them see", "아무도 들이지 마, 아무것도 보여주지 마"),
            ("Be the good girl you always have to be", "언제나 그랬듯 착한 소녀가 되어야 해"),
            ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
            ("Well, now they know!", "그런데 이제 그들이 알아버렸네!"),
            ("Let it go, let it go", "다 놓아버려, 이제 다 놓아버려"),
            ("Can't hold it back anymore", "더 이상 참을 수 없어"),
            ("Let it go, let it go", "다 놓아버려, 이제 다 놓아버려"),
            ("Turn away and slam the door!", "돌아서서 문을 쾅 닫아버릴 거야!"),
            ("I don't care what they're going to say", "사람들이 뭐라 하든 상관 안 해"),
            ("Let the storm rage on", "폭풍아 계속 휘몰아쳐라"),
            ("The cold never bothered me anyway", "어차피 추위는 날 괴롭히지 못했으니까"),
            ("It's funny how some distance makes everything seem small", "거리를 두니 모든 게 작아 보인다는 게 재밌어"),
            ("And the fears that once controlled me can't get to me at all", "한때 날 지배했던 두려움도 이젠 날 어쩌지 못해"),
            ("It's time to see what I can do", "이제 내가 뭘 할 수 있는지 확인할 시간이야"),
            ("To test the limits and break through", "한계를 시험하고 돌파할 거야"),
            ("No right, no wrong, no rules for me", "내겐 옳고 그른 것도, 규칙도 없어"),
            ("I'm free!", "난 자유야!"),
            ("Let it go, let it go", "다 놓아버려, 이제 다 놓아버려"),
            ("I am one with the wind and sky", "난 바람과 하늘과 하나가 되었어"),
            ("Let it go, let it go", "다 놓아버려, 이제 다 놓아버려"),
            ("You'll never see me cry", "내가 우는 모습은 다신 볼 수 없을 거야"),
            ("Here I stand and here I'll stay", "여기 내가 서 있고, 난 여기에 머물 거야"),
            ("Let the storm rage on", "폭풍아 계속 휘몰아쳐라"),
            ("My power flurries through the air into the ground", "내 힘은 공기를 타고 땅으로 흩날리고"),
            ("My soul is spiraling in frozen fractals all around", "내 영혼은 얼어붙은 결정체가 되어 사방에서 맴돌아"),
            ("And one thought crystallizes like an icy blast", "그리고 한 가지 생각이 얼음 폭풍처럼 선명해지지"),
            ("I'm never going back, the past is in the past", "난 절대 돌아가지 않아, 과거는 과거일 뿐이야"),
            ("Let it go, let it go", "다 놓아버려, 이제 다 놓아버려"),
            ("And I'll rise like the break of dawn", "나는 떠오르는 새벽처럼 솟아오를 거야"),
            ("Let it go, let it go", "다 놓아버려, 이제 다 놓아버려"),
            ("That perfect girl is gone", "그 완벽했던 소녀는 이제 없어"),
            ("Here I stand in the light of day", "낮의 빛 속에 여기 내가 서 있어"),
            ("Let the storm rage on", "폭풍아 계속 휘몰아쳐라"),
            ("The cold never bothered me anyway", "어차피 추위는 날 괴롭히지 못했으니까")
        ]
        
        # ▶ height 제한 없이 전체 가사 표시 (스크롤 박스 제거)
        lyrics_html = ""
        for eng, kor in full_lyrics:
            lyrics_html += f"""
            <div class="lyrics-container">
                <div class="eng-line">{eng}</div>
                <div class="kor-sub">{kor}</div>
            </div>
            """
        st.markdown(lyrics_html, unsafe_allow_html=True)

# -------------------------
# STEP 3: 순서 맞추기 (문제 여러 개)
# -------------------------
with tab3:
    st.subheader("🎧 오디오만 듣고 순서 맞추기")
    st.write("화면을 보지 않고 소리에만 집중해서 문장을 완성해보세요!")

    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 
    st.divider()

    # --- 첫 번째 문제 ---
    st.markdown("### 📝 문제 1: 첫 번째 후렴구 (First Chorus)")
    correct_1 = [
        "Let it go, let it go",
        "Can't hold it back anymore",
        "Let it go, let it go (2)",
        "Turn away and slam the door!"
    ]
    scrambled_1 = [
        "Can't hold it back anymore",
        "Turn away and slam the door!",
        "Let it go, let it go (2)",
        "Let it go, let it go"
    ]

    c1, c2 = st.columns(2)
    for i, line in enumerate(scrambled_1):
        if (c1 if i % 2 == 0 else c2).button(line, key=f"q1_btn_{i}", use_container_width=True):
            st.session_state.q1_cards.append(line)

    if st.session_state.q1_cards:
        st.markdown("**👉 내가 나열한 순서:**")
        for idx, item in enumerate(st.session_state.q1_cards):
            st.info(f"{idx+1}. {item}")
        
        if len(st.session_state.q1_cards) == len(correct_1):
            if st.session_state.q1_cards == correct_1:
                st.success("✅ 완벽합니다! 첫 번째 문제 정답!")
            else:
                st.error("❌ 순서가 틀렸어요. 다시 한번 들어보세요.")
            
            if st.button("🔄 문제 1 다시 도전", key="reset_q1"):
                st.session_state.q1_cards = []
                st.rerun()

    st.divider()

    # --- 두 번째 문제 ---
    st.markdown("### 📝 문제 2: 클라이맥스 (Climax)")
    correct_2 = [
        "Let it go, let it go",
        "And I'll rise like the break of dawn",
        "Let it go, let it go (2)",
        "That perfect girl is gone"
    ]
    scrambled_2 = [
        "That perfect girl is gone",
        "Let it go, let it go",
        "And I'll rise like the break of dawn",
        "Let it go, let it go (2)"
    ]

    c3, c4 = st.columns(2)
    for i, line in enumerate(scrambled_2):
        if (c3 if i % 2 == 0 else c4).button(line, key=f"q2_btn_{i}", use_container_width=True):
            st.session_state.q2_cards.append(line)

    if st.session_state.q2_cards:
        st.markdown("**👉 내가 나열한 순서:**")
        for idx, item in enumerate(st.session_state.q2_cards):
            st.info(f"{idx+1}. {item}")
        
        if len(st.session_state.q2_cards) == len(correct_2):
            if st.session_state.q2_cards == correct_2:
                st.success("✅ 대단해요! 클라이맥스까지 완벽하게 맞추셨습니다!")
                st.balloons()
            else:
                st.error("❌ 아쉽습니다. 순서가 조금 다르네요.")
            
            if st.button("🔄 문제 2 다시 도전", key="reset_q2"):
                st.session_state.q2_cards = []
                st.rerun()
