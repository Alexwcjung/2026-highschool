import streamlit as st
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Speaking Practice",
    page_icon="🗣️",
    layout="wide"
)

st.title("🗣️ Phonics Speaking Practice")
st.caption("스펠링을 보고 먼저 말한 뒤, 원어민 발음을 듣고, 글자 소리가 어떻게 합쳐지는지 배워 봅시다.")

# =========================
# 안내 박스
# =========================
st.markdown(
    """
    <div style="
        border-left: 7px solid #ff9f1c;
        background: linear-gradient(135deg, #fff7e6, #fff0f5);
        padding: 18px 20px;
        border-radius: 18px;
        margin-bottom: 24px;
        line-height: 1.8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    ">
        <div style="font-size:22px; font-weight:900; margin-bottom:10px;">
            📌 연습 방법
        </div>
        <div>1. 화면에 보이는 <b>영어 단어</b>를 먼저 큰 소리로 읽습니다.</div>
        <div>2. <b>🔊 원어민 발음 듣기</b> 버튼을 눌러 실제 발음을 확인합니다.</div>
        <div>3. <b>글자 소리가 어떻게 합쳐지는지</b> 확인합니다.</div>
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


def play_audio(text, key):
    if st.button("🔊 원어민 발음 듣기", key=key):
        audio_bytes = make_tts_audio(text)
        st.audio(audio_bytes, format="audio/mp3")


# =========================
# 연습 단어 데이터
# =========================
practice_sets = {
    "① 자음 소리": [
        {
            "word": "bat",
            "explain": "b의 '브' 소리 + a의 '애' 소리 + t의 '트' 소리가 합쳐져서 뱉(bat)처럼 발음됩니다."
        },
        {
            "word": "cat",
            "explain": "c의 '크' 소리 + a의 '애' 소리 + t의 '트' 소리가 합쳐져서 캣(cat)처럼 발음됩니다."
        },
        {
            "word": "dog",
            "explain": "d의 '드' 소리 + o의 '아/오' 소리 + g의 '그' 소리가 합쳐져서 닥/독(dog)처럼 발음됩니다."
        },
        {
            "word": "fish",
            "explain": "f의 '프' 소리 + i의 짧은 '이' 소리 + sh의 '쉬' 소리가 합쳐져서 피쉬(fish)처럼 발음됩니다."
        },
        {
            "word": "goat",
            "explain": "g의 '그' 소리 + oa의 '오우' 소리 + t의 '트' 소리가 합쳐져서 고우트(goat)처럼 발음됩니다."
        },
        {
            "word": "hat",
            "explain": "h의 '흐' 소리 + a의 '애' 소리 + t의 '트' 소리가 합쳐져서 햇(hat)처럼 발음됩니다."
        },
        {
            "word": "jam",
            "explain": "j의 '쥬/즈' 소리 + a의 '애' 소리 + m의 '므' 소리가 합쳐져서 잼(jam)처럼 발음됩니다."
        },
        {
            "word": "sun",
            "explain": "s의 '스' 소리 + u의 '어' 소리 + n의 '느' 소리가 합쳐져서 썬(sun)처럼 발음됩니다."
        },
        {
            "word": "van",
            "explain": "v의 '브' 소리 + a의 '애' 소리 + n의 '느' 소리가 합쳐져서 밴(van)처럼 발음됩니다."
        },
        {
            "word": "yes",
            "explain": "y의 '이/여' 소리 + e의 '에' 소리 + s의 '스' 소리가 합쳐져서 예스(yes)처럼 발음됩니다."
        },
    ],

    "② 짧은 모음": [
        {
            "word": "apple",
            "explain": "a의 '애' 소리 + pp의 '프' 소리 + le의 약한 '을' 소리가 합쳐져서 애플(apple)처럼 발음됩니다."
        },
        {
            "word": "cat",
            "explain": "c의 '크' 소리 + a의 '애' 소리 + t의 '트' 소리가 합쳐져서 캣(cat)처럼 발음됩니다."
        },
        {
            "word": "egg",
            "explain": "e의 '에' 소리 + gg의 '그' 소리가 합쳐져서 에그(egg)처럼 발음됩니다."
        },
        {
            "word": "bed",
            "explain": "b의 '브' 소리 + e의 '에' 소리 + d의 '드' 소리가 합쳐져서 베드(bed)처럼 발음됩니다."
        },
        {
            "word": "sit",
            "explain": "s의 '스' 소리 + i의 짧은 '이' 소리 + t의 '트' 소리가 합쳐져서 싯(sit)처럼 발음됩니다."
        },
        {
            "word": "pig",
            "explain": "p의 '프' 소리 + i의 짧은 '이' 소리 + g의 '그' 소리가 합쳐져서 피그(pig)처럼 발음됩니다."
        },
        {
            "word": "hot",
            "explain": "h의 '흐' 소리 + o의 '아/오' 소리 + t의 '트' 소리가 합쳐져서 핱(hot)처럼 발음됩니다."
        },
        {
            "word": "cup",
            "explain": "c의 '크' 소리 + u의 '어' 소리 + p의 '프' 소리가 합쳐져서 컵(cup)처럼 발음됩니다."
        },
        {
            "word": "bus",
            "explain": "b의 '브' 소리 + u의 '어' 소리 + s의 '스' 소리가 합쳐져서 버스(bus)처럼 발음됩니다."
        },
        {
            "word": "fox",
            "explain": "f의 '프' 소리 + o의 '아/오' 소리 + x의 '크스' 소리가 합쳐져서 팍스/폭스(fox)처럼 발음됩니다."
        },
    ],

    "③ 긴 모음": [
        {
            "word": "cake",
            "explain": "c의 '크' 소리 + a의 이름 소리 '에이' + k의 '크' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 케이크(cake)처럼 발음됩니다."
        },
        {
            "word": "name",
            "explain": "n의 '느' 소리 + a의 이름 소리 '에이' + m의 '므' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 네임(name)처럼 발음됩니다."
        },
        {
            "word": "tree",
            "explain": "t의 '트' 소리 + r의 '르' 소리 + ee의 긴 '이' 소리가 합쳐져서 트리(tree)처럼 발음됩니다."
        },
        {
            "word": "see",
            "explain": "s의 '스' 소리 + ee의 긴 '이' 소리가 합쳐져서 씨(see)처럼 발음됩니다."
        },
        {
            "word": "bike",
            "explain": "b의 '브' 소리 + i의 이름 소리 '아이' + k의 '크' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 바이크(bike)처럼 발음됩니다."
        },
        {
            "word": "five",
            "explain": "f의 '프' 소리 + i의 이름 소리 '아이' + v의 '브' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 파이브(five)처럼 발음됩니다."
        },
        {
            "word": "rope",
            "explain": "r의 '르' 소리 + o의 이름 소리 '오우' + p의 '프' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 로우프(rope)처럼 발음됩니다."
        },
        {
            "word": "home",
            "explain": "h의 '흐' 소리 + o의 이름 소리 '오우' + m의 '므' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 호움(home)처럼 발음됩니다."
        },
        {
            "word": "cube",
            "explain": "c의 '크' 소리 + u의 이름 소리 '유' + b의 '브' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 큐브(cube)처럼 발음됩니다."
        },
        {
            "word": "cute",
            "explain": "c의 '크' 소리 + u의 이름 소리 '유' + t의 '트' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 큐트(cute)처럼 발음됩니다."
        },
    ],

    "④ 모음 예외": [
        {
            "word": "ball",
            "explain": "b의 '브' 소리 + all의 '올' 소리가 합쳐져서 볼(ball)처럼 발음됩니다."
        },
        {
            "word": "call",
            "explain": "c의 '크' 소리 + all의 '올' 소리가 합쳐져서 콜(call)처럼 발음됩니다."
        },
        {
            "word": "car",
            "explain": "c의 '크' 소리 + ar의 '아알' 소리가 합쳐져서 카알(car)처럼 발음됩니다."
        },
        {
            "word": "father",
            "explain": "f의 '프' 소리 + a의 '아' 소리 + th의 부드러운 'ㄷ' 소리 + er의 약한 '어' 소리가 합쳐져서 파더(father)처럼 발음됩니다."
        },
        {
            "word": "about",
            "explain": "a의 약한 '어' 소리 + b의 '브' 소리 + ou의 '아우' 소리 + t의 '트' 소리가 합쳐져서 어바웃(about)처럼 발음됩니다."
        },
        {
            "word": "love",
            "explain": "l의 '르' 소리 + o의 '어' 소리 + v의 '브' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 러브(love)처럼 발음됩니다."
        },
        {
            "word": "do",
            "explain": "d의 '드' 소리 + o의 긴 '우' 소리가 합쳐져서 두(do)처럼 발음됩니다."
        },
        {
            "word": "book",
            "explain": "b의 '브' 소리 + oo의 짧은 '우' 소리 + k의 '크' 소리가 합쳐져서 북(book)처럼 발음됩니다."
        },
        {
            "word": "moon",
            "explain": "m의 '므' 소리 + oo의 긴 '우' 소리 + n의 '느' 소리가 합쳐져서 문(moon)처럼 발음됩니다."
        },
        {
            "word": "bread",
            "explain": "b의 '브' 소리 + r의 '르' 소리 + ea의 '에' 소리 + d의 '드' 소리가 합쳐져서 브레드(bread)처럼 발음됩니다."
        },
    ],

    "⑤ Blends": [
        {
            "word": "black",
            "explain": "bl의 '블' 소리 + a의 '애' 소리 + ck의 '크' 소리가 합쳐져서 블랙(black)처럼 발음됩니다."
        },
        {
            "word": "brown",
            "explain": "br의 '브르' 소리 + ow의 '아우' 소리 + n의 '느' 소리가 합쳐져서 브라운(brown)처럼 발음됩니다."
        },
        {
            "word": "clock",
            "explain": "cl의 '클' 소리 + o의 '아/오' 소리 + ck의 '크' 소리가 합쳐져서 클락(clock)처럼 발음됩니다."
        },
        {
            "word": "crab",
            "explain": "cr의 '크르' 소리 + a의 '애' 소리 + b의 '브' 소리가 합쳐져서 크랩(crab)처럼 발음됩니다."
        },
        {
            "word": "drum",
            "explain": "dr의 '드르' 소리 + u의 '어' 소리 + m의 '므' 소리가 합쳐져서 드럼(drum)처럼 발음됩니다."
        },
        {
            "word": "flag",
            "explain": "fl의 '플' 소리 + a의 '애' 소리 + g의 '그' 소리가 합쳐져서 플래그(flag)처럼 발음됩니다."
        },
        {
            "word": "frog",
            "explain": "fr의 '프르' 소리 + o의 '아/오' 소리 + g의 '그' 소리가 합쳐져서 프락/프로그(frog)처럼 발음됩니다."
        },
        {
            "word": "green",
            "explain": "gr의 '그르' 소리 + ee의 긴 '이' 소리 + n의 '느' 소리가 합쳐져서 그린(green)처럼 발음됩니다."
        },
        {
            "word": "spoon",
            "explain": "sp의 '스프' 소리 + oo의 긴 '우' 소리 + n의 '느' 소리가 합쳐져서 스푼(spoon)처럼 발음됩니다."
        },
        {
            "word": "star",
            "explain": "st의 '스트' 소리 + ar의 '아알' 소리가 합쳐져서 스타알(star)처럼 발음됩니다."
        },
    ],

    "⑥ Digraphs": [
        {
            "word": "chair",
            "explain": "ch의 '치' 소리 + air의 '에어' 소리가 합쳐져서 체어(chair)처럼 발음됩니다."
        },
        {
            "word": "ship",
            "explain": "sh의 '쉬' 소리 + i의 짧은 '이' 소리 + p의 '프' 소리가 합쳐져서 쉽(ship)처럼 발음됩니다."
        },
        {
            "word": "three",
            "explain": "th의 혀를 살짝 내미는 '쓰' 소리 + r의 '르' 소리 + ee의 긴 '이' 소리가 합쳐져서 쓰리(three)처럼 발음됩니다."
        },
        {
            "word": "this",
            "explain": "th의 혀를 살짝 내미는 '드' 소리 + i의 짧은 '이' 소리 + s의 '스' 소리가 합쳐져서 디스(this)처럼 발음됩니다."
        },
        {
            "word": "phone",
            "explain": "ph의 '프' 소리 + o의 이름 소리 '오우' + n의 '느' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 포운(phone)처럼 발음됩니다."
        },
        {
            "word": "whale",
            "explain": "wh의 '우/워' 소리 + a의 이름 소리 '에이' + l의 '을' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 웨일(whale)처럼 발음됩니다."
        },
        {
            "word": "duck",
            "explain": "d의 '드' 소리 + u의 '어' 소리 + ck의 '크' 소리가 합쳐져서 덕(duck)처럼 발음됩니다."
        },
        {
            "word": "shop",
            "explain": "sh의 '쉬' 소리 + o의 '아/오' 소리 + p의 '프' 소리가 합쳐져서 샵(shop)처럼 발음됩니다."
        },
        {
            "word": "cheese",
            "explain": "ch의 '치' 소리 + ee의 긴 '이' 소리 + s의 '즈' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 치즈(cheese)처럼 발음됩니다."
        },
        {
            "word": "photo",
            "explain": "ph의 '프' 소리 + o의 '오우' 소리 + t의 '트' 소리 + o의 '오우' 소리가 합쳐져서 포토(photo)처럼 발음됩니다."
        },
    ],

    "⑦ Vowel Teams": [
        {
            "word": "rain",
            "explain": "r의 '르' 소리 + ai의 '에이' 소리 + n의 '느' 소리가 합쳐져서 레인(rain)처럼 발음됩니다."
        },
        {
            "word": "day",
            "explain": "d의 '드' 소리 + ay의 '에이' 소리가 합쳐져서 데이(day)처럼 발음됩니다."
        },
        {
            "word": "see",
            "explain": "s의 '스' 소리 + ee의 긴 '이' 소리가 합쳐져서 씨(see)처럼 발음됩니다."
        },
        {
            "word": "eat",
            "explain": "ea의 긴 '이' 소리 + t의 '트' 소리가 합쳐져서 잇(eat)처럼 발음됩니다."
        },
        {
            "word": "boat",
            "explain": "b의 '브' 소리 + oa의 '오우' 소리 + t의 '트' 소리가 합쳐져서 보우트(boat)처럼 발음됩니다."
        },
        {
            "word": "snow",
            "explain": "sn의 '스느' 소리 + ow의 '오우' 소리가 합쳐져서 스노우(snow)처럼 발음됩니다."
        },
        {
            "word": "cow",
            "explain": "c의 '크' 소리 + ow의 '아우' 소리가 합쳐져서 카우(cow)처럼 발음됩니다."
        },
        {
            "word": "house",
            "explain": "h의 '흐' 소리 + ou의 '아우' 소리 + s의 '스' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 하우스(house)처럼 발음됩니다."
        },
        {
            "word": "coin",
            "explain": "c의 '크' 소리 + oi의 '오이' 소리 + n의 '느' 소리가 합쳐져서 코인(coin)처럼 발음됩니다."
        },
        {
            "word": "boy",
            "explain": "b의 '브' 소리 + oy의 '오이' 소리가 합쳐져서 보이(boy)처럼 발음됩니다."
        },
    ],

    "⑧ R-Controlled": [
        {
            "word": "car",
            "explain": "c의 '크' 소리 + ar의 '아알' 소리가 합쳐져서 카알(car)처럼 발음됩니다."
        },
        {
            "word": "star",
            "explain": "st의 '스트' 소리 + ar의 '아알' 소리가 합쳐져서 스타알(star)처럼 발음됩니다."
        },
        {
            "word": "her",
            "explain": "h의 '흐' 소리 + er의 '얼' 소리가 합쳐져서 헐(her)처럼 발음됩니다."
        },
        {
            "word": "bird",
            "explain": "b의 '브' 소리 + ir의 '얼' 소리 + d의 '드' 소리가 합쳐져서 벌드(bird)처럼 발음됩니다."
        },
        {
            "word": "girl",
            "explain": "g의 '그' 소리 + ir의 '얼' 소리 + l의 '을' 소리가 합쳐져서 걸(girl)처럼 발음됩니다."
        },
        {
            "word": "corn",
            "explain": "c의 '크' 소리 + or의 '오얼' 소리 + n의 '느' 소리가 합쳐져서 코언(corn)처럼 발음됩니다."
        },
        {
            "word": "fork",
            "explain": "f의 '프' 소리 + or의 '오얼' 소리 + k의 '크' 소리가 합쳐져서 포크(fork)처럼 발음됩니다."
        },
        {
            "word": "turn",
            "explain": "t의 '트' 소리 + ur의 '얼' 소리 + n의 '느' 소리가 합쳐져서 턴(turn)처럼 발음됩니다."
        },
        {
            "word": "burn",
            "explain": "b의 '브' 소리 + ur의 '얼' 소리 + n의 '느' 소리가 합쳐져서 번(burn)처럼 발음됩니다."
        },
        {
            "word": "teacher",
            "explain": "t의 '트' 소리 + ea의 긴 '이' 소리 + ch의 '치' 소리 + er의 약한 '어' 소리가 합쳐져서 티처(teacher)처럼 발음됩니다."
        },
    ],

    "⑨ Silent e": [
        {
            "word": "cake",
            "explain": "c의 '크' 소리 + a의 이름 소리 '에이' + k의 '크' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 케이크(cake)처럼 발음됩니다."
        },
        {
            "word": "name",
            "explain": "n의 '느' 소리 + a의 이름 소리 '에이' + m의 '므' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 네임(name)처럼 발음됩니다."
        },
        {
            "word": "bike",
            "explain": "b의 '브' 소리 + i의 이름 소리 '아이' + k의 '크' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 바이크(bike)처럼 발음됩니다."
        },
        {
            "word": "five",
            "explain": "f의 '프' 소리 + i의 이름 소리 '아이' + v의 '브' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 파이브(five)처럼 발음됩니다."
        },
        {
            "word": "home",
            "explain": "h의 '흐' 소리 + o의 이름 소리 '오우' + m의 '므' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 호움(home)처럼 발음됩니다."
        },
        {
            "word": "rope",
            "explain": "r의 '르' 소리 + o의 이름 소리 '오우' + p의 '프' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 로우프(rope)처럼 발음됩니다."
        },
        {
            "word": "cube",
            "explain": "c의 '크' 소리 + u의 이름 소리 '유' + b의 '브' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 큐브(cube)처럼 발음됩니다."
        },
        {
            "word": "cute",
            "explain": "c의 '크' 소리 + u의 이름 소리 '유' + t의 '트' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 큐트(cute)처럼 발음됩니다."
        },
        {
            "word": "make",
            "explain": "m의 '므' 소리 + a의 이름 소리 '에이' + k의 '크' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 메이크(make)처럼 발음됩니다."
        },
        {
            "word": "hope",
            "explain": "h의 '흐' 소리 + o의 이름 소리 '오우' + p의 '프' 소리가 합쳐집니다. 끝의 e는 소리 나지 않아서 호우프(hope)처럼 발음됩니다."
        },
    ],
}


# =========================
# 말하기 연습 출력 함수
# =========================
def show_speaking_practice(tab_name, items):
    st.subheader(tab_name)

    st.markdown(
        """
        <div style="
            background-color:#f8fbff;
            border:1px solid #dbeafe;
            border-radius:16px;
            padding:14px 16px;
            margin-bottom:18px;
            line-height:1.7;
        ">
            👀 <b>단어를 보고 먼저 직접 읽어 보세요.</b><br>
            그 다음 원어민 발음을 듣고, 마지막으로 글자 소리가 어떻게 합쳐지는지 확인합니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, item in enumerate(items):
        word = item["word"]
        explain = item["explain"]

        st.markdown("---")

        col1, col2 = st.columns([2, 3])

        with col1:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #e0f2fe, #fef3c7);
                    border-radius:22px;
                    padding:30px 20px;
                    text-align:center;
                    box-shadow:0 4px 10px rgba(0,0,0,0.08);
                ">
                    <div style="font-size:18px; font-weight:700; color:#555;">
                        Word {i + 1}
                    </div>
                    <div style="font-size:52px; font-weight:900; color:#111827; margin-top:10px;">
                        {word}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown("### 1단계: 먼저 직접 말하기")
            st.write("스펠링을 보고 단어를 먼저 큰 소리로 읽어 보세요.")

            st.markdown("### 2단계: 원어민 발음 듣기")
            play_audio(word, key=f"{tab_name}_audio_{i}")

            st.markdown("### 3단계: 소리 이해하기")
            st.info(explain)


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(practice_sets.keys()))

for tab, tab_name in zip(tabs, practice_sets.keys()):
    with tab:
        show_speaking_practice(tab_name, practice_sets[tab_name])
