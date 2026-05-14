import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS
import io
import base64
import urllib.parse
from pathlib import Path

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

# =========================
# 기본 함수
# =========================
def make_google_translate_url(text, source="auto", target="en"):
    encoded_text = urllib.parse.quote(str(text).strip())
    return f"https://translate.google.com/?sl={source}&tl={target}&text={encoded_text}&op=translate"


@st.cache_data(show_spinner=False)
def make_english_tts_audio(text, slow=False):
    """
    영어 발음 mp3 생성
    브라우저 TTS가 아니라 gTTS 영어 음성을 사용함
    """
    text = str(text).strip()

    if not text:
        text = "Hello."

    fp = io.BytesIO()

    tts = gTTS(
        text=text,
        lang="en",
        tld="com",
        slow=slow
    )

    tts.write_to_fp(fp)
    fp.seek(0)

    return fp.read()


# =========================
# 앱 안에서 영어 발음 듣기 버튼
# 듣기 / 멈춤만 있음
# =========================
def english_audio_buttons(text, key, slow=False):
    try:
        audio_bytes = make_english_tts_audio(text, slow=slow)
        audio_base64 = base64.b64encode(audio_bytes).decode()

        html_code = f"""
        <div style="
            display:flex;
            gap:8px;
            flex-wrap:wrap;
            width:100%;
            margin:4px 0 14px 0;
        ">
            <audio id="audio_{key}">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>

            <button onclick="
                var audio = document.getElementById('audio_{key}');
                audio.currentTime = 0;
                audio.play();
            "
            style="
                flex:1;
                min-width:120px;
                background-color:#2563eb;
                color:white;
                border:none;
                border-radius:12px;
                padding:11px 14px;
                font-size:16px;
                cursor:pointer;
                font-weight:800;
            ">
                ▶ 듣기
            </button>

            <button onclick="
                var audio = document.getElementById('audio_{key}');
                audio.pause();
                audio.currentTime = 0;
            "
            style="
                flex:1;
                min-width:120px;
                background-color:#ef4444;
                color:white;
                border:none;
                border-radius:12px;
                padding:11px 14px;
                font-size:16px;
                cursor:pointer;
                font-weight:800;
            ">
                ■ 멈춤
            </button>
        </div>
        """

        components.html(html_code, height=72)

    except Exception as e:
        st.error("영어 음성 생성 중 오류가 발생했습니다.")
        st.caption(str(e))


# =========================
# 문장 카드
# =========================
def sentence_card(korean, english, key, slow=False, show_audio=True):
    st.markdown(
        f"""
        <div style="
            background:linear-gradient(135deg,#ffffff,#f8fafc);
            border:1px solid #e5e7eb;
            border-radius:18px;
            padding:18px 20px;
            margin:10px 0 10px 0;
            box-shadow:0 3px 10px rgba(0,0,0,0.04);
        ">
            <div style="font-size:17px; color:#374151; font-weight:700; margin-bottom:8px;">
                🇰🇷 {korean}
            </div>
            <div style="font-size:28px; color:#111827; font-weight:800; line-height:1.5;">
                {english}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if show_audio:
        english_audio_buttons(english, key, slow=slow)


# =========================
# 화면 시작
# =========================
st.title("🎤 영어 말하기 수행평가 연습")
st.caption("영어 문장을 보고 듣고 따라 말해 봅시다.")

st.markdown("---")

# =========================
# 듣기 속도 선택
# =========================
st.subheader("🔊 듣기 속도")

speed_label = st.selectbox(
    "듣기 속도를 선택하세요.",
    ["보통", "느리게"],
    index=0
)

slow_mode = True if speed_label == "느리게" else False

st.info("1번, 3번, 4번, 5번 발음은 앱 안에서 영어 음성으로 재생됩니다. 2번 취미 입력은 구글 번역으로 연결합니다.")

st.markdown("---")

# =========================
# 1. 자기소개
# =========================
st.subheader("1. 자기소개하기")

name_input = st.text_input(
    "내 이름을 영어로 써 보세요.",
    placeholder="예: Woochang, Minsu, Jimin"
)

name_text = str(name_input).strip() if str(name_input).strip() else "Woochang"
name_sentence = f"I am {name_text}."

sentence_card(
    "나는 (본인 이름)입니다.",
    name_sentence,
    "name",
    slow=slow_mode
)

st.markdown("---")

# =========================
# 2. 내가 좋아하는 것 / 취미 말하기
# =========================
st.subheader("2. 내가 좋아하는 것 말하기")

st.markdown(
    """
    <div style="
        background:linear-gradient(135deg,#fff7ed,#fffbeb);
        border:1px solid #fed7aa;
        border-radius:18px;
        padding:18px 20px;
        margin:10px 0 12px 0;
        box-shadow:0 3px 10px rgba(0,0,0,0.04);
    ">
        <div style="font-size:17px; color:#9a3412; font-weight:800; margin-bottom:8px;">
            🇰🇷 나의 취미를 말해 봅시다.
        </div>
        <div style="font-size:28px; color:#111827; font-weight:800; line-height:1.5;">
            My hobby is ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ).<br>
            I am a student and tall.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

hobby_input = st.text_input(
    "취미를 한국어로 입력하면 구글 번역으로 이동합니다.",
    placeholder="예: 축구, 노래 부르기, 게임하기, 음악 듣기, 자동차 정비"
)

if hobby_input.strip():
    google_translate_input_url = make_google_translate_url(
        hobby_input,
        source="auto",
        target="en"
    )

    st.link_button(
        "🌐 구글 번역에서 취미 영어 표현과 발음 확인하기",
        google_translate_input_url,
        use_container_width=True
    )

    st.markdown(
        """
        <div style="
            background:#fff7ed;
            border:1px solid #fed7aa;
            border-radius:16px;
            padding:15px 18px;
            margin-top:10px;
            font-size:17px;
            font-weight:700;
            color:#9a3412;
        ">
            구글 번역에서 나온 영어 표현을 괄호 안에 넣어 말하면 됩니다.<br>
            예: My hobby is playing soccer. I am a student and tall.
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("취미를 입력하면 구글 번역으로 연결됩니다.")

st.markdown("---")

# =========================
# 3. 시간 묻기
# =========================
st.subheader("3. 시간 묻기와 하고 싶은 말하기")

sentence_card(
    "지금 몇 시인가요? 저는 지금 집에 가고 싶습니다.",
    "What time is it? I want to go home now.",
    "time_home",
    slow=slow_mode
)

st.markdown("---")

# =========================
# 4. 필요한 것 말하기
# =========================
st.subheader("4. 필요한 것 말하기")

sentence_card(
    "물을 마시고 싶어요. 음식도 먹고 싶습니다.",
    "I want water. I want food too.",
    "water_food",
    slow=slow_mode
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
        st.warning("사진 파일을 찾을 수 없습니다. pages/images/speaking_test.png 또는 images/speaking_test.png 로 저장하세요.")

st.info("⏱️ 20초 안에 사진을 묘사해 봅시다.")

picture_script = """
There are many people in the street.
I can see trees and buildings too.
Some people are riding bikes and some are sitting in chairs.
They look happy.
"""

st.markdown("### 📢 사진 묘사 전체 듣기")

english_audio_buttons(
    picture_script,
    "picture_full",
    slow=slow_mode
)

st.markdown(
    """
    <div style="
        background:#f8fafc;
        border:1px solid #e5e7eb;
        border-radius:18px;
        padding:18px 20px;
        margin-top:12px;
    ">
        <div style="font-size:25px; font-weight:800; line-height:1.7;">
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
