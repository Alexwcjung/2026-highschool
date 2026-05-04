import streamlit as st
from gtts import gTTS
import io
import random
import base64
import uuid
import re
from pathlib import Path
import streamlit.components.v1 as components

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Fun Word Garden",
    page_icon="🌈",
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
        background: linear-gradient(135deg, #fce7f3 0%, #e0f2fe 50%, #fef3c7 100%);
        border-radius: 26px;
        padding: 28px 30px;
        margin-bottom: 28px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
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
        background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 50%, #06b6d4 100%);
        color: white;
        padding: 22px 26px;
        border-radius: 24px;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(139,92,246,0.25);
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

    .word-card {
        background: white;
        border-radius: 22px;
        padding: 18px 20px;
        margin-bottom: 14px;
        border: 1px solid #f3e8ff;
        box-shadow: 0 5px 16px rgba(0,0,0,0.05);
    }

    .word-badge {
        display: inline-block;
        background: #fce7f3;
        color: #be185d;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .word-text {
        font-size: 31px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 4px;
    }

    .meaning-text {
        font-size: 20px;
        font-weight: 700;
        color: #374151;
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

    .small-muted {
        font-size: 14px;
        color: #6b7280;
    }

    div[data-testid="stRadio"] > label {
        font-weight: 800;
        color: #374151;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        border: 1px solid #d1d5db;
        padding: 0.45rem 1rem;
    }

    .stButton > button:hover {
        border-color: #ec4899;
        color: #ec4899;
    }


    .dialogue-box {
        background: #fefce8;
        border: 1px solid #fde68a;
        border-radius: 22px;
        padding: 18px 20px;
        margin-bottom: 20px;
        box-shadow: 0 5px 14px rgba(0,0,0,0.05);
    }

    .dialogue-title {
        font-size: 21px;
        font-weight: 900;
        color: #854d0e;
        margin-bottom: 12px;
    }

    .dialogue-line {
        font-size: 17px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 4px;
    }

    .dialogue-meaning {
        font-size: 15px;
        color: #6b7280;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 상단 제목
# =========================
st.markdown("<div class='main-title'>🌟 Fun Word Garden 🌟</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>귀여운 단어 정원에서 테마별 영어 단어를 듣고, 보고, 퀴즈로 익혀 봅시다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🌱 오늘의 단어 학습 루틴</div>
        <div class="hero-text">
            • 단어를 <b>테마별</b>로 묶어 기억합니다.<br>
            • 먼저 <b>단어 익히기</b>에서 뜻과 발음을 확인합니다.<br>
            • 다음으로 <b>퀴즈 풀기</b>에서 영어 단어를 보고 알맞은 뜻을 고릅니다.<br>
            • 1차 제출 후 틀린 단어만 다시 풀고, 2차 제출 후 정답을 확인합니다.
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
    """
    영어 문장 또는 단어 1번 발음 mp3 만들기
    """
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def safe_filename(text):
    """
    파일 이름에 쓸 수 없는 문자를 정리합니다.
    """
    text = re.sub(r"[^a-zA-Z0-9가-힣_ -]", "", text)
    text = text.strip().replace(" ", "_")
    return text[:60] if text else "audio"


def save_tts_file(text, filename, folder="audio_files"):
    """
    듣기 mp3 파일을 실제 파일로 저장합니다.
    이미 있으면 다시 만들지 않습니다.
    """
    folder_path = Path(folder)
    folder_path.mkdir(exist_ok=True)

    file_path = folder_path / filename

    if not file_path.exists():
        audio_bytes = make_tts_audio(text)
        file_path.write_bytes(audio_bytes)

    return file_path


def audio_button(label, text, key, repeat_count=20, pause_ms=1500):
    """
    HTML 버튼을 누르면 단어를 20번 반복 재생합니다.
    각 발음 사이에는 pause_ms 만큼 쉽니다.
    Streamlit 자동재생 차단 문제를 피하기 위해 components.html 내부 버튼을 사용합니다.
    """
    audio_bytes = make_tts_audio(text)
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    audio_id = f"audio_{uuid.uuid4().hex}"
    btn_id = f"btn_{uuid.uuid4().hex}"
    status_id = f"status_{uuid.uuid4().hex}"

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif;">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <button id="{btn_id}" style="
                background: linear-gradient(135deg, #fce7f3, #dbeafe);
                border: 1px solid #e9d5ff;
                border-radius: 999px;
                padding: 9px 15px;
                font-weight: 800;
                font-size: 14px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 3px 8px rgba(0,0,0,0.08);
            ">
                {label}
            </button>

            <div id="{status_id}" style="
                margin-top: 8px;
                font-size: 13px;
                color: #075985;
                font-weight: 700;
            "></div>

            <script>
            const audio = document.getElementById("{audio_id}");
            const btn = document.getElementById("{btn_id}");
            const status = document.getElementById("{status_id}");

            let count = 0;
            const maxCount = {repeat_count};
            const pauseMs = {pause_ms};

            function playOnce() {{
                if (count >= maxCount) {{
                    status.innerText = "✅ " + maxCount + "번 반복 재생 완료";
                    btn.disabled = false;
                    btn.innerText = "{label}";
                    return;
                }}

                audio.currentTime = 0;

                audio.play().then(() => {{
                    count += 1;
                    status.innerText = "🔊 {text} 재생 중: " + count + " / " + maxCount;
                }}).catch((error) => {{
                    status.innerText = "⚠️ 소리 재생이 차단되었습니다. 버튼을 다시 눌러 주세요.";
                    btn.disabled = false;
                    btn.innerText = "{label}";
                }});
            }}

            audio.addEventListener("ended", function() {{
                setTimeout(playOnce, pauseMs);
            }});

            btn.addEventListener("click", function() {{
                count = 0;
                btn.disabled = true;
                btn.innerText = "재생 중...";
                status.innerText = "🔊 {text} 반복 재생을 시작합니다.";
                playOnce();
            }});
            </script>
        </div>
        """,
        height=82
    )


def simple_audio_player(text, key, label="▶️ 대화 듣기"):
    """
    대화문은 일반 st.audio로 들려줍니다.
    동시에 mp3 파일도 audio_files 폴더에 저장됩니다.
    """
    filename = safe_filename(key) + ".mp3"
    file_path = save_tts_file(text, filename)

    st.audio(str(file_path), format="audio/mp3")
    with open(file_path, "rb") as f:
        st.download_button(
            label=f"⬇️ {label} 파일 다운로드",
            data=f,
            file_name=filename,
            mime="audio/mp3",
            key=f"download_{key}"
        )


# =========================
# 테마별 단어 데이터
# =========================
word_themes = {
    "🧑‍🤝‍🧑 사람·관계": [
        {"word": "person", "meaning": "사람"},
        {"word": "man", "meaning": "남자"},
        {"word": "woman", "meaning": "여자"},
        {"word": "child", "meaning": "아이"},
        {"word": "baby", "meaning": "아기"},
        {"word": "boy", "meaning": "소년"},
        {"word": "girl", "meaning": "소녀"},
        {"word": "friend", "meaning": "친구"},
        {"word": "family", "meaning": "가족"},
        {"word": "parent", "meaning": "부모"},
        {"word": "father", "meaning": "아버지"},
        {"word": "mother", "meaning": "어머니"},
        {"word": "brother", "meaning": "형제, 남자 형제"},
        {"word": "sister", "meaning": "자매, 여자 형제"},
        {"word": "son", "meaning": "아들"},
        {"word": "daughter", "meaning": "딸"},
        {"word": "teacher", "meaning": "선생님"},
        {"word": "student", "meaning": "학생"},
        {"word": "classmate", "meaning": "반 친구"},
        {"word": "neighbor", "meaning": "이웃"},
        {"word": "customer", "meaning": "손님, 고객"},
        {"word": "worker", "meaning": "노동자, 직원"},
        {"word": "driver", "meaning": "운전자"},
        {"word": "doctor", "meaning": "의사"},
        {"word": "nurse", "meaning": "간호사"},
        {"word": "police officer", "meaning": "경찰관"},
        {"word": "owner", "meaning": "주인"},
        {"word": "guest", "meaning": "손님"},
        {"word": "team", "meaning": "팀, 무리"},
        {"word": "member", "meaning": "구성원"},
    ],

    "🏫 학교·교실": [
        {"word": "school", "meaning": "학교"},
        {"word": "class", "meaning": "수업, 학급"},
        {"word": "classroom", "meaning": "교실"},
        {"word": "lesson", "meaning": "수업, 과"},
        {"word": "homework", "meaning": "숙제"},
        {"word": "test", "meaning": "시험"},
        {"word": "exam", "meaning": "시험"},
        {"word": "quiz", "meaning": "퀴즈, 간단한 시험"},
        {"word": "question", "meaning": "질문, 문제"},
        {"word": "answer", "meaning": "대답, 정답"},
        {"word": "book", "meaning": "책"},
        {"word": "notebook", "meaning": "공책"},
        {"word": "paper", "meaning": "종이, 보고서"},
        {"word": "pen", "meaning": "펜"},
        {"word": "pencil", "meaning": "연필"},
        {"word": "desk", "meaning": "책상"},
        {"word": "chair", "meaning": "의자"},
        {"word": "board", "meaning": "칠판, 게시판"},
        {"word": "page", "meaning": "쪽, 페이지"},
        {"word": "word", "meaning": "단어, 말"},
        {"word": "sentence", "meaning": "문장"},
        {"word": "story", "meaning": "이야기"},
        {"word": "language", "meaning": "언어"},
        {"word": "English", "meaning": "영어"},
        {"word": "Korean", "meaning": "한국어"},
        {"word": "grade", "meaning": "성적, 학년"},
        {"word": "score", "meaning": "점수"},
        {"word": "rule", "meaning": "규칙"},
        {"word": "practice", "meaning": "연습하다, 연습"},
        {"word": "study", "meaning": "공부하다"},
    ],

    "🏃 기본 동작 동사": [
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
        {"word": "make", "meaning": "만들다"},
        {"word": "do", "meaning": "하다"},
        {"word": "have", "meaning": "가지다, 먹다"},
        {"word": "get", "meaning": "얻다, 받다, 되다"},
        {"word": "take", "meaning": "가져가다, 타다"},
        {"word": "give", "meaning": "주다"},
        {"word": "put", "meaning": "놓다, 두다"},
        {"word": "bring", "meaning": "가져오다"},
        {"word": "use", "meaning": "사용하다"},
        {"word": "find", "meaning": "찾다"},
        {"word": "keep", "meaning": "유지하다, 보관하다"},
        {"word": "leave", "meaning": "떠나다, 남기다"},
        {"word": "move", "meaning": "움직이다, 이사하다"},
        {"word": "turn", "meaning": "돌다, 돌리다"},
        {"word": "wait", "meaning": "기다리다"},
        {"word": "help", "meaning": "돕다"},
        {"word": "try", "meaning": "시도하다"},
        {"word": "need", "meaning": "필요하다"},
        {"word": "want", "meaning": "원하다"},
        {"word": "like", "meaning": "좋아하다"},
    ],

    "💖 감정·성격": [
        {"word": "happy", "meaning": "행복한"},
        {"word": "sad", "meaning": "슬픈"},
        {"word": "angry", "meaning": "화난"},
        {"word": "tired", "meaning": "피곤한"},
        {"word": "hungry", "meaning": "배고픈"},
        {"word": "thirsty", "meaning": "목마른"},
        {"word": "excited", "meaning": "신난"},
        {"word": "bored", "meaning": "지루한"},
        {"word": "afraid", "meaning": "두려워하는"},
        {"word": "worried", "meaning": "걱정하는"},
        {"word": "proud", "meaning": "자랑스러워하는"},
        {"word": "kind", "meaning": "친절한"},
        {"word": "nice", "meaning": "좋은, 친절한"},
        {"word": "brave", "meaning": "용감한"},
        {"word": "honest", "meaning": "정직한"},
        {"word": "friendly", "meaning": "친근한"},
        {"word": "quiet", "meaning": "조용한"},
        {"word": "shy", "meaning": "수줍은"},
        {"word": "smart", "meaning": "똑똑한"},
        {"word": "strong", "meaning": "강한"},
        {"word": "weak", "meaning": "약한"},
        {"word": "careful", "meaning": "조심하는"},
        {"word": "lazy", "meaning": "게으른"},
        {"word": "busy", "meaning": "바쁜"},
        {"word": "ready", "meaning": "준비된"},
        {"word": "sorry", "meaning": "미안한"},
        {"word": "thankful", "meaning": "감사하는"},
        {"word": "lonely", "meaning": "외로운"},
        {"word": "nervous", "meaning": "긴장한"},
        {"word": "calm", "meaning": "차분한"},
    ],

    "🍎 음식·건강": [
        {"word": "food", "meaning": "음식"},
        {"word": "rice", "meaning": "밥, 쌀"},
        {"word": "bread", "meaning": "빵"},
        {"word": "water", "meaning": "물"},
        {"word": "milk", "meaning": "우유"},
        {"word": "juice", "meaning": "주스"},
        {"word": "coffee", "meaning": "커피"},
        {"word": "tea", "meaning": "차"},
        {"word": "apple", "meaning": "사과"},
        {"word": "banana", "meaning": "바나나"},
        {"word": "egg", "meaning": "달걀"},
        {"word": "meat", "meaning": "고기"},
        {"word": "fish", "meaning": "생선, 물고기"},
        {"word": "chicken", "meaning": "닭고기, 닭"},
        {"word": "vegetable", "meaning": "채소"},
        {"word": "fruit", "meaning": "과일"},
        {"word": "breakfast", "meaning": "아침 식사"},
        {"word": "lunch", "meaning": "점심 식사"},
        {"word": "dinner", "meaning": "저녁 식사"},
        {"word": "snack", "meaning": "간식"},
        {"word": "healthy", "meaning": "건강한"},
        {"word": "sick", "meaning": "아픈"},
        {"word": "pain", "meaning": "통증"},
        {"word": "headache", "meaning": "두통"},
        {"word": "medicine", "meaning": "약"},
        {"word": "hospital", "meaning": "병원"},
        {"word": "exercise", "meaning": "운동하다, 운동"},
        {"word": "sleep", "meaning": "자다, 잠"},
        {"word": "rest", "meaning": "쉬다, 휴식"},
        {"word": "wash", "meaning": "씻다"},
    ],

    "🚗 장소·이동": [
        {"word": "home", "meaning": "집"},
        {"word": "house", "meaning": "집"},
        {"word": "room", "meaning": "방"},
        {"word": "kitchen", "meaning": "부엌"},
        {"word": "bathroom", "meaning": "화장실, 욕실"},
        {"word": "door", "meaning": "문"},
        {"word": "window", "meaning": "창문"},
        {"word": "city", "meaning": "도시"},
        {"word": "town", "meaning": "마을"},
        {"word": "country", "meaning": "나라, 시골"},
        {"word": "street", "meaning": "거리"},
        {"word": "road", "meaning": "도로"},
        {"word": "park", "meaning": "공원"},
        {"word": "store", "meaning": "가게"},
        {"word": "market", "meaning": "시장"},
        {"word": "station", "meaning": "역"},
        {"word": "bus", "meaning": "버스"},
        {"word": "car", "meaning": "자동차"},
        {"word": "bike", "meaning": "자전거"},
        {"word": "train", "meaning": "기차"},
        {"word": "plane", "meaning": "비행기"},
        {"word": "ship", "meaning": "배"},
        {"word": "map", "meaning": "지도"},
        {"word": "place", "meaning": "장소"},
        {"word": "here", "meaning": "여기"},
        {"word": "there", "meaning": "거기"},
        {"word": "left", "meaning": "왼쪽"},
        {"word": "right", "meaning": "오른쪽, 맞는"},
        {"word": "near", "meaning": "가까운"},
        {"word": "far", "meaning": "먼"},
    ],
        "🌤️ 자연·날씨": [
        {"word": "sun", "meaning": "태양"},
        {"word": "moon", "meaning": "달"},
        {"word": "star", "meaning": "별"},
        {"word": "sky", "meaning": "하늘"},
        {"word": "cloud", "meaning": "구름"},
        {"word": "rain", "meaning": "비"},
        {"word": "snow", "meaning": "눈"},
        {"word": "wind", "meaning": "바람"},
        {"word": "weather", "meaning": "날씨"},
        {"word": "air", "meaning": "공기"},
        {"word": "water", "meaning": "물"},
        {"word": "fire", "meaning": "불"},
        {"word": "tree", "meaning": "나무"},
        {"word": "flower", "meaning": "꽃"},
        {"word": "grass", "meaning": "풀, 잔디"},
        {"word": "mountain", "meaning": "산"},
        {"word": "river", "meaning": "강"},
        {"word": "sea", "meaning": "바다"},
        {"word": "beach", "meaning": "해변"},
        {"word": "forest", "meaning": "숲"},
        {"word": "earth", "meaning": "지구, 땅"},
        {"word": "ground", "meaning": "땅, 지면"},
        {"word": "rock", "meaning": "바위"},
        {"word": "hill", "meaning": "언덕"},
        {"word": "lake", "meaning": "호수"},
        {"word": "island", "meaning": "섬"},
        {"word": "cold", "meaning": "추운, 차가운"},
        {"word": "hot", "meaning": "뜨거운, 더운"},
        {"word": "warm", "meaning": "따뜻한"},
        {"word": "cool", "meaning": "시원한, 멋진"},
    ],

    "🐶 동물 이름": [
        {"word": "dog", "meaning": "개"},
        {"word": "cat", "meaning": "고양이"},
        {"word": "bird", "meaning": "새"},
        {"word": "fish", "meaning": "물고기"},
        {"word": "horse", "meaning": "말"},
        {"word": "cow", "meaning": "소"},
        {"word": "pig", "meaning": "돼지"},
        {"word": "sheep", "meaning": "양"},
        {"word": "goat", "meaning": "염소"},
        {"word": "chicken", "meaning": "닭"},
        {"word": "duck", "meaning": "오리"},
        {"word": "rabbit", "meaning": "토끼"},
        {"word": "mouse", "meaning": "쥐"},
        {"word": "monkey", "meaning": "원숭이"},
        {"word": "lion", "meaning": "사자"},
        {"word": "tiger", "meaning": "호랑이"},
        {"word": "bear", "meaning": "곰"},
        {"word": "wolf", "meaning": "늑대"},
        {"word": "fox", "meaning": "여우"},
        {"word": "deer", "meaning": "사슴"},
        {"word": "elephant", "meaning": "코끼리"},
        {"word": "giraffe", "meaning": "기린"},
        {"word": "zebra", "meaning": "얼룩말"},
        {"word": "snake", "meaning": "뱀"},
        {"word": "frog", "meaning": "개구리"},
        {"word": "turtle", "meaning": "거북이"},
        {"word": "whale", "meaning": "고래"},
        {"word": "dolphin", "meaning": "돌고래"},
        {"word": "shark", "meaning": "상어"},
        {"word": "penguin", "meaning": "펭귄"},
    ],

    "⏰ 시간·숫자": [
        {"word": "time", "meaning": "시간"},
        {"word": "day", "meaning": "날, 하루"},
        {"word": "week", "meaning": "주"},
        {"word": "month", "meaning": "달, 월"},
        {"word": "year", "meaning": "해, 년"},
        {"word": "today", "meaning": "오늘"},
        {"word": "tomorrow", "meaning": "내일"},
        {"word": "yesterday", "meaning": "어제"},
        {"word": "morning", "meaning": "아침"},
        {"word": "afternoon", "meaning": "오후"},
        {"word": "evening", "meaning": "저녁"},
        {"word": "night", "meaning": "밤"},
        {"word": "hour", "meaning": "시간"},
        {"word": "minute", "meaning": "분"},
        {"word": "second", "meaning": "초"},
        {"word": "early", "meaning": "이른"},
        {"word": "late", "meaning": "늦은"},
        {"word": "now", "meaning": "지금"},
        {"word": "before", "meaning": "~전에"},
        {"word": "after", "meaning": "~후에"},
        {"word": "first", "meaning": "첫 번째"},
        {"word": "last", "meaning": "마지막의, 지난"},
        {"word": "one", "meaning": "하나"},
        {"word": "two", "meaning": "둘"},
        {"word": "three", "meaning": "셋"},
        {"word": "four", "meaning": "넷"},
        {"word": "five", "meaning": "다섯"},
        {"word": "many", "meaning": "많은"},
        {"word": "much", "meaning": "많은"},
        {"word": "few", "meaning": "거의 없는, 몇몇의"},
    ],

    "🧸 물건·도구": [
        {"word": "thing", "meaning": "것, 물건"},
        {"word": "bag", "meaning": "가방"},
        {"word": "box", "meaning": "상자"},
        {"word": "cup", "meaning": "컵"},
        {"word": "bottle", "meaning": "병"},
        {"word": "phone", "meaning": "전화기"},
        {"word": "computer", "meaning": "컴퓨터"},
        {"word": "camera", "meaning": "카메라"},
        {"word": "key", "meaning": "열쇠"},
        {"word": "money", "meaning": "돈"},
        {"word": "card", "meaning": "카드"},
        {"word": "ticket", "meaning": "표, 티켓"},
        {"word": "clothes", "meaning": "옷"},
        {"word": "shirt", "meaning": "셔츠"},
        {"word": "pants", "meaning": "바지"},
        {"word": "shoes", "meaning": "신발"},
        {"word": "hat", "meaning": "모자"},
        {"word": "watch", "meaning": "시계"},
        {"word": "table", "meaning": "탁자"},
        {"word": "bed", "meaning": "침대"},
        {"word": "light", "meaning": "빛, 전등"},
        {"word": "picture", "meaning": "그림, 사진"},
        {"word": "music", "meaning": "음악"},
        {"word": "game", "meaning": "게임, 경기"},
        {"word": "ball", "meaning": "공"},
        {"word": "tool", "meaning": "도구"},
        {"word": "knife", "meaning": "칼"},
        {"word": "spoon", "meaning": "숟가락"},
        {"word": "fork", "meaning": "포크"},
        {"word": "plate", "meaning": "접시"},
    ],

    "💬 생각·말하기": [
        {"word": "think", "meaning": "생각하다"},
        {"word": "know", "meaning": "알다"},
        {"word": "understand", "meaning": "이해하다"},
        {"word": "remember", "meaning": "기억하다"},
        {"word": "forget", "meaning": "잊다"},
        {"word": "say", "meaning": "말하다"},
        {"word": "tell", "meaning": "말하다, 알려주다"},
        {"word": "speak", "meaning": "말하다"},
        {"word": "talk", "meaning": "이야기하다"},
        {"word": "ask", "meaning": "묻다"},
        {"word": "answer", "meaning": "대답하다, 답"},
        {"word": "call", "meaning": "부르다, 전화하다"},
        {"word": "listen", "meaning": "듣다"},
        {"word": "hear", "meaning": "듣다, 들리다"},
        {"word": "read", "meaning": "읽다"},
        {"word": "write", "meaning": "쓰다"},
        {"word": "learn", "meaning": "배우다"},
        {"word": "teach", "meaning": "가르치다"},
        {"word": "mean", "meaning": "의미하다"},
        {"word": "feel", "meaning": "느끼다"},
        {"word": "believe", "meaning": "믿다"},
        {"word": "hope", "meaning": "바라다, 희망하다"},
        {"word": "choose", "meaning": "선택하다"},
        {"word": "decide", "meaning": "결정하다"},
        {"word": "explain", "meaning": "설명하다"},
        {"word": "show", "meaning": "보여주다"},
        {"word": "share", "meaning": "나누다, 공유하다"},
        {"word": "agree", "meaning": "동의하다"},
        {"word": "worry", "meaning": "걱정하다"},
        {"word": "thank", "meaning": "감사하다"},
    ],

    "🎨 상태·형용사": [
        {"word": "good", "meaning": "좋은"},
        {"word": "bad", "meaning": "나쁜"},
        {"word": "big", "meaning": "큰"},
        {"word": "small", "meaning": "작은"},
        {"word": "long", "meaning": "긴"},
        {"word": "short", "meaning": "짧은"},
        {"word": "new", "meaning": "새로운"},
        {"word": "old", "meaning": "오래된, 나이 든"},
        {"word": "young", "meaning": "어린, 젊은"},
        {"word": "high", "meaning": "높은"},
        {"word": "low", "meaning": "낮은"},
        {"word": "fast", "meaning": "빠른"},
        {"word": "slow", "meaning": "느린"},
        {"word": "easy", "meaning": "쉬운"},
        {"word": "hard", "meaning": "어려운, 딱딱한"},
        {"word": "right", "meaning": "맞는, 오른쪽의"},
        {"word": "wrong", "meaning": "틀린"},
        {"word": "same", "meaning": "같은"},
        {"word": "different", "meaning": "다른"},
        {"word": "important", "meaning": "중요한"},
        {"word": "beautiful", "meaning": "아름다운"},
        {"word": "clean", "meaning": "깨끗한"},
        {"word": "dirty", "meaning": "더러운"},
        {"word": "full", "meaning": "가득 찬"},
        {"word": "empty", "meaning": "빈"},
        {"word": "free", "meaning": "자유로운, 무료의"},
        {"word": "safe", "meaning": "안전한"},
        {"word": "dangerous", "meaning": "위험한"},
        {"word": "true", "meaning": "진짜의, 사실인"},
        {"word": "false", "meaning": "거짓의"},
    ],
}

# =========================
# 테마별 쉬운 대화
# =========================
theme_dialogues = {
    "🧑‍🤝‍🧑 사람·관계": [
        {"en": "A: Who is he?", "ko": "A: 그는 누구니?"},
        {"en": "B: He is my friend.", "ko": "B: 그는 내 친구야."},
        {"en": "A: Is she your teacher?", "ko": "A: 그녀는 너의 선생님이니?"},
        {"en": "B: Yes, she is.", "ko": "B: 응, 맞아."},
    ],
    "🏫 학교·교실": [
        {"en": "A: Where is your book?", "ko": "A: 네 책은 어디에 있니?"},
        {"en": "B: It is on my desk.", "ko": "B: 내 책상 위에 있어."},
        {"en": "A: Do you have a pen?", "ko": "A: 너 펜 있니?"},
        {"en": "B: Yes, I do.", "ko": "B: 응, 있어."},
    ],
    "🏃 기본 동작 동사": [
        {"en": "A: What do you do?", "ko": "A: 너는 무엇을 하니?"},
        {"en": "B: I run.", "ko": "B: 나는 달려."},
        {"en": "A: Can you help me?", "ko": "A: 나를 도와줄 수 있니?"},
        {"en": "B: Yes, I can.", "ko": "B: 응, 할 수 있어."},
    ],
    "💖 감정·성격": [
        {"en": "A: Are you happy?", "ko": "A: 너 행복하니?"},
        {"en": "B: Yes, I am happy.", "ko": "B: 응, 나는 행복해."},
        {"en": "A: Are you tired?", "ko": "A: 너 피곤하니?"},
        {"en": "B: No, I am okay.", "ko": "B: 아니, 나는 괜찮아."},
    ],
    "🍎 음식·건강": [
        {"en": "A: Are you hungry?", "ko": "A: 너 배고프니?"},
        {"en": "B: Yes, I am hungry.", "ko": "B: 응, 나는 배고파."},
        {"en": "A: Do you want water?", "ko": "A: 물 마시고 싶니?"},
        {"en": "B: Yes, please.", "ko": "B: 응, 부탁해."},
    ],
    "🚗 장소·이동": [
        {"en": "A: Where is your home?", "ko": "A: 너의 집은 어디에 있니?"},
        {"en": "B: It is near the school.", "ko": "B: 학교 근처에 있어."},
        {"en": "A: Do you go by bus?", "ko": "A: 너는 버스로 가니?"},
        {"en": "B: Yes, I do.", "ko": "B: 응, 그래."},
    ],
    "🌤️ 자연·날씨": [
        {"en": "A: How is the weather?", "ko": "A: 날씨가 어때?"},
        {"en": "B: It is sunny.", "ko": "B: 날씨가 맑아."},
        {"en": "A: Is it cold?", "ko": "A: 춥니?"},
        {"en": "B: No, it is warm.", "ko": "B: 아니, 따뜻해."},
    ],
    "🐶 동물 이름": [
        {"en": "A: What animal do you like?", "ko": "A: 너는 어떤 동물을 좋아하니?"},
        {"en": "B: I like dogs.", "ko": "B: 나는 개를 좋아해."},
        {"en": "A: Do you like cats?", "ko": "A: 고양이를 좋아하니?"},
        {"en": "B: Yes, I do.", "ko": "B: 응, 좋아해."},
    ],
    "⏰ 시간·숫자": [
        {"en": "A: What time is it?", "ko": "A: 지금 몇 시니?"},
        {"en": "B: It is two.", "ko": "B: 2시야."},
        {"en": "A: Is it morning?", "ko": "A: 아침이니?"},
        {"en": "B: Yes, it is.", "ko": "B: 응, 맞아."},
    ],
    "🧸 물건·도구": [
        {"en": "A: What is this?", "ko": "A: 이것은 무엇이니?"},
        {"en": "B: It is a bag.", "ko": "B: 그것은 가방이야."},
        {"en": "A: Is this your phone?", "ko": "A: 이것은 네 전화기니?"},
        {"en": "B: Yes, it is.", "ko": "B: 응, 맞아."},
    ],
    "💬 생각·말하기": [
        {"en": "A: Do you understand?", "ko": "A: 이해했니?"},
        {"en": "B: Yes, I understand.", "ko": "B: 응, 이해했어."},
        {"en": "A: Can you say it?", "ko": "A: 그것을 말할 수 있니?"},
        {"en": "B: Yes, I can.", "ko": "B: 응, 할 수 있어."},
    ],
    "🎨 상태·형용사": [
        {"en": "A: Is it big?", "ko": "A: 그것은 크니?"},
        {"en": "B: No, it is small.", "ko": "B: 아니, 그것은 작아."},
        {"en": "A: Is this easy?", "ko": "A: 이것은 쉬우니?"},
        {"en": "B: Yes, it is easy.", "ko": "B: 응, 쉬워."},
    ],
}


# =========================
# 쉬운 대화 보여주기
# =========================
def show_dialogue(theme_name):
    dialogue = theme_dialogues.get(theme_name, [])

    if not dialogue:
        return

    st.markdown('<div class="dialogue-box">', unsafe_allow_html=True)
    st.markdown('<div class="dialogue-title">💬 아주 쉬운 대화</div>', unsafe_allow_html=True)

    english_lines = []

    for line in dialogue:
        english_lines.append(line["en"])
        st.markdown(f"<div class='dialogue-line'>{line['en']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dialogue-meaning'>{line['ko']}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    dialogue_text = " ".join(english_lines)
    audio_key = safe_filename(theme_name + "_dialogue")
    st.markdown("#### 🎧 대화 듣기")
    simple_audio_player(dialogue_text, key=audio_key, label="대화 듣기")


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
# 단어 익히기
# =========================
def show_word_cards(theme_words, theme_name):
    st.markdown("### 🌼 단어 익히기")
    st.write("단어, 뜻, 발음을 먼저 확인하세요.")

    for idx, item in enumerate(theme_words):
        st.markdown('<div class="word-card">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1.3, 2.1, 1.2])

        with col1:
            st.markdown(f"<div class='word-badge'>🌱 Word {idx + 1}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='word-text'>{item['word']}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='small-muted'>뜻</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='meaning-text'>{item['meaning']}</div>", unsafe_allow_html=True)

        with col3:
            audio_button(
                "🔊 발음 듣기",
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
            st.success("🌈 완벽합니다! 이 테마의 단어를 모두 잘 기억하고 있습니다.")

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
tabs = st.tabs(list(word_themes.keys()))

for tab, theme_name in zip(tabs, word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]

        st.markdown(
            f"""
            <div class="theme-header">
                <div class="theme-title">{theme_name}</div>
                <div class="theme-desc">이 테마에는 {len(theme_words)}개의 단어가 있습니다. 먼저 익히고, 퀴즈로 확인해 봅시다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        show_dialogue(theme_name)

        mode = st.radio(
            "학습 모드를 선택하세요.",
            ["🌼 단어 익히기", "🧸 퀴즈 풀기"],
            key=f"{theme_name}_mode",
            horizontal=True
        )

        if mode == "🌼 단어 익히기":
            show_word_cards(theme_words, theme_name)
        else:
            show_quiz(theme_words, theme_name)
