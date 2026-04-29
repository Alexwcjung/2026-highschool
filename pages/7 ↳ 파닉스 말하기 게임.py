import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Speaking Boom Game",
    page_icon="💥",
    layout="wide"
)

st.title("💥 Phonics Speaking Boom Game")
st.caption("단어가 차례대로 내려오고, 말하면 단어가 터지는 말하기 게임입니다.")

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .game-box {
        height: 560px;
        border-radius: 28px;
        background: linear-gradient(180deg, #dbeafe 0%, #fef9c3 55%, #ffe4e6 100%);
        border: 4px solid #93c5fd;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 22px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }

    .falling-word {
        position: absolute;
        background: white;
        color: #111827;
        font-size: 38px;
        font-weight: 900;
        padding: 12px 26px;
        border-radius: 24px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.20);
        border: 4px solid #fb923c;
        min-width: 130px;
        text-align: center;
    }

    .score-card {
        background: linear-gradient(135deg, #fff7ed, #fef3c7);
        border-radius: 22px;
        padding: 18px;
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        border: 3px solid #fed7aa;
        box-shadow: 0 5px 12px rgba(0,0,0,0.10);
    }

    .message-box {
        background: linear-gradient(135deg, #fef3c7, #fed7aa);
        border: 4px solid #fb923c;
        border-radius: 26px;
        padding: 18px;
        text-align: center;
        font-size: 30px;
        font-weight: 900;
        color: #7c2d12;
        margin-bottom: 16px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.14);
    }

    .boom-box {
        background: linear-gradient(135deg, #fee2e2, #fca5a5);
        border: 4px solid #ef4444;
        border-radius: 28px;
        padding: 22px;
        text-align: center;
        font-size: 44px;
        font-weight: 900;
        color: #7f1d1d;
        margin-bottom: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.18);
        animation: pop 0.5s ease-in-out;
    }

    @keyframes pop {
        0% { transform: scale(0.7); opacity: 0.3; }
        50% { transform: scale(1.15); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }

    .ready-box {
        background: #ffffff;
        border-radius: 26px;
        padding: 28px;
        margin-top: 20px;
        border: 3px solid #dbeafe;
        box-shadow: 0 6px 16px rgba(0,0,0,0.10);
        text-align: center;
    }

    .ready-title {
        font-size: 54px;
        font-weight: 900;
        color: #1f2937;
    }

    .word-preview {
        background: #f8fafc;
        border-radius: 20px;
        padding: 18px;
        border: 2px solid #e2e8f0;
        font-size: 20px;
        line-height: 1.8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 단어 데이터
# =========================
word_sets = {
    "짧은 모음": [
        "cat", "bat", "hat", "bed", "egg",
        "sit", "pig", "hot", "cup", "bus",
        "fox", "dog", "sun", "jam", "van"
    ],
    "긴 모음": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope",
        "see", "tree", "goat", "rain", "day"
    ],
    "Blends": [
        "black", "brown", "clock", "crab", "drum",
        "flag", "frog", "green", "spoon", "star",
        "blue", "grass", "snake", "smile", "train"
    ],
    "Digraphs": [
        "chair", "ship", "three", "this", "phone",
        "whale", "duck", "shop", "cheese", "photo",
        "fish", "chick", "thin", "thank", "white"
    ],
    "Vowel Teams": [
        "rain", "day", "see", "eat", "boat",
        "snow", "cow", "house", "coin", "boy",
        "road", "team", "seed", "toy", "out"
    ],
    "R-Controlled": [
        "car", "star", "her", "bird", "girl",
        "corn", "fork", "turn", "burn", "teacher",
        "park", "farm", "short", "shirt", "tiger"
    ],
    "Silent e": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope",
        "lake", "time", "nose", "line", "game"
    ],
}

# =========================
# 세션 상태 초기화
# =========================
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "falling_words" not in st.session_state:
    st.session_state.falling_words = []

if "score" not in st.session_state:
    st.session_state.score = 0

if "lives" not in st.session_state:
    st.session_state.lives = 5

if "message" not in st.session_state:
    st.session_state.message = "게임을 시작해 보세요!"

if "used_words" not in st.session_state:
    st.session_state.used_words = []

if "boom_word" not in st.session_state:
    st.session_state.boom_word = ""

if "last_recognized" not in st.session_state:
    st.session_state.last_recognized = ""

if "audio_debug" not in st.session_state:
    st.session_state.audio_debug = ""

if "step_count" not in st.session_state:
    st.session_state.step_count = 0

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
# 단어 관련 함수
# =========================
def get_random_word(words):
    remaining = [w for w in words if w not in st.session_state.used_words]

    if len(remaining) == 0:
        st.session_state.used_words = []
        remaining = words[:]

    word = random.choice(remaining)
    st.session_state.used_words.append(word)
    return word


def add_falling_word(words):
    word = get_random_word(words)

    # 차례대로 내려오게 하기 위해 y 위치를 다르게 시작
    current_count = len(st.session_state.falling_words)

    new_item = {
        "word": word,
        "x": random.randint(8, 78),
        "y": -120 - (current_count * 110),
        "id": random.randint(100000, 999999)
    }

    st.session_state.falling_words.append(new_item)


def move_words_down(words, word_count, fall_step):
    new_words = []

    for item in st.session_state.falling_words:
        item["y"] += fall_step

        if item["y"] >= 500:
            st.session_state.lives -= 1
            st.session_state.message = f"😢 '{item['word']}'를 놓쳤어요!"
        else:
            new_words.append(item)

    st.session_state.falling_words = new_words

    while len(st.session_state.falling_words) < word_count:
        add_falling_word(words)

    st.session_state.step_count += 1


def reset_game():
    st.session_state.game_started = False
    st.session_state.falling_words = []
    st.session_state.score = 0
    st.session_state.lives = 5
    st.session_state.message = "게임을 다시 시작해 보세요!"
    st.session_state.used_words = []
    st.session_state.boom_word = ""
    st.session_state.last_recognized = ""
    st.session_state.audio_debug = ""
    st.session_state.step_count = 0

# =========================
# 사이드바
# =========================
st.sidebar.header("🎲 게임 설정")

category = st.sidebar.selectbox(
    "단어 세트 선택",
    list(word_sets.keys())
)

word_count = st.sidebar.slider(
    "화면에 나오는 단어 수",
    min_value=2,
    max_value=8,
    value=5,
    step=1
)

fall_step = st.sidebar.slider(
    "한 번에 내려오는 거리",
    min_value=20,
    max_value=90,
    value=45,
    step=5
)

target_score = st.sidebar.slider(
    "목표 점수",
    min_value=5,
    max_value=50,
    value=15,
    step=5
)

words = word_sets[category]

st.sidebar.markdown("---")
st.sidebar.write("📌 사용 방법")
st.sidebar.write("1. 게임 시작")
st.sidebar.write("2. 단어 진행 버튼을 누르면 차례대로 내려옴")
st.sidebar.write("3. 보이는 단어 중 하나 말하기")
st.sidebar.write("4. 인식되면 해당 단어가 터짐")
st.sidebar.write("5. 다시 단어 진행 버튼을 눌러 계속 진행")

# =========================
# 점수판
# =========================
col_score, col_life, col_target = st.columns(3)

with col_score:
    st.markdown(
        f"""
        <div class="score-card">
            ⭐ 점수<br>{st.session_state.score}
        </div>
        """,
        unsafe_allow_html=True
    )

with col_life:
    st.markdown(
        f"""
        <div class="score-card">
            ❤️ 기회<br>{st.session_state.lives}
        </div>
        """,
        unsafe_allow_html=True
    )

with col_target:
    st.markdown(
        f"""
        <div class="score-card">
            🎯 목표<br>{target_score}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("")

# =========================
# 버튼
# =========================
col_start, col_move, col_reset = st.columns(3)

with col_start:
    if st.button("▶️ 게임 시작", use_container_width=True):
        st.session_state.game_started = True
        st.session_state.score = 0
        st.session_state.lives = 5
        st.session_state.falling_words = []
        st.session_state.used_words = []
        st.session_state.boom_word = ""
        st.session_state.last_recognized = ""
        st.session_state.audio_debug = ""
        st.session_state.step_count = 0
        st.session_state.message = "단어가 차례대로 내려옵니다. 보이는 단어를 말해 보세요!"

        for _ in range(word_count):
            add_falling_word(words)

        # 시작하자마자 조금 보이도록 이동
        move_words_down(words, word_count, fall_step)

        st.rerun()

with col_move:
    if st.button("⬇️ 단어 진행", use_container_width=True):
        if st.session_state.game_started:
            move_words_down(words, word_count, fall_step)
            st.rerun()

with col_reset:
    if st.button("🔄 다시 시작", use_container_width=True):
        reset_game()
        st.rerun()

# =========================
# 게임 화면
# =========================
if st.session_state.game_started:

    if st.session_state.score >= target_score:
        st.balloons()
        st.success("🎉 목표 점수 달성! 훌륭합니다!")
        st.session_state.game_started = False

    elif st.session_state.lives <= 0:
        st.error("💥 Game Over! 다시 도전해 봅시다.")
        st.session_state.game_started = False

    else:
        while len(st.session_state.falling_words) < word_count:
            add_falling_word(words)

        # BOOM 효과
        if st.session_state.boom_word:
            st.markdown(
                f"""
                <div class="boom-box">
                    💥 BOOM! '{st.session_state.boom_word}' 터졌다!
                </div>
                """,
                unsafe_allow_html=True
            )
            st.session_state.boom_word = ""

        # 메시지
        st.markdown(
            f"""
            <div class="message-box">
                {st.session_state.message}
            </div>
            """,
            unsafe_allow_html=True
        )

        # 게임 박스
        words_html = ""

        for item in st.session_state.falling_words:
            words_html += f"""
            <div class="falling-word" style="left:{item['x']}%; top:{item['y']}px;">
                {item['word']}
            </div>
            """

        st.markdown(
            f"""
            <div class="game-box">
                {words_html}
            </div>
            """,
            unsafe_allow_html=True
        )

        # 마이크
        st.markdown("### 🎤 보이는 단어 중 하나를 말해 보세요")

        audio = mic_recorder(
            start_prompt="🎤 말하기 시작",
            stop_prompt="💥 말했어요! 터뜨리기",
            just_once=True,
            use_container_width=True,
            key="stable_mic"
        )

        if audio:
            audio_bytes = audio["bytes"]

            st.session_state.audio_debug = f"녹음 파일 크기: {len(audio_bytes)} bytes"

            recognized = recognize_speech(audio_bytes)
            st.session_state.last_recognized = recognized

            matched_word = None

            for item in st.session_state.falling_words:
                target_word = item["word"].lower()

                if recognized == target_word:
                    matched_word = item
                    break

                if target_word in recognized.split():
                    matched_word = item
                    break

            if matched_word:
                st.session_state.score += 1
                st.session_state.boom_word = matched_word["word"]
                st.session_state.message = f"✅ 성공! '{matched_word['word']}' 단어를 정확히 말했어요!"

                st.session_state.falling_words = [
                    item for item in st.session_state.falling_words
                    if item["id"] != matched_word["id"]
                ]

                add_falling_word(words)

                st.rerun()

            else:
                if recognized:
                    st.session_state.message = f"🤔 '{recognized}'라고 들렸어요. 화면에 있는 단어를 다시 말해 봅시다."
                else:
                    st.session_state.message = "🤔 인식하지 못했어요. 더 크게, 또박또박 말해 보세요."

                st.rerun()

        if st.session_state.last_recognized:
            st.info(f"🗣️ 마지막 인식: {st.session_state.last_recognized}")

        if st.session_state.audio_debug:
            st.caption(st.session_state.audio_debug)

else:
    st.markdown(
        """
        <div class="ready-box">
            <div class="ready-title">💥 Ready?</div>
            <p style="font-size:21px;">
                게임 시작 버튼을 누르면 단어들이 차례대로 위에서 아래로 내려옵니다.
            </p>
            <p style="font-size:19px;">
                학생은 보이는 단어 중 하나를 골라 크게 말합니다.
            </p>
            <p style="font-size:19px;">
                발음이 인식되면 그 단어가 <b>💥 BOOM!</b> 하고 터집니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📚 연습 단어 미리 보기")

    st.markdown(
        f"""
        <div class="word-preview">
            {", ".join(words)}
        </div>
        """,
        unsafe_allow_html=True
    )
