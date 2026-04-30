import streamlit as st
from gtts import gTTS
import io
import random

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="단어 말판 게임",
    page_icon="🎲",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 44px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 4px;
    }

    .sub-title {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 24px;
    }

    .hero-box {
        background: linear-gradient(135deg, #fce7f3 0%, #e0f2fe 50%, #fef3c7 100%);
        border-radius: 26px;
        padding: 24px 28px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
        line-height: 1.8;
    }

    .status-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 24px;
        padding: 22px 24px;
        margin: 18px 0;
        text-align: center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border: 1.5px solid #bbf7d0;
    }

    .current-word-box {
        background: white;
        border-radius: 26px;
        padding: 24px;
        margin: 18px 0;
        text-align: center;
        border: 3px solid #fed7aa;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }

    .board-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
        margin-top: 18px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        border: 1px solid #d1d5db;
        padding: 0.45rem 1rem;
    }

    .stButton > button:hover {
        border-color: #ec4899;
        color: #ec4899;
    }

    @media (max-width: 700px) {
        .main-title {
            font-size: 32px;
        }

        .board-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 제목
# =========================
st.markdown("<div class='main-title'>🎲 단어 말판 게임</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>주사위를 굴려 도착한 칸의 영어 단어를 읽고 뜻을 말하는 모둠 게임입니다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <b>📌 게임 방법</b><br>
        1. 테마를 고르고 모둠 수와 말판 칸 수를 정합니다.<br>
        2. 모둠이 차례대로 주사위를 굴립니다.<br>
        3. 도착한 칸의 <b>영어 단어를 읽고 뜻을 말합니다.</b><br>
        4. 맞으면 그 자리에 머물고, 틀리면 뒤로 이동합니다.<br>
        5. 먼저 마지막 칸에 도착한 모둠이 승리합니다.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS 함수
# =========================
@st.cache_data
def make_tts_audio(text, lang="en", tld="com"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def audio_button(label, text, key):
    if st.button(label, key=key):
        audio_bytes = make_tts_audio(text)
        st.audio(audio_bytes, format="audio/mp3")


# =========================
# 테마별 단어 데이터
# =========================
word_themes = {
    "🧑‍🤝‍🧑 사람·관계": [
        {"word": "person", "meaning": "사람"},
        {"word": "man", "meaning": "남자"},
        {"word": "woman", "meaning": "여자"},
        {"word": "child", "meaning": "아이"},
        {"word": "baby", "meaning": "아기"},
        {"word": "boy", "meaning": "소년"},
        {"word": "girl", "meaning": "소녀"},
        {"word": "friend", "meaning": "친구"},
        {"word": "family", "meaning": "가족"},
        {"word": "parent", "meaning": "부모"},
        {"word": "father", "meaning": "아버지"},
        {"word": "mother", "meaning": "어머니"},
        {"word": "brother", "meaning": "형제, 남자 형제"},
        {"word": "sister", "meaning": "자매, 여자 형제"},
        {"word": "son", "meaning": "아들"},
        {"word": "daughter", "meaning": "딸"},
        {"word": "teacher", "meaning": "선생님"},
        {"word": "student", "meaning": "학생"},
        {"word": "classmate", "meaning": "반 친구"},
        {"word": "neighbor", "meaning": "이웃"},
        {"word": "customer", "meaning": "손님, 고객"},
        {"word": "worker", "meaning": "노동자, 직원"},
        {"word": "driver", "meaning": "운전자"},
        {"word": "doctor", "meaning": "의사"},
        {"word": "nurse", "meaning": "간호사"},
        {"word": "police officer", "meaning": "경찰관"},
        {"word": "owner", "meaning": "주인"},
        {"word": "guest", "meaning": "손님"},
        {"word": "team", "meaning": "팀, 무리"},
        {"word": "member", "meaning": "구성원"},
    ],

    "🏫 학교·교실": [
        {"word": "school", "meaning": "학교"},
        {"word": "class", "meaning": "수업, 학급"},
        {"word": "classroom", "meaning": "교실"},
        {"word": "lesson", "meaning": "수업, 과"},
        {"word": "homework", "meaning": "숙제"},
        {"word": "test", "meaning": "시험"},
        {"word": "exam", "meaning": "시험"},
        {"word": "quiz", "meaning": "퀴즈, 간단한 시험"},
        {"word": "question", "meaning": "질문, 문제"},
        {"word": "answer", "meaning": "대답, 정답"},
        {"word": "book", "meaning": "책"},
        {"word": "notebook", "meaning": "공책"},
        {"word": "paper", "meaning": "종이, 보고서"},
        {"word": "pen", "meaning": "펜"},
        {"word": "pencil", "meaning": "연필"},
        {"word": "desk", "meaning": "책상"},
        {"word": "chair", "meaning": "의자"},
        {"word": "board", "meaning": "칠판, 게시판"},
        {"word": "page", "meaning": "쪽, 페이지"},
        {"word": "word", "meaning": "단어, 말"},
        {"word": "sentence", "meaning": "문장"},
        {"word": "story", "meaning": "이야기"},
        {"word": "language", "meaning": "언어"},
        {"word": "English", "meaning": "영어"},
        {"word": "Korean", "meaning": "한국어"},
        {"word": "grade", "meaning": "성적, 학년"},
        {"word": "score", "meaning": "점수"},
        {"word": "rule", "meaning": "규칙"},
        {"word": "practice", "meaning": "연습하다, 연습"},
        {"word": "study", "meaning": "공부하다"},
    ],

    "🏃 기본 동작 동사": [
        {"word": "go", "meaning": "가다"},
        {"word": "come", "meaning": "오다"},
        {"word": "walk", "meaning": "걷다"},
        {"word": "run", "meaning": "달리다"},
        {"word": "sit", "meaning": "앉다"},
        {"word": "stand", "meaning": "서다"},
        {"word": "stop", "meaning": "멈추다"},
        {"word": "start", "meaning": "시작하다"},
        {"word": "open", "meaning": "열다"},
        {"word": "close", "meaning": "닫다"},
        {"word": "make", "meaning": "만들다"},
        {"word": "do", "meaning": "하다"},
        {"word": "have", "meaning": "가지다, 먹다"},
        {"word": "get", "meaning": "얻다, 받다, 되다"},
        {"word": "take", "meaning": "가져가다, 타다"},
        {"word": "give", "meaning": "주다"},
        {"word": "put", "meaning": "놓다, 두다"},
        {"word": "bring", "meaning": "가져오다"},
        {"word": "use", "meaning": "사용하다"},
        {"word": "find", "meaning": "찾다"},
        {"word": "keep", "meaning": "유지하다, 보관하다"},
        {"word": "leave", "meaning": "떠나다, 남기다"},
        {"word": "move", "meaning": "움직이다, 이사하다"},
        {"word": "turn", "meaning": "돌다, 돌리다"},
        {"word": "wait", "meaning": "기다리다"},
        {"word": "help", "meaning": "돕다"},
        {"word": "try", "meaning": "시도하다"},
        {"word": "need", "meaning": "필요하다"},
        {"word": "want", "meaning": "원하다"},
        {"word": "like", "meaning": "좋아하다"},
    ],

    "💖 감정·성격": [
        {"word": "happy", "meaning": "행복한"},
        {"word": "sad", "meaning": "슬픈"},
        {"word": "angry", "meaning": "화난"},
        {"word": "tired", "meaning": "피곤한"},
        {"word": "hungry", "meaning": "배고픈"},
        {"word": "thirsty", "meaning": "목마른"},
        {"word": "excited", "meaning": "신난"},
        {"word": "bored", "meaning": "지루한"},
        {"word": "afraid", "meaning": "두려워하는"},
        {"word": "worried", "meaning": "걱정하는"},
        {"word": "proud", "meaning": "자랑스러워하는"},
        {"word": "kind", "meaning": "친절한"},
        {"word": "nice", "meaning": "좋은, 친절한"},
        {"word": "brave", "meaning": "용감한"},
        {"word": "honest", "meaning": "정직한"},
        {"word": "friendly", "meaning": "친근한"},
        {"word": "quiet", "meaning": "조용한"},
        {"word": "shy", "meaning": "수줍은"},
        {"word": "smart", "meaning": "똑똑한"},
        {"word": "strong", "meaning": "강한"},
        {"word": "weak", "meaning": "약한"},
        {"word": "careful", "meaning": "조심하는"},
        {"word": "lazy", "meaning": "게으른"},
        {"word": "busy", "meaning": "바쁜"},
        {"word": "ready", "meaning": "준비된"},
        {"word": "sorry", "meaning": "미안한"},
        {"word": "thankful", "meaning": "감사하는"},
        {"word": "lonely", "meaning": "외로운"},
        {"word": "nervous", "meaning": "긴장한"},
        {"word": "calm", "meaning": "차분한"},
    ],

    "🍎 음식·건강": [
        {"word": "food", "meaning": "음식"},
        {"word": "rice", "meaning": "밥, 쌀"},
        {"word": "bread", "meaning": "빵"},
        {"word": "water", "meaning": "물"},
        {"word": "milk", "meaning": "우유"},
        {"word": "juice", "meaning": "주스"},
        {"word": "coffee", "meaning": "커피"},
        {"word": "tea", "meaning": "차"},
        {"word": "apple", "meaning": "사과"},
        {"word": "banana", "meaning": "바나나"},
        {"word": "egg", "meaning": "달걀"},
        {"word": "meat", "meaning": "고기"},
        {"word": "fish", "meaning": "생선, 물고기"},
        {"word": "chicken", "meaning": "닭고기, 닭"},
        {"word": "vegetable", "meaning": "채소"},
        {"word": "fruit", "meaning": "과일"},
        {"word": "breakfast", "meaning": "아침 식사"},
        {"word": "lunch", "meaning": "점심 식사"},
        {"word": "dinner", "meaning": "저녁 식사"},
        {"word": "snack", "meaning": "간식"},
        {"word": "healthy", "meaning": "건강한"},
        {"word": "sick", "meaning": "아픈"},
        {"word": "pain", "meaning": "통증"},
        {"word": "headache", "meaning": "두통"},
        {"word": "medicine", "meaning": "약"},
        {"word": "hospital", "meaning": "병원"},
        {"word": "exercise", "meaning": "운동하다, 운동"},
        {"word": "sleep", "meaning": "자다, 잠"},
        {"word": "rest", "meaning": "쉬다, 휴식"},
        {"word": "wash", "meaning": "씻다"},
    ],

    "🚗 장소·이동": [
        {"word": "home", "meaning": "집"},
        {"word": "house", "meaning": "집"},
        {"word": "room", "meaning": "방"},
        {"word": "kitchen", "meaning": "부엌"},
        {"word": "bathroom", "meaning": "화장실, 욕실"},
        {"word": "door", "meaning": "문"},
        {"word": "window", "meaning": "창문"},
        {"word": "city", "meaning": "도시"},
        {"word": "town", "meaning": "마을"},
        {"word": "country", "meaning": "나라, 시골"},
        {"word": "street", "meaning": "거리"},
        {"word": "road", "meaning": "도로"},
        {"word": "park", "meaning": "공원"},
        {"word": "store", "meaning": "가게"},
        {"word": "market", "meaning": "시장"},
        {"word": "station", "meaning": "역"},
        {"word": "bus", "meaning": "버스"},
        {"word": "car", "meaning": "자동차"},
        {"word": "bike", "meaning": "자전거"},
        {"word": "train", "meaning": "기차"},
        {"word": "plane", "meaning": "비행기"},
        {"word": "ship", "meaning": "배"},
        {"word": "map", "meaning": "지도"},
        {"word": "place", "meaning": "장소"},
        {"word": "here", "meaning": "여기"},
        {"word": "there", "meaning": "거기"},
        {"word": "left", "meaning": "왼쪽"},
        {"word": "right", "meaning": "오른쪽, 맞는"},
        {"word": "near", "meaning": "가까운"},
        {"word": "far", "meaning": "먼"},
    ],
}

# =========================
# 게임 상태 함수
# =========================
def init_board_game(theme_name, theme_words, board_size, team_count):
    prefix = f"board_game_{theme_name}"

    board_key = f"{prefix}_words"
    pos_key = f"{prefix}_positions"
    turn_key = f"{prefix}_turn"
    dice_key = f"{prefix}_dice"
    msg_key = f"{prefix}_message"
    finished_key = f"{prefix}_finished"

    if board_key not in st.session_state:
        words = theme_words[:]

        if len(words) < board_size:
            repeated = []
            while len(repeated) < board_size:
                repeated.extend(words)
            words = repeated[:board_size]
        else:
            random.seed(f"{theme_name}_{board_size}")
            words = random.sample(words, board_size)

        st.session_state[board_key] = words

    if pos_key not in st.session_state:
        st.session_state[pos_key] = [0 for _ in range(team_count)]

    if turn_key not in st.session_state:
        st.session_state[turn_key] = 0

    if dice_key not in st.session_state:
        st.session_state[dice_key] = "-"

    if msg_key not in st.session_state:
        st.session_state[msg_key] = "🎲 주사위를 굴려 게임을 시작하세요!"

    if finished_key not in st.session_state:
        st.session_state[finished_key] = False

    return board_key, pos_key, turn_key, dice_key, msg_key, finished_key


def reset_board_game(theme_name):
    prefix = f"board_game_{theme_name}"
    delete_keys = [key for key in st.session_state.keys() if key.startswith(prefix)]

    for key in delete_keys:
        del st.session_state[key]


# =========================
# 게임 설정
# =========================
st.markdown("### 🎲 게임 설정")

theme_name = st.selectbox(
    "단어 테마를 선택하세요.",
    list(word_themes.keys())
)

theme_words = word_themes[theme_name]

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    team_count = st.slider(
        "모둠 수",
        min_value=2,
        max_value=6,
        value=4,
        step=1
    )

with col_b:
    board_size = st.slider(
        "말판 칸 수",
        min_value=12,
        max_value=30,
        value=20,
        step=2
    )

with col_c:
    penalty = st.slider(
        "틀리면 뒤로",
        min_value=0,
        max_value=3,
        value=1,
        step=1
    )

with col_d:
    show_meaning = st.checkbox(
        "말판에 뜻 보이기",
        value=True
    )

board_key, pos_key, turn_key, dice_key, msg_key, finished_key = init_board_game(
    theme_name,
    theme_words,
    board_size,
    team_count
)

board_words = st.session_state[board_key]
positions = st.session_state[pos_key]

if len(positions) != team_count:
    st.session_state[pos_key] = [0 for _ in range(team_count)]
    positions = st.session_state[pos_key]
    st.session_state[turn_key] = 0

current_turn = st.session_state[turn_key]

if current_turn >= team_count:
    current_turn = 0
    st.session_state[turn_key] = 0

# =========================
# 상태판
# =========================
st.markdown(
    f"""
    <div class="status-box">
        <div style="font-size:30px; font-weight:900; color:#14532d;">
            현재 차례: {current_turn + 1}모둠
        </div>
        <div style="font-size:21px; font-weight:800; color:#334155; margin-top:8px;">
            🎲 마지막 주사위: {st.session_state[dice_key]}
        </div>
        <div style="font-size:18px; font-weight:700; color:#475569; margin-top:8px;">
            {st.session_state[msg_key]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 현재 단어
# =========================
current_position = positions[current_turn]
current_word_item = board_words[current_position]

st.markdown(
    f"""
    <div class="current-word-box">
        <div style="font-size:18px; font-weight:900; color:#9a3412;">
            {current_turn + 1}모둠 현재 단어
        </div>
        <div style="font-size:48px; font-weight:900; color:#111827; margin-top:8px;">
            {current_word_item["word"]}
        </div>
        <div style="font-size:26px; font-weight:800; color:#2563eb; margin-top:8px;">
            뜻: {current_word_item["meaning"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

audio_button(
    "🔊 현재 단어 발음 듣기",
    current_word_item["word"],
    key=f"audio_{theme_name}_{current_turn}_{current_position}"
)

# =========================
# 조작 버튼
# =========================
col_roll, col_correct, col_wrong, col_reset = st.columns(4)

with col_roll:
    if st.button("🎲 주사위 굴리기", use_container_width=True):
        if not st.session_state[finished_key]:
            dice = random.randint(1, 6)
            st.session_state[dice_key] = dice

            new_pos = positions[current_turn] + dice

            if new_pos >= board_size - 1:
                new_pos = board_size - 1
                positions[current_turn] = new_pos
                st.session_state[msg_key] = f"🎉 {current_turn + 1}모둠이 마지막 칸에 도착했습니다! 단어를 맞히면 승리!"
            else:
                positions[current_turn] = new_pos
                word = board_words[new_pos]["word"]
                st.session_state[msg_key] = f"🚀 {current_turn + 1}모둠이 {dice}칸 이동했습니다. 단어 '{word}'를 말해 보세요!"

            st.rerun()

with col_correct:
    if st.button("✅ 맞았어요", use_container_width=True):
        if not st.session_state[finished_key]:
            if positions[current_turn] >= board_size - 1:
                st.session_state[finished_key] = True
                st.session_state[msg_key] = f"🏆 {current_turn + 1}모둠 승리!"
                st.balloons()
            else:
                st.session_state[msg_key] = f"✅ {current_turn + 1}모둠 정답! 다음 모둠 차례입니다."
                st.session_state[turn_key] = (current_turn + 1) % team_count

            st.rerun()

with col_wrong:
    if st.button("❌ 틀렸어요", use_container_width=True):
        if not st.session_state[finished_key]:
            old_pos = positions[current_turn]
            new_pos = max(0, old_pos - penalty)
            positions[current_turn] = new_pos

            st.session_state[msg_key] = f"😢 {current_turn + 1}모둠 오답! {penalty}칸 뒤로 이동합니다."
            st.session_state[turn_key] = (current_turn + 1) % team_count

            st.rerun()

with col_reset:
    if st.button("🔄 게임 리셋", use_container_width=True):
        reset_board_game(theme_name)
        st.rerun()

st.markdown("---")

# =========================
# 말판 출력
# =========================
st.markdown("### 🗺️ 말판")

team_colors = ["🔴", "🔵", "🟢", "🟡", "🟣", "🟠"]

board_html = """
<div class="board-grid">
"""

for i, item in enumerate(board_words):
    teams_here = []

    for team_idx, pos in enumerate(positions):
        if pos == i:
            teams_here.append(f"{team_colors[team_idx]}{team_idx + 1}")

    if i == board_size - 1:
        bg = "linear-gradient(135deg, #fef3c7, #fecaca)"
        border = "#f97316"
        label = "🏁 FINISH"
    elif i == 0:
        bg = "linear-gradient(135deg, #dcfce7, #dbeafe)"
        border = "#22c55e"
        label = "START"
    else:
        bg = "white"
        border = "#e5e7eb"
        label = f"{i + 1}"

    markers = " ".join(teams_here)

    meaning_html = (
        f"""
        <div style="font-size:14px; font-weight:700; color:#475569; margin-top:4px;">
            {item["meaning"]}
        </div>
        """
        if show_meaning else ""
    )

    board_html += f"""
    <div style="
        min-height:112px;
        background:{bg};
        border:3px solid {border};
        border-radius:18px;
        padding:10px;
        box-shadow:0 4px 10px rgba(0,0,0,0.06);
        text-align:center;
    ">
        <div style="font-size:13px; font-weight:900; color:#64748b;">
            {label}
        </div>
        <div style="font-size:22px; font-weight:900; color:#111827; margin-top:6px;">
            {item["word"]}
        </div>
        {meaning_html}
        <div style="font-size:18px; font-weight:900; margin-top:6px;">
            {markers}
        </div>
    </div>
    """

board_html += "</div>"

st.markdown(board_html, unsafe_allow_html=True)

st.markdown("---")

# =========================
# 모둠 위치
# =========================
st.markdown("### 📍 모둠 위치")

cols = st.columns(team_count)

for i in range(team_count):
    with cols[i]:
        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border-radius:18px;
                padding:16px;
                text-align:center;
                border:2px solid #dbeafe;
                box-shadow:0 4px 10px rgba(0,0,0,0.05);
            ">
                <div style="font-size:24px; font-weight:900;">
                    {team_colors[i]} {i + 1}모둠
                </div>
                <div style="font-size:18px; font-weight:800; color:#475569; margin-top:6px;">
                    {positions[i] + 1}번 칸
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
