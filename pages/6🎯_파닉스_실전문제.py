import streamlit as st
import random
import io
from gtts import gTTS

st.set_page_config(page_title="Phonics Practice", layout="centered")

st.title("🎯 Phonics Practice")
st.caption("소리를 듣고, 글자와 단어의 규칙을 맞혀 봅시다.")


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
# 공통 결과 메시지
# =========================================================
def show_result_message(score, total):
    if score == total:
        st.success("만점입니다! 파닉스 감각이 아주 좋습니다! 🎉")
        st.balloons()
    elif score >= total * 0.8:
        st.success("아주 잘했습니다! 소리와 글자의 관계를 잘 이해하고 있어요.")
    elif score >= total * 0.6:
        st.info("좋습니다. 헷갈린 문제만 다시 보면 더 좋아질 수 있습니다.")
    else:
        st.warning("괜찮습니다. 파닉스는 반복해서 듣고 읽으면 금방 익숙해집니다.")


# =========================================================
# 공통 퀴즈 함수
# =========================================================
def run_phonics_quiz(prefix, title, caption, guide_text, question_data):
    total = len(question_data)

    st.subheader(title)
    st.caption(caption)
    st.info(guide_text)

    if f"{prefix}_data" not in st.session_state:
        quiz_data = question_data.copy()
        random.shuffle(quiz_data)
        st.session_state[f"{prefix}_data"] = quiz_data

    if f"{prefix}_stage" not in st.session_state:
        st.session_state[f"{prefix}_stage"] = 1

    if f"{prefix}_first_score" not in st.session_state:
        st.session_state[f"{prefix}_first_score"] = 0

    if f"{prefix}_second_score" not in st.session_state:
        st.session_state[f"{prefix}_second_score"] = 0

    if f"{prefix}_final_score" not in st.session_state:
        st.session_state[f"{prefix}_final_score"] = 0

    if f"{prefix}_wrong_indices" not in st.session_state:
        st.session_state[f"{prefix}_wrong_indices"] = []

    if f"{prefix}_final_wrong_indices" not in st.session_state:
        st.session_state[f"{prefix}_final_wrong_indices"] = []

    if st.button("처음부터 다시 시작", key=f"reset_{prefix}"):
        for key in list(st.session_state.keys()):
            if (
                key.startswith(f"{prefix}_")
                or key.startswith(f"q1_{prefix}_")
                or key.startswith(f"q2_{prefix}_")
            ):
                del st.session_state[key]
        st.rerun()

    st.markdown("---")

    quiz_data = st.session_state[f"{prefix}_data"]
    stage = st.session_state[f"{prefix}_stage"]

    # =====================================================
    # 1단계: 1차 풀이
    # =====================================================
    if stage == 1:
        st.subheader("1차 풀이")
        st.caption("문제를 보고 알맞은 답을 고르세요.")

        for i, item in enumerate(quiz_data):
            st.markdown(f"### {i+1}. {item['question']}")

            if item.get("audio"):
                st.write("🔊 소리를 먼저 들어 보세요.")
                play_audio(item["audio"])

            st.radio(
                "정답을 고르세요.",
                item["choices"],
                key=f"q1_{prefix}_{i}",
                index=None
            )

            st.markdown("---")

        if st.button("1차 제출", key=f"submit_1_{prefix}"):
            correct_count = 0
            wrong_indices = []

            for i, item in enumerate(quiz_data):
                user_answer = st.session_state.get(f"q1_{prefix}_{i}")

                if user_answer == item["answer"]:
                    correct_count += 1
                else:
                    wrong_indices.append(i)

            st.session_state[f"{prefix}_first_score"] = correct_count
            st.session_state[f"{prefix}_wrong_indices"] = wrong_indices
            st.session_state[f"{prefix}_stage"] = 1.5
            st.rerun()

    # =====================================================
    # 1.5단계: 1차 결과
    # =====================================================
    elif stage == 1.5:
        first_score = st.session_state[f"{prefix}_first_score"]
        wrong_indices = st.session_state[f"{prefix}_wrong_indices"]
        wrong_count = len(wrong_indices)

        st.subheader("🎉 1차 풀이 완료!")
        st.write(f"1차 점수: **{first_score} / {total}**")
        st.write(f"다시 풀 문제: **{wrong_count}문제**")
        st.progress(first_score / total)

        if wrong_count == 0:
            st.success("완벽합니다! 바로 정답을 확인해 봅시다.")
            st.balloons()

            if st.button("최종 결과 보기", key=f"final_after_first_{prefix}"):
                st.session_state[f"{prefix}_final_score"] = total
                st.session_state[f"{prefix}_second_score"] = 0
                st.session_state[f"{prefix}_final_wrong_indices"] = []
                st.session_state[f"{prefix}_stage"] = 3
                st.rerun()
        else:
            st.info("틀린 문제만 한 번 더 풀어 봅시다.")

            if st.button("2차 오답 다시 풀기", key=f"go_second_{prefix}"):
                st.session_state[f"{prefix}_stage"] = 2
                st.rerun()

    # =====================================================
    # 2단계: 오답 다시 풀기
    # =====================================================
    elif stage == 2:
        wrong_indices = st.session_state[f"{prefix}_wrong_indices"]

        st.subheader("2차 풀이")
        st.caption("1차에서 틀린 문제만 다시 풉니다.")

        for idx in wrong_indices:
            item = quiz_data[idx]

            st.markdown(f"### {idx+1}. {item['question']}")

            if item.get("audio"):
                st.write("🔊 다시 들어 보세요.")
                play_audio(item["audio"])

            st.radio(
                "다시 정답을 고르세요.",
                item["choices"],
                key=f"q2_{prefix}_{idx}",
                index=None
            )

            st.markdown("---")

        if st.button("2차 제출", key=f"submit_2_{prefix}"):
            additional_correct = 0
            final_wrong_indices = []

            for idx in wrong_indices:
                item = quiz_data[idx]
                user_answer = st.session_state.get(f"q2_{prefix}_{idx}")

                if user_answer == item["answer"]:
                    additional_correct += 1
                else:
                    final_wrong_indices.append(idx)

            st.session_state[f"{prefix}_second_score"] = additional_correct
            st.session_state[f"{prefix}_final_score"] = (
                st.session_state[f"{prefix}_first_score"] + additional_correct
            )
            st.session_state[f"{prefix}_final_wrong_indices"] = final_wrong_indices
            st.session_state[f"{prefix}_stage"] = 2.5
            st.rerun()

    # =====================================================
    # 2.5단계: 2차 결과
    # =====================================================
    elif stage == 2.5:
        final_score = st.session_state[f"{prefix}_final_score"]
        second_score = st.session_state[f"{prefix}_second_score"]
        retry_total = len(st.session_state[f"{prefix}_wrong_indices"])

        st.subheader("🌟 2차 풀이 완료!")
        st.write(f"2차에서 **{retry_total}문제 중 {second_score}문제**를 다시 맞혔습니다.")
        st.write(f"현재 최종 점수: **{final_score} / {total}**")
        st.progress(final_score / total)

        st.success("끝까지 다시 도전한 것이 정말 멋집니다!")

        if st.button("최종 결과와 정답 확인하기", key=f"go_final_{prefix}"):
            st.session_state[f"{prefix}_stage"] = 3
            st.rerun()

    # =====================================================
    # 3단계: 최종 결과 + 정답 확인
    # =====================================================
    elif stage == 3:
        first_score = st.session_state[f"{prefix}_first_score"]
        second_score = st.session_state[f"{prefix}_second_score"]
        final_score = st.session_state[f"{prefix}_final_score"]
        final_wrong_indices = st.session_state[f"{prefix}_final_wrong_indices"]

        st.subheader("최종 결과")
        st.write(f"1차 점수: **{first_score} / {total}**")
        st.write(f"2차에서 다시 맞힌 문제 수: **{second_score}문제**")
        st.write(f"최종 점수: **{final_score} / {total}**")

        show_result_message(final_score, total)

        st.markdown("---")
        st.subheader("📌 정답 확인")

        for i, item in enumerate(quiz_data):
            first_answer = st.session_state.get(f"q1_{prefix}_{i}")
            second_answer = st.session_state.get(f"q2_{prefix}_{i}")

            st.markdown(f"### {i+1}. {item['question']}")

            if item.get("audio"):
                st.write("🔊 문제 소리 다시 듣기")
                play_audio(item["audio"])

            st.write(f"- 정답: **{item['answer']}**")

            if second_answer:
                st.write(f"- 1차 선택: {first_answer if first_answer else '미응답'}")
                st.write(f"- 2차 선택: {second_answer if second_answer else '미응답'}")

                if i in final_wrong_indices:
                    st.error("최종 오답")
                else:
                    st.success("2차에서 정답")
            else:
                st.write(f"- 선택: {first_answer if first_answer else '미응답'}")

                if first_answer == item["answer"]:
                    st.success("1차에서 정답")
                else:
                    st.error("오답")

            if item.get("explanation"):
                st.info(item["explanation"])

            st.markdown("---")


