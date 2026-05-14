import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS
import urllib.parse
import base64
import hashlib
from pathlib import Path

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

# =========================
# TTS 저장 폴더
# =========================
AUDIO_DIR = Path("tts_audio")
AUDIO_DIR.mkdir(exist_ok=True)


# =========================
# 기본 함수
# =========================
def make_google_translate_url(text, source="auto", target="en"):
    encoded_text = urllib.parse.quote(str(text).strip())
    return f"https://translate.google.com/?sl={source}&tl={target}&text={encoded_text}&op=translate"


def safe_file_name(text, slow=False):
    raw = str(text) + str(slow)
    return hashlib.md5(raw.encode("utf-8")).hexdigest() + ".mp3"


def make_english_mp3_file(text, slow=False):
    """
    영어 mp3 파일을 직접 생성함.
    브라우저 음성 기능을 쓰지 않으므로 KR 음성으로 읽히지 않음.
    """
    text = str(text).strip()

    if not text:
        text = "Hello."

    file_name = safe_file_name(text, slow)
    file_path = AUDIO_DIR / file_name

    if not file_path.exists():
        tts = gTTS(
            text=text,
            lang="en",
            tld="com",
            slow=slow
        )
        tts.save(str(file_path))

    return file_path


def mp3_file_to_base64(file_path):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode("utf-8")


# =========================
# 영어 듣기 / 멈춤 버튼
# =========================
def english_audio_buttons(text, key, slow=False):
    try:
        file_path = make_english_mp3_file(text, slow=slow)
        audio_base64 = mp3_file_to_base64(file_path)

        html_code = f"""
        <div style="
            display:flex;
            gap:8px;
            flex-wrap:wrap;
            width:100%;
            margin:4px 0 14px 0;
        ">
            <audio id="audio_{key}" preload="auto">
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            </audio>

            <button onclick="
                var audio = document.getElementById('audio_{key}');
                audio.pause();
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

        components.html(html_code, height=76)

    except Exception as e:
        st.error("영어 음성 파일을 만들지 못했습니다.")
        st.caption("Streamlit Cloud에서 gTTS 접속이 막히면 이 오류가 날 수 있습니다.")
        st.caption(str(e))


# =========================
# 문장 카드
# =========================
def sentence_card(korean, english, key, slow=False):
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

    english_audio_buttons(english, key, slow=slow)


# =========================
# 화면 시작
# =========================
st.title("🎤 영어 말하기 수행평가 연습")
st.caption("영어 문장을 보고 듣고 따라 말해 봅시다.")

st.markdown("---")

# =========================
# 듣기 속도
# =========================
st.subheader("🔊 듣기 속도")

speed_label = st.selectbox(
    "듣기 속도를 선택하세요.",
    ["보통", "느리게"],
    index=0
)

slow_mode = True if speed_label == "느리게" else False

st.info(
    "1번, 3번, 4번, 5번은 앱 안에서 영어 mp3로 재생됩니다. "
    "2번 취미 입력은 구글 번역으로 이동해서 영어 표현과 발음을 확인합니다."
)

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
    "name_audio",
    slow=slow_mode
)

st.markdown("---")

# =========================
# 2. 취미 말하기
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
    st.info("취미를 입력하면 구글 번역으로 연결됩니다. 2번 발음은 구글 번역에서 확인합니다.")

st.markdown("---")

# =========================
# 3. 시간 묻기
# =========================
st.subheader("3. 시간 묻기와 하고 싶은 말하기")

sentence_card(
    "지금 몇 시인가요? 저는 지금 집에 가고 싶습니다.",
    "What time is it? I want to go home now.",
    "time_home_audio",
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
    "water_food_audio",
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

english_audio_buttons(
    picture_script,
    "picture_full_audio",
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
