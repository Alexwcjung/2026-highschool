import streamlit as st
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Concept",
    page_icon="🔤",
    layout="wide"
)

st.title("🔤 Phonics Concept")
st.caption("알파벳 이름, 실제 소리, 예시 단어 발음을 듣고 익혀 봅시다.")

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


def audio_button(label, text, key):
    if st.button(label, key=key):
        audio_bytes = make_tts_audio(text)
        st.audio(audio_bytes, format="audio/mp3")


# 실제 소리 두 번 반복 + 간격 주기
def repeat_sound(sound_text):
    return f"{sound_text}. {sound_text}."


# =========================
# 데이터
# =========================

alphabet_sounds = [
    {
        "pattern": "B b",
        "concept": "Consonant sound",
        "sound_name": "/b/",
        "sound_audio": repeat_sound("buh"),
        "word": "bat",
        "word_audio": "bat"
    },
    {
        "pattern": "C c",
        "concept": "Consonant sound",
        "sound_name": "/k/",
        "sound_audio": repeat_sound("kuh"),
        "word": "cat",
        "word_audio": "cat"
    },
    {
        "pattern": "D d",
        "concept": "Consonant sound",
        "sound_name": "/d/",
        "sound_audio": repeat_sound("duh"),
        "word": "dog",
        "word_audio": "dog"
    },
    {
        "pattern": "F f",
        "concept": "Consonant sound",
        "sound_name": "/f/",
        "sound_audio": repeat_sound("fff"),
        "word": "fish",
        "word_audio": "fish"
    },
    {
        "pattern": "G g",
        "concept": "Consonant sound",
        "sound_name": "/g/",
        "sound_audio": repeat_sound("guh"),
        "word": "goat",
        "word_audio": "goat"
    },
    {
        "pattern": "H h",
        "concept": "Consonant sound",
        "sound_name": "/h/",
        "sound_audio": repeat_sound("huh"),
        "word": "hat",
        "word_audio": "hat"
    },
    {
        "pattern": "J j",
        "concept": "Consonant sound",
        "sound_name": "/j/",
        "sound_audio": repeat_sound("juh"),
        "word": "jam",
        "word_audio": "jam"
    },
    {
        "pattern": "K k",
        "concept": "Consonant sound",
        "sound_name": "/k/",
        "sound_audio": repeat_sound("kuh"),
        "word": "kite",
        "word_audio": "kite"
    },
    {
        "pattern": "L l",
        "concept": "Consonant sound",
        "sound_name": "/l/",
        "sound_audio": repeat_sound("lll"),
        "word": "lion",
        "word_audio": "lion"
    },
    {
        "pattern": "M m",
        "concept": "Consonant sound",
        "sound_name": "/m/",
        "sound_audio": repeat_sound("mmm"),
        "word": "moon",
        "word_audio": "moon"
    },
    {
        "pattern": "N n",
        "concept": "Consonant sound",
        "sound_name": "/n/",
        "sound_audio": repeat_sound("nnn"),
        "word": "nest",
        "word_audio": "nest"
    },
    {
        "pattern": "P p",
        "concept": "Consonant sound",
        "sound_name": "/p/",
        "sound_audio": repeat_sound("puh"),
        "word": "pig",
        "word_audio": "pig"
    },
    {
        "pattern": "Q q",
        "concept": "Usually /kw/",
        "sound_name": "/kw/",
        "sound_audio": repeat_sound("kwuh"),
        "word": "queen",
        "word_audio": "queen"
    },
    {
        "pattern": "R r",
        "concept": "Consonant sound",
        "sound_name": "/r/",
        "sound_audio": repeat_sound("ruh"),
        "word": "red",
        "word_audio": "red"
    },
    {
        "pattern": "S s",
        "concept": "Consonant sound",
        "sound_name": "/s/",
        "sound_audio": repeat_sound("sss"),
        "word": "sun",
        "word_audio": "sun"
    },
    {
        "pattern": "T t",
        "concept": "Consonant sound",
        "sound_name": "/t/",
        "sound_audio": repeat_sound("tuh"),
        "word": "top",
        "word_audio": "top"
    },
    {
        "pattern": "V v",
        "concept": "Consonant sound",
        "sound_name": "/v/",
        "sound_audio": repeat_sound("vvv"),
        "word": "van",
        "word_audio": "van"
    },
    {
        "pattern": "W w",
        "concept": "Consonant sound",
        "sound_name": "/w/",
        "sound_audio": repeat_sound("wuh"),
        "word": "window",
        "word_audio": "window"
    },
    {
        "pattern": "X x",
        "concept": "Often /ks/",
        "sound_name": "/ks/",
        "sound_audio": repeat_sound("ks"),
        "word": "fox",
        "word_audio": "fox"
    },
    {
        "pattern": "Y y",
        "concept": "Consonant sound",
        "sound_name": "/y/",
        "sound_audio": repeat_sound("yuh"),
        "word": "yes",
        "word_audio": "yes"
    },
    {
        "pattern": "Z z",
        "concept": "Consonant sound",
        "sound_name": "/z/",
        "sound_audio": repeat_sound("zzz"),
        "word": "zebra",
        "word_audio": "zebra"
    },
]


