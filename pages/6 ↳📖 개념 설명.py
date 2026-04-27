import streamlit as st

st.set_page_config(page_title="English Grammar Guide", layout="centered")

st.title("📚 English Grammar Guide")
st.caption("영어 문장의 기본 규칙을 쉽게 정리해 봅시다.")

tabs = st.tabs([
    "① Be동사 / 일반동사",
    "② 현재진행형",
    "③ 미래형",
    "④ 과거형"
])


# =========================================================
# Tab 1: Be동사 / 일반동사
# =========================================================
with tabs[0]:
    st.subheader("① Be동사 / 일반동사")

    st.markdown(
        """
        <div style="
            background-color:#f8fbff;
            border:1.5px solid #d9e7ff;
            border-radius:20px;
            padding:24px;
            margin-bottom:20px;
            box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
            <h3 style="color:#1f4e79;">📌 Be동사란?</h3>
            <p style="font-size:21px; line-height:1.8;">
                <b>Be동사</b>는 보통 <b>‘~이다’</b>라는 뜻으로 쓰입니다.
            </p>
            <p style="font-size:21px; line-height:1.8;">
                예: <b>I am a boy.</b> → 나는 소년이다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Be동사에는 am, are, is가 있습니다.")

    st.markdown(
        """
        ### ✅ Be동사 고르는 법

        - **am**: 주어가 **I**일 때  
          - I **am** a student.

        - **is**: 주어가 **1개**일 때  
          - He **is** kind.  
          - She **is** happy.  
          - It **is** a dog.

        - **are**: 주어가 **2개 이상**이거나 **you / we / they**일 때  
          - You **are** my friend.  
          - We **are** students.  
          - They **are** happy.
        """
    )

    st.markdown("---")

    st.markdown(
        """
        ### ✅ 일반동사란?

        **Be동사 am, are, is를 제외한 나머지 동작 표현**은 대부분 일반동사입니다.

        예를 들면:

        - **do**: 하다
        - **play**: 놀다 / 경기하다
        - **sleep**: 자다
        - **eat**: 먹다
        - **go**: 가다
        - **study**: 공부하다
        """
    )


# =========================================================
# Tab 2: 현재진행형
# =========================================================
with tabs[1]:
    st.subheader("② 현재진행형")

    st.markdown(
        """
        <div style="
            background-color:#fffdf7;
            border:1.5px solid #ffe7b8;
            border-radius:20px;
            padding:24px;
            margin-bottom:20px;
            box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
            <h3 style="color:#8a5a00;">📌 현재진행형이란?</h3>
            <p style="font-size:21px; line-height:1.8;">
                <b>현재진행형</b>은 <b>지금 하고 있는 일</b>을 말할 때 씁니다.
            </p>
            <p style="font-size:24px; font-weight:800; color:#8a5a00;">
                be동사 + 동사-ing
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### ✅ 만드는 법

        **am / are / is + 동사ing**

        예문:

        - I **am eating** lunch.  
          → 나는 점심을 먹고 있다.

        - She **is reading** a book.  
          → 그녀는 책을 읽고 있다.

        - They **are playing** soccer.  
          → 그들은 축구를 하고 있다.
        """
    )


# =========================================================
# Tab 3: 미래형
# =========================================================
with tabs[2]:
    st.subheader("③ 미래형")

    st.markdown(
        """
        <div style="
            background-color:#f7fff9;
            border:1.5px solid #cdeed6;
            border-radius:20px;
            padding:24px;
            margin-bottom:20px;
            box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
            <h3 style="color:#247a3d;">📌 미래형이란?</h3>
            <p style="font-size:21px; line-height:1.8;">
                <b>미래형</b>은 <b>앞으로 일어날 일</b>을 말할 때 씁니다.
            </p>
            <p style="font-size:24px; font-weight:800; color:#247a3d;">
                will + 동사원형
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### ✅ 만드는 법

        **will + 동사원형**

        예문:

        - I **will study** English.  
          → 나는 영어를 공부할 것이다.

        - She **will call** me.  
          → 그녀는 나에게 전화할 것이다.

        - We **will go** to Busan.  
          → 우리는 부산에 갈 것이다.
        """
    )


# =========================================================
# Tab 4: 과거형
# =========================================================
# =========================================================
# Tab 4: 과거형
# =========================================================
with tabs[3]:
    st.subheader("④ 과거형")

    st.markdown(
        """
        <div style="
            background-color:#fff8fb;
            border:1.5px solid #ffd6e5;
            border-radius:20px;
            padding:24px;
            margin-bottom:20px;
            box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
            <h3 style="color:#9b2c5a;">📌 과거형이란?</h3>
            <p style="font-size:21px; line-height:1.8;">
                <b>과거형</b>은 <b>이미 일어난 일</b>을 말할 때 씁니다.
            </p>
            <p style="font-size:24px; font-weight:800; color:#9b2c5a;">
                규칙동사: 동사 + ed
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### ✅ 규칙동사 만드는 법

        규칙동사는 보통 동사 뒤에 **-ed**를 붙입니다.

        - play → **played**  
          I **played** soccer yesterday.  
          → 나는 어제 축구를 했다.

        - walk → **walked**  
          She **walked** to school.  
          → 그녀는 학교에 걸어갔다.

        - clean → **cleaned**  
          We **cleaned** the room.  
          → 우리는 방을 청소했다.
        """
    )

    st.markdown("---")

    st.markdown(
        """
        ### ⭐ 불규칙동사

        하지만 모든 동사에 **-ed**를 붙이는 것은 아닙니다.  
        **불규칙동사는 모양이 다르게 바뀌기 때문에 따로 외워야 합니다.**

        자주 나오는 불규칙동사 예시는 다음과 같습니다.

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

    st.info("Tip: 불규칙동사는 규칙이 일정하지 않기 때문에 자주 보고, 읽고, 써 보면서 익히는 것이 좋습니다.")
