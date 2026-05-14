import streamlit as st
import streamlit.components.v1 as components
import re
import json
from pathlib import Path

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

# =========================
# 기본 함수
# =========================
def has_korean(text):
    return any("가" <= ch <= "힣" for ch in str(text))


def clean_english_input(text):
    text = str(text).strip()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# =========================
# 한국어 취미 → 영어 변환
# =========================
hobby_dict = {
    "축구": "soccer",
    "축구하기": "soccer",
    "풋살": "futsal",
    "농구": "basketball",
    "야구": "baseball",
    "배구": "volleyball",
    "테니스": "tennis",
    "탁구": "table tennis",
    "배드민턴": "badminton",
    "수영": "swimming",
    "달리기": "running",
    "조깅": "jogging",
    "자전거": "riding a bike",
    "자전거타기": "riding a bike",
    "자전거 타기": "riding a bike",
    "등산": "hiking",
    "낚시": "fishing",

    "게임": "playing games",
    "게임하기": "playing games",
    "컴퓨터게임": "playing computer games",
    "컴퓨터 게임": "playing computer games",
    "휴대폰게임": "playing mobile games",
    "휴대폰 게임": "playing mobile games",
    "모바일게임": "playing mobile games",
    "모바일 게임": "playing mobile games",

    "노래": "singing",
    "노래부르기": "singing",
    "노래 부르기": "singing",
    "춤": "dancing",
    "춤추기": "dancing",

    "음악": "listening to music",
    "음악듣기": "listening to music",
    "음악 듣기": "listening to music",

    "영화": "watching movies",
    "영화보기": "watching movies",
    "영화 보기": "watching movies",
    "드라마": "watching dramas",
    "드라마보기": "watching dramas",
    "드라마 보기": "watching dramas",
    "유튜브": "watching YouTube",
    "유튜브보기": "watching YouTube",
    "유튜브 보기": "watching YouTube",

    "그림": "drawing",
    "그림그리기": "drawing",
    "그림 그리기": "drawing",
    "독서": "reading books",
    "책읽기": "reading books",
    "책 읽기": "reading books",
    "요리": "cooking",
    "사진": "taking pictures",
    "사진찍기": "taking pictures",
    "사진 찍기": "taking pictures",

    "잠": "sleeping",
    "잠자기": "sleeping",
    "걷기": "walking",
    "산책": "walking",
    "여행": "traveling",
    "운동": "exercising",
}


def translate_hobby(hobby_input):
    hobby_input = str(hobby_input).strip()

    if not hobby_input:
        return "soccer"

    hobby_no_space = hobby_input.replace(" ", "")

    if hobby_input in hobby_dict:
        return hobby_dict[hobby_input]

    if hobby_no_space in hobby_dict:
        return hobby_dict[hobby_no_space]

    # 사전에 없는 한국어 입력 시 기본값
    if has_korean(hobby_input):
        return "playing sports"

    # 영어로 입력한 경우
    cleaned = clean_english_input(hobby_input)
    return cleaned if cleaned else "playing sports"


# =========================
# 브라우저 음성 버튼
# gTTS 사용 안 함
# =========================
def speech_button(text, key, speed=1.0, label="🔊 듣기"):
    text_js = json.dumps(str(text))
    key = re.sub(r"[^a-zA-Z0-9_]", "_", str(key))

    html_code = f"""
    <button onclick="
        window.speechSynthesis.cancel();
        var utterance = new SpeechSynthesisUtterance({text_js});
        utterance.lang = 'en-US';
        utterance.rate = {speed};
        utterance.pitch = 1;
        window.speechSynthesis.speak(utterance);
    "
    style="
        background-color:#2563eb;
        color:white;
        border:none;
        border-radius:10px;
        padding:8px 12px;
        font-size:14px;
        cursor:pointer;
        width:100%;
    ">
        {label}
    </button>
    """

    components.html(html_code, height=45)


def simple_speech_controls(text, key, speed=1.0):
    text_js = json.dumps(str(text))
    key = re.sub(r"[^a-zA-Z0-9_]", "_", str(key))

    html_code = f"""
    <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <button onclick="
            window.speechSynthesis.cancel();
            var utterance = new SpeechSynthesisUtterance({text_js});
            utterance.lang = 'en-US';
            utterance.rate = {speed};
            utterance.pitch = 1;
            window.speechSynthesis.speak(utterance);
        "
        style="
            background-color:#2563eb;
            color:white;
            border:none;
            border-radius:10px;
            padding:9px 14px;
            font-size:15px;
            cursor:pointer;
        ">
            ▶ 전체 듣기
        </button>

        <button onclick="window.speechSynthesis.cancel();"
        style="
            background-color:#dc2626;
            color:white;
            border:none;
            border-radius:10px;
            padding:9px 14px;
            font-size:15px;
            cursor:pointer;
        ">
            ⏹ 멈춤
        </button>
    </div>
    """

    components.html(html_code, height=60)


