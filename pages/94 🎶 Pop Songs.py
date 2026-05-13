import streamlit as st
import random

# =========================
# 1. 페이지 설정 및 스타일
# =========================
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f8fafc; padding: 25px; border-radius: 15px;
        border: 2px solid #6366f1; text-align: center; color: #4338ca; margin-bottom: 25px;
    }
    .big-label {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #1e3a8a !important;
        margin-bottom: 15px !important;
        display: block;
    }
    .info-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 12px;
        border: 1px solid #cbd5e1; line-height: 1.8; margin-bottom: 20px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 2px solid #cbd5e1; padding-bottom: 10px; margin-top: 0; }
    .lyrics-container {
        padding: 8px 15px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 초기화
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'show_q3_result' not in st.session_state: st.session_state.show_q3_result = False

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state:
        del st.session_state.scrambled

# -------------------------
# 상단 곡 선택 메뉴
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King"
]

song_choice = st.selectbox("Song Selection", song_options, label_visibility="collapsed", key="song_selector_main")

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# 곡별 데이터 설정
# -------------------------
if "1. Let It Go" in song_choice:
    v_id = "letitgo"
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_text = "<h3>❄️ Let It Go</h3><p>엘사가 진정한 자유를 선언하는 명곡입니다.</p>"
    full_lyrics = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어버려요! 더 이상 참을 수 없어요")
    ]
    questions = [("1. 엘사의 상태는?", ["행복", "해방감", "슬픔"], "해방감")]

elif "2. Hello" in song_choice:
    v_id = "hello"
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_text = "<h3>☎️ Hello</h3><p>과거의 인연에게 전하는 진심 어린 사과입니다.</p>"
    full_lyrics = [
        ("Hello, it's me", "안녕, 나야"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything", "미안하다고 말하기 위해서")
    ]
    questions = [("1. 노래의 목적은?", ["사과", "부탁", "자랑"], "사과")]

elif "3. A Whole New World" in song_choice:
    v_id = "aladdin"
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_text = "<h3>✨ A Whole New World</h3><p>새로운 세상을 향한 경이로움을 담았습니다.</p>"
    full_lyrics = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("A whole new world!", "완전히 새로운 세상!"),
        ("A new fantastic point of view", "환상적인 새로운 시야")
    ]
    questions = [("1. 무엇을 타고 있나요?", ["양탄자", "배", "구름"], "양탄자")]

else:
    v_id = "standbyme"
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_text = "<h3>🤝 Stand By Me</h3><p>곁에 누군가 있다면 시련도 두렵지 않다는 노래입니다.</p>"
    full_lyrics = [
        ("When the night has come and the land is dark", "밤이 오고 세상이 어두워질 때"),
        ("No, I won't be afraid", "난 두렵지 않을 거예요"),
        ("Just as long as you stand by me", "당신이 내 곁에 있어 주기만 한다면")
    ]
    questions = [("1. 화자가 원하는 것은?", ["우정/신뢰", "돈", "잠"], "우정/신뢰")]

# -------------------------
# 탭 및 영상 위젯 (핵심 수정 부분)
# -------------------------
tab1, tab2, tab3 = st.tabs(["1. 🎬 배경 학습", "2. 📖 전체 가사 & 퀴즈", "3. 🧩 순서 배열"])

with tab1:
    st.markdown(f'<div class="info-box">{bg_text}</div>', unsafe_allow_html=True)
    # 탭 1 영상: 곡 ID + tab1 조합으로 고유 키 생성
    st.video(video_url, key=f"video_{v_id}_tab1")

with tab2:
    col_v, col_l = st.columns([1, 1.2])
    with col_v:
        # 탭 2 영상: 곡 ID + tab2 조합으로 고유 키 생성 (절대 충돌 없음)
        st.video(video_url, key=f"video_{v_id}_tab2")
        st.divider()
        st.markdown("### 💡 퀴즈 풀기")
        with st.form(key=f"form_{v_id}"):
            for i, (q, opts, ans) in enumerate(questions):
                st.radio(q, opts, index=None, key=f"q_{v_id}_{i}")
            if st.form_submit_button("제출"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col_l:
        st.markdown("### 🎼 가사 해석")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 순서 맞추기")
    correct_order = [line[0] for line in full_lyrics]
    if 'scrambled' not in st.session_state:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(text, key=f"btn_{v_id}_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
            
    st.divider()
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del_{v_id}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
    
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 정답 확인", key=f"final_{v_id}"):
            st.session_state.show_q3_result = True
            st.rerun()
    
    if st.session_state.show_q3_result:
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"{i+1}: 정답!")
            else: st.error(f"{i+1}: 오답 (원래 순서: {correct_order[i]})")
