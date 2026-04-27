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
# 공통 결과 메시지 함수
# =========================================================
def show_result_message(final_score, total):
    if final_score == total:
        st.success("만점입니다! 정말 훌륭합니다! 🎉")
        st.balloons()
    elif final_score >= total * 0.8:
        st.success("아주 잘했습니다! 영어 문장 구조를 잘 이해하고 있어요!")
    elif final_score >= total * 0.6:
        st.info("잘했습니다. 조금만 더 연습하면 훨씬 더 좋아질 수 있습니다.")
    else:
        st.warning("괜찮습니다. 틀린 문제를 다시 보면서 천천히 익혀 봅시다.")


# =========================================================
# 공통 퀴즈 실행 함수
# =========================================================
def run_quiz(prefix, title, caption, guide_text, question_data):
    total = len(question_data)

    st.subheader(title)
    st.caption(caption)
    st.info(guide_text)

    if f"{prefix}_quiz_data" not in st.session_state:
        quiz_data = question_data.copy()
        random.shuffle(quiz_data)
        st.session_state[f"{prefix}_quiz_data"] = quiz_data

    if f"{prefix}_stage" not in st.session_state:
        # 1: 1차 풀이
        # 1.5: 1차 응원 화면
        # 2: 2차 오답 풀이
        # 2.5: 2차 응원 화면
        # 3: 최종 결과 및 정답 공개
        st.session_state[f"{prefix}_stage"] = 1

    if f"{prefix}_wrong_indices" not in st.session_state:
        st.session_state[f"{prefix}_wrong_indices"] = []

    if f"{prefix}_final_wrong_indices" not in st.session_state:
        st.session_state[f"{prefix}_final_wrong_indices"] = []

    if f"{prefix}_first_score" not in st.session_state:
        st.session_state[f"{prefix}_first_score"] = 0

    if f"{prefix}_second_score" not in st.session_state:
        st.session_state[f"{prefix}_second_score"] = 0

    if f"{prefix}_final_score" not in st.session_state:
        st.session_state[f"{prefix}_final_score"] = 0

    if f"{prefix}_first_celebration_shown" not in st.session_state:
        st.session_state[f"{prefix}_first_celebration_shown"] = False

    if f"{prefix}_second_celebration_shown" not in st.session_state:
        st.session_state[f"{prefix}_second_celebration_shown"] = False

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

    quiz_data = st.session_state[f"{prefix}_quiz_data"]
    stage = st.session_state[f"{prefix}_stage"]

    # ---------------------------
    # 1단계: 1차 풀이
    # ---------------------------
    if stage == 1:
        st.subheader("1차 풀이")
        st.caption("문장을 읽고 빈칸에 알맞은 표현을 고르세요.")

        for i, item in enumerate(quiz_data):
            st.write(f"### {i+1}. {item['question']}")
            st.radio(
                "알맞은 답을 고르세요.",
                item["choices"],
                key=f"q1_{prefix}_{i}",
                index=None
            )
            st.markdown("---")

        if st.button("1차 제출", key=f"submit_{prefix}_1"):
            wrong_indices = []
            correct_count = 0

            for i, item in enumerate(quiz_data):
                user_answer = st.session_state.get(f"q1_{prefix}_{i}")

                if user_answer == item["answer"]:
                    correct_count += 1
                else:
                    wrong_indices.append(i)

            st.session_state[f"{prefix}_first_score"] = correct_count
            st.session_state[f"{prefix}_wrong_indices"] = wrong_indices
            st.session_state[f"{prefix}_first_celebration_shown"] = False
            st.session_state[f"{prefix}_stage"] = 1.5

            st.rerun()

    # ---------------------------
    # 1.5단계: 1차 응원 화면
    # ---------------------------
    elif stage == 1.5:
        score = st.session_state[f"{prefix}_first_score"]
        wrong_indices = st.session_state[f"{prefix}_wrong_indices"]
        wrong_count = len(wrong_indices)

        if not st.session_state[f"{prefix}_first_celebration_shown"]:
            st.balloons()
            st.session_state[f"{prefix}_first_celebration_shown"] = True

        st.subheader("🎉 1차 풀이 완료!")
        st.success("좋습니다! 끝까지 1차 문제를 풀어낸 것만으로도 충분히 잘했습니다.")
        st.write(f"1차 점수: **{score} / {total}**")
        st.write(f"다시 풀 문제: **{wrong_count}문제**")

        st.progress(score / total)

        if wrong_count == 0:
            st.success("완벽합니다! 1차에서 모든 문제를 맞혔습니다. 정말 훌륭합니다!")
            st.info("바로 최종 결과에서 정답을 확인해 봅시다.")

            if st.button("최종 결과 보기", key=f"go_final_{prefix}_after_first"):
                st.session_state[f"{prefix}_final_score"] = total
                st.session_state[f"{prefix}_second_score"] = 0
                st.session_state[f"{prefix}_final_wrong_indices"] = []
                st.session_state[f"{prefix}_stage"] = 3
                st.rerun()
        else:
            st.info("틀린 문제는 실패가 아니라 다시 배울 기회입니다. 한 번 더 풀면 더 오래 기억할 수 있어요!")

            if st.button("2차 오답 다시 풀기 시작하기", key=f"go_second_{prefix}"):
                st.session_state[f"{prefix}_stage"] = 2
                st.rerun()

    # ---------------------------
    # 2단계: 오답 다시 풀기
    # ---------------------------
    elif stage == 2:
        wrong_indices = st.session_state[f"{prefix}_wrong_indices"]

        st.subheader("2차 풀이")
        st.write(f"1차 점수: **{st.session_state[f'{prefix}_first_score']} / {total}**")
        st.warning(f"다시 풀 문제: **{len(wrong_indices)}문제**")
        st.caption("1차에서 틀린 문제만 다시 풉니다.")

        st.markdown("---")

        for idx in wrong_indices:
            item = quiz_data[idx]
            st.write(f"### {idx+1}. {item['question']}")
            st.radio(
                "다시 정답을 고르세요.",
                item["choices"],
                key=f"q2_{prefix}_{idx}",
                index=None
            )
            st.markdown("---")

        if st.button("2차 제출", key=f"submit_{prefix}_2"):
            additional_correct = 0
            final_wrong_indices = []

            for idx in wrong_indices:
                item = quiz_data[idx]
                retry_answer = st.session_state.get(f"q2_{prefix}_{idx}")

                if retry_answer == item["answer"]:
                    additional_correct += 1
                else:
                    final_wrong_indices.append(idx)

            st.session_state[f"{prefix}_second_score"] = additional_correct
            st.session_state[f"{prefix}_final_score"] = (
                st.session_state[f"{prefix}_first_score"] + additional_correct
            )
            st.session_state[f"{prefix}_final_wrong_indices"] = final_wrong_indices
            st.session_state[f"{prefix}_second_celebration_shown"] = False
            st.session_state[f"{prefix}_stage"] = 2.5

            st.rerun()

    # ---------------------------
    # 2.5단계: 2차 응원 화면
    # ---------------------------
    elif stage == 2.5:
        retry_total = len(st.session_state[f"{prefix}_wrong_indices"])
        second_score = st.session_state[f"{prefix}_second_score"]
        final_score = st.session_state[f"{prefix}_final_score"]
        final_wrong_count = len(st.session_state[f"{prefix}_final_wrong_indices"])

        if not st.session_state[f"{prefix}_second_celebration_shown"]:
            st.balloons()
            st.session_state[f"{prefix}_second_celebration_shown"] = True

        st.subheader("🌟 2차 풀이 완료!")
        st.success("끝까지 다시 도전한 것이 정말 멋집니다!")
        st.write(f"2차에서 **{retry_total}문제 중 {second_score}문제**를 다시 맞혔습니다.")
        st.write(f"현재 최종 점수: **{final_score} / {total}**")

        st.progress(final_score / total)

        if final_wrong_count == 0:
            st.success("대단합니다! 2차까지 모두 해결했습니다. 실력이 분명히 늘고 있습니다.")
        else:
            st.info(f"아직 헷갈린 문제는 **{final_wrong_count}문제**입니다. 마지막 정답 확인에서 다시 정리해 봅시다.")

        if st.button("최종 결과와 정답 확인하기", key=f"go_final_{prefix}_after_second"):
            st.session_state[f"{prefix}_stage"] = 3
            st.rerun()

    # ---------------------------
    # 3단계: 최종 결과 + 정답 공개
    # ---------------------------
    elif stage == 3:
        st.subheader("최종 결과")

        first_score = st.session_state[f"{prefix}_first_score"]
        second_score = st.session_state[f"{prefix}_second_score"]
        final_score = st.session_state[f"{prefix}_final_score"]

        st.write(f"1차 점수: **{first_score} / {total}**")
        st.write(f"2차에서 다시 맞힌 문제 수: **{second_score}문제**")
        st.write(f"최종 점수: **{final_score} / {total}**")

        show_result_message(final_score, total)

        st.markdown("---")
        st.subheader("정답 확인")

        final_wrong_indices = st.session_state.get(f"{prefix}_final_wrong_indices", [])

        for i, item in enumerate(quiz_data):
            first_answer = st.session_state.get(f"q1_{prefix}_{i}")
            second_answer = (
                st.session_state.get(f"q2_{prefix}_{i}")
                if f"q2_{prefix}_{i}" in st.session_state
                else None
            )

            st.write(f"### {i+1}. {item['question']}")
            st.write(f"- 정답: **{item['answer']}**")

            if second_answer is not None:
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

            st.markdown("---")


