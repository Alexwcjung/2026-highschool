import streamlit as st
from gtts import gTTS
import base64
import io

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

# =========================
# TTS 함수
# =========================
def make_tts_button(text, key):
    tts = gTTS(text=text, lang="en", tld="com")
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    audio_base64 = base64.b64encode(fp.read()).decode()

    audio_html = f"""
    <audio id="audio_{key}">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    <button onclick="document.getElementById('audio_{key}').play()"
        style="
            background-color:#2563eb;
            color:white;
            border:none;
            border-radius:10px;
            padding:8px 14px;
            font-size:15px;
            cursor:pointer;
        ">
        🔊 듣기
    </button>
    """

    st.components.v1.html(audio_html, height=45)


def sentence_card(korean, english, key):
    col1, col2, col3 = st.columns([2, 3, 1])

    with col1:
        st.markdown(f"**🇰🇷 {korean}**")

    with col2:
        st.markdown(f"### {english}")

    with col3:
        make_tts_button(english, key)


# =========================
# 제목
# =========================
st.title("🎤 영어 말하기 수행평가 연습")
st.caption("영어 문장을 보고 듣고 따라 말해 봅시다.")

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
    "name"
)

st.markdown("---")

# =========================
# 2. 취미 말하기
# =========================
st.subheader("2. 나의 취미 말하기")

hobby = st.text_input("나의 취미를 영어로 써 보세요.", placeholder="예: soccer, music, dancing")

if hobby:
    hobby_sentence = f"My hobby is {hobby}. I am a student and tall."
else:
    hobby_sentence = "My hobby is soccer. I am a student and tall."

sentence_card(
    "나의 취미는 ~입니다. 나는 학생이고 키가 큽니다.",
    hobby_sentence,
    "hobby"
)

st.markdown("---")

# =========================
# 3. 시간 묻기
# =========================
st.subheader("3. 시간 묻기와 하고 싶은 말하기")

sentence_card(
    "지금 몇 시인가요? 저는 지금 집에 가고 싶습니다.",
    "What time is it? I want to go home now.",
    "time_home"
)

st.markdown("---")

# =========================
# 4. 물과 음식 말하기
# =========================
st.subheader("4. 필요한 것 말하기")

sentence_card(
    "물을 마시고 싶어요. 음식도 먹고 싶습니다.",
    "I want water. I want food too.",
    "water_food"
)

st.markdown("---")

# =========================
# 5. 사진 묘사하기
# =========================
st.subheader("5. 사진 묘사하기")

st.info("⏱️ 20초 안에 사진을 묘사해 봅시다.")

picture_sentences = [
    (
        "거리에 사람들이 많이 있습니다.",
        "There are many people in the street.",
        "pic1"
    ),
    (
        "나무와 건물들도 보입니다.",
        "I can see trees and buildings too.",
        "pic2"
    ),
    (
        "몇몇 사람들은 자전거를 타고 있습니다.",
        "Some people are riding bikes.",
        "pic3"
    ),
    (
        "몇몇 사람들은 의자에 앉아 있습니다.",
        "Some people are sitting in chairs.",
        "pic4"
    ),
    (
        "그들은 행복해 보입니다.",
        "They look happy.",
        "pic5"
    )
]

for korean, english, key in picture_sentences:
    sentence_card(korean, english, key)

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
Some people are riding bikes.
Some people are sitting in chairs.
They look happy.
"""

st.text_area("전체 말하기 대본", full_script, height=250)

make_tts_button(full_script, "full_script")

st.success("영어 문장을 듣고 따라 말하면서 연습해 보세요.")
