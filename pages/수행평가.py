import streamlit as st
from urllib.parse import quote
from pathlib import Path
import requests
import re

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

# =========================
# 기본 함수
# =========================
def make_google_translate_url(text, source="auto", target="en"):
    encoded_text = quote(str(text).strip())
    return f"https://translate.google.com/?sl={source}&tl={target}&text={encoded_text}&op=translate"


def make_google_tts_url(text, lang="en"):
    clean_text = str(text).strip() or "Hello."
    encoded = quote(clean_text)
    return f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={lang}&q={encoded}"


@st.cache_data(show_spinner=False)
def get_tts_mp3_bytes(text, lang="en"):
    clean_text = str(text).strip() or "Hello."
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


def english_audio_player(text):
    """화면에 영어 오디오를 바로 표시합니다."""
    text = str(text).strip()
    if not text:
        return
    try:
        audio_bytes = get_tts_mp3_bytes(text, lang="en")
        st.audio(audio_bytes, format="audio/mp3")
    except Exception as e:
        st.error("영어 발음 오디오를 만들지 못했습니다.")
        st.caption(f"오류 내용: {e}")
        st.link_button("🔊 새 창에서 듣기", make_google_tts_url(text, lang="en"), use_container_width=True)


# =========================
# 한글 이름 간단 로마자 변환
# =========================
CHO = [
    "g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s",
    "ss", "", "j", "jj", "ch", "k", "t", "p", "h"
]
JUNG = [
    "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa",
    "wae", "oe", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"
]
JONG = [
    "", "k", "k", "ks", "n", "nj", "nh", "t", "l", "lk",
    "lm", "lb", "ls", "lt", "lp", "lh", "m", "p", "ps", "t",
    "t", "ng", "t", "t", "k", "t", "p", "t"
]


def romanize_hangul_name(text):
    """학생 이름 입력용 간단 로마자 변환. 완벽한 여권식 변환은 아니지만 수업용으로 바로 쓸 수 있게 함."""
    text = str(text).strip()
    if not text:
        return "Woochang"

    result = []
    for ch in text:
        code = ord(ch)
        if 0xAC00 <= code <= 0xD7A3:
            s_index = code - 0xAC00
            cho = s_index // 588
            jung = (s_index % 588) // 28
            jong = s_index % 28
            syllable = CHO[cho] + JUNG[jung] + JONG[jong]
            result.append(syllable)
        elif ch.isalpha() or ch in [" ", "-"]:
            result.append(ch)
        else:
            result.append(" ")

    romanized = "".join(result)
    romanized = re.sub(r"\s+", " ", romanized).strip()
    if not romanized:
        return "Woochang"
    return " ".join(part.capitalize() for part in romanized.split())


# =========================
# 디자인
# =========================
st.markdown(
    """
    <style>
    .stApp { background-color:#ffffff; }
    .main-title {
        background:linear-gradient(135deg,#ecfeff,#fef3c7,#fce7f3);
        padding:26px;
        border-radius:22px;
        border:1px solid #e5e7eb;
        box-shadow:0 6px 18px rgba(0,0,0,0.06);
        margin-bottom:24px;
    }
    .main-title h1 {
        margin:0;
        font-size:42px;
        font-weight:900;
        color:#111827;
    }
    .main-title p {
        margin:8px 0 0 0;
        font-size:17px;
        font-weight:800;
        color:#475569;
    }
    .sentence-card {
        background:linear-gradient(135deg,#ffffff,#f8fafc);
        border:1px solid #e5e7eb;
        border-radius:18px;
        padding:18px 20px;
        margin:10px 0 10px 0;
        box-shadow:0 3px 10px rgba(0,0,0,0.04);
    }
    .ko-line {
        font-size:17px;
        color:#374151;
        font-weight:800;
        margin-bottom:8px;
        line-height:1.6;
    }
    .en-line {
        font-size:28px;
        color:#111827;
        font-weight:900;
        line-height:1.5;
    }
    .orange-card {
        background:linear-gradient(135deg,#fff7ed,#fffbeb);
        border:1px solid #fed7aa;
        border-radius:18px;
        padding:18px 20px;
        margin:10px 0 12px 0;
        box-shadow:0 3px 10px rgba(0,0,0,0.04);
    }
    </style>
    """,
    unsafe_allow_html=True
)


