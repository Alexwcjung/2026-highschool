import streamlit as st

st.set_page_config(page_title="Alex's Fun English", page_icon="🌈", layout="wide")

# ---------------------------
# CSS
# ---------------------------
st.markdown(
    """
    <style>
    .top-card {
        background: linear-gradient(135deg, #ffffff 0%, #eef6ff 45%, #fff7ed 100%);
        border: 1.5px solid #d9e7ff;
        border-radius: 34px;
        padding: 46px 34px;
        text-align: center;
        box-shadow: 0 12px 32px rgba(31,78,121,0.13);
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
    }

    .abc-strip {
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }

    .abc-badge {
        width: 46px;
        height: 46px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
        font-weight: 900;
        color: #1f4e79;
        background: #ffffff;
        border: 1.5px solid #d9e7ff;
        box-shadow: 0 4px 10px rgba(31,78,121,0.08);
    }

    .abc-badge:nth-child(2n) {
        background: #fff3d9;
        color: #8a5a00;
        border-color: #ffe7b8;
    }

    .abc-badge:nth-child(3n) {
        background: #eafaf0;
        color: #2f7d46;
        border-color: #ccefd8;
    }

    .abc-badge:nth-child(4n) {
        background: #fce7f3;
        color: #be185d;
        border-color: #fbcfe8;
    }

    .course-pill {
        display: inline-block;
        background: linear-gradient(135deg, #eaf3ff, #ffffff);
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
        font-size: 50px;
        font-weight: 950;
        margin: 12px 0 8px 0;
        letter-spacing: -1px;
    }

    .main-subtitle {
        color:#2f6f9f;
        font-size: 29px;
        font-weight: 850;
        margin: 0 0 22px 0;
    }

    .main-desc {
        font-size: 22px;
        line-height: 1.78;
        color: #34495e;
        margin: 0 auto;
        max-width: 920px;
    }

    .highlight {
        background: linear-gradient(transparent 58%, #fff1a8 58%);
        font-weight: 900;
        color: #1f4e79;
    }

    .section-title {
        color:#1f4e79;
        font-size:31px;
        font-weight:900;
        margin: 30px 0 16px 0;
    }

    .activity-card {
        background:#ffffff;
        border: 1.5px solid #e4ebff;
        border-radius: 24px;
        padding: 24px 26px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        min-height: 185px;
        transition: transform 0.2s ease;
    }

    .activity-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 24px rgba(0,0,0,0.08);
    }

    .activity-icon {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .activity-title {
        font-size: 23px;
        font-weight: 900;
        color:#1f4e79;
        margin-bottom: 8px;
    }

    .activity-text {
        font-size: 18px;
        line-height: 1.65;
        color:#34495e;
    }

    .path-card-blue {
        background: linear-gradient(135deg, #f7fbff, #eaf3ff);
        border: 1.5px solid #d9e7ff;
        border-radius: 25px;
        padding: 26px;
        text-align:center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        min-height: 225px;
    }

    .path-card-yellow {
        background: linear-gradient(135deg, #fffdf7, #fff3d9);
        border: 1.5px solid #ffe7b8;
        border-radius: 25px;
        padding: 26px;
        text-align:center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        min-height: 225px;
    }

    .path-card-green {
        background: linear-gradient(135deg, #f7fff9, #e7f8ed);
        border: 1.5px solid #ccefd8;
        border-radius: 25px;
        padding: 26px;
        text-align:center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        min-height: 225px;
    }

    .path-step {
        display: inline-block;
        padding: 7px 16px;
        border-radius: 999px;
        background: white;
        font-size: 15px;
        font-weight: 900;
        margin-bottom: 12px;
        border: 1px solid rgba(0,0,0,0.06);
    }

    .path-icon {
        font-size: 46px;
        margin-bottom: 6px;
    }

    .path-title {
        font-size: 25px;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .path-text {
        font-size: 20px;
        line-height: 1.6;
        color:#34495e;
    }

    .message-card {
        background: linear-gradient(135deg, #fff7ed, #fffdf7);
        border: 2px solid #ffe7b8;
        border-radius: 28px;
        padding: 30px 28px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        margin-top: 8px;
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
# Top Card
# ---------------------------
st.markdown(
    """
    <div class="top-card">
        <div class="abc-strip">
            <div class="abc-badge">A</div>
            <div class="abc-badge">B</div>
            <div class="abc-badge">C</div>
            <div class="abc-badge">D</div>
            <div class="abc-badge">E</div>
            <div class="abc-badge">F</div>
            <div class="abc-badge">G</div>
            <div class="abc-badge">H</div>
            <div class="abc-badge">I</div>
            <div class="abc-badge">J</div>
            <div class="abc-badge">K</div>
            <div class="abc-badge">L</div>
            <div class="abc-badge">M</div>
        </div>

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

        <div class="abc-strip" style="margin-top: 28px;">
            <div class="abc-badge">N</div>
            <div class="abc-badge">O</div>
            <div class="abc-badge">P</div>
            <div class="abc-badge">Q</div>
            <div class="abc-badge">R</div>
            <div class="abc-badge">S</div>
            <div class="abc-badge">T</div>
            <div class="abc-badge">U</div>
            <div class="abc-badge">V</div>
            <div class="abc-badge">W</div>
            <div class="abc-badge">X</div>
            <div class="abc-badge">Y</div>
            <div class="abc-badge">Z</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Course Activities
# ---------------------------
st.markdown("<div class='section-title'>🧭 Course Activities</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="activity-card">
            <div class="activity-icon">🔤</div>
            <div class="activity-title">Alphabet & Phonics</div>
            <div class="activity-text">
                알파벳 이름과 실제 소리를 듣고, 영어 읽기의 첫걸음을 익혀요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="activity-card">
            <div class="activity-icon">🌱</div>
            <div class="activity-title">Word Practice</div>
            <div class="activity-text">
                자주 쓰는 쉬운 단어를 테마별로 배우고 반복해서 복습해요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="activity-card">
            <div class="activity-icon">🔊</div>
            <div class="activity-title">Listening Practice</div>
            <div class="activity-text">
                단어와 문장을 듣고, 소리와 의미를 자연스럽게 연결해요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(
        """
        <div class="activity-card">
            <div class="activity-icon">🧩</div>
            <div class="activity-title">Sentence Structure</div>
            <div class="activity-text">
                be동사, 일반동사, 시제, 부정문을 쉬운 문제로 연습해요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        """
        <div class="activity-card">
            <div class="activity-icon">🗣️</div>
            <div class="activity-title">Speaking Practice</div>
            <div class="activity-text">
                쉬운 단어와 문장을 따라 말하며 영어 말하기 자신감을 길러요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col6:
    st.markdown(
        """
        <div class="activity-card">
            <div class="activity-icon">🎮</div>
            <div class="activity-title">Fun Review</div>
            <div class="activity-text">
                퀴즈와 반복 연습으로 영어를 게임처럼 즐겁게 복습해요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
            <div class="path-title" style="color:#1f4e79;">Alphabet</div>
            <div class="path-text">
                A B C부터 시작해<br>
                <b>글자와 소리</b>를 익혀요.
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
                <b>뜻과 발음</b>을 연결해요.
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
            <div class="path-title" style="color:#2f7d46;">Sentences</div>
            <div class="path-text">
                단어를 문장으로 연결해<br>
                <b>기초 문장 구조</b>를 배워요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
# Class Message
# ---------------------------
st.markdown("<div class='section-title'>🎯 Class Message</div>", unsafe_allow_html=True)

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
