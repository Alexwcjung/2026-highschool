import streamlit as st
import random

st.set_page_config(page_title="After School English", layout="centered")

st.title("🌱 After School English")
st.caption("Alex선생님과 함께하는 영어 복습 활동")

tabs = st.tabs([
    "⏰ Tense Quiz",
    "❌ Negative Quiz",
    "🔤 Word Quiz",
    "📚 Class Guide"
])

# ---------------------------
# Tab 1: Tense Quiz
# ---------------------------
with tabs[0]:

    st.subheader("⏰ 영어 시제 퀴즈")
    st.caption("빈칸에 알맞은 표현을 고르는 30문제 · 4지선다 퀴즈")

    question_data = [
        {
            "question": "She (     ) a book now.",
            "answer": "is reading",
            "choices": ["is reading", "reads", "read", "will read"]
        },
        {
            "question": "I (     ) lunch every day.",
            "answer": "eat",
            "choices": ["am eating", "eat", "ate", "will eat"]
        },
        {
            "question": "They (     ) soccer yesterday.",
            "answer": "played",
            "choices": ["play", "are playing", "played", "will play"]
        },
        {
            "question": "He (     ) to school tomorrow.",
            "answer": "will go",
            "choices": ["goes", "went", "is going", "will go"]
        },
        {
            "question": "We (     ) TV now.",
            "answer": "are watching",
            "choices": ["watch", "watched", "are watching", "will watch"]
        },
        {
            "question": "My father (     ) coffee every morning.",
            "answer": "drinks",
            "choices": ["is drinking", "drinks", "drank", "will drink"]
        },
        {
            "question": "The baby (     ) last night.",
            "answer": "cried",
            "choices": ["cries", "is crying", "cried", "will cry"]
        },
        {
            "question": "I (     ) my homework tonight.",
            "answer": "will do",
            "choices": ["do", "am doing", "did", "will do"]
        },
        {
            "question": "She (     ) dinner now.",
            "answer": "is cooking",
            "choices": ["cooks", "cooked", "is cooking", "will cook"]
        },
        {
            "question": "He (     ) English very well.",
            "answer": "speaks",
            "choices": ["is speaking", "speaks", "spoke", "will speak"]
        },
    ]

    TOTAL_QUESTIONS = len(question_data)

    # ---------------------------
    # 세션 상태 초기화
    # 탭을 여러 개 쓸 때는 key 이름을 구분해 주는 것이 중요함
    # ---------------------------
    if "tense_quiz_data" not in st.session_state:
        quiz_data = question_data.copy()
        random.shuffle(quiz_data)
        st.session_state.tense_quiz_data = quiz_data

    if "tense_stage" not in st.session_state:
        st.session_state.tense_stage = 1

    if "tense_wrong_indices" not in st.session_state:
        st.session_state.tense_wrong_indices = []

    if "tense_first_score" not in st.session_state:
        st.session_state.tense_first_score = 0

    if "tense_final_score" not in st.session_state:
        st.session_state.tense_final_score = 0

    # ---------------------------
    # 다시 시작 버튼
    # ---------------------------
    if st.button("처음부터 다시 시작", key="reset_tense"):
        for key in list(st.session_state.keys()):
            if key.startswith("tense_") or key.startswith("q1_tense_") or key.startswith("q2_tense_"):
                del st.session_state[key]
        st.rerun()

    st.markdown("---")

    quiz_data = st.session_state.tense_quiz_data

    # ---------------------------
    # 1단계: 전체 문제 풀이
    # ---------------------------
    if st.session_state.tense_stage == 1:
        st.subheader("1차 풀이")

        for i, item in enumerate(quiz_data):
            st.write(f"### {i+1}. {item['question']}")
            st.radio(
                "알맞은 답을 고르세요.",
                item["choices"],
                key=f"q1_tense_{i}",
                index=None
            )

        if st.button("1차 제출", key="submit_tense_1"):
            wrong_indices = []
            correct_count = 0

            for i, item in enumerate(quiz_data):
                user_answer = st.session_state.get(f"q1_tense_{i}")

                if user_answer == item["answer"]:
                    correct_count += 1
                else:
                    wrong_indices.append(i)

            st.session_state.tense_first_score = correct_count
            st.session_state.tense_wrong_indices = wrong_indices

            if len(wrong_indices) == 0:
                st.session_state.tense_final_score = TOTAL_QUESTIONS
                st.session_state.tense_stage = 3
            else:
                st.session_state.tense_stage = 2

            st.rerun()

    # ---------------------------
    # 2단계: 오답 다시 풀기
    # ---------------------------
    elif st.session_state.tense_stage == 2:
        first_score = st.session_state.tense_first_score
        wrong_indices = st.session_state.tense_wrong_indices

        st.subheader("1차 결과")
        st.write(f"점수: **{first_score} / {TOTAL_QUESTIONS}**")
        st.warning(f"틀린 문제 수: {len(wrong_indices)}문제")

        st.markdown("---")
        st.subheader("오답 다시 풀기")
        st.caption("틀린 문제만 다시 풀고 제출하세요. 이후 정답이 공개됩니다.")

        for idx in wrong_indices:
            item = quiz_data[idx]
            st.write(f"### {idx+1}. {item['question']}")
            st.radio(
                "다시 정답을 고르세요.",
                item["choices"],
                key=f"q2_tense_{idx}",
                index=None
            )

        if st.button("다시 풀기 제출", key="submit_tense_2"):
            additional_correct = 0

            for idx in wrong_indices:
                item = quiz_data[idx]
                retry_answer = st.session_state.get(f"q2_tense_{idx}")

                if retry_answer == item["answer"]:
                    additional_correct += 1

            st.session_state.tense_final_score = st.session_state.tense_first_score + additional_correct
            st.session_state.tense_stage = 3
            st.rerun()

    # ---------------------------
    # 3단계: 최종 결과 + 정답 공개
    # ---------------------------
    elif st.session_state.tense_stage == 3:
        st.subheader("최종 결과")

        st.write(f"1차 점수: **{st.session_state.tense_first_score} / {TOTAL_QUESTIONS}**")
        st.write(f"최종 점수: **{st.session_state.tense_final_score} / {TOTAL_QUESTIONS}**")

        if st.session_state.tense_final_score == TOTAL_QUESTIONS:
            st.success("만점입니다!")
            st.balloons()
        elif st.session_state.tense_final_score >= TOTAL_QUESTIONS * 0.8:
            st.success("아주 잘했습니다!")
        elif st.session_state.tense_final_score >= TOTAL_QUESTIONS * 0.6:
            st.info("잘했습니다.")
        else:
            st.warning("조금 더 연습해 봅시다.")

        st.markdown("---")
        st.subheader("정답 확인")

        for i, item in enumerate(quiz_data):
            first_answer = st.session_state.get(f"q1_tense_{i}")
            second_answer = st.session_state.get(f"q2_tense_{i}") if f"q2_tense_{i}" in st.session_state else None

            st.write(f"### {i+1}. {item['question']}")
            st.write(f"- 정답: **{item['answer']}**")

            if second_answer is not None:
                st.write(f"- 1차 선택: {first_answer if first_answer else '미응답'}")
                st.write(f"- 2차 선택: {second_answer if second_answer else '미응답'}")

                if second_answer == item["answer"]:
                    st.success("최종 정답")
                else:
                    st.error("최종 오답")
            else:
                st.write(f"- 선택: {first_answer if first_answer else '미응답'}")

                if first_answer == item["answer"]:
                    st.success("정답")
                else:
                    st.error("오답")


