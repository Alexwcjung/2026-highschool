import streamlit as st
import random
import io
from gtts import gTTS

st.set_page_config(page_title="Phonics Pronunciation Practice", layout="centered")

st.title("🎯 Phonics Pronunciation Practice")
st.caption("단어를 보고, 발음을 듣고, 큰 소리로 따라 읽어 봅시다.")


# =========================================================
# TTS 함수
# =========================================================
@st.cache_data
def make_tts_audio(text):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang="en")
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def play_audio(text):
    st.audio(make_tts_audio(text), format="audio/mp3")


# =========================================================
# 공통 발음 연습 함수
# =========================================================
def run_pronunciation_practice(prefix, title, caption, guide_text, word_data):
    st.subheader(title)
    st.caption(caption)
    st.info(guide_text)

    if f"{prefix}_words" not in st.session_state:
        words = word_data.copy()
        random.shuffle(words)
        st.session_state[f"{prefix}_words"] = words

    if f"{prefix}_checked" not in st.session_state:
        st.session_state[f"{prefix}_checked"] = {}

    words = st.session_state[f"{prefix}_words"]

    if st.button("단어 순서 다시 섞기", key=f"shuffle_{prefix}"):
        random.shuffle(words)
        st.session_state[f"{prefix}_words"] = words
        st.session_state[f"{prefix}_checked"] = {}
        st.rerun()

    st.markdown("---")

    for i, item in enumerate(words):
        word = item["word"]
        meaning = item["meaning"]
        pattern = item["pattern"]
        audio_text = item.get("audio", word)

        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border-radius:22px;
                padding:24px;
                margin:18px 0;
                box-shadow:0 5px 16px rgba(0,0,0,0.07);
                border:1px solid #eeeeee;
                text-align:center;
            ">
                <p style="font-size:17px; color:#666; margin-bottom:5px;">
                    {i+1}번 단어
                </p>
                <h1 style="font-size:46px; color:#1f4e79; margin:8px 0;">
                    {word}
                </h1>
                <p style="font-size:20px; color:#333;">
                    뜻: <b>{meaning}</b>
                </p>
                <p style="font-size:18px; color:#777;">
                    소리 패턴: <b>{pattern}</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("🔊 발음을 듣고 따라 읽어 보세요.")
        play_audio(audio_text)

        checked = st.checkbox(
            "따라 읽기 완료",
            key=f"{prefix}_check_{i}"
        )

        st.session_state[f"{prefix}_checked"][i] = checked

        st.markdown("---")

    completed = sum(1 for v in st.session_state[f"{prefix}_checked"].values() if v)
    total = len(words)

    st.subheader("학습 진행 상황")
    st.write(f"완료한 단어: **{completed} / {total}**")
    st.progress(completed / total)

    if completed == total:
        st.success("모든 단어를 따라 읽었습니다! 아주 잘했습니다 🎉")
        st.balloons()
    elif completed >= total * 0.7:
        st.success("좋습니다! 거의 다 했습니다.")
    elif completed >= total * 0.4:
        st.info("잘하고 있습니다. 남은 단어도 천천히 따라 읽어 봅시다.")
    else:
        st.warning("먼저 발음을 듣고 한 단어씩 따라 읽어 봅시다.")


# =========================================================
# 단어 데이터 1: 자음 단어
# =========================================================
consonant_words = [
    {"word": "bat", "meaning": "박쥐 / 방망이", "pattern": "b sound"},
    {"word": "bag", "meaning": "가방", "pattern": "b sound"},
    {"word": "dog", "meaning": "개", "pattern": "d sound"},
    {"word": "desk", "meaning": "책상", "pattern": "d sound"},
    {"word": "fish", "meaning": "물고기", "pattern": "f sound"},
    {"word": "fox", "meaning": "여우", "pattern": "f sound"},
    {"word": "goat", "meaning": "염소", "pattern": "g sound"},
    {"word": "gum", "meaning": "껌", "pattern": "g sound"},
    {"word": "hat", "meaning": "모자", "pattern": "h sound"},
    {"word": "hen", "meaning": "암탉", "pattern": "h sound"},
    {"word": "jam", "meaning": "잼", "pattern": "j sound"},
    {"word": "jet", "meaning": "제트기", "pattern": "j sound"},
    {"word": "king", "meaning": "왕", "pattern": "k sound"},
    {"word": "kite", "meaning": "연", "pattern": "k sound"},
    {"word": "lion", "meaning": "사자", "pattern": "l sound"},
    {"word": "leg", "meaning": "다리", "pattern": "l sound"},
    {"word": "man", "meaning": "남자", "pattern": "m sound"},
    {"word": "milk", "meaning": "우유", "pattern": "m sound"},
    {"word": "net", "meaning": "그물", "pattern": "n sound"},
    {"word": "nose", "meaning": "코", "pattern": "n sound"},
]


