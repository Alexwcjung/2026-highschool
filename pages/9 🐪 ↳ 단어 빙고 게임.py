import streamlit as st
import random
import io
import re
import time
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Speaking Word Pop Game",
    page_icon="💥",
    layout="centered"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #fff7ed 0%, #fdf2f8 45%, #eff6ff 100%);
    }

    .title-box {
        background: linear-gradient(135deg, #fb7185, #a78bfa, #38bdf8);
        color: white;
        border-radius: 28px;
        padding: 24px 22px;
        text-align: center;
        box-shadow: 0 10px 24px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }

    .title-main {
        font-size: 30px;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .title-sub {
        font-size: 16px;
        font-weight: 700;
        opacity: 0.95;
    }

    .word-card {
        background: white;
        border-radius: 32px;
        padding: 42px 20px;
        text-align: center;
        box-shadow: 0 12px 28px rgba(0,0,0,0.12);
        border: 4px solid #fbcfe8;
        margin: 18px 0;
    }

    .word-label {
        font-size: 17px;
        font-weight: 800;
        color: #64748b;
        margin-bottom: 12px;
    }

    .target-word {
        font-size: 58px;
        font-weight: 1000;
        color: #be185d;
        letter-spacing: 1px;
    }

    .pop-word {
        background: linear-gradient(135deg, #fef3c7, #fecaca, #ddd6fe);
        border-radius: 32px;
        padding: 42px 20px;
        text-align: center;
        box-shadow: 0 12px 28px rgba(0,0,0,0.12);
        border: 4px solid #fb7185;
        margin: 18px 0;
        animation: pop 0.7s ease-in-out;
    }

    .pop-text {
        font-size: 54px;
        font-weight: 1000;
        color: #dc2626;
    }

    @keyframes pop {
        0% { transform: scale(0.7); opacity: 0.4; }
        45% { transform: scale(1.18); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }

    .score-box {
        background: white;
        border-radius: 22px;
        padding: 16px 10px;
        text-align: center;
        box-shadow: 0 5px 14px rgba(0,0,0,0.08);
        border: 2px solid #e0e7ff;
        font-size: 18px;
        font-weight: 900;
        color: #1e293b;
    }

    .message-good {
        background: #dcfce7;
        color: #14532d;
        border-radius: 20px;
        padding: 16px;
        font-size: 18px;
        font-weight: 900;
        text-align: center;
        margin: 16px 0;
        border: 2px solid #86efac;
    }

    .message-bad {
        background: #fff7ed;
        color: #9a3412;
        border-radius: 20px;
        padding: 16px;
        font-size: 18px;
        font-weight: 900;
        text-align: center;
        margin: 16px 0;
        border: 2px solid #fdba74;
    }

    .recognized-box {
        background: #f8fafc;
        border-radius: 18px;
        padding: 14px;
        font-size: 16px;
        font-weight: 800;
        text-align: center;
        color: #334155;
        border: 1px solid #cbd5e1;
        margin-top: 12px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        font-size: 17px;
        min-height: 48px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 제목
# =========================
st.markdown(
    """
    <div class="title-box">
        <div class="title-main">💥 Speaking Word Pop</div>
        <div class="title-sub">폰으로 단어를 하나씩 말하면 단어가 펑! 터집니다</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 단어 데이터
# =========================
word_groups = {
    "🌱 기초 동작": [
        "go", "come", "walk", "run", "sit", "stand", "stop", "start",
        "open", "close", "make", "do", "have", "get", "take", "give",
        "put", "bring", "use", "find", "help", "try", "need", "want",
        "like", "read", "write", "speak", "listen", "eat"
    ],
    "🍎 음식": [
        "food", "rice", "bread", "water", "milk", "juice", "coffee", "tea",
        "apple", "banana", "egg", "meat", "fish", "chicken", "fruit",
        "breakfast", "lunch", "dinner", "snack", "cake"
    ],
    "🐶 동물": [
        "dog", "cat", "bird", "fish", "horse", "cow", "pig", "sheep",
        "goat", "chicken", "duck", "rabbit", "monkey", "lion", "tiger",
        "bear", "fox", "deer", "whale", "shark"
    ],
    "💖 감정": [
        "happy", "sad", "angry", "tired", "hungry", "thirsty",
        "excited", "bored", "afraid", "worried", "proud", "kind",
        "nice", "brave", "shy", "smart", "strong", "busy", "ready", "sorry"
    ],
    "🏫 학교": [
        "school", "class", "teacher", "student", "book", "notebook",
        "paper", "pen", "pencil", "desk", "chair", "board", "word",
        "sentence", "English", "Korean", "homework", "test", "quiz", "score"
    ]
}

# =========================
# 함수
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


def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text


def is_correct(spoken_text, target_word):
    spoken_text = normalize_text(spoken_text)
    target_word = normalize_text(target_word)

    if not spoken_text:
        return False

    spoken_words = spoken_text.split()

    if spoken_text == target_word:
        return True

    if target_word in spoken_words:
        return True

    return False


def init_game(group_name, word_count):
    key = f"word_pop_{group_name}_{word_count}"

    if f"{key}_words" not in st.session_state:
        words = word_groups[group_name].copy()
        random.shuffle(words)

        st.session_state[f"{key}_words"] = words[:word_count]
        st.session_state[f"{key}_index"] = 0
        st.session_state[f"{key}_score"] = 0
        st.session_state[f"{key}_wrong"] = 0
        st.session_state[f"{key}_started"] = False
        st.session_state[f"{key}_recognized"] = ""
        st.session_state[f"{key}_message"] = "시작 버튼을 누르고 단어를 크게 말해 보세요!"
        st.session_state[f"{key}_pop"] = False

    return key


def reset_game(key):
    delete_keys = [k for k in st.session_state.keys() if k.startswith(key)]
    for k in delete_keys:
        del st.session_state[k]


# =========================
# 게임 설정
# =========================
group_name = st.selectbox(
    "연습할 단어 묶음 선택",
    list(word_groups.keys())
)

word_count = st.radio(
    "연습할 단어 수",
    [5, 10, 15, 20],
    index=1,
    horizontal=True
)

key = init_game(group_name, word_count)

words = st.session_state[f"{key}_words"]
index = st.session_state[f"{key}_index"]
score = st.session_state[f"{key}_score"]
wrong = st.session_state[f"{key}_wrong"]
started = st.session_state[f"{key}_started"]
recognized = st.session_state[f"{key}_recognized"]
message = st.session_state[f"{key}_message"]
pop = st.session_state[f"{key}_pop"]

# =========================
# 점수판
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="score-box">
            ⭐ 성공<br>{score}
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="score-box">
            🔥 진행<br>{index}/{len(words)}
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="score-box">
            💪 다시 도전<br>{wrong}
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 시작 / 초기화 버튼
# =========================
col_start, col_reset = st.columns(2)

with col_start:
    if st.button("▶️ 게임 시작", use_container_width=True):
        st.session_state[f"{key}_started"] = True
        st.session_state[f"{key}_message"] = "아래 단어를 보고 폰으로 크게 말하세요!"
        st.rerun()

with col_reset:
    if st.button("🔄 새 단어로 다시 시작", use_container_width=True):
        reset_game(key)
        st.rerun()

# =========================
# 게임 종료
# =========================
if index >= len(words):
    st.balloons()
    st.success(f"🎉 완료! 총 {len(words)}개 중 {score}개 성공했습니다!")

    if st.button("처음부터 다시 하기", use_container_width=True):
        reset_game(key)
        st.rerun()

    st.stop()

# =========================
# 현재 단어
# =========================
target_word = words[index]

if pop:
    st.markdown(
        f"""
        <div class="pop-word">
            <div class="pop-text">💥 {target_word} 💥</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.7)

    st.session_state[f"{key}_index"] += 1
    st.session_state[f"{key}_pop"] = False
    st.rerun()

else:
    st.markdown(
        f"""
        <div class="word-card">
            <div class="word-label">이 단어를 말하세요</div>
            <div class="target-word">{target_word}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 메시지
# =========================
if "정답" in message or "성공" in message:
    st.markdown(
        f"""
        <div class="message-good">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )
elif "다시" in message or "인식 실패" in message:
    st.markdown(
        f"""
        <div class="message-bad">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info(message)

# =========================
# 음성 인식
# =========================
st.markdown("### 🎤 발음하기")

if not started:
    st.write("먼저 게임 시작 버튼을 눌러 주세요.")
else:
    audio = mic_recorder(
        start_prompt="🎙️ 말하기 시작",
        stop_prompt="⏹️ 말하기 끝",
        just_once=True,
        use_container_width=True,
        key=f"{key}_mic_{index}_{score}_{wrong}"
    )

    if audio:
        audio_bytes = audio["bytes"]
        spoken_text = recognize_speech(audio_bytes)

        st.session_state[f"{key}_recognized"] = spoken_text

        if is_correct(spoken_text, target_word):
            st.session_state[f"{key}_score"] += 1
            st.session_state[f"{key}_message"] = f"✅ 정답! {target_word} 성공!"
            st.session_state[f"{key}_pop"] = True
            st.rerun()
        else:
            st.session_state[f"{key}_wrong"] += 1

            if spoken_text:
                st.session_state[f"{key}_message"] = f"🤔 인식된 말: {spoken_text} / 다시 말해 보세요!"
            else:
                st.session_state[f"{key}_message"] = "🎤 인식 실패! 조금 더 크게 또박또박 말해 보세요!"

            st.rerun()

# =========================
# 최근 인식 결과
# =========================
if recognized:
    st.markdown(
        f"""
        <div class="recognized-box">
            🗣️ 최근 인식된 말: {recognized}
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 안내
# =========================
with st.expander("📱 폰에서 사용할 때 주의할 점"):
    st.write("""
    1. Streamlit 앱 주소를 폰으로 접속합니다.
    2. 마이크 권한을 허용해야 합니다.
    3. 단어 하나를 말한 뒤, 말하기 끝 버튼을 누릅니다.
    4. 발음이 인식되면 단어가 펑 터지고 다음 단어로 넘어갑니다.
    """)