# =========================================================
# 문제 데이터 1: 자음 소리
# =========================================================
consonant_questions = [
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "bat",
        "answer": "b",
        "choices": ["b", "d"],
        "explanation": "bat은 /b/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "dog",
        "answer": "d",
        "choices": ["d", "t"],
        "explanation": "dog은 /d/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "fish",
        "answer": "f",
        "choices": ["f", "v"],
        "explanation": "fish는 /f/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "sun",
        "answer": "s",
        "choices": ["s", "z"],
        "explanation": "sun은 /s/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "van",
        "answer": "v",
        "choices": ["v", "f"],
        "explanation": "van은 /v/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "red",
        "answer": "r",
        "choices": ["r", "l"],
        "explanation": "red는 /r/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "leg",
        "answer": "l",
        "choices": ["l", "r"],
        "explanation": "leg는 /l/ 소리로 시작합니다."
    },
    {
        "question": "소리를 듣고, 단어의 첫 글자로 알맞은 자음을 고르세요.",
        "audio": "zip",
        "answer": "z",
        "choices": ["z", "s"],
        "explanation": "zip은 /z/ 소리로 시작합니다."
    },
]


# =========================================================
# 문제 데이터 2: 단모음
# =========================================================
short_vowel_questions = [
    {
        "question": "cat의 모음 소리로 알맞은 것은?",
        "audio": "cat",
        "answer": "short a",
        "choices": ["short a", "long a"],
        "explanation": "cat의 a는 짧은 /a/ 소리입니다."
    },
    {
        "question": "bed의 모음 소리로 알맞은 것은?",
        "audio": "bed",
        "answer": "short e",
        "choices": ["short e", "long e"],
        "explanation": "bed의 e는 짧은 /e/ 소리입니다."
    },
    {
        "question": "sit의 모음 소리로 알맞은 것은?",
        "audio": "sit",
        "answer": "short i",
        "choices": ["short i", "long i"],
        "explanation": "sit의 i는 짧은 /i/ 소리입니다."
    },
    {
        "question": "hot의 모음 소리로 알맞은 것은?",
        "audio": "hot",
        "answer": "short o",
        "choices": ["short o", "long o"],
        "explanation": "hot의 o는 짧은 /o/ 소리입니다."
    },
    {
        "question": "cup의 모음 소리로 알맞은 것은?",
        "audio": "cup",
        "answer": "short u",
        "choices": ["short u", "long u"],
        "explanation": "cup의 u는 짧은 /u/ 소리입니다."
    },
    {
        "question": "fish의 모음 소리로 알맞은 것은?",
        "audio": "fish",
        "answer": "short i",
        "choices": ["short i", "long i"],
        "explanation": "fish의 i는 짧은 /i/ 소리입니다."
    },
    {
        "question": "bag의 모음 소리로 알맞은 것은?",
        "audio": "bag",
        "answer": "short a",
        "choices": ["short a", "long a"],
        "explanation": "bag의 a는 짧은 /a/ 소리입니다."
    },
    {
        "question": "sun의 모음 소리로 알맞은 것은?",
        "audio": "sun",
        "answer": "short u",
        "choices": ["short u", "long u"],
        "explanation": "sun의 u는 짧은 /u/ 소리입니다."
    },
]


