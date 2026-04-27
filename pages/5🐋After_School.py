import streamlit as st

st.set_page_config(page_title="After School English", layout="wide")

st.sidebar.title("🌱 After School English")

menu = st.sidebar.radio(
    "Menu",
    [
        "📚 개념",
        "✏️ 실전연습"
    ]
)

if menu == "📚 개념":
    st.title("📚 개념")
    
    concept_tab = st.tabs([
        "Be동사 / 일반동사",
        "현재진행형",
        "미래형",
        "과거형"
    ])

    with concept_tab[0]:
        st.subheader("Be동사 / 일반동사")
        st.write("Be동사는 '~이다'라는 뜻으로 쓰입니다.")
        st.write("예: I am a boy. → 나는 소년이다.")
        st.write("am, are, is가 있습니다.")
        st.write("am은 주어가 I일 때 씁니다.")
        st.write("is는 주어가 1개일 때 씁니다.")
        st.write("are은 주어가 2개 이상이거나 you, we, they일 때 씁니다.")
        st.write("나머지는 대부분 일반동사입니다. 예: do, play, sleep, eat")

    with concept_tab[1]:
        st.subheader("현재진행형")
        st.write("현재진행형은 지금 하고 있는 일을 말할 때 씁니다.")
        st.success("be동사 + 동사-ing")
        st.write("예: I am eating lunch.")
        st.write("예: She is reading a book.")
        st.write("예: They are playing soccer.")

    with concept_tab[2]:
        st.subheader("미래형")
        st.write("미래형은 앞으로 일어날 일을 말할 때 씁니다.")
        st.success("will + 동사원형")
        st.write("예: I will study English.")
        st.write("예: She will call me.")
        st.write("예: We will go to Busan.")

    with concept_tab[3]:
        st.subheader("과거형")
        st.write("과거형은 이미 일어난 일을 말할 때 씁니다.")
        st.success("규칙동사: 동사 + ed")
        st.write("예: play → played")
        st.write("예: walk → walked")
        st.write("예: clean → cleaned")
        st.warning("불규칙동사는 모양이 다르게 바뀌기 때문에 따로 외워야 합니다.")
        st.write("예: go → went, eat → ate, see → saw, do → did, have → had")

elif menu == "✏️ 실전연습":
    st.title("✏️ 실전연습")

    practice_tab = st.tabs([
        "시제 맞추기",
        "부정문 만들기",
        "의문문 만들기"
    ])

    with practice_tab[0]:
        st.subheader("시제 맞추기")
        st.info("여기에 기존 시제 퀴즈 코드를 넣으면 됩니다.")

    with practice_tab[1]:
        st.subheader("부정문 만들기")
        st.info("여기에 기존 부정문 퀴즈 코드를 넣으면 됩니다.")

    with practice_tab[2]:
        st.subheader("의문문 만들기")
        st.info("여기에 기존 의문문 퀴즈 코드를 넣으면 됩니다.")
