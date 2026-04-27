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
st.caption("단어를 보고 발음을 들은 뒤, 알맞은 소리나 패턴을 골라 봅시다.")

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
        <div>• 단어를 먼저 보고, <b>🔊 단어 듣기</b> 버튼을 눌러 발음을 들어 봅니다.</div>
        <div>• 그 단어에서 들리는 알맞은 소리나 글자 패턴을 고릅니다.</div>
        <div>• 개념을 외우는 문제보다, 실제 단어 발음을 듣고 소리와 철자를 연결하는 연습입니다.</div>
        <div>• 1차 제출 후 틀린 문제만 다시 풀고, 2차 제출 후 정답을 확인할 수 있습니다.</div>
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
# 문제 데이터
# =========================

practice_sets = {
    "① 자음 소리": [
        {"word": "bat", "question": "bat에서 처음 들리는 자음 소리는?", "answer": "b", "options": ["b", "d", "p", "t"]},
        {"word": "cat", "question": "cat에서 처음 들리는 자음 소리는?", "answer": "c / k", "options": ["c / k", "s", "g", "t"]},
        {"word": "dog", "question": "dog에서 처음 들리는 자음 소리는?", "answer": "d", "options": ["b", "d", "g", "t"]},
        {"word": "fish", "question": "fish에서 처음 들리는 자음 소리는?", "answer": "f", "options": ["f", "p", "v", "h"]},
        {"word": "goat", "question": "goat에서 처음 들리는 자음 소리는?", "answer": "g", "options": ["g", "k", "j", "d"]},
        {"word": "hat", "question": "hat에서 처음 들리는 자음 소리는?", "answer": "h", "options": ["h", "f", "k", "w"]},
        {"word": "jam", "question": "jam에서 처음 들리는 자음 소리는?", "answer": "j", "options": ["j", "g", "y", "z"]},
        {"word": "sun", "question": "sun에서 처음 들리는 자음 소리는?", "answer": "s", "options": ["s", "z", "sh", "ch"]},
        {"word": "van", "question": "van에서 처음 들리는 자음 소리는?", "answer": "v", "options": ["v", "f", "b", "w"]},
        {"word": "yes", "question": "yes에서 처음 들리는 자음 소리는?", "answer": "y", "options": ["y", "j", "w", "r"]},
    ],

    "② 짧은 모음": [
        {"word": "apple", "question": "apple에서 들리는 a 소리는?", "answer": "Short a", "options": ["Short a", "Long a", "Short e", "Long e"]},
        {"word": "cat", "question": "cat에서 들리는 a 소리는?", "answer": "Short a", "options": ["Short a", "Long a", "Short o", "Long o"]},
        {"word": "egg", "question": "egg에서 들리는 e 소리는?", "answer": "Short e", "options": ["Short e", "Long e", "Short i", "Long i"]},
        {"word": "bed", "question": "bed에서 들리는 e 소리는?", "answer": "Short e", "options": ["Short e", "Long e", "Short a", "Long a"]},
        {"word": "sit", "question": "sit에서 들리는 i 소리는?", "answer": "Short i", "options": ["Short i", "Long i", "Short e", "Long e"]},
        {"word": "pig", "question": "pig에서 들리는 i 소리는?", "answer": "Short i", "options": ["Short i", "Long i", "Short u", "Long u"]},
        {"word": "hot", "question": "hot에서 들리는 o 소리는?", "answer": "Short o", "options": ["Short o", "Long o", "Short a", "Long a"]},
        {"word": "cup", "question": "cup에서 들리는 u 소리는?", "answer": "Short u", "options": ["Short u", "Long u", "Short o", "Long o"]},
        {"word": "bus", "question": "bus에서 들리는 u 소리는?", "answer": "Short u", "options": ["Short u", "Long u", "Short i", "Long i"]},
        {"word": "fox", "question": "fox에서 들리는 o 소리는?", "answer": "Short o", "options": ["Short o", "Long o", "Short u", "Long u"]},
    ],

    "③ 긴 모음": [
        {"word": "cake", "question": "cake에서 들리는 a 소리는?", "answer": "Long a", "options": ["Long a", "Short a", "Long e", "Short e"]},
        {"word": "name", "question": "name에서 들리는 a 소리는?", "answer": "Long a", "options": ["Long a", "Short a", "Long i", "Short i"]},
        {"word": "tree", "question": "tree에서 들리는 ee 소리는?", "answer": "Long e", "options": ["Long e", "Short e", "Long a", "Short a"]},
        {"word": "see", "question": "see에서 들리는 ee 소리는?", "answer": "Long e", "options": ["Long e", "Short e", "Long i", "Short i"]},
        {"word": "bike", "question": "bike에서 들리는 i 소리는?", "answer": "Long i", "options": ["Long i", "Short i", "Long e", "Short e"]},
        {"word": "five", "question": "five에서 들리는 i 소리는?", "answer": "Long i", "options": ["Long i", "Short i", "Long o", "Short o"]},
        {"word": "rope", "question": "rope에서 들리는 o 소리는?", "answer": "Long o", "options": ["Long o", "Short o", "Long a", "Short a"]},
        {"word": "home", "question": "home에서 들리는 o 소리는?", "answer": "Long o", "options": ["Long o", "Short o", "Long u", "Short u"]},
        {"word": "cube", "question": "cube에서 들리는 u 소리는?", "answer": "Long u", "options": ["Long u", "Short u", "Long o", "Short o"]},
        {"word": "cute", "question": "cute에서 들리는 u 소리는?", "answer": "Long u", "options": ["Long u", "Short u", "Long e", "Short e"]},
    ],

    "④ 모음 예외": [
        {"word": "ball", "question": "ball에서 a는 어떤 소리에 가깝게 들리나요?", "answer": "aw 소리", "options": ["aw 소리", "Short a", "Long a", "Long e"]},
        {"word": "call", "question": "call에서 a는 어떤 소리에 가깝게 들리나요?", "answer": "aw 소리", "options": ["aw 소리", "Short a", "Long a", "Short i"]},
        {"word": "car", "question": "car에서 ar은 어떤 소리에 가깝게 들리나요?", "answer": "ar 소리", "options": ["ar 소리", "Short a", "Long a", "ee 소리"]},
        {"word": "father", "question": "father에서 a는 어떤 소리에 가깝게 들리나요?", "answer": "ah 소리", "options": ["ah 소리", "Short a", "Long a", "Short e"]},
        {"word": "about", "question": "about의 첫 a는 어떤 소리에 가깝게 약하게 들리나요?", "answer": "uh 소리", "options": ["uh 소리", "Long a", "Short a", "ee 소리"]},
        {"word": "love", "question": "love에서 o는 어떤 소리에 가깝게 들리나요?", "answer": "uh 소리", "options": ["uh 소리", "Long o", "Short o", "ee 소리"]},
        {"word": "do", "question": "do에서 o는 어떤 소리에 가깝게 들리나요?", "answer": "oo 소리", "options": ["oo 소리", "Short o", "Long o", "Short u"]},
        {"word": "book", "question": "book에서 oo는 어떤 소리인가요?", "answer": "짧은 oo", "options": ["짧은 oo", "긴 oo", "Long a", "Short a"]},
        {"word": "moon", "question": "moon에서 oo는 어떤 소리인가요?", "answer": "긴 oo", "options": ["긴 oo", "짧은 oo", "Short e", "Long i"]},
        {"word": "bread", "question": "bread에서 ea는 어떤 소리에 가깝게 들리나요?", "answer": "eh 소리", "options": ["eh 소리", "ee 소리", "ay 소리", "ow 소리"]},
    ],

    "⑤ Blends": [
        {"word": "black", "question": "black에 들어 있는 blend는?", "answer": "bl", "options": ["bl", "br", "cl", "cr"]},
        {"word": "brown", "question": "brown에 들어 있는 blend는?", "answer": "br", "options": ["br", "bl", "gr", "tr"]},
        {"word": "clock", "question": "clock에 들어 있는 blend는?", "answer": "cl", "options": ["cl", "cr", "fl", "gl"]},
        {"word": "crab", "question": "crab에 들어 있는 blend는?", "answer": "cr", "options": ["cr", "cl", "dr", "fr"]},
        {"word": "drum", "question": "drum에 들어 있는 blend는?", "answer": "dr", "options": ["dr", "tr", "br", "gr"]},
        {"word": "flag", "question": "flag에 들어 있는 blend는?", "answer": "fl", "options": ["fl", "fr", "pl", "sl"]},
        {"word": "frog", "question": "frog에 들어 있는 blend는?", "answer": "fr", "options": ["fr", "fl", "gr", "br"]},
        {"word": "green", "question": "green에 들어 있는 blend는?", "answer": "gr", "options": ["gr", "gl", "br", "tr"]},
        {"word": "spoon", "question": "spoon에 들어 있는 blend는?", "answer": "sp", "options": ["sp", "st", "sn", "sl"]},
        {"word": "star", "question": "star에 들어 있는 blend는?", "answer": "st", "options": ["st", "sp", "sk", "sm"]},
    ],

    "⑥ Digraphs": [
        {"word": "chair", "question": "chair에 들어 있는 digraph는?", "answer": "ch", "options": ["ch", "sh", "th", "ph"]},
        {"word": "ship", "question": "ship에 들어 있는 digraph는?", "answer": "sh", "options": ["sh", "ch", "th", "ck"]},
        {"word": "three", "question": "three에 들어 있는 digraph는?", "answer": "th", "options": ["th", "sh", "ch", "ph"]},
        {"word": "this", "question": "this에 들어 있는 digraph는?", "answer": "th", "options": ["th", "ch", "sh", "wh"]},
        {"word": "phone", "question": "phone에 들어 있는 digraph는?", "answer": "ph", "options": ["ph", "sh", "ch", "th"]},
        {"word": "whale", "question": "whale에 들어 있는 digraph는?", "answer": "wh", "options": ["wh", "ph", "sh", "ch"]},
        {"word": "duck", "question": "duck에 들어 있는 digraph는?", "answer": "ck", "options": ["ck", "ch", "sh", "th"]},
        {"word": "shop", "question": "shop에 들어 있는 digraph는?", "answer": "sh", "options": ["sh", "ch", "ph", "wh"]},
        {"word": "cheese", "question": "cheese에 들어 있는 digraph는?", "answer": "ch", "options": ["ch", "sh", "th", "ck"]},
        {"word": "photo", "question": "photo에 들어 있는 digraph는?", "answer": "ph", "options": ["ph", "th", "ch", "sh"]},
    ],

    "⑦ Vowel Teams": [
        {"word": "rain", "question": "rain에 들어 있는 vowel team은?", "answer": "ai", "options": ["ai", "ay", "ee", "oa"]},
        {"word": "day", "question": "day에 들어 있는 vowel team은?", "answer": "ay", "options": ["ay", "ai", "oi", "oy"]},
        {"word": "see", "question": "see에 들어 있는 vowel team은?", "answer": "ee", "options": ["ee", "ea", "ai", "oa"]},
        {"word": "eat", "question": "eat에 들어 있는 vowel team은?", "answer": "ea", "options": ["ea", "ee", "ai", "ay"]},
        {"word": "boat", "question": "boat에 들어 있는 vowel team은?", "answer": "oa", "options": ["oa", "ow", "ou", "oi"]},
        {"word": "snow", "question": "snow에 들어 있는 vowel team은?", "answer": "ow", "options": ["ow", "oa", "ou", "oy"]},
        {"word": "cow", "question": "cow에 들어 있는 vowel team은?", "answer": "ow", "options": ["ow", "ou", "oa", "oi"]},
        {"word": "house", "question": "house에 들어 있는 vowel team은?", "answer": "ou", "options": ["ou", "ow", "oi", "oy"]},
        {"word": "coin", "question": "coin에 들어 있는 vowel team은?", "answer": "oi", "options": ["oi", "oy", "ai", "ay"]},
        {"word": "boy", "question": "boy에 들어 있는 vowel team은?", "answer": "oy", "options": ["oy", "oi", "ow", "ou"]},
    ],

    "⑧ R-Controlled": [
        {"word": "car", "question": "car에 들어 있는 r-controlled pattern은?", "answer": "ar", "options": ["ar", "er", "ir", "or"]},
        {"word": "star", "question": "star에 들어 있는 r-controlled pattern은?", "answer": "ar", "options": ["ar", "ur", "or", "er"]},
        {"word": "her", "question": "her에 들어 있는 r-controlled pattern은?", "answer": "er", "options": ["er", "ir", "ur", "ar"]},
        {"word": "bird", "question": "bird에 들어 있는 r-controlled pattern은?", "answer": "ir", "options": ["ir", "er", "ur", "or"]},
        {"word": "girl", "question": "girl에 들어 있는 r-controlled pattern은?", "answer": "ir", "options": ["ir", "er", "ar", "or"]},
        {"word": "corn", "question": "corn에 들어 있는 r-controlled pattern은?", "answer": "or", "options": ["or", "ar", "er", "ur"]},
        {"word": "fork", "question": "fork에 들어 있는 r-controlled pattern은?", "answer": "or", "options": ["or", "ar", "ir", "er"]},
        {"word": "turn", "question": "turn에 들어 있는 r-controlled pattern은?", "answer": "ur", "options": ["ur", "er", "ir", "or"]},
        {"word": "burn", "question": "burn에 들어 있는 r-controlled pattern은?", "answer": "ur", "options": ["ur", "ir", "er", "ar"]},
        {"word": "teacher", "question": "teacher 끝부분에 들어 있는 r-controlled pattern은?", "answer": "er", "options": ["er", "ar", "or", "ir"]},
    ],

    "⑨ Silent e": [
        {"word": "cake", "question": "cake에서 긴 모음 소리를 만드는 패턴은?", "answer": "a_e", "options": ["a_e", "i_e", "o_e", "u_e"]},
        {"word": "name", "question": "name에서 긴 모음 소리를 만드는 패턴은?", "answer": "a_e", "options": ["a_e", "i_e", "o_e", "u_e"]},
        {"word": "bike", "question": "bike에서 긴 모음 소리를 만드는 패턴은?", "answer": "i_e", "options": ["i_e", "a_e", "o_e", "u_e"]},
        {"word": "five", "question": "five에서 긴 모음 소리를 만드는 패턴은?", "answer": "i_e", "options": ["i_e", "a_e", "e_e", "o_e"]},
        {"word": "home", "question": "home에서 긴 모음 소리를 만드는 패턴은?", "answer": "o_e", "options": ["o_e", "a_e", "i_e", "u_e"]},
        {"word": "rope", "question": "rope에서 긴 모음 소리를 만드는 패턴은?", "answer": "o_e", "options": ["o_e", "i_e", "a_e", "u_e"]},
        {"word": "cube", "question": "cube에서 긴 모음 소리를 만드는 패턴은?", "answer": "u_e", "options": ["u_e", "a_e", "i_e", "o_e"]},
        {"word": "cute", "question": "cute에서 긴 모음 소리를 만드는 패턴은?", "answer": "u_e", "options": ["u_e", "a_e", "i_e", "o_e"]},
        {"word": "make", "question": "make에서 긴 모음 소리를 만드는 패턴은?", "answer": "a_e", "options": ["a_e", "i_e", "o_e", "u_e"]},
        {"word": "hope", "question": "hope에서 긴 모음 소리를 만드는 패턴은?", "answer": "o_e", "options": ["o_e", "a_e", "i_e", "u_e"]},
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


# =========================
# 문제 출력 함수
# =========================
def show_quiz(tab_name, questions):
    init_tab_state(tab_name)

    st.subheader(tab_name)
    st.write("단어를 보고 발음을 들은 뒤, 알맞은 답을 고르세요.")

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
            st.markdown(f"### {i + 1}. {q['word']}")
            audio_button("🔊 단어 듣기", q["word"], key=f"{tab_name}_audio1_{i}")

            # 보기 순서는 고정하되, 문제별로 적당히 섞인 상태를 유지
            st.radio(
                q["question"],
                q["options"],
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
    # 1차 결과
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

            for count, i in enumerate(wrong_indices):
                q = questions[i]
                st.markdown("---")
                st.markdown(f"### {i + 1}. {q['word']}")
                audio_button("🔊 단어 듣기", q["word"], key=f"{tab_name}_audio2_{i}")

                st.radio(
                    q["question"],
                    q["options"],
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

        first_score = len(questions) - len(wrong_indices)
        second_score = len(questions) - len(second_wrong)

        st.success(f"🎉 최종 결과: {second_score} / {len(questions)}점")

        if len(second_wrong) == 0:
            st.balloons()
            st.success("좋습니다! 2차 도전까지 통해 모두 해결했습니다.")
        else:
            st.warning("아래에서 정답을 확인해 봅시다.")

        st.markdown("### ✅ 정답 확인")

        for i in wrong_indices:
            q = questions[i]
            user_answer_1 = st.session_state.get(f"{tab_name}_q1_{i}")
            user_answer_2 = st.session_state.get(f"{tab_name}_q2_{i}")

            st.markdown("---")
            st.markdown(f"### {i + 1}. {q['word']}")
            audio_button("🔊 단어 다시 듣기", q["word"], key=f"{tab_name}_audio_answer_{i}")
            st.write(f"문제: {q['question']}")
            st.write(f"1차 선택: {user_answer_1}")
            st.write(f"2차 선택: {user_answer_2}")
            st.success(f"정답: {q['answer']}")

        if st.button("🔄 다시 풀기", key=f"{tab_name}_reset"):
            reset_quiz(tab_name)
            st.rerun()


def reset_quiz(tab_name):
    keys_to_delete = []
    for key in st.session_state.keys():
        if key.startswith(tab_name):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del st.session_state[key]


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(practice_sets.keys()))

for tab, tab_name in zip(tabs, practice_sets.keys()):
    with tab:
        show_quiz(tab_name, practice_sets[tab_name])