# =========================================================
# 문제 데이터 3: 장모음
# =========================================================
long_vowel_questions = [
    {
        "question": "cake의 모음 소리로 알맞은 것은?",
        "audio": "cake",
        "answer": "long a",
        "choices": ["long a", "short a"],
        "explanation": "cake의 a는 이름처럼 길게 나는 long a 소리입니다."
    },
    {
        "question": "bike의 모음 소리로 알맞은 것은?",
        "audio": "bike",
        "answer": "long i",
        "choices": ["long i", "short i"],
        "explanation": "bike의 i는 long i 소리입니다."
    },
    {
        "question": "home의 모음 소리로 알맞은 것은?",
        "audio": "home",
        "answer": "long o",
        "choices": ["long o", "short o"],
        "explanation": "home의 o는 long o 소리입니다."
    },
    {
        "question": "cute의 모음 소리로 알맞은 것은?",
        "audio": "cute",
        "answer": "long u",
        "choices": ["long u", "short u"],
        "explanation": "cute의 u는 long u 소리입니다."
    },
    {
        "question": "tree의 모음 소리로 알맞은 것은?",
        "audio": "tree",
        "answer": "long e",
        "choices": ["long e", "short e"],
        "explanation": "tree의 ee는 long e 소리입니다."
    },
    {
        "question": "rain의 모음 소리로 알맞은 것은?",
        "audio": "rain",
        "answer": "long a",
        "choices": ["long a", "short a"],
        "explanation": "rain의 ai는 long a 소리입니다."
    },
    {
        "question": "boat의 모음 소리로 알맞은 것은?",
        "audio": "boat",
        "answer": "long o",
        "choices": ["long o", "short o"],
        "explanation": "boat의 oa는 long o 소리입니다."
    },
    {
        "question": "five의 모음 소리로 알맞은 것은?",
        "audio": "five",
        "answer": "long i",
        "choices": ["long i", "short i"],
        "explanation": "five의 i는 long i 소리입니다."
    },
]


