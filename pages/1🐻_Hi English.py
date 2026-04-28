import streamlit as st

st.set_page_config(
    page_title="Alex's Fun English",
    page_icon="🌈",
    layout="wide"
)

# ---------------------------
# Top Section
# ---------------------------
st.markdown("# 🌼 Alex의 영어교실")
st.markdown("### ✨ 영어가 낯설고 자신 없는 학습자를 위한 첫걸음")

st.info(
    """
    **Alex의 영어교실**은 알파벳을 처음 읽는 학습자부터  
    기초 영어 듣기와 문장 구조를 다시 배우고 싶은 학습자까지  
    누구나 쉽게 시작할 수 있도록 만든 영어 학습 공간입니다.
    """
)

st.divider()

# ---------------------------
# Quick Guide
# ---------------------------
st.markdown("## 💖 이 앱은 이런 분들을 위한 공간입니다")

g1, g2, g3 = st.columns(3)

with g1:
    with st.container(border=True):
        st.markdown("### 🌱 처음부터 배우고 싶은 분")
        st.write("알파벳과 영어 소리부터 차근차근 시작할 수 있습니다.")
        st.caption("작은 시작도 괜찮아요.")

with g2:
    with st.container(border=True):
        st.markdown("### 🔊 듣기가 어려운 분")
        st.write("단어와 문장을 반복해서 들으며 소리와 뜻을 연결합니다.")
        st.caption("많이 들을수록 익숙해져요.")

with g3:
    with st.container(border=True):
        st.markdown("### 🧩 문장이 막막한 분")
        st.write("be동사, 일반동사, 시제, 부정문을 쉽게 연습합니다.")
        st.caption("문장도 조각처럼 맞추면 쉬워요.")

st.divider()

# ---------------------------
# Learning Path
# ---------------------------
st.markdown("## 🌈 Learning Path")
st.caption("아래 순서대로 천천히 따라오면 영어 기초를 자연스럽게 쌓을 수 있습니다.")

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
        st.success("🌱 목표: 영어 글자를 보고 소리를 떠올리기")

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
        st.warning("🍯 목표: 단어의 소리와 뜻을 함께 기억하기")

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
        st.info("🌈 목표: 쉬운 영어 문장을 스스로 이해하기")

st.divider()

# ---------------------------
# Study Routine
# ---------------------------
st.markdown("## 🪄 추천 학습 루틴")
st.caption("매일 조금씩 반복하면 영어가 훨씬 덜 낯설어집니다.")

r1, r2, r3, r4 = st.columns(4)

with r1:
    with st.container(border=True):
        st.markdown("### 1️⃣ 듣기")
        st.write("먼저 영어 소리를 들어 봅니다.")
        st.success("🔊 Listen first")

with r2:
    with st.container(border=True):
        st.markdown("### 2️⃣ 따라하기")
        st.write("단어와 문장을 소리 내어 따라 합니다.")
        st.info("🗣️ Repeat aloud")

with r3:
    with st.container(border=True):
        st.markdown("### 3️⃣ 문제 풀기")
        st.write("퀴즈로 내가 아는지 확인합니다.")
        st.warning("📝 Check yourself")

with r4:
    with st.container(border=True):
        st.markdown("### 4️⃣ 다시 복습")
        st.write("틀린 문제만 다시 풀며 기억합니다.")
        st.success("🌱 Try again")

st.divider()

# ---------------------------
# Class Message
# ---------------------------
st.success(
    """
    🎯 **Class Message**

    영어는 더 큰 세상으로 나아가는 작은 첫걸음입니다.
    Alex의 영어교실에서 오늘도 한 글자, 한 단어, 한 문장씩  
    천천히 성장해 봅시다.
    """
)
