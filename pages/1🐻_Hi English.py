import streamlit as st

st.set_page_config(
    page_title="Alex's Fun English",
    page_icon="🌈",
    layout="wide"
)

# ---------------------------
# Top Section
# ---------------------------
st.markdown("# 🌈 Alex의 영어교실")
st.markdown("### 기초부터 말하기와 듣기를 익히는 영어 학습 공간")

st.info(
    """
    **Alex의 영어교실**은 영어가 낯설고 자신 없는 학습자도  
    쉬운 단어와 문장을 듣고, 따라 말하며  
    기초 영어 실력을 천천히 쌓을 수 있도록 만든 학습 앱입니다.
    """
)

st.divider()

# ---------------------------
# Main Guide
# ---------------------------
st.markdown("## 🌱 이 앱에서 할 수 있는 것")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 🔊 듣기")
        st.write("단어와 문장을 반복해서 들으며 영어 소리에 익숙해집니다.")

with col2:
    with st.container(border=True):
        st.markdown("### 🗣️ 따라 말하기")
        st.write("들은 영어를 직접 소리 내어 말하며 표현을 익힙니다.")

with col3:
    with st.container(border=True):
        st.markdown("### 📝 확인하기")
        st.write("간단한 퀴즈와 활동으로 내가 익힌 내용을 확인합니다.")

st.divider()

# ---------------------------
# Learning Flow
# ---------------------------
st.markdown("## 🪄 학습 순서")

step1, step2, step3, step4 = st.columns(4)

with step1:
    with st.container(border=True):
        st.markdown("### 1️⃣ 보기")
        st.write("오늘 배울 단어와 표현을 확인합니다.")

with step2:
    with st.container(border=True):
        st.markdown("### 2️⃣ 듣기")
        st.write("영어 발음을 반복해서 들어 봅니다.")

with step3:
    with st.container(border=True):
        st.markdown("### 3️⃣ 말하기")
        st.write("소리 내어 따라 말해 봅니다.")

with step4:
    with st.container(border=True):
        st.markdown("### 4️⃣ 복습")
        st.write("퀴즈로 다시 확인합니다.")

st.divider()

# ---------------------------
# Closing Message
# ---------------------------
st.success(
    """
    🎯 **오늘의 한 걸음**

    영어는 한 번에 잘하려고 하기보다  
    매일 조금씩 듣고 말하면서 익숙해지는 것이 중요합니다.

    오늘도 한 단어, 한 문장씩 천천히 연습해 봅시다.
    """
)
