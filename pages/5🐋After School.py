import streamlit as st
import random

st.set_page_config(page_title="After School English", layout="centered")

st.title("🌱 After School English")
st.caption("Alex선생님과 함께하는 영어 복습 퀴즈")

tabs = st.tabs([
    "⏰ 시제 맞추기",
    "❌ 부정문 만들기",
    "❓ 의문문 만들기"
])


# =========================================================
# 공통 결과 출력 함수
# =========================================================
def show_result_message(final_score, total):
    if final_score == total:
        st.success("만점입니다! 정말 훌륭합니다! 🎉")
        st.balloons()
    elif final_score >= total * 0.8:
        st.success("아주 잘했습니다!")
    elif final_score >= total * 0.6:
        st.info("잘했습니다. 조금만 더 연습해 봅시다.")
    else:
        st.warning("괜찮습니다. 다시 보면 더 잘할 수 있습니다.")


# =========================================================
# Tab 1: 일반동사 / Be동사 시제 맞추기
# =========================================================
with tabs[0]:

    st.subheader("⏰ 일반동사 / Be동사 시제 맞추기")
    st.caption("현재형, 현재진행형, 과거형, 미래형 중 알맞은 표현을 고르세요.")

    st.info(
        """
        현재형: 평소에 하는 일  
        현재진행형: 지금 하고 있는 일 → be동사 + -ing  
        과거형: 이미 일어난 일  
        미래형: 앞으로 일어날 일 → will + 동사원형
        """
    )

    tense_question_data = [
        {"question": "She (     ) a book now.", "answer": "is reading", "choices": ["is reading", "reads", "read", "will read"]},
        {"question": "I (     ) lunch every day.", "answer": "eat", "choices": ["am eating", "eat", "ate", "will eat"]},
        {"question": "They (     ) soccer yesterday.", "answer": "played", "choices": ["play", "are playing", "played", "will play"]},
        {"question": "He (     ) to school tomorrow.", "answer": "will go", "choices": ["goes", "went", "is going", "will go"]},
        {"question": "We (     ) TV now.", "answer": "are watching", "choices": ["watch", "watched", "are watching", "will watch"]},
        {"question": "My father (     ) coffee every morning.", "answer": "drinks", "choices": ["is drinking", "drinks", "drank", "will drink"]},
        {"question": "The baby (     ) last night.", "answer": "cried", "choices": ["cries", "is crying", "cried", "will cry"]},
        {"question": "I (     ) my homework tonight.", "answer": "will do", "choices": ["do", "am doing", "did", "will do"]},
        {"question": "She (     ) dinner now.", "answer": "is cooking", "choices": ["cooks", "cooked", "is cooking", "will cook"]},
        {"question": "He (     ) English very well.", "answer": "speaks", "choices": ["is speaking", "speaks", "spoke", "will speak"]},
        {"question": "We (     ) in the park yesterday.", "answer": "walked", "choices": ["walk", "are walking", "walked", "will walk"]},
        {"question": "They (     ) their grandma next weekend.", "answer": "will visit", "choices": ["visit", "visited", "are visiting", "will visit"]},
        {"question": "I (     ) to music now.", "answer": "am listening", "choices": ["listen", "listened", "am listening", "will listen"]},
        {"question": "She (     ) breakfast at 7 every day.", "answer": "has", "choices": ["is having", "has", "had", "will have"]},
        {"question": "My friends (     ) a movie last Saturday.", "answer": "watched", "choices": ["watch", "are watching", "watched", "will watch"]},
        {"question": "He (     ) his uncle next month.", "answer": "will meet", "choices": ["meets", "met", "is meeting", "will meet"]},
        {"question": "The students (     ) in the classroom now.", "answer": "are studying", "choices": ["study", "studied", "are studying", "will study"]},
        {"question": "My mother (     ) dinner every evening.", "answer": "makes", "choices": ["is making", "makes", "made", "will make"]},
        {"question": "I (     ) my phone at home yesterday.", "answer": "left", "choices": ["leave", "am leaving", "left", "will leave"]},
        {"question": "We (     ) to Busan next week.", "answer": "will travel", "choices": ["travel", "traveled", "are traveling", "will travel"]},
    ]

    TENSE_TOTAL = len(tense_question_data)

    if "tense_quiz_data" not in st.session_state:
        tense_quiz_data = tense_question_data.copy()
        random.shuffle(tense_quiz_data)
        st.session_state.tense_quiz_data = tense_quiz_data

    if "tense_stage" not in st.session_state:
        st.session_state.tense_stage = 1

    if "tense_wrong_indices" not in st.session_state:
        st.session_state.tense_wrong_indices = []

    if "tense_first_score" not in st.session_state:
        st.session_state.tense_first_score = 0

    if "tense_final_score" not in st.session_state:
        st.session_state.tense_final_score = 0

    if st.button("시제 퀴즈 처음부터 다시 시작", key="reset_tense"):
        for key in list(st.session_state.keys()):
            if key.startswith("tense_") or key.startswith("q1_tense_") or key.startswith("q2_tense_"):
                del st.session_state[key]
        st.rerun()

    st.markdown("---")
    tense_quiz_data = st.session_state.tense_quiz_data

    if st.session_state.tense_stage == 1:
        st.subheader("1차 풀이")

        for i, item in enumerate(tense_quiz_data):
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

            for i, item in enumerate(tense_quiz_data):
                user_answer = st.session_state.get(f"q1_tense_{i}")
                if user_answer == item["answer"]:
                    correct_count += 1
                else:
                    wrong_indices.append(i)

            st.session_state.tense_first_score = correct_count
            st.session_state.tense_wrong_indices = wrong_indices

            if len(wrong_indices) == 0:
                st.session_state.tense_final_score = TENSE_TOTAL
                st.session_state.tense_stage = 3
            else:
                st.session_state.tense_stage = 2

            st.rerun()

    elif st.session_state.tense_stage == 2:
        wrong_indices = st.session_state.tense_wrong_indices

        st.subheader("1차 결과")
        st.write(f"점수: **{st.session_state.tense_first_score} / {TENSE_TOTAL}**")
        st.warning(f"틀린 문제 수: {len(wrong_indices)}문제")

        st.markdown("---")
        st.subheader("오답 다시 풀기")

        for idx in wrong_indices:
            item = tense_quiz_data[idx]
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
                item = tense_quiz_data[idx]
                retry_answer = st.session_state.get(f"q2_tense_{idx}")
                if retry_answer == item["answer"]:
                    additional_correct += 1

            st.session_state.tense_final_score = st.session_state.tense_first_score + additional_correct
            st.session_state.tense_stage = 3
            st.rerun()

    elif st.session_state.tense_stage == 3:
        st.subheader("최종 결과")
        st.write(f"1차 점수: **{st.session_state.tense_first_score} / {TENSE_TOTAL}**")
        st.write(f"최종 점수: **{st.session_state.tense_final_score} / {TENSE_TOTAL}**")

        show_result_message(st.session_state.tense_final_score, TENSE_TOTAL)

        st.markdown("---")
        st.subheader("정답 확인")

        for i, item in enumerate(tense_quiz_data):
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


