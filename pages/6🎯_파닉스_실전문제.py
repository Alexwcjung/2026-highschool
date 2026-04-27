import streamlit as st
from gtts import gTTS
import io
import random

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Phonics Practice",
    page_icon="🎧",
    layout="wide"
)

st.title("🎧 Phonics Practice")
st.caption("단어 발음을 듣고, 알맞은 소리나 글자 패턴을 골라 봅시다.")

# =========================
# 안내 박스
# =========================
st.markdown(
    """
    <div style="
        border-left: 6px solid #4f8df7;
        background-color: #f4f8ff;
        padding: 16px 18px;
        border-radius: 12px;
        margin-bottom: 22px;
        line-height: 1.7;
    ">
        <div style="font-size:20px; font-weight:900; margin-bottom:8px;">
            📌 실전 연습 방법
        </div>
        <div>• <b>🔊 단어 듣기</b> 버튼을 눌러 발음을 먼저 들어 봅니다.</div>
        <div>• 문제를 풀 때는 단어 철자를 먼저 보여주지 않습니다.</div>
        <div>• 들리는 소리를 바탕으로 알맞은 소리나 글자 패턴을 고릅니다.</div>
        <div>• 1차 제출 후 틀린 문제만 다시 풀고, 2차 제출 후 정답과 단어를 확인할 수 있습니다.</div>
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


def audio_button(label, text, key):
    if st.button(label, key=key):
        audio_bytes = make_tts_audio(text)
        st.audio(audio_bytes, format="audio/mp3")


# =========================
# 보기 고정 랜덤 섞기
# =========================
def get_shuffled_options(tab_name, question_index, options):
    """
    보기 순서를 문제별로 고정 랜덤 처리.
    새로고침하거나 1차/2차로 넘어가도 같은 문제의 보기 순서는 유지됨.
    """
    key = f"{tab_name}_shuffled_options_{question_index}"

    if key not in st.session_state:
        shuffled = options[:]
        random.seed(f"{tab_name}_{question_index}")
        random.shuffle(shuffled)
        st.session_state[key] = shuffled

    return st.session_state[key]


# =========================
# 문제 데이터
# =========================
practice_sets = {
    "① 자음 소리": [
        {
            "word": "bat",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/b/ (브에 가까운 소리)",
            "options": ["/b/ (브에 가까운 소리)", "/d/ (드에 가까운 소리)", "/p/ (프에 가까운 소리)", "/t/ (트에 가까운 소리)"]
        },
        {
            "word": "cat",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/k/ (크에 가까운 소리)",
            "options": ["/k/ (크에 가까운 소리)", "/s/ (스에 가까운 소리)", "/g/ (그에 가까운 소리)", "/t/ (트에 가까운 소리)"]
        },
        {
            "word": "dog",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/d/ (드에 가까운 소리)",
            "options": ["/d/ (드에 가까운 소리)", "/b/ (브에 가까운 소리)", "/g/ (그에 가까운 소리)", "/t/ (트에 가까운 소리)"]
        },
        {
            "word": "fish",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/f/ (입술을 가볍게 물고 내는 프 소리)",
            "options": ["/f/ (입술을 가볍게 물고 내는 프 소리)", "/p/ (프에 가까운 소리)", "/v/ (입술을 가볍게 물고 내는 브 소리)", "/h/ (ㅎ에 가까운 숨소리)"]
        },
        {
            "word": "goat",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/g/ (그에 가까운 소리)",
            "options": ["/g/ (그에 가까운 소리)", "/k/ (크에 가까운 소리)", "/j/ (즈와 쥬 사이 소리)", "/d/ (드에 가까운 소리)"]
        },
        {
            "word": "hat",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/h/ (ㅎ에 가까운 숨소리)",
            "options": ["/h/ (ㅎ에 가까운 숨소리)", "/f/ (입술을 가볍게 물고 내는 프 소리)", "/k/ (크에 가까운 소리)", "/w/ (우에서 시작하는 w 소리)"]
        },
        {
            "word": "jam",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/j/ (즈와 쥬 사이 소리)",
            "options": ["/j/ (즈와 쥬 사이 소리)", "/g/ (그에 가까운 소리)", "/y/ (이에서 시작하는 y 소리)", "/z/ (즈에 가까운 소리)"]
        },
        {
            "word": "sun",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/s/ (스에 가까운 소리)",
            "options": ["/s/ (스에 가까운 소리)", "/z/ (즈에 가까운 소리)", "/sh/ (쉬에 가까운 소리)", "/ch/ (치에 가까운 소리)"]
        },
        {
            "word": "van",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/v/ (입술을 가볍게 물고 내는 브 소리)",
            "options": ["/v/ (입술을 가볍게 물고 내는 브 소리)", "/f/ (입술을 가볍게 물고 내는 프 소리)", "/b/ (브에 가까운 소리)", "/w/ (우에서 시작하는 w 소리)"]
        },
        {
            "word": "yes",
            "question": "단어를 듣고, 처음 들리는 자음 소리를 고르세요.",
            "answer": "/y/ (이에서 시작하는 y 소리)",
            "options": ["/y/ (이에서 시작하는 y 소리)", "/j/ (즈와 쥬 사이 소리)", "/w/ (우에서 시작하는 w 소리)", "/r/ (혀를 말아 내는 r 소리)"]
        },
    ],

    "② 짧은 모음": [
        {
            "word": "apple",
            "question": "단어를 듣고, 가운데 또는 주요 모음 소리를 고르세요.",
            "answer": "Short a /æ/ (애에 가까운 소리)",
            "options": ["Short a /æ/ (애에 가까운 소리)", "Long a /eɪ/ (에이에 가까운 소리)", "Short e /e/ (에에 가까운 소리)", "Long e /iː/ (긴 이 소리)"]
        },
        {
            "word": "cat",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short a /æ/ (애에 가까운 소리)",
            "options": ["Short a /æ/ (애에 가까운 소리)", "Long a /eɪ/ (에이에 가까운 소리)", "Short o /ɑ/ (아에 가까운 소리)", "Short u /ʌ/ (짧은 어에 가까운 소리)"]
        },
        {
            "word": "egg",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short e /e/ (에에 가까운 소리)",
            "options": ["Short e /e/ (에에 가까운 소리)", "Long e /iː/ (긴 이 소리)", "Short i /ɪ/ (이와 에 사이의 짧은 소리)", "Long i /aɪ/ (아이 소리)"]
        },
        {
            "word": "bed",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short e /e/ (에에 가까운 소리)",
            "options": ["Short e /e/ (에에 가까운 소리)", "Long e /iː/ (긴 이 소리)", "Short a /æ/ (애에 가까운 소리)", "Long a /eɪ/ (에이에 가까운 소리)"]
        },
        {
            "word": "sit",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short i /ɪ/ (이와 에 사이의 짧은 소리)",
            "options": ["Short i /ɪ/ (이와 에 사이의 짧은 소리)", "Long i /aɪ/ (아이 소리)", "Short e /e/ (에에 가까운 소리)", "Long e /iː/ (긴 이 소리)"]
        },
        {
            "word": "pig",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short i /ɪ/ (이와 에 사이의 짧은 소리)",
            "options": ["Short i /ɪ/ (이와 에 사이의 짧은 소리)", "Long i /aɪ/ (아이 소리)", "Short u /ʌ/ (짧은 어에 가까운 소리)", "Long u /juː/ (유에 가까운 소리)"]
        },
        {
            "word": "hot",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short o /ɑ/ (아에 가까운 소리)",
            "options": ["Short o /ɑ/ (아에 가까운 소리)", "Long o /oʊ/ (오우에 가까운 소리)", "Short a /æ/ (애에 가까운 소리)", "Long a /eɪ/ (에이에 가까운 소리)"]
        },
        {
            "word": "cup",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short u /ʌ/ (짧은 어에 가까운 소리)",
            "options": ["Short u /ʌ/ (짧은 어에 가까운 소리)", "Long u /juː/ (유에 가까운 소리)", "Short o /ɑ/ (아에 가까운 소리)", "Long o /oʊ/ (오우에 가까운 소리)"]
        },
        {
            "word": "bus",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short u /ʌ/ (짧은 어에 가까운 소리)",
            "options": ["Short u /ʌ/ (짧은 어에 가까운 소리)", "Long u /juː/ (유에 가까운 소리)", "Short i /ɪ/ (이와 에 사이의 짧은 소리)", "Long i /aɪ/ (아이 소리)"]
        },
        {
            "word": "fox",
            "question": "단어를 듣고, 가운데 모음 소리를 고르세요.",
            "answer": "Short o /ɑ/ (아에 가까운 소리)",
            "options": ["Short o /ɑ/ (아에 가까운 소리)", "Long o /oʊ/ (오우에 가까운 소리)", "Short u /ʌ/ (짧은 어에 가까운 소리)", "Long u /juː/ (유에 가까운 소리)"]
        },
    ],

    "③ 긴 모음": [
        {"word": "cake", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long a /eɪ/ (에이에 가까운 소리)", "options": ["Long a /eɪ/ (에이에 가까운 소리)", "Short a /æ/ (애에 가까운 소리)", "Long e /iː/ (긴 이 소리)", "Short e /e/ (에에 가까운 소리)"]},
        {"word": "name", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long a /eɪ/ (에이에 가까운 소리)", "options": ["Long a /eɪ/ (에이에 가까운 소리)", "Short a /æ/ (애에 가까운 소리)", "Long i /aɪ/ (아이 소리)", "Short i /ɪ/ (이와 에 사이의 짧은 소리)"]},
        {"word": "tree", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long e /iː/ (긴 이 소리)", "options": ["Long e /iː/ (긴 이 소리)", "Short e /e/ (에에 가까운 소리)", "Long a /eɪ/ (에이에 가까운 소리)", "Short a /æ/ (애에 가까운 소리)"]},
        {"word": "see", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long e /iː/ (긴 이 소리)", "options": ["Long e /iː/ (긴 이 소리)", "Short e /e/ (에에 가까운 소리)", "Long i /aɪ/ (아이 소리)", "Short i /ɪ/ (이와 에 사이의 짧은 소리)"]},
        {"word": "bike", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long i /aɪ/ (아이 소리)", "options": ["Long i /aɪ/ (아이 소리)", "Short i /ɪ/ (이와 에 사이의 짧은 소리)", "Long e /iː/ (긴 이 소리)", "Short e /e/ (에에 가까운 소리)"]},
        {"word": "five", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long i /aɪ/ (아이 소리)", "options": ["Long i /aɪ/ (아이 소리)", "Short i /ɪ/ (이와 에 사이의 짧은 소리)", "Long o /oʊ/ (오우에 가까운 소리)", "Short o /ɑ/ (아에 가까운 소리)"]},
        {"word": "rope", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long o /oʊ/ (오우에 가까운 소리)", "options": ["Long o /oʊ/ (오우에 가까운 소리)", "Short o /ɑ/ (아에 가까운 소리)", "Long a /eɪ/ (에이에 가까운 소리)", "Short a /æ/ (애에 가까운 소리)"]},
        {"word": "home", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long o /oʊ/ (오우에 가까운 소리)", "options": ["Long o /oʊ/ (오우에 가까운 소리)", "Short o /ɑ/ (아에 가까운 소리)", "Long u /juː/ (유에 가까운 소리)", "Short u /ʌ/ (짧은 어에 가까운 소리)"]},
        {"word": "cube", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long u /juː/ (유에 가까운 소리)", "options": ["Long u /juː/ (유에 가까운 소리)", "Short u /ʌ/ (짧은 어에 가까운 소리)", "Long o /oʊ/ (오우에 가까운 소리)", "Short o /ɑ/ (아에 가까운 소리)"]},
        {"word": "cute", "question": "단어를 듣고, 들리는 긴 모음 소리를 고르세요.", "answer": "Long u /juː/ (유에 가까운 소리)", "options": ["Long u /juː/ (유에 가까운 소리)", "Short u /ʌ/ (짧은 어에 가까운 소리)", "Long e /iː/ (긴 이 소리)", "Short e /e/ (에에 가까운 소리)"]},
    ],

    "④ 모음 예외": [
        {"word": "ball", "question": "단어를 듣고, 들리는 모음 예외 소리를 고르세요.", "answer": "aw 소리", "options": ["aw 소리", "Short a", "Long a", "ee 소리"]},
        {"word": "call", "question": "단어를 듣고, 들리는 모음 예외 소리를 고르세요.", "answer": "aw 소리", "options": ["aw 소리", "Short a", "Long a", "Short i"]},
        {"word": "car", "question": "단어를 듣고, 들리는 r의 영향을 받은 소리를 고르세요.", "answer": "ar 소리", "options": ["ar 소리", "Short a", "Long a", "ee 소리"]},
        {"word": "father", "question": "단어를 듣고, a가 어떤 소리로 들리는지 고르세요.", "answer": "ah 소리", "options": ["ah 소리", "Short a", "Long a", "Short e"]},
        {"word": "about", "question": "단어를 듣고, 첫 a가 약하게 어떤 소리로 들리는지 고르세요.", "answer": "uh 소리", "options": ["uh 소리", "Long a", "Short a", "ee 소리"]},
        {"word": "love", "question": "단어를 듣고, o가 어떤 소리로 들리는지 고르세요.", "answer": "uh 소리", "options": ["uh 소리", "Long o", "Short o", "ee 소리"]},
        {"word": "do", "question": "단어를 듣고, o가 어떤 소리로 들리는지 고르세요.", "answer": "oo 소리", "options": ["oo 소리", "Short o", "Long o", "Short u"]},
        {"word": "book", "question": "단어를 듣고, oo 소리의 종류를 고르세요.", "answer": "짧은 oo", "options": ["짧은 oo", "긴 oo", "Long a", "Short a"]},
        {"word": "moon", "question": "단어를 듣고, oo 소리의 종류를 고르세요.", "answer": "긴 oo", "options": ["긴 oo", "짧은 oo", "Short e", "Long i"]},
        {"word": "bread", "question": "단어를 듣고, ea가 어떤 소리로 들리는지 고르세요.", "answer": "eh 소리", "options": ["eh 소리", "ee 소리", "ay 소리", "ow 소리"]},
    ],

    "⑤ Blends": [
        {"word": "black", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "bl", "options": ["bl", "br", "cl", "cr"]},
        {"word": "brown", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "br", "options": ["br", "bl", "gr", "tr"]},
        {"word": "clock", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "cl", "options": ["cl", "cr", "fl", "gl"]},
        {"word": "crab", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "cr", "options": ["cr", "cl", "dr", "fr"]},
        {"word": "drum", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "dr", "options": ["dr", "tr", "br", "gr"]},
        {"word": "flag", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "fl", "options": ["fl", "fr", "pl", "sl"]},
        {"word": "frog", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "fr", "options": ["fr", "fl", "gr", "br"]},
        {"word": "green", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "gr", "options": ["gr", "gl", "br", "tr"]},
        {"word": "spoon", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "sp", "options": ["sp", "st", "sn", "sl"]},
        {"word": "star", "question": "단어를 듣고, 처음에 들리는 blend를 고르세요.", "answer": "st", "options": ["st", "sp", "sk", "sm"]},
    ],

    "⑥ Digraphs": [
        {"word": "chair", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "ch", "options": ["ch", "sh", "th", "ph"]},
        {"word": "ship", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "sh", "options": ["sh", "ch", "th", "ck"]},
        {"word": "three", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "th", "options": ["th", "sh", "ch", "ph"]},
        {"word": "this", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "th", "options": ["th", "ch", "sh", "wh"]},
        {"word": "phone", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "ph", "options": ["ph", "sh", "ch", "th"]},
        {"word": "whale", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "wh", "options": ["wh", "ph", "sh", "ch"]},
        {"word": "duck", "question": "단어를 듣고, 끝에 들리는 digraph를 고르세요.", "answer": "ck", "options": ["ck", "ch", "sh", "th"]},
        {"word": "shop", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "sh", "options": ["sh", "ch", "ph", "wh"]},
        {"word": "cheese", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "ch", "options": ["ch", "sh", "th", "ck"]},
        {"word": "photo", "question": "단어를 듣고, 처음에 들리는 digraph를 고르세요.", "answer": "ph", "options": ["ph", "th", "ch", "sh"]},
    ],

    "⑦ Vowel Teams": [
        {"word": "rain", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ai", "options": ["ai", "ay", "ee", "oa"]},
        {"word": "day", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ay", "options": ["ay", "ai", "oi", "oy"]},
        {"word": "see", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ee", "options": ["ee", "ea", "ai", "oa"]},
        {"word": "eat", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ea", "options": ["ea", "ee", "ai", "ay"]},
        {"word": "boat", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "oa", "options": ["oa", "ow", "ou", "oi"]},
        {"word": "snow", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ow", "options": ["ow", "oa", "ou", "oy"]},
        {"word": "cow", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ow", "options": ["ow", "ou", "oa", "oi"]},
        {"word": "house", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "ou", "options": ["ou", "ow", "oi", "oy"]},
        {"word": "coin", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "oi", "options": ["oi", "oy", "ai", "ay"]},
        {"word": "boy", "question": "단어를 듣고, 들리는 vowel team을 고르세요.", "answer": "oy", "options": ["oy", "oi", "ow", "ou"]},
    ],

    "⑧ R-Controlled": [
        {"word": "car", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "ar", "options": ["ar", "er", "ir", "or"]},
        {"word": "star", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "ar", "options": ["ar", "ur", "or", "er"]},
        {"word": "her", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "er", "options": ["er", "ir", "ur", "ar"]},
        {"word": "bird", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "ir", "options": ["ir", "er", "ur", "or"]},
        {"word": "girl", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "ir", "options": ["ir", "er", "ar", "or"]},
        {"word": "corn", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "or", "options": ["or", "ar", "er", "ur"]},
        {"word": "fork", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "or", "options": ["or", "ar", "ir", "er"]},
        {"word": "turn", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "ur", "options": ["ur", "er", "ir", "or"]},
        {"word": "burn", "question": "단어를 듣고, 들리는 r-controlled pattern을 고르세요.", "answer": "ur", "options": ["ur", "ir", "er", "ar"]},
        {"word": "teacher", "question": "단어를 듣고, 끝부분에 들리는 r-controlled pattern을 고르세요.", "answer": "er", "options": ["er", "ar", "or", "ir"]},
    ],

    "⑨ Silent e": [
        {"word": "cake", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "a_e", "options": ["a_e", "i_e", "o_e", "u_e"]},
        {"word": "name", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "a_e", "options": ["a_e", "i_e", "o_e", "u_e"]},
        {"word": "bike", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "i_e", "options": ["i_e", "a_e", "o_e", "u_e"]},
        {"word": "five", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "i_e", "options": ["i_e", "a_e", "e_e", "o_e"]},
        {"word": "home", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "o_e", "options": ["o_e", "a_e", "i_e", "u_e"]},
        {"word": "rope", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "o_e", "options": ["o_e", "i_e", "a_e", "u_e"]},
        {"word": "cube", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "u_e", "options": ["u_e", "a_e", "i_e", "o_e"]},
        {"word": "cute", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "u_e", "options": ["u_e", "a_e", "i_e", "o_e"]},
        {"word": "make", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "a_e", "options": ["a_e", "i_e", "o_e", "u_e"]},
        {"word": "hope", "question": "단어를 듣고, 긴 모음 소리를 만드는 silent e 패턴을 고르세요.", "answer": "o_e", "options": ["o_e", "a_e", "i_e", "u_e"]},
    ],
}


# =========================
# 세션 상태 초기화
# =========================
def init_tab_state(tab_name):
    if f"{tab_name}_submitted1" not in st.session_state:
        st.session_state[f"{tab_name}_submitted1"] = False
    if f"{tab_name}_submitted2" not in st.session_state:
        st.session_state[f"{tab_name}_submitted2"] = False
    if f"{tab_name}_wrong_indices" not in st.session_state:
        st.session_state[f"{tab_name}_wrong_indices"] = []


def reset_quiz(tab_name):
    keys_to_delete = []
    for key in st.session_state.keys():
        if key.startswith(tab_name):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del st.session_state[key]


# =========================
# 문제 출력 함수
# =========================
def show_quiz(tab_name, questions):
    init_tab_state(tab_name)

    st.subheader(tab_name)
    st.write("단어 철자를 먼저 보지 말고, 발음을 듣고 알맞은 답을 고르세요.")

    submitted1_key = f"{tab_name}_submitted1"
    submitted2_key = f"{tab_name}_submitted2"
    wrong_key = f"{tab_name}_wrong_indices"

    # -------------------------
    # 1차 풀이
    # -------------------------
    if not st.session_state[submitted1_key]:
        st.markdown("### 📝 1차 도전")

        for i, q in enumerate(questions):
            st.markdown("---")
            st.markdown(f"### {i + 1}. Listen and choose.")
            audio_button("🔊 단어 듣기", q["word"], key=f"{tab_name}_audio1_{i}")

            shuffled_options = get_shuffled_options(tab_name, i, q["options"])

            st.radio(
                q["question"],
                shuffled_options,
                key=f"{tab_name}_q1_{i}"
            )

        if st.button("✅ 1차 제출하기", key=f"{tab_name}_submit1"):
            wrong_indices = []

            for i, q in enumerate(questions):
                user_answer = st.session_state.get(f"{tab_name}_q1_{i}")
                if user_answer != q["answer"]:
                    wrong_indices.append(i)

            st.session_state[wrong_key] = wrong_indices
            st.session_state[submitted1_key] = True
            st.rerun()

    # -------------------------
    # 1차 결과 및 2차 풀이
    # -------------------------
    elif st.session_state[submitted1_key] and not st.session_state[submitted2_key]:
        wrong_indices = st.session_state[wrong_key]
        score = len(questions) - len(wrong_indices)

        st.success(f"🎉 1차 결과: {score} / {len(questions)}점")

        if len(wrong_indices) == 0:
            st.balloons()
            st.success("완벽합니다! 모든 문제를 맞혔습니다.")

            if st.button("🔄 다시 풀기", key=f"{tab_name}_reset_all_correct"):
                reset_quiz(tab_name)
                st.rerun()

        else:
            st.warning(f"아쉬운 문제 {len(wrong_indices)}개를 다시 풀어 봅시다.")
            st.markdown("### 🔁 2차 도전: 틀린 문제만 다시 풀기")

            for i in wrong_indices:
                q = questions[i]

                st.markdown("---")
                st.markdown(f"### {i + 1}. Listen again and choose.")
                audio_button("🔊 단어 다시 듣기", q["word"], key=f"{tab_name}_audio2_{i}")

                shuffled_options = get_shuffled_options(tab_name, i, q["options"])

                st.radio(
                    q["question"],
                    shuffled_options,
                    key=f"{tab_name}_q2_{i}"
                )

            if st.button("✅ 2차 제출하기", key=f"{tab_name}_submit2"):
                st.session_state[submitted2_key] = True
                st.rerun()

    # -------------------------
    # 2차 결과 및 정답 공개
    # -------------------------
    else:
        wrong_indices = st.session_state[wrong_key]
        second_wrong = []

        for i in wrong_indices:
            q = questions[i]
            user_answer = st.session_state.get(f"{tab_name}_q2_{i}")
            if user_answer != q["answer"]:
                second_wrong.append(i)

        second_score = len(questions) - len(second_wrong)

        st.success(f"🎉 최종 결과: {second_score} / {len(questions)}점")

        if len(second_wrong) == 0:
            st.balloons()
            st.success("좋습니다! 2차 도전까지 통해 모두 해결했습니다.")
        else:
            st.warning("아래에서 정답과 실제 단어를 확인해 봅시다.")

        st.markdown("### ✅ 정답 확인")

        if len(wrong_indices) == 0:
            st.info("틀린 문제가 없어 확인할 정답이 없습니다.")
        else:
            for i in wrong_indices:
                q = questions[i]
                user_answer_1 = st.session_state.get(f"{tab_name}_q1_{i}")
                user_answer_2 = st.session_state.get(f"{tab_name}_q2_{i}")

                st.markdown("---")
                st.markdown(f"### {i + 1}. 정답 단어: **{q['word']}**")
                audio_button("🔊 단어 다시 듣기", q["word"], key=f"{tab_name}_audio_answer_{i}")
                st.write(f"문제: {q['question']}")
                st.write(f"1차 선택: {user_answer_1}")
                st.write(f"2차 선택: {user_answer_2}")
                st.success(f"정답: {q['answer']}")

        if st.button("🔄 다시 풀기", key=f"{tab_name}_reset"):
            reset_quiz(tab_name)
            st.rerun()


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(practice_sets.keys()))

for tab, tab_name in zip(tabs, practice_sets.keys()):
    with tab:
        show_quiz(tab_name, practice_sets[tab_name])
