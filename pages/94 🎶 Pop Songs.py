import streamlit as st

# =========================
# 1. 기본 설정 및 디자인
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
if 'chorus_cards' not in st.session_state:
    st.session_state.chorus_cards = []

st.markdown('<div class="main-title"><h1>❄️ Frozen: Let It Go Interactive Class</h1></div>', unsafe_allow_html=True)

# =========================
# 2. 탭 구성
# =========================
tab1, tab2, tab3 = st.tabs(["📖 STEP 1. 영화 배경 알기", "🎧 STEP 2. 가사 듣기 & 이해", "🧩 STEP 3. 후렴구 순서 맞추기"])

# -------------------------
# STEP 1: 상세 배경 설명
# -------------------------
with tab1:
    st.subheader("❄️ 영화 '겨울왕국(Frozen)'의 배경")
    col_img, col_txt = st.columns([1, 1.5])
    
    with col_img:
        st.info("🏠 **아렌델 왕국 (Arendelle)**\n\n북유럽의 노르웨이를 모델로 한 아름다운 항구 도시입니다. 평화롭지만 마법을 두려워하는 전통이 있는 곳이죠.")

    with col_txt:
        st.markdown("""
        <div class="info-box">
            <b>1. 엘사의 비밀</b><br>
            주인공 엘사는 모든 것을 얼려버리는 마법을 가지고 태어났습니다. 부모님은 엘사에게 마법을 숨기라고 가르쳤죠. "숨기고, 느끼지 마(Conceal, don't feel)."가 그녀의 규칙이었습니다.<br><br>
            <b>2. 대관식 날의 사건</b><br>
            여왕이 되는 날, 엘사는 마법을 들키고 맙니다. 사람들은 겁을 먹었고, 엘사는 북쪽 산으로 홀로 도망칩니다.<br><br>
            <b>3. 'Let It Go'의 의미</b><br>
            산 정상에서 엘사는 더 이상 능력을 숨기지 않기로 결심합니다. <b>억눌렸던 삶을 던져버리고(Let it go), 진짜 나를 찾는 해방감</b>을 노래합니다.
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# STEP 2: 가사 전체 노출 & 왼쪽 퀴즈
# -------------------------
with tab2:
    st.subheader("📜 가사 전체 보기 및 이해도 체크")
    
    # 왼쪽 퀴즈(작게), 오른쪽 가사(전체)
    col_quiz, col_lyrics = st.columns([1, 2])
    
    with col_quiz:
        st.markdown("### ❓ 이해도 퀴즈")
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU") # 영상도 작게 배치
        
        st.markdown('<span class="q-label">1. 노래 초반, 엘사의 감정은?</span>', unsafe_allow_html=True)
        ans1 = st.radio("a1", ["신나고 자유로움", "외롭고 답답함", "화가 남"], index=None, key="q2_1", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">2. "Well, now they know!"의 심정은?</span>', unsafe_allow_html=True)
        ans2 = st.radio("a2", ["들켜서 슬픔", "차라리 속 시원함", "다시 숨고 싶음"], index=None, key="q2_2", label_visibility="collapsed")
        
        st.markdown('<span class="q-label">3. "isolation"의 뜻은?</span>', unsafe_allow_html=True)
        ans3 = st.radio("a3", ["축제", "혼자 있음(고립)", "마법"], index=None, key="q2_3", label_visibility="collapsed")

        if st.button("정답 확인하기", type="primary"):
            if ans1 == "외롭고 답답함" and ans2 == "차라리 속 시원함" and ans3 == "혼자 있음(고립)":
                st.success("✅ 정답입니다! 엘사의 마음을 잘 읽으셨네요.")
                st.balloons()
            else:
                st.error("오답이 있습니다. 다시 풀어보세요!")

    with col_lyrics:
        st.markdown("### 📜 1절 전체 가사")
        # 1절 가사 리스트 (더 길게 구성)
        full_lyrics_v1 = [
            ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
            ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
            ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 이곳의 여왕인 것 같아"),
            ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
            ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내가 노력했다는 걸 알 거야"),
            ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
            ("Be the good girl you always have to be", "언제나 그랬듯 착한 소녀가 되어야 해"),
            ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
            ("Well, now they know!", "그런데 이제 그들이 알아버렸어!"),
            ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
            ("Can't hold it back anymore", "더 이상 참을 수 없어"),
            ("Turn away and slam the door!", "뒤돌아서 문을 쾅 닫아버릴 거야")
        ]
        
        for eng, kor in full_lyrics_v1:
            st.markdown(f"""
            <div class="lyrics-container">
                <div class="eng-line">{eng}</div>
                <div class="kor-sub">{kor}</div>
            </div>
            """, unsafe_allow_html=True)

# -------------------------
# STEP 3: 후렴구 순서 맞추기 (음성만)
# -------------------------
with tab3:
    st.subheader("🎧 오디오만 듣고 순서 맞추기")
    st.write("화면을 보지 않고 소리에만 집중해서 후렴구(Chorus)를 완성해보세요!")

    # 음성 파일 (예시 링크)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 

    chorus_correct = [
        "Let it go, let it go",
        "Can't hold it back anymore",
        "Let it go, let it go",
        "Turn away and slam the door!"
    ]
    chorus_scrambled = [
        "Can't hold it back anymore",
        "Turn away and slam the door!",
        "Let it go, let it go",
        "Let it go, let it go"
    ]

    st.divider()
    c1, c2 = st.columns(2)
    for i, line in enumerate(chorus_scrambled):
        if (c1 if i % 2 == 0 else c2).button(line, key=f"chorus_{i}", use_container_width=True):
            st.session_state.chorus_cards.append(line)

    if st.session_state.chorus_cards:
        st.markdown("### 📥 내가 나열한 순서:")
        for idx, item in enumerate(st.session_state.chorus_cards):
            st.info(f"{idx+1}. {item}")
        
        if len(st.session_state.chorus_cards) == len(chorus_correct):
            if st.session_state.chorus_cards == chorus_correct:
                st.balloons()
                st.success("🎉 완벽한 리스닝이었습니다!")
            else:
                st.error("순서가 틀렸어요. 다시 한번 들어보세요.")
            
            if st.button("다시 도전"):
                st.session_state.chorus_cards = []
                st.rerun()
