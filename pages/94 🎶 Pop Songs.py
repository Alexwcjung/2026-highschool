import streamlit as st

# =========================
# 1. 기본 설정 및 디자인
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
        border-left: 4px solid #e2e8f0;
        margin-bottom: 10px;
    }
    .eng-line { font-size: 1.2rem; font-weight: 700; color: #1e3a8a; margin-bottom: 2px; }
    .kor-sub { font-size: 1rem; color: #64748b; margin-bottom: 12px; }
    .section-label { 
        font-size: 1.1rem; font-weight: 800; color: #0ea5e9; 
        margin-top: 20px; margin-bottom: 10px; 
        padding: 8px 12px; background-color: #f0f9ff; border-radius: 8px;
    }
    .q-label { font-size: 1.05rem; font-weight: 800; color: #0f172a; display: block; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'chorus_cards' not in st.session_state:
    st.session_state.chorus_cards = []
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = 0

st.markdown('<div class="main-title"><h1>❄️ Frozen: Let It Go Interactive Class</h1></div>', unsafe_allow_html=True)

# =========================
# 2. 탭 구성
# =========================
tab1, tab2, tab3 = st.tabs(["📖 STEP 1. 영화 배경 알기", "🎧 STEP 2. 가사 듣기 & 이해", "🧩 STEP 3. 후렴구 순서 맞추기"])

# -------------------------
# STEP 1: 상세 배경 설명 + 영상
# -------------------------
with tab1:
    st.subheader("❄️ 영화 '겨울왕국(Frozen)'의 배경")
    
    # 영상 섹션
    st.markdown("### 🎬 Let It Go 뮤직비디오")
    st.video("[youtube.com](https://www.youtube.com/watch?v=L0MK7qz13bU)")
    
    st.divider()
    
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
# STEP 2: 전체 가사 + 퀴즈
# -------------------------
with tab2:
    st.subheader("📜 전체 가사 보기 및 이해도 체크")
    
    col_quiz, col_lyrics = st.columns([1, 2])
    
    with col_quiz:
        st.markdown("### ❓ 이해도 퀴즈")
        st.video("[youtube.com](https://www.youtube.com/watch?v=L0MK7qz13bU)")
        
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
        # 전체 가사 데이터
        full_lyrics = {
            "🎵 Verse 1 (1절)": [
                ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
                ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
                ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 이곳의 여왕인 것 같아"),
                ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
                ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내가 노력했다는 걸 알 거야"),
            ],
            "🔒 Pre-Chorus (프리코러스)": [
                ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
                ("Be the good girl you always have to be", "언제나 그랬듯 착한 소녀가 되어야 해"),
                ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
                ("Well, now they know!", "그런데 이제 그들이 알아버렸어!"),
            ],
            "✨ Chorus 1 (후렴 1)": [
                ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
                ("Can't hold it back anymore", "더 이상 참을 수 없어"),
                ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
                ("Turn away and slam the door!", "뒤돌아서 문을 쾅 닫아버릴 거야"),
                ("I don't care what they're going to say", "사람들이 뭐라 하든 상관없어"),
                ("Let the storm rage on", "폭풍아 휘몰아쳐라"),
                ("The cold never bothered me anyway", "추위는 어차피 날 힘들게 한 적 없으니까"),
            ],
            "🎵 Verse 2 (2절)": [
                ("It's funny how some distance makes everything seem small", "거리를 두니 모든 게 작아 보이는 게 신기해"),
                ("And the fears that once controlled me can't get to me at all", "한때 날 지배했던 두려움도 이젠 닿지 못해"),
                ("It's time to see what I can do", "이제 내가 뭘 할 수 있는지 볼 시간이야"),
                ("To test the limits and break through", "한계를 시험하고 뛰어넘을 거야"),
                ("No right, no wrong, no rules for me", "옳고 그름도, 규칙도 없어"),
                ("I'm free!", "나는 자유야!"),
            ],
            "✨ Chorus 2 (후렴 2)": [
                ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
                ("I am one with the wind and sky", "나는 바람과 하늘과 하나야"),
                ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
                ("You'll never see me cry", "내가 우는 걸 다신 못 볼 거야"),
                ("Here I stand and here I stay", "여기 서서 여기 머물 거야"),
                ("Let the storm rage on", "폭풍아 휘몰아쳐라"),
            ],
            "🌟 Bridge (브릿지)": [
                ("My power flurries through the air into the ground", "내 힘이 하늘을 지나 땅으로 휘몰아쳐"),
                ("My soul is spiraling in frozen fractals all around", "내 영혼은 얼어붙은 결정 속에서 소용돌이치고 있어"),
                ("And one thought crystallizes like an icy blast", "그리고 하나의 생각이 차가운 폭풍처럼 결정화돼"),
                ("I'm never going back, the past is in the past!", "난 절대 돌아가지 않아, 과거는 과거일 뿐!"),
            ],
            "✨ Final Chorus (마지막 후렴)": [
                ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
                ("And I'll rise like the break of dawn", "나는 새벽녘처럼 일어설 거야"),
                ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
                ("That perfect girl is gone!", "그 완벽한 소녀는 사라졌어!"),
                ("Here I stand in the light of day", "햇살 아래 여기 서 있어"),
                ("Let the storm rage on!", "폭풍아 휘몰아쳐라!"),
                ("The cold never bothered me anyway", "추위는 어차피 날 힘들게 한 적 없으니까"),
            ],
        }
        
        for section, lines in full_lyrics.items():
            st.markdown(f'<div class="section-label">{section}</div>', unsafe_allow_html=True)
            for eng, kor in lines:
                st.markdown(f"""
                <div class="lyrics-container">
                    <div class="eng-line">{eng}</div>
                    <div class="kor-sub">{kor}</div>
                </div>
                """, unsafe_allow_html=True)

# -------------------------
# STEP 3: 확장된 순서 맞추기
# -------------------------
with tab3:
    st.subheader("🎧 오디오만 듣고 순서 맞추기")
    st.write("화면을 보지 않고 소리에만 집중해서 가사를 완성해보세요!")
    
    st.audio("[soundhelix.com](https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3)")
    
    # 여러 퀴즈 세트
    quiz_sets = [
        {
            "title": "🎯 Quiz 1: 첫 번째 후렴구",
            "correct": [
                "Let it go, let it go",
                "Can't hold it back anymore",
                "Let it go, let it go",
                "Turn away and slam the door!"
            ],
            "scrambled": [
                "Can't hold it back anymore",
                "Turn away and slam the door!",
                "Let it go, let it go",
                "Let it go, let it go"
            ]
        },
        {
            "title": "🎯 Quiz 2: 프리코러스",
            "correct": [
                "Don't let them in, don't let them see",
                "Be the good girl you always have to be",
                "Conceal, don't feel, don't let them know",
                "Well, now they know!"
            ],
            "scrambled": [
                "Conceal, don't feel, don't let them know",
                "Don't let them in, don't let them see",
                "Well, now they know!",
                "Be the good girl you always have to be"
            ]
        },
        {
            "title": "🎯 Quiz 3: 2절 시작",
            "correct": [
                "It's funny how some distance makes everything seem small",
                "And the fears that once controlled me can't get to me at all",
                "It's time to see what I can do",
                "To test the limits and break through"
            ],
            "scrambled": [
                "To test the limits and break through",
                "It's funny how some distance makes everything seem small",
                "It's time to see what I can do",
                "And the fears that once controlled me can't get to me at all"
            ]
        },
        {
            "title": "🎯 Quiz 4: 마지막 후렴구",
            "correct": [
                "Let it go, let it go",
                "And I'll rise like the break of dawn",
                "Let it go, let it go",
                "That perfect girl is gone!"
            ],
            "scrambled": [
                "That perfect girl is gone!",
                "Let it go, let it go",
                "And I'll rise like the break of dawn",
                "Let it go, let it go"
            ]
        },
        {
            "title": "🎯 Quiz 5: 브릿지",
            "correct": [
                "My power flurries through the air into the ground",
                "My soul is spiraling in frozen fractals all around",
                "And one thought crystallizes like an icy blast",
                "I'm never going back, the past is in the past!"
            ],
            "scrambled": [
                "I'm never going back, the past is in the past!",
                "My power flurries through the air into the ground",
                "And one thought crystallizes like an icy blast",
                "My soul is spiraling in frozen fractals all around"
            ]
        }
    ]
    
    st.divider()
    
    # 퀴즈 선택
    quiz_titles = [q["title"] for q in quiz_sets]
    selected_quiz = st.selectbox("문제를 선택하세요:", quiz_titles, key="quiz_selector")
    current_quiz = quiz_titles.index(selected_quiz)
    
    # 퀴즈 변경 시 초기화
    if st.session_state.current_quiz != current_quiz:
        st.session_state.chorus_cards = []
        st.session_state.current_quiz = current_quiz
    
    quiz = quiz_sets[current_quiz]
    
    st.markdown(f"### {quiz['title']}")
    st.info("👆 아래 버튼을 순서대로 클릭하세요!")
    
    st.divider()
    
    # 버튼 배치
    cols = st.columns(2)
    for i, line in enumerate(quiz["scrambled"]):
        col = cols[i % 2]
        # 이미 선택된 항목은 비활성화 표시
        if line in st.session_state.chorus_cards:
            col.button(f"✓ {line}", key=f"quiz_{current_quiz}_{i}", disabled=True, use_container_width=True)
        else:
            if col.button(line, key=f"quiz_{current_quiz}_{i}", use_container_width=True):
                st.session_state.chorus_cards.append(line)
                st.rerun()

    # 선택된 순서 표시
    if st.session_state.chorus_cards:
        st.markdown("### 📥 내가 나열한 순서:")
        for idx, item in enumerate(st.session_state.chorus_cards):
            st.info(f"{idx+1}. {item}")
        
        # 정답 체크
        if len(st.session_state.chorus_cards) == len(quiz["correct"]):
            if st.session_state.chorus_cards == quiz["correct"]:
                st.balloons()
                st.success("🎉 완벽합니다! 다음 문제에 도전해보세요!")
            else:
                st.error("❌ 순서가 틀렸어요. 다시 들어보세요!")
                st.markdown("**정답:**")
                for idx, item in enumerate(quiz["correct"]):
                    st.write(f"{idx+1}. {item}")
        
        # 다시 도전 버튼
        if st.button("🔄 다시 도전", type="primary"):
            st.session_state.chorus_cards = []
            st.rerun()
    
    # 진행 상황
    st.divider()
    st.markdown("### 📊 진행 상황")
    progress_cols = st.columns(5)
    for i, q in enumerate(quiz_sets):
        with progress_cols[i]:
            if i == current_quiz:
                st.markdown(f"**🔵 Quiz {i+1}**")
            else:
                st.markdown(f"⚪ Quiz {i+1}")
