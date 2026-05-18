import streamlit as st
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(layout="wide")

st.markdown("#### Spring 2026")
st.caption("This page is continuously updated.")

IMAGE_URL = "https://raw.githubusercontent.com/Alexwcjung/Fun-English/main/a143182b-832c-4a27-87fb-74214eabb338.png?v=11"

st.image(
    IMAGE_URL,
    use_container_width=True
)

# =========================
# TTS 함수
# =========================
def make_audio(text, lang="en"):
    """
    영어 단어 또는 문장을 mp3 음성으로 변환합니다.
    """
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld="com")
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def play_audio(text, key=None):
    """
    Streamlit에서 음성을 재생합니다.
    """
    try:
        audio_bytes = make_audio(text)
        st.audio(audio_bytes, format="audio/mp3")
    except Exception:
        st.warning("음성을 만들 수 없습니다. 잠시 후 다시 시도해 주세요.")


# =========================
# 모르는 단어 저장 공간
# =========================
if "unknown_words" not in st.session_state:
    st.session_state.unknown_words = []

if "unknown_word_meanings" not in st.session_state:
    st.session_state.unknown_word_meanings = {}


def add_unknown_word(word, meaning):
    """
    모르는 단어를 저장합니다.
    """
    if word not in st.session_state.unknown_words:
        st.session_state.unknown_words.append(word)

    st.session_state.unknown_word_meanings[word] = meaning


def remove_unknown_word(word):
    """
    체크 해제한 단어를 목록에서 제거합니다.
    """
    if word in st.session_state.unknown_words:
        st.session_state.unknown_words.remove(word)

    if word in st.session_state.unknown_word_meanings:
        del st.session_state.unknown_word_meanings[word]


def toggle_unknown_word(word, meaning):
    """
    체크박스 상태에 따라 단어를 추가하거나 제거합니다.
    """
    if word in st.session_state.unknown_words:
        remove_unknown_word(word)
    else:
        add_unknown_word(word, meaning)


