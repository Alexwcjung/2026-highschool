import streamlit as st

st.set_page_config(
    page_title="Alex's Fun English",
    page_icon="🌈",
    layout="wide"
)

# ---------------------------
# CSS
# ---------------------------
st.markdown(
    """
    <style>
    .top-card {
        background: linear-gradient(135deg, #ffffff 0%, #eef6ff 50%, #fff7ed 100%);
        border: 1.5px solid #d9e7ff;
        border-radius: 34px;
        padding: 42px 34px;
        text-align: center;
        box-shadow: 0 12px 32px rgba(31,78,121,0.13);
        margin-bottom: 30px;
    }

    .course-pill {
        display: inline-block;
        background-color: #eaf3ff;
        color: #1f4e79;
        font-size: 16px;
        font-weight: 800;
        padding: 9px 20px;
        border-radius: 999px;
        margin-bottom: 18px;
        border: 1px solid #d9e7ff;
    }

    .main-title {
        color:#1f4e79;
        font-size: 48px;
        font-weight: 900;
        margin: 12px 0 10px 0;
    }

    .main-subtitle {
        color:#2f6f9f;
        font-size: 28px;
        font-weight: 800;
        margin: 0 0 22px 0;
    }

    .main-desc {
        font-size: 22px;
        line-height: 1.75;
        color: #34495e;
        margin: 0 auto;
        max-width: 900px;
    }

    .highlight {
        background: linear-gradient(transparent 58%, #fff1a8 58%);
        font-weight: 900;
        color: #1f4e79;
    }

    .abc-box {
        background: #ffffff;
        border: 1.5px solid #d9e7ff;
        border-radius: 16px;
        padding: 12px 0;
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        color: #1f4e79;
        box-shadow: 0 4px 10px rgba(31,78,121,0.08);
        margin-bottom: 8px;
    }

    .section-title {
        color:#1f4e79;
        font-size:32px;
        font-weight:900;
        margin: 28px 0 18px 0;
        text-align: center;
    }

    .path-card-blue {
        background: linear-gradient(135deg, #f7fbff, #eaf3ff);
        border: 1.5px solid #d9e7ff;
        border-radius: 28px;
        padding: 30px 24px;
        text-align:center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        min-height: 250px;
    }

    .path-card-yellow {
        background: linear-gradient(135deg, #fffdf7, #fff3d9);
        border: 1.5px solid #ffe7b8;
        border-radius: 28px;
        padding: 30px 24px;
        text-align:center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        min-height: 250px;
    }

    .path-card-green {
        background: linear-gradient(135deg, #f7fff9, #e7f8ed);
        border: 1.5px solid #ccefd8;
        border-radius: 28px;
        padding: 30px 24px;
        text-align:center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        min-height: 250px;
    }

    .path-step {
        display: inline-block;
        padding: 7px 16px;
        border-radius: 999px;
        background: white;
        font-size: 15px;
        font-weight: 900;
        margin-bottom: 14px;
        border: 1px solid rgba(0,0,0,0.06);
    }

    .path-icon {
        font-size: 50px;
        margin-bottom: 8px;
    }

    .path-title {
        font-size: 26px;
        font-weight: 900;
        margin-bottom: 10px;
    }

    .path-text {
        font-size: 20px;
        line-height: 1.65;
        color:#34495e;
    }

    .message-card {
        background: linear-gradient(135deg, #fff7ed, #fffdf7);
        border: 2px solid #ffe7b8;
        border-radius: 28px;
        padding: 30px 28px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        margin-top: 26px;
    }

    .message-main {
        font-size:27px;
        font-weight:900;
        color:#8a5a00;
        margin:0;
        line-height:1.65;
    }

    .mini-note {
        margin-top: 12px;
        font-size: 18px;
        color:#6b4e16;
        line-height:1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Alphabet Decoration
# ---------------------------
letters1 = ["A", "B", "C", "D", "E", "F", "G"]
letters2 = ["H", "I", "J", "K", "L", "M", "N"]

cols = st.columns(len(letters1))
for col, letter in zip(cols, letters1):
    with col:
        st.markdown(f"<div class='abc-box'>{letter}</div>", unsafe_allow_html=True)

cols = st.columns(len(letters2))
for col, letter in zip(cols, letters2):
    with col:
        st.markdown(f"<div class='abc-box'>{letter}</div>", unsafe_allow_html=True)

# ---------------------------
# Top Card
# ---------------------------
st.markdown(
    """
    <div class="top-card">
        <div style="font-size: 58px; margin-bottom: 10px;">
            🌱 🔤 🌈 ✨
        </div>

        <div class="course-pill">
            Fun English · Spring 2026
        </div>

        <h1 class="main-title">
            Alex의 영어교실
        </h1>

        <h2 class="main-subtitle">
            알파벳을 처음 읽는 순간부터 쉬운 영어 문장까지
        </h2>

        <p class="main-desc">
            이 앱은 <span class="highlight">알파벳을 처음 읽는 학습자</span>도 부담 없이 시작할 수 있도록 만든 
            기초 영어 학습 공간입니다.<br>
            알파벳 소리, 쉬운 단어, 기초 영어 듣기, 그리고 문장 구조를 
            <span class="highlight">차근차근 재미있게</span> 배울 수 있습니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

letters3 = ["O", "P", "Q", "R", "S", "T"]
letters4 = ["U", "V", "W", "X", "Y", "Z"]

cols = st.columns(len(letters3))
for col, letter in zip(cols, letters3):
    with col:
        st.markdown(f"<div class='abc-box'>{letter}</div>", unsafe_allow_html=True)

cols = st.columns(len(letters4))
for col, letter in zip(cols, letters4):
    with col:
        st.markdown(f"<div class='abc-box'>{letter}</div>", unsafe_allow_html=True)

# ---------------------------
# Learning Path
# ---------------------------
st.markdown("<div class='section-title'>🌈 Learning Path</div>", unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown(
        """
        <div class="path-card-blue">
            <div class="path-step">STEP 1</div>
            <div class="path-icon">🔤</div>
            <div class="path-title" style="color:#1f4e79;">Alphabet & Phonics</div>
            <div class="path-text">
                A B C부터 시작해<br>
                <b>글자와 소리</b>를 익혀요.<br><br>
                알파벳 이름과 실제 소리를<br>
                구분하며 읽기 기초를 배웁니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with p2:
    st.markdown(
        """
        <div class="path-card-yellow">
            <div class="path-step">STEP 2</div>
            <div class="path-icon">🔊</div>
            <div class="path-title" style="color:#8a5a00;">Words & Listening</div>
            <div class="path-text">
                쉬운 단어를 듣고<br>
                <b>뜻과 발음</b>을 연결해요.<br><br>
                자주 쓰는 단어를<br>
                테마별로 반복 학습합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with p3:
    st.markdown(
        """
        <div class="path-card-green">
            <div class="path-step">STEP 3</div>
            <div class="path-icon">🧩</div>
            <div class="path-title" style="color:#2f7d46;">Sentence Structure</div>
            <div class="path-text">
                단어를 문장으로 연결해<br>
                <b>기초 문장 구조</b>를 배워요.<br><br>
                be동사, 일반동사, 시제,<br>
                부정문을 쉽게 연습합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Class Message
# ---------------------------
st.markdown(
    """
    <div class="message-card">
        <p class="message-main">
            영어는 어려운 과목이 아니라,<br>
            더 큰 세상으로 나아가는 작은 첫걸음입니다.
        </p>
        <div class="mini-note">
            Alex의 영어교실에서 오늘도 한 글자, 한 단어, 한 문장씩 천천히 성장해 봅시다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