short_vowels = [
    {
        "pattern": "A a",
        "concept": "Short vowel",
        "sound_name": "Short a /æ/",
        "sound_audio": repeat_sound("a"),
        "word": "apple",
        "word_audio": "apple"
    },
    {
        "pattern": "E e",
        "concept": "Short vowel",
        "sound_name": "Short e /e/",
        "sound_audio": repeat_sound("eh"),
        "word": "egg",
        "word_audio": "egg"
    },
    {
        "pattern": "I i",
        "concept": "Short vowel",
        "sound_name": "Short i /ɪ/",
        "sound_audio": repeat_sound("ih"),
        "word": "igloo",
        "word_audio": "igloo"
    },
    {
        "pattern": "O o",
        "concept": "Short vowel",
        "sound_name": "Short o /ɑ/",
        "sound_audio": repeat_sound("ah"),
        "word": "octopus",
        "word_audio": "octopus"
    },
    {
        "pattern": "U u",
        "concept": "Short vowel",
        "sound_name": "Short u /ʌ/",
        "sound_audio": repeat_sound("uh"),
        "word": "umbrella",
        "word_audio": "umbrella"
    },
]


long_vowels = [
    {
        "pattern": "A a",
        "concept": "Long vowel",
        "sound_name": "Long a /eɪ/",
        "sound_audio": repeat_sound("ay"),
        "word": "cake",
        "word_audio": "cake"
    },
    {
        "pattern": "E e",
        "concept": "Long vowel",
        "sound_name": "Long e /iː/",
        "sound_audio": repeat_sound("ee"),
        "word": "tree",
        "word_audio": "tree"
    },
    {
        "pattern": "I i",
        "concept": "Long vowel",
        "sound_name": "Long i /aɪ/",
        "sound_audio": repeat_sound("eye"),
        "word": "bike",
        "word_audio": "bike"
    },
    {
        "pattern": "O o",
        "concept": "Long vowel",
        "sound_name": "Long o /oʊ/",
        "sound_audio": repeat_sound("oh"),
        "word": "rope",
        "word_audio": "rope"
    },
    {
        "pattern": "U u",
        "concept": "Long vowel",
        "sound_name": "Long u /juː/",
        "sound_audio": repeat_sound("you"),
        "word": "cube",
        "word_audio": "cube"
    },
]