# =========================
# 문장 카드
# =========================
def sentence_card(korean, english, key, speed=1.0):
    col1, col2, col3 = st.columns([2.2, 4, 1.3])

    with col1:
        st.markdown(f"**🇰🇷 {korean}**")

    with col2:
        st.markdown(f"### {english}")

    with col3:
        speech_button(english, key, speed)


# =========================
# 화면 시작
# =========================
st.title("🎤 영어 말하기 수행평가 연습")
st.caption("영어 문장을 보고 듣고 따라 말해 봅시다.")

st.markdown("---")

# =========================
# 듣기 속도 조절
# =========================
st.subheader("🔊 듣기 속도 조절")

speed_label = st.selectbox(
    "듣기 속도를 선택하세요.",
    [
        "느리게 0.7배",
        "조금 느리게 0.85배",
        "보통 1.0배",
        "조금 빠르게 1.15배",
        "빠르게 1.3배"
    ],
    index=2
)

speed_dict = {
    "느리게 0.7배": 0.7,
    "조금 느리게 0.85배": 0.85,
    "보통 1.0배": 1.0,
    "조금 빠르게 1.15배": 1.15,
    "빠르게 1.3배": 1.3
}

speed = speed_dict[speed_label]

st.info("이 버전은 gTTS를 사용하지 않고, 휴대폰/브라우저의 기본 음성 기능을 사용합니다.")

st.markdown("---")

# =========================
# 1. 자기소개
# =========================
st.subheader("1. 자기소개하기")

name_input = st.text_input(
    "내 이름을 한국어 또는 영어로 써 보세요.",
    placeholder="예: 정우창, Woochang"
)

if name_input.strip():
    name_for_sentence = name_input.strip()
else:
    name_for_sentence = "Woochang"

name_sentence = f"I am {name_for_sentence}."

sentence_card(
    "나는 (본인 이름)입니다.",
    name_sentence,
    "name",
    speed
)

st.markdown("---")

# =========================
# 2. 취미 말하기
# =========================
st.subheader("2. 나의 취미 말하기")

hobby_input = st.text_input(
    "나의 취미를 한국어 또는 영어로 써 보세요.",
    placeholder="예: 축구, 노래, 게임, 음악 듣기"
)

hobby_english = translate_hobby(hobby_input)

if hobby_input.strip():
    st.info(f"입력한 취미: {hobby_input} → 영어 표현: {hobby_english}")

hobby_sentence = f"My hobby is {hobby_english}. I am a student and tall."

sentence_card(
    "나의 취미는 ~입니다. 나는 학생이고 키가 큽니다.",
    hobby_sentence,
    "hobby",
    speed
)

st.markdown("---")

# =========================
# 3. 시간 묻기
# =========================
st.subheader("3. 시간 묻기와 하고 싶은 말하기")

sentence_card(
    "지금 몇 시인가요? 저는 지금 집에 가고 싶습니다.",
    "What time is it? I want to go home now.",
    "time_home",
    speed
)

st.markdown("---")

# =========================
# 4. 물과 음식 말하기
# =========================
st.subheader("4. 필요한 것 말하기")

sentence_card(
    "물을 마시고 싶어요. 음식도 먹고 싶습니다.",
    "I want water. I want food too.",
    "water_food",
    speed
)

st.markdown("---")

# =========================
# 5. 사진 묘사하기
# =========================
st.subheader("5. 사진 묘사하기")

image_paths = [
    Path("pages/images/speaking_test.png"),
    Path("pages/images/수행평가 그림.png"),
]

image_path = None
for p in image_paths:
    if p.exists():
        image_path = p
        break

left_col, center_col, right_col = st.columns([1.3, 1.8, 1.3])

with center_col:
    if image_path:
        st.image(
            str(image_path),
            caption="Describe the picture.",
            use_container_width=True
        )
    else:
        st.warning("사진 파일을 찾을 수 없습니다. pages/images/speaking_test.png 로 저장하는 것을 추천합니다.")

st.info("⏱️ 20초 안에 사진을 묘사해 봅시다.")

picture_script = """
There are many people in the street.
I can see trees and buildings too.
Some people are riding bikes and some are sitting in chairs.
They look happy.
"""

st.markdown("### 📢 사진 묘사 전체 듣기")
simple_speech_controls(picture_script, "picture_full", speed)

st.markdown("### There are many people in the street.")
st.markdown("### I can see trees and buildings too.")
st.markdown("### Some people are riding bikes and some are sitting in chairs.")
st.markdown("### They look happy.")

st.markdown("---")

# =========================
# 전체 듣기
# =========================
st.subheader("📢 전체 말하기 대본 듣기")

full_script = f"""
{name_sentence}

{hobby_sentence}

What time is it? I want to go home now.

I want water. I want food too.

There are many people in the street.
I can see trees and buildings too.
Some people are riding bikes and some are sitting in chairs.
They look happy.
"""

st.text_area(
    "전체 말하기 대본",
    full_script,
    height=250
)

simple_speech_controls(full_script, "full_script", speed)

st.success("영어 문장을 듣고 따라 말하면서 연습해 보세요.")