# ---------------------------
# Tab 2: 일반동사
# ---------------------------
with tabs[1]:
    st.subheader("❌ 일반동사와 be동사의 부정문")
import streamlit as st

st.set_page_config(page_title="영어 일반동사 퀴즈", layout="centered")

st.title("🚀 Alex선생님과 함께하는 영어 부정문 퀴즈")
st.caption("일반동사와 be동사의 부정문 · 10문제 · 2지선다")

# ---------------------------
# 문제 데이터 (10문제)
# 이미 섞어 둔 고정 순서
# ---------------------------
question_data = [
    {"question": "I (     ) like pizza.", "answer": "do not", "choices": ["am not", "do not"]},
    {"question": "She (     ) happy.", "answer": "is not", "choices": ["is not", "does not"]},
    {"question": "They (     ) study English.", "answer": "do not", "choices": ["are not", "do not"]},
    {"question": "My mother (     ) a doctor.", "answer": "is not", "choices": ["is not", "does not"]},
    {"question": "He (     ) eat breakfast.", "answer": "does not", "choices": ["is not", "does not"]},
    {"question": "Tom and I (     ) classmates.", "answer": "are not", "choices": ["are not", "do not"]},
    {"question": "My brother (     ) get up early.", "answer": "does not", "choices": ["is not", "does not"]},
    {"question": "I (     ) a student.", "answer": "am not", "choices": ["am not", "do not"]},
    {"question": "The students (     ) run fast.", "answer": "do not", "choices": ["are not", "do not"]},
    {"question": "He (     ) tall.", "answer": "is not", "choices": ["is not", "does not"]},
]

# ---------------------------
# 세션 상태 초기화
# ---------------------------
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = question_data.copy()

if "stage" not in st.session_state:
    # stage 1: 전체 풀이
    # stage 2: 틀린 문제만 다시 풀이
    # stage 3: 1차에서 틀린 문제만 정답 공개
    st.session_state.stage = 1

