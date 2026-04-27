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
    """
    text를 영어 음성 mp3로 변환
    tld='com'은 미국식 영어에 가까움
    """
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def audio_button(label, text, key):
    """
    버튼을 누르면 해당 text를 영어 음성으로 재생
    """
    if st.button(label, key=key):
        audio_bytes = make_tts_audio(text)
        st.audio(audio_bytes, format="audio/mp3")


# =========================
# 데이터
# =========================

consonants = [
    {
        "letter": "B b",
        "name": "bee",
        "sound_name": "/b/",
        "sound_audio": "buh buh",
        "word": "bat",
        "word_audio": "bat"
    },
    {
        "letter": "C c",
        "name": "see",
        "sound_name": "/k/",
        "sound_audio": "kuh kuh",
        "word": "cat",
        "word_audio": "cat"
    },
    {
        "letter": "D d",
        "name": "dee",
        "sound_name": "/d/",
        "sound_audio": "duh duh",
        "word": "dog",
        "word_audio": "dog"
    },
    {
        "letter": "F f",
        "name": "eff",
        "sound_name": "/f/",
        "sound_audio": "fff fff",
        "word": "fish",
        "word_audio": "fish"
    },
    {
        "letter": "G g",
        "name": "gee",
        "sound_name": "/g/",
        "sound_audio": "guh guh",
        "word": "goat",
        "word_audio": "goat"
    },
    {
        "letter": "H h",
        "name": "aitch",
        "sound_name": "/h/",
        "sound_audio": "huh huh",
        "word": "hat",
        "word_audio": "hat"
    },
    {
        "letter": "J j",
        "name": "jay",
        "sound_name": "/dʒ/",
        "sound_audio": "juh juh",
        "word": "jam",
        "word_audio": "jam"
    },
    {
        "letter": "K k",
        "name": "kay",
        "sound_name": "/k/",
        "sound_audio": "kuh kuh",
        "word": "kite",
        "word_audio": "kite"
    },
    {
        "letter": "L l",
        "name": "el",
        "sound_name": "/l/",
        "sound_audio": "lll lll",
        "word": "lion",
        "word_audio": "lion"
    },
    {
        "letter": "M m",
        "name": "em",
        "sound_name": "/m/",
        "sound_audio": "mmm mmm",
        "word": "moon",
        "word_audio": "moon"
    },
    {
        "letter": "N n",
        "name": "en",
        "sound_name": "/n/",
        "sound_audio": "nnn nnn",
        "word": "nose",
        "word_audio": "nose"
    },
    {
        "letter": "P p",
        "name": "pee",
        "sound_name": "/p/",
        "sound_audio": "puh puh",
        "word": "pig",
        "word_audio": "pig"
    },
    {
        "letter": "Q q",
        "name": "cue",
        "sound_name": "/kw/",
        "sound_audio": "kwuh kwuh",
        "word": "queen",
        "word_audio": "queen"
    },
    {
        "letter": "R r",
        "name": "ar",
        "sound_name": "/r/",
        "sound_audio": "ruh ruh",
        "word": "red",
        "word_audio": "red"
    },
    {
        "letter": "S s",
        "name": "ess",
        "sound_name": "/s/",
        "sound_audio": "sss sss",
        "word": "sun",
        "word_audio": "sun"
    },
    {
        "letter": "T t",
        "name": "tee",
        "sound_name": "/t/",
        "sound_audio": "tuh tuh",
        "word": "top",
        "word_audio": "top"
    },
    {
        "letter": "V v",
        "name": "vee",
        "sound_name": "/v/",
        "sound_audio": "vvv vvv",
        "word": "van",
        "word_audio": "van"
    },
    {
        "letter": "W w",
        "name": "double you",
        "sound_name": "/w/",
        "sound_audio": "wuh wuh",
        "word": "window",
        "word_audio": "window"
    },
    {
        "letter": "X x",
        "name": "ex",
        "sound_name": "/ks/",
        "sound_audio": "ks ks",
        "word": "fox",
        "word_audio": "fox"
    },
    {
        "letter": "Y y",
        "name": "why",
        "sound_name": "/j/",
        "sound_audio": "yuh yuh",
        "word": "yes",
        "word_audio": "yes"
    },
    {
        "letter": "Z z",
        "name": "zee",
        "sound_name": "/z/",
        "sound_audio": "zzz zzz",
        "word": "zebra",
        "word_audio": "zebra"
    },
]

