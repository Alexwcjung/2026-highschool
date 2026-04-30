import streamlit as st
import random

st.set_page_config(
    page_title="단어 뜻 쓰기 게임",
    page_icon="✏️",
    layout="centered"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .title-box {
        background: linear-gradient(135deg, #fce7f3, #e0f2fe, #fef3c7);
        border-radius: 28px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        margin-bottom: 24px;
    }

    .title-box h1 {
        font-size: 40px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 8px;
    }

    .title-box p {
        font-size: 18px;
        color: #4b5563;
        margin: 0;
    }

    .word-card {
        background: linear-gradient(135deg, #ffffff, #fff7ed);
        border: 4px solid #fed7aa;
        border-radius: 32px;
        padding: 38px 24px;
        text-align: center;
        box-shadow: 0 10px 26px rgba(0,0,0,0.12);
        margin: 24px 0;
    }

    .word-label {
        font-size: 19px;
        font-weight: 900;
        color: #9a3412;
        margin-bottom: 12px;
    }

    .word-text {
        font-size: 58px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7, #dbeafe, #fce7f3);
        border-radius: 22px;
        padding: 18px;
        text-align: center;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 5px 14px rgba(0,0,0,0.08);
        border: 2px solid #bbf7d0;
    }

    .result-good {
        background: #dcfce7;
        border-left: 7px solid #22c55e;
        border-radius: 18px;
        padding: 18px;
        font-size: 22px;
        font-weight: 900;
        color: #14532d;
        margin: 18px 0;
    }

    .result-bad {
        background: #fee2e2;
        border-left: 7px solid #ef4444;
        border-radius: 18px;
        padding: 18px;
        font-size: 22px;
        font-weight: 900;
        color: #7f1d1d;
        margin: 18px 0;
    }

    .answer-box {
        background: #f8fafc;
        border: 2px solid #e2e8f0;
        border-radius: 18px;
        padding: 16px;
        font-size: 18px;
        line-height: 1.7;
        margin: 14px 0;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        padding: 0.55rem 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 제목
# =========================
st.markdown(
    """
    <div class="title-box">
        <h1>✏️ 단어 뜻 쓰기 게임</h1>
        <p>영어 단어를 보고 한국어 뜻을 직접 써 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 단어 데이터
# =========================
word_data = [
    {"word": "cat", "meaning": ["고양이"]},
    {"word": "dog", "meaning": ["개"]},
    {"word": "sun", "meaning": ["태양", "해"]},
    {"word": "run", "meaning": ["달리다", "뛰다"]},
    {"word": "sit", "meaning": ["앉다"]},
    {"word": "big", "meaning": ["큰", "크다"]},
    {"word": "red", "meaning": ["빨간", "빨간색"]},
    {"word": "pen", "meaning": ["펜"]},
    {"word": "box", "meaning": ["상자"]},
    {"word": "cup", "meaning": ["컵"]},
    {"word": "fish", "meaning": ["물고기", "생선"]},
    {"word": "book", "meaning": ["책"]},
    {"word": "milk", "meaning": ["우유"]},
    {"word": "jump", "meaning": ["점프하다", "뛰다", "뛰어오르다"]},
    {"word": "bed", "meaning": ["침대"]},
    {"word": "apple", "meaning": ["사과"]},
    {"word": "banana", "meaning": ["바나나"]},
    {"word": "happy", "meaning": ["행복한", "기쁜"]},
    {"word": "sad", "meaning": ["슬픈"]},
    {"word": "school", "meaning": ["학교"]},
    {"word": "teacher", "meaning": ["선생님", "교사"]},
    {"word": "student", "meaning": ["학생"]},
    {"word": "water", "meaning": ["물"]},
    {"word": "chair", "meaning": ["의자"]},
    {"word": "desk", "meaning": ["책상"]},
    {"word": "phone", "meaning": ["전화기", "휴대폰", "폰"]},
    {"word": "music", "meaning": ["음악"]},
    {"word": "pizza", "meaning": ["피자"]},
    {"word": "green", "meaning": ["초록색", "초록", "녹색"]},
    {"word": "blue", "meaning": ["파란색", "파랑", "푸른"]},
]

# =========================
# 설정
# =========================
st.markdown("### 🎲 게임 설정")

col1, col2 = st.columns(2)

with col1:
    question_count = st.slider(
        "문제 개수",
        min_value=5,
        max_value=len(word_data),
        value=10,
        step=5
    )

with col2:
    show_hint = st.checkbox(
        "힌트 보기",
        value=False
    )

# =========================
# 상태 초기화
# =========================
if "meaning_game_questions" not in st.session_state:
    st.session_state.meaning_game_questions = random.sample(word_data, question_count)

if "meaning_game_index" not in st.session_state:
    st.session_state.meaning_game_index = 0

if "meaning_game_score" not in st.session_state:
    st.session_state.meaning_game_score = 0

if "meaning_game_checked" not in st.session_state:
    st.session_state.meaning_game_checked = False

if "meaning_game_result" not in st.session_state:
    st.session_state.meaning_game_result = ""

if "meaning_game_wrong" not in st.session_state:
    st.session_state.meaning_game_wrong = []

# 문제 개수를 바꾸면 새로 시작
if "last_question_count" not in st.session_state:
    st.session_state.last_question_count = question_count

if st.session_state.last_question_count != question_count:
    st.session_state.meaning_game_questions = random.sample(word_data, question_count)
    st.session_state.meaning_game_index = 0
    st.session_state.meaning_game_score = 0
    st.session_state.meaning_game_checked = False
    st.session_state.meaning_game_result = ""
    st.session_state.meaning_game_wrong = []
    st.session_state.last_question_count = question_count
    st.rerun()

# =========================
# 점수판
# =========================
total_questions = len(st.session_state.meaning_game_questions)
current_index = st.session_state.meaning_game_index

col_score1, col_score2, col_score3 = st.columns(3)

with col_score1:
    st.markdown(
        f"""
        <div class="score-box">
            문제<br>{min(current_index + 1, total_questions)} / {total_questions}
        </div>
        """,
        unsafe_allow_html=True
    )

with col_score2:
    st.markdown(
        f"""
        <div class="score-box">
            점수<br>{st.session_state.meaning_game_score}
        </div>
        """,
        unsafe_allow_html=True
    )

with col_score3:
    remaining = max(0, total_questions - current_index)
    st.markdown(
        f"""
        <div class="score-box">
            남은 문제<br>{remaining}
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 게임 종료
# =========================
if current_index >= total_questions:
    st.success("🎉 게임이 끝났습니다!")

    st.markdown(
        f"""
        <div class="score-box">
            🏆 최종 점수: {st.session_state.meaning_game_score} / {total_questions}
        </div>
        """,
        unsafe_allow_html=True
    )

    if len(st.session_state.meaning_game_wrong) == 0:
        st.balloons()
        st.success("완벽합니다! 모든 단어의 뜻을 잘 알고 있습니다.")
    else:
        st.warning("아래 단어들을 다시 복습해 보세요.")

        for item in st.session_state.meaning_game_wrong:
            st.markdown(
                f"""
                <div class="answer-box">
                    <b>{item["word"]}</b><br>
                    내가 쓴 답: {item["user_answer"]}<br>
                    정답: {", ".join(item["meaning"])}
                </div>
                """,
                unsafe_allow_html=True
            )

    if st.button("🔄 다시 시작"):
        st.session_state.meaning_game_questions = random.sample(word_data, question_count)
        st.session_state.meaning_game_index = 0
        st.session_state.meaning_game_score = 0
        st.session_state.meaning_game_checked = False
        st.session_state.meaning_game_result = ""
        st.session_state.meaning_game_wrong = []
        st.rerun()

else:
    # =========================
    # 현재 문제
    # =========================
    current_q = st.session_state.meaning_game_questions[current_index]
    word = current_q["word"]
    meanings = current_q["meaning"]

    st.markdown(
        f"""
        <div class="word-card">
            <div class="word-label">영어 단어</div>
            <div class="word-text">{word}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if show_hint:
        first_hint = meanings[0][0]
        st.info(f"힌트: 한국어 뜻은 '{first_hint}'로 시작합니다.")

    user_answer = st.text_input(
        "한국어 뜻을 쓰세요.",
        key=f"meaning_answer_{current_index}",
        placeholder="예: 고양이"
    )

    col_check, col_next, col_pass = st.columns(3)

    with col_check:
        if st.button("✅ 정답 확인", use_container_width=True):
            answer_clean = user_answer.strip().replace(" ", "")
            correct_list = [m.replace(" ", "") for m in meanings]

            if answer_clean in correct_list:
                st.session_state.meaning_game_score += 1
                st.session_state.meaning_game_result = "correct"
            else:
                st.session_state.meaning_game_result = "wrong"
                st.session_state.meaning_game_wrong.append({
                    "word": word,
                    "meaning": meanings,
                    "user_answer": user_answer
                })

            st.session_state.meaning_game_checked = True
            st.rerun()

    with col_next:
        if st.button("➡️ 다음 문제", use_container_width=True):
            if st.session_state.meaning_game_checked:
                st.session_state.meaning_game_index += 1
                st.session_state.meaning_game_checked = False
                st.session_state.meaning_game_result = ""
                st.rerun()
            else:
                st.warning("먼저 정답 확인을 눌러 주세요.")

    with col_pass:
        if st.button("⏭️ 넘기기", use_container_width=True):
            st.session_state.meaning_game_wrong.append({
                "word": word,
                "meaning": meanings,
                "user_answer": "넘김"
            })
            st.session_state.meaning_game_index += 1
            st.session_state.meaning_game_checked = False
            st.session_state.meaning_game_result = ""
            st.rerun()

    # =========================
    # 결과 표시
    # =========================
    if st.session_state.meaning_game_checked:
        if st.session_state.meaning_game_result == "correct":
            st.markdown(
                """
                <div class="result-good">
                    🎉 정답입니다! 잘했어요!
                </div>
                """,
                unsafe_allow_html=True
            )
        elif st.session_state.meaning_game_result == "wrong":
            st.markdown(
                f"""
                <div class="result-bad">
                    😢 아쉬워요! 정답은 {", ".join(meanings)} 입니다.
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    if st.button("🔄 게임 전체 다시 시작"):
        st.session_state.meaning_game_questions = random.sample(word_data, question_count)
        st.session_state.meaning_game_index = 0
        st.session_state.meaning_game_score = 0
        st.session_state.meaning_game_checked = False
        st.session_state.meaning_game_result = ""
        st.session_state.meaning_game_wrong = []
        st.rerun()
