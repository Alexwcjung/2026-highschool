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
        border: 1px solid #e2e8f0; line-height: 1.6; margin-bottom: 20px;
    }
    .lyrics-container {
        padding: 8px 15px;
        border-left: 4px solid #38bdf8;
        margin-bottom: 8px;
        background-color: #f1f5f9;
        border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False

st.markdown('<div class="main-title"><h1>❄️ Frozen: Let It Go Interactive Class</h1></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 영화 배경", "📖 STEP 2. 가사 학습 & 퀴즈", "🧩 STEP 3. 1절 전체 순서 맞추기"])

# -------------------------
# STEP 1: 영화 배경 (이미지 제거)
# -------------------------
with tab1:
    col_vid1, col_txt1 = st.columns(2)
    with col_vid1:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    with col_txt1:
        st.markdown("""
        <div class="info-box">
            <h3>🏰 아렌델과 엘사의 이야기</h3>
            엘사는 모든 것을 얼리는 마법을 숨기기 위해 평생 고립된 삶을 살았습니다. 
            대관식 날 비밀이 드러나자 도망친 엘사가 산 위에서 부르는 이 노래는 
            과거의 굴레를 벗어던지고 <b>진정한 자유</b>를 선언하는 순간입니다.
            <br><br>
            이 탭에서 영상을 시청하며 엘사의 감정 변화를 느껴보세요.
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# STEP 2: 가사 학습 & 즉시 체크 퀴즈
# -------------------------
with tab2:
    col_vid2, col_lyrics2 = st.columns([1, 1])
    
    with col_vid2:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        st.divider()
        st.markdown("### 💡 내용 이해 퀴즈 (6문제)")
        
        questions = [
            ("1. 노래 시작 부분의 배경은 어떤 상태인가요?", ["발자국이 가득한 거리", "아무도 없는 고립된 눈산", "햇살이 비치는 해변"], "아무도 없는 고립된 눈산"),
            ("2. 엘사가 그동안 지켜온 규칙은?", ["말을 많이 해라", "숨기고 느끼지 마라", "문을 항상 열어두어라"], "숨기고 느끼지 마라"),
            ("3. 'Well, now they know!'는 어떤 상황인가요?", ["마법을 영원히 숨기게 됨", "사람들에게 마법을 들킴", "왕국으로 돌아가는 중"], "사람들에게 마법을 들킴"),
            ("4. 'Let it go'의 핵심 의미는?", ["다시 돌아가기", "포기하고 울기", "억눌렸던 것을 놓아주기"], "억눌렸던 것을 놓아주기"),
            ("5. 'The cold never bothered me anyway'의 뜻은?", ["추위는 나를 괴롭힌 적 없다", "날씨가 너무 춥다", "감기에 걸릴 것 같다"], "추위는 나를 괴롭힌 적 없다"),
            ("6. 엘사가 마지막에 '문(door)'을 닫는 행위의 의미는?", ["배가 고파서", "과거와의 단절과 새로운 시작", "청소를 하기 위해"], "과거와의 단절과 새로운 시작")
        ]
        
        user_answers_step2 = []
        for i, (q, opts, ans) in enumerate(questions):
            choice = st.radio(q, opts, index=None, key=f"step2_q{i}")
            user_answers_step2.append(choice)
            if st.session_state.submitted_step2:
                if choice == ans: st.success("✅ 정답!")
                else: st.error(f"❌ 오답! (정답: {ans})")

        if st.button("STEP 2 정답 제출"):
            st.session_state.submitted_step2 = True
            st.rerun()

    with col_lyrics2:
        st.markdown("### ❄️ 전체 가사 (Section 1)")
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
# STEP 3: 문장 순서 맞추기 (실시간 정답 체크)
# -------------------------
with tab3:
    st.subheader("🧩 1절 실시간 순서 맞추기")
    st.write("문장을 클릭하면 즉시 정답 여부가 확인됩니다. 올바른 순서(A→G)로 나열해보세요!")
    
    q3_correct = [
        "A. The snow glows white on the mountain tonight, not a footprint to be seen. A kingdom of isolation, and it looks like I'm the queen.",
        "B. The wind is howling like this swirling storm inside. Couldn't keep it in, heaven knows I tried.",
        "C. Don't let them in, don't let them see. Be the good girl you always have to be.",
        "D. Conceal, don't feel, don't let them know. Well, now they know!",
        "E. Let it go, let it go! Can't hold it back anymore.",
        "F. Let it go, let it go! Turn away and slam the door!",
        "G. I don't care what they're going to say. Let the storm rage on. The cold never bothered me anyway."
    ]
    
    q3_scrambled = [
        "D. Conceal, don't feel, don't let them know. Well, now they know!",
        "A. The snow glows white on the mountain tonight, not a footprint to be seen. A kingdom of isolation, and it looks like I'm the queen.",
        "G. I don't care what they're going to say. Let the storm rage on. The cold never bothered me anyway.",
        "B. The wind is howling like this swirling storm inside. Couldn't keep it in, heaven knows I tried.",
        "F. Let it go, let it go! Turn away and slam the door!",
        "C. Don't let them in, don't let them see. Be the good girl you always have to be.",
        "E. Let it go, let it go! Can't hold it back anymore."
    ]
    
    cols = st.columns(2)
    for i, sentence in enumerate(q3_scrambled):
        if (cols[0] if i % 2 == 0 else cols[1]).button(sentence, key=f"q3_btn_{i}", use_container_width=True):
            if sentence not in st.session_state.q3_cards:
                st.session_state.q3_cards.append(sentence)
                st.rerun()

    st.divider()
    st.markdown("### 📥 실시간 채점 결과")
    
    correct_count = 0
    for idx, s in enumerate(st.session_state.q3_cards):
        col_text, col_del = st.columns([0.85, 0.15])
        
        # 현재 위치의 정답 문장과 비교
        if s == q3_correct[idx]:
            col_text.success(f"✅ 단계 {idx+1} (정답): {s}")
            correct_count += 1
        else:
            col_text.error(f"❌ 단계 {idx+1} (오답): {s}")
            
        if col_del.button("삭제", key=f"del_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    # 모든 정답을 맞혔을 때 피드백
    if correct_count == len(q3_correct):
        st.balloons()
        st.success("🎉 완벽합니다! 1절의 모든 문장을 올바른 감정 흐름에 맞춰 완성하셨습니다!")
    
    if len(st.session_state.q3_cards) > 0:
        if st.button("전체 초기화"):
            st.session_state.q3_cards = []
            st.rerun()