# =========================================================
# Tab 2: 일반동사 / Be동사의 부정문 만들기
# =========================================================
with tabs[1]:

    st.subheader("❌ 일반동사 / Be동사의 부정문 만들기")
    st.caption("빈칸에 알맞은 부정 표현을 고르세요.")

    st.info(
        """
        Be동사의 부정문: am / is / are + not  
        일반동사의 부정문: do not / does not / did not + 동사원형  
        미래 부정문: will not + 동사원형
        """
    )

    negative_question_data = [
        {"question": "I (     ) a student.", "answer": "am not", "choices": ["am not", "do not", "does not", "did not"]},
        {"question": "She (     ) happy now.", "answer": "is not", "choices": ["is not", "does not", "did not", "will not"]},
        {"question": "They (     ) in the classroom.", "answer": "are not", "choices": ["are not", "do not", "does not", "did not"]},
        {"question": "I (     ) like coffee.", "answer": "do not", "choices": ["am not", "do not", "does not", "was not"]},
        {"question": "He (     ) play soccer.", "answer": "does not", "choices": ["is not", "do not", "does not", "did not"]},
        {"question": "We (     ) go to school yesterday.", "answer": "did not", "choices": ["are not", "do not", "does not", "did not"]},
        {"question": "She (     ) eat breakfast every day.", "answer": "does not", "choices": ["is not", "do not", "does not", "did not"]},
        {"question": "My friends (     ) watch TV last night.", "answer": "did not", "choices": ["are not", "do not", "does not", "did not"]},
        {"question": "You (     ) tired.", "answer": "are not", "choices": ["are not", "do not", "does not", "did not"]},
        {"question": "He (     ) at home yesterday.", "answer": "was not", "choices": ["is not", "was not", "does not", "did not"]},
        {"question": "They (     ) busy last week.", "answer": "were not", "choices": ["are not", "were not", "do not", "did not"]},
        {"question": "I (     ) study English yesterday.", "answer": "did not", "choices": ["am not", "do not", "does not", "did not"]},
        {"question": "My brother (     ) clean his room.", "answer": "does not", "choices": ["is not", "do not", "does not", "did not"]},
        {"question": "We (     ) have lunch at school tomorrow.", "answer": "will not", "choices": ["are not", "do not", "did not", "will not"]},
        {"question": "She (     ) call me tonight.", "answer": "will not", "choices": ["is not", "does not", "did not", "will not"]},
        {"question": "The dog (     ) sleep on the bed.", "answer": "does not", "choices": ["is not", "do not", "does not", "did not"]},
        {"question": "I (     ) late for school.", "answer": "am not", "choices": ["am not", "do not", "does not", "did not"]},
        {"question": "The students (     ) studying now.", "answer": "are not", "choices": ["are not", "do not", "does not", "did not"]},
        {"question": "He (     ) go to bed early.", "answer": "does not", "choices": ["is not", "do not", "does not", "did not"]},
        {"question": "We (     ) clean the room last Sunday.", "answer": "did not", "choices": ["are not", "do not", "does not", "did not"]},
    ]

    NEGATIVE_TOTAL = len(negative_question_data)

    if "negative_quiz_data" not in st.session_state:
        negative_quiz_data = negative_question_data.copy()
        random.shuffle(negative_quiz_data)
        st.session_state.negative_quiz_data = negative_quiz_data

    if "negative_stage" not in st.session_state:
        st.session_state.negative_stage = 1

    if "negative_wrong_indices" not in st.session_state:
        st.session_state.negative_wrong_indices = []

    if "negative_first_score" not in st.session_state:
        st.session_state.negative_first_score = 0

    if "negative_final_score" not in st.session_state:
        st.session_state.negative_final_score = 0

    if st.button("부정문 퀴즈 처음부터 다시 시작", key="reset_negative"):
        for key in list(st.session_state.keys()):
            if key.startswith("negative_") or key.startswith("q1_negative_") or key.startswith("q2_negative_"):
                del st.session_state[key]
        st.rerun()

    st.markdown("---")
    negative_quiz_data = st.session_state.negative_quiz_data

    if st.session_state.negative_stage == 1:
        st.subheader("1차 풀이")

        for i, item in enumerate(negative_quiz_data):
            st.write(f"### {i+1}. {item['question']}")
            st.radio(
                "알맞은 답을 고르세요.",
                item["choices"],
                key=f"q1_negative_{i}",
                index=None
            )

        if st.button("1차 제출", key="submit_negative_1"):
            wrong_indices = []
            correct_count = 0

            for i, item in enumerate(negative_quiz_data):
                user_answer = st.session_state.get(f"q1_negative_{i}")
                if user_answer == item["answer"]:
                    correct_count += 1
                else:
                    wrong_indices.append(i)

            st.session_state.negative_first_score = correct_count
            st.session_state.negative_wrong_indices = wrong_indices

            if len(wrong_indices) == 0:
                st.session_state.negative_final_score = NEGATIVE_TOTAL
                st.session_state.negative_stage = 3
            else:
                st.session_state.negative_stage = 2

            st.rerun()

    elif st.session_state.negative_stage == 2:
        wrong_indices = st.session_state.negative_wrong_indices

        st.subheader("1차 결과")
        st.write(f"점수: **{st.session_state.negative_first_score} / {NEGATIVE_TOTAL}**")
        st.warning(f"틀린 문제 수: {len(wrong_indices)}문제")

        st.markdown("---")
        st.subheader("오답 다시 풀기")

        for idx in wrong_indices:
            item = negative_quiz_data[idx]
            st.write(f"### {idx+1}. {item['question']}")
            st.radio(
                "다시 정답을 고르세요.",
                item["choices"],
                key=f"q2_negative_{idx}",
                index=None
            )

        if st.button("다시 풀기 제출", key="submit_negative_2"):
            additional_correct = 0

            for idx in wrong_indices:
                item = negative_quiz_data[idx]
                retry_answer = st.session_state.get(f"q2_negative_{idx}")
                if retry_answer == item["answer"]:
                    additional_correct += 1

            st.session_state.negative_final_score = st.session_state.negative_first_score + additional_correct
            st.session_state.negative_stage = 3
            st.rerun()

    elif st.session_state.negative_stage == 3:
        st.subheader("최종 결과")
        st.write(f"1차 점수: **{st.session_state.negative_first_score} / {NEGATIVE_TOTAL}**")
        st.write(f"최종 점수: **{st.session_state.negative_final_score} / {NEGATIVE_TOTAL}**")

        show_result_message(st.session_state.negative_final_score, NEGATIVE_TOTAL)

        st.markdown("---")
        st.subheader("정답 확인")

        for i, item in enumerate(negative_quiz_data):
            first_answer = st.session_state.get(f"q1_negative_{i}")
            second_answer = st.session_state.get(f"q2_negative_{i}") if f"q2_negative_{i}" in st.session_state else None

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