vowel_exceptions = [
    {
        "pattern": "A a",
        "concept": "Exception",
        "sound_name": "A as /ɑː/",
        "sound_audio": repeat_sound("ah"),
        "word": "father",
        "word_audio": "father"
    },
    {
        "pattern": "A a",
        "concept": "Exception",
        "sound_name": "A as /ɔː/",
        "sound_audio": repeat_sound("aw"),
        "word": "ball",
        "word_audio": "ball"
    },
    {
        "pattern": "A a",
        "concept": "Exception",
        "sound_name": "A as /ə/",
        "sound_audio": repeat_sound("uh"),
        "word": "about",
        "word_audio": "about"
    },
    {
        "pattern": "O o",
        "concept": "Exception",
        "sound_name": "O as /ʌ/",
        "sound_audio": repeat_sound("uh"),
        "word": "love",
        "word_audio": "love"
    },
    {
        "pattern": "O o",
        "concept": "Exception",
        "sound_name": "O as /uː/",
        "sound_audio": repeat_sound("oo"),
        "word": "do",
        "word_audio": "do"
    },
    {
        "pattern": "OO",
        "concept": "Exception",
        "sound_name": "OO as /ʊ/",
        "sound_audio": repeat_sound("u"),
        "word": "book",
        "word_audio": "book"
    },
    {
        "pattern": "OO",
        "concept": "Exception",
        "sound_name": "OO as /uː/",
        "sound_audio": repeat_sound("oo"),
        "word": "moon",
        "word_audio": "moon"
    },
    {
        "pattern": "EA",
        "concept": "Exception",
        "sound_name": "EA as /e/",
        "sound_audio": repeat_sound("eh"),
        "word": "bread",
        "word_audio": "bread"
    },
]


blends = [
    {
        "pattern": "bl",
        "concept": "Consonant blend",
        "sound_name": "bl",
        "sound_audio": repeat_sound("bl"),
        "word": "black",
        "word_audio": "black"
    },
    {
        "pattern": "br",
        "concept": "Consonant blend",
        "sound_name": "br",
        "sound_audio": repeat_sound("br"),
        "word": "brown",
        "word_audio": "brown"
    },
    {
        "pattern": "cl",
        "concept": "Consonant blend",
        "sound_name": "cl",
        "sound_audio": repeat_sound("cl"),
        "word": "clock",
        "word_audio": "clock"
    },
    {
        "pattern": "cr",
        "concept": "Consonant blend",
        "sound_name": "cr",
        "sound_audio": repeat_sound("cr"),
        "word": "crab",
        "word_audio": "crab"
    },
    {
        "pattern": "dr",
        "concept": "Consonant blend",
        "sound_name": "dr",
        "sound_audio": repeat_sound("dr"),
        "word": "drum",
        "word_audio": "drum"
    },
    {
        "pattern": "fl",
        "concept": "Consonant blend",
        "sound_name": "fl",
        "sound_audio": repeat_sound("fl"),
        "word": "flag",
        "word_audio": "flag"
    },
    {
        "pattern": "fr",
        "concept": "Consonant blend",
        "sound_name": "fr",
        "sound_audio": repeat_sound("fr"),
        "word": "frog",
        "word_audio": "frog"
    },
    {
        "pattern": "gl",
        "concept": "Consonant blend",
        "sound_name": "gl",
        "sound_audio": repeat_sound("gl"),
        "word": "glass",
        "word_audio": "glass"
    },
    {
        "pattern": "gr",
        "concept": "Consonant blend",
        "sound_name": "gr",
        "sound_audio": repeat_sound("gr"),
        "word": "green",
        "word_audio": "green"
    },
    {
        "pattern": "pl",
        "concept": "Consonant blend",
        "sound_name": "pl",
        "sound_audio": repeat_sound("pl"),
        "word": "plane",
        "word_audio": "plane"
    },
    {
        "pattern": "pr",
        "concept": "Consonant blend",
        "sound_name": "pr",
        "sound_audio": repeat_sound("pr"),
        "word": "present",
        "word_audio": "present"
    },
    {
        "pattern": "sk",
        "concept": "Consonant blend",
        "sound_name": "sk",
        "sound_audio": repeat_sound("sk"),
        "word": "skate",
        "word_audio": "skate"
    },
    {
        "pattern": "sl",
        "concept": "Consonant blend",
        "sound_name": "sl",
        "sound_audio": repeat_sound("sl"),
        "word": "sleep",
        "word_audio": "sleep"
    },
    {
        "pattern": "sm",
        "concept": "Consonant blend",
        "sound_name": "sm",
        "sound_audio": repeat_sound("sm"),
        "word": "smile",
        "word_audio": "smile"
    },
    {
        "pattern": "sn",
        "concept": "Consonant blend",
        "sound_name": "sn",
        "sound_audio": repeat_sound("sn"),
        "word": "snake",
        "word_audio": "snake"
    },
    {
        "pattern": "sp",
        "concept": "Consonant blend",
        "sound_name": "sp",
        "sound_audio": repeat_sound("sp"),
        "word": "spoon",
        "word_audio": "spoon"
    },
    {
        "pattern": "st",
        "concept": "Consonant blend",
        "sound_name": "st",
        "sound_audio": repeat_sound("st"),
        "word": "star",
        "word_audio": "star"
    },
    {
        "pattern": "tr",
        "concept": "Consonant blend",
        "sound_name": "tr",
        "sound_audio": repeat_sound("tr"),
        "word": "tree",
        "word_audio": "tree"
    },
]