if "wrong_indices" not in st.session_state:
    st.session_state.wrong_indices = []

if "first_score" not in st.session_state:
    st.session_state.first_score = 0

if "final_score" not in st.session_state:
    st.session_state.final_score = 0

# ---------------------------
# 다시 시작
# ---------------------------
if st.button("처음부터 다시 시작"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

st.markdown("---")
quiz_data = st.session_state.quiz_data

# ---------------------------
# 1단계: 전체 문제 풀이
# ---------------------------
if st.session_state.stage == 1:
    st.subheader("1차 풀이")

    for i, item in enumerate(quiz_data):
        st.write(f"### {i+1}. {item['question']}")
        st.radio(
            "알맞은 답을 고르세요.",
            item["choices"],
            key=f"q1_{i}",
            index=None
        )

    if st.button("1차 제출"):
        wrong_indices = []
        correct_count = 0

        for i, item in enumerate(quiz_data):
            user_answer = st.session_state.get(f"q1_{i}")
            if user_answer == item["answer"]:
                correct_count += 1
            else:
                wrong_indices.append(i)

        st.session_state.first_score = correct_count
        st.session_state.wrong_indices = wrong_indices

        if len(wrong_indices) == 0:
            st.session_state.final_score = 10
            st.session_state.stage = 3
        else:
            st.session_state.stage = 2

        st.rerun()

# ---------------------------
# 2단계: 틀린 문제만 다시 풀기
# ---------------------------
elif st.session_state.stage == 2:
    first_score = st.session_state.first_score
    wrong_indices = st.session_state.wrong_indices

    st.subheader("1차 결과")
    st.write(f"점수: **{first_score} / 10**")
    st.warning(f"틀린 문제 수: {len(wrong_indices)}문제")

    st.markdown("---")
    st.subheader("2차 풀이")
    st.caption("1차에서 틀린 문제만 다시 풉니다.")

    for idx in wrong_indices:
        item = quiz_data[idx]
        st.write(f"### {idx+1}. {item['question']}")
        st.radio(
            "다시 정답을 고르세요.",
            item["choices"],
            key=f"q2_{idx}",
            index=None
        )

    if st.button("2차 제출"):
        additional_correct = 0

        for idx in wrong_indices:
            item = quiz_data[idx]
            retry_answer = st.session_state.get(f"q2_{idx}")
            if retry_answer == item["answer"]:
                additional_correct += 1

        st.session_state.final_score = st.session_state.first_score + additional_correct
        st.session_state.stage = 3
        st.rerun()

# ---------------------------
# 3단계: 1차에서 틀린 문제만 정답 공개
# ---------------------------
elif st.session_state.stage == 3:
    wrong_indices = st.session_state.wrong_indices

    st.subheader("최종 결과")
    st.write(f"1차 점수: **{st.session_state.first_score} / 10**")
    st.write(f"최종 점수: **{st.session_state.final_score} / 10**")

    if st.session_state.final_score == 10:
        st.success("만점입니다!")
        st.balloons()
    elif st.session_state.final_score >= 8:
        st.success("아주 잘했습니다!")
    elif st.session_state.final_score >= 6:
        st.info("잘했습니다.")
    else:
        st.warning("조금 더 연습해 봅시다.")

    st.markdown("---")
    st.subheader("정답 확인")

    if len(wrong_indices) == 0:
        st.success("1차에서 모두 맞혔습니다. 확인할 오답이 없습니다.")
    else:
        st.caption("아래에는 1차에서 틀린 문제만 표시됩니다.")

        for idx in wrong_indices:
            item = quiz_data[idx]
            first_answer = st.session_state.get(f"q1_{idx}")
            second_answer = st.session_state.get(f"q2_{idx}")

            st.write(f"### {idx+1}. {item['question']}")
            st.write(f"- 정답: **{item['answer']}**")
            st.write(f"- 1차 선택: {first_answer if first_answer else '미응답'}")
            st.write(f"- 2차 선택: {second_answer if second_answer else '미응답'}")

            if second_answer == item["answer"]:
                st.success("2차에서 정답")
            else:
                st.error("2차에서도 오답")

# ---------------------------
# Tab 3: Word Quiz
# ---------------------------
with tabs[2]:
    st.subheader("🔤 Word Quiz")
    st.info("여기에 단어 듣기 퀴즈 코드를 넣으면 됩니다.")


# ---------------------------
# Tab 4: Class Guide
# ---------------------------
with tabs[3]:
    st.subheader("📚 Class Guide")
    st.markdown(
        """
        ### 수업 안내

        - ⏰ **Tense Quiz**: 현재형, 현재진행형, 과거형, 미래형 연습
        - ❌ **Negative Quiz**: be동사와 일반동사의 부정문 연습
        - 🔤 **Word Quiz**: 그림과 소리를 활용한 단어 복습
        """
    )
