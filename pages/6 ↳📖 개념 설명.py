import streamlit as st

st.set_page_config(page_title="English Grammar Guide", layout="centered")

# =========================================================
# 전체 디자인 CSS
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #fbfcff;
    }

    .title-box {
        background: linear-gradient(135deg, #e9f2ff, #fff7e6);
        padding: 28px;
        border-radius: 24px;
        margin-bottom: 24px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        text-align: center;
    }

    .title-box h1 {
        color: #1f3b57;
        margin-bottom: 8px;
        font-size: 34px;
    }

    .title-box p {
        color: #555;
        font-size: 18px;
        margin: 0;
    }

    .grammar-card {
        border-radius: 24px;
        padding: 26px;
        margin: 18px 0 24px 0;
        box-shadow: 0 6px 16px rgba(0,0,0,0.07);
        border: 1.5px solid rgba(0,0,0,0.05);
    }

    .grammar-card h3 {
        margin-top: 0;
        font-size: 25px;
    }

    .grammar-card p {
        font-size: 21px;
        line-height: 1.8;
    }

    .formula-box {
        background-color: rgba(255,255,255,0.75);
        padding: 16px;
        border-radius: 18px;
        font-size: 25px;
        font-weight: 800;
        text-align: center;
        margin-top: 14px;
    }

    .example-box {
        background-color: #ffffff;
        border-left: 6px solid #8bbcff;
        padding: 18px 20px;
        border-radius: 16px;
        margin: 14px 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
        font-size: 19px;
        line-height: 1.8;
    }

    .mini-card {
        background-color: #ffffff;
        border-radius: 18px;
        padding: 18px;
        margin: 12px 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        border: 1px solid #eeeeee;
    }

    .mini-card h4 {
        margin-top: 0;
        color: #1f4e79;
    }

    .word-chip {
        display: inline-block;
        background-color: #eef5ff;
        border: 1px solid #cfe2ff;
        border-radius: 999px;
        padding: 8px 14px;
        margin: 5px;
        font-size: 18px;
        font-weight: 700;
    }

    table {
        font-size: 18px !important;
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
        <h1>📚 English Grammar Guide</h1>
        <p>영어 문장의 기본 규칙을 쉽고 예쁘게 정리해 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

tabs = st.tabs([
    "🌱 Be동사 / 일반동사",
    "🏃 현재진행형",
    "🚀 미래형",
    "🕰️ 과거형",
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
            <h3 style="color:#1f4e79;">📌 Be동사란?</h3>
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
            <h4>1. am</h4>
            <p>주어가 <b>I</b>일 때 씁니다.</p>
            <div class="example-box">
                I <b>am</b> a student.<br>
                → 나는 학생이다.
            </div>
        </div>

        <div class="mini-card">
            <h4>2. is</h4>
            <p>주어가 <b>1개</b>일 때 씁니다.</p>
            <div class="example-box">
                He <b>is</b> kind.<br>
                She <b>is</b> happy.<br>
                It <b>is</b> a dog.
            </div>
        </div>

        <div class="mini-card">
            <h4>3. are</h4>
            <p>주어가 <b>2개 이상</b>이거나 <b>you / we / they</b>일 때 씁니다.</p>
            <div class="example-box">
                You <b>are</b> my friend.<br>
                We <b>are</b> students.<br>
                They <b>are</b> happy.
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
            <h3 style="color:#8a5a00;">📌 현재진행형이란?</h3>
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
            <h3 style="color:#247a3d;">📌 미래형이란?</h3>
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
            <h3 style="color:#9b2c5a;">📌 과거형이란?</h3>
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

    st.info("Tip: 불규칙동사는 자주 보고, 읽고, 써 보면서 익히는 것이 좋습니다.")


# =========================================================
# Tab 5: 부정문
# =========================================================
with tabs[4]:
    st.subheader("❌ 부정문 만들기")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fff3f3,#ffffff);">
            <h3 style="color:#b23a3a;">📌 부정문이란?</h3>
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
# Tab 6: 의문문
# =========================================================
with tabs[5]:
    st.subheader("❓ 의문문 만들기")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#f3f0ff,#ffffff);">
            <h3 style="color:#5b3aa4;">📌 의문문이란?</h3>
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
