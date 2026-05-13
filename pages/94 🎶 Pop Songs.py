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
    .eng-line { font-size: 1.25rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 1.05rem; color: #475569; margin-bottom: 15px; font-weight: 500; }
    .q-label { font-size: 1.2rem; font-weight: 800; color: #0f172a; display: block; margin-top: 15px; }
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
        # 영화의 분위기를 보여주는 이미지 (실제 앱에서는 st.image 사용 권장)
        st.info("🏠 **아렌델 왕국 (Arendelle)**\n\n북유럽의 노르웨이를 모델로 한 아름다운 항구 도시입니다. 평화롭지만 마법을 두려워하는 전통이 있는 곳이죠.")

    with col_txt:
        st.markdown("""
        <div class="info-box">
            <b>1. 엘사의 저주 혹은 선물</b><br>
            주인공 엘사는 모든 것을 얼려버리는 강력한 마법을 가지고 태어났습니다. 어린 시절 실수로 동생 안나를 다치게 한 후, 부모님은 엘사의 마법을 철저히 숨기도록 가르쳤습니다. "숨기고, 느끼지 마(Conceal, don't feel)."가 엘사의 삶을 지배한 좌우명이었습니다.<br><br>
            <b>2. 대관식 날의 사건</b><br>
            성인이 되어 여왕으로 즉위하는 날, 엘사는 감정을 조절하지 못해 마법을 사람들에게 들키고 맙니다. 사람들은 엘사를 괴물로 생각하고, 겁에 질린 엘사는 아무도 살지 않는 북쪽 산으로 홀로 도망칩니다.<br><br>
            <b>3. 'Let It Go'의 의미</b><br>
            산 정상에 도착한 엘사는 이제 더 이상 남의 눈치를 보며 능력을 숨기지 않기로 결심합니다. 이 노래는 <b>억눌렸던 삶을 던져버리고(Let it go), 진정한 자신의 모습을 찾는 해방감</b>을 노래하고 있습니다.
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# STEP 2: 1절 가사 청취 및 심층 이해
# -------------------------
with tab2:
    st.subheader("📜 전체 가사 감상 및 심층 이해")
    col_v2, col_q2 = st.columns([1.2, 1])
    
    with col_v2:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.write("---")
        # 1절 가사 리스트
        lyrics_v1 = [
            ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
            ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 이곳의 여왕인 것 같아"),
            ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
            ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
            ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
            ("Well, now they know!", "그런데 이제 그들이 알아버렸어!")
        ]
        for eng, kor in lyrics_v1:
            st.markdown(f'<div class="eng-line">{eng}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kor-sub">{kor}</div>', unsafe_allow_html=True)

    with col_q2:
        st.subheader("❓ 심층 이해 퀴즈")
        st.markdown('<span class="q-label">1. 노래 초반, 엘사가 느끼는 감정은 어떠한가요?</span>', unsafe_allow_html=True)
        ans1 = st.radio("a1", ["신나고 자유로움", "외롭고 답답함", "화가 나고 억울함"], index=None, label_visibility="collapsed")
        
        st.markdown('<span class="q-label">2. "Well, now they know!"라고 말할 때 엘사의 마음은?</span>', unsafe_allow_html=True)
        ans2 = st.radio("a2", ["들켜서 절망함", "차라리 잘됐다고 생각함", "다시 돌아가고 싶어함"], index=None, label_visibility="collapsed")
        
        st.markdown('<span class="q-label">3. 가사 속 "isolation"은 무슨 뜻일까요?</span>', unsafe_allow_html=True)
        ans3 = st.radio("a3", ["축제", "고립(혼자 있음)", "마법"], index=None, label_visibility="collapsed")

        if st.button("정답 확인하기"):
            if ans1 == "외롭고 답답함" and ans2 == "차라리 잘됐다고 생각함" and ans3 == "고립(혼자 있음)":
                st.success("대단해요! 가사의 숨은 의미를 잘 파악하셨네요.")
                st.balloons()
            else:
                st.error("가사와 엘사의 상황을 다시 한번 떠올려보세요!")

# -------------------------
# STEP 3: 음성만 듣고 후렴구 배열 (Chorus 집중)
# -------------------------
with tab3:
    st.subheader("🎧 오디오만 듣고 순서 맞추기 (Chorus 집중)")
    st.write("화면을 보지 않고 소리에만 집중해서 후렴구(Chorus) 문장을 완성해보세요!")

    # 음성 파일 업로드/링크 (테스트용으로 오디오 위젯 사용)
    # 실제로는 유튜브 음성만 따거나 st.audio를 사용합니다.
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # 예시 파일
    st.warning("⚠️ 실제 수업 시 노래의 후렴구 부분 음성 파일을 이곳에 연결하세요.")

    # 후렴구 데이터
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

    st.write("---")
    c1, c2 = st.columns(2)
    for i, line in enumerate(chorus_scrambled):
        if (c1 if i % 2 == 0 else c2).button(line, key=f"chorus_{i}", use_container_width=True):
            st.session_state.chorus_cards.append(line)

    if st.session_state.chorus_cards:
        st.markdown("### 📥 내가 나열한 가사:")
        for idx, item in enumerate(st.session_state.chorus_cards):
            st.info(f"{idx+1}. {item}")
        
        if len(st.session_state.chorus_cards) == len(chorus_correct):
            # 후렴구 특성상 중복 문장이 있어 단순 비교보다 흐름이 중요
            if st.session_state.chorus_cards == chorus_correct:
                st.balloons()
                st.success("🎉 완벽합니다! 소리에 완벽히 집중하셨군요!")
            else:
                st.error("순서가 조금 틀렸어요. 다시 한번 들어볼까요?")
            
            if st.button("다시 도전"):
                st.session_state.chorus_cards = []
                st.rerun()