# =========================================================
# 문제 데이터 1: 시제 맞추기
# =========================================================
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


# =========================================================
# 문제 데이터 2: 부정문 만들기
# =========================================================
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


# =========================================================
# 문제 데이터 3: 의문문 만들기
# =========================================================
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


# =========================================================
# 탭 실행
# =========================================================
with tabs[0]:
    run_quiz(
        prefix="tense",
        title="⏰ 일반동사 / Be동사 시제 맞추기",
        caption="현재형, 현재진행형, 과거형, 미래형 중 알맞은 표현을 고르세요.",
        guide_text="""
        현재형: 평소에 하는 일  
        현재진행형: 지금 하고 있는 일 → be동사 + -ing  
        과거형: 이미 일어난 일  
        미래형: 앞으로 일어날 일 → will + 동사원형
        """,
        question_data=tense_question_data
    )

with tabs[1]:
    run_quiz(
        prefix="negative",
        title="❌ 일반동사 / Be동사의 부정문 만들기",
        caption="빈칸에 알맞은 부정 표현을 고르세요.",
        guide_text="""
        Be동사의 부정문: am / is / are + not  
        일반동사의 부정문: do not / does not / did not + 동사원형  
        미래 부정문: will not + 동사원형
        """,
        question_data=negative_question_data
    )

with tabs[2]:
    run_quiz(
        prefix="question",
        title="❓ 일반동사 / Be동사의 의문문 만들기",
        caption="빈칸에 알맞은 의문문 표현을 고르세요.",
        guide_text="""
        Be동사 의문문: Am / Is / Are + 주어 ~ ?  
        일반동사 의문문: Do / Does / Did + 주어 + 동사원형 ~ ?  
        미래 의문문: Will + 주어 + 동사원형 ~ ?
        """,
        question_data=question_question_data
    )