# =========================================================
# 단어 데이터 2: 단모음
# =========================================================
short_vowel_words = [
    {"word": "cat", "meaning": "고양이", "pattern": "short a"},
    {"word": "bag", "meaning": "가방", "pattern": "short a"},
    {"word": "man", "meaning": "남자", "pattern": "short a"},
    {"word": "hat", "meaning": "모자", "pattern": "short a"},
    {"word": "bed", "meaning": "침대", "pattern": "short e"},
    {"word": "pen", "meaning": "펜", "pattern": "short e"},
    {"word": "ten", "meaning": "10", "pattern": "short e"},
    {"word": "hen", "meaning": "암탉", "pattern": "short e"},
    {"word": "sit", "meaning": "앉다", "pattern": "short i"},
    {"word": "big", "meaning": "큰", "pattern": "short i"},
    {"word": "fish", "meaning": "물고기", "pattern": "short i"},
    {"word": "pig", "meaning": "돼지", "pattern": "short i"},
    {"word": "hot", "meaning": "뜨거운", "pattern": "short o"},
    {"word": "dog", "meaning": "개", "pattern": "short o"},
    {"word": "box", "meaning": "상자", "pattern": "short o"},
    {"word": "fox", "meaning": "여우", "pattern": "short o"},
    {"word": "cup", "meaning": "컵", "pattern": "short u"},
    {"word": "sun", "meaning": "태양", "pattern": "short u"},
    {"word": "bus", "meaning": "버스", "pattern": "short u"},
    {"word": "run", "meaning": "달리다", "pattern": "short u"},
]


# =========================================================
# 단어 데이터 3: 장모음
# =========================================================
long_vowel_words = [
    {"word": "cake", "meaning": "케이크", "pattern": "long a"},
    {"word": "name", "meaning": "이름", "pattern": "long a"},
    {"word": "rain", "meaning": "비", "pattern": "long a"},
    {"word": "train", "meaning": "기차", "pattern": "long a"},
    {"word": "he", "meaning": "그", "pattern": "long e"},
    {"word": "we", "meaning": "우리", "pattern": "long e"},
    {"word": "tree", "meaning": "나무", "pattern": "long e"},
    {"word": "green", "meaning": "초록색", "pattern": "long e"},
    {"word": "bike", "meaning": "자전거", "pattern": "long i"},
    {"word": "time", "meaning": "시간", "pattern": "long i"},
    {"word": "five", "meaning": "5", "pattern": "long i"},
    {"word": "kite", "meaning": "연", "pattern": "long i"},
    {"word": "home", "meaning": "집", "pattern": "long o"},
    {"word": "note", "meaning": "메모", "pattern": "long o"},
    {"word": "boat", "meaning": "배", "pattern": "long o"},
    {"word": "road", "meaning": "길", "pattern": "long o"},
    {"word": "cute", "meaning": "귀여운", "pattern": "long u"},
    {"word": "use", "meaning": "사용하다", "pattern": "long u"},
    {"word": "blue", "meaning": "파란색", "pattern": "long u"},
    {"word": "music", "meaning": "음악", "pattern": "long u"},
]


# =========================================================
# 단어 데이터 4: Magic E
# =========================================================
magic_e_words = [
    {"word": "cape", "meaning": "망토", "pattern": "Magic E: cap → cape", "audio": "cap, cape"},
    {"word": "tape", "meaning": "테이프", "pattern": "Magic E: tap → tape", "audio": "tap, tape"},
    {"word": "kite", "meaning": "연", "pattern": "Magic E: kit → kite", "audio": "kit, kite"},
    {"word": "bite", "meaning": "물다", "pattern": "Magic E: bit → bite", "audio": "bit, bite"},
    {"word": "hope", "meaning": "희망하다", "pattern": "Magic E: hop → hope", "audio": "hop, hope"},
    {"word": "cute", "meaning": "귀여운", "pattern": "Magic E: cut → cute", "audio": "cut, cute"},
    {"word": "make", "meaning": "만들다", "pattern": "Magic E"},
    {"word": "take", "meaning": "가져가다", "pattern": "Magic E"},
    {"word": "like", "meaning": "좋아하다", "pattern": "Magic E"},
    {"word": "ride", "meaning": "타다", "pattern": "Magic E"},
    {"word": "home", "meaning": "집", "pattern": "Magic E"},
    {"word": "nose", "meaning": "코", "pattern": "Magic E"},
]