def sentence_card(korean, english):
    st.markdown(
        f"""
        <div class="sentence-card">
            <div class="ko-line">🇰🇷 {korean}</div>
            <div class="en-line">{english}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    english_audio_player(english)


# =========================
# 화면 시작
# =========================
st.markdown(
    """
    <div class="main-title">
        <h1>🎤 영어 말하기 수행평가 연습</h1>
        <p>영어 문장을 보고, 듣고, 따라 말해 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =========================
# 1. 자기소개
# =========================
st.subheader("1. 자기소개하기")

name_input = st.text_input(
    "내 이름을 한국어 또는 영어로 써 보세요.",
    placeholder="예: 정우창, 민수, Jimin"
)

name_text = str(name_input).strip() if str(name_input).strip() else "Woochang"
romanized_name = romanize_hangul_name(name_text)

if name_input.strip() and romanized_name.lower() != name_text.lower():
    st.info(f"영어 이름 표기 예시: **{romanized_name}**")

name_sentence = f"I am {romanized_name}."

sentence_card(
    "나는 (본인 이름)입니다.",
    name_sentence
)

st.markdown("---")

# =========================
# 2. 내가 좋아하는 것 / 취미 말하기
# =========================
st.subheader("2. 내가 좋아하는 것 말하기")

st.markdown(
    """
    <div class="orange-card">
        <div class="ko-line" style="color:#9a3412;">
            🇰🇷 내 취미는 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )입니다.<br>
            나는 학생이고 키가 큽니다.
        </div>
        <div class="en-line">
            My hobby is ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ).<br>
            I am a student and tall.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

hobby_ko_input = st.text_input(
    "취미를 한국어로 입력하면 구글 번역으로 이동합니다.",
    placeholder="예: 축구, 노래 부르기, 게임하기, 음악 듣기, 자동차 정비"
)

if hobby_ko_input.strip():
    st.link_button(
        "🌐 구글 번역에서 취미 영어 표현과 발음 확인하기",
        make_google_translate_url(hobby_ko_input, source="auto", target="en"),
        use_container_width=True
    )
else:
    st.info("취미를 한국어로 입력하면 구글 번역으로 연결됩니다.")

hobby_en_input = st.text_input(
    "구글 번역에서 나온 영어 취미 표현을 여기에 넣어 보세요.",
    placeholder="예: playing soccer, listening to music, playing games"
)

hobby_en = str(hobby_en_input).strip() if str(hobby_en_input).strip() else "playing soccer"
hobby_sentence = f"My hobby is {hobby_en}. I am a student and tall."

sentence_card(
    f"내 취미는 {hobby_ko_input.strip() if hobby_ko_input.strip() else '(취미)'}입니다. 나는 학생이고 키가 큽니다.",
    hobby_sentence
)

st.markdown("---")

# =========================
# 3. 시간 묻기
# =========================
st.subheader("3. 시간 묻기와 하고 싶은 말하기")

sentence_card(
    "지금 몇 시인가요? 저는 지금 집에 가고 싶습니다.",
    "What time is it? I want to go home now."
)

st.markdown("---")

# =========================
# 4. 필요한 것 말하기
# =========================
st.subheader("4. 필요한 것 말하기")

sentence_card(
    "물을 마시고 싶어요. 음식도 먹고 싶습니다.",
    "I want water. I want food too."
)

st.markdown("---")

# =========================
# 5. 사진 묘사하기
# =========================
st.subheader("5. 사진 묘사하기")

image_paths = [
    Path("pages/images/speaking_test.png"),
    Path("pages/images/수행평가 그림.png"),
    Path("images/speaking_test.png"),
    Path("images/수행평가 그림.png"),
]

image_path = None
for p in image_paths:
    if p.exists():
        image_path = p
        break

left_col, center_col, right_col = st.columns([1.2, 1.8, 1.2])

with center_col:
    if image_path:
        st.image(
            str(image_path),
            caption="Describe the picture.",
            use_container_width=True
        )
    else:
        st.warning(
            "사진 파일을 찾을 수 없습니다. "
            "pages/images/speaking_test.png 또는 images/speaking_test.png 로 저장하세요."
        )

st.info("⏱️ 20초 안에 사진을 묘사해 봅시다.")

picture_script = (
    "There are many people in the street. "
    "I can see trees and buildings too. "
    "Some people are riding bikes and some are sitting in chairs. "
    "They look happy."
)

st.markdown("### 📢 사진 묘사 전체 듣기")
english_audio_player(picture_script)

st.markdown(
    """
    <div style="
        background:#f8fafc;
        border:1px solid #e5e7eb;
        border-radius:18px;
        padding:18px 20px;
        margin-top:12px;
    ">
        <div style="font-size:25px; font-weight:800; line-height:1.7; color:#111827;">
            There are many people in the street.<br>
            I can see trees and buildings too.<br>
            Some people are riding bikes and some are sitting in chairs.<br>
            They look happy.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.success("영어 문장을 듣고 따라 말하면서 연습해 보세요.")