digraphs = [
    {
        "pattern": "ch",
        "concept": "Consonant digraph",
        "sound_name": "/tʃ/",
        "sound_audio": repeat_sound("ch"),
        "word": "chair",
        "word_audio": "chair"
    },
    {
        "pattern": "sh",
        "concept": "Consonant digraph",
        "sound_name": "/ʃ/",
        "sound_audio": repeat_sound("sh"),
        "word": "ship",
        "word_audio": "ship"
    },
    {
        "pattern": "th",
        "concept": "Consonant digraph",
        "sound_name": "Voiceless th /θ/",
        "sound_audio": repeat_sound("th"),
        "word": "three",
        "word_audio": "three"
    },
    {
        "pattern": "th",
        "concept": "Consonant digraph",
        "sound_name": "Voiced th /ð/",
        "sound_audio": repeat_sound("th"),
        "word": "this",
        "word_audio": "this"
    },
    {
        "pattern": "wh",
        "concept": "Consonant digraph",
        "sound_name": "/w/",
        "sound_audio": repeat_sound("wuh"),
        "word": "whale",
        "word_audio": "whale"
    },
    {
        "pattern": "ph",
        "concept": "Consonant digraph",
        "sound_name": "/f/",
        "sound_audio": repeat_sound("fff"),
        "word": "phone",
        "word_audio": "phone"
    },
    {
        "pattern": "ck",
        "concept": "Consonant digraph",
        "sound_name": "/k/",
        "sound_audio": repeat_sound("kuh"),
        "word": "duck",
        "word_audio": "duck"
    },
]


