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
st.caption("스펠링을 보고 먼저 말해 본 뒤, 원어민 발음을 듣고 따라 말해 봅시다.")

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
        <div>3. 다시 한 번 따라 말합니다.</div>
        <div>4. 스스로 잘 읽었는지 체크합니다.</div>
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
        "bat", "cat", "dog", "fish", "goat",
        "hat", "jam", "sun", "van", "yes"
    ],

    "② 짧은 모음": [
        "apple", "cat", "egg", "bed", "sit",
        "pig", "hot", "cup", "bus", "fox"
    ],

    "③ 긴 모음": [
        "cake", "name", "tree", "see", "bike",
        "five", "rope", "home", "cube", "cute"
    ],

    "④ 모음 예외": [
        "ball", "call", "car", "father", "about",
        "love", "do", "book", "moon", "bread"
    ],

    "⑤ Blends": [
        "black", "brown", "clock", "crab", "drum",
        "flag", "frog", "green", "spoon", "star"
    ],

    "⑥ Digraphs": [
        "chair", "ship", "three", "this", "phone",
        "whale", "duck", "shop", "cheese", "photo"
    ],

    "⑦ Vowel Teams": [
        "rain", "day", "see", "eat", "boat",
        "snow", "cow", "house", "coin", "boy"
    ],

    "⑧ R-Controlled": [
        "car", "star", "her", "bird", "girl",
        "corn", "fork", "turn", "burn", "teacher"
    ],

    "⑨ Silent e": [
        "cake", "name", "bike", "five", "home",
        "rope", "cube", "cute", "make", "hope"
    ],
}


# =========================
# 세션 상태 초기화
# =========================
def init_tab_state(tab_name, words):
    for i in range(len(words)):
        key = f"{tab_name}_check_{i}"
        if key not in st.session_state:
            st.session_state[key] = False


def reset_tab(tab_name):
    keys_to_delete = []
    for key in st.session_state.keys():
        if key.startswith(tab_name):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del st.session_state[key]


# =========================
# 말하기 연습 출력 함수
# =========================
def show_speaking_practice(tab_name, words):
    init_tab_state(tab_name, words)

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
            👀 <b>먼저 단어를 보고 직접 읽어 보세요.</b><br>
            그 다음 원어민 발음을 듣고, 다시 한 번 따라 말해 봅니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    total = len(words)
    checked = sum(
        1 for i in range(total)
        if st.session_state.get(f"{tab_name}_check_{i}", False)
    )

    st.progress(checked / total)
    st.write(f"✅ 연습 완료: **{checked} / {total}개**")

    for i, word in enumerate(words):
        st.markdown("---")

        col1, col2 = st.columns([2, 3])

        with col1:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #e0f2fe, #fef3c7);
                    border-radius:22px;
                    padding:28px 20px;
                    text-align:center;
                    box-shadow:0 4px 10px rgba(0,0,0,0.08);
                ">
                    <div style="font-size:18px; font-weight:700; color:#555;">
                        Word {i + 1}
                    </div>
                    <div style="font-size:48px; font-weight:900; color:#111827; margin-top:10px;">
                        {word}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown("### 1단계: 먼저 직접 말하기")
            st.write("단어를 보고 선생님 또는 친구 앞에서 먼저 읽어 보세요.")

            st.markdown("### 2단계: 원어민 발음 확인")
            play_audio(word, key=f"{tab_name}_audio_{i}")

            st.markdown("### 3단계: 따라 말하고 체크")
            st.checkbox(
                "따라 말하기 완료!",
                key=f"{tab_name}_check_{i}"
            )

    st.markdown("---")

    checked = sum(
        1 for i in range(total)
        if st.session_state.get(f"{tab_name}_check_{i}", False)
    )

    if checked == total:
        st.balloons()
        st.success("🎉 모든 단어 말하기 연습을 완료했습니다! 아주 좋습니다!")
    else:
        st.info(f"조금만 더 해 봅시다! 아직 {total - checked}개가 남았습니다.")

    if st.button("🔄 이 탭 다시 연습하기", key=f"{tab_name}_reset"):
        reset_tab(tab_name)
        st.rerun()


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(practice_sets.keys()))

for tab, tab_name in zip(tabs, practice_sets.keys()):
    with tab:
        show_speaking_practice(tab_name, practice_sets[tab_name])
