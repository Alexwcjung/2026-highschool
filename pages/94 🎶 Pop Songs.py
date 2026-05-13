import streamlit as st
import random
import string

# 1. 기본 설정 및 디자인
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f8fafc; padding: 25px; border-radius: 15px;
        border: 2px solid #6366f1; text-align: center; color: #4338ca; margin-bottom: 25px;
    }
    .big-label {
        font-size: 1.8rem !important; font-weight: 800 !important;
        color: #1e3a8a !important; margin-bottom: 15px !important; display: block;
    }
    .info-box {
        background-color: #f1f5f9; padding: 35px; border-radius: 15px;
        border: 1px solid #cbd5e1; line-height: 2.0; margin-bottom: 25px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 3px solid #6366f1; padding-bottom: 12px; font-size: 1.6rem; }
    .info-box b { color: #1e3a8a; }
    .lyrics-container {
        padding: 12px 20px; border-left: 5px solid #6366f1;
        margin-bottom: 10px; background-color: #f8fafc; border-radius: 0 10px 10px 0;
    }
    .eng-line { font-size: 1.15rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.95rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 핵심 해결책: 세션 상태 관리 (초기화 로직 최적화)
# ==========================================
song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST"
]

# 위젯이 리렌더링될 때 값이 날아가지 않도록 세션 초기화
if 'selected_song' not in st.session_state:
    st.session_state.selected_song = song_options[0]
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"
if 'q3_cards' not in st.session_state:
    st.session_state.q3_cards = []
if 'submitted_step2' not in st.session_state:
    st.session_state.submitted_step2 = False
if 'show_q3_result' not in st.session_state:
    st.session_state.show_q3_result = False

# 곡 선택 UI
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)

# 곡이 바뀌면 모든 상태 리셋
def on_song_change():
    st.session_state.q3_cards = []
    st.session_state.submitted_step2 = False
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state:
        del st.session_state.scrambled

current_song = st.selectbox("", song_options, key="song_selector", on_change=on_song_change)
st.session_state.selected_song = current_song

# 탭 선택 UI (라디오 버튼 대신 탭 위젯 사용 - 이동 오류가 훨씬 적음)
tab1, tab2, tab3 = st.tabs(["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"])

# -------------------------
# 3. 데이터 설정
# -------------------------
if "1. Let It Go" in current_song:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 완벽함을 강요받는 사회에서의 탈출</h3>
    <p><b>[작품 배경]</b> 디즈니 애니메이션 '겨울왕국'의 엘사는 태어날 때부터 통제할 수 없는 강력한 마법 능력을 가졌습니다. 그녀의 부모는 능력을 숨기라고 가르쳤고, 엘사는 평생을 자신을 억누르며 '착한 소녀(Good girl)'로 살기 위해 고군분투했습니다. 이 곡은 그녀의 비밀이 온 세상에 탄로나고, 모든 것을 내려놓은 뒤 홀로 북쪽 산으로 향하며 부르는 노래입니다.</p>
    <p><b>[문학적 해석]</b> 노래 초반부의 '고립된 왕국'은 엘사의 심리적 폐쇄성을 상징합니다. 하지만 곡이 진행될수록 엘사는 자신의 능력을 더 이상 '저주'가 아닌 '자아의 일부'로 받아들입니다. 가사 속 <b>"Conceal, don't feel"</b>은 감정을 억압해야 했던 과거를, <b>"Let it go"</b>는 타인의 시선에서 해방되어 진정한 자신의 모습으로 살겠다는 선언을 담고 있습니다.</p>
    <p><b>[핵심 메시지]</b> 이 곡은 전 세계적으로 <b>'자기 수용(Self-Acceptance)'</b>의 찬가가 되었습니다. "추위는 더 이상 나를 괴롭히지 못한다"는 선언은, 나를 옥죄던 세상의 차가운 편견조차 나의 자존감을 꺾을 수 없음을 시사합니다.</p>
    """
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나고"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 말고, 모르게 해"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어")
    ]
    questions = [("1. 엘사의 현재 주요 심경은?", ["해방감", "공포", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"), ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 날씨", "겨울 휴가"], "사회적 시선")]

elif "2. Hello" in current_song:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 상처와 조우하는 용기</h3>
    <p><b>[작품 배경]</b> 아델(Adele)의 이 노래는 단순히 헤어진 연인에게 보내는 편지가 아니라, <b>'과거의 자신과 화해하고 싶은 마음'</b>을 담고 있습니다. 나이가 들면서 잊고 지냈던 소중한 사람들, 그리고 한때 순수했던 예전의 나에게 건네는 안부입니다.</p>
    <p><b>[문학적 해석]</b> <b>"Hello from the other side"</b>라는 표현은 중의적입니다. 물리적으로는 전화기 너머를 뜻하지만, 은유적으로는 '성장이 끝난 현재의 나'가 '미숙했던 과거의 나'를 바라보는 경계를 의미합니다.</p>
    """
    lyrics_raw = [
        ("Hello, it's me. I was wondering if you'd like to meet", "안녕, 나야. 네가 만나고 싶어 할지 궁금했어"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야")
    ]
    questions = [("1. 화자가 전화를 거는 이유는?", ["사과", "돈", "심심해서"], "사과")]
else:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = "<h3>✨ A Whole New World</h3><p>새로운 시야에 대한 이야기입니다.</p>"
    lyrics_raw = [("I can show you the world", "세상을 보여줄게요")]
    questions = [("1. 주제는?", ["자유", "잠"], "자유")]

# -------------------------
# 4. 각 탭의 내용 구성
# -------------------------
with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

with tab2:
    col_left, col_right = st.columns([1, 1.2])
    with col_left:
        st.video(video_url)
        st.markdown("### 💡 Quiz")
        # 폼(Form)을 사용하여 한 번에 처리 (인식 오류 방지)
        with st.form(key=f"quiz_{current_song}"):
            for i, (q, opts, ans) in enumerate(questions):
                st.radio(q, opts, key=f"q_{current_song}_{i}")
            if st.form_submit_button("정답 제출"):
                st.session_state.submitted_step2 = True
                st.write("채점이 완료되었습니다!")
    with col_right:
        for eng, kor in lyrics_raw:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 가사를 올바른 순서대로 클릭하세요")
    
    # 섞인 가사 생성
    correct_order = [f"{i+1}. {line[0]}" for i, line in enumerate(lyrics_raw)]
    if 'scrambled' not in st.session_state:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    
    # 가사 선택 버튼들
    cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        btn_col = cols[i % 2]
        already_selected = text in st.session_state.q3_cards
        if btn_col.button(text, key=f"btn_{current_song}_{i}", disabled=already_selected, use_container_width=True):
            st.session_state.q3_cards.append(text)
            st.rerun()

    # 선택된 결과 표시
    st.markdown("---")
    st.write("📝 **내가 선택한 순서:**")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("❌", key=f"del_{current_song}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 정답 확인", type="primary"):
            for i, val in enumerate(st.session_state.q3_cards):
                if val == correct_order[i]: st.success(f"{i+1}번: 맞았습니다!")
                else: st.error(f"{i+1}번: 틀렸습니다! (정답: {correct_order[i]})")
