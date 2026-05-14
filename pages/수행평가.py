import streamlit as st
import streamlit.components.v1 as components
import re
import urllib.parse
import html
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


def make_google_translate_url(text, source="auto", target="en"):
    encoded_text = urllib.parse.quote(str(text).strip())
    return f"https://translate.google.com/?sl={source}&tl={target}&text={encoded_text}&op=translate"


@st.cache_data(show_spinner=False)
def translate_to_english_with_deep_translator(text):
    from deep_translator import GoogleTranslator

    return GoogleTranslator(
        source="auto",
        target="en"
    ).translate(str(text).strip())


# =========================
# 좋아하는 것 변환 사전
# =========================
like_dict = {
    "축구": "soccer",
    "풋살": "futsal",
    "농구": "basketball",
    "야구": "baseball",
    "배구": "volleyball",
    "테니스": "tennis",
    "탁구": "table tennis",
    "배드민턴": "badminton",
    "수영": "swimming",
    "달리기": "running",
    "자전거": "riding a bike",
    "자전거타기": "riding a bike",
    "자전거 타기": "riding a bike",
    "등산": "hiking",
    "낚시": "fishing",
    "운동": "exercising",

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

    "자동차": "cars",
    "자동차 정비": "fixing cars",
    "자동차정비": "fixing cars",
    "차": "cars",
    "정비": "fixing cars",
    "기계": "machines",
    "기계 정비": "fixing machines",
    "기계정비": "fixing machines",
}


def translate_like_item(like_input):
    like_input = str(like_input).strip()

    if not like_input:
        return "soccer", "기본 예시", False

    like_no_space = like_input.replace(" ", "")

    if like_input in like_dict:
        return like_dict[like_input], "기본 단어 사전", False

    if like_no_space in like_dict:
        return like_dict[like_no_space], "기본 단어 사전", False

    if has_korean(like_input):
        try:
            translated = translate_to_english_with_deep_translator(like_input)
            translated = str(translated).strip()

            if translated:
                return translated, "자동 번역", False

        except Exception:
            return "", "구글 번역 연결 필요", True

    cleaned = clean_english_input(like_input)
    return cleaned if cleaned else "soccer", "직접 입력", False


# =========================
# 앱 안에서 발음 듣기 버튼
# =========================
def browser_speech_controls_simple(text, key, speed=1.0):
    safe_text = html.escape(str(text)).replace("\n", " ")

    html_code = f"""
    <div style="
        display:flex;
        gap:8px;
        flex-wrap:wrap;
        width:100%;
        margin:4px 0 14px 0;
    ">
        <button id="speak_{key}"
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

        <button id="pause_{key}"
        style="
            flex:1;
            min-width:120px;
            background-color:#64748b;
            color:white;
            border:none;
            border-radius:12px;
            padding:11px 14px;
            font-size:16px;
            cursor:pointer;
            font-weight:800;
        ">
            ⏸ 잠깐 멈춤
        </button>

        <button id="stop_{key}"
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

    <script>
    const text_{key} = `{safe_text}`;

    document.getElementById("speak_{key}").onclick = function() {{
        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text_{key});
        utterance.lang = "en-US";
        utterance.rate = {speed};
        utterance.pitch = 1;

        window.speechSynthesis.speak(utterance);
    }};

    document.getElementById("pause_{key}").onclick = function() {{
        if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {{
            window.speechSynthesis.pause();
        }} else if (window.speechSynthesis.paused) {{
            window.speechSynthesis.resume();
        }}
    }};

    document.getElementById("stop_{key}").onclick = function() {{
        window.speechSynthesis.cancel();
    }};
    </script>
    """

    components.html(html_code, height=78)


# =========================
# 문장 카드
# =========================
def sentence_card(korean, english, key, speed=1.0):
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

    browser_speech_controls_simple(english, key, speed)


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

st.info("2번에서 한국어 자동 번역이 실패할 때만 구글 번역으로 연결합니다. 나머지 발음은 앱 안에서 바로 들을 수 있습니다.")

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
    speed
)

st.markdown("---")

# =========================
# 2. 내가 좋아하는 것 말하기
# =========================
st.subheader("2. 내가 좋아하는 것 말하기")

like_input = st.text_input(
    "내가 좋아하는 것을 한국어 또는 영어로 써 보세요.",
    placeholder="예: 축구, 노래, 게임, 음악 듣기, 자동차 정비"
)

like_english, translate_method, need_google = translate_like_item(like_input)

if like_input:
    if need_google:
        st.warning("앱 안에서 자동 번역이 되지 않았습니다. 아래 버튼으로 구글 번역에서 영어 표현을 확인하세요.")

        google_translate_input_url = make_google_translate_url(
            like_input,
            source="auto",
            target="en"
        )

        st.link_button(
            "🌐 구글 번역에서 영어 표현 확인하기",
            google_translate_input_url,
            use_container_width=True
        )

        like_english = "soccer"

        st.info("일단 예시 문장은 I like soccer. 로 보여 줍니다.")

    else:
        st.success(f"입력한 내용: {like_input} → 영어 표현: {like_english}")

like_sentence = f"I like {like_english}."

sentence_card(
    "나는 ~을/를 좋아합니다.",
    like_sentence,
    "like",
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
browser_speech_controls_simple(
    picture_script,
    "picture_full",
    speed
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
