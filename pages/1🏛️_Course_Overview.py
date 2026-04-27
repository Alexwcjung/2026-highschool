import streamlit as st

st.set_page_config(page_title="Alex's Fun English", layout="wide")

# ---------------------------
# Top Card
# ---------------------------
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #ffffff, #eef6ff);
        border: 1.5px solid #d9e7ff;
        border-radius: 30px;
        padding: 42px 32px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(31,78,121,0.12);
        margin-bottom: 30px;
    ">
        <div style="font-size: 64px; margin-bottom: 12px;">
            🌱 🔤 🌈 ✨
        </div>
        <div style="
            display: inline-block;
            background-color: #eaf3ff;
            color: #1f4e79;
            font-size: 16px;
            font-weight: 700;
            padding: 8px 18px;
            border-radius: 999px;
            margin-bottom: 18px;
        ">
            Fun English · Spring 2026
        </div>
        <h1 style="
            color:#1f4e79;
            font-size: 46px;
            font-weight: 900;
            margin: 12px 0 10px 0;
        ">
            Alex의 영어교실
        </h1>
        <h2 style="
            color:#2f6f9f;
            font-size: 28px;
            font-weight: 800;
            margin: 0 0 20px 0;
        ">
            처음 읽는 알파벳부터 쉬운 영어 문장까지
        </h2>
        <p style="
            font-size: 22px;
            line-height: 1.75;
            color: #34495e;
            margin: 0 auto;
            max-width: 850px;
        ">
            이 앱은 <b>알파벳을 처음 읽는 학습자</b>도 부담 없이 시작할 수 있도록 만든 
            기초 영어 학습 공간입니다.<br>
            소리로 알파벳과 단어를 익히고, 쉬운 활동을 통해 
            <b>기초 영어 듣기</b>와 <b>문장 구조</b>를 차근차근 배울 수 있습니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Course Activities
# ---------------------------
st.markdown(
    """
    <h2 style="
        color:#1f4e79;
        font-size:30px;
        margin-bottom:18px;
    ">
        🧭 Course Activities
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        background-color:#ffffff;
        border: 1.5px solid #e4ebff;
        border-radius: 22px;
        padding: 24px 28px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 26px;
    ">
        <p style="font-size:23px; line-height:1.8; margin:10px 0;">
            🔤 <b>Alphabet & Phonics</b>: 알파벳 이름과 실제 소리를 듣고 읽기 기초를 익혀요
        </p>
        <p style="font-size:23px; line-height:1.8; margin:10px 0;">
            🌱 <b>Word Practice</b>: 자주 쓰는 쉬운 단어를 테마별로 배우고 복습해요
        </p>
        <p style="font-size:23px; line-height:1.8; margin:10px 0;">
            🔊 <b>Listening Practice</b>: 단어와 문장을 듣고 소리와 의미를 연결해요
        </p>
        <p style="font-size:23px; line-height:1.8; margin:10px 0;">
            🧩 <b>Sentence Structure</b>: be동사, 일반동사, 시제, 부정문을 쉽게 연습해요
        </p>
        <p style="font-size:23px; line-height:1.8; margin:10px 0;">
            🗣️ <b>Speaking Practice</b>: 쉬운 단어와 문장을 따라 말하며 자신감을 길러요
        </p>
        <p style="font-size:23px; line-height:1.8; margin:10px 0;">
            🧰 <b>Class Tools</b>: 퀴즈, 듣기 활동, 반복 연습으로 즐겁게 영어를 배워요
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Learning Path
# ---------------------------
st.markdown(
    """
    <h2 style="
        color:#1f4e79;
        font-size:30px;
        margin-bottom:14px;
    ">
        🌈 Learning Path
    </h2>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f7fbff, #eaf3ff);
            border: 1.5px solid #d9e7ff;
            border-radius: 22px;
            padding: 24px;
            text-align:center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            min-height: 210px;
        ">
            <div style="font-size:42px;">🔤</div>
            <h3 style="color:#1f4e79; font-size:24px;">Step 1</h3>
            <p style="font-size:20px; line-height:1.6; color:#34495e;">
                알파벳과<br><b>기초 소리</b> 익히기
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #fffdf7, #fff3d9);
            border: 1.5px solid #ffe7b8;
            border-radius: 22px;
            padding: 24px;
            text-align:center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            min-height: 210px;
        ">
            <div style="font-size:42px;">🔊</div>
            <h3 style="color:#8a5a00; font-size:24px;">Step 2</h3>
            <p style="font-size:20px; line-height:1.6; color:#6b4e16;">
                단어와 문장을 듣고<br><b>의미 연결</b>하기
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #f7fff9, #e7f8ed);
            border: 1.5px solid #ccefd8;
            border-radius: 22px;
            padding: 24px;
            text-align:center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            min-height: 210px;
        ">
            <div style="font-size:42px;">🧩</div>
            <h3 style="color:#2f7d46; font-size:24px;">Step 3</h3>
            <p style="font-size:20px; line-height:1.6; color:#355f42;">
                쉬운 문장 구조를<br><b>반복 연습</b>하기
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Class Message
# ---------------------------
st.markdown(
    """
    <h2 style="
        color:#1f4e79;
        font-size:30px;
        margin-top:28px;
        margin-bottom:14px;
    ">
        🎯 Class Message
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #fffdf7, #fff3d9);
        border: 2px solid #ffe7b8;
        border-radius: 22px;
        padding: 26px 28px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    ">
        <p style="
            font-size:25px;
            font-weight:800;
            color:#8a5a00;
            margin:0;
            line-height:1.6;
        ">
            영어는 어려운 과목이 아니라,<br>
            더 큰 세상으로 나아가는 작은 첫걸음입니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
