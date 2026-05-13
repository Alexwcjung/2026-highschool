import streamlit as st
import random
import time

# =========================
# 1. 페이지 설정 및 디자인
# =========================
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

# CSS: 디자인 요소
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f8fafc; padding: 20px; border-radius: 15px;
        border: 2px solid #6366f1; text-align: center; color: #4338ca; margin-bottom: 20px;
    }
    .info-box {
        background-color: #f1f5f9; padding: 20px; border-radius: 12px;
        border: 1px solid #cbd5e1; line-height: 1.6; margin-bottom: 20px;
    }
    .lyrics-container {
        padding: 10px 15px; border-left: 4px solid #6366f1;
        margin-bottom: 10px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 초기화
# -------------------------
if 'selected_song' not in st.session_state:
    st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state:
    st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state:
    st.session_state.q3_cards = []
if 'show_q3_result' not in st.session_state:
    st.session_state.show_q3_result = False

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state:
        del st.session_state.scrambled

# -------------------------
# 상단 곡 선택 메뉴 (1~4번 확실히 부여)
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King"
]

# 곡 선택 시 바로 리셋되도록 설정
song_choice = st.selectbox("학습할 노래를 선택하세요", song_options, key="song_selector_unique")

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# 곡별 데이터 라이브러리
# -------------------------
songs_data = {
    "1. Let It Go - Frozen OST": {
        "url": "https://www.youtube.com/watch?v=L0MK7qz13bU",
        "desc": "<h3>❄️ Let It Go</h3><p>자유와 해방을 노래하는 겨울왕국 메인 테마곡입니다.</p>",
        "lyrics": [("The snow glows white", "눈이 하얗게 빛나네요"), ("Let it go!", "다 잊어버려!")],
        "quiz": [("기분이 어떤가요?", ["해방감", "슬픔"], "해방감")]
    },
    "2. Hello - Adele": {
        "url": "https://www.youtube.com/watch?v=YQHsXMglC9A",
        "desc": "<h3>☎️ Hello</h3><p>아델의 파워풀한 보컬이 돋보이는 사과의 노래입니다.</p>",
        "lyrics": [("Hello, it's me", "안녕, 나야"), ("I'm sorry", "미안해요")],
        "quiz": [("주제는?", ["사과", "화남"], "사과")]
    },
    "3. A Whole New World - Aladdin OST": {
        "url": "https://www.youtube.com/watch?v=eitDnP0_83k",
        "desc": "<h3>✨ A Whole New World</h3><p>알라딘과 자스민의 환상적인 모험을 담은 곡입니다.</p>",
        "lyrics": [("I can show you the world", "세상을 보여줄게요"), ("A whole new world", "완전히 새로운 세상")],
        "quiz": [("무엇을 타고 있나요?", ["양탄자", "마차"], "양탄자")]
    },
    "4. Stand By Me - Ben E. King": {
        "url": "https://www.youtube.com/watch?v=Us-TVg40ExM",
        "desc": "<h3>🤝 Stand By Me</h3><p>영원한 우정과 신뢰를 노래하는 올드팝 명곡입니다.</p>",
        "lyrics": [("When the night has come", "밤이 찾아올 때"), ("Stand by me", "내 곁에 있어줘")],
        "quiz": [("핵심 메시지는?", ["신뢰", "돈"], "신뢰")]
    }
}

current_data = songs_data[song_choice]
video_url = current_data["url"]
# 영상 충돌 방지를 위한 곡별 고유 ID 생성 (특수문자 제거)
safe_id = song_choice.split(".")[0].strip()

# -------------------------
# 메인 탭 구성
# -------------------------
tab1, tab2, tab3 = st.tabs(["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 맞추기"])

with tab1:
    st.markdown(f'<div class="info-box">{current_data["desc"]}</div>', unsafe_allow_html=True)
    # 중복 ID 에러 원천 차단: key에 탭 이름과 곡 ID를 모두 포함
    st.video(video_url, key=f"vid_tab1_{safe_id}")

with tab2:
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.video(video_url, key=f"vid_tab2_{safe_id}")
        st.divider()
        st.subheader("💡 확인 퀴즈")
        with st.form(key=f"quiz_form_{safe_id}"):
            for i, (q, opts, ans) in enumerate(current_data["quiz"]):
                st.radio(q, opts, index=None, key=f"q_{safe_id}_{i}")
            if st.form_submit_button("채점하기"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col2:
        st.subheader("🎼 핵심 가사")
        for eng, kor in current_data["lyrics"]:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 문장 순서 맞추기")
    correct_order = [line[0] for line in current_data["lyrics"]]
    
    if 'scrambled' not in st.session_state:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    
    st.write("아래 버튼을 순서대로 누르세요:")
    cols = st.columns(2)
    for i, txt in enumerate(st.session_state.scrambled):
        is_used = txt in st.session_state.q3_cards
        if (cols[0] if i%2==0 else cols[1]).button(txt, key=f"btn_{safe_id}_{i}", use_container_width=True, disabled=is_used):
            st.session_state.q3_cards.append(txt)
            st.rerun()
            
    st.divider()
    if st.button("🔄 다시 하기", key=f"reset_{safe_id}"):
        st.session_state.q3_cards = []
        st.session_state.show_q3_result = False
        st.rerun()

    # 선택된 카드들 보여주기
    for idx, val in enumerate(st.session_state.q3_cards):
        st.info(f"{idx+1}: {val}")
        
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 결과 확인", type="primary", key=f"fin_{safe_id}"):
            st.session_state.show_q3_result = True
            st.rerun()
            
    if st.session_state.show_q3_result:
        for i, user_val in enumerate(st.session_state.q3_cards):
            if user_val == correct_order[i]:
                st.success(f"{i+1}번 문장: 정답!")
            else:
                st.error(f"{i+1}번 문장: 오답 (정답: {correct_order[i]})")
