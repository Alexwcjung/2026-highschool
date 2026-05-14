import streamlit as st
from urllib.parse import quote
import requests
import hashlib
import random
import re

# =====================================================
# Survival English 160 - 안정형 버전
# 핵심 수정:
# 1) Streamlit 컴포넌트 방식 삭제
# 2) 브라우저 스크립트 방식 삭제
# 3) gTTS 서버 생성 방식 삭제
# 4) Google TTS URL + requests + Streamlit 기본 st.audio() 사용
# 5) 카세트는 여러 조각 mp3를 하나로 이어 붙여 한 번에 재생
# 6) 단어 카드는 추가 버튼 없이 오디오 플레이어를 바로 표시
# =====================================================

st.set_page_config(
    page_title="Survival English 160",
    page_icon="🛟",
    layout="wide"
)

# =====================================================
# CSS 디자인
# =====================================================
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
    .theme-header {
        background: linear-gradient(135deg, #0ea5e9 0%, #8b5cf6 50%, #ec4899 100%);
        color: white;
        padding: 28px 30px;
        border-radius: 26px;
        margin-bottom: 22px;
        box-shadow: 0 10px 24px rgba(14,165,233,0.28);
    }
    .theme-title {
        font-size: 38px;
        font-weight: 1000;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
        line-height: 1.15;
    }
    .theme-desc {
        font-size: 18px;
        font-weight: 800;
        opacity: 0.98;
        line-height: 1.55;
    }
    .cassette-box {
        background: linear-gradient(135deg, #eff6ff 0%, #fff7ed 48%, #fdf2f8 100%);
        border: 1px solid #bae6fd;
        border-radius: 26px;
        padding: 20px 22px;
        margin-bottom: 24px;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
    }
    .cassette-title {
        font-size: 24px;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 8px;
    }
    .cassette-note {
        font-size: 14px;
        font-weight: 800;
        color: #475569;
        margin-bottom: 12px;
        line-height: 1.6;
    }
    .dialogue-box {
        background: #fefce8;
        border: 1px solid #fde68a;
        border-radius: 24px;
        padding: 20px 22px;
        margin-bottom: 22px;
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
        padding: 12px 14px;
        margin-bottom: 10px;
        border: 1px solid #e0f2fe;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }
    .word-number {
        display:inline-block;
        min-width: 34px;
        font-size: 13px;
        font-weight: 900;
        color: #0369a1;
        background: #e0f2fe;
        border-radius: 999px;
        padding: 5px 9px;
        text-align: center;
        margin-right: 8px;
    }
    .word-text {
        font-size: 25px;
        font-weight: 900;
        color: #111827;
    }
    .meaning-text {
        font-size: 18px;
        font-weight: 800;
        color: #374151;
    }
    .emoji-text {
        font-size: 26px;
        text-align: center;
    }
    .quiz-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 22px 24px;
        margin-bottom: 18px;
        border: 1px solid #e9d5ff;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    }
    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 24px;
        padding: 20px 22px;
        margin: 20px 0;
        border: 1px solid #bbf7d0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        font-size: 22px;
        font-weight: 900;
        color: #14532d;
    }
    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        border: 1px solid #d1d5db;
        padding: 0.45rem 1rem;
    }
    div[data-baseweb="tab-list"] {
        gap: 10px;
        flex-wrap: wrap;
    }
    button[data-baseweb="tab"] {
        min-height: 56px;
        padding: 12px 18px;
        border-radius: 18px 18px 0 0;
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        margin-right: 4px;
    }
    button[data-baseweb="tab"] p {
        font-size: 20px !important;
        font-weight: 1000 !important;
        color: #111827 !important;
        line-height: 1.25 !important;
        white-space: nowrap;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #dbeafe, #fce7f3);
        border-bottom: 4px solid #8b5cf6;
    }
    @media (max-width: 600px) {
        .main-title { font-size: 34px; }
        .theme-header { padding: 22px 20px; border-radius: 22px; }
        .theme-title { font-size: 31px; }
        .theme-desc { font-size: 16px; }
        button[data-baseweb="tab"] { min-height: 50px; padding: 9px 12px; }
        button[data-baseweb="tab"] p { font-size: 17px !important; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# TTS 함수 - JavaScript/gTTS 제거 + requests로 mp3 직접 받아오기
# =====================================================
def make_google_tts_url(text, lang="en"):
    clean_text = str(text).strip()
    if not clean_text:
        clean_text = "Hello"

    # Google Translate TTS는 너무 긴 문장을 싫어하므로 호출부에서 짧게 자릅니다.
    encoded = quote(clean_text)
    return f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={lang}&q={encoded}"


@st.cache_data(show_spinner=False)
def get_tts_mp3_bytes(text, lang="en"):
    """
    st.audio(url)이 재생되지 않는 경우가 있어서,
    requests로 mp3 파일을 직접 받아온 뒤 st.audio(bytes)로 재생합니다.
    """
    clean_text = str(text).strip()
    if not clean_text:
        clean_text = "Hello"

    url = make_google_tts_url(clean_text, lang=lang)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://translate.google.com/",
    }

    response = requests.get(url, headers=headers, timeout=12)
    response.raise_for_status()

    audio_bytes = response.content
    if not audio_bytes or len(audio_bytes) < 500:
        raise ValueError("음성 파일이 비어 있습니다.")

    return audio_bytes


def split_tts_chunks(text, max_chars=130):
    """긴 카세트 대본을 TTS가 재생 가능한 짧은 덩어리로 나눕니다."""
    words = str(text).split()
    chunks = []
    current = ""

    for w in words:
        candidate = (current + " " + w).strip()
        if len(candidate) > max_chars and current:
            chunks.append(current)
            current = w
        else:
            current = candidate

    if current:
        chunks.append(current)

    return chunks


@st.cache_data(show_spinner=False)
def get_combined_tts_mp3_bytes(text, lang="en", max_chars=155):
    """
    긴 카세트 대본을 Google TTS가 처리할 수 있는 길이로 나눈 뒤,
    여러 mp3 조각을 하나로 이어 붙여 st.audio() 하나로 재생합니다.
    별도 라이브러리나 ffmpeg가 필요 없습니다.
    """
    chunks = split_tts_chunks(text, max_chars=max_chars)
    combined = b""

    for chunk in chunks:
        combined += get_tts_mp3_bytes(chunk, lang=lang)

    if not combined or len(combined) < 500:
        raise ValueError("통합 음성 파일이 비어 있습니다.")

    return combined


def play_audio_block(text, label="🔊 듣기", show_link=True, key=None):
    """
    대화처럼 긴 오디오는 버튼을 눌렀을 때만 mp3를 받아옵니다.
    단어 카드는 아래 direct_audio_player()를 사용해서 오디오 바를 바로 보여줍니다.
    """
    text = str(text).strip()
    if not text:
        return

    if key is None:
        key = "audio_" + hashlib.md5((label + "::" + text).encode("utf-8")).hexdigest()

    if st.button(label, key=key, use_container_width=True):
        try:
            audio_bytes = get_tts_mp3_bytes(text, lang="en")
            st.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.error("음성 파일을 만들지 못했습니다. requirements.txt에 requests가 있는지 확인해 주세요.")
            st.caption(f"오류 내용: {e}")
            if show_link:
                st.link_button("🔊 새 창에서 듣기", make_google_tts_url(text, lang="en"), use_container_width=True)


def direct_audio_player(text, show_link=True):
    """
    단어 카드용: expander나 추가 버튼 없이 오디오 플레이어를 바로 보여줍니다.
    학생은 오디오 바의 재생 버튼만 한 번 누르면 됩니다.
    """
    text = str(text).strip()
    if not text:
        return

    try:
        audio_bytes = get_tts_mp3_bytes(text, lang="en")
        st.audio(audio_bytes, format="audio/mp3")
    except Exception as e:
        st.error("음성 파일을 만들지 못했습니다.")
        st.caption(f"오류 내용: {e}")
        if show_link:
            st.link_button("🔊 새 창에서 듣기", make_google_tts_url(text, lang="en"), use_container_width=True)


def remove_speaker_label(sentence):
    return re.sub(r"^[A-Z]:\s*", "", sentence).strip()


def make_dialogue_tts_text(dialogue):
    return " ".join([remove_speaker_label(item["en"]) for item in dialogue])


# =====================================================
# 생존 회화 160 테마별 단어
# =====================================================
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
        {"word": "nine", "meaning": "아홉"},
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

# =====================================================
# 단어별 예문
# =====================================================
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
    "nine": "I have nine books.", "ten": "I have ten books.",

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
    "eight": "나는 책 여덟 권이 있습니다.", "nine": "나는 책 아홉 권이 있습니다.", "ten": "나는 책 열 권이 있습니다.",

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

# =====================================================
# 단어별 이모지
# =====================================================
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
    "seven": "7️⃣", "eight": "8️⃣", "nine": "9️⃣", "ten": "🔟",
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


# =====================================================
# 오늘의 생존 대화
# =====================================================
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


# =====================================================
# 카테고리 통합
# =====================================================
CATEGORY_MERGE_MAP = {
    "🧍 나와 사람": "🧍 사람·상태",
    "💖 감정·몸 상태": "🧍 사람·상태",

    "🏃 기본 동작": "🏃 동작·도움",
    "🆘 도움 요청": "🏃 동작·도움",

    "🍎 음식·물": "🍎 음식·건강",

    "🚗 장소·이동": "🚗 장소·이동",

    "⏰ 시간·숫자": "⏰ 시간·숫자",

    "🎒 물건·돈": "🎒 물건·돈",
}


def merge_categories(original_dict):
    merged = {}
    for old_cat, items in original_dict.items():
        new_cat = CATEGORY_MERGE_MAP.get(old_cat, old_cat)
        if new_cat not in merged:
            merged[new_cat] = []
        merged[new_cat].extend(items)
    return merged


word_themes = merge_categories(word_themes)
theme_dialogues = merge_categories(theme_dialogues)


# =====================================================
# 카세트용 데이터
# =====================================================
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
            all_items.append({
                "number": number,
                "theme": theme_name,
                "word": word,
                "meaning": item["meaning"],
                "example": get_example_sentence(word),
                "example_ko": get_example_sentence_ko(word),
            })
            number += 1
    return all_items


def make_theme_cassette_items(theme_words, theme_name):
    theme_items = []
    for idx, item in enumerate(theme_words, start=1):
        word = item["word"]
        theme_items.append({
            "number": idx,
            "theme": theme_name,
            "word": word,
            "meaning": item["meaning"],
            "example": get_example_sentence(word),
            "example_ko": get_example_sentence_ko(word),
        })
    return theme_items


def make_cassette_text(items, repeat_word=2, include_example=False):
    parts = []
    for item in items:
        word = item["word"]
        if repeat_word == 1:
            parts.append(f"{word}.")
        elif repeat_word == 2:
            parts.append(f"{word}. {word}.")
        else:
            parts.append(f"{word}. {word}. {word}.")

        if include_example:
            parts.append(item["example"])
    return " ".join(parts)


def show_cassette_audio(items, title):
    st.markdown(
        f"""
        <div class="cassette-box">
            <div class="cassette-title">{title}</div>
            <div class="cassette-note">
                예문은 빼고 단어만 재생합니다. 버튼을 누르면 전체 단어 카세트를 하나의 오디오로 만들어 재생합니다.
                멈춤은 오디오 바의 일시정지 버튼을 사용하면 됩니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    repeat_word = st.selectbox(
        "단어 반복 횟수",
        [1, 2, 3],
        index=1,
        key=f"repeat_{title}"
    )

    # 예문은 듣기에 넣지 않습니다. 단어만 반복해서 카세트로 만듭니다.
    text = make_cassette_text(items, repeat_word=repeat_word, include_example=False)

    with st.expander("📜 실제 재생 대본 보기"):
        st.write(text)

    if st.button("▶️ 카세트 한 번에 듣기", key=f"one_cassette_{title}", use_container_width=True):
        try:
            with st.spinner("카세트 음성을 만드는 중입니다. 처음 한 번은 조금 걸릴 수 있습니다."):
                audio_bytes = get_combined_tts_mp3_bytes(text, lang="en", max_chars=155)
            st.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.error("카세트 음성을 만들지 못했습니다. requirements.txt에 requests가 있는지 확인해 주세요.")
            st.caption(f"오류 내용: {e}")


def show_cassette_player(theme_words, theme_name):
    st.markdown("### 🎧 이 카테고리 단어 카세트 듣기")
    theme_items = make_theme_cassette_items(theme_words, theme_name)
    show_cassette_audio(theme_items, f"📼 {theme_name} 단어 카세트")


def show_all_cassette_tab():
    st.markdown("## 🎧 전체 단어 카세트 듣기")
    all_items = flatten_survival_words()
    show_cassette_audio(all_items, "📼 전체 단어 카세트 듣기")

    with st.expander("📜 전체 카세트 단어 목록 보기"):
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
                        {item['number']}. {get_word_emoji(item['word'])} {item['word']}
                    </div>
                    <div style="font-size:15px; font-weight:800; color:#374151; margin-top:4px;">
                        뜻: {item['meaning']}
                    </div>
                    <div style="font-size:13px; font-weight:700; color:#64748b; margin-top:4px;">
                        예문: {item['example']}
                    </div>
                    <div style="font-size:12px; color:#94a3b8; margin-top:4px;">
                        {item['theme']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# =====================================================
# 대화
# =====================================================
def show_dialogue(theme_name):
    dialogue = theme_dialogues.get(theme_name, [])
    if not dialogue:
        return

    st.markdown('<div class="dialogue-box">', unsafe_allow_html=True)
    st.markdown('<div class="dialogue-title">💬 오늘의 생존 대화</div>', unsafe_allow_html=True)

    for line in dialogue:
        st.markdown(f"<div class='dialogue-line'>{line['en']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dialogue-meaning'>{line['ko']}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    dialogue_text = make_dialogue_tts_text(dialogue)
    play_audio_block(dialogue_text, label="🔊 대화 전체 듣기", key=f"dialogue_{theme_name}")


# =====================================================
# 단어 카드
# =====================================================
def show_word_cards(theme_words, theme_name):
    show_cassette_player(theme_words, theme_name)

    st.markdown("---")
    st.markdown("### 🌱 핵심 단어 익히기")

    for idx, item in enumerate(theme_words, start=1):
        with st.container():
            st.markdown('<div class="word-card">', unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns([1.5, 1.2, 0.4, 1.8])

            with col1:
                st.markdown(
                    f"<span class='word-number'>{idx}</span><span class='word-text'>{item['word']}</span>",
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(f"<div class='meaning-text'>{item['meaning']}</div>", unsafe_allow_html=True)

            with col3:
                st.markdown(f"<div class='emoji-text'>{get_word_emoji(item['word'])}</div>", unsafe_allow_html=True)

            with col4:
                direct_audio_player(item["word"])

            st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# 퀴즈
# =====================================================
def make_quiz_items(theme_name, theme_words):
    quiz_key = f"quiz_items_{theme_name}"
    if quiz_key not in st.session_state:
        quiz_items = theme_words.copy()
        random.shuffle(quiz_items)
        st.session_state[quiz_key] = quiz_items[:min(10, len(quiz_items))]
    return st.session_state[quiz_key]


def reset_quiz(theme_name):
    quiz_key = f"quiz_items_{theme_name}"
    answer_key = f"answers_{theme_name}"
    if quiz_key in st.session_state:
        del st.session_state[quiz_key]
    if answer_key in st.session_state:
        del st.session_state[answer_key]


def show_quiz(theme_name, theme_words):
    st.markdown("### 📝 단어 뜻 퀴즈")
    st.caption("영어 단어를 보고 알맞은 뜻을 고르세요.")

    if st.button("🔄 퀴즈 새로 만들기", key=f"reset_{theme_name}"):
        reset_quiz(theme_name)
        st.rerun()

    quiz_items = make_quiz_items(theme_name, theme_words)

    all_words = []
    for words in word_themes.values():
        all_words.extend(words)
    all_meanings = list({item["meaning"] for item in all_words})

    answers = {}

    for q_idx, item in enumerate(quiz_items, start=1):
        correct = item["meaning"]
        wrongs = [m for m in all_meanings if m != correct]
        random.seed(f"{theme_name}_{q_idx}_{item['word']}")
        options = random.sample(wrongs, min(3, len(wrongs))) + [correct]
        random.shuffle(options)

        st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
        st.markdown(f"**문제 {q_idx}.** `{item['word']}` 의 뜻은?")
        answers[q_idx] = st.radio(
            "정답 선택",
            options,
            key=f"quiz_{theme_name}_{q_idx}",
            label_visibility="collapsed"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("✅ 채점하기", key=f"submit_{theme_name}"):
        score = 0
        wrong_list = []

        for q_idx, item in enumerate(quiz_items, start=1):
            if answers[q_idx] == item["meaning"]:
                score += 1
            else:
                wrong_list.append((item["word"], item["meaning"], answers[q_idx]))

        st.markdown(
            f"<div class='score-box'>점수: {score} / {len(quiz_items)}</div>",
            unsafe_allow_html=True
        )

        if score == len(quiz_items):
            st.balloons()
            st.success("완벽합니다!")
        else:
            st.warning("틀린 문제를 다시 확인해 봅시다.")
            for word, correct, user_answer in wrong_list:
                st.write(f"- **{word}**: 정답 **{correct}** / 선택 **{user_answer}**")


# =====================================================
# 상단 제목
# =====================================================
st.markdown("<div class='main-title'>🛟 Survival English 160</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>생존 회화에 꼭 필요한 문장과 단어를 듣고, 따라 하고, 퀴즈로 익혀 봅시다.</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="hero-box">
        <div style="font-size:18px; font-weight:900; color:#374151;">
            이 단어 160개만 외우면 미국에서 생존이 가능합니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================================
# 탭 구성
# =====================================================
tab_names = list(word_themes.keys()) + ["🎧 전체 카세트 듣기"]
tabs = st.tabs(tab_names)

for tab, theme_name in zip(tabs[:-1], word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]

        st.markdown(
            f"""
            <div class="theme-header">
                <div class="theme-title">{theme_name}</div>
                <div class="theme-desc">이 카테고리에는 {len(theme_words)}개의 생존 단어가 있습니다. 핵심 단어를 듣고 익혀 봅시다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        mode = st.radio(
            "학습 모드 선택",
            ["🎧 듣기·단어", "💬 대화", "📝 퀴즈"],
            horizontal=True,
            key=f"mode_{theme_name}"
        )

        if mode == "🎧 듣기·단어":
            show_word_cards(theme_words, theme_name)
        elif mode == "💬 대화":
            show_dialogue(theme_name)
        else:
            show_quiz(theme_name, theme_words)

with tabs[-1]:
    show_all_cassette_tab()
