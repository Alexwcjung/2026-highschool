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
st.caption("스펠링을 보고 먼저 말한 뒤, 원어민 발음을 듣고, 단어의 소리를 이해해 봅시다.")

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
        <div>👀 화면에 보이는 <b>영어 단어</b>를 먼저 큰 소리로 읽습니다.</div>
        <div>🔊 <b>원어민 발음 듣기</b> 버튼을 눌러 실제 발음을 확인합니다.</div>
        <div>💡 아래 설명을 보며 <b>단어의 소리를 이해해 봅니다.</b></div>
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
        {"word": "bat", "explain": "b의 /b/ 소리 + a의 짧은 '애' 소리 + t의 /t/ 소리가 합쳐진 단어입니다."},
        {"word": "cat", "explain": "c의 /k/ 소리 + a의 짧은 '애' 소리 + t의 /t/ 소리가 합쳐진 단어입니다."},
        {"word": "dog", "explain": "d의 /d/ 소리 + o의 짧은 모음 소리 + g의 /g/ 소리가 합쳐진 단어입니다."},
        {"word": "fish", "explain": "f의 /f/ 소리와 sh의 /ʃ/ 소리를 함께 연습할 수 있는 단어입니다."},
        {"word": "goat", "explain": "g의 /g/ 소리와 oa의 긴 o 소리를 함께 연습할 수 있는 단어입니다."},
        {"word": "hat", "explain": "h의 숨소리 /h/와 짧은 a 소리를 연습할 수 있는 단어입니다."},
        {"word": "jam", "explain": "j의 /dʒ/ 소리와 짧은 a 소리를 연습할 수 있는 단어입니다."},
        {"word": "sun", "explain": "s의 /s/ 소리와 u의 짧은 '어' 소리를 연습할 수 있는 단어입니다."},
        {"word": "van", "explain": "v의 /v/ 소리를 연습할 수 있는 단어입니다. f와 달리 목소리가 울립니다."},
        {"word": "yes", "explain": "y가 단어 앞에서 /j/ 소리로 나는 것을 연습할 수 있는 단어입니다."},
    ],

    "② 짧은 모음": [
        {"word": "apple", "explain": "a가 짧은 /æ/ 소리로 나는 단어입니다."},
        {"word": "cat", "explain": "a가 짧은 '애' 소리로 나는 CVC 단어입니다."},
        {"word": "egg", "explain": "e가 짧은 /e/ 소리로 나는 단어입니다."},
        {"word": "bed", "explain": "e가 짧은 '에' 소리로 나는 CVC 단어입니다."},
        {"word": "sit", "explain": "i가 짧은 /ɪ/ 소리로 나는 단어입니다."},
        {"word": "pig", "explain": "i가 짧은 '이'에 가까운 소리로 나는 단어입니다."},
        {"word": "hot", "explain": "o가 짧은 모음 소리로 나는 단어입니다."},
        {"word": "cup", "explain": "u가 짧은 /ʌ/ 소리로 나는 단어입니다."},
        {"word": "bus", "explain": "u가 짧은 '어' 소리로 나는 단어입니다."},
        {"word": "fox", "explain": "o의 짧은 모음 소리와 x의 /ks/ 소리를 함께 연습할 수 있는 단어입니다."},
    ],

    "③ 긴 모음": [
        {"word": "cake", "explain": "a가 긴 모음 /eɪ/ 소리로 납니다. 끝의 e는 소리 나지 않습니다."},
        {"word": "name", "explain": "a_e 구조로 a가 이름 소리 /eɪ/로 납니다."},
        {"word": "tree", "explain": "ee가 긴 /iː/ 소리로 나는 단어입니다."},
        {"word": "see", "explain": "ee가 긴 '이' 소리로 나는 단어입니다."},
        {"word": "bike", "explain": "i_e 구조로 i가 긴 /aɪ/ 소리로 납니다."},
        {"word": "five", "explain": "i가 이름 소리 /aɪ/로 나는 단어입니다. 끝의 e는 소리 나지 않습니다."},
        {"word": "rope", "explain": "o_e 구조로 o가 긴 /oʊ/ 소리로 납니다."},
        {"word": "home", "explain": "o가 긴 '오우' 소리로 나는 단어입니다."},
        {"word": "cube", "explain": "u_e 구조로 u가 긴 /juː/ 소리로 납니다."},
        {"word": "cute", "explain": "u가 긴 '유' 소리로 나는 단어입니다."},
    ],

    "④ 모음 예외": [
        {"word": "ball", "explain": "a가 기본 short a가 아니라 all에서 '올'에 가까운 소리로 납니다."},
        {"word": "call", "explain": "all이 '올'에 가까운 소리로 나는 단어입니다."},
        {"word": "car", "explain": "ar이 r의 영향을 받아 '아알'에 가까운 소리로 납니다."},
        {"word": "father", "explain": "a가 기본 short a가 아니라 '아'에 가까운 소리로 납니다."},
        {"word": "about", "explain": "처음 a가 강세를 받지 않아 약한 /ə/ 소리로 납니다."},
        {"word": "love", "explain": "o가 /o/가 아니라 짧은 '어' 소리 /ʌ/로 납니다."},
        {"word": "come", "explain": "o가 /ʌ/ 소리로 나는 예외 단어입니다."},
        {"word": "do", "explain": "o가 긴 /uː/ 소리로 나는 예외 단어입니다."},
        {"word": "book", "explain": "oo가 긴 /uː/가 아니라 짧은 /ʊ/ 소리로 납니다."},
        {"word": "bread", "explain": "ea가 긴 e 소리가 아니라 짧은 /e/ 소리로 납니다."},
    ],

    "⑤ 자음 이어 읽기": [
        {"word": "black", "explain": "bl의 두 자음 소리가 이어져 나는 단어입니다."},
        {"word": "brown", "explain": "br의 b와 r 소리가 이어져 나는 단어입니다."},
        {"word": "clock", "explain": "cl의 c/k 소리와 l 소리가 이어져 나는 단어입니다."},
        {"word": "crab", "explain": "cr의 c/k 소리와 r 소리가 이어져 나는 단어입니다."},
        {"word": "drum", "explain": "dr의 d와 r 소리가 이어져 나는 단어입니다."},
        {"word": "flag", "explain": "fl의 f와 l 소리가 이어져 나는 단어입니다."},
        {"word": "frog", "explain": "fr의 f와 r 소리가 이어져 나는 단어입니다."},
        {"word": "green", "explain": "gr의 g와 r 소리가 이어져 나는 단어입니다."},
        {"word": "spoon", "explain": "sp의 s와 p 소리가 이어져 나는 단어입니다."},
        {"word": "star", "explain": "st의 s와 t 소리가 이어져 나는 단어입니다."},
    ],

    "⑥ 두 글자 한 소리": [
        {"word": "chair", "explain": "ch가 /tʃ/ 소리, 즉 '치'에 가까운 소리로 납니다."},
        {"word": "ship", "explain": "sh가 /ʃ/ 소리, 즉 '쉬'에 가까운 소리로 납니다."},
        {"word": "three", "explain": "th가 혀를 살짝 내미는 /θ/ 소리로 납니다."},
        {"word": "this", "explain": "th가 목소리가 울리는 /ð/ 소리로 납니다."},
        {"word": "phone", "explain": "ph가 f와 같은 /f/ 소리로 납니다."},
        {"word": "whale", "explain": "wh가 /w/ 소리로 나는 단어입니다."},
        {"word": "duck", "explain": "ck가 /k/ 소리로 나는 단어입니다."},
        {"word": "shop", "explain": "sh의 /ʃ/ 소리를 연습할 수 있는 단어입니다."},
        {"word": "cheese", "explain": "ch의 /tʃ/ 소리와 ee의 긴 e 소리를 함께 연습할 수 있습니다."},
        {"word": "photo", "explain": "ph가 /f/ 소리로 나는 것을 연습할 수 있는 단어입니다."},
    ],

    "⑦ 모음 두 글자 소리": [
        {"word": "rain", "explain": "ai가 /eɪ/ 소리로 나는 단어입니다."},
        {"word": "day", "explain": "ay가 /eɪ/ 소리로 나는 단어입니다."},
        {"word": "see", "explain": "ee가 긴 /iː/ 소리로 나는 단어입니다."},
        {"word": "eat", "explain": "ea가 긴 /iː/ 소리로 나는 단어입니다."},
        {"word": "boat", "explain": "oa가 /oʊ/ 소리로 나는 단어입니다."},
        {"word": "snow", "explain": "ow가 /oʊ/ 소리로 나는 단어입니다."},
        {"word": "cow", "explain": "ow가 /aʊ/ 소리로 나는 단어입니다."},
        {"word": "house", "explain": "ou가 /aʊ/ 소리로 나는 단어입니다."},
        {"word": "coin", "explain": "oi가 /ɔɪ/ 소리로 나는 단어입니다."},
        {"word": "boy", "explain": "oy가 /ɔɪ/ 소리로 나는 단어입니다."},
    ],

    "⑧ r이 붙은 모음": [
        {"word": "car", "explain": "ar이 /ɑːr/ 소리로 나는 단어입니다."},
        {"word": "star", "explain": "st 소리 뒤에 ar 소리가 이어지는 단어입니다."},
        {"word": "her", "explain": "er이 /ɜːr/ 소리로 나는 단어입니다."},
        {"word": "bird", "explain": "ir이 /ɜːr/ 소리로 나는 단어입니다."},
        {"word": "girl", "explain": "ir이 r의 영향을 받아 '얼'에 가까운 소리로 납니다."},
        {"word": "corn", "explain": "or이 /ɔːr/ 소리로 나는 단어입니다."},
        {"word": "fork", "explain": "or의 r-controlled vowel 소리를 연습할 수 있는 단어입니다."},
        {"word": "turn", "explain": "ur이 /ɜːr/ 소리로 나는 단어입니다."},
        {"word": "burn", "explain": "ur이 '얼'에 가까운 소리로 나는 단어입니다."},
        {"word": "teacher", "explain": "끝의 er이 약한 r-controlled 소리로 나는 단어입니다."},
    ],

    "⑨ 소리 안 나는 e": [
        {"word": "cake", "explain": "끝의 e는 소리 나지 않고, a를 긴 /eɪ/ 소리로 만듭니다."},
        {"word": "name", "explain": "a_e 구조로 a가 긴 모음 소리로 납니다."},
        {"word": "bike", "explain": "i_e 구조로 i가 긴 /aɪ/ 소리로 납니다."},
        {"word": "five", "explain": "끝의 e는 소리 나지 않고, i가 긴 모음 소리로 납니다."},
        {"word": "home", "explain": "o_e 구조로 o가 긴 /oʊ/ 소리로 납니다."},
        {"word": "rope", "explain": "끝의 e는 소리 나지 않고, o를 긴 소리로 만듭니다."},
        {"word": "cube", "explain": "u_e 구조로 u가 긴 /juː/ 소리로 납니다."},
        {"word": "cute", "explain": "u가 긴 '유' 소리로 나는 단어입니다."},
        {"word": "make", "explain": "a_e 구조로 a가 긴 /eɪ/ 소리로 납니다."},
        {"word": "hope", "explain": "o_e 구조로 o가 긴 /oʊ/ 소리로 납니다."},
    ],

    "⑩ 자음 예외": [
        {"word": "cent", "explain": "c 뒤에 e가 와서 c가 /s/ 소리로 납니다."},
        {"word": "city", "explain": "c 뒤에 i가 와서 c가 /s/ 소리로 납니다."},
        {"word": "cycle", "explain": "c 뒤에 y가 와서 c가 /s/ 소리로 납니다."},
        {"word": "gem", "explain": "g 뒤에 e가 와서 g가 /dʒ/ 소리로 납니다."},
        {"word": "giant", "explain": "g 뒤에 i가 와서 g가 /dʒ/ 소리로 납니다."},
        {"word": "gym", "explain": "g 뒤에 y가 와서 g가 /dʒ/ 소리로 납니다."},
        {"word": "knee", "explain": "kn에서 k는 소리 나지 않고 n 소리만 납니다."},
        {"word": "write", "explain": "wr에서 w는 소리 나지 않고 r 소리만 납니다."},
        {"word": "lamb", "explain": "단어 끝 mb에서 b는 소리 나지 않습니다."},
        {"word": "exam", "explain": "x가 /gz/ 소리로 나는 경우를 연습할 수 있는 단어입니다."},
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
            🔊 그 다음 원어민 발음을 듣고, 💡 단어의 소리를 이해해 봅니다.
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
            st.markdown("### 🗣️ 먼저 직접 말해 보기")
            st.write("스펠링을 보고 단어를 먼저 큰 소리로 읽어 보세요.")

            st.markdown("### 🔊 원어민 발음 듣기")
            play_audio(word, key=f"{tab_name}_audio_{i}")

            st.markdown("### 💡 소리 이해하기")
            st.info(explain)


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(practice_sets.keys()))

for tab, tab_name in zip(tabs, practice_sets.keys()):
    with tab:
        show_speaking_practice(tab_name, practice_sets[tab_name])