short_vowels = [
    {
        "letter": "A a",
        "name": "ay",
        "sound_name": "Short a /æ/",
        "sound_audio": "ă ă",
        "word": "apple",
        "word_audio": "apple"
    },
    {
        "letter": "E e",
        "name": "ee",
        "sound_name": "Short e /e/",
        "sound_audio": "eh eh",
        "word": "egg",
        "word_audio": "egg"
    },
    {
        "letter": "I i",
        "name": "eye",
        "sound_name": "Short i /ɪ/",
        "sound_audio": "ih ih",
        "word": "igloo",
        "word_audio": "igloo"
    },
    {
        "letter": "O o",
        "name": "oh",
        "sound_name": "Short o /ɑ/",
        "sound_audio": "ŏ ŏ",
        "word": "octopus",
        "word_audio": "octopus"
    },
    {
        "letter": "U u",
        "name": "you",
        "sound_name": "Short u /ʌ/",
        "sound_audio": "uh uh",
        "word": "umbrella",
        "word_audio": "umbrella"
    },
]

long_vowels = [
    {
        "letter": "A a",
        "name": "ay",
        "sound_name": "Long a /eɪ/",
        "sound_audio": "ay ay",
        "word": "cake",
        "word_audio": "cake"
    },
    {
        "letter": "E e",
        "name": "ee",
        "sound_name": "Long e /iː/",
        "sound_audio": "ee ee",
        "word": "tree",
        "word_audio": "tree"
    },
    {
        "letter": "I i",
        "name": "eye",
        "sound_name": "Long i /aɪ/",
        "sound_audio": "eye eye",
        "word": "bike",
        "word_audio": "bike"
    },
    {
        "letter": "O o",
        "name": "oh",
        "sound_name": "Long o /oʊ/",
        "sound_audio": "oh oh",
        "word": "rope",
        "word_audio": "rope"
    },
    {
        "letter": "U u",
        "name": "you",
        "sound_name": "Long u /juː/",
        "sound_audio": "you you",
        "word": "cube",
        "word_audio": "cube"
    },
]

vowel_exceptions = [
    {
        "letter": "A a",
        "name": "ay",
        "sound_name": "A as /ɑː/",
        "sound_audio": "ah ah",
        "word": "father",
        "word_audio": "father"
    },
    {
        "letter": "A a",
        "name": "ay",
        "sound_name": "A as /ɔː/",
        "sound_audio": "aw aw",
        "word": "ball",
        "word_audio": "ball"
    },
    {
        "letter": "A a",
        "name": "ay",
        "sound_name": "A as /ə/",
        "sound_audio": "uh uh",
        "word": "about",
        "word_audio": "about"
    },
    {
        "letter": "E e",
        "name": "ee",
        "sound_name": "E as silent",
        "sound_audio": "make",
        "word": "make",
        "word_audio": "make"
    },
    {
        "letter": "O o",
        "name": "oh",
        "sound_name": "O as /ʌ/",
        "sound_audio": "uh uh",
        "word": "love",
        "word_audio": "love"
    },
    {
        "letter": "O o",
        "name": "oh",
        "sound_name": "O as /uː/",
        "sound_audio": "oo oo",
        "word": "do",
        "word_audio": "do"
    },
    {
        "letter": "OO",
        "name": "double o",
        "sound_name": "OO as /ʊ/",
        "sound_audio": "oo oo",
        "word": "book",
        "word_audio": "book"
    },
    {
        "letter": "OO",
        "name": "double o",
        "sound_name": "OO as /uː/",
        "sound_audio": "oo oo",
        "word": "moon",
        "word_audio": "moon"
    },
    {
        "letter": "EA",
        "name": "e a",
        "sound_name": "EA as /iː/",
        "sound_audio": "ee ee",
        "word": "eat",
        "word_audio": "eat"
    },
    {
        "letter": "EA",
        "name": "e a",
        "sound_name": "EA as /e/",
        "sound_audio": "eh eh",
        "word": "bread",
        "word_audio": "bread"
    },
    {
        "letter": "OW",
        "name": "o w",
        "sound_name": "OW as /aʊ/",
        "sound_audio": "ow ow",
        "word": "cow",
        "word_audio": "cow"
    },
    {
        "letter": "OW",
        "name": "o w",
        "sound_name": "OW as /oʊ/",
        "sound_audio": "oh oh",
        "word": "snow",
        "word_audio": "snow"
    },
]

