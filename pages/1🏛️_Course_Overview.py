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
        padding: 46px 36px;
        text-align: center;
        box-shadow: 0 12px 32px rgba(31,78,121,0.13);
        margin-bottom: 34px;
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
        font-size: 50px;
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
        line-height: 1.78;
        color: #34495e;
        margin: 0 auto;
        max-width: 940px;
    }

    .highlight {
        background: linear-gradient(transparent 58%, #fff1a8 58%);
        font-weight: 900;
        color: #1f4e79;
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
            영어가 낯설고 자신 없는 학습자를 위한 첫걸음
        </h2>

        <p class="main-desc">
            영어에 자신감이 없으신가요?<br>
            영어만 생각하면 어렵고, 틀릴까 봐 말하기가 망설여지나요?<br><br>

            이 앱은 <span class="highlight">알파벳을 처음 읽는 학습자</span>부터 
            <span class="highlight">기초 영어 듣기와 문장 구조</span>를 다시 배우고 싶은 학습자까지 
            누구나 쉽게 시작할 수 있도록 만든 영어 학습 공간입니다.<br>

            한 글자, 한 단어, 한 문장씩 천천히 익히며 
            영어에 대한 부담을 줄이고 자신감을 키워 봅시다.
        </p>
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
