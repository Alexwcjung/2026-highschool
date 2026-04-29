import streamlit as st
import random
import time
import io
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Speaking Bingo Game",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Time Attack Speaking Bingo")
st.caption("빙고판의 단어를 보고 직접 말하세요. 음성 인식이 성공하면 칸이 체크됩니다!")

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
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
    }

    .hero-title {
        font-size: 28px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 10px;
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

    .bingo-card {
        background: white;
        border-radius: 24px;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.07);
        border: 1px solid #e9d5ff;
        margin-bottom: 20px;
    }

    .word-cell {
        background: #ffffff;
        border: 2px solid #dbeafe;
        border-radius: 18px;
        min-height: 76px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 10px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
    }

    .marked-cell {
        background: linear-gradient(135deg, #bbf7d0, #dbeafe);
        border: 2px solid #22c55e;
        border-radius: 18px;
        min-height: 76px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
        font-weight: 900;
        color: #14532d;
        margin-bottom: 10px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
    }

    .message-box {
        background: #fff7ed;
        border-left: 7px solid #fb923c;
        border-radius: 18px;
        padding: 16px 18px;
        margin: 18px 0;
        font-size: 17px;
        font-weight: 800;
        color: #7c2d12;
    }

    .recognized-box {
        background: #f8fafc;
        border-radius: 18px;
        padding: 16px 18px;
        border: 1px solid #e2e8f0;
        margin: 14px 0;
        font-size: 18px;
        font-weight: 800;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        font-size: 16px;
        min-height: 45px;
        border: 1px solid #d1d5db;
    }

    .stButton > button:hover {
        border-color: #ec4899;
        color: #ec4899;
        background: #fdf2f8;
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
        <div class="hero-title">🎯 게임 방법</div>
        <div class="hero-text">
            1. <b>게임 시작</b> 버튼을 누릅니다.<br>
            2. 빙고판에 있는 영어 단어 중 하나를 골라 직접 말합니다.<br>
            3. 음성 인식이 성공하면 해당 단어 칸이 체크됩니다.<br>
            4. 제한 시간 안에 가로, 세로, 대각선 한 줄을 완성하면 <b>BINGO!</b>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 단어 데이터
# =========================
word_groups = {
    "🌱 사람·학교·동작": [
        "person", "man", "woman", "child", "baby", "boy", "girl", "friend", "family", "parent",
        "father", "mother", "brother", "sister", "son", "daughter", "teacher", "student", "classmate", "neighbor",
        "customer", "worker", "driver", "doctor", "nurse", "owner", "guest", "team", "member",
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
# 음성 인식 함수
# =========================
def recognize_speech(audio_bytes):
    recognizer = sr.Recognizer()

    try:
        audio_file = sr.AudioFile(io.BytesIO(audio_bytes))

        with audio_file as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data, language="en-US")
        return text.lower().strip()

    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
    except Exception:
        return ""


# =========================
# 빙고 함수
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

    for r in range(size):
        if all(marked[r][c] for c in range(size)):
            lines += 1

    for c in range(size):
        if all(marked[r][c] for r in range(size)):
            lines += 1

    if all(marked[i][i] for i in range(size)):
        lines += 1

    if all(marked[i][size - 1 - i] for i in range(size)):
        lines += 1

    return lines


def normalize_text(text):
    return text.lower().strip().replace(".", "").replace(",", "").replace("!", "").replace("?", "")


def init_game_state(group_name, words, size):
    prefix = f"speak_bingo_{group_name}_{size}"

    if f"{prefix}_board" not in st.session_state:
        st.session_state[f"{prefix}_board"] = make_board(words, size, f"{group_name}_{size}_board")
        st.session_state[f"{prefix}_marked"] = [[False for _ in range(size)] for _ in range(size)]
        st.session_state[f"{prefix}_score"] = 0
        st.session_state[f"{prefix}_started"] = False
        st.session_state[f"{prefix}_start_time"] = None
        st.session_state[f"{prefix}_time_limit"] = 90
        st.session_state[f"{prefix}_message"] = "게임 시작 버튼을 눌러 주세요."
        st.session_state[f"{prefix}_recognized"] = ""

    return prefix


def reset_game(prefix):
    keys_to_delete = [key for key in st.session_state.keys() if key.startswith(prefix)]
    for key in keys_to_delete:
        del st.session_state[key]


def find_word_on_board(board, marked, size, spoken_text):
    spoken_text = normalize_text(spoken_text)

    if not spoken_text:
        return None

    spoken_words = spoken_text.split()

    for r in range(size):
        for c in range(size):
            target = normalize_text(board[r][c])

            if marked[r][c]:
                continue

            # 정확히 말한 경우
            if spoken_text == target:
                return r, c

            # 인식 결과 문장 안에 단어가 들어간 경우
            if target in spoken_words:
                return r, c

    return None


# =========================
# 게임 출력 함수
# =========================
def show_speaking_bingo(group_name, words):
    st.markdown(
        f"""
        <div class="theme-header">
            <div class="theme-title">{group_name}</div>
            <div class="theme-desc">빙고판에 있는 단어를 직접 말해서 칸을 채우세요.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_size, col_time = st.columns(2)

    with col_size:
        size = st.radio(
            "빙고판 크기",
            [3, 4, 5],
            index=0,
            horizontal=True,
            key=f"{group_name}_size_select"
        )

    with col_time:
        time_limit = st.selectbox(
            "제한 시간",
            [60, 90, 120, 180],
            index=1,
            key=f"{group_name}_time_select"
        )

    prefix = init_game_state(group_name, words, size)

    # 제한 시간 반영
    st.session_state[f"{prefix}_time_limit"] = time_limit

    board = st.session_state[f"{prefix}_board"]
    marked = st.session_state[f"{prefix}_marked"]
    score = st.session_state[f"{prefix}_score"]
    started = st.session_state[f"{prefix}_started"]
    start_time = st.session_state[f"{prefix}_start_time"]
    message = st.session_state[f"{prefix}_message"]
    recognized = st.session_state[f"{prefix}_recognized"]

    bingo_lines = count_bingo_lines(marked, size)

    # 시간 계산
    if started and start_time is not None:
        elapsed = int(time.time() - start_time)
        remaining = max(0, time_limit - elapsed)
    else:
        elapsed = 0
        remaining = time_limit

    # 시간 종료 처리
    if started and remaining <= 0 and bingo_lines == 0:
        st.session_state[f"{prefix}_started"] = False
        st.session_state[f"{prefix}_message"] = "⏰ 시간 종료! 다시 도전해 봅시다."
        st.rerun()

    # 점수판
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="score-box">
                ⏰ 남은 시간<br>{remaining}초
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="score-box">
                ⭐ 맞힌 단어<br>{score}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="score-box">
                🎯 빙고 줄<br>{bingo_lines}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="score-box">
                🧩 전체 칸<br>{size * size}
            </div>
            """,
            unsafe_allow_html=True
        )

    # 버튼
    col_start, col_reset = st.columns(2)

    with col_start:
        if st.button("▶️ 게임 시작", use_container_width=True, key=f"{prefix}_start"):
            st.session_state[f"{prefix}_started"] = True
            st.session_state[f"{prefix}_start_time"] = time.time()
            st.session_state[f"{prefix}_message"] = "빙고판에 있는 단어 중 하나를 골라 크게 말하세요!"
            st.rerun()

    with col_reset:
        if st.button("🔄 새 빙고판 만들기", use_container_width=True, key=f"{prefix}_reset"):
            reset_game(prefix)
            st.rerun()

    # 메시지
    if "BINGO" in message:
        st.balloons()
        st.success(message)
    elif "정답" in message or "성공" in message:
        st.success(message)
    elif "시간 종료" in message or "인식 실패" in message:
        st.warning(message)
    else:
        st.info(message)

    # 음성 인식
    st.markdown("### 🎤 단어 말하기")

    if not started:
        st.write("게임 시작 버튼을 누른 뒤 말하기를 시작하세요.")
    else:
        audio = mic_recorder(
            start_prompt="🎙️ 녹음 시작",
            stop_prompt="⏹️ 녹음 끝",
            just_once=True,
            use_container_width=True,
            key=f"{prefix}_mic_{score}_{remaining}_{bingo_lines}"
        )

        if audio:
            audio_bytes = audio["bytes"]
            spoken_text = recognize_speech(audio_bytes)
            st.session_state[f"{prefix}_recognized"] = spoken_text

            result = find_word_on_board(board, marked, size, spoken_text)

            if result is not None:
                r, c = result
                word = board[r][c]

                st.session_state[f"{prefix}_marked"][r][c] = True
                st.session_state[f"{prefix}_score"] += 1

                new_bingo_lines = count_bingo_lines(st.session_state[f"{prefix}_marked"], size)

                if new_bingo_lines > bingo_lines:
                    st.session_state[f"{prefix}_started"] = False
                    st.session_state[f"{prefix}_message"] = f"🎉 BINGO! {word} 단어를 말해서 빙고 완성!"
                else:
                    st.session_state[f"{prefix}_message"] = f"✅ 정답! {word} 칸이 체크되었습니다."

                st.rerun()

            else:
                if spoken_text:
                    st.session_state[f"{prefix}_message"] = f"🤔 인식된 말: {spoken_text} / 빙고판에 있는 단어를 다시 말해 보세요."
                else:
                    st.session_state[f"{prefix}_message"] = "🎤 인식 실패! 조금 더 크게 또박또박 말해 보세요."

                st.rerun()

    if recognized:
        st.markdown(
            f"""
            <div class="recognized-box">
                🗣️ 최근 인식된 말: {recognized}
            </div>
            """,
            unsafe_allow_html=True
        )

    # 빙고판
    st.markdown("### 🎯 Bingo Board")
    st.markdown('<div class="bingo-card">', unsafe_allow_html=True)

    for r in range(size):
        cols = st.columns(size)

        for c in range(size):
            word = board[r][c]
            is_marked = marked[r][c]

            with cols[c]:
                if is_marked:
                    st.markdown(
                        f"""
                        <div class="marked-cell">
                            ✅ {word}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div class="word-cell">
                            {word}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    st.markdown('</div>', unsafe_allow_html=True)

    # 자동 시간 갱신
    if started and bingo_lines == 0 and remaining > 0:
        time.sleep(1)
        st.rerun()


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(word_groups.keys()))

for tab, group_name in zip(tabs, word_groups.keys()):
    with tab:
        show_speaking_bingo(group_name, word_groups[group_name])
