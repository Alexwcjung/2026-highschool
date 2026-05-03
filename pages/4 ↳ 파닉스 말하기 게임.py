import streamlit as st
from gtts import gTTS
import io
import random
import time

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Mole Game",
    page_icon="🔨",
    layout="wide"
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

# =========================
# CSS 디자인
# =========================
st.markdown(
    """
    <style>
    .main {
        background-color: #fffdfb;
    }

    .hero-box {
        background: linear-gradient(135deg, #fff1f2 0%, #eef2ff 50%, #ecfeff 100%);
        border-radius: 30px;
        padding: 30px;
        margin-bottom: 24px;
        text-align: center;
        border: 1px solid #fbcfe8;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 900;
        color: #334155;
        margin-bottom: 8px;
    }

    .hero-sub {
        font-size: 17px;
        color: #64748b;
        line-height: 1.7;
    }

    .guide-box {
        background: linear-gradient(135deg, #fff7ed 0%, #fffbeb 100%);
        border-radius: 22px;
        padding: 20px 24px;
        margin-bottom: 22px;
        border: 1px solid #fed7aa;
        box-shadow: 0 6px 16px rgba(0,0,0,0.05);
    }

    .guide-title {
        font-size: 22px;
        font-weight: 900;
        color: #c2410c;
        margin-bottom: 8px;
    }

    .guide-text {
        font-size: 16px;
        color: #7c2d12;
        line-height: 1.8;
    }

    .score-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-radius: 20px;
        padding: 18px;
        text-align: center;
        border: 1px solid #bbf7d0;
        font-size: 22px;
        font-weight: 900;
        color: #166534;
        margin-bottom: 20px;
    }

    .target-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-radius: 24px;
        padding: 22px;
        border: 1px solid #bfdbfe;
        text-align: center;
        margin-bottom: 20px;
    }

    .target-title {
        font-size: 20px;
        font-weight: 900;
        color: #1d4ed8;
        margin-bottom: 8px;
    }

    .target-word {
        font-size: 34px;
        font-weight: 900;
        color: #111827;
    }

    .mole-card {
        background: linear-gradient(135deg, #ffffff 0%, #fef3c7 100%);
        border-radius: 26px;
        padding: 22px 10px;
        text-align: center;
        border: 2px solid #fde68a;
        box-shadow: 0 6px 16px rgba(0,0,0,0.07);
        margin-bottom: 14px;
        min-height: 150px;
    }

    .mole-emoji {
        font-size: 48px;
        margin-bottom: 6px;
    }

    .mole-word {
        font-size: 28px;
        font-weight: 900;
        color: #3f3f46;
        margin-bottom: 6px;
    }

    .hole-card {
        background: linear-gradient(135deg, #e5e7eb 0%, #f3f4f6 100%);
        border-radius: 26px;
        padding: 22px 10px;
        text-align: center;
        border: 2px dashed #d1d5db;
        margin-bottom: 14px;
        min-height: 150px;
    }

    .hole-emoji {
        font-size: 48px;
        opacity: 0.45;
        margin-bottom: 6px;
    }

    .hole-text {
        font-size: 22px;
        font-weight: 800;
        color: #9ca3af;
    }

    .result-correct {
        background: #dcfce7;
        color: #166534;
        border-radius: 18px;
        padding: 16px;
        font-size: 22px;
        font-weight: 900;
        text-align: center;
        margin: 18px 0;
    }

    .result-wrong {
        background: #fee2e2;
        color: #991b1b;
        border-radius: 18px;
        padding: 16px;
        font-size: 22px;
        font-weight: 900;
        text-align: center;
        margin: 18px 0;
    }

    .stButton > button {
        width: 100%;
        border-radius: 999px;
        font-weight: 900;
        font-size: 17px;
        padding: 0.55rem 1rem;
        border: 1px solid #d1d5db;
    }

    .stButton > button:hover {
        border-color: #f97316;
        color: #f97316;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 문제 데이터
# =========================
PHONICS_SETS = {
    "짧은 모음 Short Vowels": [
        {"word": "cat", "sound": "cat", "hint": "short a"},
        {"word": "bed", "sound": "bed", "hint": "short e"},
        {"word": "sit", "sound": "sit", "hint": "short i"},
        {"word": "hot", "sound": "hot", "hint": "short o"},
        {"word": "cup", "sound": "cup", "hint": "short u"},
        {"word": "map", "sound": "map", "hint": "short a"},
        {"word": "pen", "sound": "pen", "hint": "short e"},
        {"word": "pig", "sound": "pig", "hint": "short i"},
        {"word": "dog", "sound": "dog", "hint": "short o"},
        {"word": "sun", "sound": "sun", "hint": "short u"},
    ],
    "긴 모음 Long Vowels": [
        {"word": "cake", "sound": "cake", "hint": "long a"},
        {"word": "tree", "sound": "tree", "hint": "long e"},
        {"word": "bike", "sound": "bike", "hint": "long i"},
        {"word": "home", "sound": "home", "hint": "long o"},
        {"word": "cube", "sound": "cube", "hint": "long u"},
        {"word": "rain", "sound": "rain", "hint": "long a"},
        {"word": "see", "sound": "see", "hint": "long e"},
        {"word": "kite", "sound": "kite", "hint": "long i"},
        {"word": "boat", "sound": "boat", "hint": "long o"},
        {"word": "music", "sound": "music", "hint": "long u"},
    ],
    "자음 이어 읽기 Blends": [
        {"word": "black", "sound": "black", "hint": "bl"},
        {"word": "brown", "sound": "brown", "hint": "br"},
        {"word": "clock", "sound": "clock", "hint": "cl"},
        {"word": "frog", "sound": "frog", "hint": "fr"},
        {"word": "green", "sound": "green", "hint": "gr"},
        {"word": "plane", "sound": "plane", "hint": "pl"},
        {"word": "snake", "sound": "snake", "hint": "sn"},
        {"word": "spoon", "sound": "spoon", "hint": "sp"},
        {"word": "star", "sound": "star", "hint": "st"},
        {"word": "tree", "sound": "tree", "hint": "tr"},
    ],
    "두 글자 한 소리 Digraphs": [
        {"word": "chair", "sound": "chair", "hint": "ch"},
        {"word": "ship", "sound": "ship", "hint": "sh"},
        {"word": "three", "sound": "three", "hint": "th"},
        {"word": "this", "sound": "this", "hint": "th"},
        {"word": "phone", "sound": "phone", "hint": "ph"},
        {"word": "duck", "sound": "duck", "hint": "ck"},
        {"word": "whale", "sound": "whale", "hint": "wh"},
    ],
    "자음 예외": [
        {"word": "city", "sound": "city", "hint": "soft c"},
        {"word": "cent", "sound": "cent", "hint": "soft c"},
        {"word": "cycle", "sound": "cycle", "hint": "soft c"},
        {"word": "gem", "sound": "gem", "hint": "soft g"},
        {"word": "giant", "sound": "giant", "hint": "soft g"},
        {"word": "gym", "sound": "gym", "hint": "soft g"},
        {"word": "knee", "sound": "knee", "hint": "silent k"},
        {"word": "write", "sound": "write", "hint": "silent w"},
        {"word": "lamb", "sound": "lamb", "hint": "silent b"},
        {"word": "exam", "sound": "exam", "hint": "x as gz"},
    ],
}

# =========================
# 세션 상태 초기화
# =========================
if "score" not in st.session_state:
    st.session_state.score = 0

if "round" not in st.session_state:
    st.session_state.round = 1

if "target" not in st.session_state:
    st.session_state.target = None

if "choices" not in st.session_state:
    st.session_state.choices = []

if "result" not in st.session_state:
    st.session_state.result = ""

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "selected_set" not in st.session_state:
    st.session_state.selected_set = "짧은 모음 Short Vowels"


# =========================
# 게임 함수
# =========================
def make_new_round(word_list):
    target = random.choice(word_list)

    wrong_choices = [item for item in word_list if item["word"] != target["word"]]
    distractors = random.sample(wrong_choices, min(5, len(wrong_choices)))

    choices = distractors + [target]
    random.shuffle(choices)

    st.session_state.target = target
    st.session_state.choices = choices
    st.session_state.result = ""
    st.session_state.game_started = True


def reset_game():
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.target = None
    st.session_state.choices = []
    st.session_state.result = ""
    st.session_state.game_started = False


def choose_answer(choice):
    target = st.session_state.target

    if choice["word"] == target["word"]:
        st.session_state.score += 1
        st.session_state.result = "correct"
    else:
        st.session_state.result = "wrong"

    st.session_state.round += 1


# =========================
# 상단 화면
# =========================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🔨🐹 파닉스 두더지 잡기 게임</div>
        <div class="hero-sub">
            소리를 듣고 맞는 단어 두더지를 빠르게 잡아 보세요!<br>
            짧은 모음, 긴 모음, 자음 이어 읽기, 두 글자 한 소리, 자음 예외를 연습할 수 있습니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="guide-box">
        <div class="guide-title">🎯 게임 방법</div>
        <div class="guide-text">
            1. 연습할 파닉스 영역을 고릅니다.<br>
            2. <b>새 문제 시작</b>을 누릅니다.<br>
            3. 소리를 듣고, 같은 단어가 적힌 두더지를 클릭합니다.<br>
            4. 맞으면 점수가 올라갑니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 설정 영역
# =========================
col_a, col_b, col_c = st.columns([2, 1, 1])

with col_a:
    selected_set = st.selectbox(
        "연습할 파닉스 영역을 선택하세요",
        list(PHONICS_SETS.keys()),
        index=list(PHONICS_SETS.keys()).index(st.session_state.selected_set)
    )

    if selected_set != st.session_state.selected_set:
        st.session_state.selected_set = selected_set
        reset_game()

with col_b:
    if st.button("🚀 새 문제 시작"):
        make_new_round(PHONICS_SETS[st.session_state.selected_set])

with col_c:
    if st.button("🔄 점수 초기화"):
        reset_game()

# =========================
# 점수판
# =========================
st.markdown(
    f"""
    <div class="score-box">
        🏆 점수: {st.session_state.score}점 &nbsp;&nbsp; | &nbsp;&nbsp; 🎲 현재 라운드: {st.session_state.round}
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 문제 영역
# =========================
if not st.session_state.game_started:
    st.info("먼저 🚀 새 문제 시작 버튼을 눌러 주세요.")
else:
    target = st.session_state.target

    st.markdown(
        f"""
        <div class="target-box">
            <div class="target-title">🔊 아래 소리를 듣고 맞는 두더지를 잡으세요!</div>
            <div class="target-word">힌트: {target['hint']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    audio_bytes = make_tts_audio(target["sound"])
    st.audio(audio_bytes, format="audio/mp3")

    if st.session_state.result == "correct":
        st.markdown(
            """
            <div class="result-correct">
                🎉 정답입니다! 잘했어요!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()

        if st.button("➡️ 다음 문제"):
            make_new_round(PHONICS_SETS[st.session_state.selected_set])
            st.rerun()

    elif st.session_state.result == "wrong":
        st.markdown(
            f"""
            <div class="result-wrong">
                😭 아쉬워요! 정답은 {target['word']} 입니다.
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("➡️ 다음 문제"):
            make_new_round(PHONICS_SETS[st.session_state.selected_set])
            st.rerun()

    else:
        st.markdown("### 🕳️ 두더지를 잡아 보세요!")

        choices = st.session_state.choices

        # 6칸 두더지 판
        while len(choices) < 6:
            choices.append({"word": "", "sound": "", "hint": ""})

        row1 = st.columns(3)
        row2 = st.columns(3)
        grid_cols = row1 + row2

        for idx, col in enumerate(grid_cols):
            choice = choices[idx]

            with col:
                if choice["word"]:
                    st.markdown(
                        f"""
                        <div class="mole-card">
                            <div class="mole-emoji">🐹</div>
                            <div class="mole-word">{choice['word']}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"🔨 {choice['word']} 잡기",
                        key=f"mole_{idx}_{choice['word']}_{st.session_state.round}"
                    ):
                        choose_answer(choice)
                        st.rerun()

                else:
                    st.markdown(
                        """
                        <div class="hole-card">
                            <div class="hole-emoji">🕳️</div>
                            <div class="hole-text">빈 구멍</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

# =========================
# 수업 활용 팁
# =========================
st.markdown("---")
st.markdown("### 💡 수업 활용 팁")

st.markdown(
    """
- 처음에는 선생님이 소리를 같이 들려주고 학생들이 손으로 단어를 가리키게 해도 좋습니다.
- 익숙해지면 학생이 직접 나와서 두더지를 잡게 하면 활동성이 생깁니다.
- `자음 예외` 세트는 기본 파닉스를 한 뒤 복습용으로 사용하면 좋습니다.
- 단어를 더 넣고 싶으면 코드 위쪽 `PHONICS_SETS` 안에 단어를 추가하면 됩니다.
"""
)
