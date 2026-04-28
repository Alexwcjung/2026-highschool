import streamlit as st

st.set_page_config(page_title="English Sentence Guide", page_icon="🧩", layout="centered")

# =========================================================
# 전체 디자인 CSS
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #fffdfc;
    }

    .title-box {
        background: linear-gradient(135deg, #fff7fb 0%, #eef7ff 50%, #fff8e8 100%);
        padding: 34px 30px;
        border-radius: 32px;
        margin-bottom: 28px;
        box-shadow: 0 10px 26px rgba(80, 80, 120, 0.12);
        text-align: center;
        border: 1.5px solid #f3e8ff;
    }

    .title-box h1 {
        color: #334155;
        margin-bottom: 10px;
        font-size: 38px;
        font-weight: 900;
    }

    .title-box p {
        color: #64748b;
        font-size: 19px;
        margin: 0;
        line-height: 1.7;
    }

    .grammar-card {
        border-radius: 30px;
        padding: 28px 30px;
        margin: 20px 0 26px 0;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        border: 1.5px solid rgba(255,255,255,0.9);
    }

    .grammar-card h3 {
        margin-top: 0;
        font-size: 27px;
        font-weight: 900;
    }

    .grammar-card p {
        font-size: 21px;
        line-height: 1.85;
        color: #374151;
    }

    .formula-box {
        background: rgba(255,255,255,0.85);
        padding: 18px 20px;
        border-radius: 22px;
        font-size: 27px;
        font-weight: 900;
        text-align: center;
        margin-top: 16px;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.9);
    }

    .example-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
        padding: 20px 22px;
        border-radius: 22px;
        margin: 16px 0;
        box-shadow: 0 5px 14px rgba(0,0,0,0.055);
        font-size: 20px;
        line-height: 1.85;
        border: 1.5px solid #e8f0ff;
        color: #334155;
    }

    .example-box b {
        color: #2563eb;
    }

    .mini-card {
        background: linear-gradient(135deg, #ffffff 0%, #fbfdff 100%);
        border-radius: 24px;
        padding: 22px 24px;
        margin: 14px 0;
        box-shadow: 0 5px 16px rgba(0,0,0,0.055);
        border: 1.5px solid #edf2ff;
    }

    .mini-card h4 {
        margin-top: 0;
        color: #2563eb;
        font-size: 22px;
        font-weight: 900;
    }

    .mini-card p {
        font-size: 20px;
        line-height: 1.75;
        color: #374151;
    }

    .word-chip {
        display: inline-block;
        background: linear-gradient(135deg, #eef6ff, #ffffff);
        border: 1.5px solid #cfe2ff;
        border-radius: 999px;
        padding: 9px 16px;
        margin: 6px;
        font-size: 18px;
        font-weight: 800;
        color: #1f4e79;
        box-shadow: 0 3px 8px rgba(31,78,121,0.08);
    }

    button[data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 800;
    }

    table {
        font-size: 18px !important;
        border-radius: 14px;
        overflow: hidden;
    }

    thead tr th {
        background-color: #eef6ff !important;
        color: #1f4e79 !important;
        font-weight: 900 !important;
    }

    tbody tr td {
        background-color: #ffffff !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 18px;
        font-size: 18px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        padding: 0.45rem 1.1rem;
        border: 1.5px solid #d9e7ff;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        color: #2563eb;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 상단 제목
# =========================================================
st.markdown(
    """
    <div class="title-box">
        <h1>🧩 English Sentence Guide</h1>
        <p>be동사, 일반동사, 시제, 부정문, 의문문을 차근차근 익혀 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

tabs = st.tabs([
    "🌱 Be동사 / 일반동사",
    "🏃 현재진행형",
    "🚀 미래형",
    "🕰️ 과거형",
    "🎮 불규칙동사 게임",
    "❌ 부정문",
    "❓ 의문문"
])


# =========================================================
# Tab 1: Be동사 / 일반동사
# =========================================================
with tabs[0]:
    st.subheader("🌱 Be동사 / 일반동사")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#f3f8ff,#ffffff);">
            <h3 style="color:#1f4e79;">🌼 Be동사란?</h3>
            <p>
                <b>Be동사</b>는 보통 <b>‘~이다’</b>라는 뜻으로 쓰입니다.
            </p>
            <div class="example-box">
                <b>I am a boy.</b><br>
                → 나는 소년이다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Be동사에는 am, are, is가 있습니다.")

    st.markdown("### ✅ Be동사 고르는 법")

    st.markdown(
        """
        <div class="mini-card">
            <h4>🌷 2. is</h4>
            <p>주어가 <b>1개</b>일 때 씁니다.</p>
            <div class="example-box">
                He <b>is</b> kind.<br>
                She <b>is</b> happy.<br>
                It <b>is</b> a dog.
            </div>
        </div>

        <div class="mini-card">
            <h4>🌈 3. are</h4>
            <p>주어가 <b>2개 이상</b>이거나 <b>you / we / they</b>일 때 씁니다.</p>
            <div class="example-box">
                You <b>are</b> my friend.<br>
                We <b>are</b> students.<br>
                They <b>are</b> happy.
            </div>
        </div>
                <div class="mini-card">
            <h4>🌱 1. am</h4>
            <p>주어가 <b>I</b>일 때 씁니다. '나'는 1명이지만 나는 특별하기에 다른 것들과 차별을 두기 위해서 'is'가 아닌 'am'을 씁니다.</p>
            <div class="example-box">
                I <b>am</b> a student.<br>
                → 나는 학생이다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 일반동사란?")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fffdf4,#ffffff);">
            <p>
                <b>Be동사 am, are, is를 제외한 나머지 동작 표현</b>은 대부분 일반동사입니다.
            </p>
            <p>예를 들면 다음과 같습니다.</p>
            <span class="word-chip">do 하다</span>
            <span class="word-chip">play 놀다 / 경기하다</span>
            <span class="word-chip">sleep 자다</span>
            <span class="word-chip">eat 먹다</span>
            <span class="word-chip">go 가다</span>
            <span class="word-chip">study 공부하다</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Tab 2: 현재진행형
# =========================================================
with tabs[1]:
    st.subheader("🏃 현재진행형")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fff8e6,#ffffff);">
            <h3 style="color:#8a5a00;">🏃 현재진행형이란?</h3>
            <p>
                <b>현재진행형</b>은 <b>지금 하고 있는 일</b>을 말할 때 씁니다.
            </p>
            <div class="formula-box" style="color:#8a5a00;">
                be동사 + 동사-ing
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 만드는 법")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>am / are / is + 동사ing</b></p>
        </div>

        <div class="example-box">
            I <b>am eating</b> lunch.<br>
            → 나는 점심을 먹고 있다.
        </div>

        <div class="example-box">
            She <b>is reading</b> a book.<br>
            → 그녀는 책을 읽고 있다.
        </div>

        <div class="example-box">
            They <b>are playing</b> soccer.<br>
            → 그들은 축구를 하고 있다.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Tab 3: 미래형
# =========================================================
with tabs[2]:
    st.subheader("🚀 미래형")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#ecfff1,#ffffff);">
            <h3 style="color:#247a3d;">🚀 미래형이란?</h3>
            <p>
                <b>미래형</b>은 <b>앞으로 일어날 일</b>을 말할 때 씁니다.
            </p>
            <div class="formula-box" style="color:#247a3d;">
                will + 동사원형
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 만드는 법")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>will + 동사원형</b></p>
            <p>will 뒤에는 동사의 기본 모양을 씁니다.</p>
        </div>

        <div class="example-box">
            I <b>will study</b> English.<br>
            → 나는 영어를 공부할 것이다.
        </div>

        <div class="example-box">
            She <b>will call</b> me.<br>
            → 그녀는 나에게 전화할 것이다.
        </div>

        <div class="example-box">
            We <b>will go</b> to Busan.<br>
            → 우리는 부산에 갈 것이다.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Tab 4: 과거형
# =========================================================
with tabs[3]:
    st.subheader("🕰️ 과거형")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fff0f6,#ffffff);">
            <h3 style="color:#9b2c5a;">🕰️ 과거형이란?</h3>
            <p>
                <b>과거형</b>은 <b>이미 일어난 일</b>을 말할 때 씁니다.
            </p>
            <div class="formula-box" style="color:#9b2c5a;">
                규칙동사: 동사 + ed
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 규칙동사 만드는 법")

    st.markdown(
        """
        <div class="mini-card">
            <p>규칙동사는 보통 동사 뒤에 <b>-ed</b>를 붙입니다.</p>
        </div>

        <div class="example-box">
            play → <b>played</b><br>
            I <b>played</b> soccer yesterday.<br>
            → 나는 어제 축구를 했다.
        </div>

        <div class="example-box">
            walk → <b>walked</b><br>
            She <b>walked</b> to school.<br>
            → 그녀는 학교에 걸어갔다.
        </div>

        <div class="example-box">
            clean → <b>cleaned</b><br>
            We <b>cleaned</b> the room.<br>
            → 우리는 방을 청소했다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ⭐ 불규칙동사")

    st.warning("모든 동사에 -ed를 붙이는 것은 아닙니다. 불규칙동사는 따로 외워야 합니다.")

    st.markdown(
        """
        | 현재형 | 과거형 | 뜻 |
        |---|---|---|
        | go | went | 가다 |
        | eat | ate | 먹다 |
        | see | saw | 보다 |
        | have | had | 가지다 / 먹다 |
        | make | made | 만들다 |
        | come | came | 오다 |
        | do | did | 하다 |
        | take | took | 가져가다 / 타다 |
        | write | wrote | 쓰다 |
        | read | read | 읽다 |
        """
    )

    st.info("Tip: 불규칙동사는 바로 옆의 🎮 불규칙동사 게임 탭에서 재미있게 연습할 수 있습니다.")


# =========================================================
# Tab 5: 불규칙동사 게임
# =========================================================
with tabs[4]:
    st.subheader("🎮 불규칙동사 미니게임")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fffbe6,#ffffff);">
            <h3 style="color:#8a6d00;">🎲 불규칙동사란?</h3>
            <p>
                <b>불규칙동사</b>는 과거형을 만들 때 <b>-ed를 붙이지 않고</b>
                모양이 다르게 바뀌는 동사입니다.
            </p>
            <div class="formula-box" style="color:#8a6d00;">
                go → went / eat → ate / see → saw
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("먼저 카드로 외우고, 그다음 직접 맞혀 보세요!")

    irregular_verbs = [
        {"base": "be", "past": "was / were", "meaning": "~이다 / 있다"},
        {"base": "become", "past": "became", "meaning": "~이 되다"},
        {"base": "begin", "past": "began", "meaning": "시작하다"},
        {"base": "break", "past": "broke", "meaning": "깨다 / 부수다"},
        {"base": "bring", "past": "brought", "meaning": "가져오다"},
        {"base": "build", "past": "built", "meaning": "짓다 / 만들다"},
        {"base": "buy", "past": "bought", "meaning": "사다"},
        {"base": "catch", "past": "caught", "meaning": "잡다"},
        {"base": "choose", "past": "chose", "meaning": "고르다"},
        {"base": "come", "past": "came", "meaning": "오다"},
        {"base": "cut", "past": "cut", "meaning": "자르다"},
        {"base": "do", "past": "did", "meaning": "하다"},
        {"base": "draw", "past": "drew", "meaning": "그리다"},
        {"base": "drink", "past": "drank", "meaning": "마시다"},
        {"base": "drive", "past": "drove", "meaning": "운전하다"},
        {"base": "eat", "past": "ate", "meaning": "먹다"},
        {"base": "fall", "past": "fell", "meaning": "떨어지다 / 넘어지다"},
        {"base": "feel", "past": "felt", "meaning": "느끼다"},
        {"base": "find", "past": "found", "meaning": "찾다 / 발견하다"},
        {"base": "fly", "past": "flew", "meaning": "날다"},
        {"base": "forget", "past": "forgot", "meaning": "잊다"},
        {"base": "get", "past": "got", "meaning": "얻다 / 받다 / 되다"},
        {"base": "give", "past": "gave", "meaning": "주다"},
        {"base": "go", "past": "went", "meaning": "가다"},
        {"base": "grow", "past": "grew", "meaning": "자라다 / 기르다"},
        {"base": "have", "past": "had", "meaning": "가지다 / 먹다"},
        {"base": "hear", "past": "heard", "meaning": "듣다"},
        {"base": "hold", "past": "held", "meaning": "잡다 / 열다"},
        {"base": "keep", "past": "kept", "meaning": "유지하다 / 보관하다"},
        {"base": "know", "past": "knew", "meaning": "알다"},
        {"base": "leave", "past": "left", "meaning": "떠나다 / 남기다"},
        {"base": "lose", "past": "lost", "meaning": "잃다 / 지다"},
        {"base": "make", "past": "made", "meaning": "만들다"},
        {"base": "meet", "past": "met", "meaning": "만나다"},
        {"base": "pay", "past": "paid", "meaning": "지불하다"},
        {"base": "put", "past": "put", "meaning": "놓다 / 두다"},
        {"base": "read", "past": "read", "meaning": "읽다"},
        {"base": "ride", "past": "rode", "meaning": "타다"},
        {"base": "run", "past": "ran", "meaning": "달리다"},
        {"base": "say", "past": "said", "meaning": "말하다"},
        {"base": "see", "past": "saw", "meaning": "보다"},
        {"base": "sell", "past": "sold", "meaning": "팔다"},
        {"base": "send", "past": "sent", "meaning": "보내다"},
        {"base": "sing", "past": "sang", "meaning": "노래하다"},
        {"base": "sit", "past": "sat", "meaning": "앉다"},
        {"base": "sleep", "past": "slept", "meaning": "자다"},
        {"base": "speak", "past": "spoke", "meaning": "말하다"},
        {"base": "spend", "past": "spent", "meaning": "쓰다 / 보내다"},
        {"base": "stand", "past": "stood", "meaning": "서다"},
        {"base": "swim", "past": "swam", "meaning": "수영하다"},
    ]

    game_tabs = st.tabs([
        "🃏 카드로 외우기",
        "✏️ 직접 맞히기",
        "📋 전체 리스트"
    ])

    with game_tabs[0]:
        st.markdown("### 🃏 카드로 외우기")
        st.caption("버튼을 누르면 불규칙동사가 하나씩 나옵니다.")

        if "verb_card_index" not in st.session_state:
            st.session_state.verb_card_index = 0

        current = irregular_verbs[st.session_state.verb_card_index]

        st.markdown(
            f"""
            <div style="
                background:linear-gradient(135deg,#eef5ff,#ffffff);
                border-radius:30px;
                padding:32px;
                margin:20px 0;
                text-align:center;
                box-shadow:0 8px 22px rgba(0,0,0,0.08);
                border:1.5px solid #d7e8ff;
            ">
                <p style="font-size:20px; color:#666; margin-bottom:8px;">현재형</p>
                <h1 style="font-size:48px; color:#1f4e79; margin:8px 0;">{current["base"]}</h1>
                <p style="font-size:20px; color:#666; margin-bottom:8px;">과거형</p>
                <h1 style="font-size:48px; color:#d46b08; margin:8px 0;">{current["past"]}</h1>
                <p style="font-size:23px; color:#333; margin-top:18px;">
                    뜻: <b>{current["meaning"]}</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            f"현재 카드: **{st.session_state.verb_card_index + 1} / {len(irregular_verbs)}**"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅️ 이전 카드"):
                st.session_state.verb_card_index -= 1

                if st.session_state.verb_card_index < 0:
                    st.session_state.verb_card_index = len(irregular_verbs) - 1

                st.rerun()

        with col2:
            if st.button("다음 카드 ➡️"):
                st.session_state.verb_card_index += 1

                if st.session_state.verb_card_index >= len(irregular_verbs):
                    st.session_state.verb_card_index = 0

                st.rerun()

    with game_tabs[1]:
        st.markdown("### ✏️ 직접 맞히기")
        st.caption("현재형을 보고 과거형을 직접 입력해 봅시다.")

        if "verb_quiz_index" not in st.session_state:
            st.session_state.verb_quiz_index = 0

        if "verb_score" not in st.session_state:
            st.session_state.verb_score = 0

        if "verb_answer_checked" not in st.session_state:
            st.session_state.verb_answer_checked = False

        quiz_item = irregular_verbs[st.session_state.verb_quiz_index]

        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border-radius:26px;
                padding:26px;
                margin:18px 0;
                text-align:center;
                box-shadow:0 6px 16px rgba(0,0,0,0.07);
                border:1.5px solid #eeeeee;
            ">
                <p style="font-size:20px; color:#666;">다음 동사의 과거형은?</p>
                <h1 style="font-size:46px; color:#1f4e79;">{quiz_item["base"]}</h1>
                <p style="font-size:20px;">뜻: <b>{quiz_item["meaning"]}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        user_answer = st.text_input(
            "과거형을 입력하세요.",
            key=f"verb_input_{st.session_state.verb_quiz_index}"
        )

        if st.button("정답 확인"):
            st.session_state.verb_answer_checked = True

            correct_answer = quiz_item["past"].replace(" ", "").lower()
            user_clean = user_answer.strip().replace(" ", "").lower()

            if user_clean == correct_answer:
                st.success("정답입니다! 아주 좋아요 🎉")
                st.balloons()
                st.session_state.verb_score += 1
            else:
                st.error("아쉽습니다. 다시 확인해 봅시다.")
                st.write(f"정답은 **{quiz_item['past']}** 입니다.")

        if st.session_state.verb_answer_checked:
            if st.button("다음 문제"):
                st.session_state.verb_quiz_index += 1
                st.session_state.verb_answer_checked = False

                if st.session_state.verb_quiz_index >= len(irregular_verbs):
                    st.session_state.verb_quiz_index = 0
                    st.success("한 바퀴를 모두 끝냈습니다! 다시 처음부터 연습합니다.")

                st.rerun()

        st.markdown("---")
        st.write(f"현재 문제: **{st.session_state.verb_quiz_index + 1} / {len(irregular_verbs)}**")
        st.write(f"현재 점수: **{st.session_state.verb_score}점**")

        if st.button("점수 초기화"):
            st.session_state.verb_score = 0
            st.session_state.verb_quiz_index = 0
            st.session_state.verb_answer_checked = False
            st.rerun()

    with game_tabs[2]:
        st.markdown("### 📋 자주 나오는 불규칙동사 50개")
        st.caption("10개씩 나누어 보면서 익혀 봅시다.")

        for i in range(0, len(irregular_verbs), 10):
            st.markdown(f"#### {i + 1}번 ~ {min(i + 10, len(irregular_verbs))}번")

            table_text = "| 현재형 | 과거형 | 뜻 |\n|---|---|---|\n"

            for verb in irregular_verbs[i:i + 10]:
                table_text += f"| {verb['base']} | {verb['past']} | {verb['meaning']} |\n"

            st.markdown(table_text)

        st.info("먼저 카드로 외우고, 그다음 직접 맞히기를 하면 훨씬 잘 기억납니다.")


# =========================================================
# Tab 6: 부정문
# =========================================================
with tabs[5]:
    st.subheader("❌ 부정문 만들기")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fff3f3,#ffffff);">
            <h3 style="color:#b23a3a;">❌ 부정문이란?</h3>
            <p>
                <b>부정문</b>은 <b>‘~이 아니다’, ‘~하지 않는다’</b>라는 뜻을 나타내는 문장입니다.
            </p>
            <div class="formula-box" style="color:#b23a3a;">
                not을 넣어서 부정의 뜻을 만듭니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 1. Be동사의 부정문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>Be동사 + not</b></p>
            <p>am, are, is 뒤에 <b>not</b>을 붙입니다.</p>
        </div>

        <div class="example-box">
            I <b>am not</b> a student.<br>
            → 나는 학생이 아니다.
        </div>

        <div class="example-box">
            She <b>is not</b> happy.<br>
            → 그녀는 행복하지 않다.
        </div>

        <div class="example-box">
            They <b>are not</b> busy.<br>
            → 그들은 바쁘지 않다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 2. 일반동사의 부정문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>do not / does not / did not + 동사원형</b></p>
            <p>일반동사는 바로 not을 붙이지 않고 <b>do, does, did</b>의 도움을 받습니다.</p>
        </div>

        <div class="example-box">
            I <b>do not like</b> coffee.<br>
            → 나는 커피를 좋아하지 않는다.
        </div>

        <div class="example-box">
            He <b>does not play</b> soccer.<br>
            → 그는 축구를 하지 않는다.
        </div>

        <div class="example-box">
            They <b>did not go</b> to school yesterday.<br>
            → 그들은 어제 학교에 가지 않았다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: does not, did not 뒤에는 동사의 기본 모양을 씁니다. 예: does not plays ❌ / does not play ✅")


# =========================================================
# Tab 7: 의문문
# =========================================================
with tabs[6]:
    st.subheader("❓ 의문문 만들기")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#f3f0ff,#ffffff);">
            <h3 style="color:#5b3aa4;">❓ 의문문이란?</h3>
            <p>
                <b>의문문</b>은 <b>질문하는 문장</b>입니다.
            </p>
            <div class="formula-box" style="color:#5b3aa4;">
                앞에 오는 단어가 중요합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 1. Be동사의 의문문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>Be동사 + 주어 ~ ?</b></p>
            <p>am, are, is를 문장 앞으로 보냅니다.</p>
        </div>

        <div class="example-box">
            You are a student.<br>
            ↓<br>
            <b>Are you</b> a student?<br>
            → 너는 학생이니?
        </div>

        <div class="example-box">
            She is happy.<br>
            ↓<br>
            <b>Is she</b> happy?<br>
            → 그녀는 행복하니?
        </div>

        <div class="example-box">
            They are in the classroom.<br>
            ↓<br>
            <b>Are they</b> in the classroom?<br>
            → 그들은 교실에 있니?
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 2. 일반동사의 의문문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>Do / Does / Did + 주어 + 동사원형 ~ ?</b></p>
            <p>일반동사 의문문은 <b>Do, Does, Did</b>를 문장 앞에 씁니다.</p>
        </div>

        <div class="example-box">
            You like coffee.<br>
            ↓<br>
            <b>Do you like</b> coffee?<br>
            → 너는 커피를 좋아하니?
        </div>

        <div class="example-box">
            He plays soccer.<br>
            ↓<br>
            <b>Does he play</b> soccer?<br>
            → 그는 축구를 하니?
        </div>

        <div class="example-box">
            They went to school yesterday.<br>
            ↓<br>
            <b>Did they go</b> to school yesterday?<br>
            → 그들은 어제 학교에 갔니?
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: Does, Did가 앞에 오면 뒤의 동사는 기본 모양을 씁니다. 예: Does he plays? ❌ / Does he play? ✅")
