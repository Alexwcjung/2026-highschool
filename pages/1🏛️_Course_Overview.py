import streamlit as st

st.set_page_config(
    page_title="Alex's Fun English",
    page_icon="🌈",
    layout="wide"
)

# ---------------------------
# Top Section
# ---------------------------
st.markdown("## 🌱 🔤 🌈 ✨")
st.title("Alex의 영어교실")

st.markdown("### 영어가 낯설고 자신 없는 학습자를 위한 첫걸음")

st.info(
    """
    영어에 자신감이 없으신가요?  
    영어만 생각하면 어렵고, 틀릴까 봐 말하기가 망설여지나요?

    **Alex의 영어교실**은 알파벳을 처음 읽는 학습자부터  
    기초 영어 듣기와 문장 구조를 다시 배우고 싶은 학습자까지  
    누구나 쉽게 시작할 수 있도록 만든 영어 학습 공간입니다.
    """
)

st.divider()

# ---------------------------
# Learning Path
# ---------------------------
st.markdown("## 🌈 Learning Path")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 🔤 STEP 1")
        st.markdown("## Alphabet & Phonics")
        st.markdown(
            """
            A B C부터 시작해  
            **글자와 소리**를 익혀요.

            알파벳 이름과 실제 소리를  
            구분하며 읽기 기초를 배웁니다.
            """
        )

with col2:
    with st.container(border=True):
        st.markdown("### 🔊 STEP 2")
        st.markdown("## Words & Listening")
        st.markdown(
            """
            쉬운 단어를 듣고  
            **뜻과 발음**을 연결해요.

            자주 쓰는 단어를  
            테마별로 반복 학습합니다.
            """
        )

with col3:
    with st.container(border=True):
        st.markdown("### 🧩 STEP 3")
        st.markdown("## Sentence Structure")
        st.markdown(
            """
            단어를 문장으로 연결해  
            **기초 문장 구조**를 배워요.

            be동사, 일반동사, 시제,  
            부정문을 쉽게 연습합니다.
            """
        )

st.divider()

# ---------------------------
# Class Message
# ---------------------------
st.success(
    """
    🎯 **Class Message**

    영어는 어려운 과목이 아니라,  
    더 큰 세상으로 나아가는 작은 첫걸음입니다.

    Alex의 영어교실에서 오늘도 한 글자, 한 단어, 한 문장씩  
    천천히 성장해 봅시다.
    """
)