# =========================================================
# 단어 데이터 5: Blends
# =========================================================
blend_words = [
    {"word": "black", "meaning": "검은색", "pattern": "bl"},
    {"word": "blue", "meaning": "파란색", "pattern": "bl"},
    {"word": "brown", "meaning": "갈색", "pattern": "br"},
    {"word": "bread", "meaning": "빵", "pattern": "br"},
    {"word": "clap", "meaning": "박수치다", "pattern": "cl"},
    {"word": "clock", "meaning": "시계", "pattern": "cl"},
    {"word": "crab", "meaning": "게", "pattern": "cr"},
    {"word": "cross", "meaning": "건너다", "pattern": "cr"},
    {"word": "drum", "meaning": "드럼", "pattern": "dr"},
    {"word": "drive", "meaning": "운전하다", "pattern": "dr"},
    {"word": "flag", "meaning": "깃발", "pattern": "fl"},
    {"word": "flower", "meaning": "꽃", "pattern": "fl"},
    {"word": "frog", "meaning": "개구리", "pattern": "fr"},
    {"word": "friend", "meaning": "친구", "pattern": "fr"},
    {"word": "green", "meaning": "초록색", "pattern": "gr"},
    {"word": "grape", "meaning": "포도", "pattern": "gr"},
    {"word": "plane", "meaning": "비행기", "pattern": "pl"},
    {"word": "play", "meaning": "놀다", "pattern": "pl"},
    {"word": "train", "meaning": "기차", "pattern": "tr"},
    {"word": "tree", "meaning": "나무", "pattern": "tr"},
]


# =========================================================
# 단어 데이터 6: Digraphs
# =========================================================
digraph_words = [
    {"word": "ship", "meaning": "배", "pattern": "sh"},
    {"word": "shop", "meaning": "가게", "pattern": "sh"},
    {"word": "fish", "meaning": "물고기", "pattern": "sh"},
    {"word": "chair", "meaning": "의자", "pattern": "ch"},
    {"word": "cheese", "meaning": "치즈", "pattern": "ch"},
    {"word": "lunch", "meaning": "점심", "pattern": "ch"},
    {"word": "thin", "meaning": "얇은", "pattern": "th"},
    {"word": "this", "meaning": "이것", "pattern": "th"},
    {"word": "bath", "meaning": "목욕", "pattern": "th"},
    {"word": "what", "meaning": "무엇", "pattern": "wh"},
    {"word": "when", "meaning": "언제", "pattern": "wh"},
    {"word": "white", "meaning": "흰색", "pattern": "wh"},
    {"word": "phone", "meaning": "전화", "pattern": "ph"},
    {"word": "photo", "meaning": "사진", "pattern": "ph"},
    {"word": "duck", "meaning": "오리", "pattern": "ck"},
    {"word": "sock", "meaning": "양말", "pattern": "ck"},
]


# =========================================================
# 단어 데이터 7: Vowel Teams
# =========================================================
vowel_team_words = [
    {"word": "rain", "meaning": "비", "pattern": "ai"},
    {"word": "train", "meaning": "기차", "pattern": "ai"},
    {"word": "paint", "meaning": "페인트칠하다", "pattern": "ai"},
    {"word": "day", "meaning": "날", "pattern": "ay"},
    {"word": "play", "meaning": "놀다", "pattern": "ay"},
    {"word": "say", "meaning": "말하다", "pattern": "ay"},
    {"word": "see", "meaning": "보다", "pattern": "ee"},
    {"word": "tree", "meaning": "나무", "pattern": "ee"},
    {"word": "green", "meaning": "초록색", "pattern": "ee"},
    {"word": "eat", "meaning": "먹다", "pattern": "ea"},
    {"word": "meat", "meaning": "고기", "pattern": "ea"},
    {"word": "sea", "meaning": "바다", "pattern": "ea"},
    {"word": "boat", "meaning": "배", "pattern": "oa"},
    {"word": "coat", "meaning": "코트", "pattern": "oa"},
    {"word": "road", "meaning": "길", "pattern": "oa"},
    {"word": "coin", "meaning": "동전", "pattern": "oi"},
    {"word": "boy", "meaning": "소년", "pattern": "oy"},
    {"word": "moon", "meaning": "달", "pattern": "oo"},
    {"word": "book", "meaning": "책", "pattern": "oo"},
    {"word": "cow", "meaning": "소", "pattern": "ow"},
]