vowel_teams = [
    {
        "pattern": "ai",
        "concept": "Vowel team",
        "sound_name": "/eɪ/",
        "sound_audio": repeat_sound("ay"),
        "word": "rain",
        "word_audio": "rain"
    },
    {
        "pattern": "ay",
        "concept": "Vowel team",
        "sound_name": "/eɪ/",
        "sound_audio": repeat_sound("ay"),
        "word": "day",
        "word_audio": "day"
    },
    {
        "pattern": "ee",
        "concept": "Vowel team",
        "sound_name": "/iː/",
        "sound_audio": repeat_sound("ee"),
        "word": "see",
        "word_audio": "see"
    },
    {
        "pattern": "ea",
        "concept": "Vowel team",
        "sound_name": "/iː/",
        "sound_audio": repeat_sound("ee"),
        "word": "eat",
        "word_audio": "eat"
    },
    {
        "pattern": "oa",
        "concept": "Vowel team",
        "sound_name": "/oʊ/",
        "sound_audio": repeat_sound("oh"),
        "word": "boat",
        "word_audio": "boat"
    },
    {
        "pattern": "ow",
        "concept": "Vowel team",
        "sound_name": "/oʊ/",
        "sound_audio": repeat_sound("oh"),
        "word": "snow",
        "word_audio": "snow"
    },
    {
        "pattern": "ow",
        "concept": "Vowel team",
        "sound_name": "/aʊ/",
        "sound_audio": repeat_sound("ow"),
        "word": "cow",
        "word_audio": "cow"
    },
    {
        "pattern": "ou",
        "concept": "Vowel team",
        "sound_name": "/aʊ/",
        "sound_audio": repeat_sound("ow"),
        "word": "house",
        "word_audio": "house"
    },
    {
        "pattern": "oi",
        "concept": "Vowel team",
        "sound_name": "/ɔɪ/",
        "sound_audio": repeat_sound("oy"),
        "word": "coin",
        "word_audio": "coin"
    },
    {
        "pattern": "oy",
        "concept": "Vowel team",
        "sound_name": "/ɔɪ/",
        "sound_audio": repeat_sound("oy"),
        "word": "boy",
        "word_audio": "boy"
    },
]


r_controlled = [
    {
        "pattern": "ar",
        "concept": "R-controlled vowel",
        "sound_name": "/ɑːr/",
        "sound_audio": repeat_sound("ar"),
        "word": "car",
        "word_audio": "car"
    },
    {
        "pattern": "er",
        "concept": "R-controlled vowel",
        "sound_name": "/ɜːr/",
        "sound_audio": repeat_sound("er"),
        "word": "her",
        "word_audio": "her"
    },
    {
        "pattern": "ir",
        "concept": "R-controlled vowel",
        "sound_name": "/ɜːr/",
        "sound_audio": repeat_sound("er"),
        "word": "bird",
        "word_audio": "bird"
    },
    {
        "pattern": "or",
        "concept": "R-controlled vowel",
        "sound_name": "/ɔːr/",
        "sound_audio": repeat_sound("or"),
        "word": "corn",
        "word_audio": "corn"
    },
    {
        "pattern": "ur",
        "concept": "R-controlled vowel",
        "sound_name": "/ɜːr/",
        "sound_audio": repeat_sound("er"),
        "word": "turn",
        "word_audio": "turn"
    },
]


silent_e = [
    {
        "pattern": "a_e",
        "concept": "Silent e",
        "sound_name": "Long a /eɪ/",
        "sound_audio": repeat_sound("ay"),
        "word": "cake",
        "word_audio": "cake"
    },
    {
        "pattern": "i_e",
        "concept": "Silent e",
        "sound_name": "Long i /aɪ/",
        "sound_audio": repeat_sound("eye"),
        "word": "bike",
        "word_audio": "bike"
    },
    {
        "pattern": "o_e",
        "concept": "Silent e",
        "sound_name": "Long o /oʊ/",
        "sound_audio": repeat_sound("oh"),
        "word": "home",
        "word_audio": "home"
    },
    {
        "pattern": "u_e",
        "concept": "Silent e",
        "sound_name": "Long u /juː/",
        "sound_audio": repeat_sound("you"),
        "word": "cube",
        "word_audio": "cube"
    },
]