# =========================================================
# Tab 3: 일반동사 / Be동사의 의문문 만들기
# =========================================================
with tabs[2]:

    st.subheader("❓ 일반동사 / Be동사의 의문문 만들기")
    st.caption("빈칸에 알맞은 의문문 표현을 고르세요.")

    st.info(
        """
        Be동사 의문문: Am / Is / Are + 주어 ~ ?  
        일반동사 의문문: Do / Does / Did + 주어 + 동사원형 ~ ?  
        미래 의문문: Will + 주어 + 동사원형 ~ ?
        """
    )

    question_question_data = [
        {"question": "(     ) you a student?", "answer": "Are", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) she happy now?", "answer": "Is", "choices": ["Is", "Does", "Did", "Will"]},
        {"question": "(     ) they in the classroom?", "answer": "Are", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) you like coffee?", "answer": "Do", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) he play soccer?", "answer": "Does", "choices": ["Is", "Do", "Does", "Did"]},
        {"question": "(     ) they go to school yesterday?", "answer": "Did", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) she eat breakfast every day?", "answer": "Does", "choices": ["Is", "Do", "Does", "Did"]},
        {"question": "(     ) your friends watch TV last night?", "answer": "Did", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) you tired?", "answer": "Are", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) he at home yesterday?", "answer": "Was", "choices": ["Is", "Was", "Does", "Did"]},
        {"question": "(     ) they busy last week?", "answer": "Were", "choices": ["Are", "Were", "Do", "Did"]},
        {"question": "(     ) you study English yesterday?", "answer": "Did", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) your brother clean his room?", "answer": "Does", "choices": ["Is", "Do", "Does", "Did"]},
        {"question": "(     ) we have lunch at school tomorrow?", "answer": "Will", "choices": ["Are", "Do", "Did", "Will"]},
        {"question": "(     ) she call me tonight?", "answer": "Will", "choices": ["Is", "Does", "Did", "Will"]},
        {"question": "(     ) the dog sleep on the bed?", "answer": "Does", "choices": ["Is", "Do", "Does", "Did"]},
        {"question": "(     ) I late for school?", "answer": "Am", "choices": ["Am", "Do", "Does", "Did"]},
        {"question": "(     ) the students studying now?", "answer": "Are", "choices": ["Are", "Do", "Does", "Did"]},
        {"question": "(     ) he go to bed early?", "answer": "Does", "choices": ["Is", "Do", "Does", "Did"]},
        {"question": "(     ) we clean the room last Sunday?", "answer": "Did", "choices": ["Are", "Do", "Does", "Did"]},
    ]

    QUESTION_TOTAL = len(question_question_data)

    if "question_quiz_data" not in st.session_state:
        question_quiz_data = question_question_data.copy()
        random.shuffle(question_quiz_data)
        st.session_state.question_quiz_data = question_quiz_data

    if "question_stage" not in st.session_state:
        st.session_state.question_stage = 1

    if "question_wrong_indices" not in st.session_state:
        st.session_state.question_wrong_indices = []

    if "question_first_score" not in st.session_state:
        st.session_state.question_first_score = 0

    if "question_final_score" not in st.session_state:
        st.session_state.question_final_score = 0

    if st.button("의문문 퀴즈 처음부터 다시 시작", key="reset_question"):
        for key in list(st.session_state.keys()):
            if key.startswith("question_") or key.startswith("q1_question_") or key.startswith("q2_question_"):
                del st.session_state[key]
        st.rerun()

    st.markdown("---")
    question_quiz_data = st.session_state.question_quiz_data

    if st.session_state.question_stage == 1:
        st.subheader("1차 풀이")

        for i, item in enumerate(question_quiz_data):
            st.write(f"### {i+1}. {item['question']}")
            st.radio(
                "알맞은 답을 고르세요.",
                item["choices"],
                key=f"q1_question_{i}",
                index=None
            )

        if st.button("1차 제출", key="submit_question_1"):
            wrong_indices = []
            correct_count = 0

            for i, item in enumerate(question_quiz_data):
                user_answer = st.session_state.get(f"q1_question_{i}")
                if user_answer == item["answer"]:
                    correct_count += 1
                else:
                    wrong_indices.append(i)

            st.session_state.question_first_score = correct_count
            st.session_state.question_wrong_indices = wrong_indices

            if len(wrong_indices) == 0:
                st.session_state.question_final_score = QUESTION_TOTAL
                st.session_state.question_stage = 3
            else:
                st.session_state.question_stage = 2

            st.rerun()

    elif st.session_state.question_stage == 2:
        wrong_indices = st.session_state.question_wrong_indices

        st.subheader("1차 결과")
        st.write(f"점수: **{st.session_state.question_first_score} / {QUESTION_TOTAL}**")
        st.warning(f"틀린 문제 수: {len(wrong_indices)}문제")

        st.markdown("---")
        st.subheader("오답 다시 풀기")

        for idx in wrong_indices:
            item = question_quiz_data[idx]
            st.write(f"### {idx+1}. {item['question']}")
            st.radio(
                "다시 정답을 고르세요.",
                item["choices"],
                key=f"q2_question_{idx}",
                index=None
            )

        if st.button("다시 풀기 제출", key="submit_question_2"):
            additional_correct = 0

            for idx in wrong_indices:
                item = question_quiz_data[idx]
                retry_answer = st.session_state.get(f"q2_question_{idx}")
                if retry_answer == item["answer"]:
                    additional_correct += 1

            st.session_state.question_final_score = st.session_state.question_first_score + additional_correct
            st.session_state.question_stage = 3
            st.rerun()

    elif st.session_state.question_stage == 3:
        st.subheader("최종 결과")
        st.write(f"1차 점수: **{st.session_state.question_first_score} / {QUESTION_TOTAL}**")
        st.write(f"최종 점수: **{st.session_state.question_final_score} / {QUESTION_TOTAL}**")

        show_result_message(st.session_state.question_final_score, QUESTION_TOTAL)

        st.markdown("---")
        st.subheader("정답 확인")

        for i, item in enumerate(question_quiz_data):
            first_answer = st.session_state.get(f"q1_question_{i}")
            second_answer = st.session_state.get(f"q2_question_{i}") if f"q2_question_{i}" in st.session_state else None

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
