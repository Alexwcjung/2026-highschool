
import streamlit as st
from gtts import gTTS
import io
import random
import base64
import uuid
import re
import json
import html
import streamlit.components.v1 as components

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Survival English 160",
    page_icon="🛟",
    layout="wide"
)

# =========================
# CSS 디자인
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
        background: linear-gradient(135deg, #ecfeff 0%, #fef3c7 50%, #fce7f3 100%);
        border-radius: 22px;
        padding: 18px 22px;
        margin-bottom: 24px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        border: 1px solid rgba(255,255,255,0.8);
    }

    .hero-title {
        font-size: 27px;
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
        background: linear-gradient(135deg, #0ea5e9 0%, #8b5cf6 50%, #ec4899 100%);
        color: white;
        padding: 22px 26px;
        border-radius: 24px;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(14,165,233,0.25);
    }

    .theme-title {
        font-size: 27px;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .theme-desc {
        font-size: 15px;
        opacity: 0.95;
    }

    .dialogue-box {
        background: #fefce8;
        border: 1px solid #fde68a;
        border-radius: 24px;
        padding: 20px 22px;
        margin-bottom: 24px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    .dialogue-title {
        font-size: 24px;
        font-weight: 900;
        color: #854d0e;
        margin-bottom: 14px;
    }

    .dialogue-line {
        font-size: 18px;
        font-weight: 900;
        color: #111827;
        margin-top: 10px;
    }

    .dialogue-meaning {
        font-size: 15px;
        color: #6b7280;
        margin-bottom: 5px;
    }

    .word-card {
        background: white;
        border-radius: 18px;
        padding: 10px 14px;
        margin-bottom: 8px;
        border: 1px solid #e0f2fe;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }

    .word-row {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .word-number {
        min-width: 38px;
        font-size: 13px;
        font-weight: 900;
        color: #0369a1;
        background: #e0f2fe;
        border-radius: 999px;
        padding: 5px 9px;
        text-align: center;
    }

    .word-text {
        min-width: 170px;
        font-size: 25px;
        font-weight: 900;
        color: #111827;
        white-space: nowrap;
    }

    .meaning-text {
        font-size: 19px;
        font-weight: 800;
        color: #374151;
        margin-left: 8px;
        white-space: nowrap;
        line-height: 42px;
    }

    .emoji-text {
        font-size: 25px;
        line-height: 1;
        text-align: center;
        padding-top: 2px;
    }

    .quiz-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 22px 24px;
        margin-bottom: 18px;
        border: 1px solid #e9d5ff;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    }

    .quiz-number {
        display: inline-block;
        background: #dcfce7;
        color: #166534;
        padding: 6px 12px;
        border-radius: 999px;
        font-weight: 900;
        font-size: 13px;
        margin-bottom: 10px;
    }

    .quiz-word {
        font-size: 34px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 24px;
        padding: 24px 26px;
        margin: 20px 0;
        border: 1px solid #bbf7d0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    .score-title {
        font-size: 27px;
        font-weight: 900;
        color: #14532d;
    }

    .wrong-box {
        background: #fff7ed;
        border-left: 6px solid #fb923c;
        border-radius: 18px;
        padding: 16px 18px;
        margin: 18px 0;
        color: #7c2d12;
        font-weight: 700;
    }

    .answer-box {
        background: #f8fafc;
        border-radius: 20px;
        padding: 18px 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        border: 1px solid #d1d5db;
        padding: 0.45rem 1rem;
    }

    .stButton > button:hover {
        border-color: #0ea5e9;
        color: #0ea5e9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 상단 제목
# =========================
st.markdown("<div class='main-title'>🛟 Survival English 160</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>생존 회화에 꼭 필요한 문장과 단어를 듣고, 따라 하고, 퀴즈로 익혀 봅시다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-text" style="font-size:18px; font-weight:900; color:#374151;">
            이 단어 160개만 외우면 미국에서 생존이 가능합니다.
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


def remove_speaker_label(sentence):
    return re.sub(r"^[A-Z]:\s*", "", sentence).strip()


def make_dialogue_tts_text(dialogue):
    return " ".join([remove_speaker_label(item["en"]) for item in dialogue])


# =========================
# 생존 회화 160 테마별 단어
# =========================
word_themes = {
    "🧍 나와 사람": [
        {"word": "I", "meaning": "나"},
        {"word": "you", "meaning": "너, 당신"},
        {"word": "he", "meaning": "그"},
        {"word": "she", "meaning": "그녀"},
        {"word": "we", "meaning": "우리"},
        {"word": "they", "meaning": "그들"},
        {"word": "friend", "meaning": "친구"},
        {"word": "teacher", "meaning": "선생님"},
        {"word": "student", "meaning": "학생"},
        {"word": "classmate", "meaning": "반 친구"},
        {"word": "family", "meaning": "가족"},
        {"word": "father", "meaning": "아버지"},
        {"word": "mother", "meaning": "어머니"},
        {"word": "brother", "meaning": "형제, 남자 형제"},
        {"word": "sister", "meaning": "자매, 여자 형제"},
        {"word": "name", "meaning": "이름"},
        {"word": "person", "meaning": "사람"},
        {"word": "man", "meaning": "남자"},
        {"word": "woman", "meaning": "여자"},
        {"word": "child", "meaning": "아이"},
    ],
    "🏃 기본 동작": [
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
        {"word": "eat", "meaning": "먹다"},
        {"word": "drink", "meaning": "마시다"},
        {"word": "sleep", "meaning": "자다"},
        {"word": "study", "meaning": "공부하다"},
        {"word": "read", "meaning": "읽다"},
        {"word": "write", "meaning": "쓰다"},
        {"word": "listen", "meaning": "듣다"},
        {"word": "speak", "meaning": "말하다"},
        {"word": "help", "meaning": "돕다"},
        {"word": "wait", "meaning": "기다리다"},
    ],
    "💖 감정·몸 상태": [
        {"word": "happy", "meaning": "행복한"},
        {"word": "sad", "meaning": "슬픈"},
        {"word": "angry", "meaning": "화난"},
        {"word": "tired", "meaning": "피곤한"},
        {"word": "hungry", "meaning": "배고픈"},
        {"word": "thirsty", "meaning": "목마른"},
        {"word": "sick", "meaning": "아픈"},
        {"word": "okay", "meaning": "괜찮은"},
        {"word": "fine", "meaning": "괜찮은"},
        {"word": "cold", "meaning": "추운, 차가운"},
        {"word": "hot", "meaning": "더운, 뜨거운"},
        {"word": "pain", "meaning": "통증"},
        {"word": "headache", "meaning": "두통"},
        {"word": "stomachache", "meaning": "복통"},
        {"word": "fever", "meaning": "열"},
        {"word": "hurt", "meaning": "아프다, 다치다"},
        {"word": "good", "meaning": "좋은"},
        {"word": "bad", "meaning": "나쁜"},
        {"word": "worried", "meaning": "걱정하는"},
        {"word": "scared", "meaning": "무서워하는"},
    ],
    "🍎 음식·물": [
        {"word": "food", "meaning": "음식"},
        {"word": "water", "meaning": "물"},
        {"word": "rice", "meaning": "밥, 쌀"},
        {"word": "bread", "meaning": "빵"},
        {"word": "milk", "meaning": "우유"},
        {"word": "juice", "meaning": "주스"},
        {"word": "coffee", "meaning": "커피"},
        {"word": "tea", "meaning": "차"},
        {"word": "apple", "meaning": "사과"},
        {"word": "banana", "meaning": "바나나"},
        {"word": "egg", "meaning": "달걀"},
        {"word": "meat", "meaning": "고기"},
        {"word": "chicken", "meaning": "닭고기, 닭"},
        {"word": "fish", "meaning": "생선, 물고기"},
        {"word": "breakfast", "meaning": "아침 식사"},
        {"word": "lunch", "meaning": "점심 식사"},
        {"word": "dinner", "meaning": "저녁 식사"},
        {"word": "snack", "meaning": "간식"},
        {"word": "medicine", "meaning": "약"},
        {"word": "hospital", "meaning": "병원"},
    ],
    "🚗 장소·이동": [
        {"word": "home", "meaning": "집"},
        {"word": "school", "meaning": "학교"},
        {"word": "classroom", "meaning": "교실"},
        {"word": "bathroom", "meaning": "화장실"},
        {"word": "hospital", "meaning": "병원"},
        {"word": "store", "meaning": "가게"},
        {"word": "station", "meaning": "역"},
        {"word": "bus", "meaning": "버스"},
        {"word": "car", "meaning": "자동차"},
        {"word": "taxi", "meaning": "택시"},
        {"word": "train", "meaning": "기차"},
        {"word": "bike", "meaning": "자전거"},
        {"word": "road", "meaning": "도로"},
        {"word": "street", "meaning": "거리"},
        {"word": "here", "meaning": "여기"},
        {"word": "there", "meaning": "거기"},
        {"word": "near", "meaning": "가까운"},
        {"word": "far", "meaning": "먼"},
        {"word": "left", "meaning": "왼쪽"},
        {"word": "right", "meaning": "오른쪽, 맞는"},
    ],
    "⏰ 시간·숫자": [
        {"word": "time", "meaning": "시간"},
        {"word": "now", "meaning": "지금"},
        {"word": "today", "meaning": "오늘"},
        {"word": "tomorrow", "meaning": "내일"},
        {"word": "yesterday", "meaning": "어제"},
        {"word": "morning", "meaning": "아침"},
        {"word": "afternoon", "meaning": "오후"},
        {"word": "evening", "meaning": "저녁"},
        {"word": "night", "meaning": "밤"},
        {"word": "early", "meaning": "이른"},
        {"word": "late", "meaning": "늦은"},
        {"word": "one", "meaning": "하나"},
        {"word": "two", "meaning": "둘"},
        {"word": "three", "meaning": "셋"},
        {"word": "four", "meaning": "넷"},
        {"word": "five", "meaning": "다섯"},
        {"word": "six", "meaning": "여섯"},
        {"word": "seven", "meaning": "일곱"},
        {"word": "eight", "meaning": "여덟"},
        {"word": "ten", "meaning": "열"},
    ],
    "🎒 물건·돈": [
        {"word": "bag", "meaning": "가방"},
        {"word": "phone", "meaning": "전화기"},
        {"word": "book", "meaning": "책"},
        {"word": "notebook", "meaning": "공책"},
        {"word": "pen", "meaning": "펜"},
        {"word": "pencil", "meaning": "연필"},
        {"word": "desk", "meaning": "책상"},
        {"word": "chair", "meaning": "의자"},
        {"word": "door", "meaning": "문"},
        {"word": "window", "meaning": "창문"},
        {"word": "key", "meaning": "열쇠"},
        {"word": "money", "meaning": "돈"},
        {"word": "card", "meaning": "카드"},
        {"word": "ticket", "meaning": "표, 티켓"},
        {"word": "clothes", "meaning": "옷"},
        {"word": "shoes", "meaning": "신발"},
        {"word": "hat", "meaning": "모자"},
        {"word": "watch", "meaning": "시계"},
        {"word": "cup", "meaning": "컵"},
        {"word": "bottle", "meaning": "병"},
    ],
    "🆘 도움 요청": [
        {"word": "help", "meaning": "도움, 돕다"},
        {"word": "please", "meaning": "부디, 제발"},
        {"word": "sorry", "meaning": "미안합니다"},
        {"word": "excuse me", "meaning": "실례합니다"},
        {"word": "again", "meaning": "다시"},
        {"word": "slowly", "meaning": "천천히"},
        {"word": "understand", "meaning": "이해하다"},
        {"word": "question", "meaning": "질문"},
        {"word": "problem", "meaning": "문제"},
        {"word": "need", "meaning": "필요하다"},
        {"word": "want", "meaning": "원하다"},
        {"word": "know", "meaning": "알다"},
        {"word": "say", "meaning": "말하다"},
        {"word": "tell", "meaning": "말하다, 알려주다"},
        {"word": "ask", "meaning": "묻다"},
        {"word": "answer", "meaning": "대답, 답"},
        {"word": "repeat", "meaning": "반복하다"},
        {"word": "speak", "meaning": "말하다"},
        {"word": "look", "meaning": "보다"},
        {"word": "listen", "meaning": "듣다"},
    ],
}

# =========================
# 단어별 예문
# =========================
CASSETTE_EXAMPLES = {
    "I": "I am a student.", "you": "You are my friend.", "he": "He is my friend.", "she": "She is a student.",
    "we": "We are happy.", "they": "They are students.", "friend": "He is my friend.", "teacher": "She is my teacher.",
    "student": "I am a student.", "classmate": "He is my classmate.", "family": "This is my family.",
    "father": "He is my father.", "mother": "She is my mother.", "brother": "He is my brother.",
    "sister": "She is my sister.", "name": "My name is Alex.", "person": "He is a good person.",
    "man": "He is a man.", "woman": "She is a woman.", "child": "He is a child.",

    "go": "I go to school.", "come": "Please come here.", "walk": "I walk to school.", "run": "I can run.",
    "sit": "Please sit down.", "stand": "Please stand up.", "stop": "Please stop.", "start": "Let's start.",
    "open": "Open the door.", "close": "Close the door.", "eat": "I eat lunch.", "drink": "I drink water.",
    "sleep": "I sleep at night.", "study": "I study English.", "read": "I read a book.", "write": "I write my name.",
    "listen": "Listen carefully.", "speak": "Please speak slowly.", "help": "Can you help me?", "wait": "Please wait.",

    "happy": "I am happy.", "sad": "I am sad.", "angry": "I am angry.", "tired": "I am tired.",
    "hungry": "I am hungry.", "thirsty": "I am thirsty.", "sick": "I am sick.", "okay": "I am okay.",
    "fine": "I am fine.", "cold": "I am cold.", "hot": "It is hot.", "pain": "I have pain.",
    "headache": "I have a headache.", "stomachache": "I have a stomachache.", "fever": "I have a fever.",
    "hurt": "My leg hurts.", "good": "It is good.", "bad": "It is bad.", "worried": "I am worried.",
    "scared": "I am scared.",

    "food": "I need food.", "water": "I need water.", "rice": "I eat rice.", "bread": "I eat bread.",
    "milk": "I drink milk.", "juice": "I drink juice.", "coffee": "I drink coffee.", "tea": "I drink tea.",
    "apple": "I like apples.", "banana": "I like bananas.", "egg": "I eat an egg.", "meat": "I eat meat.",
    "chicken": "I like chicken.", "fish": "I eat fish.", "breakfast": "I eat breakfast.", "lunch": "I eat lunch.",
    "dinner": "I eat dinner.", "snack": "I want a snack.", "medicine": "I need medicine.", "hospital": "I need a hospital.",

    "home": "I go home.", "school": "I go to school.", "classroom": "This is my classroom.",
    "bathroom": "Where is the bathroom?", "store": "I go to the store.", "station": "Where is the station?",
    "bus": "I take a bus.", "car": "This is my car.", "taxi": "I need a taxi.", "train": "I take a train.",
    "bike": "I ride a bike.", "road": "This road is long.", "street": "This street is busy.",
    "here": "Come here.", "there": "Go there.", "near": "It is near here.", "far": "It is far.",
    "left": "Turn left.", "right": "Turn right.",

    "time": "What time is it?", "now": "I am here now.", "today": "Today is Monday.",
    "tomorrow": "See you tomorrow.", "yesterday": "I studied yesterday.", "morning": "Good morning.",
    "afternoon": "Good afternoon.", "evening": "Good evening.", "night": "Good night.",
    "early": "It is early.", "late": "It is late.", "one": "I have one book.", "two": "I have two books.",
    "three": "I have three books.", "four": "I have four books.", "five": "I have five books.",
    "six": "I have six books.", "seven": "I have seven books.", "eight": "I have eight books.",
    "ten": "I have ten books.",

    "bag": "This is my bag.", "phone": "This is my phone.", "book": "This is my book.",
    "notebook": "This is my notebook.", "pen": "I have a pen.", "pencil": "I have a pencil.",
    "desk": "This is my desk.", "chair": "This is my chair.", "door": "Open the door.",
    "window": "Close the window.", "key": "I need a key.", "money": "I need money.",
    "card": "I have a card.", "ticket": "I need a ticket.", "clothes": "These are my clothes.",
    "shoes": "These are my shoes.", "hat": "This is my hat.", "watch": "This is my watch.",
    "cup": "This is my cup.", "bottle": "This is my bottle.",

    "please": "Please help me.", "sorry": "I am sorry.", "excuse me": "Excuse me.",
    "again": "Please say it again.", "slowly": "Please speak slowly.", "understand": "I understand.",
    "question": "I have a question.", "problem": "I have a problem.", "need": "I need help.",
    "want": "I want water.", "know": "I know.", "say": "Please say it again.",
    "tell": "Please tell me.", "ask": "Can I ask you?", "answer": "This is the answer.",
    "repeat": "Please repeat.", "look": "Look at this.",
}

CASSETTE_EXAMPLES_KO = {
    "I": "나는 학생입니다.", "you": "너는 나의 친구입니다.", "he": "그는 나의 친구입니다.", "she": "그녀는 학생입니다.",
    "we": "우리는 행복합니다.", "they": "그들은 학생들입니다.", "friend": "그는 나의 친구입니다.", "teacher": "그녀는 나의 선생님입니다.",
    "student": "나는 학생입니다.", "classmate": "그는 나의 반 친구입니다.", "family": "이것은 나의 가족입니다.",
    "father": "그는 나의 아버지입니다.", "mother": "그녀는 나의 어머니입니다.", "brother": "그는 나의 남자 형제입니다.",
    "sister": "그녀는 나의 여자 형제입니다.", "name": "내 이름은 Alex입니다.", "person": "그는 좋은 사람입니다.",
    "man": "그는 남자입니다.", "woman": "그녀는 여자입니다.", "child": "그는 아이입니다.",

    "go": "나는 학교에 갑니다.", "come": "이리 와 주세요.", "walk": "나는 걸어서 학교에 갑니다.", "run": "나는 달릴 수 있습니다.",
    "sit": "앉아 주세요.", "stand": "일어나 주세요.", "stop": "멈춰 주세요.", "start": "시작합시다.",
    "open": "문을 여세요.", "close": "문을 닫으세요.", "eat": "나는 점심을 먹습니다.", "drink": "나는 물을 마십니다.",
    "sleep": "나는 밤에 잡니다.", "study": "나는 영어를 공부합니다.", "read": "나는 책을 읽습니다.", "write": "나는 내 이름을 씁니다.",
    "listen": "주의 깊게 들으세요.", "speak": "천천히 말해 주세요.", "help": "나를 도와줄 수 있나요?", "wait": "기다려 주세요.",

    "happy": "나는 행복합니다.", "sad": "나는 슬픕니다.", "angry": "나는 화가 났습니다.", "tired": "나는 피곤합니다.",
    "hungry": "나는 배고픕니다.", "thirsty": "나는 목마릅니다.", "sick": "나는 아픕니다.", "okay": "나는 괜찮습니다.",
    "fine": "나는 괜찮습니다.", "cold": "나는 춥습니다.", "hot": "날씨가 덥습니다.", "pain": "나는 통증이 있습니다.",
    "headache": "나는 두통이 있습니다.", "stomachache": "나는 복통이 있습니다.", "fever": "나는 열이 있습니다.",
    "hurt": "내 다리가 아픕니다.", "good": "그것은 좋습니다.", "bad": "그것은 나쁩니다.", "worried": "나는 걱정됩니다.",
    "scared": "나는 무섭습니다.",

    "food": "나는 음식이 필요합니다.", "water": "나는 물이 필요합니다.", "rice": "나는 밥을 먹습니다.", "bread": "나는 빵을 먹습니다.",
    "milk": "나는 우유를 마십니다.", "juice": "나는 주스를 마십니다.", "coffee": "나는 커피를 마십니다.", "tea": "나는 차를 마십니다.",
    "apple": "나는 사과를 좋아합니다.", "banana": "나는 바나나를 좋아합니다.", "egg": "나는 달걀 하나를 먹습니다.",
    "meat": "나는 고기를 먹습니다.", "chicken": "나는 닭고기를 좋아합니다.", "fish": "나는 생선을 먹습니다.",
    "breakfast": "나는 아침 식사를 먹습니다.", "lunch": "나는 점심을 먹습니다.", "dinner": "나는 저녁을 먹습니다.",
    "snack": "나는 간식을 원합니다.", "medicine": "나는 약이 필요합니다.", "hospital": "나는 병원이 필요합니다.",

    "home": "나는 집에 갑니다.", "school": "나는 학교에 갑니다.", "classroom": "여기는 나의 교실입니다.",
    "bathroom": "화장실이 어디에 있나요?", "store": "나는 가게에 갑니다.", "station": "역은 어디에 있나요?",
    "bus": "나는 버스를 탑니다.", "car": "이것은 나의 차입니다.", "taxi": "나는 택시가 필요합니다.",
    "train": "나는 기차를 탑니다.", "bike": "나는 자전거를 탑니다.", "road": "이 도로는 깁니다.",
    "street": "이 거리는 붐빕니다.", "here": "여기로 오세요.", "there": "그곳으로 가세요.",
    "near": "그것은 여기 근처에 있습니다.", "far": "그것은 멉니다.", "left": "왼쪽으로 도세요.", "right": "오른쪽으로 도세요.",

    "time": "지금 몇 시인가요?", "now": "나는 지금 여기에 있습니다.", "today": "오늘은 월요일입니다.",
    "tomorrow": "내일 봅시다.", "yesterday": "나는 어제 공부했습니다.", "morning": "좋은 아침입니다.",
    "afternoon": "좋은 오후입니다.", "evening": "좋은 저녁입니다.", "night": "안녕히 주무세요.",
    "early": "이릅니다.", "late": "늦었습니다.", "one": "나는 책 한 권이 있습니다.",
    "two": "나는 책 두 권이 있습니다.", "three": "나는 책 세 권이 있습니다.", "four": "나는 책 네 권이 있습니다.",
    "five": "나는 책 다섯 권이 있습니다.", "six": "나는 책 여섯 권이 있습니다.", "seven": "나는 책 일곱 권이 있습니다.",
    "eight": "나는 책 여덟 권이 있습니다.", "ten": "나는 책 열 권이 있습니다.",

    "bag": "이것은 나의 가방입니다.", "phone": "이것은 나의 전화기입니다.", "book": "이것은 나의 책입니다.",
    "notebook": "이것은 나의 공책입니다.", "pen": "나는 펜이 있습니다.", "pencil": "나는 연필이 있습니다.",
    "desk": "이것은 나의 책상입니다.", "chair": "이것은 나의 의자입니다.", "door": "문을 여세요.",
    "window": "창문을 닫으세요.", "key": "나는 열쇠가 필요합니다.", "money": "나는 돈이 필요합니다.",
    "card": "나는 카드가 있습니다.", "ticket": "나는 표가 필요합니다.", "clothes": "이것들은 나의 옷입니다.",
    "shoes": "이것들은 나의 신발입니다.", "hat": "이것은 나의 모자입니다.", "watch": "이것은 나의 시계입니다.",
    "cup": "이것은 나의 컵입니다.", "bottle": "이것은 나의 병입니다.",

    "please": "제발 나를 도와주세요.", "sorry": "미안합니다.", "excuse me": "실례합니다.",
    "again": "다시 말해 주세요.", "slowly": "천천히 말해 주세요.", "understand": "나는 이해합니다.",
    "question": "나는 질문이 있습니다.", "problem": "나는 문제가 있습니다.", "need": "나는 도움이 필요합니다.",
    "want": "나는 물을 원합니다.", "know": "나는 압니다.", "say": "다시 말해 주세요.",
    "tell": "나에게 말해 주세요.", "ask": "질문해도 될까요?", "answer": "이것이 답입니다.",
    "repeat": "반복해 주세요.", "look": "이것을 보세요.",
}

# =========================
# 단어별 이모지
# =========================
WORD_EMOJIS = {
    "I": "🙋", "you": "👉", "he": "👦", "she": "👧", "we": "👥", "they": "👥",
    "friend": "🤝", "teacher": "👩‍🏫", "student": "🧑‍🎓", "classmate": "👫", "family": "👨‍👩‍👧",
    "father": "👨", "mother": "👩", "brother": "👦", "sister": "👧", "name": "🏷️",
    "person": "🧍", "man": "👨", "woman": "👩", "child": "🧒",
    "go": "➡️", "come": "⬅️", "walk": "🚶", "run": "🏃", "sit": "🪑", "stand": "🧍",
    "stop": "🛑", "start": "▶️", "open": "📂", "close": "📕", "eat": "🍽️", "drink": "🥤",
    "sleep": "😴", "study": "📚", "read": "📖", "write": "✏️", "listen": "👂", "speak": "🗣️",
    "help": "🆘", "wait": "⏳",
    "happy": "😊", "sad": "😢", "angry": "😠", "tired": "🥱", "hungry": "😋", "thirsty": "🥤",
    "sick": "🤒", "okay": "👌", "fine": "🙂", "cold": "🥶", "hot": "🥵", "pain": "🤕",
    "headache": "🤯", "stomachache": "🤢", "fever": "🌡️", "hurt": "🩹", "good": "👍", "bad": "👎",
    "worried": "😟", "scared": "😨",
    "food": "🍽️", "water": "💧", "rice": "🍚", "bread": "🍞", "milk": "🥛", "juice": "🧃",
    "coffee": "☕", "tea": "🍵", "apple": "🍎", "banana": "🍌", "egg": "🥚", "meat": "🥩",
    "chicken": "🍗", "fish": "🐟", "breakfast": "🍳", "lunch": "🍱", "dinner": "🍽️", "snack": "🍪",
    "medicine": "💊", "hospital": "🏥",
    "home": "🏠", "school": "🏫", "classroom": "🧑‍🏫", "bathroom": "🚻", "store": "🏪", "station": "🚉",
    "bus": "🚌", "car": "🚗", "taxi": "🚕", "train": "🚆", "bike": "🚲", "road": "🛣️",
    "street": "🏙️", "here": "📍", "there": "📌", "near": "↔️", "far": "🌁", "left": "⬅️", "right": "➡️",
    "time": "⏰", "now": "🕒", "today": "📅", "tomorrow": "➡️📅", "yesterday": "⬅️📅",
    "morning": "🌅", "afternoon": "☀️", "evening": "🌆", "night": "🌙", "early": "🐓", "late": "🌃",
    "one": "1️⃣", "two": "2️⃣", "three": "3️⃣", "four": "4️⃣", "five": "5️⃣", "six": "6️⃣",
    "seven": "7️⃣", "eight": "8️⃣", "ten": "🔟",
    "bag": "🎒", "phone": "📱", "book": "📘", "notebook": "📓", "pen": "🖊️", "pencil": "✏️",
    "desk": "🪑", "chair": "🪑", "door": "🚪", "window": "🪟", "key": "🔑", "money": "💵",
    "card": "💳", "ticket": "🎫", "clothes": "👕", "shoes": "👟", "hat": "🧢", "watch": "⌚",
    "cup": "☕", "bottle": "🍼",
    "please": "🙏", "sorry": "🙇", "excuse me": "🙋", "again": "🔁", "slowly": "🐢",
    "understand": "💡", "question": "❓", "problem": "⚠️", "need": "📌", "want": "✨",
    "know": "🧠", "say": "💬", "tell": "📣", "ask": "❔", "answer": "✅",
    "repeat": "🔁", "look": "👀",
}


def get_word_emoji(word):
    return WORD_EMOJIS.get(word, "🌱")


# =========================
# 오디오 공통 중지 채널
# =========================
AUDIO_CHANNEL_NAME = "survival_english_audio_channel"


# =========================
# 단어용 HTML 오디오 플레이어
# =========================
def html_word_audio_player(label, text, repeat_count=20, pause_ms=1500, height=42):
    audio_bytes = make_tts_audio(text)
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    audio_id = f"audio_{uuid.uuid4().hex}"
    play_btn_id = f"play_btn_{uuid.uuid4().hex}"
    stop_btn_id = f"stop_btn_{uuid.uuid4().hex}"
    status_id = f"status_{uuid.uuid4().hex}"
    player_id = f"player_{uuid.uuid4().hex}"

    safe_label = json.dumps(label)
    safe_text = json.dumps(text)
    safe_player_id = json.dumps(player_id)
    safe_channel = json.dumps(AUDIO_CHANNEL_NAME)

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; gap:6px; height:36px;">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #fce7f3, #dbeafe);
                border: 1px solid #e9d5ff;
                border-radius: 999px;
                padding: 5px 8px;
                font-weight: 800;
                font-size: 12px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.06);
                white-space: nowrap;
            ">
                {label}
            </button>

            <button id="{stop_btn_id}" style="
                background: #fff7ed;
                border: 1px solid #fed7aa;
                border-radius: 999px;
                padding: 5px 8px;
                font-weight: 800;
                font-size: 12px;
                color: #9a3412;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.04);
                white-space: nowrap;
            ">
                ⏹ 중지
            </button>

            <span id="{status_id}" style="
                font-size: 12px;
                color: #075985;
                font-weight: 700;
                white-space: nowrap;
            "></span>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");

            let count = 0;
            let timer = null;
            let isStopped = false;

            const maxCount = {repeat_count};
            const pauseMs = {pause_ms};
            const labelText = {safe_label};
            const wordText = {safe_text};
            const playerId = {safe_player_id};
            const channelName = {safe_channel};

            const channel = new BroadcastChannel(channelName);

            function stopThisAudio(showMessage = false) {{
                isStopped = true;

                if (timer) {{
                    clearTimeout(timer);
                    timer = null;
                }}

                audio.pause();
                audio.currentTime = 0;
                count = 0;

                playBtn.disabled = false;
                playBtn.innerText = labelText;

                if (showMessage) {{
                    status.innerText = "중지됨";
                }} else {{
                    status.innerText = "";
                }}
            }}

            channel.onmessage = function(event) {{
                if (!event.data) return;

                if (event.data.type === "STOP_OTHERS" && event.data.playerId !== playerId) {{
                    stopThisAudio(false);
                }}
            }};

            function playOnce() {{
                if (isStopped) return;

                if (count >= maxCount) {{
                    status.innerText = "완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                    return;
                }}

                audio.currentTime = 0;

                audio.play().then(() => {{
                    count += 1;
                    status.innerText = count + "/" + maxCount;
                }}).catch((error) => {{
                    status.innerText = "다시 클릭";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }});
            }}

            audio.addEventListener("ended", function() {{
                if (isStopped) return;

                if (count < maxCount) {{
                    timer = setTimeout(playOnce, pauseMs);
                }} else {{
                    status.innerText = "완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }}
            }});

            playBtn.addEventListener("click", function() {{
                channel.postMessage({{
                    type: "STOP_OTHERS",
                    playerId: playerId
                }});

                stopThisAudio(false);

                isStopped = false;
                count = 0;
                playBtn.disabled = true;
                playBtn.innerText = "재생중";
                status.innerText = "시작";
                playOnce();
            }});

            stopBtn.addEventListener("click", function() {{
                stopThisAudio(true);
            }});
            </script>
        </div>
        """,
        height=height
    )


def audio_button(label, text, key=None):
    html_word_audio_player(
        label=label,
        text=text,
        repeat_count=20,
        pause_ms=1500,
        height=42
    )


# =========================
# 대화용 HTML 오디오 플레이어
# =========================
def html_dialogue_audio_player(label, dialogue_lines, line_pause_ms=1400, height=105):
    audio_data_list = []

    for line in dialogue_lines:
        clean_text = remove_speaker_label(line["en"])
        audio_bytes = make_tts_audio(clean_text)
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        audio_data_list.append({
            "text": clean_text,
            "src": f"data:audio/mp3;base64,{audio_base64}"
        })

    audio_json = json.dumps(audio_data_list)
    safe_label = json.dumps(label)

    audio_id = f"dialogue_audio_{uuid.uuid4().hex}"
    play_btn_id = f"dialogue_play_{uuid.uuid4().hex}"
    stop_btn_id = f"dialogue_stop_{uuid.uuid4().hex}"
    status_id = f"dialogue_status_{uuid.uuid4().hex}"
    player_id = f"dialogue_player_{uuid.uuid4().hex}"
    safe_player_id = json.dumps(player_id)
    safe_channel = json.dumps(AUDIO_CHANNEL_NAME)

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; gap:6px; height:42px;">
            <audio id="{audio_id}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #fef3c7, #dbeafe);
                border: 1px solid #fde68a;
                border-radius: 999px;
                padding: 9px 15px;
                font-weight: 800;
                font-size: 14px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 3px 8px rgba(0,0,0,0.08);
                margin-right: 6px;
            ">
                {label}
            </button>

            <button id="{stop_btn_id}" style="
                background: #fff7ed;
                border: 1px solid #fed7aa;
                border-radius: 999px;
                padding: 9px 15px;
                font-weight: 800;
                font-size: 14px;
                color: #9a3412;
                cursor: pointer;
                box-shadow: 0 3px 8px rgba(0,0,0,0.05);
            ">
                ⏹ 중지
            </button>

            <div id="{status_id}" style="
                margin-top: 8px;
                font-size: 13px;
                color: #075985;
                font-weight: 700;
            "></div>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");

            const dialogueAudios = {audio_json};
            const linePauseMs = {line_pause_ms};
            const labelText = {safe_label};
            const playerId = {safe_player_id};
            const channelName = {safe_channel};

            let index = 0;
            let timer = null;
            let isStopped = false;

            const channel = new BroadcastChannel(channelName);

            function stopThisAudio(showMessage = false) {{
                isStopped = true;

                if (timer) {{
                    clearTimeout(timer);
                    timer = null;
                }}

                audio.pause();
                audio.currentTime = 0;
                index = 0;

                playBtn.disabled = false;
                playBtn.innerText = labelText;

                if (showMessage) {{
                    status.innerText = "⏹ 대화 듣기를 중지했습니다.";
                }} else {{
                    status.innerText = "";
                }}
            }}

            channel.onmessage = function(event) {{
                if (!event.data) return;

                if (event.data.type === "STOP_OTHERS" && event.data.playerId !== playerId) {{
                    stopThisAudio(false);
                }}
            }};

            function playCurrentLine() {{
                if (isStopped) return;

                if (index >= dialogueAudios.length) {{
                    status.innerText = "✅ 대화 재생 완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                    return;
                }}

                audio.src = dialogueAudios[index].src;
                audio.currentTime = 0;

                audio.play().then(() => {{
                    status.innerText = "🔊 대화 재생 중: " + (index + 1) + " / " + dialogueAudios.length;
                }}).catch((error) => {{
                    status.innerText = "⚠️ 소리 재생이 차단되었습니다. 버튼을 다시 눌러 주세요.";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }});
            }}

            audio.addEventListener("ended", function() {{
                if (isStopped) return;

                index += 1;

                if (index < dialogueAudios.length) {{
                    timer = setTimeout(playCurrentLine, linePauseMs);
                }} else {{
                    status.innerText = "✅ 대화 재생 완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }}
            }});

            playBtn.addEventListener("click", function() {{
                channel.postMessage({{
                    type: "STOP_OTHERS",
                    playerId: playerId
                }});

                stopThisAudio(false);

                isStopped = false;
                index = 0;
                playBtn.disabled = true;
                playBtn.innerText = "재생 중...";
                status.innerText = "🔊 대화 듣기를 시작합니다.";
                playCurrentLine();
            }});

            stopBtn.addEventListener("click", function() {{
                stopThisAudio(true);
            }});
            </script>
        </div>
        """,
        height=height
    )


# =========================
# 오늘의 생존 대화
# =========================
theme_dialogues = {
    "🧍 나와 사람": [
        {"en": "A: Hello. What is your name?", "ko": "A: 안녕. 네 이름은 뭐니?"},
        {"en": "B: My name is Alex.", "ko": "B: 내 이름은 Alex야."},
        {"en": "A: Are you a student?", "ko": "A: 너는 학생이니?"},
        {"en": "B: Yes, I am a student.", "ko": "B: 응, 나는 학생이야."},
        {"en": "A: Is he your friend?", "ko": "A: 그는 네 친구니?"},
        {"en": "B: Yes, he is my friend.", "ko": "B: 응, 그는 내 친구야."},
    ],
    "🏃 기본 동작": [
        {"en": "A: Can you come here?", "ko": "A: 여기로 올 수 있니?"},
        {"en": "B: Yes, I can come.", "ko": "B: 응, 갈 수 있어."},
        {"en": "A: Please sit down.", "ko": "A: 앉아 주세요."},
        {"en": "B: Okay. I will sit down.", "ko": "B: 좋아요. 앉을게요."},
        {"en": "A: Can you help me?", "ko": "A: 나를 도와줄 수 있니?"},
        {"en": "B: Yes, I can help you.", "ko": "B: 응, 도와줄 수 있어."},
    ],
    "💖 감정·몸 상태": [
        {"en": "A: Are you okay?", "ko": "A: 너 괜찮니?"},
        {"en": "B: No, I am tired.", "ko": "B: 아니, 나는 피곤해."},
        {"en": "A: Are you hungry?", "ko": "A: 너 배고프니?"},
        {"en": "B: Yes, I am hungry.", "ko": "B: 응, 나는 배고파."},
        {"en": "A: Are you sick?", "ko": "A: 너 아프니?"},
        {"en": "B: Yes, I am sick.", "ko": "B: 응, 나는 아파."},
    ],
    "🍎 음식·물": [
        {"en": "A: Are you thirsty?", "ko": "A: 너 목마르니?"},
        {"en": "B: Yes, I need water.", "ko": "B: 응, 나는 물이 필요해."},
        {"en": "A: Do you want food?", "ko": "A: 음식이 필요하니?"},
        {"en": "B: Yes, I want food.", "ko": "B: 응, 나는 음식이 필요해."},
        {"en": "A: Do you like apples?", "ko": "A: 너는 사과를 좋아하니?"},
        {"en": "B: Yes, I like apples.", "ko": "B: 응, 나는 사과를 좋아해."},
    ],
    "🚗 장소·이동": [
        {"en": "A: Where is the bathroom?", "ko": "A: 화장실은 어디에 있나요?"},
        {"en": "B: It is near here.", "ko": "B: 여기 근처에 있어요."},
        {"en": "A: I want to go home.", "ko": "A: 나는 집에 가고 싶어요."},
        {"en": "B: You can go by bus.", "ko": "B: 버스로 갈 수 있어요."},
        {"en": "A: Where is the station?", "ko": "A: 역은 어디에 있나요?"},
        {"en": "B: It is not far.", "ko": "B: 멀지 않아요."},
    ],
    "⏰ 시간·숫자": [
        {"en": "A: What time is it?", "ko": "A: 지금 몇 시니?"},
        {"en": "B: It is three.", "ko": "B: 3시야."},
        {"en": "A: Is it morning?", "ko": "A: 아침이니?"},
        {"en": "B: No, it is afternoon.", "ko": "B: 아니, 오후야."},
        {"en": "A: Do you study today?", "ko": "A: 너는 오늘 공부하니?"},
        {"en": "B: Yes, I study today.", "ko": "B: 응, 나는 오늘 공부해."},
    ],
    "🎒 물건·돈": [
        {"en": "A: Where is my phone?", "ko": "A: 내 전화기는 어디에 있니?"},
        {"en": "B: It is in your bag.", "ko": "B: 네 가방 안에 있어."},
        {"en": "A: Do you have money?", "ko": "A: 너 돈 있니?"},
        {"en": "B: No, I do not have money.", "ko": "B: 아니, 돈이 없어."},
        {"en": "A: Is this your book?", "ko": "A: 이것은 네 책이니?"},
        {"en": "B: Yes, it is my book.", "ko": "B: 응, 그것은 내 책이야."},
    ],
    "🆘 도움 요청": [
        {"en": "A: Excuse me.", "ko": "A: 실례합니다."},
        {"en": "B: Yes?", "ko": "B: 네?"},
        {"en": "A: I don't understand.", "ko": "A: 이해하지 못했어요."},
        {"en": "B: Okay. I will say it again.", "ko": "B: 알겠어요. 다시 말할게요."},
        {"en": "A: Please speak slowly.", "ko": "A: 천천히 말해 주세요."},
        {"en": "B: Sure. I can help you.", "ko": "B: 물론이죠. 도와줄 수 있어요."},
    ],
}


# =========================
# 전체 카세트 듣기 기능
# 브라우저 음성 엔진 사용
# =========================
def get_example_sentence(word):
    return CASSETTE_EXAMPLES.get(word, f"This is {word}.")


def get_example_sentence_ko(word):
    return CASSETTE_EXAMPLES_KO.get(word, "이 단어를 사용한 생존 영어 문장입니다.")


def flatten_survival_words():
    all_items = []
    number = 1

    for theme_name, theme_words in word_themes.items():
        for item in theme_words:
            word = item["word"]
            example = get_example_sentence(word)
            example_ko = get_example_sentence_ko(word)

            all_items.append({
                "number": number,
                "theme": theme_name,
                "word": word,
                "meaning": item["meaning"],
                "example": example,
                "example_ko": example_ko,
                "script": f"{word}. {word}. {example} {word}."
            })
            number += 1

    return all_items


def make_theme_cassette_items(theme_words, theme_name):
    theme_items = []

    for idx, item in enumerate(theme_words, start=1):
        word = item["word"]
        example = get_example_sentence(word)
        example_ko = get_example_sentence_ko(word)

        theme_items.append({
            "number": idx,
            "theme": theme_name,
            "word": word,
            "meaning": item["meaning"],
            "example": example,
            "example_ko": example_ko,
            "script": f"{word}. {word}. {example} {word}."
        })

    return theme_items



def browser_survival_cassette_player(all_items, height=700):
    """
    모바일 수정판 카세트 플레이어.
    - 폰 화면에서 버튼 줄 깨짐 방지
    - 재생 버튼 클릭 시 모바일 브라우저에서 바로 speechSynthesis 실행
    - 전체 단어/테마 단어를 3회 반복 재생
    """
    player_id = f"survival_mobile_cassette_{uuid.uuid4().hex}"
    play_btn_id = f"survival_mobile_play_{uuid.uuid4().hex}"
    pause_btn_id = f"survival_mobile_pause_{uuid.uuid4().hex}"
    stop_btn_id = f"survival_mobile_stop_{uuid.uuid4().hex}"
    prev_btn_id = f"survival_mobile_prev_{uuid.uuid4().hex}"
    next_btn_id = f"survival_mobile_next_{uuid.uuid4().hex}"
    prev10_btn_id = f"survival_mobile_prev10_{uuid.uuid4().hex}"
    next10_btn_id = f"survival_mobile_next10_{uuid.uuid4().hex}"
    slow_btn_id = f"survival_mobile_slow_{uuid.uuid4().hex}"
    mid_slow_btn_id = f"survival_mobile_midslow_{uuid.uuid4().hex}"
    normal_btn_id = f"survival_mobile_normal_{uuid.uuid4().hex}"
    mid_fast_btn_id = f"survival_mobile_midfast_{uuid.uuid4().hex}"
    fast_btn_id = f"survival_mobile_fast_{uuid.uuid4().hex}"
    speed_status_id = f"survival_mobile_speed_{uuid.uuid4().hex}"
    progress_id = f"survival_mobile_progress_{uuid.uuid4().hex}"
    visual_bar_id = f"survival_mobile_bar_{uuid.uuid4().hex}"
    percent_id = f"survival_mobile_percent_{uuid.uuid4().hex}"
    status_id = f"survival_mobile_status_{uuid.uuid4().hex}"
    word_id = f"survival_mobile_word_{uuid.uuid4().hex}"
    meaning_id = f"survival_mobile_meaning_{uuid.uuid4().hex}"

    cassette_json = json.dumps(all_items, ensure_ascii=False)
    emoji_json = json.dumps(WORD_EMOJIS, ensure_ascii=False)
    title_text = "Survival English 160 전체 카세트"
    max_index = max(len(all_items) - 1, 0)
    total_len = len(all_items)

    html_code = '\n        <div id="__PLAYER_ID__" class="cassette-wrap">\n            <style>\n                #__PLAYER_ID__ {\n                    box-sizing: border-box;\n                    width: 100%;\n                    max-width: 100%;\n                    overflow: hidden;\n                    font-family: Arial, sans-serif;\n                    padding: 16px;\n                    border-radius: 22px;\n                    background: linear-gradient(135deg, #eff6ff, #fff7ed, #fdf2f8);\n                    border: 1px solid #bfdbfe;\n                    box-shadow: 0 4px 14px rgba(0,0,0,0.08);\n                }\n                #__PLAYER_ID__ * { box-sizing: border-box; }\n                #__PLAYER_ID__ .cassette-title {\n                    font-size: 19px; font-weight: 900; color: #0f172a;\n                    margin-bottom: 10px; line-height: 1.35;\n                }\n                #__PLAYER_ID__ .cassette-word {\n                    font-size: 32px; font-weight: 900; color: #111827;\n                    margin-bottom: 8px; line-height: 1.15;\n                    word-break: keep-all; overflow-wrap: anywhere;\n                }\n                #__PLAYER_ID__ .cassette-meaning {\n                    font-size: 15px; font-weight: 800; color: #475569;\n                    margin-bottom: 12px; line-height: 1.6;\n                    background: rgba(255,255,255,0.78);\n                    border: 1px solid #dbeafe; border-radius: 18px; padding: 12px;\n                    word-break: keep-all; overflow-wrap: anywhere;\n                }\n                #__PLAYER_ID__ .progress-card {\n                    margin: 12px 0; background: rgba(255,255,255,0.86);\n                    border: 1px solid #bfdbfe; border-radius: 18px; padding: 12px;\n                }\n                #__PLAYER_ID__ .progress-top {\n                    display: flex; justify-content: space-between; align-items: center;\n                    gap: 8px; margin-bottom: 8px;\n                }\n                #__PLAYER_ID__ .progress-label { font-size: 14px; font-weight: 900; color: #075985; }\n                #__PLAYER_ID__ .percent-pill {\n                    font-size: 13px; font-weight: 900; color: #7c3aed;\n                    background: #f3e8ff; border-radius: 999px; padding: 5px 10px; flex-shrink: 0;\n                }\n                #__PLAYER_ID__ .visual-track {\n                    width: 100%; height: 11px; background: #e2e8f0;\n                    border-radius: 999px; overflow: hidden; margin-bottom: 8px;\n                }\n                #__PLAYER_ID__ .visual-bar {\n                    height: 100%; width: 0%;\n                    background: linear-gradient(90deg, #38bdf8, #8b5cf6, #ec4899);\n                    border-radius: 999px;\n                }\n                #__PLAYER_ID__ input[type=range] {\n                    width: 100%; min-width: 0; height: 36px; cursor: pointer; accent-color: #8b5cf6;\n                }\n                #__PLAYER_ID__ .range-caption {\n                    display: flex; justify-content: space-between;\n                    font-size: 12px; color: #64748b; font-weight: 800;\n                }\n                #__PLAYER_ID__ .button-grid {\n                    display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));\n                    gap: 8px; width: 100%; margin-top: 10px;\n                }\n                #__PLAYER_ID__ .speed-grid {\n                    display: grid; grid-template-columns: repeat(6, minmax(0, 1fr));\n                    gap: 8px; width: 100%; margin-top: 10px; align-items: center;\n                }\n                #__PLAYER_ID__ button {\n                    width: 100%; min-height: 42px; border-radius: 999px; padding: 8px 8px;\n                    font-weight: 900; font-size: 13px; cursor: pointer;\n                    touch-action: manipulation; -webkit-tap-highlight-color: transparent;\n                    border: 1px solid #cbd5e1; color: #334155; background: #f8fafc;\n                    white-space: nowrap;\n                }\n                #__PLAYER_ID__ button:active { transform: scale(0.98); }\n                #__PLAYER_ID__ .btn-play {\n                    background: linear-gradient(135deg, #dbeafe, #fce7f3);\n                    border-color: #bfdbfe; color: #1f2937; box-shadow: 0 3px 8px rgba(0,0,0,0.08);\n                }\n                #__PLAYER_ID__ .btn-pause { background: #ecfeff; border-color: #67e8f9; color: #155e75; }\n                #__PLAYER_ID__ .btn-stop { background: #fff7ed; border-color: #fed7aa; color: #9a3412; }\n                #__PLAYER_ID__ .btn-prev10 { background: #fef3c7; border-color: #fde68a; color: #92400e; }\n                #__PLAYER_ID__ .btn-next10 { background: #dcfce7; border-color: #bbf7d0; color: #166534; }\n                #__PLAYER_ID__ .speed-label {\n                    grid-column: span 2; font-size: 13px; font-weight: 900; color: #475569;\n                    background: #f8fafc; border-radius: 999px; padding: 9px 10px;\n                    text-align: center; border: 1px dashed #c4b5fd;\n                }\n                #__PLAYER_ID__ .speed-status {\n                    grid-column: span 2; font-size: 13px; color: #7c3aed; font-weight: 900;\n                    background: #f3e8ff; border-radius: 999px; padding: 9px 10px; text-align: center;\n                }\n                #__PLAYER_ID__ .status-line {\n                    margin-top: 10px; min-height: 22px; font-size: 13px;\n                    color: #075985; font-weight: 900; line-height: 1.5; word-break: keep-all;\n                }\n                @media (max-width: 600px) {\n                    #__PLAYER_ID__ { padding: 12px; border-radius: 18px; }\n                    #__PLAYER_ID__ .cassette-title { font-size: 17px; }\n                    #__PLAYER_ID__ .cassette-word { font-size: 26px; }\n                    #__PLAYER_ID__ .cassette-meaning { font-size: 13.5px; padding: 10px; }\n                    #__PLAYER_ID__ .button-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 7px; }\n                    #__PLAYER_ID__ .speed-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 7px; }\n                    #__PLAYER_ID__ .speed-label, #__PLAYER_ID__ .speed-status { grid-column: span 3; }\n                    #__PLAYER_ID__ button { min-height: 42px; font-size: 12.5px; padding: 8px 6px; }\n                }\n            </style>\n\n            <div class="cassette-title">📼 __TITLE_TEXT__</div>\n            <div id="__WORD_ID__" class="cassette-word">Ready</div>\n            <div id="__MEANING_ID__" class="cassette-meaning">재생 버튼을 누르면 단어와 예문이 차례대로 재생됩니다.</div>\n\n            <div class="progress-card">\n                <div class="progress-top">\n                    <div class="progress-label">🎚️ 이동</div>\n                    <div id="__PERCENT_ID__" class="percent-pill">0%</div>\n                </div>\n                <div class="visual-track"><div id="__VISUAL_BAR_ID__" class="visual-bar"></div></div>\n                <input id="__PROGRESS_ID__" type="range" min="0" max="__MAX_INDEX__" value="0" step="1">\n                <div class="range-caption"><span>1번</span><span>__TOTAL_LEN__번</span></div>\n            </div>\n\n            <div class="button-grid">\n                <button type="button" id="__PREV10_BTN_ID__" class="btn-prev10">⏪ 10개 전</button>\n                <button type="button" id="__PREV_BTN_ID__">⏮ 이전</button>\n                <button type="button" id="__PLAY_BTN_ID__" class="btn-play">▶️ 재생</button>\n                <button type="button" id="__PAUSE_BTN_ID__" class="btn-pause">⏸ 일시정지</button>\n                <button type="button" id="__NEXT_BTN_ID__">⏭ 다음</button>\n                <button type="button" id="__NEXT10_BTN_ID__" class="btn-next10">⏩ 10개 후</button>\n                <button type="button" id="__STOP_BTN_ID__" class="btn-stop">⏹ 중지</button>\n            </div>\n\n            <div class="speed-grid">\n                <div class="speed-label">🎚️ 속도 조절</div>\n                <button type="button" id="__SLOW_BTN_ID__">0.5x</button>\n                <button type="button" id="__MID_SLOW_BTN_ID__">0.75x</button>\n                <button type="button" id="__NORMAL_BTN_ID__">1.0x</button>\n                <button type="button" id="__MID_FAST_BTN_ID__">1.25x</button>\n                <button type="button" id="__FAST_BTN_ID__">1.5x</button>\n                <div id="__SPEED_STATUS_ID__" class="speed-status">현재: 1.0x</div>\n            </div>\n\n            <div id="__STATUS_ID__" class="status-line"></div>\n\n            <script>\n            (function() {\n                const cassetteItems = __CASSETTE_JSON__;\n                const emojiMap = __EMOJI_JSON__;\n                const playBtn = document.getElementById("__PLAY_BTN_ID__");\n                const pauseBtn = document.getElementById("__PAUSE_BTN_ID__");\n                const stopBtn = document.getElementById("__STOP_BTN_ID__");\n                const prevBtn = document.getElementById("__PREV_BTN_ID__");\n                const nextBtn = document.getElementById("__NEXT_BTN_ID__");\n                const prev10Btn = document.getElementById("__PREV10_BTN_ID__");\n                const next10Btn = document.getElementById("__NEXT10_BTN_ID__");\n                const slowBtn = document.getElementById("__SLOW_BTN_ID__");\n                const midSlowBtn = document.getElementById("__MID_SLOW_BTN_ID__");\n                const normalBtn = document.getElementById("__NORMAL_BTN_ID__");\n                const midFastBtn = document.getElementById("__MID_FAST_BTN_ID__");\n                const fastBtn = document.getElementById("__FAST_BTN_ID__");\n                const speedStatus = document.getElementById("__SPEED_STATUS_ID__");\n                const progress = document.getElementById("__PROGRESS_ID__");\n                const visualBar = document.getElementById("__VISUAL_BAR_ID__");\n                const percentBox = document.getElementById("__PERCENT_ID__");\n                const status = document.getElementById("__STATUS_ID__");\n                const wordBox = document.getElementById("__WORD_ID__");\n                const meaningBox = document.getElementById("__MEANING_ID__");\n\n                let index = 0, isPlaying = false, isPaused = false, playToken = 0, repeatRound = 1;\n                const maxRepeatRound = 3;\n                let speechRate = 0.75, nextTimer = null, safetyTimer = null, cachedVoice = null;\n\n                function escapeHtml(text) {\n                    const div = document.createElement("div");\n                    div.innerText = String(text ?? "");\n                    return div.innerHTML;\n                }\n                function safeCancel() { try { window.speechSynthesis.cancel(); } catch(e) {} }\n                function clearTimers() {\n                    if (nextTimer) { clearTimeout(nextTimer); nextTimer = null; }\n                    if (safetyTimer) { clearTimeout(safetyTimer); safetyTimer = null; }\n                }\n                function getEmoji(word) { return emojiMap[word] || "🌱"; }\n                function updateProgressVisual() {\n                    const max = Math.max(cassetteItems.length - 1, 1);\n                    const pct = Math.round((index / max) * 100);\n                    visualBar.style.width = pct + "%";\n                    percentBox.innerText = pct + "%";\n                }\n                function updateDisplay() {\n                    const item = cassetteItems[index];\n                    if (!item) return;\n                    progress.value = index;\n                    updateProgressVisual();\n                    wordBox.innerText = item.number + ". " + item.word + " " + getEmoji(item.word);\n                    meaningBox.innerHTML =\n                        "<div style=\'font-size:15px; color:#374151; font-weight:900;\'>단어 뜻: " + escapeHtml(item.meaning) + "</div>" +\n                        "<div style=\'font-size:15px; color:#0369a1; font-weight:900; margin-top:4px;\'>예문: " + escapeHtml(item.example) + "</div>" +\n                        "<div style=\'font-size:15px; color:#166534; font-weight:900; margin-top:4px;\'>예문 뜻: " + escapeHtml(item.example_ko) + "</div>" +\n                        "<div style=\'font-size:12px; color:#94a3b8; font-weight:800; margin-top:6px;\'>" + escapeHtml(item.theme || "") + "</div>";\n                    status.innerText = "전체 반복 " + repeatRound + "/" + maxRepeatRound + " · " + (index + 1) + " / " + cassetteItems.length;\n                }\n                function getEnglishVoice() {\n                    if (cachedVoice) return cachedVoice;\n                    let voices = [];\n                    try { voices = window.speechSynthesis.getVoices() || []; } catch(e) { voices = []; }\n                    cachedVoice = voices.find(v => /en-US/i.test(v.lang || "")) || voices.find(v => /^en/i.test(v.lang || "")) || null;\n                    return cachedVoice;\n                }\n                function makeUtterance(text) {\n                    const u = new SpeechSynthesisUtterance(text);\n                    u.lang = "en-US"; u.rate = speechRate; u.pitch = 1; u.volume = 1;\n                    const voice = getEnglishVoice();\n                    if (voice) u.voice = voice;\n                    return u;\n                }\n                function scheduleNext(tokenAtPlay) {\n                    if (!isPlaying || isPaused || tokenAtPlay !== playToken) return;\n                    index += 1;\n                    if (index >= cassetteItems.length) {\n                        if (repeatRound < maxRepeatRound) { repeatRound += 1; index = 0; }\n                        else {\n                            isPlaying = false; isPaused = false; playBtn.innerText = "▶️ 재생";\n                            status.innerText = "✅ 전체 3회 반복 재생 완료";\n                            safeCancel(); return;\n                        }\n                    }\n                    updateDisplay();\n                    nextTimer = setTimeout(function() { speakCurrent(tokenAtPlay); }, 650);\n                }\n                function speakCurrent(tokenAtPlay) {\n                    if (!isPlaying || isPaused || tokenAtPlay !== playToken) return;\n                    const item = cassetteItems[index];\n                    if (!item) return;\n                    clearTimers(); updateDisplay(); safeCancel();\n                    const script = item.script || (item.word + ". " + item.word + ". " + item.example + " " + item.word + ".");\n                    const utter = makeUtterance(script);\n                    let ended = false;\n                    utter.onend = function() { ended = true; scheduleNext(tokenAtPlay); };\n                    utter.onerror = function() {\n                        if (tokenAtPlay !== playToken) return;\n                        status.innerText = "⚠️ 재생이 막혔습니다. 재생 버튼을 한 번 더 눌러 주세요.";\n                        isPlaying = false; isPaused = false; playBtn.innerText = "▶️ 다시 재생";\n                    };\n                    try { window.speechSynthesis.speak(utter); }\n                    catch(e) {\n                        status.innerText = "⚠️ 이 브라우저에서는 음성 재생이 제한되었습니다.";\n                        isPlaying = false; isPaused = false; playBtn.innerText = "▶️ 재생"; return;\n                    }\n                    safetyTimer = setTimeout(function() {\n                        if (!ended && isPlaying && !isPaused && tokenAtPlay === playToken) {\n                            safeCancel(); scheduleNext(tokenAtPlay);\n                        }\n                    }, 9000);\n                }\n                function startFromCurrent() {\n                    if (!("speechSynthesis" in window)) {\n                        status.innerText = "⚠️ 이 브라우저는 음성 재생을 지원하지 않습니다."; return;\n                    }\n                    playToken += 1;\n                    const tokenAtPlay = playToken;\n                    clearTimers(); safeCancel();\n                    isPlaying = true; isPaused = false; playBtn.innerText = "재생 중...";\n                    updateDisplay();\n                    speakCurrent(tokenAtPlay);\n                }\n                function stopAll(message) {\n                    playToken += 1; clearTimers(); safeCancel();\n                    isPlaying = false; isPaused = false; repeatRound = 1; playBtn.innerText = "▶️ 재생";\n                    updateDisplay(); if (message) status.innerText = message;\n                }\n                function jumpTo(newIndex, autoPlay) {\n                    index = Math.max(0, Math.min(cassetteItems.length - 1, newIndex));\n                    repeatRound = 1; updateDisplay();\n                    if (autoPlay) startFromCurrent();\n                }\n                playBtn.addEventListener("click", function(e) {\n                    e.preventDefault();\n                    if (isPaused) {\n                        try {\n                            window.speechSynthesis.resume(); isPaused = false; isPlaying = true;\n                            playBtn.innerText = "재생 중...";\n                            status.innerText = "이어 듣기: " + (index + 1) + " / " + cassetteItems.length;\n                        } catch(err) { startFromCurrent(); }\n                        return;\n                    }\n                    startFromCurrent();\n                });\n                pauseBtn.addEventListener("click", function(e) {\n                    e.preventDefault();\n                    if (isPlaying && window.speechSynthesis.speaking) {\n                        try { window.speechSynthesis.pause(); } catch(err) {}\n                        isPaused = true; playBtn.innerText = "▶️ 이어 듣기";\n                        status.innerText = "일시정지: " + (index + 1) + " / " + cassetteItems.length;\n                    }\n                });\n                stopBtn.addEventListener("click", function(e) { e.preventDefault(); stopAll("⏹ 중지됨"); });\n                prevBtn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index - 1, isPlaying); });\n                nextBtn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index + 1, isPlaying); });\n                prev10Btn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index - 10, isPlaying); });\n                next10Btn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index + 10, isPlaying); });\n                function setSpeed(rate, label, bg, color) {\n                    speechRate = rate; speedStatus.innerText = "현재: " + label;\n                    speedStatus.style.background = bg; speedStatus.style.color = color;\n                    if (isPlaying && !isPaused) startFromCurrent();\n                }\n                slowBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.375, "0.5x", "#fef3c7", "#92400e"); });\n                midSlowBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.5625, "0.75x", "#fffbeb", "#92400e"); });\n                normalBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.75, "1.0x", "#f3e8ff", "#7c3aed"); });\n                midFastBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.9375, "1.25x", "#ecfdf5", "#166534"); });\n                fastBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(1.125, "1.5x", "#dcfce7", "#166534"); });\n                progress.addEventListener("input", function() { index = parseInt(progress.value || "0"); updateDisplay(); });\n                progress.addEventListener("change", function() { jumpTo(parseInt(progress.value || "0"), isPlaying); });\n                if (typeof speechSynthesis !== "undefined") {\n                    speechSynthesis.onvoiceschanged = function() { cachedVoice = null; getEnglishVoice(); };\n                    getEnglishVoice();\n                }\n                updateDisplay();\n            })();\n            </script>\n        </div>\n'
    replacements = {
        "__PLAYER_ID__": player_id,
        "__PLAY_BTN_ID__": play_btn_id,
        "__PAUSE_BTN_ID__": pause_btn_id,
        "__STOP_BTN_ID__": stop_btn_id,
        "__PREV_BTN_ID__": prev_btn_id,
        "__NEXT_BTN_ID__": next_btn_id,
        "__PREV10_BTN_ID__": prev10_btn_id,
        "__NEXT10_BTN_ID__": next10_btn_id,
        "__SLOW_BTN_ID__": slow_btn_id,
        "__MID_SLOW_BTN_ID__": mid_slow_btn_id,
        "__NORMAL_BTN_ID__": normal_btn_id,
        "__MID_FAST_BTN_ID__": mid_fast_btn_id,
        "__FAST_BTN_ID__": fast_btn_id,
        "__SPEED_STATUS_ID__": speed_status_id,
        "__PROGRESS_ID__": progress_id,
        "__VISUAL_BAR_ID__": visual_bar_id,
        "__PERCENT_ID__": percent_id,
        "__STATUS_ID__": status_id,
        "__WORD_ID__": word_id,
        "__MEANING_ID__": meaning_id,
        "__CASSETTE_JSON__": cassette_json,
        "__EMOJI_JSON__": emoji_json,
        "__TITLE_TEXT__": html.escape(title_text),
        "__MAX_INDEX__": str(max_index),
        "__TOTAL_LEN__": str(total_len),
    }
    for old, new in replacements.items():
        html_code = html_code.replace(old, new)

    components.html(html_code, height=height)



def browser_theme_cassette_player(theme_items, theme_name, height=700):
    """
    모바일 수정판 카세트 플레이어.
    - 폰 화면에서 버튼 줄 깨짐 방지
    - 재생 버튼 클릭 시 모바일 브라우저에서 바로 speechSynthesis 실행
    - 전체 단어/테마 단어를 3회 반복 재생
    """
    player_id = f"theme_mobile_cassette_{uuid.uuid4().hex}"
    play_btn_id = f"theme_mobile_play_{uuid.uuid4().hex}"
    pause_btn_id = f"theme_mobile_pause_{uuid.uuid4().hex}"
    stop_btn_id = f"theme_mobile_stop_{uuid.uuid4().hex}"
    prev_btn_id = f"theme_mobile_prev_{uuid.uuid4().hex}"
    next_btn_id = f"theme_mobile_next_{uuid.uuid4().hex}"
    prev10_btn_id = f"theme_mobile_prev10_{uuid.uuid4().hex}"
    next10_btn_id = f"theme_mobile_next10_{uuid.uuid4().hex}"
    slow_btn_id = f"theme_mobile_slow_{uuid.uuid4().hex}"
    mid_slow_btn_id = f"theme_mobile_midslow_{uuid.uuid4().hex}"
    normal_btn_id = f"theme_mobile_normal_{uuid.uuid4().hex}"
    mid_fast_btn_id = f"theme_mobile_midfast_{uuid.uuid4().hex}"
    fast_btn_id = f"theme_mobile_fast_{uuid.uuid4().hex}"
    speed_status_id = f"theme_mobile_speed_{uuid.uuid4().hex}"
    progress_id = f"theme_mobile_progress_{uuid.uuid4().hex}"
    visual_bar_id = f"theme_mobile_bar_{uuid.uuid4().hex}"
    percent_id = f"theme_mobile_percent_{uuid.uuid4().hex}"
    status_id = f"theme_mobile_status_{uuid.uuid4().hex}"
    word_id = f"theme_mobile_word_{uuid.uuid4().hex}"
    meaning_id = f"theme_mobile_meaning_{uuid.uuid4().hex}"

    cassette_json = json.dumps(theme_items, ensure_ascii=False)
    emoji_json = json.dumps(WORD_EMOJIS, ensure_ascii=False)
    title_text = f"{theme_name} 카세트 듣기"
    max_index = max(len(theme_items) - 1, 0)
    total_len = len(theme_items)

    html_code = '\n        <div id="__PLAYER_ID__" class="cassette-wrap">\n            <style>\n                #__PLAYER_ID__ {\n                    box-sizing: border-box;\n                    width: 100%;\n                    max-width: 100%;\n                    overflow: hidden;\n                    font-family: Arial, sans-serif;\n                    padding: 16px;\n                    border-radius: 22px;\n                    background: linear-gradient(135deg, #eff6ff, #fff7ed, #fdf2f8);\n                    border: 1px solid #bfdbfe;\n                    box-shadow: 0 4px 14px rgba(0,0,0,0.08);\n                }\n                #__PLAYER_ID__ * { box-sizing: border-box; }\n                #__PLAYER_ID__ .cassette-title {\n                    font-size: 19px; font-weight: 900; color: #0f172a;\n                    margin-bottom: 10px; line-height: 1.35;\n                }\n                #__PLAYER_ID__ .cassette-word {\n                    font-size: 32px; font-weight: 900; color: #111827;\n                    margin-bottom: 8px; line-height: 1.15;\n                    word-break: keep-all; overflow-wrap: anywhere;\n                }\n                #__PLAYER_ID__ .cassette-meaning {\n                    font-size: 15px; font-weight: 800; color: #475569;\n                    margin-bottom: 12px; line-height: 1.6;\n                    background: rgba(255,255,255,0.78);\n                    border: 1px solid #dbeafe; border-radius: 18px; padding: 12px;\n                    word-break: keep-all; overflow-wrap: anywhere;\n                }\n                #__PLAYER_ID__ .progress-card {\n                    margin: 12px 0; background: rgba(255,255,255,0.86);\n                    border: 1px solid #bfdbfe; border-radius: 18px; padding: 12px;\n                }\n                #__PLAYER_ID__ .progress-top {\n                    display: flex; justify-content: space-between; align-items: center;\n                    gap: 8px; margin-bottom: 8px;\n                }\n                #__PLAYER_ID__ .progress-label { font-size: 14px; font-weight: 900; color: #075985; }\n                #__PLAYER_ID__ .percent-pill {\n                    font-size: 13px; font-weight: 900; color: #7c3aed;\n                    background: #f3e8ff; border-radius: 999px; padding: 5px 10px; flex-shrink: 0;\n                }\n                #__PLAYER_ID__ .visual-track {\n                    width: 100%; height: 11px; background: #e2e8f0;\n                    border-radius: 999px; overflow: hidden; margin-bottom: 8px;\n                }\n                #__PLAYER_ID__ .visual-bar {\n                    height: 100%; width: 0%;\n                    background: linear-gradient(90deg, #38bdf8, #8b5cf6, #ec4899);\n                    border-radius: 999px;\n                }\n                #__PLAYER_ID__ input[type=range] {\n                    width: 100%; min-width: 0; height: 36px; cursor: pointer; accent-color: #8b5cf6;\n                }\n                #__PLAYER_ID__ .range-caption {\n                    display: flex; justify-content: space-between;\n                    font-size: 12px; color: #64748b; font-weight: 800;\n                }\n                #__PLAYER_ID__ .button-grid {\n                    display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));\n                    gap: 8px; width: 100%; margin-top: 10px;\n                }\n                #__PLAYER_ID__ .speed-grid {\n                    display: grid; grid-template-columns: repeat(6, minmax(0, 1fr));\n                    gap: 8px; width: 100%; margin-top: 10px; align-items: center;\n                }\n                #__PLAYER_ID__ button {\n                    width: 100%; min-height: 42px; border-radius: 999px; padding: 8px 8px;\n                    font-weight: 900; font-size: 13px; cursor: pointer;\n                    touch-action: manipulation; -webkit-tap-highlight-color: transparent;\n                    border: 1px solid #cbd5e1; color: #334155; background: #f8fafc;\n                    white-space: nowrap;\n                }\n                #__PLAYER_ID__ button:active { transform: scale(0.98); }\n                #__PLAYER_ID__ .btn-play {\n                    background: linear-gradient(135deg, #dbeafe, #fce7f3);\n                    border-color: #bfdbfe; color: #1f2937; box-shadow: 0 3px 8px rgba(0,0,0,0.08);\n                }\n                #__PLAYER_ID__ .btn-pause { background: #ecfeff; border-color: #67e8f9; color: #155e75; }\n                #__PLAYER_ID__ .btn-stop { background: #fff7ed; border-color: #fed7aa; color: #9a3412; }\n                #__PLAYER_ID__ .btn-prev10 { background: #fef3c7; border-color: #fde68a; color: #92400e; }\n                #__PLAYER_ID__ .btn-next10 { background: #dcfce7; border-color: #bbf7d0; color: #166534; }\n                #__PLAYER_ID__ .speed-label {\n                    grid-column: span 2; font-size: 13px; font-weight: 900; color: #475569;\n                    background: #f8fafc; border-radius: 999px; padding: 9px 10px;\n                    text-align: center; border: 1px dashed #c4b5fd;\n                }\n                #__PLAYER_ID__ .speed-status {\n                    grid-column: span 2; font-size: 13px; color: #7c3aed; font-weight: 900;\n                    background: #f3e8ff; border-radius: 999px; padding: 9px 10px; text-align: center;\n                }\n                #__PLAYER_ID__ .status-line {\n                    margin-top: 10px; min-height: 22px; font-size: 13px;\n                    color: #075985; font-weight: 900; line-height: 1.5; word-break: keep-all;\n                }\n                @media (max-width: 600px) {\n                    #__PLAYER_ID__ { padding: 12px; border-radius: 18px; }\n                    #__PLAYER_ID__ .cassette-title { font-size: 17px; }\n                    #__PLAYER_ID__ .cassette-word { font-size: 26px; }\n                    #__PLAYER_ID__ .cassette-meaning { font-size: 13.5px; padding: 10px; }\n                    #__PLAYER_ID__ .button-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 7px; }\n                    #__PLAYER_ID__ .speed-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 7px; }\n                    #__PLAYER_ID__ .speed-label, #__PLAYER_ID__ .speed-status { grid-column: span 3; }\n                    #__PLAYER_ID__ button { min-height: 42px; font-size: 12.5px; padding: 8px 6px; }\n                }\n            </style>\n\n            <div class="cassette-title">📼 __TITLE_TEXT__</div>\n            <div id="__WORD_ID__" class="cassette-word">Ready</div>\n            <div id="__MEANING_ID__" class="cassette-meaning">재생 버튼을 누르면 단어와 예문이 차례대로 재생됩니다.</div>\n\n            <div class="progress-card">\n                <div class="progress-top">\n                    <div class="progress-label">🎚️ 이동</div>\n                    <div id="__PERCENT_ID__" class="percent-pill">0%</div>\n                </div>\n                <div class="visual-track"><div id="__VISUAL_BAR_ID__" class="visual-bar"></div></div>\n                <input id="__PROGRESS_ID__" type="range" min="0" max="__MAX_INDEX__" value="0" step="1">\n                <div class="range-caption"><span>1번</span><span>__TOTAL_LEN__번</span></div>\n            </div>\n\n            <div class="button-grid">\n                <button type="button" id="__PREV10_BTN_ID__" class="btn-prev10">⏪ 10개 전</button>\n                <button type="button" id="__PREV_BTN_ID__">⏮ 이전</button>\n                <button type="button" id="__PLAY_BTN_ID__" class="btn-play">▶️ 재생</button>\n                <button type="button" id="__PAUSE_BTN_ID__" class="btn-pause">⏸ 일시정지</button>\n                <button type="button" id="__NEXT_BTN_ID__">⏭ 다음</button>\n                <button type="button" id="__NEXT10_BTN_ID__" class="btn-next10">⏩ 10개 후</button>\n                <button type="button" id="__STOP_BTN_ID__" class="btn-stop">⏹ 중지</button>\n            </div>\n\n            <div class="speed-grid">\n                <div class="speed-label">🎚️ 속도 조절</div>\n                <button type="button" id="__SLOW_BTN_ID__">0.5x</button>\n                <button type="button" id="__MID_SLOW_BTN_ID__">0.75x</button>\n                <button type="button" id="__NORMAL_BTN_ID__">1.0x</button>\n                <button type="button" id="__MID_FAST_BTN_ID__">1.25x</button>\n                <button type="button" id="__FAST_BTN_ID__">1.5x</button>\n                <div id="__SPEED_STATUS_ID__" class="speed-status">현재: 1.0x</div>\n            </div>\n\n            <div id="__STATUS_ID__" class="status-line"></div>\n\n            <script>\n            (function() {\n                const cassetteItems = __CASSETTE_JSON__;\n                const emojiMap = __EMOJI_JSON__;\n                const playBtn = document.getElementById("__PLAY_BTN_ID__");\n                const pauseBtn = document.getElementById("__PAUSE_BTN_ID__");\n                const stopBtn = document.getElementById("__STOP_BTN_ID__");\n                const prevBtn = document.getElementById("__PREV_BTN_ID__");\n                const nextBtn = document.getElementById("__NEXT_BTN_ID__");\n                const prev10Btn = document.getElementById("__PREV10_BTN_ID__");\n                const next10Btn = document.getElementById("__NEXT10_BTN_ID__");\n                const slowBtn = document.getElementById("__SLOW_BTN_ID__");\n                const midSlowBtn = document.getElementById("__MID_SLOW_BTN_ID__");\n                const normalBtn = document.getElementById("__NORMAL_BTN_ID__");\n                const midFastBtn = document.getElementById("__MID_FAST_BTN_ID__");\n                const fastBtn = document.getElementById("__FAST_BTN_ID__");\n                const speedStatus = document.getElementById("__SPEED_STATUS_ID__");\n                const progress = document.getElementById("__PROGRESS_ID__");\n                const visualBar = document.getElementById("__VISUAL_BAR_ID__");\n                const percentBox = document.getElementById("__PERCENT_ID__");\n                const status = document.getElementById("__STATUS_ID__");\n                const wordBox = document.getElementById("__WORD_ID__");\n                const meaningBox = document.getElementById("__MEANING_ID__");\n\n                let index = 0, isPlaying = false, isPaused = false, playToken = 0, repeatRound = 1;\n                const maxRepeatRound = 3;\n                let speechRate = 0.75, nextTimer = null, safetyTimer = null, cachedVoice = null;\n\n                function escapeHtml(text) {\n                    const div = document.createElement("div");\n                    div.innerText = String(text ?? "");\n                    return div.innerHTML;\n                }\n                function safeCancel() { try { window.speechSynthesis.cancel(); } catch(e) {} }\n                function clearTimers() {\n                    if (nextTimer) { clearTimeout(nextTimer); nextTimer = null; }\n                    if (safetyTimer) { clearTimeout(safetyTimer); safetyTimer = null; }\n                }\n                function getEmoji(word) { return emojiMap[word] || "🌱"; }\n                function updateProgressVisual() {\n                    const max = Math.max(cassetteItems.length - 1, 1);\n                    const pct = Math.round((index / max) * 100);\n                    visualBar.style.width = pct + "%";\n                    percentBox.innerText = pct + "%";\n                }\n                function updateDisplay() {\n                    const item = cassetteItems[index];\n                    if (!item) return;\n                    progress.value = index;\n                    updateProgressVisual();\n                    wordBox.innerText = item.number + ". " + item.word + " " + getEmoji(item.word);\n                    meaningBox.innerHTML =\n                        "<div style=\'font-size:15px; color:#374151; font-weight:900;\'>단어 뜻: " + escapeHtml(item.meaning) + "</div>" +\n                        "<div style=\'font-size:15px; color:#0369a1; font-weight:900; margin-top:4px;\'>예문: " + escapeHtml(item.example) + "</div>" +\n                        "<div style=\'font-size:15px; color:#166534; font-weight:900; margin-top:4px;\'>예문 뜻: " + escapeHtml(item.example_ko) + "</div>" +\n                        "<div style=\'font-size:12px; color:#94a3b8; font-weight:800; margin-top:6px;\'>" + escapeHtml(item.theme || "") + "</div>";\n                    status.innerText = "전체 반복 " + repeatRound + "/" + maxRepeatRound + " · " + (index + 1) + " / " + cassetteItems.length;\n                }\n                function getEnglishVoice() {\n                    if (cachedVoice) return cachedVoice;\n                    let voices = [];\n                    try { voices = window.speechSynthesis.getVoices() || []; } catch(e) { voices = []; }\n                    cachedVoice = voices.find(v => /en-US/i.test(v.lang || "")) || voices.find(v => /^en/i.test(v.lang || "")) || null;\n                    return cachedVoice;\n                }\n                function makeUtterance(text) {\n                    const u = new SpeechSynthesisUtterance(text);\n                    u.lang = "en-US"; u.rate = speechRate; u.pitch = 1; u.volume = 1;\n                    const voice = getEnglishVoice();\n                    if (voice) u.voice = voice;\n                    return u;\n                }\n                function scheduleNext(tokenAtPlay) {\n                    if (!isPlaying || isPaused || tokenAtPlay !== playToken) return;\n                    index += 1;\n                    if (index >= cassetteItems.length) {\n                        if (repeatRound < maxRepeatRound) { repeatRound += 1; index = 0; }\n                        else {\n                            isPlaying = false; isPaused = false; playBtn.innerText = "▶️ 재생";\n                            status.innerText = "✅ 전체 3회 반복 재생 완료";\n                            safeCancel(); return;\n                        }\n                    }\n                    updateDisplay();\n                    nextTimer = setTimeout(function() { speakCurrent(tokenAtPlay); }, 650);\n                }\n                function speakCurrent(tokenAtPlay) {\n                    if (!isPlaying || isPaused || tokenAtPlay !== playToken) return;\n                    const item = cassetteItems[index];\n                    if (!item) return;\n                    clearTimers(); updateDisplay(); safeCancel();\n                    const script = item.script || (item.word + ". " + item.word + ". " + item.example + " " + item.word + ".");\n                    const utter = makeUtterance(script);\n                    let ended = false;\n                    utter.onend = function() { ended = true; scheduleNext(tokenAtPlay); };\n                    utter.onerror = function() {\n                        if (tokenAtPlay !== playToken) return;\n                        status.innerText = "⚠️ 재생이 막혔습니다. 재생 버튼을 한 번 더 눌러 주세요.";\n                        isPlaying = false; isPaused = false; playBtn.innerText = "▶️ 다시 재생";\n                    };\n                    try { window.speechSynthesis.speak(utter); }\n                    catch(e) {\n                        status.innerText = "⚠️ 이 브라우저에서는 음성 재생이 제한되었습니다.";\n                        isPlaying = false; isPaused = false; playBtn.innerText = "▶️ 재생"; return;\n                    }\n                    safetyTimer = setTimeout(function() {\n                        if (!ended && isPlaying && !isPaused && tokenAtPlay === playToken) {\n                            safeCancel(); scheduleNext(tokenAtPlay);\n                        }\n                    }, 9000);\n                }\n                function startFromCurrent() {\n                    if (!("speechSynthesis" in window)) {\n                        status.innerText = "⚠️ 이 브라우저는 음성 재생을 지원하지 않습니다."; return;\n                    }\n                    playToken += 1;\n                    const tokenAtPlay = playToken;\n                    clearTimers(); safeCancel();\n                    isPlaying = true; isPaused = false; playBtn.innerText = "재생 중...";\n                    updateDisplay();\n                    speakCurrent(tokenAtPlay);\n                }\n                function stopAll(message) {\n                    playToken += 1; clearTimers(); safeCancel();\n                    isPlaying = false; isPaused = false; repeatRound = 1; playBtn.innerText = "▶️ 재생";\n                    updateDisplay(); if (message) status.innerText = message;\n                }\n                function jumpTo(newIndex, autoPlay) {\n                    index = Math.max(0, Math.min(cassetteItems.length - 1, newIndex));\n                    repeatRound = 1; updateDisplay();\n                    if (autoPlay) startFromCurrent();\n                }\n                playBtn.addEventListener("click", function(e) {\n                    e.preventDefault();\n                    if (isPaused) {\n                        try {\n                            window.speechSynthesis.resume(); isPaused = false; isPlaying = true;\n                            playBtn.innerText = "재생 중...";\n                            status.innerText = "이어 듣기: " + (index + 1) + " / " + cassetteItems.length;\n                        } catch(err) { startFromCurrent(); }\n                        return;\n                    }\n                    startFromCurrent();\n                });\n                pauseBtn.addEventListener("click", function(e) {\n                    e.preventDefault();\n                    if (isPlaying && window.speechSynthesis.speaking) {\n                        try { window.speechSynthesis.pause(); } catch(err) {}\n                        isPaused = true; playBtn.innerText = "▶️ 이어 듣기";\n                        status.innerText = "일시정지: " + (index + 1) + " / " + cassetteItems.length;\n                    }\n                });\n                stopBtn.addEventListener("click", function(e) { e.preventDefault(); stopAll("⏹ 중지됨"); });\n                prevBtn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index - 1, isPlaying); });\n                nextBtn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index + 1, isPlaying); });\n                prev10Btn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index - 10, isPlaying); });\n                next10Btn.addEventListener("click", function(e) { e.preventDefault(); jumpTo(index + 10, isPlaying); });\n                function setSpeed(rate, label, bg, color) {\n                    speechRate = rate; speedStatus.innerText = "현재: " + label;\n                    speedStatus.style.background = bg; speedStatus.style.color = color;\n                    if (isPlaying && !isPaused) startFromCurrent();\n                }\n                slowBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.375, "0.5x", "#fef3c7", "#92400e"); });\n                midSlowBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.5625, "0.75x", "#fffbeb", "#92400e"); });\n                normalBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.75, "1.0x", "#f3e8ff", "#7c3aed"); });\n                midFastBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(0.9375, "1.25x", "#ecfdf5", "#166534"); });\n                fastBtn.addEventListener("click", function(e) { e.preventDefault(); setSpeed(1.125, "1.5x", "#dcfce7", "#166534"); });\n                progress.addEventListener("input", function() { index = parseInt(progress.value || "0"); updateDisplay(); });\n                progress.addEventListener("change", function() { jumpTo(parseInt(progress.value || "0"), isPlaying); });\n                if (typeof speechSynthesis !== "undefined") {\n                    speechSynthesis.onvoiceschanged = function() { cachedVoice = null; getEnglishVoice(); };\n                    getEnglishVoice();\n                }\n                updateDisplay();\n            })();\n            </script>\n        </div>\n'
    replacements = {
        "__PLAYER_ID__": player_id,
        "__PLAY_BTN_ID__": play_btn_id,
        "__PAUSE_BTN_ID__": pause_btn_id,
        "__STOP_BTN_ID__": stop_btn_id,
        "__PREV_BTN_ID__": prev_btn_id,
        "__NEXT_BTN_ID__": next_btn_id,
        "__PREV10_BTN_ID__": prev10_btn_id,
        "__NEXT10_BTN_ID__": next10_btn_id,
        "__SLOW_BTN_ID__": slow_btn_id,
        "__MID_SLOW_BTN_ID__": mid_slow_btn_id,
        "__NORMAL_BTN_ID__": normal_btn_id,
        "__MID_FAST_BTN_ID__": mid_fast_btn_id,
        "__FAST_BTN_ID__": fast_btn_id,
        "__SPEED_STATUS_ID__": speed_status_id,
        "__PROGRESS_ID__": progress_id,
        "__VISUAL_BAR_ID__": visual_bar_id,
        "__PERCENT_ID__": percent_id,
        "__STATUS_ID__": status_id,
        "__WORD_ID__": word_id,
        "__MEANING_ID__": meaning_id,
        "__CASSETTE_JSON__": cassette_json,
        "__EMOJI_JSON__": emoji_json,
        "__TITLE_TEXT__": html.escape(title_text),
        "__MAX_INDEX__": str(max_index),
        "__TOTAL_LEN__": str(total_len),
    }
    for old, new in replacements.items():
        html_code = html_code.replace(old, new)

    components.html(html_code, height=height)


def show_all_cassette_tab():
    st.markdown("## 🎧 전체 카세트 듣기")

    all_items = flatten_survival_words()
    browser_survival_cassette_player(all_items, height=700)

    with st.expander("📜 전체 카세트 단어 목록 보기"):
        st.write("카세트에서 실제로 들려주는 단어, 예문, 예문 뜻을 함께 확인할 수 있습니다.")

        for item in all_items:
            st.markdown(
                f"""
                <div style="
                    background:white;
                    border:1px solid #dbeafe;
                    border-radius:16px;
                    padding:12px 14px;
                    margin-bottom:8px;
                    box-shadow:0 2px 8px rgba(0,0,0,0.035);
                ">
                    <div style="font-size:18px; font-weight:900; color:#111827;">
                        {item['number']}. {item['word']}
                    </div>
                    <div style="font-size:15px; font-weight:800; color:#374151; margin-top:4px;">
                        단어 뜻: {item['meaning']}
                    </div>
                    <div style="font-size:15px; font-weight:800; color:#0369a1; margin-top:4px;">
                        예문: {item['example']}
                    </div>
                    <div style="font-size:15px; font-weight:800; color:#166534; margin-top:4px;">
                        예문 뜻: {item['example_ko']}
                    </div>
                    <div style="font-size:12px; color:#94a3b8; margin-top:4px;">
                        {item['theme']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


def show_cassette_player(theme_words, theme_name):
    st.markdown("### 🎧 이 테마 카세트 듣기")

    theme_items = make_theme_cassette_items(theme_words, theme_name)

    browser_theme_cassette_player(
        theme_items,
        theme_name,
        height=700
    )


# =========================
# 전체 뜻 목록 만들기
# =========================
all_words = []
for theme_words in word_themes.values():
    all_words.extend(theme_words)

all_meanings = [item["meaning"] for item in all_words]


# =========================
# 보기 고정 랜덤 섞기
# =========================
def get_shuffled_options(theme_name, index, options):
    key = f"{theme_name}_options_{index}"

    if key not in st.session_state:
        shuffled = options[:]
        random.seed(f"{theme_name}_{index}")
        random.shuffle(shuffled)
        st.session_state[key] = shuffled

    return st.session_state[key]


# =========================
# 퀴즈 문항 만들기
# =========================
def make_quiz_items(theme_words, theme_name):
    quiz_items = []

    for idx, item in enumerate(theme_words):
        correct = item["meaning"]
        distractors = [m for m in all_meanings if m != correct]
        random.seed(f"{theme_name}_{item['word']}_{idx}")
        wrong_options = random.sample(distractors, 3)

        options = [correct] + wrong_options

        quiz_items.append({
            "word": item["word"],
            "answer": correct,
            "options": options
        })

    return quiz_items


# =========================
# 상태 초기화
# =========================
def init_state(theme_name):
    if f"{theme_name}_submitted1" not in st.session_state:
        st.session_state[f"{theme_name}_submitted1"] = False

    if f"{theme_name}_submitted2" not in st.session_state:
        st.session_state[f"{theme_name}_submitted2"] = False

    if f"{theme_name}_wrong" not in st.session_state:
        st.session_state[f"{theme_name}_wrong"] = []


def reset_theme(theme_name):
    keys_to_delete = []

    for key in st.session_state.keys():
        if key.startswith(theme_name):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del st.session_state[key]


# =========================
# 오늘의 생존 대화 보여주기
# =========================
def show_dialogue(theme_name):
    dialogue = theme_dialogues.get(theme_name, [])

    if not dialogue:
        return

    st.markdown('<div class="dialogue-box">', unsafe_allow_html=True)
    st.markdown('<div class="dialogue-title">💬 오늘의 생존 대화</div>', unsafe_allow_html=True)

    for line in dialogue:
        st.markdown(
            f"<div class='dialogue-line'>{line['en']}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='dialogue-meaning'>{line['ko']}</div>",
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    html_dialogue_audio_player(
        label="🔊 대화 듣기",
        dialogue_lines=dialogue,
        line_pause_ms=1400,
        height=105
    )



# =========================
# 단어 익히기
# =========================
def show_word_cards(theme_words, theme_name):
    st.markdown("### 🌱 핵심 단어 익히기")
    st.write("생존 회화에 꼭 필요한 단어를 듣고 익혀 보세요.")

    for idx, item in enumerate(theme_words):
        st.markdown('<div class="word-card">', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns([1.25, 1.05, 0.35, 1.65])

        with col1:
            st.markdown(
                f"""
                <div class="word-row">
                    <div class="word-number">{idx + 1}</div>
                    <div class="word-text">{item['word']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div class='meaning-text'>{item['meaning']}</div>",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"<div class='emoji-text'>{get_word_emoji(item['word'])}</div>",
                unsafe_allow_html=True
            )

        with col4:
            audio_button(
                "🔊 듣기",
                item["word"],
                key=f"{theme_name}_learn_audio_{idx}"
            )

        st.markdown('</div>', unsafe_allow_html=True)


# =========================
# 퀴즈 풀기
# =========================
def show_quiz(theme_words, theme_name):
    init_state(theme_name)

    quiz_items = make_quiz_items(theme_words, theme_name)

    submitted1_key = f"{theme_name}_submitted1"
    submitted2_key = f"{theme_name}_submitted2"
    wrong_key = f"{theme_name}_wrong"

    if not st.session_state[submitted1_key]:
        st.markdown("### 🧸 1차 퀴즈")
        st.write("영어 단어를 보고 알맞은 뜻을 고르세요.")

        for i, q in enumerate(quiz_items):
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

            st.markdown(f"<div class='quiz-number'>🌟 Question {i + 1}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='quiz-word'>{q['word']}</div>", unsafe_allow_html=True)

            audio_button(
                "🔊 발음 듣기",
                q["word"],
                key=f"{theme_name}_quiz_audio1_{i}"
            )

            options = get_shuffled_options(theme_name, i, q["options"])

            st.radio(
                "뜻을 고르세요.",
                options,
                key=f"{theme_name}_q1_{i}"
            )

            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("✅ 1차 제출하기", key=f"{theme_name}_submit1"):
            wrong = []

            for i, q in enumerate(quiz_items):
                user_answer = st.session_state.get(f"{theme_name}_q1_{i}")

                if user_answer != q["answer"]:
                    wrong.append(i)

            st.session_state[wrong_key] = wrong
            st.session_state[submitted1_key] = True
            st.rerun()

    elif st.session_state[submitted1_key] and not st.session_state[submitted2_key]:
        wrong = st.session_state[wrong_key]
        score = len(quiz_items) - len(wrong)

        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-title">🎉 1차 결과: {score} / {len(quiz_items)}점</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if len(wrong) == 0:
            st.balloons()
            st.success("🌈 완벽합니다! 이 테마의 생존 단어를 모두 잘 기억하고 있습니다.")

            if st.button("🔄 다시 풀기", key=f"{theme_name}_reset_all_correct"):
                reset_theme(theme_name)
                st.rerun()

        else:
            st.markdown(
                f"""
                <div class="wrong-box">
                    🍊 틀린 단어 {len(wrong)}개를 다시 풀어 봅시다.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 🔁 2차 퀴즈: 틀린 단어만 다시 풀기")

            for i in wrong:
                q = quiz_items[i]

                st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

                st.markdown(f"<div class='quiz-number'>🌟 Retry {i + 1}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='quiz-word'>{q['word']}</div>", unsafe_allow_html=True)

                audio_button(
                    "🔊 발음 다시 듣기",
                    q["word"],
                    key=f"{theme_name}_quiz_audio2_{i}"
                )

                options = get_shuffled_options(theme_name, i, q["options"])

                st.radio(
                    "뜻을 다시 고르세요.",
                    options,
                    key=f"{theme_name}_q2_{i}"
                )

                st.markdown('</div>', unsafe_allow_html=True)

            if st.button("✅ 2차 제출하기", key=f"{theme_name}_submit2"):
                st.session_state[submitted2_key] = True
                st.rerun()

    else:
        wrong = st.session_state[wrong_key]
        second_wrong = []

        for i in wrong:
            q = quiz_items[i]
            user_answer = st.session_state.get(f"{theme_name}_q2_{i}")

            if user_answer != q["answer"]:
                second_wrong.append(i)

        final_score = len(quiz_items) - len(second_wrong)

        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-title">🏆 최종 결과: {final_score} / {len(quiz_items)}점</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if len(second_wrong) == 0:
            st.balloons()
            st.success("💖 좋습니다! 틀렸던 단어까지 모두 다시 확인했습니다.")
        else:
            st.warning("🍊 아래 단어들은 다시 복습하면 좋습니다.")

        st.markdown("### ✅ 정답 확인")

        if len(wrong) == 0:
            st.info("틀린 문제가 없습니다.")
        else:
            for i in wrong:
                q = quiz_items[i]
                user1 = st.session_state.get(f"{theme_name}_q1_{i}")
                user2 = st.session_state.get(f"{theme_name}_q2_{i}")

                st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                st.markdown(f"### 🌱 {q['word']}")

                audio_button(
                    "🔊 발음 다시 듣기",
                    q["word"],
                    key=f"{theme_name}_answer_audio_{i}"
                )

                st.write(f"1차 선택: {user1}")
                st.write(f"2차 선택: {user2}")
                st.success(f"정답: {q['answer']}")
                st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🔄 다시 풀기", key=f"{theme_name}_reset"):
            reset_theme(theme_name)
            st.rerun()


# =========================
# 탭 구성
# =========================
tab_names = ["🎧 전체 카세트 듣기"] + list(word_themes.keys())
tabs = st.tabs(tab_names)

with tabs[0]:
    show_all_cassette_tab()

for tab, theme_name in zip(tabs[1:], word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]

        st.markdown(
            f"""
            <div class="theme-header">
                <div class="theme-title">{theme_name}</div>
                <div class="theme-desc">이 테마에는 {len(theme_words)}개의 생존 단어가 있습니다. 먼저 대화를 듣고, 핵심 단어를 익혀 봅시다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        show_dialogue(theme_name)

        show_cassette_player(theme_words, theme_name)

        mode = st.radio(
            "학습 모드를 선택하세요.",
            ["🌱 핵심 단어 익히기", "🧸 퀴즈 풀기"],
            key=f"{theme_name}_mode",
            horizontal=True
        )

        if mode == "🌱 핵심 단어 익히기":
            show_word_cards(theme_words, theme_name)
        else:
            show_quiz(theme_words, theme_name)
