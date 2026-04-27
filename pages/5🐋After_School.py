import streamlit as st

st.set_page_config(page_title="After School English", layout="wide")

st.title("🌱 After School English")
st.caption("개념을 먼저 보고, 실전연습으로 확인해 봅시다.")

# ---------------------------
# 큰 메뉴
# ---------------------------
main_menu = st.radio(
    "학습 메뉴를 선택하세요.",
    ["📚 개념", "✏️ 실전연습"],
    horizontal=True
)

st.markdown("---")


# =========================================================
# 1. 개념
# =========================================================
if main_menu == "📚 개념":

    st.header("📚 개념")

    concept_tab = st.tabs([
        "① Be동사 / 일반동사",
        "② 현재진행형",
        "③ 미래형",
        "④ 과거형"
    ])

    # ---------------------------
    # Be동사 / 일반동사
    # ---------------------------
    with concept_tab[0]:
        st.subheader("① Be동사 / 일반동사")

        st.info("Be동사는 보통 ‘~이다’라는 뜻으로 쓰입니다.")

        st.markdown(
            """
            ### ✅ Be동사란?

            **Be동사**는 `am`, `are`, `is`가 있습니다.

            예문:

            - **I am a boy.**  
              → 나는 소년이다.

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

            예:

            - **do**: 하다
            - **play**: 놀다 / 경기하다
            - **sleep**: 자다
            - **eat**: 먹다
            - **go**: 가다
            - **study**: 공부하다
            """
        )

    # ---------------------------
    # 현재진행형
    # ---------------------------
    with concept_tab[1]:
        st.subheader("② 현재진행형")

        st.info("현재진행형은 지금 하고 있는 일을 말할 때 씁니다.")

        st.success("현재진행형 만드는 법: be동사 + 동사-ing")

        st.markdown(
            """
            예문:

            - I **am eating** lunch.  
              → 나는 점심을 먹고 있다.

            - She **is reading** a book.  
              → 그녀는 책을 읽고 있다.

            - They **are playing** soccer.  
              → 그들은 축구를 하고 있다.
            """
        )

    # ---------------------------
    # 미래형
    # ---------------------------
    with concept_tab[2]:
        st.subheader("③ 미래형")

        st.info("미래형은 앞으로 일어날 일을 말할 때 씁니다.")

        st.success("미래형 만드는 법: will + 동사원형")

        st.markdown(
            """
            예문:

            - I **will study** English.  
              → 나는 영어를 공부할 것이다.

            - She **will call** me.  
              → 그녀는 나에게 전화할 것이다.

            - We **will go** to Busan.  
              → 우리는 부산에 갈 것이다.
            """
        )

    # ---------------------------
    # 과거형
    # ---------------------------
    with concept_tab[3]:
        st.subheader("④ 과거형")

        st.info("과거형은 이미 일어난 일을 말할 때 씁니다.")

        st.success("규칙동사 과거형 만드는 법: 동사 + ed")

        st.markdown(
            """
            ### ✅ 규칙동사

            - play → **played**  
              I **played** soccer yesterday.

            - walk → **walked**  
              She **walked** to school.

            - clean → **cleaned**  
              We **cleaned** the room.
            """
        )

        st.warning("불규칙동사는 모양이 다르게 바뀌기 때문에 따로 외워야 합니다.")

        st.markdown(
            """
            ### ⭐ 자주 나오는 불규칙동사

            | 현재형 | 과거형 | 뜻 |
            |---|---|---|
            | go | went | 가다 |
            | eat | ate | 먹다 |
            | see | saw | 보다 |
            | do | did | 하다 |
            | have | had | 가지다 / 먹다 |
            | make | made | 만들다 |
            | come | came | 오다 |
            | take | took | 가져가다 / 타다 |
            | write | wrote | 쓰다 |
            | read | read | 읽다 |
            """
        )


# =========================================================
# 2. 실전연습
# =========================================================
elif main_menu == "✏️ 실전연습":

    st.header("✏️ 실전연습")

    practice_tab = st.tabs([
        "① 시제 맞추기",
        "② 부정문 만들기",
        "③ 의문문 만들기"
    ])

    with practice_tab[0]:
        st.subheader("① 시제 맞추기")
        st.info("여기에 기존 시제 맞추기 퀴즈 코드를 넣으면 됩니다.")

    with practice_tab[1]:
        st.subheader("② 부정문 만들기")
        st.info("여기에 기존 부정문 만들기 퀴즈 코드를 넣으면 됩니다.")

    with practice_tab[2]:
        st.subheader("③ 의문문 만들기")
        st.info("여기에 기존 의문문 만들기 퀴즈 코드를 넣으면 됩니다.")
