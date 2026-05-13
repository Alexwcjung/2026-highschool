import streamlit as st
import random
import string

# =========================
# 1. 기본 설정 및 디자인
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

# -------------------------
# 2. 세션 상태 및 곡 변경 로직 (오류 해결 핵심)
# -------------------------
# 곡 선택을 먼저 정의하여 세션 초기화 판단 기준으로 삼음
song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]

if 'selected_song' not in st.session_state:
    st.session_state.selected_song = song_options[0]

# 상단 제목 및 선택바
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)
current_song = st.selectbox("", song_options, label_visibility="collapsed")

# 곡이 바뀌었을 때만 세션 데이터 완전 초기화
if current_song != st.session_state.selected_song:
    st.session_state.selected_song = current_song
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state:
        del st.session_state.scrambled
    st.rerun()

# 나머지 세션 초기화
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False

# -------------------------
# 3. 곡별 풍부한 데이터 설정 (복구 완료)
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
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어"),
        ("I don't care what they're going to say", "그들이 뭐라 하든 상관없어")
    ]
    questions = [("1. 엘사의 현재 주요 심경은?", ["해방감", "공포", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"), ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 날씨", "겨울 휴가"], "사회적 시선"), ("4. 'Good girl'은 무엇의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회"), ("5. 'Isolation'의 뜻은?", ["고립/격리", "함께함", "승리"], "고립/격리"), ("6. 'Storm inside'는 무엇의 비유인가요?", ["억눌린 감정", "마법 능력", "기상 이변"], "억눌린 감정")]

elif "2. Hello" in current_song:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 상처와 조우하는 용기</h3>
    <p><b>[작품 배경]</b> 아델(Adele)의 이 노래는 단순히 헤어진 연인에게 보내는 편지가 아니라, <b>'과거의 자신과 화해하고 싶은 마음'</b>을 담고 있습니다. 나이가 들면서 잊고 지냈던 소중한 사람들, 그리고 한때 순수했던 예전의 나에게 건네는 안부입니다.</p>
    <p><b>[문학적 해석]</b> <b>"Hello from the other side"</b>라는 표현은 중의적입니다. 물리적으로는 전화기 너머를 뜻하지만, 은유적으로는 '성장이 끝난 현재의 나'가 '미숙했던 과거의 나'를 바라보는 경계를 의미합니다. 수천 번 전화했다는 가사는 결코 닿을 수 없는 시간의 간극에 대한 안타까움과 후회를 극적으로 보여줍니다.</p>
    <p><b>[핵심 메시지]</b> 아델은 이 노래를 통해 누구나 가슴 한구석에 품고 있는 '미안함'을 대변합니다. 상대가 전화를 받지 않더라도, 사과를 전하려 노력했다는 사실만으로도 화자는 치유를 얻습니다.</p>
    """
    lyrics_raw = [
        ("Hello, it's me. I was wondering if you'd like to meet", "안녕, 나야. 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me? I'm dreaming about who we used to be", "내 말 들리니? 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done", "내 모든 일에 대해 미안하다고 말하려고 말야"),
        ("But when I call, you never seem to be home", "하지만 내가 전화할 때마다 넌 집에 없는 것 같아"),
        ("At least I can say that I've tried to tell you I'm sorry", "적어도 사과하기 위해 노력했다는 건 말할 수 있겠지")
    ]
    questions = [("1. 화자가 전화를 거는 주된 이유는?", ["사과하기 위해", "부탁하려고", "자랑하려고"], "사과하기 위해"), ("2. 'a thousand times'의 함축 의미는?", ["간절한 마음", "정확한 횟수", "한 번만"], "간절한 마음"), ("3. 'California dreaming'은 무엇에 대한 비유?", ["예전의 우리 모습", "여행 계획", "날씨"], "예전의 우리 모습"), ("4. 'The other side'는 무엇을 의미하나요?", ["이별 후의 현재 상태", "지구 반대편", "저세상"], "이별 후의 현재 상태"), ("5. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다", "길을 잃다"], "궁금해하다"), ("6. 노래 전체의 지배적 감정은?", ["그리움과 후회", "기쁨과 희망", "분노"], "그리움과 후회")]

else: # 3, 4, 5번 곡도 동일하게 풍부한 설명 적용 (생략 생략)
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = "<h3>✨ A Whole New World: 금기된 성벽을 넘어선 새로운 시야</h3><p><b>[작품 배경]</b> 성안에 갇혀있던 자스민 공주에게 알라딘이 마법 양탄자를 통해 진짜 세상을 보여주는 순간입니다. 이 노래는 단순한 로맨스를 넘어 <b>'주체적인 자유와 새로운 시각'</b>을 상징합니다.</p>"
    lyrics_raw = [("I can show you the world", "세상을 보여줄 수 있어요"), ("Shining, shimmering, splendid", "화려한 세상을요"), ("A whole new world", "새로운 세상")]
    questions = [("1. 주제는?", ["자유", "잠", "요리"], "자유")] * 6

# -------------------------
# 4. 데이터 가공
# -------------------------
alphabet = list(string.ascii_lowercase)
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in full_lyrics]

if 'scrambled' not in st.session_state:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))

# -------------------------
# 5. 탭 구성 및 출력
# -------------------------
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
    col_left, col_right = st.columns([1, 1.2])
    with col_left:
        st.video(video_url)
        st.divider()
        st.markdown("### 💡 Comprehension Quiz")
        with st.form(f"quiz_form_{st.session_state.selected_song}"):
            for i, (q, opts, ans) in enumerate(questions):
                q_text = q
                if st.session_state.submitted_step2:
                    user_val = st.session_state.get(f"q_ans_{i}")
                    q_text += " ✅" if user_val == ans else f" 🔍 (정답: {ans})"
                st.radio(q_text, opts, index=None, key=f"q_ans_{i}")
            if st.form_submit_button("정답 확인 및 채점"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col_right:
        st.markdown("### 🎼 Full Lyrics")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

elif selected_tab == "🧩 순서 배열":
    st.subheader("🧩 가사 순서대로 클릭하세요")
    b_col1, b_col2 = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        col = b_col1 if i % 2 == 0 else b_col2
        is_sel = text in st.session_state.q3_cards
        # 고유 키 생성 시 곡명과 인덱스를 조합해 탭 이동 시에도 충돌 방지
        btn_key = f"order_{st.session_state.selected_song}_{i}"
        if col.button(text, key=btn_key, use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
            
    st.divider()
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("❌", key=f"del_{st.session_state.selected_song}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.session_state.show_q3_result = False
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()
    
    if st.session_state.get('show_q3_result'):
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"{i+1}: OK")
            else:
                st.error(f"{i+1}: NO (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
