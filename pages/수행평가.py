import streamlit as st

st.set_page_config(
    page_title="Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 영어 말하기 수행평가 연습")
st.caption("기초 영어 표현과 사진 묘사 말하기를 연습해 봅시다.")

st.markdown("---")

# =========================
# 1. 자기소개
# =========================
st.subheader("1. 자기소개하기")

st.markdown("""
### 🇰🇷 한국어
나는 **(본인 이름)** 입니다.

### 🇺🇸 English
**I am (name).**
""")

name = st.text_input("내 이름을 영어로 써 보세요.", placeholder="예: Woochang")

if name:
    st.success(f"I am {name}.")
else:
    st.info("예시: I am Woochang.")

st.markdown("---")

# =========================
# 2. 취미 말하기
# =========================
st.subheader("2. 나의 취미 말하기")

st.markdown("""
### 🇰🇷 한국어
나의 취미는 ~입니다. 나는 학생이고 키가 큽니다.

### 🇺🇸 English
**My hobby is (     ). I am a student and tall.**
""")

hobby = st.text_input("나의 취미를 영어로 써 보세요.", placeholder="예: soccer, music, dancing")

if hobby:
    st.success(f"My hobby is {hobby}. I am a student and tall.")
else:
    st.info("예시: My hobby is soccer. I am a student and tall.")

st.markdown("---")

# =========================
# 3. 시간 묻기 / 집에 가고 싶다
# =========================
st.subheader("3. 시간 묻기와 하고 싶은 말하기")

st.markdown("""
### 🇰🇷 한국어
지금 몇 시인가요? 저는 지금 집에 가고 싶습니다.

### 🇺🇸 English
**What time is it? I want to go home now.**
""")

st.code("What time is it? I want to go home now.", language="text")

st.markdown("---")

# =========================
# 4. 물과 음식 말하기
# =========================
st.subheader("4. 필요한 것 말하기")

st.markdown("""
### 🇰🇷 한국어
물을 마시고 싶어요. 음식도 먹고 싶습니다.

### 🇺🇸 English
**I want water. I want food too.**
""")

st.code("I want water. I want food too.", language="text")

st.markdown("---")

# =========================
# 5. 사진 묘사하기
# =========================
st.subheader("5. 사진 묘사하기")

st.markdown("""
### ⏱️ 제한 시간
**20초 안에 사진을 묘사해 봅시다.**

### 예시 문장
**There are many people in the street.  
I can see trees and buildings too.  
Some people are riding bikes and some are sitting in chairs.  
They look happy.**
""")

with st.expander("📘 사진 묘사 표현 보기"):
    st.markdown("""
    - **There are many people.**  
      사람들이 많이 있습니다.

    - **I can see trees and buildings.**  
      나무와 건물들이 보입니다.

    - **Some people are riding bikes.**  
      몇몇 사람들은 자전거를 타고 있습니다.

    - **Some people are sitting in chairs.**  
      몇몇 사람들은 의자에 앉아 있습니다.

    - **They look happy.**  
      그들은 행복해 보입니다.
    """)

st.markdown("---")

# =========================
# 전체 연습 문장
# =========================
st.subheader("📢 전체 말하기 연습")

full_script = """
I am (name).

My hobby is (hobby). I am a student and tall.

What time is it? I want to go home now.

I want water. I want food too.

There are many people in the street.
I can see trees and buildings too.
Some people are riding bikes and some are sitting in chairs.
They look happy.
"""

st.text_area("전체 말하기 대본", full_script, height=260)

st.success("위 문장을 보고 천천히 읽으면서 말하기 연습을 해 보세요.")