# =========================
# 표 출력 함수
# =========================
def show_phonics_table(data, title):
    st.subheader(title)

    st.markdown(
        """
        <style>
        .phonics-card {
            border: 1px solid #e6e6e6;
            border-radius: 14px;
            padding: 16px;
            margin-bottom: 12px;
            background-color: #fafafa;
        }
        .letter-box {
            font-size: 30px;
            font-weight: 800;
        }
        .small-label {
            color: #666666;
            font-size: 14px;
        }
        .sound-name {
            font-size: 18px;
            font-weight: 700;
        }
        .word-box {
            font-size: 22px;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for idx, item in enumerate(data):
        with st.container():
            st.markdown('<div class="phonics-card">', unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns([1.1, 1.4, 1.6, 1.6])

            with col1:
                st.markdown(f"<div class='small-label'>글자</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='letter-box'>{item['letter']}</div>", unsafe_allow_html=True)

            with col2:
                st.markdown(f"<div class='small-label'>알파벳 이름</div>", unsafe_allow_html=True)
                st.markdown(f"**{item['name']}**")
                audio_button(
                    "🔊 이름 듣기",
                    item["name"],
                    key=f"name_{title}_{idx}_{item['letter']}_{item['word']}"
                )

            with col3:
                st.markdown(f"<div class='small-label'>실제 소리</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='sound-name'>{item['sound_name']}</div>", unsafe_allow_html=True)
                audio_button(
                    "🔊 실제 소리 듣기",
                    item["sound_audio"],
                    key=f"sound_{title}_{idx}_{item['letter']}_{item['word']}"
                )

            with col4:
                st.markdown(f"<div class='small-label'>예시 단어</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='word-box'>{item['word']}</div>", unsafe_allow_html=True)
                audio_button(
                    "🔊 단어 듣기",
                    item["word_audio"],
                    key=f"word_{title}_{idx}_{item['letter']}_{item['word']}"
                )

            st.markdown('</div>', unsafe_allow_html=True)


# =========================
# 탭 구성
# =========================
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "① 자음 소리",
        "② 단모음 Short Vowels",
        "③ 장모음 Long Vowels",
        "④ 모음 예외 소리"
    ]
)

with tab1:
    st.info("알파벳 이름과 실제 자음 소리는 다릅니다. 예: B의 이름은 bee, 실제 소리는 /b/입니다.")
    show_phonics_table(consonants, "자음 소리")

with tab2:
    st.info("단모음은 짧게 나는 모음 소리입니다. 버튼을 누르면 'short a'라고 읽지 않고 실제 소리를 들려줍니다.")
    show_phonics_table(short_vowels, "단모음 Short Vowels")

with tab3:
    st.info("장모음은 보통 알파벳 이름과 비슷하게 나는 소리입니다.")
    show_phonics_table(long_vowels, "장모음 Long Vowels")

with tab4:
    st.info("모음은 단모음, 장모음 외에도 예외적인 소리가 있습니다. 설명은 화면에만 보이고, 오디오는 실제 소리 중심으로 재생됩니다.")
    show_phonics_table(vowel_exceptions, "모음 예외 소리")