# =========================================================
# 문제 데이터 4: Magic E
# =========================================================
magic_e_questions = [
    {
        "question": "cap에 Magic E가 붙으면 어떤 단어가 되나요?",
        "audio": "cap, cape",
        "answer": "cape",
        "choices": ["cape", "caped"],
        "explanation": "cap + e = cape입니다. a가 long a 소리로 바뀝니다."
    },
    {
        "question": "kit에 Magic E가 붙으면 어떤 단어가 되나요?",
        "audio": "kit, kite",
        "answer": "kite",
        "choices": ["kite", "kited"],
        "explanation": "kit + e = kite입니다. i가 long i 소리로 바뀝니다."
    },
    {
        "question": "hop에 Magic E가 붙으면 어떤 단어가 되나요?",
        "audio": "hop, hope",
        "answer": "hope",
        "choices": ["hope", "hoping"],
        "explanation": "hop + e = hope입니다. o가 long o 소리로 바뀝니다."
    },
    {
        "question": "cut에 Magic E가 붙으면 어떤 단어가 되나요?",
        "audio": "cut, cute",
        "answer": "cute",
        "choices": ["cute", "cuted"],
        "explanation": "cut + e = cute입니다. u가 long u 소리로 바뀝니다."
    },
    {
        "question": "tap에 Magic E가 붙으면 어떤 단어가 되나요?",
        "audio": "tap, tape",
        "answer": "tape",
        "choices": ["tape", "taped"],
        "explanation": "tap + e = tape입니다."
    },
    {
        "question": "bit에 Magic E가 붙으면 어떤 단어가 되나요?",
        "audio": "bit, bite",
        "answer": "bite",
        "choices": ["bite", "bited"],
        "explanation": "bit + e = bite입니다."
    },
]


# =========================================================
# 문제 데이터 5: Blends & Digraphs
# =========================================================
blend_digraph_questions = [
    {
        "question": "black의 처음 소리로 알맞은 것은?",
        "audio": "black",
        "answer": "bl",
        "choices": ["bl", "br"],
        "explanation": "black은 bl 소리로 시작합니다."
    },
    {
        "question": "train의 처음 소리로 알맞은 것은?",
        "audio": "train",
        "answer": "tr",
        "choices": ["tr", "dr"],
        "explanation": "train은 tr 소리로 시작합니다."
    },
    {
        "question": "frog의 처음 소리로 알맞은 것은?",
        "audio": "frog",
        "answer": "fr",
        "choices": ["fr", "fl"],
        "explanation": "frog는 fr 소리로 시작합니다."
    },
    {
        "question": "ship의 처음 소리로 알맞은 것은?",
        "audio": "ship",
        "answer": "sh",
        "choices": ["sh", "ch"],
        "explanation": "ship은 sh 소리로 시작합니다."
    },
    {
        "question": "chair의 처음 소리로 알맞은 것은?",
        "audio": "chair",
        "answer": "ch",
        "choices": ["ch", "sh"],
        "explanation": "chair는 ch 소리로 시작합니다."
    },
    {
        "question": "phone에서 ph의 소리로 알맞은 것은?",
        "audio": "phone",
        "answer": "f",
        "choices": ["f", "p"],
        "explanation": "phone의 ph는 /f/ 소리입니다."
    },
    {
        "question": "duck에서 ck의 소리로 알맞은 것은?",
        "audio": "duck",
        "answer": "k",
        "choices": ["k", "ch"],
        "explanation": "duck의 ck는 /k/ 소리입니다."
    },
    {
        "question": "smile의 처음 소리로 알맞은 것은?",
        "audio": "smile",
        "answer": "sm",
        "choices": ["sm", "sn"],
        "explanation": "smile은 sm 소리로 시작합니다."
    },
]