# =========================================================
# 단어 데이터 8: R-Controlled
# =========================================================
r_controlled_words = [
    {"word": "car", "meaning": "자동차", "pattern": "ar"},
    {"word": "star", "meaning": "별", "pattern": "ar"},
    {"word": "park", "meaning": "공원", "pattern": "ar"},
    {"word": "her", "meaning": "그녀의", "pattern": "er"},
    {"word": "teacher", "meaning": "선생님", "pattern": "er"},
    {"word": "sister", "meaning": "여자 형제", "pattern": "er"},
    {"word": "bird", "meaning": "새", "pattern": "ir"},
    {"word": "girl", "meaning": "소녀", "pattern": "ir"},
    {"word": "shirt", "meaning": "셔츠", "pattern": "ir"},
    {"word": "corn", "meaning": "옥수수", "pattern": "or"},
    {"word": "horse", "meaning": "말", "pattern": "or"},
    {"word": "sport", "meaning": "스포츠", "pattern": "or"},
    {"word": "turn", "meaning": "돌다", "pattern": "ur"},
    {"word": "nurse", "meaning": "간호사", "pattern": "ur"},
    {"word": "purple", "meaning": "보라색", "pattern": "ur"},
]


# =========================================================
# 탭 구성
# =========================================================
tabs = st.tabs([
    "🧩 자음 단어",
    "🍎 단모음 단어",
    "🌟 장모음 단어",
    "🪄 Magic E",
    "🤝 Blends",
    "👯 Digraphs",
    "🌊 Vowel Teams",
    "🚗 R-Controlled"
])


# =========================================================
# 탭 실행
# =========================================================
with tabs[0]:
    run_pronunciation_practice(
        prefix="consonant",
        title="🧩 자음 단어 발음 연습",
        caption="자음으로 시작하는 단어를 듣고 따라 읽어 봅시다.",
        guide_text="알파벳 이름이 아니라 단어 안에서 나는 실제 자음 소리에 집중해 봅시다.",
        word_data=consonant_words
    )

with tabs[1]:
    run_pronunciation_practice(
        prefix="short_vowel",
        title="🍎 단모음 단어 발음 연습",
        caption="짧은 모음 소리가 들어간 단어를 듣고 따라 읽어 봅시다.",
        guide_text="cat, bed, sit, hot, cup처럼 짧은 모음 소리에 집중해 봅시다.",
        word_data=short_vowel_words
    )

with tabs[2]:
    run_pronunciation_practice(
        prefix="long_vowel",
        title="🌟 장모음 단어 발음 연습",
        caption="긴 모음 소리가 들어간 단어를 듣고 따라 읽어 봅시다.",
        guide_text="cake, bike, home처럼 모음 이름과 비슷하게 나는 소리를 들어 봅시다.",
        word_data=long_vowel_words
    )

with tabs[3]:
    run_pronunciation_practice(
        prefix="magic_e",
        title="🪄 Magic E 발음 연습",
        caption="Magic E가 붙었을 때 소리가 어떻게 바뀌는지 들어 봅시다.",
        guide_text="cap → cape, kit → kite처럼 짧은 소리와 긴 소리를 비교해 봅시다.",
        word_data=magic_e_words
    )

with tabs[4]:
    run_pronunciation_practice(
        prefix="blend",
        title="🤝 Blend 단어 발음 연습",
        caption="두 자음 소리가 함께 나는 단어를 듣고 따라 읽어 봅시다.",
        guide_text="bl, br, cl, tr처럼 두 자음 소리가 함께 나는 부분에 집중해 봅시다.",
        word_data=blend_words
    )

with tabs[5]:
    run_pronunciation_practice(
        prefix="digraph",
        title="👯 Digraph 단어 발음 연습",
        caption="두 글자가 만나 하나의 새 소리를 내는 단어를 듣고 따라 읽어 봅시다.",
        guide_text="sh, ch, th, ph처럼 두 글자가 하나의 소리를 만드는 부분에 집중해 봅시다.",
        word_data=digraph_words
    )

with tabs[6]:
    run_pronunciation_practice(
        prefix="vowel_team",
        title="🌊 Vowel Team 단어 발음 연습",
        caption="모음 두 개가 함께 만드는 소리를 듣고 따라 읽어 봅시다.",
        guide_text="ai, ay, ee, oa, oo처럼 모음 조합의 소리에 집중해 봅시다.",
        word_data=vowel_team_words
    )

with tabs[7]:
    run_pronunciation_practice(
        prefix="r_controlled",
        title="🚗 R-Controlled 단어 발음 연습",
        caption="모음 뒤에 r이 올 때 달라지는 소리를 듣고 따라 읽어 봅시다.",
        guide_text="ar, er, ir, or, ur 소리에 집중해 봅시다.",
        word_data=r_controlled_words
    )
