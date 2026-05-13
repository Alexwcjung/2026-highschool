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
# CSS 디자인 (강조 및 잠금 효과)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } 
    .title-box {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 25px;
    }
    .lyrics-row {
        padding: 12px;
        margin: 5px 0;
        border-radius: 8px;
        font-size: 1.3rem;
        transition: all 0.3s;
    }
    /* 현재 풀어야 할 가사 강조 */
    .active-row {
        background-color: rgba(56, 189, 248, 0.25);
        border-left: 6px solid #38bdf8;
        font-weight: bold;
    }
    /* 아직 도달하지 않은 가사 흐리게 */
    .locked-row {
        color: #475569;
        filter: blur(1px);
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Step-by-Step</h1><p>정답을 맞춰야 다음 가사가 나타납니다!</p></div>', unsafe_allow_html=True)

# =========================
# 세션 상태 초기화 (진행 단계 관리)
# =========================
if 'step' not in st.session_state:
    st.session_state.step = 1  # 1단계부터 시작
if 'score' not in st.session_state:
    st.session_state.score = 0

# 문제 데이터
questions = [
    {"id": 1, "text": "The snow glows white on the...", "options": ["mountain", "fountain"], "ans": "mountain", "after": "tonight, Not a footprint to be seen."},
    {"id": 2, "text": "A kingdom of...", "options": ["isolation", "imagination"], "ans": "isolation", "after": "And it looks like I'm the queen."},
    {"id": 3, "text": "The wind is howling like this...", "options": ["swirling", "swinging"], "ans": "swirling", "after": "storm inside. Heaven knows I tried."},
    {"id": 4, "text": "Don't let them in, don't let them see. Be the good girl you always have to be...", "options": ["conceal", "reveal"], "ans": "conceal", "after": "don't feel, don't let them know."},
    {"id": 5, "text": "Let it go, let it go. Can't hold it back...", "options": ["anymore", "anyhow"], "ans": "anymore", "after": "Turn away and slam the door!"}
]

# =========================
# 메인 레이아웃
# =========================
col_v, col_l = st.columns([1, 1.2])

with col_v:
    st.subheader("🎬 Watch & Listen")
    st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    
    st.divider()
    st.metric("Progress", f"{st.session_state.step - 1} / 5 Solved")
    st.progress((st.session_state.step - 1) / 5)
    
    if st.session_state.step > 5:
        st.balloons()
        st.success("Perfect! 모든 단어를 찾아냈습니다! ❄️")
        if st.button("다시 도전하기"):
            st.session_state.step = 1
            st.rerun()

with col_l:
    st.subheader("📜 Interactive Lyrics")

    for i, q in enumerate(questions):
        current_num = i + 1
        
        # 1. 이미 푼 문제들 (결과 표시)
        if st.session_state.step > current_num:
            st.markdown(f'<div class="lyrics-row">{q["text"]} **{q["ans"]}**</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="lyrics-row text-dim">{q["after"]}</div>', unsafe_allow_html=True)
            st.divider()

        # 2. 현재 풀어야 할 문제
        elif st.session_state.step == current_num:
            st.markdown(f'<div class="lyrics-row active-row">{q["text"]}</div>', unsafe_allow_html=True)
            
            # 선택지 버튼
            choice = st.radio(f"Select word for Step {current_num}", q["options"], index=None, key=f"q{current_num}", horizontal=True)
            
            if choice:
                if choice == q["ans"]:
                    st.success("Correct! 다음 줄로 넘어갑니다.")
                    if st.button("Next Line →", key=f"btn{current_num}"):
                        st.session_state.step += 1
                        st.rerun()
                else:
                    st.error("다시 한 번 잘 들어보세요!")
            break # 현재 단계 아래는 보여주지 않음

        # 3. 아직 잠겨있는 문제들
        else:
            st.markdown(f'<div class="lyrics-row locked-row">Next lyrics is locked...</div>', unsafe_allow_html=True)
