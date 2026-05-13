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
    if 'scrambled' in st.session_state: del st.session_state.scrambled

# -------------------------
# 상단 곡 선택 메뉴 (1, 2, 3, 4 번호 추가)
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King"
]

# selectbox에 고유 key 부여
song_choice = st.selectbox("Song Selection", song_options, label_visibility="collapsed", key="global_song_selector")

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# 곡별 데이터 빌드
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_text = "<h3>❄️ Let It Go</h3><p>자신의 마법을 숨기던 엘사가 진정한 자유를 찾는 순간입니다.</p>"
    full_lyrics = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어요"),
        ("Don't let them in, don't let them see", "그들을 들이지 마세요, 보여주지 마세요"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마세요, 모르게 하세요"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어버려요! 더 이상 참을 수 없어요")
    ]
    questions = [("1. 엘사의 기분은?", ["행복", "해방감", "슬픔"], "해방감"), ("2. 'Conceal'의 뜻?", ["숨기다", "보여주다", "웃다"], "숨기다")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_text = "<h3>☎️ Hello</h3><p>과거의 인연에게 건네는 뒤늦은 사과와 그리움을 담은 곡입니다.</p>"
    full_lyrics = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어할지 궁금했어"),
        ("Hello from the other side", "반대편에서 인사할게"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done", "내가 한 모든 일들에 대해 미안하다고 말하려고")
    ]
    questions = [("1. 화자의 목적은?", ["사과", "부탁", "자랑"], "사과"), ("2. 'Thousand times'의 뜻?", ["딱 천 번", "아주 많이", "열 번"], "아주 많이")]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_text = "<h3>✨ A Whole New World</h3><p>알라딘과 자스민이 마법 양탄자를 타고 새로운 세상을 경험하는 노래입니다.</p>"
    full_lyrics = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 어른거리며 화려한 세상을요"),
        ("A whole new world!", "완전히 새로운 세상!"),
        ("A new fantastic point of view", "새롭고 환상적인 시야가 펼쳐져요"),
        ("No one to tell us 'No' or where to go", "누구도 우리에게 안 된다거나 어디로 가라고 말 못해요")
    ]
    questions = [("1. 무엇을 타고 있나요?", ["양탄자", "비행기", "배"], "양탄자"), ("2. 기분이 어떤가요?", ["지루함", "경이로움", "화남"], "경이로움")]

else: # 4. Stand By Me
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_text = "<h3>🤝 Stand By Me</h3><p>어두운 밤에도 곁에 누군가 있다면 두렵지 않다는 우정의 메시지입니다.</p>"
    full_lyrics = [
        ("When the night has come and the land is dark", "밤이 오고 세상이 어두워질 때"),
        ("And the moon is the only light we'll see", "우리가 볼 수 있는 건 달빛뿐일 때"),
        ("No, I won't be afraid", "난 두렵지 않을 거예요"),
        ("Just as long as you stand by me", "당신이 내 곁에 있어 주기만 한다면요")
    ]
    questions = [("1. 시간적 배경은?", ["아침", "낮", "밤"], "밤"), ("2. 'Stand by me'의 뜻?", ["내 뒤에 서라", "내 곁에 있어라", "일어서라"], "내 곁에 있어라")]

# -------------------------
# 탭 구성 (각 영상 위젯에 고유 Key 부여 필수)
# -------------------------
tab1, tab2, tab3 = st.tabs(["1. 🎬 배경 학습", "2. 📖 전체 가사 & 퀴즈", "3. 🧩 순서 배열"])

with tab1:
    st.markdown(f'<div class="info-box">{bg_text}</div>', unsafe_allow_html=True)
    # 탭 1 영상 (ID: vid_tab_1)
    st.video(video_url, key="vid_tab_1")

with tab2:
    col_v, col_l = st.columns([1, 1.2])
    with col_v:
        # 탭 2 영상 (ID: vid_tab_2) - 탭 1 영상과 독립적으로 작동
        st.video(video_url, key="vid_tab_2")
        st.divider()
        st.markdown("### 💡 Quiz Time")
        # 폼에도 고유 ID 부여
        with st.form(key=f"quiz_form_{song_choice}"):
            for i, (q, opts, ans) in enumerate(questions):
                q_label = q
                if st.session_state.submitted_step2:
                    user_val = st.session_state.get(f"user_ans_{i}")
                    q_label += " ✅" if user_val == ans else f" ❌ (정답: {ans})"
                st.radio(q_label, opts, index=None, key=f"user_ans_{i}")
            
            if st.form_submit_button("정답 확인 및 채점"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col_l:
        st.markdown("### 🎼 가사 확인")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 문장 순서 맞추기")
    correct_order = [line[0] for line in full_lyrics]
    
    if 'scrambled' not in st.session_state:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    
    st.write("순서대로 문장을 클릭하세요.")
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        # 버튼에도 고유 키 부여
        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(text, key=f"puzzle_btn_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.session_state.show_q3_result = False
            st.rerun()
            
    st.divider()
    # 선택된 목록
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del_card_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
            
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 결과 확인", type="primary", use_container_width=True, key="final_check_btn"):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.show_q3_result:
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"{i+1}: Perfect!")
            else:
                st.error(f"{i+1}: Wrong Order (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
