import streamlit as st
from gtts import gTTS
import io
import random

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Word Bingo Game",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Word Bingo Game")
st.caption("원어민 발음을 듣고, 빙고판에서 알맞은 영어 단어를 찾아 클릭하세요!")

# =========================
# CSS 디자인
# =========================
st.markdown(
    """
    <style>
    .hero-box {
        background: linear-gradient(135deg, #fce7f3 0%, #e0f2fe 50%, #fef3c7 100%);
        border-radius: 26px;
        padding: 24px 28px;
        margin-bottom: 26px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
    }

    .hero-title {
        font-size: 27px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .hero-text {
        font-size: 16px;
        color: #374151;
        line-height: 1.8;
    }

    .theme-header {
        background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 50%, #06b6d4 100%);
        color: white;
        padding: 20px 24px;
        border-radius: 24px;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(139,92,246,0.25);
    }

    .theme-title {
        font-size: 25px;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .theme-desc {
        font-size: 15px;
        opacity: 0.95;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 22px;
        padding: 18px 22px;
        margin-bottom: 18px;
        border: 1px solid #bbf7d0;
        box-shadow: 0 5px 16px rgba(0,0,0,0.06);
        text-align: center;
        font-size: 23px;
        font-weight: 900;
        color: #14532d;
    }

    .call-box {
        background: #fff7ed;
        border-left: 7px solid #fb923c;
        border-radius: 18px;
        padding: 18px 20px;
        margin: 18px 0;
        font-size: 18px;
        font-weight: 800;
        color: #7c2d12;
    }

    .bingo-card {
        background: white;
        border-radius: 24px;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.07);
        border: 1px solid #e9d5ff;
        margin-bottom: 20px;
    }

    .stButton > button {
        border-radius: 18px;
        font-weight: 900;
        font-size: 18px;
        min-height: 68px;
        border: 2px solid #dbeafe;
        background: #ffffff;
        color: #111827;
    }

    .stButton > button:hover {
        border-color: #ec4899;
        color: #ec4899;
        background: #fdf2f8;
    }

    .small-guide {
        font-size: 15px;
        color: #6b7280;
        line-height: 1.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 안내 박스
# =========================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🌟 단어 빙고 게임 방법</div>
        <div class="hero-text">
            1. <b>새 단어 듣기</b> 버튼을 누릅니다.<br>
            2. 원어민 발음을 듣고, 빙고판에서 해당 단어를 찾습니다.<br>
            3. 맞는 단어를 클릭하면 칸이 표시됩니다.<br>
            4. 가로, 세로, 대각선 한 줄을 완성하면 <b>BINGO!</b>
        </div>
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


def play_audio(text):
    audio_bytes = make_tts_audio(text)
    st.audio(audio_bytes, format="audio/mp3")


# =========================
# 단어 데이터
# =========================
word_groups = {
    "🌱 사람·학교·동작": [
        "person", "man", "woman", "child", "baby", "boy", "girl", "friend", "family", "parent",
        "father", "mother", "brother", "sister", "son", "daughter", "teacher", "student", "classmate", "neighbor",
        "customer", "worker", "driver", "doctor", "nurse", "police officer", "owner", "guest", "team", "member",

        "school", "class", "classroom", "lesson", "homework", "test", "exam", "quiz", "question", "answer",
        "book", "notebook", "paper", "pen", "pencil", "desk", "chair", "board", "page", "word",
        "sentence", "story", "language", "English", "Korean", "grade", "score", "rule", "practice", "study",

        "go", "come", "walk", "run", "sit", "stand", "stop", "start", "open", "close",
        "make", "do", "have", "get", "take", "give", "put", "bring", "use", "find",
        "keep", "leave", "move", "turn", "wait", "help", "try", "need", "want", "like",
    ],

    "💖 감정·상태": [
        "happy", "sad", "angry", "tired", "hungry", "thirsty", "excited", "bored", "afraid", "worried",
        "proud", "kind", "nice", "brave", "honest", "friendly", "quiet", "shy", "smart", "strong",
        "weak", "careful", "lazy", "busy", "ready", "sorry", "thankful", "lonely", "nervous", "calm",

        "good", "bad", "big", "small", "long", "short", "new", "old", "young", "high",
        "low", "fast", "slow", "easy", "hard", "right", "wrong", "same", "different", "important",
        "beautiful", "clean", "dirty", "full", "empty", "free", "safe", "dangerous", "true", "false",
    ],

    "🍎 음식·장소·이동": [
        "food", "rice", "bread", "water", "milk", "juice", "coffee", "tea", "apple", "banana",
        "egg", "meat", "fish", "chicken", "vegetable", "fruit", "breakfast", "lunch", "dinner", "snack",
        "healthy", "sick", "pain", "headache", "medicine", "hospital", "exercise", "sleep", "rest", "wash",

        "home", "house", "room", "kitchen", "bathroom", "door", "window", "city", "town", "country",
        "street", "road", "park", "store", "market", "station", "bus", "car", "bike", "train",
        "plane", "ship", "map", "place", "here", "there", "left", "right", "near", "far",
    ],

    "🌤️ 자연·동물": [
        "sun", "moon", "star", "sky", "cloud", "rain", "snow", "wind", "weather", "air",
        "water", "fire", "tree", "flower", "grass", "mountain", "river", "sea", "beach", "forest",
        "earth", "ground", "rock", "hill", "lake", "island", "cold", "hot", "warm", "cool",

        "dog", "cat", "bird", "fish", "horse", "cow", "pig", "sheep", "goat", "chicken",
        "duck", "rabbit", "mouse", "monkey", "lion", "tiger", "bear", "wolf", "fox", "deer",
        "elephant", "giraffe", "zebra", "snake", "frog", "turtle", "whale", "dolphin", "shark", "penguin",
    ],

    "⏰ 시간·물건·생각": [
        "time", "day", "week", "month", "year", "today", "tomorrow", "yesterday", "morning", "afternoon",
        "evening", "night", "hour", "minute", "second", "early", "late", "now", "before", "after",
        "first", "last", "one", "two", "three", "four", "five", "many", "much", "few",

        "thing", "bag", "box", "cup", "bottle", "phone", "computer", "camera", "key", "money",
        "card", "ticket", "clothes", "shirt", "pants", "shoes", "hat", "watch", "table", "bed",
        "light", "picture", "music", "game", "ball", "tool", "knife", "spoon", "fork", "plate",

        "think", "know", "understand", "remember", "forget", "say", "tell", "speak", "talk", "ask",
        "answer", "call", "listen", "hear", "read", "write", "learn", "teach", "mean", "feel",
        "believe", "hope", "choose", "decide", "explain", "show", "share", "agree", "worry", "thank",
    ],
}

# =========================
# 빙고 관련 함수
# =========================
def make_board(words, size, seed_key):
    random.seed(seed_key)
    selected = random.sample(words, size * size)
    board = []
    idx = 0

    for r in range(size):
        row = []
        for c in range(size):
            row.append(selected[idx])
            idx += 1
        board.append(row)

    return board


def count_bingo_lines(marked, size):
    lines = 0

    # 가로
    for r in range(size):
        if all(marked[r][c] for c in range(size)):
            lines += 1

    # 세로
    for c in range(size):
        if all(marked[r][c] for r in range(size)):
            lines += 1

    # 대각선
    if all(marked[i][i] for i in range(size)):
        lines += 1

    if all(marked[i][size - 1 - i] for i in range(size)):
        lines += 1

    return lines


def init_bingo_state(group_name, words, size):
    prefix = f"bingo_{group_name}_{size}"

    if f"{prefix}_board" not in st.session_state:
        st.session_state[f"{prefix}_board"] = make_board(words, size, f"{group_name}_{size}_board")
        st.session_state[f"{prefix}_marked"] = [[False for _ in range(size)] for _ in range(size)]
        st.session_state[f"{prefix}_called"] = []
        st.session_state[f"{prefix}_current"] = None
        st.session_state[f"{prefix}_message"] = "새 단어 듣기 버튼을 눌러 시작하세요."
        st.session_state[f"{prefix}_score"] = 0

    return prefix


def reset_bingo(prefix):
    keys = [key for key in st.session_state.keys() if key.startswith(prefix)]
    for key in keys:
        del st.session_state[key]


def get_unmarked_words(board, marked, size):
    words = []

    for r in range(size):
        for c in range(size):
            if not marked[r][c]:
                words.append(board[r][c])

    return words


def call_new_word(prefix, size):
    board = st.session_state[f"{prefix}_board"]
    marked = st.session_state[f"{prefix}_marked"]

    remaining = get_unmarked_words(board, marked, size)

    if len(remaining) == 0:
        st.session_state[f"{prefix}_current"] = None
        st.session_state[f"{prefix}_message"] = "모든 단어를 맞혔습니다!"
        return

    current = random.choice(remaining)
    st.session_state[f"{prefix}_current"] = current
    st.session_state[f"{prefix}_called"].append(current)
    st.session_state[f"{prefix}_message"] = "발음을 듣고 빙고판에서 단어를 찾아 클릭하세요."


# =========================
# 빙고 게임 출력 함수
# =========================
def show_bingo_game(group_name, words):
    st.markdown(
        f"""
        <div class="theme-header">
            <div class="theme-title">{group_name}</div>
            <div class="theme-desc">이 묶음의 단어 중 일부가 빙고판에 나옵니다. 발음을 듣고 알맞은 단어를 클릭하세요.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_setting1, col_setting2 = st.columns([1, 2])

    with col_setting1:
        size = st.radio(
            "빙고판 크기",
            [3, 4, 5],
            index=1,
            horizontal=True,
            key=f"{group_name}_size"
        )

    with col_setting2:
        show_answer = st.checkbox(
            "교사용: 현재 정답 단어 보기",
            value=False,
            key=f"{group_name}_show_answer"
        )

    prefix = init_bingo_state(group_name, words, size)

    board = st.session_state[f"{prefix}_board"]
    marked = st.session_state[f"{prefix}_marked"]
    current = st.session_state[f"{prefix}_current"]
    score = st.session_state[f"{prefix}_score"]
    bingo_lines = count_bingo_lines(marked, size)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="score-box">
                ⭐ 맞힌 단어<br>{score}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="score-box">
                🎯 빙고 줄<br>{bingo_lines}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="score-box">
                🧩 전체 칸<br>{size * size}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 🔊 단어 듣기")

    btn1, btn2, btn3 = st.columns(3)

    with btn1:
        if st.button("🎧 새 단어 듣기", use_container_width=True, key=f"{prefix}_call"):
            call_new_word(prefix, size)
            st.rerun()

    with btn2:
        if st.button("🔁 현재 단어 다시 듣기", use_container_width=True, key=f"{prefix}_again"):
            if st.session_state[f"{prefix}_current"] is None:
                st.warning("먼저 새 단어를 들어 주세요.")
            else:
                pass

    with btn3:
        if st.button("🔄 새 빙고판 만들기", use_container_width=True, key=f"{prefix}_reset"):
            reset_bingo(prefix)
            st.rerun()

    current = st.session_state[f"{prefix}_current"]

    if current:
        play_audio(current)

        if show_answer:
            st.markdown(
                f"""
                <div class="call-box">
                    👩‍🏫 교사용 정답: {current}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div class="call-box">
                    🎧 발음을 듣고 빙고판에서 알맞은 단어를 클릭하세요.
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info(st.session_state[f"{prefix}_message"])

    # 빙고판
    st.markdown("### 🎯 Bingo Board")
    st.markdown('<div class="bingo-card">', unsafe_allow_html=True)

    for r in range(size):
        cols = st.columns(size)

        for c in range(size):
            word = board[r][c]
            is_marked = marked[r][c]

            if is_marked:
                label = f"✅ {word}"
            else:
                label = word

            with cols[c]:
                if st.button(label, key=f"{prefix}_cell_{r}_{c}", use_container_width=True):
                    current_word = st.session_state[f"{prefix}_current"]

                    if is_marked:
                        st.session_state[f"{prefix}_message"] = "이미 맞힌 단어입니다."
                        st.rerun()

                    if current_word is None:
                        st.session_state[f"{prefix}_message"] = "먼저 새 단어를 들어 주세요."
                        st.rerun()

                    if word == current_word:
                        st.session_state[f"{prefix}_marked"][r][c] = True
                        st.session_state[f"{prefix}_score"] += 1
                        st.session_state[f"{prefix}_current"] = None

                        new_lines = count_bingo_lines(st.session_state[f"{prefix}_marked"], size)

                        if new_lines > bingo_lines:
                            st.session_state[f"{prefix}_message"] = f"🎉 BINGO! 현재 {new_lines}줄 완성!"
                        else:
                            st.session_state[f"{prefix}_message"] = f"✅ 정답! {word} 단어를 맞혔습니다."

                        st.rerun()

                    else:
                        st.session_state[f"{prefix}_message"] = f"❌ 다시 생각해 봅시다. 선택한 단어: {word}"
                        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    message = st.session_state[f"{prefix}_message"]

    if "BINGO" in message:
        st.balloons()
        st.success(message)
    elif "정답" in message:
        st.success(message)
    elif "다시" in message or "먼저" in message:
        st.warning(message)
    else:
        st.info(message)

    # 최근 불린 단어
    called = st.session_state[f"{prefix}_called"]

    if len(called) > 0:
        with st.expander("📜 지금까지 나온 단어 보기"):
            st.write(", ".join(called))


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(word_groups.keys()))

for tab, group_name in zip(tabs, word_groups.keys()):
    with tab:
        show_bingo_game(group_name, word_groups[group_name])