# =========================================================
# 문제 데이터 6: Vowel Teams
# =========================================================
vowel_team_questions = [
    {
        "question": "rain에서 long a 소리를 만드는 철자는?",
        "audio": "rain",
        "answer": "ai",
        "choices": ["ai", "ea"],
        "explanation": "rain의 ai는 long a 소리입니다."
    },
    {
        "question": "play에서 long a 소리를 만드는 철자는?",
        "audio": "play",
        "answer": "ay",
        "choices": ["ay", "oy"],
        "explanation": "play의 ay는 long a 소리입니다."
    },
    {
        "question": "tree에서 long e 소리를 만드는 철자는?",
        "audio": "tree",
        "answer": "ee",
        "choices": ["ee", "oo"],
        "explanation": "tree의 ee는 long e 소리입니다."
    },
    {
        "question": "boat에서 long o 소리를 만드는 철자는?",
        "audio": "boat",
        "answer": "oa",
        "choices": ["oa", "ai"],
        "explanation": "boat의 oa는 long o 소리입니다."
    },
    {
        "question": "coin에서 /oi/ 소리를 만드는 철자는?",
        "audio": "coin",
        "answer": "oi",
        "choices": ["oi", "ou"],
        "explanation": "coin의 oi는 /oi/ 소리입니다."
    },
    {
        "question": "boy에서 /oy/ 소리를 만드는 철자는?",
        "audio": "boy",
        "answer": "oy",
        "choices": ["oy", "ay"],
        "explanation": "boy의 oy는 /oy/ 소리입니다."
    },
    {
        "question": "moon에서 /oo/ 소리를 만드는 철자는?",
        "audio": "moon",
        "answer": "oo",
        "choices": ["oo", "oa"],
        "explanation": "moon의 oo는 긴 /oo/ 소리입니다."
    },
    {
        "question": "cow에서 /ow/ 소리를 만드는 철자는?",
        "audio": "cow",
        "answer": "ow",
        "choices": ["ow", "oa"],
        "explanation": "cow의 ow는 /ow/ 소리입니다."
    },
]


# =========================================================
# 탭 구성
# =========================================================
tabs = st.tabs([
    "🧩 자음",
    "🍎 단모음",
    "🌟 장모음",
    "🪄 Magic E",
    "🤝 Blends & Digraphs",
    "🌊 Vowel Teams"
])


# =========================================================
# 탭 실행
# =========================================================
with tabs[0]:
    run_phonics_quiz(
        prefix="consonant",
        title="🧩 자음 소리 문제",
        caption="소리를 듣고 알맞은 첫 자음을 고르세요.",
        guide_text="알파벳 이름과 실제 소리는 다릅니다. 단어의 첫소리를 잘 들어 보세요.",
        question_data=consonant_questions
    )

with tabs[1]:
    run_phonics_quiz(
        prefix="short_vowel",
        title="🍎 단모음 문제",
        caption="단어를 듣고 짧은 모음 소리를 고르세요.",
        guide_text="단모음은 CVC 단어에서 자주 나옵니다. 예: cat, bed, sit, hot, cup",
        question_data=short_vowel_questions
    )

with tabs[2]:
    run_phonics_quiz(
        prefix="long_vowel",
        title="🌟 장모음 문제",
        caption="단어를 듣고 긴 모음 소리를 고르세요.",
        guide_text="장모음은 모음 글자의 이름처럼 나는 소리입니다. 예: cake, bike, home",
        question_data=long_vowel_questions
    )

with tabs[3]:
    run_phonics_quiz(
        prefix="magic_e",
        title="🪄 Magic E 문제",
        caption="Magic E가 붙었을 때 바뀌는 단어를 고르세요.",
        guide_text="단어 끝의 e는 조용하지만, 앞의 모음을 길게 만들어 줍니다.",
        question_data=magic_e_questions
    )

with tabs[4]:
    run_phonics_quiz(
        prefix="blend_digraph",
        title="🤝 Blends & Digraphs 문제",
        caption="단어의 처음 소리나 글자 조합을 고르세요.",
        guide_text="blend는 두 자음 소리가 살아 있고, digraph는 두 글자가 하나의 새 소리를 만듭니다.",
        question_data=blend_digraph_questions
    )

with tabs[5]:
    run_phonics_quiz(
        prefix="vowel_team",
        title="🌊 Vowel Team 문제",
        caption="모음 조합이 만드는 소리를 고르세요.",
        guide_text="vowel team은 두 모음이 함께 나와 하나의 소리를 만드는 경우입니다.",
        question_data=vowel_team_questions
    )
