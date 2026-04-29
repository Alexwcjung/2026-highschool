import streamlit as st
import random
import time
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Falling Words Game",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Phonics Falling Words Game")
st.caption("떨어지는 단어를 보고 크게 말해 보세요. 발음이 인식되면 단어가 사라집니다!")

# =========================
# CSS 디자인
# =========================
st.markdown(
    """
    <style>
    .game-box {
        height: 520px;
        border-radius: 24px;
        background: linear-gradient(180deg, #e0f2fe 0%, #fef9c3 100%);
        border: 3px solid #bae6fd;
        position: relative;
        overflow: hidden;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        margin-bottom: 20px;
    }

    .falling-word {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        background: white;
        color: #111827;
        font-size: 48px;
        font-weight: 900;
        padding: 18px 34px;
        border-radius: 26px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.18);
        border: 3px solid #fb923c;
    }

    .score-card {
        background: linear-gradient(135deg, #fff7ed, #fef3c7);
        border-radius: 20px;
        padding: 18px;
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        border: 2px solid #fed7aa;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    .word-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 12px;
        border: 2px solid #dbeafe;
        box-shadow: 0 3px 8px rgba(0,0,0,0.07);
    }

    .big-word {
        font-size: 52px;
        font-weight: 900;
        text-align: center;
        color: #1f2937;
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
        "sit", "pig", "hot", "cup", "bus"
    ],
    "긴 모음": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope"
    ],
    "Blends": [
        "black", "brown", "clock", "crab", "drum",
        "flag", "frog", "green", "spoon", "star"
    ],
    "Digraphs": [
        "chair", "ship", "three", "this", "phone",
        "whale", "duck", "shop", "cheese", "photo"
    ],
    "Vowel Teams": [
        "rain", "day", "see", "eat", "boat",
        "snow", "cow", "house", "coin", "boy"
    ],
    "R-Controlled": [
        "car", "star", "her", "bird", "girl",
        "corn", "fork", "turn", "burn", "teacher"
    ],
    "Silent e": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope"
    ],
}

# =========================
# 세션 상태 초기화
# =========================
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "current_word" not in st.session_state:
    st.session_state.current_word = None

if "word_y" not in st.session_state:
    st.session_state.word_y = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "lives" not in st.session_state:
    st.session_state.lives = 3

if "recognized_text" not in st.session_state:
    st.session_state.recognized_text = ""

if "message" not in st.session_state:
    st.session_state.message = "게임을 시작해 보세요!"

if "used_words" not in st.session_state:
    st.session_state.used_words = []

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
# 단어 선택 함수
# =========================
def choose_new_word(words):
    remaining = [w for w in words if w not in st.session_state.used_words]

    if len(remaining) == 0:
        st.session_state.used_words = []
        remaining = words[:]

    new_word = random.choice(remaining)
    st.session_state.current_word = new_word
    st.session_state.used_words.append(new_word)
    st.session_state.word_y = 0


# =========================
# 사이드바 설정
# =========================
st.sidebar.header("🎲 게임 설정")

category = st.sidebar.selectbox(
    "단어 세트 선택",
    list(word_sets.keys())
)

speed = st.sidebar.slider(
    "단어 내려오는 속도",
    min_value=20,
    max_value=80,
    value=35,
    step=5
)

target_score = st.sidebar.slider(
    "목표 점수",
    min_value=5,
    max_value=30,
    value=10,
    step=5
)

words = word_sets[category]

st.sidebar.markdown("---")
st.sidebar.write("📌 사용 방법")
st.sidebar.write("1. 게임 시작")
st.sidebar.write("2. 내려오는 단어 읽기")
st.sidebar.write("3. 마이크 버튼 누르고 말하기")
st.sidebar.write("4. 인식되면 단어 제거")

# =========================
# 상단 점수판
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
# 게임 버튼
# =========================
col_start, col_next, col_reset = st.columns(3)

with col_start:
    if st.button("▶️ 게임 시작", use_container_width=True):
        st.session_state.game_started = True
        st.session_state.score = 0
        st.session_state.lives = 3
        st.session_state.used_words = []
        st.session_state.recognized_text = ""
        st.session_state.message = "단어를 보고 크게 말해 보세요!"
        choose_new_word(words)
        st.rerun()

with col_next:
    if st.button("⏭️ 다음 단어", use_container_width=True):
        if st.session_state.game_started:
            choose_new_word(words)
            st.session_state.message = "새 단어가 내려옵니다!"
            st.rerun()

with col_reset:
    if st.button("🔄 다시 시작", use_container_width=True):
        st.session_state.game_started = False
        st.session_state.current_word = None
        st.session_state.word_y = 0
        st.session_state.score = 0
        st.session_state.lives = 3
        st.session_state.used_words = []
        st.session_state.recognized_text = ""
        st.session_state.message = "게임을 다시 시작해 보세요!"
        st.rerun()

# =========================
# 게임 진행
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
        if st.session_state.current_word is None:
            choose_new_word(words)

        current_word = st.session_state.current_word

        # 단어 위치 증가
        st.session_state.word_y += speed

        # 단어가 바닥에 닿으면 기회 차감
        if st.session_state.word_y >= 430:
            st.session_state.lives -= 1
            st.session_state.message = f"😢 {current_word}를 놓쳤어요!"
            choose_new_word(words)
            st.rerun()

        # 게임 화면
        st.markdown(
            f"""
            <div class="game-box">
                <div class="falling-word" style="top:{st.session_state.word_y}px;">
                    {current_word}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(st.session_state.message)

        # 마이크 입력
        st.markdown("### 🎤 단어를 말해 보세요")

        audio = mic_recorder(
            start_prompt="🎙️ 녹음 시작",
            stop_prompt="⏹️ 녹음 끝",
            just_once=True,
            use_container_width=True,
            key=f"mic_{current_word}_{st.session_state.score}_{st.session_state.lives}"
        )

        if audio:
            audio_bytes = audio["bytes"]
            recognized = recognize_speech(audio_bytes)
            st.session_state.recognized_text = recognized

            st.write(f"🗣️ 인식된 말: **{recognized if recognized else '인식 실패'}**")

            # 인식된 문장 안에 현재 단어가 들어가도 정답 처리
            if current_word.lower() in recognized.split() or recognized == current_word.lower():
                st.session_state.score += 1
                st.session_state.message = f"✅ 성공! {current_word} 단어가 사라졌습니다!"
                choose_new_word(words)
                st.rerun()
            else:
                st.session_state.message = f"🤔 다시 한 번 말해 봅시다. 목표 단어는 {current_word}입니다."
                st.rerun()

        # 자동으로 조금씩 내려오게 하기
        time.sleep(0.4)
        st.rerun()

else:
    st.markdown(
        """
        <div class="word-card">
            <div class="big-word">🎮 Ready?</div>
            <p style="text-align:center; font-size:20px;">
                게임 시작 버튼을 누르면 단어가 위에서 아래로 내려옵니다.
            </p>
            <p style="text-align:center; font-size:18px;">
                학생은 단어를 보고 직접 말합니다. 발음이 인식되면 단어가 사라집니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📚 연습 단어 미리 보기")
    st.write(", ".join(words))
