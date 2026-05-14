import streamlit as st
from gtts import gTTS
import base64
import io
import re

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

# =========================
# 안전한 key 만들기 함수
# =========================
def safe_key(key):
    return re.sub(r"[^a-zA-Z0-9_]", "_", key)


# =========================
# 한국어 취미 → 영어 변환
# =========================
hobby_dict = {
    "축구": "soccer",
    "농구": "basketball",
    "야구": "baseball",
    "배구": "volleyball",
    "테니스": "tennis",
    "탁구": "table tennis",
    "배드민턴": "badminton",
    "수영": "swimming",
    "달리기": "running",
    "자전거": "riding a bike",
    "자전거 타기": "riding a bike",
    "등산": "hiking",
    "낚시": "fishing",
    "게임": "playing games",
    "컴퓨터 게임": "playing computer games",
    "노래": "singing",
    "노래 부르기": "singing",
    "춤": "dancing",
    "춤추기": "dancing",
    "음악": "listening to music",
    "음악 듣기": "listening to music",
    "영화": "watching movies",
    "영화 보기": "watching movies",
    "드라마": "watching dramas",
    "유튜브": "watching YouTube",
    "그림": "drawing",
    "그림 그리기": "drawing",
    "독서": "reading books",
    "책 읽기": "reading books",
    "요리": "cooking",
    "사진": "taking pictures",
    "사진 찍기": "taking pictures",
    "잠자기": "sleeping",
    "걷기": "walking",
    "여행": "traveling",
    "운동": "exercising",
}


def translate_hobby(hobby_input):
    hobby_input = hobby_input.strip()

    if not hobby_input:
        return "soccer"

    # 한국어 사전에 있으면 영어로 변환
    if hobby_input in hobby_dict:
        return hobby_dict[hobby_input]

    # 이미 영어로 쓴 경우 그대로 사용
    return hobby_input


# =========================
# TTS 오디오 만들기
# =========================
def make_audio_base64(text):
    tts = gTTS(text=text, lang="en", tld="com")
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return base64.b64encode(fp.read()).decode()


# =========================
# 짧은 듣기 버튼
# =========================
def make_tts_button(text, key, speed=1.0):
    key = safe_key(key)
    audio_base64 = make_audio_base64(text)

    audio_html = f"""
    <audio id="audio_{key}">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>

    <button onclick="
        var audio = document.getElementById('audio_{key}');
        audio.playbackRate = {speed};
        audio.currentTime = 0;
        audio.play();
    "
        style="
            background-color:#2563eb;
            color:white;
            border:none;
            border-radius:10px;
            padding:8px 14px;
            font-size:15px;
            cursor:pointer;
            width:100%;
        ">
        🔊 듣기
    </button>
    """

    st.components.v1.html(audio_html, height=45)


# =========================
# 전체 오디오 플레이어
# =========================
def make_audio_player(text, key, speed=1.0):
    key = safe_key(key)
    audio_base64 = make_audio_base64(text)

    audio_html = f"""
    <audio id="player_{key}" controls style="width:100%;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>

    <script>
        var audio = document.getElementById("player_{key}");
        audio.playbackRate = {speed};
    </script>
    """

    st.components.v1.html(audio_html, height=60)


def sentence_card(korean, english, key, speed=1.0):
    col1, col2, col3 = st.columns([2.2, 4, 1.2])

    with col1:
        st.markdown(f"**🇰🇷 {korean}**")

    with col2:
        st.markdown(f"### {english}")

    with col3:
        make_tts_button(english, key, speed)


# =========================
# 제목
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
    ["느리게 0.7배", "조금 느리게 0.85배", "보통 1.0배", "조금 빠르게 1.15배", "빠르게 1.3배"],
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

st.markdown("---")

# =========================
# 1. 자기소개
# =========================
st.subheader("1. 자기소개하기")

name = st.text_input("내 이름을 영어로 써 보세요.", placeholder="예: Woochang")

if name:
    name_sentence = f"I am {name}."
else:
    name_sentence = "I am Woochang."

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

if hobby_input:
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

# 사진 크기 줄이기
left_col, center_col, right_col = st.columns([1.3, 1.8, 1.3])

with center_col:
    st.image(
        "pages/images/수행평가 그림.png",
        caption="Describe the picture.",
        use_container_width=True
    )

st.info("⏱️ 20초 안에 사진을 묘사해 봅시다.")

picture_script = """
There are many people in the street.
I can see trees and buildings too.
Some people are riding bikes and some are sitting in chairs.
They look happy.
"""

st.markdown("### 📢 사진 묘사 전체 듣기")
st.caption("오디오 바를 움직이면 앞뒤로 이동할 수 있습니다.")

make_audio_player(picture_script, "picture_full", speed)

st.text_area(
    "사진 묘사 대본",
    picture_script,
    height=150
)

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

st.text_area("전체 말하기 대본", full_script, height=250)

make_audio_player(full_script, "full_script", speed)

st.success("영어 문장을 듣고 따라 말하면서 연습해 보세요.")
