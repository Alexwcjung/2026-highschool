import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Lyrics Training: Let It Go",
    page_icon="❄️",
    layout="wide"
)

# =========================
# 고급 CSS 디자인 (A/B 선택 강조)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } 
    .title-box {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    .lyrics-window {
        background-color: #1e293b;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #38bdf8;
        height: 500px;
        overflow-y: auto;
        line-height: 3.0;
        font-size: 1.25rem;
        font-family: 'Courier New', monospace;
        color: #e2e8f0;
    }
    .choice-tag {
        color: #fbbf24;
        font-weight: bold;
        background-color: #334155;
        padding: 3px 8px;
        border-radius: 6px;
        border: 1px solid #fbbf24;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Verse 1 Training</h1><p>노래를 들으며 가사 속 [ A / B ] 중 들리는 단어를 순서대로 고르세요!</p></div>', unsafe_allow_html=True)

# =========================
# 1절 데이터 설정 (A/B 보기)
# =========================
questions = [
    {"id": 1, "options": ["mountain", "fountain"], "ans": "mountain"},
    {"id": 2, "options": ["footsteps", "footprints"], "ans": "footprints"},
    {"id": 3, "options": ["isolation", "imagination"], "ans": "isolation"},
    {"id": 4, "options": ["swirling", "swinging"], "ans": "swirling"},
    {"id": 5, "options": ["heaven", "hidden"], "ans": "heaven"},
    {"id": 6, "options": ["conceal", "reveal"], "ans": "conceal"},
    {"id": 7, "options": ["anymore", "anyhow"], "ans": "anymore"},
    {"id": 8, "options": ["rage", "race"], "ans": "rage"}
]

# =========================
# 메인 레이아웃 (영상 | 가사 및 퀴즈)
# =========================
tab_play, tab_result = st.tabs(["🎮 Game Mode", "📊 My Score"])

with tab_play:
    col_v, col_l = st.columns([1, 1.2])

    with col_v:
        st.subheader("🎬 Watch & Listen")
        # 1절 분량에 집중할 수 있도록 영상 배치[cite: 1]
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
        
        st.divider()
        st.markdown("### 👂 가사를 들으며 고르세요!")
        
        # 가사 순서대로 Radio 버튼 배치[cite: 1]
        user_answers = []
        c1, c2 = st.columns(2)
        for i, q in enumerate(questions):
            target_col = c1 if i < 4 else c2
            choice = target_col.radio(
                f"Question {q['id']}", 
                q['options'], 
                index=None, 
                key=f"q_{q['id']}"
            )
            user_answers.append(choice)

    with col_l:
        st.subheader("📜 Lyrics (Verse 1)")
        # 1절 가사 내에 선택지를 직접 노출하여 가독성 증대[cite: 1]
        lyrics_html = """
        <div class="lyrics-window">
        The snow glows white on the <span class="choice-tag">1. mountain / fountain</span> tonight<br>
        Not a <span class="choice-tag">2. footsteps / footprints</span> to be seen<br>
        A kingdom of <span class="choice-tag">3. isolation / imagination</span><br>
        And it looks like I'm the queen<br><br>
        The wind is howling like this <span class="choice-tag">4. swirling / swinging</span> storm inside<br>
        Couldn't keep it in, <span class="choice-tag">5. heaven / hidden</span> knows I tried<br><br>
        Don't let them in, don't let them see<br>
        Be the good girl you always have to be<br>
        <span class="choice-tag">6. conceal / reveal</span>, don't feel, don't let them know<br>
        Well, now they know!<br><br>
        Let it go, let it go<br>
        Can't hold it back <span class="choice-tag">7. anymore / anyhow</span><br>
        Let it go, let it go<br>
        Turn away and slam the door!<br><br>
        I don't care what they're going to say<br>
        Let the storm <span class="choice-tag">8. rage / race</span> on<br>
        The cold never bothered me anyway
        </div>
        """
        st.markdown(lyrics_html, unsafe_allow_html=True)

# =========================
# 결과 탭
# =========================
with tab_result:
    st.subheader("📊 Your Score")
    score = 0
    if None in user_answers:
        st.warning("아직 풀지 않은 문제가 있습니다!")
    
    for i, q in enumerate(questions):
        if user_answers[i] == q['ans']:
            score += 1
            st.success(f"{i+1}번: 정답! ({q['ans']})")
        elif user_answers[i] is not None:
            st.error(f"{i+1}번: 오답 (정답: {q['ans']})")
            
    st.divider()
    st.metric("Total Score", f"{score} / {len(questions)}")
    if score == len(questions):
        st.balloons()
        st.success("1절 마스터! 정말 잘 들으셨네요! ❄️")
