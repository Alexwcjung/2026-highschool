import streamlit as st

# =========================
# 1. 기본 설정 및 디자인
# =========================
st.set_page_config(page_title="Pop Song English Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f8fafc; padding: 25px; border-radius: 15px;
        border: 2px solid #6366f1; text-align: center; color: #4338ca; margin-bottom: 25px;
    }
    .info-box {
        background-color: #f1f5f9; padding: 20px; border-radius: 12px;
        border: 1px solid #cbd5e1; line-height: 1.6; margin-bottom: 20px;
    }
    .lyrics-container {
        padding: 8px 15px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = None
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False

# -------------------------
# 상단 곡 선택 메뉴
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning 🎵</h1></div>', unsafe_allow_html=True)

song_choice = st.selectbox("학습할 노래를 선택하세요:", ["선택하세요", "Let It Go - Frozen OST", "Hello - Adele"], index=0)

if song_choice == "선택하세요":
    st.info("위의 메뉴에서 노래를 선택하면 수업이 시작됩니다!")
    st.stop()

# 곡이 바뀌면 데이터 초기화
if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# 곡별 데이터 설정
# -------------------------
if song_choice == "Let It Go - Frozen OST":
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_text = "엘사는 마법을 숨기기 위해 평생 고립된 삶을 살았습니다. 이 노래는 진정한 자유를 선언하는 순간입니다."
    lyrics_data = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산에 내린 눈은 하얗게 빛나고"),
        ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
        ("Let it go, let it go", "다 잊어, 다 내려놓자"),
        ("Can't hold it back anymore", "더는 억누를 수 없어")
    ]
    questions = [
        ("1. 노래 시작 부분의 배경은?", ["발자국 가득한 거리", "아무도 없는 눈산", "햇살 비치는 해변"], "아무도 없는 눈산"),
        ("2. 'Let it go'의 의미는?", ["다시 돌아가기", "억눌렸던 것을 놓아주기", "포기하기"], "억눌렸던 것을 놓아주기")
    ]
    scrambled_lyrics = [
        "C. A kingdom of isolation, and it looks like I'm the queen.",
        "A. The snow glows white on the mountain tonight.",
        "D. Let it go, let it go! Can't hold it back anymore.",
        "B. Not a footprint to be seen.",
        "E. Turn away and slam the door!"
    ]
    correct_order = [
        "A. The snow glows white on the mountain tonight.",
        "B. Not a footprint to be seen.",
        "C. A kingdom of isolation, and it looks like I'm the queen.",
        "D. Let it go, let it go! Can't hold it back anymore.",
        "E. Turn away and slam the door!"
    ]

else: # Adele - Hello
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_text = "과거의 연인에게 연락을 시도하며 지난날을 회상하고 사과하는 애절한 발라드입니다. 아델의 명확한 발음이 돋보입니다."
    lyrics_data = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "수년이 흐른 지금, 네가 만나고 싶어할지 궁금했어"),
        ("Hello from the other side", "반대편(먼 곳)에서 인사해"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done", "내가 했던 모든 일들에 미안하다고 말하기 위해서")
    ]
    questions = [
        ("1. 'Hello, it's me'는 어떤 상황인가요?", ["자기소개 하기", "전화를 걸어 인사하기", "처음 보는 사람에게 인사"], "전화를 걸어 인사하기"),
        ("2. 'I must've called a thousand times'의 뜻은?", ["천 번 전화했다(강한 추측/강조)", "천 번 전화할 것이다", "전화가 고장 났다"], "천 번 전화했다(강한 추측/강조)")
    ]
    scrambled_lyrics = [
        "B. I was wondering if after all these years you'd like to meet.",
        "D. I must've called a thousand times.",
        "A. Hello, it's me.",
        "E. To tell you I'm sorry for everything that I've done.",
        "C. Hello from the other side."
    ]
    correct_order = [
        "A. Hello, it's me.",
        "B. I was wondering if after all these years you'd like to meet.",
        "C. Hello from the other side.",
        "D. I must've called a thousand times.",
        "E. To tell you I'm sorry for everything that I've done."
    ]

# -------------------------
# 공통 탭 구조
# -------------------------
tab1, tab2, tab3 = st.tabs(["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 맞추기"])

with tab1:
    v1, v2, v3 = st.columns([1, 2, 1])
    with v2: st.video(video_url)
    st.markdown(f'<div class="info-box"><h3>💡 노래 이야기</h3>{bg_text}</div>', unsafe_allow_html=True)

with tab2:
    l_col, q_col = st.columns([1, 1])
    with l_col:
        st.markdown("### ❄️ Lyrics Focus")
        for eng, kor in lyrics_data:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)
    
    with q_col:
        st.markdown("### 💡 Comprehension Quiz")
        with st.form("quiz_form"):
            for i, (q, opts, ans) in enumerate(questions):
                label = q
                if st.session_state.submitted_step2:
                    user_val = st.session_state.get(f"sel_{i}")
                    label += " ✅" if user_val == ans else f" 🔍 (정답: {ans})"
                st.radio(label, opts, index=None, key=f"sel_{i}")
            
            if st.form_submit_button("정답 확인하기"):
                st.session_state.submitted_step2 = True
                st.rerun()

with tab3:
    st.subheader("🧩 가사 순서 완성하기")
    b_cols = st.columns(2)
    for i, text in enumerate(scrambled_lyrics):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[0] if i%2==0 else b_cols[1]).button(text, key=f"q3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.session_state.show_q3_result = False
            st.rerun()
    
    st.divider()
    for idx, c in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {c}")
        if c2.button("🗑️", key=f"del_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
            
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 결과 확인하기", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.get('show_q3_result'):
        all_ok = True
        for i, u_s in enumerate(st.session_state.q3_cards):
            if u_s == correct_order[i]: st.success(f"{i+1}번: 정답!")
            else:
                st.warning(f"{i+1}번: 오답 (정답: {correct_order[i][:30]}...)")
                all_ok = False
        if all_ok: st.balloons()
