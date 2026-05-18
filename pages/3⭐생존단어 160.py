import streamlit as st
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Survival English 160",
    page_icon="🛟",
    layout="wide"
)

st.markdown("#### Spring 2026")
st.caption("This page is continuously updated.")

IMAGE_URL = "https://raw.githubusercontent.com/Alexwcjung/Fun-English/main/a143182b-832c-4a27-87fb-74214eabb338.png?v=11"

st.image(
    IMAGE_URL,
    use_container_width=True
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 900;
        color: #111827;
        margin-top: 8px;
        margin-bottom: 4px;
    }

    .sub-title {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 20px;
    }

    .word-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 16px 18px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }

    .word-text {
        font-size: 28px;
        font-weight: 900;
        color: #111827;
    }

    .meaning-text {
        font-size: 18px;
        color: #374151;
        margin-top: 4px;
    }

    .example-text {
        font-size: 16px;
        color: #4b5563;
        margin-top: 5px;
    }

    .section-box {
        background: linear-gradient(135deg, #ecfeff 0%, #fef3c7 50%, #fce7f3 100%);
        border-radius: 20px;
        padding: 18px 22px;
        margin-bottom: 18px;
        border: 1px solid #e5e7eb;
    }

    .small-guide {
        font-size: 16px;
        color: #4b5563;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS 함수
# =========================
@st.cache_data(show_spinner=False)
def make_audio(text):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang="en", tld="com")
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def play_audio(text):
    try:
        audio_bytes = make_audio(text)
        st.audio(audio_bytes, format="audio/mp3")
    except Exception:
        st.warning("음성을 만들 수 없습니다. 잠시 후 다시 시도해 주세요.")


# =========================
# Session State
# =========================
if "unknown_words" not in st.session_state:
    st.session_state.unknown_words = []

if "unknown_word_info" not in st.session_state:
    st.session_state.unknown_word_info = {}


def add_unknown(word, meaning, example, category):
    if word not in st.session_state.unknown_words:
        st.session_state.unknown_words.append(word)

    st.session_state.unknown_word_info[word] = {
        "meaning": meaning,
        "example": example,
        "category": category
    }


def remove_unknown(word):
    if word in st.session_state.unknown_words:
        st.session_state.unknown_words.remove(word)

    if word in st.session_state.unknown_word_info:
        del st.session_state.unknown_word_info[word]


def toggle_unknown(word, meaning, example, category):
    if word in st.session_state.unknown_words:
        remove_unknown(word)
    else:
        add_unknown(word, meaning, example, category)


def show_word_card(item, key_prefix):
    word = item["word"]
    meaning = item["meaning"]
    example = item["example"]
    category = item["category"]

    checked = word in st.session_state.unknown_words

    st.markdown(
        f"""
        <div class="word-card">
            <div class="word-text">{word}</div>
            <div class="meaning-text">뜻: <b>{meaning}</b></div>
            <div class="example-text">예문: {example}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns([1, 1.3, 5])

    with c1:
        if st.button("🔊 듣기", key=f"{key_prefix}_listen_{word}"):
            play_audio(word)

    with c2:
        st.checkbox(
            "모르는 단어",
            value=checked,
            key=f"{key_prefix}_check_{word}",
            on_change=toggle_unknown,
            args=(word, meaning, example, category)
        )

    st.divider()


# =========================
# 생존단어 160
# =========================
WORDS = [
    # 1. 나와 사람
    {"category": "🧍 나와 사람", "word": "I", "meaning": "나", "example": "I am a student."},
    {"category": "🧍 나와 사람", "word": "you", "meaning": "너, 당신", "example": "You are my friend."},
    {"category": "🧍 나와 사람", "word": "he", "meaning": "그", "example": "He is kind."},
    {"category": "🧍 나와 사람", "word": "she", "meaning": "그녀", "example": "She is my teacher."},
    {"category": "🧍 나와 사람", "word": "we", "meaning": "우리", "example": "We are classmates."},
    {"category": "🧍 나와 사람", "word": "they", "meaning": "그들", "example": "They are students."},
    {"category": "🧍 나와 사람", "word": "me", "meaning": "나를, 나에게", "example": "Please help me."},
    {"category": "🧍 나와 사람", "word": "my", "meaning": "나의", "example": "This is my bag."},
    {"category": "🧍 나와 사람", "word": "your", "meaning": "너의", "example": "What is your name?"},
    {"category": "🧍 나와 사람", "word": "friend", "meaning": "친구", "example": "He is my friend."},
    {"category": "🧍 나와 사람", "word": "teacher", "meaning": "선생님", "example": "She is my teacher."},
    {"category": "🧍 나와 사람", "word": "student", "meaning": "학생", "example": "I am a student."},
    {"category": "🧍 나와 사람", "word": "classmate", "meaning": "반 친구", "example": "He is my classmate."},
    {"category": "🧍 나와 사람", "word": "family", "meaning": "가족", "example": "I love my family."},
    {"category": "🧍 나와 사람", "word": "father", "meaning": "아버지", "example": "My father is tall."},
    {"category": "🧍 나와 사람", "word": "mother", "meaning": "어머니", "example": "My mother is kind."},
    {"category": "🧍 나와 사람", "word": "brother", "meaning": "형, 오빠, 남동생", "example": "I have a brother."},
    {"category": "🧍 나와 사람", "word": "sister", "meaning": "누나, 언니, 여동생", "example": "I have a sister."},
    {"category": "🧍 나와 사람", "word": "man", "meaning": "남자", "example": "The man is tall."},
    {"category": "🧍 나와 사람", "word": "woman", "meaning": "여자", "example": "The woman is kind."},

    # 2. 기본 동작
    {"category": "🏃 기본 동작", "word": "go", "meaning": "가다", "example": "I go to school."},
    {"category": "🏃 기본 동작", "word": "come", "meaning": "오다", "example": "Come here, please."},
    {"category": "🏃 기본 동작", "word": "eat", "meaning": "먹다", "example": "I eat lunch."},
    {"category": "🏃 기본 동작", "word": "drink", "meaning": "마시다", "example": "I drink water."},
    {"category": "🏃 기본 동작", "word": "sleep", "meaning": "자다", "example": "I sleep at night."},
    {"category": "🏃 기본 동작", "word": "wake up", "meaning": "일어나다", "example": "I wake up early."},
    {"category": "🏃 기본 동작", "word": "sit", "meaning": "앉다", "example": "Please sit down."},
    {"category": "🏃 기본 동작", "word": "stand", "meaning": "서다", "example": "Please stand up."},
    {"category": "🏃 기본 동작", "word": "walk", "meaning": "걷다", "example": "I walk to school."},
    {"category": "🏃 기본 동작", "word": "run", "meaning": "달리다", "example": "I can run fast."},
    {"category": "🏃 기본 동작", "word": "stop", "meaning": "멈추다", "example": "Stop here."},
    {"category": "🏃 기본 동작", "word": "start", "meaning": "시작하다", "example": "Let's start."},
    {"category": "🏃 기본 동작", "word": "look", "meaning": "보다", "example": "Look at this."},
    {"category": "🏃 기본 동작", "word": "see", "meaning": "보다", "example": "I see a bus."},
    {"category": "🏃 기본 동작", "word": "listen", "meaning": "듣다", "example": "Listen carefully."},
    {"category": "🏃 기본 동작", "word": "hear", "meaning": "들리다", "example": "I hear music."},
    {"category": "🏃 기본 동작", "word": "speak", "meaning": "말하다", "example": "I speak English."},
    {"category": "🏃 기본 동작", "word": "say", "meaning": "말하다", "example": "Say it again."},
    {"category": "🏃 기본 동작", "word": "read", "meaning": "읽다", "example": "I read a book."},
    {"category": "🏃 기본 동작", "word": "write", "meaning": "쓰다", "example": "Write your name."},

    # 3. 감정·몸 상태
    {"category": "💖 감정·몸 상태", "word": "happy", "meaning": "행복한", "example": "I am happy."},
    {"category": "💖 감정·몸 상태", "word": "sad", "meaning": "슬픈", "example": "I am sad."},
    {"category": "💖 감정·몸 상태", "word": "angry", "meaning": "화난", "example": "I am angry."},
    {"category": "💖 감정·몸 상태", "word": "scared", "meaning": "무서운", "example": "I am scared."},
    {"category": "💖 감정·몸 상태", "word": "tired", "meaning": "피곤한", "example": "I am tired."},
    {"category": "💖 감정·몸 상태", "word": "sleepy", "meaning": "졸린", "example": "I am sleepy."},
    {"category": "💖 감정·몸 상태", "word": "hungry", "meaning": "배고픈", "example": "I am hungry."},
    {"category": "💖 감정·몸 상태", "word": "thirsty", "meaning": "목마른", "example": "I am thirsty."},
    {"category": "💖 감정·몸 상태", "word": "sick", "meaning": "아픈", "example": "I am sick."},
    {"category": "💖 감정·몸 상태", "word": "hurt", "meaning": "다친, 아픈", "example": "My arm hurts."},
    {"category": "💖 감정·몸 상태", "word": "hot", "meaning": "더운, 뜨거운", "example": "I am hot."},
    {"category": "💖 감정·몸 상태", "word": "cold", "meaning": "추운, 차가운", "example": "I am cold."},
    {"category": "💖 감정·몸 상태", "word": "good", "meaning": "좋은", "example": "I feel good."},
    {"category": "💖 감정·몸 상태", "word": "bad", "meaning": "나쁜", "example": "I feel bad."},
    {"category": "💖 감정·몸 상태", "word": "okay", "meaning": "괜찮은", "example": "I am okay."},
    {"category": "💖 감정·몸 상태", "word": "fine", "meaning": "괜찮은", "example": "I am fine."},
    {"category": "💖 감정·몸 상태", "word": "busy", "meaning": "바쁜", "example": "I am busy."},
    {"category": "💖 감정·몸 상태", "word": "free", "meaning": "한가한, 자유로운", "example": "I am free now."},
    {"category": "💖 감정·몸 상태", "word": "worried", "meaning": "걱정하는", "example": "I am worried."},
    {"category": "💖 감정·몸 상태", "word": "excited", "meaning": "신난", "example": "I am excited."},

    # 4. 음식·물
    {"category": "🍎 음식·물", "word": "food", "meaning": "음식", "example": "I need food."},
    {"category": "🍎 음식·물", "word": "water", "meaning": "물", "example": "I need water."},
    {"category": "🍎 음식·물", "word": "rice", "meaning": "밥, 쌀", "example": "I eat rice."},
    {"category": "🍎 음식·물", "word": "bread", "meaning": "빵", "example": "I like bread."},
    {"category": "🍎 음식·물", "word": "milk", "meaning": "우유", "example": "I drink milk."},
    {"category": "🍎 음식·물", "word": "juice", "meaning": "주스", "example": "I drink juice."},
    {"category": "🍎 음식·물", "word": "coffee", "meaning": "커피", "example": "I like coffee."},
    {"category": "🍎 음식·물", "word": "tea", "meaning": "차", "example": "I drink tea."},
    {"category": "🍎 음식·물", "word": "breakfast", "meaning": "아침 식사", "example": "I eat breakfast."},
    {"category": "🍎 음식·물", "word": "lunch", "meaning": "점심", "example": "I eat lunch."},
    {"category": "🍎 음식·물", "word": "dinner", "meaning": "저녁", "example": "I eat dinner."},
    {"category": "🍎 음식·물", "word": "snack", "meaning": "간식", "example": "I eat a snack."},
    {"category": "🍎 음식·물", "word": "apple", "meaning": "사과", "example": "I eat an apple."},
    {"category": "🍎 음식·물", "word": "banana", "meaning": "바나나", "example": "I eat a banana."},
    {"category": "🍎 음식·물", "word": "chicken", "meaning": "닭고기", "example": "I like chicken."},
    {"category": "🍎 음식·물", "word": "fish", "meaning": "생선, 물고기", "example": "I eat fish."},
    {"category": "🍎 음식·물", "word": "egg", "meaning": "달걀", "example": "I eat an egg."},
    {"category": "🍎 음식·물", "word": "soup", "meaning": "수프, 국", "example": "I like soup."},
    {"category": "🍎 음식·물", "word": "delicious", "meaning": "맛있는", "example": "This is delicious."},
    {"category": "🍎 음식·물", "word": "spicy", "meaning": "매운", "example": "This food is spicy."},

    # 5. 장소·이동
    {"category": "🚗 장소·이동", "word": "school", "meaning": "학교", "example": "I go to school."},
    {"category": "🚗 장소·이동", "word": "home", "meaning": "집", "example": "I go home."},
    {"category": "🚗 장소·이동", "word": "classroom", "meaning": "교실", "example": "This is my classroom."},
    {"category": "🚗 장소·이동", "word": "bathroom", "meaning": "화장실", "example": "Where is the bathroom?"},
    {"category": "🚗 장소·이동", "word": "hospital", "meaning": "병원", "example": "I need a hospital."},
    {"category": "🚗 장소·이동", "word": "store", "meaning": "가게", "example": "I go to the store."},
    {"category": "🚗 장소·이동", "word": "restaurant", "meaning": "식당", "example": "This restaurant is good."},
    {"category": "🚗 장소·이동", "word": "park", "meaning": "공원", "example": "I go to the park."},
    {"category": "🚗 장소·이동", "word": "station", "meaning": "역", "example": "Where is the station?"},
    {"category": "🚗 장소·이동", "word": "airport", "meaning": "공항", "example": "I go to the airport."},
    {"category": "🚗 장소·이동", "word": "bus", "meaning": "버스", "example": "I take a bus."},
    {"category": "🚗 장소·이동", "word": "train", "meaning": "기차", "example": "I take a train."},
    {"category": "🚗 장소·이동", "word": "taxi", "meaning": "택시", "example": "I take a taxi."},
    {"category": "🚗 장소·이동", "word": "car", "meaning": "자동차", "example": "This is my car."},
    {"category": "🚗 장소·이동", "word": "bike", "meaning": "자전거", "example": "I ride a bike."},
    {"category": "🚗 장소·이동", "word": "road", "meaning": "길, 도로", "example": "This road is long."},
    {"category": "🚗 장소·이동", "word": "street", "meaning": "거리", "example": "This street is busy."},
    {"category": "🚗 장소·이동", "word": "left", "meaning": "왼쪽", "example": "Turn left."},
    {"category": "🚗 장소·이동", "word": "right", "meaning": "오른쪽", "example": "Turn right."},
    {"category": "🚗 장소·이동", "word": "straight", "meaning": "똑바로", "example": "Go straight."},

    # 6. 시간·숫자
    {"category": "⏰ 시간·숫자", "word": "today", "meaning": "오늘", "example": "Today is Monday."},
    {"category": "⏰ 시간·숫자", "word": "tomorrow", "meaning": "내일", "example": "See you tomorrow."},
    {"category": "⏰ 시간·숫자", "word": "yesterday", "meaning": "어제", "example": "I was busy yesterday."},
    {"category": "⏰ 시간·숫자", "word": "now", "meaning": "지금", "example": "I am busy now."},
    {"category": "⏰ 시간·숫자", "word": "later", "meaning": "나중에", "example": "See you later."},
    {"category": "⏰ 시간·숫자", "word": "morning", "meaning": "아침", "example": "Good morning."},
    {"category": "⏰ 시간·숫자", "word": "afternoon", "meaning": "오후", "example": "Good afternoon."},
    {"category": "⏰ 시간·숫자", "word": "evening", "meaning": "저녁", "example": "Good evening."},
    {"category": "⏰ 시간·숫자", "word": "night", "meaning": "밤", "example": "Good night."},
    {"category": "⏰ 시간·숫자", "word": "time", "meaning": "시간", "example": "What time is it?"},
    {"category": "⏰ 시간·숫자", "word": "one", "meaning": "하나", "example": "I have one book."},
    {"category": "⏰ 시간·숫자", "word": "two", "meaning": "둘", "example": "I have two pens."},
    {"category": "⏰ 시간·숫자", "word": "three", "meaning": "셋", "example": "I have three friends."},
    {"category": "⏰ 시간·숫자", "word": "four", "meaning": "넷", "example": "I have four books."},
    {"category": "⏰ 시간·숫자", "word": "five", "meaning": "다섯", "example": "I have five apples."},
    {"category": "⏰ 시간·숫자", "word": "six", "meaning": "여섯", "example": "I have six pencils."},
    {"category": "⏰ 시간·숫자", "word": "seven", "meaning": "일곱", "example": "I wake up at seven."},
    {"category": "⏰ 시간·숫자", "word": "eight", "meaning": "여덟", "example": "I sleep at eight."},
    {"category": "⏰ 시간·숫자", "word": "nine", "meaning": "아홉", "example": "It is nine o'clock."},
    {"category": "⏰ 시간·숫자", "word": "ten", "meaning": "열", "example": "I have ten fingers."},

    # 7. 학교생활
    {"category": "🏫 학교생활", "word": "book", "meaning": "책", "example": "This is my book."},
    {"category": "🏫 학교생활", "word": "notebook", "meaning": "공책", "example": "I have a notebook."},
    {"category": "🏫 학교생활", "word": "pen", "meaning": "펜", "example": "This is my pen."},
    {"category": "🏫 학교생활", "word": "pencil", "meaning": "연필", "example": "I need a pencil."},
    {"category": "🏫 학교생활", "word": "desk", "meaning": "책상", "example": "This is my desk."},
    {"category": "🏫 학교생활", "word": "chair", "meaning": "의자", "example": "Sit on the chair."},
    {"category": "🏫 학교생활", "word": "bag", "meaning": "가방", "example": "This is my bag."},
    {"category": "🏫 학교생활", "word": "homework", "meaning": "숙제", "example": "I do my homework."},
    {"category": "🏫 학교생활", "word": "test", "meaning": "시험", "example": "I have a test."},
    {"category": "🏫 학교생활", "word": "question", "meaning": "질문", "example": "I have a question."},
    {"category": "🏫 학교생활", "word": "answer", "meaning": "대답, 정답", "example": "What is the answer?"},
    {"category": "🏫 학교생활", "word": "lesson", "meaning": "수업", "example": "This lesson is easy."},
    {"category": "🏫 학교생활", "word": "English", "meaning": "영어", "example": "I study English."},
    {"category": "🏫 학교생활", "word": "Korean", "meaning": "한국어", "example": "I speak Korean."},
    {"category": "🏫 학교생활", "word": "math", "meaning": "수학", "example": "I study math."},
    {"category": "🏫 학교생활", "word": "easy", "meaning": "쉬운", "example": "This is easy."},
    {"category": "🏫 학교생활", "word": "hard", "meaning": "어려운, 힘든", "example": "This is hard."},
    {"category": "🏫 학교생활", "word": "right answer", "meaning": "정답", "example": "This is the right answer."},
    {"category": "🏫 학교생활", "word": "wrong answer", "meaning": "오답", "example": "This is the wrong answer."},
    {"category": "🏫 학교생활", "word": "again", "meaning": "다시", "example": "Try again."},

    # 8. 생존 표현
    {"category": "🛟 생존 표현", "word": "help", "meaning": "도움, 도와주다", "example": "Help me, please."},
    {"category": "🛟 생존 표현", "word": "please", "meaning": "제발, 부탁합니다", "example": "Please help me."},
    {"category": "🛟 생존 표현", "word": "thank you", "meaning": "고마워요", "example": "Thank you very much."},
    {"category": "🛟 생존 표현", "word": "sorry", "meaning": "미안한", "example": "I am sorry."},
    {"category": "🛟 생존 표현", "word": "excuse me", "meaning": "실례합니다", "example": "Excuse me."},
    {"category": "🛟 생존 표현", "word": "yes", "meaning": "네", "example": "Yes, I can."},
    {"category": "🛟 생존 표현", "word": "no", "meaning": "아니요", "example": "No, I can't."},
    {"category": "🛟 생존 표현", "word": "okay", "meaning": "괜찮아", "example": "Okay, I understand."},
    {"category": "🛟 생존 표현", "word": "wait", "meaning": "기다리다", "example": "Wait a minute."},
    {"category": "🛟 생존 표현", "word": "dangerous", "meaning": "위험한", "example": "This place is dangerous."},
    {"category": "🛟 생존 표현", "word": "safe", "meaning": "안전한", "example": "This place is safe."},
    {"category": "🛟 생존 표현", "word": "lost", "meaning": "길을 잃은", "example": "I am lost."},
    {"category": "🛟 생존 표현", "word": "problem", "meaning": "문제", "example": "I have a problem."},
    {"category": "🛟 생존 표현", "word": "money", "meaning": "돈", "example": "I need money."},
    {"category": "🛟 생존 표현", "word": "phone", "meaning": "전화기", "example": "I need a phone."},
    {"category": "🛟 생존 표현", "word": "name", "meaning": "이름", "example": "What is your name?"},
    {"category": "🛟 생존 표현", "word": "number", "meaning": "번호, 숫자", "example": "What is your phone number?"},
    {"category": "🛟 생존 표현", "word": "address", "meaning": "주소", "example": "What is your address?"},
    {"category": "🛟 생존 표현", "word": "police", "meaning": "경찰", "example": "Call the police."},
    {"category": "🛟 생존 표현", "word": "emergency", "meaning": "응급 상황", "example": "This is an emergency."},
]

# 개수 확인용
TOTAL_WORDS = len(WORDS)

# =========================
# 카테고리 정리
# =========================
categories = []
for item in WORDS:
    if item["category"] not in categories:
        categories.append(item["category"])

# =========================
# 제목
# =========================
st.markdown('<div class="main-title">🛟 Survival English 160</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="sub-title">기초 생존 영어 단어 {TOTAL_WORDS}개를 듣고, 모르는 단어를 체크해 보세요.</div>',
    unsafe_allow_html=True
)

# =========================
# 탭
# =========================
tab_names = categories + ["⭐ 모르는 단어 모음"]
tabs = st.tabs(tab_names)

# =========================
# 카테고리별 탭
# =========================
for idx, category in enumerate(categories):
    with tabs[idx]:
        category_words = [item for item in WORDS if item["category"] == category]

        st.markdown(
            f"""
            <div class="section-box">
                <h3>{category}</h3>
                <div class="small-guide">
                    단어를 듣고 뜻과 예문을 확인하세요. 모르는 단어는 체크하면 마지막 탭에 자동으로 모입니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"### {category} 단어 {len(category_words)}개")

        for item in category_words:
            show_word_card(item, key_prefix=category.replace(" ", "_"))


# =========================
# 마지막 탭: 모르는 단어 모음
# =========================
with tabs[-1]:
    st.markdown("## ⭐ 내가 체크한 모르는 단어")

    unknown_words = st.session_state.unknown_words
    unknown_info = st.session_state.unknown_word_info

    if not unknown_words:
        st.info("아직 체크한 단어가 없습니다. 각 탭에서 모르는 단어를 체크해 보세요.")
    else:
        st.success(f"총 {len(unknown_words)}개의 단어를 체크했습니다.")

        st.markdown("### 🎧 체크한 단어 전체 듣기")

        all_words_text = ". ".join(unknown_words)

        c1, c2 = st.columns([1, 5])

        with c1:
            if st.button("🔊 전체 듣기", key="listen_all_unknown_words"):
                play_audio(all_words_text)

        with c2:
            st.markdown("체크한 단어를 한 번에 들을 수 있습니다.")

        st.divider()

        st.markdown("### 📌 체크한 단어 목록")

        for i, word in enumerate(unknown_words, start=1):
            info = unknown_info.get(word, {})
            meaning = info.get("meaning", "")
            example = info.get("example", "")
            category = info.get("category", "")

            st.markdown(
                f"""
                <div class="word-card">
                    <div class="word-text">{i}. {word}</div>
                    <div class="meaning-text">뜻: <b>{meaning}</b></div>
                    <div class="example-text">분류: {category}</div>
                    <div class="example-text">예문: {example}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            c1, c2, c3 = st.columns([1, 1, 5])

            with c1:
                if st.button("🔊 듣기", key=f"unknown_listen_{word}"):
                    play_audio(word)

            with c2:
                if st.button("삭제", key=f"delete_unknown_{word}"):
                    remove_unknown(word)
                    st.rerun()

            st.divider()

        if st.button("🗑️ 체크한 단어 전체 삭제", key="clear_all_unknown_words"):
            st.session_state.unknown_words = []
            st.session_state.unknown_word_info = {}
            st.rerun()