# =========================
# 화면 출력 함수
# =========================
def show_cards(data, title, description):
    st.subheader(title)
    st.info(description)

    st.markdown(
        """
        <style>
        .phonics-card {
            border: 1px solid #e8e8e8;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 14px;
            background: #fafafa;
        }
        .pattern-box {
            font-size: 34px;
            font-weight: 900;
            color: #222222;
        }
        .label-small {
            font-size: 13px;
            color: #777777;
            margin-bottom: 4px;
        }
        .concept-box {
            font-size: 16px;
            font-weight: 700;
            color: #444444;
        }
        .sound-box {
            font-size: 18px;
            font-weight: 800;
            color: #222222;
        }
        .word-box {
            font-size: 24px;
            font-weight: 900;
            color: #222222;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for idx, item in enumerate(data):
        st.markdown('<div class="phonics-card">', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns([1.1, 1.5, 1.7, 1.7])

        with col1:
            st.markdown("<div class='label-small'>글자 / 패턴</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='pattern-box'>{item['pattern']}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='label-small'>개념</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='concept-box'>{item['concept']}</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='label-small'>실제 소리</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='sound-box'>{item['sound_name']}</div>", unsafe_allow_html=True)
            audio_button(
                "🔊 실제 소리 듣기",
                item["sound_audio"],
                key=f"sound_{title}_{idx}_{item['pattern']}_{item['word']}"
            )

        with col4:
            st.markdown("<div class='label-small'>예시 단어</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='word-box'>{item['word']}</div>", unsafe_allow_html=True)
            audio_button(
                "🔊 단어 듣기",
                item["word_audio"],
                key=f"word_{title}_{idx}_{item['pattern']}_{item['word']}"
            )

        st.markdown('</div>', unsafe_allow_html=True)


# =========================
# 탭 구성
# =========================
tabs = st.tabs([
    "① 알파벳 기본 소리",
    "② 단모음",
    "③ 장모음",
    "④ 모음 예외",
    "⑤ Blends",
    "⑥ Digraphs",
    "⑦ Vowel Teams",
    "⑧ R-Controlled",
    "⑨ Silent e"
])

with tabs[0]:
    show_cards(
        alphabet_sounds,
        "① 알파벳 기본 소리",
        "알파벳 이름과 실제 소리는 다릅니다. 예: B의 이름은 bee이지만 실제 소리는 /b/입니다."
    )

with tabs[1]:
    show_cards(
        short_vowels,
        "② 단모음 Short Vowels",
        "단모음은 짧게 나는 모음 소리입니다. 버튼을 누르면 'short a'라고 읽지 않고 실제 영어 소리만 두 번 들려줍니다."
    )

with tabs[2]:
    show_cards(
        long_vowels,
        "③ 장모음 Long Vowels",
        "장모음은 대체로 알파벳 이름과 비슷하게 나는 모음 소리입니다."
    )

with tabs[3]:
    show_cards(
        vowel_exceptions,
        "④ 모음 예외 소리",
        "모음은 단모음, 장모음 외에도 예외적인 소리가 있습니다. 화면에는 설명이 보이지만, 오디오는 실제 소리만 들려줍니다."
    )

with tabs[4]:
    show_cards(
        blends,
        "⑤ Consonant Blends",
        "Blends는 두 자음이 이어지지만 각각의 소리가 어느 정도 살아 있는 소리입니다. 예: bl, br, st, tr"
    )

with tabs[5]:
    show_cards(
        digraphs,
        "⑥ Consonant Digraphs",
        "Digraphs는 두 글자가 만나 하나의 새로운 소리를 만드는 경우입니다. 예: ch, sh, th, ph"
    )

with tabs[6]:
    show_cards(
        vowel_teams,
        "⑦ Vowel Teams",
        "Vowel Teams는 두 모음 글자가 함께 하나의 모음 소리를 만드는 경우입니다. 예: ai, ee, oa, ou"
    )

with tabs[7]:
    show_cards(
        r_controlled,
        "⑧ R-Controlled Vowels",
        "R-controlled vowels는 모음 뒤에 r이 와서 모음 소리가 달라지는 경우입니다. 예: ar, er, ir, or, ur"
    )

with tabs[8]:
    show_cards(
        silent_e,
        "⑨ Silent e",
        "Silent e는 단어 끝의 e가 직접 소리 나지는 않지만 앞의 모음을 장모음으로 바꾸는 경우입니다. 예: cake, bike, home"
    )
