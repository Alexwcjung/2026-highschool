import streamlit as st

st.set_page_config(
    page_title="Survival English",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------
# Top Section
# ---------------------------
st.markdown("# 🌍 Survival English")
st.markdown("### 미국 생활과 일상 대화에 꼭 필요한 기초 영어 400")

st.info(
    """
    **Survival English**는 영어가 낯설고 자신 없는 학습자도  
    일상생활에서 바로 사용할 수 있는 단어와 표현을  
    듣고, 따라하고, 퀴즈로 익힐 수 있도록 만든 영어 학습 공간입니다.

    학교, 집, 식당, 쇼핑, 교통, 여행, 감정 표현 등  
    실제 생활에서 자주 쓰는 영어를 테마별로 쉽고 반복적으로 학습합니다.
    """
)

st.divider()

# ---------------------------
# Quick Guide
# ---------------------------
st.markdown("## 🌱 이 앱은 이런 학습자를 위한 공간입니다")

g1, g2, g3 = st.columns(3)

with g1:
    with st.container(border=True):
        st.markdown("### 🔰 영어가 아직 낯선 학습자")
        st.write("어려운 문법보다 먼저, 자주 쓰는 단어와 표현부터 시작합니다.")
        st.caption("영어를 몰라도 천천히 따라올 수 있어요.")

with g2:
    with st.container(border=True):
        st.markdown("### 🔊 듣고 따라하고 싶은 학습자")
        st.write("단어 발음을 반복해서 들으며 소리와 뜻을 자연스럽게 연결합니다.")
        st.caption("많이 들으면 영어 소리가 익숙해져요.")

with g3:
    with st.container(border=True):
        st.markdown("### 🧳 실생활 영어가 필요한 학습자")
        st.write("식당, 쇼핑, 길 찾기, 여행 등 실제 상황에서 쓸 수 있는 표현을 배웁니다.")
        st.caption("교실 밖에서도 사용할 수 있는 영어입니다.")

st.divider()

# ---------------------------
# Learning Path
# ---------------------------
st.markdown("## 🌈 Learning Path")
st.caption("아래 순서대로 학습하면 단어 → 듣기 → 퀴즈 → 복습 흐름으로 영어 기초를 쌓을 수 있습니다.")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 🧠 STEP 1")
        st.markdown("## Theme Words")
        st.markdown(
            """
            학교, 집, 식당, 쇼핑, 교통, 여행 등  
            **생활 속 테마별 단어**를 익혀요.

            영어 단어와 한국어 뜻을 함께 보며  
            기본 어휘를 차근차근 쌓습니다.
            """
        )
        st.success("🌱 목표: 꼭 필요한 기초 단어 기억하기")

with col2:
    with st.container(border=True):
        st.markdown("### 🔊 STEP 2")
        st.markdown("## Cassette Listening")
        st.markdown(
            """
            카세트 듣기 기능으로  
            단어 발음을 반복해서 들어요.

            한 단어를 여러 번 듣고  
            소리와 뜻을 자연스럽게 연결합니다.
            """
        )
        st.warning("🍯 목표: 영어 소리에 익숙해지기")

with col3:
    with st.container(border=True):
        st.markdown("### 📝 STEP 3")
        st.markdown("## Quiz & Review")
        st.markdown(
            """
            단어를 익힌 뒤  
            퀴즈로 내가 기억하는지 확인해요.

            틀린 문제는 다시 복습하면서  
            오래 기억할 수 있도록 연습합니다.
            """
        )
        st.info("🌈 목표: 듣고 보고 뜻을 떠올리기")

st.divider()

# ---------------------------
# Study Routine
# ---------------------------
st.markdown("## 🪄 추천 학습 루틴")
st.caption("하루에 한 테마씩만 반복해도 영어 단어와 표현이 훨씬 익숙해집니다.")

r1, r2, r3, r4 = st.columns(4)

with r1:
    with st.container(border=True):
        st.markdown("### 1️⃣ 보기")
        st.write("먼저 오늘의 테마 단어와 뜻을 확인합니다.")
        st.success("👀 Look first")

with r2:
    with st.container(border=True):
        st.markdown("### 2️⃣ 듣기")
        st.write("단어 발음을 반복해서 들어 봅니다.")
        st.info("🔊 Listen again")

with r3:
    with st.container(border=True):
        st.markdown("### 3️⃣ 따라하기")
        st.write("들은 단어를 소리 내어 따라 말합니다.")
        st.warning("🗣️ Repeat aloud")

with r4:
    with st.container(border=True):
        st.markdown("### 4️⃣ 퀴즈")
        st.write("퀴즈를 풀며 내가 아는지 확인합니다.")
        st.success("📝 Check yourself")

st.divider()

# ---------------------------
# Survival Message
# ---------------------------
st.success(
    """
    🎯 **Survival Message**

    영어는 어려운 시험 과목이기 전에  
    더 넓은 세상에서 사람들과 연결되는 도구입니다.

    오늘은 한 단어, 내일은 한 문장.  
    작은 표현 하나가 여러분의 세상을 조금 더 넓혀 줄 수 있습니다.

    **Survival English와 함께 생활 속 영어를 천천히 익혀 봅시다.**
    """
)