def show_word_card(word, meaning, example, key_prefix):
    """
    각 탭에서 단어 카드 출력
    - 단어
    - 뜻
    - 예문
    - 듣기
    - 모르는 단어 체크
    """
    checked = word in st.session_state.unknown_words

    st.markdown(
        f"""
        <div style="
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 18px 20px;
            margin-bottom: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        ">
            <div style="font-size: 28px; font-weight: 900; color: #111827;">
                {word}
            </div>
            <div style="font-size: 18px; color: #374151; margin-top: 6px;">
                뜻: <b>{meaning}</b>
            </div>
            <div style="font-size: 17px; color: #4b5563; margin-top: 6px;">
                예문: {example}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns([1, 1, 5])

    with c1:
        if st.button("🔊 듣기", key=f"{key_prefix}_listen_{word}"):
            play_audio(word, key=f"{key_prefix}_audio_{word}")

    with c2:
        st.checkbox(
            "모르는 단어",
            value=checked,
            key=f"{key_prefix}_check_{word}",
            on_change=toggle_unknown_word,
            args=(word, meaning)
        )

    st.divider()


# =========================
# 단어 데이터
# 필요한 단어는 여기에서 바꾸면 됩니다.
# =========================
school_words = [
    {
        "word": "student",
        "meaning": "학생",
        "example": "I am a student."
    },
    {
        "word": "teacher",
        "meaning": "선생님",
        "example": "She is my English teacher."
    },
    {
        "word": "classroom",
        "meaning": "교실",
        "example": "We study English in the classroom."
    },
    {
        "word": "homework",
        "meaning": "숙제",
        "example": "I do my homework after school."
    },
    {
        "word": "question",
        "meaning": "질문",
        "example": "I have a question."
    },
    {
        "word": "answer",
        "meaning": "대답, 정답",
        "example": "Please write the answer."
    },
    {
        "word": "practice",
        "meaning": "연습하다",
        "example": "I practice English every day."
    },
    {
        "word": "listen",
        "meaning": "듣다",
        "example": "Listen carefully."
    },
    {
        "word": "speak",
        "meaning": "말하다",
        "example": "I can speak English."
    },
    {
        "word": "read",
        "meaning": "읽다",
        "example": "I read a book."
    },
]

daily_words = [
    {
        "word": "hungry",
        "meaning": "배고픈",
        "example": "I am hungry."
    },
    {
        "word": "thirsty",
        "meaning": "목마른",
        "example": "I am thirsty."
    },
    {
        "word": "tired",
        "meaning": "피곤한",
        "example": "I am tired."
    },
    {
        "word": "happy",
        "meaning": "행복한",
        "example": "I am happy today."
    },
    {
        "word": "sad",
        "meaning": "슬픈",
        "example": "I feel sad."
    },
    {
        "word": "friend",
        "meaning": "친구",
        "example": "He is my friend."
    },
    {
        "word": "family",
        "meaning": "가족",
        "example": "I love my family."
    },
    {
        "word": "water",
        "meaning": "물",
        "example": "I need water."
    },
    {
        "word": "food",
        "meaning": "음식",
        "example": "I like Korean food."
    },
    {
        "word": "money",
        "meaning": "돈",
        "example": "I need some money."
    },
]

travel_words = [
    {
        "word": "station",
        "meaning": "역",
        "example": "Where is the station?"
    },
    {
        "word": "ticket",
        "meaning": "표",
        "example": "I need a ticket."
    },
    {
        "word": "bus",
        "meaning": "버스",
        "example": "I take a bus to school."
    },
    {
        "word": "train",
        "meaning": "기차",
        "example": "The train is fast."
    },
    {
        "word": "map",
        "meaning": "지도",
        "example": "Please show me the map."
    },
    {
        "word": "hotel",
        "meaning": "호텔",
        "example": "I stay at a hotel."
    },
    {
        "word": "airport",
        "meaning": "공항",
        "example": "I go to the airport."
    },
    {
        "word": "left",
        "meaning": "왼쪽",
        "example": "Turn left."
    },
    {
        "word": "right",
        "meaning": "오른쪽",
        "example": "Turn right."
    },
    {
        "word": "straight",
        "meaning": "똑바로",
        "example": "Go straight."
    },
]

survival_words = [
    {
        "word": "help",
        "meaning": "도움, 도와주다",
        "example": "Help me, please."
    },
    {
        "word": "sorry",
        "meaning": "미안한",
        "example": "I am sorry."
    },
    {
        "word": "please",
        "meaning": "제발, 부탁합니다",
        "example": "Please help me."
    },
    {
        "word": "thanks",
        "meaning": "고마워",
        "example": "Thanks a lot."
    },
    {
        "word": "bathroom",
        "meaning": "화장실",
        "example": "Where is the bathroom?"
    },
    {
        "word": "hospital",
        "meaning": "병원",
        "example": "I need a hospital."
    },
    {
        "word": "dangerous",
        "meaning": "위험한",
        "example": "This place is dangerous."
    },
    {
        "word": "safe",
        "meaning": "안전한",
        "example": "This place is safe."
    },
    {
        "word": "lost",
        "meaning": "길을 잃은",
        "example": "I am lost."
    },
    {
        "word": "problem",
        "meaning": "문제",
        "example": "I have a problem."
    },
]


# =========================
# 탭 구성
# =========================
tabs = st.tabs([
    "🏫 학교생활",
    "🌱 일상생활",
    "🧳 여행",
    "🛟 생존영어",
    "⭐ 모르는 단어 모음"
])


# =========================
# 1. 학교생활
# =========================
with tabs[0]:
    st.subheader("🏫 학교생활 단어")

    st.markdown(
        """
        학교에서 자주 쓰는 기본 단어입니다.  
        모르는 단어는 체크해 두면 마지막 탭에 자동으로 모입니다.
        """
    )

    for item in school_words:
        show_word_card(
            item["word"],
            item["meaning"],
            item["example"],
            "school"
        )


# =========================
# 2. 일상생활
# =========================
with tabs[1]:
    st.subheader("🌱 일상생활 단어")

    st.markdown(
        """
        일상생활에서 자주 쓰는 기본 단어입니다.  
        모르는 단어는 체크해 두면 마지막 탭에 자동으로 모입니다.
        """
    )

    for item in daily_words:
        show_word_card(
            item["word"],
            item["meaning"],
            item["example"],
            "daily"
        )


# =========================
# 3. 여행
# =========================
with tabs[2]:
    st.subheader("🧳 여행 단어")

    st.markdown(
        """
        이동, 길 찾기, 여행 상황에서 자주 쓰는 단어입니다.  
        모르는 단어는 체크해 두면 마지막 탭에 자동으로 모입니다.
        """
    )

    for item in travel_words:
        show_word_card(
            item["word"],
            item["meaning"],
            item["example"],
            "travel"
        )


# =========================
# 4. 생존영어
# =========================
with tabs[3]:
    st.subheader("🛟 생존영어 단어")

    st.markdown(
        """
        실제 상황에서 바로 쓸 수 있는 생존영어 단어입니다.  
        모르는 단어는 체크해 두면 마지막 탭에 자동으로 모입니다.
        """
    )

    for item in survival_words:
        show_word_card(
            item["word"],
            item["meaning"],
            item["example"],
            "survival"
        )


# =========================
# 5. 모르는 단어 모음
# =========================
with tabs[4]:
    st.subheader("⭐ 내가 체크한 모르는 단어")

    unknown_words = st.session_state.unknown_words
    unknown_meanings = st.session_state.unknown_word_meanings

    if not unknown_words:
        st.info("아직 체크한 단어가 없습니다. 각 탭에서 모르는 단어를 체크해 보세요.")
    else:
        st.success(f"총 {len(unknown_words)}개의 단어를 체크했습니다.")

        st.markdown("### 🎧 체크한 단어 전체 듣기")

        all_words_text = ". ".join(unknown_words)

        c1, c2 = st.columns([1, 5])

        with c1:
            if st.button("🔊 전체 듣기", key="listen_all_unknown_words"):
                play_audio(all_words_text, key="all_unknown_words_audio")

        with c2:
            st.markdown(
                """
                체크한 단어를 한 번에 들을 수 있습니다.  
                단어별 듣기는 아래 목록에서 할 수 있습니다.
                """
            )

        st.divider()

        st.markdown("### 📌 체크한 단어 목록")

        for i, word in enumerate(unknown_words, start=1):
            meaning = unknown_meanings.get(word, "")

            st.markdown(
                f"""
                <div style="
                    background: #f9fafb;
                    border: 1px solid #e5e7eb;
                    border-radius: 16px;
                    padding: 16px 18px;
                    margin-bottom: 10px;
                ">
                    <div style="font-size: 24px; font-weight: 900; color: #111827;">
                        {i}. {word}
                    </div>
                    <div style="font-size: 17px; color: #374151; margin-top: 4px;">
                        뜻: <b>{meaning}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            c1, c2 = st.columns([1, 1])

            with c1:
                if st.button("🔊 듣기", key=f"unknown_listen_{word}"):
                    play_audio(word, key=f"unknown_audio_{word}")

            with c2:
                if st.button("삭제", key=f"delete_unknown_{word}"):
                    remove_unknown_word(word)
                    st.rerun()

            st.divider()

        if st.button("🗑️ 체크한 단어 전체 삭제", key="clear_all_unknown_words"):
            st.session_state.unknown_words = []
            st.session_state.unknown_word_meanings = {}
            st.rerun()
