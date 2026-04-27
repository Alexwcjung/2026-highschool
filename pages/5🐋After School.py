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
        {
            "question": "(     ) you a student?",
            "answer": "Are",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) she happy now?",
            "answer": "Is",
            "choices": ["Is", "Does", "Did", "Will"]
        },
        {
            "question": "(     ) they in the classroom?",
            "answer": "Are",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) you like coffee?",
            "answer": "Do",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) he play soccer?",
            "answer": "Does",
            "choices": ["Is", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) they go to school yesterday?",
            "answer": "Did",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) she eat breakfast every day?",
            "answer": "Does",
            "choices": ["Is", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) your friends watch TV last night?",
            "answer": "Did",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) you tired?",
            "answer": "Are",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) he at home yesterday?",
            "answer": "Was",
            "choices": ["Is", "Was", "Does", "Did"]
        },
        {
            "question": "(     ) they busy last week?",
            "answer": "Were",
            "choices": ["Are", "Were", "Do", "Did"]
        },
        {
            "question": "(     ) you study English yesterday?",
            "answer": "Did",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) your brother clean his room?",
            "answer": "Does",
            "choices": ["Is", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) we have lunch at school tomorrow?",
            "answer": "Will",
            "choices": ["Are", "Do", "Did", "Will"]
        },
        {
            "question": "(     ) she call me tonight?",
            "answer": "Will",
            "choices": ["Is", "Does", "Did", "Will"]
        },
        {
            "question": "(     ) the dog sleep on the bed?",
            "answer": "Does",
            "choices": ["Is", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) I late for school?",
            "answer": "Am",
            "choices": ["Am", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) the students studying now?",
            "answer": "Are",
            "choices": ["Are", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) he go to bed early?",
            "answer": "Does",
            "choices": ["Is", "Do", "Does", "Did"]
        },
        {
            "question": "(     ) we clean the room last Sunday?",
            "answer": "Did",
            "choices": ["Are", "Do", "Does", "Did"]
        },
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

    # ---------------------------
    # 1단계: 전체 문제 풀이
    # ---------------------------
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

    # ---------------------------
    # 2단계: 오답 다시 풀기
    # ---------------------------
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

            st.session_state.question_final_score = (
                st.session_state.question_first_score + additional_correct
            )
            st.session_state.question_stage = 3
            st.rerun()

    # ---------------------------
    # 3단계: 최종 결과 + 정답 공개
    # ---------------------------
    elif st.session_state.question_stage == 3:
        st.subheader("최종 결과")

        st.write(f"1차 점수: **{st.session_state.question_first_score} / {QUESTION_TOTAL}**")
        st.write(f"최종 점수: **{st.session_state.question_final_score} / {QUESTION_TOTAL}**")

        if st.session_state.question_final_score == QUESTION_TOTAL:
            st.success("만점입니다!")
            st.balloons()
        elif st.session_state.question_final_score >= QUESTION_TOTAL * 0.8:
            st.success("아주 잘했습니다!")
        elif st.session_state.question_final_score >= QUESTION_TOTAL * 0.6:
            st.info("잘했습니다.")
        else:
            st.warning("조금 더 연습해 봅시다.")

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
