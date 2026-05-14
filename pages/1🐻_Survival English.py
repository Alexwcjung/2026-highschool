import streamlit as st

st.set_page_config(
    page_title="Survival English",
    page_icon="🌍",
    layout="wide"
)

# =========================
# CSS Design
# =========================
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #f7fbff 0%, #ffffff 45%, #f7fff9 100%);
    }

    .hero-box {
        background: linear-gradient(135deg, #0f766e 0%, #14b8a6 45%, #22c55e 100%);
        padding: 42px 36px;
        border-radius: 28px;
        color: white;
        box-shadow: 0 10px 30px rgba(15, 118, 110, 0.25);
        margin-bottom: 28px;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 900;
        margin-bottom: 8px;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 20px;
        font-weight: 500;
        opacity: 0.95;
        line-height: 1.6;
    }

    .pill {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        color: white;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 700;
        margin-right: 8px;
        margin-top: 16px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 900;
        margin-top: 18px;
        margin-bottom: 8px;
        color: #0f172a;
    }

    .section-text {
        font-size: 17px;
        line-height: 1.8;
        color: #334155;
    }

    .card {
        background: white;
        padding: 24px 22px;
        border-radius: 24px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        border: 1px solid #e2e8f0;
        height: 100%;
    }

    .card-icon {
        font-size: 34px;
        margin-bottom: 8px;
    }

    .card-title {
        font-size: 21px;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 8px;
    }

    .card-text {
        font-size: 16px;
        line-height: 1.7;
        color: #475569;
    }

    .flow-box {
        background: #f8fafc;
        padding: 20px;
        border-radius: 22px;
        border-left: 7px solid #14b8a6;
        margin-bottom: 12px;
    }

    .flow-title {
        font-size: 20px;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 6px;
    }

    .flow-text {
        font-size: 16px;
        color: #475569;
        line-height: 1.7;
    }

    .message-box {
        background: linear-gradient(135deg, #ecfeff 0%, #f0fdf4 100%);
        padding: 28px;
        border-radius: 26px;
        border: 1px solid #99f6e4;
        box-shadow: 0 8px 20px rgba(20, 184, 166, 0.12);
        margin-top: 18px;
    }

    .message-title {
        font-size: 25px;
        font-weight: 900;
        color: #0f766e;
        margin-bottom: 10px;
    }

    .message-text {
        font-size: 18px;
        line-height: 1.8;
        color: #334155;
    }

    .small-note {
        font-size: 15px;
        color: #64748b;
        line-height: 1.7;
    }

    @media (max-width: 768px) {
        .hero-box {
            padding: 30px 22px;
            border-radius: 24px;
        }

        .hero-title {
            font-size: 34px;
        }

        .hero-subtitle {
            font-size: 17px;
        }

        .section-title {
            font-size: 24px;
        }

        .card {
            padding: 20px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Hero Section
# =========================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🌍 Survival English</div>
        <div class="hero-subtitle">
            영어가 어려운 학생도 괜찮습니다.<br>
            먼저 많이 듣고, 짧게 따라 말하고, 쉬운 표현부터 살아 있는 영어로 익힙니다.
        </div>
        <div>
            <span class="pill">🔊 Listening First</span>
            <span class="pill">🗣️ Speaking First</span>
            <span class="pill">🎵 Songs</span>
            <span class="pill">📖 Reading</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# Intro
# =========================
left, right = st.columns([1.2, 1])

with left:
    st.markdown('<div class="section-title">🌱 이 앱은 무엇을 위한 공간인가요?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-text">
        <b>Survival English</b>는 영어를 처음부터 어렵게 공부하는 앱이 아닙니다.<br>
        학생들이 실제 생활에서 쓸 수 있는 쉬운 단어와 문장을
        <b>듣고, 따라 말하고, 다시 확인하면서</b> 영어에 익숙해지는 공간입니다.
        <br><br>
        문법을 길게 설명하기보다, 먼저 영어 소리에 익숙해지고
        입으로 짧은 표현을 말해 보는 것을 중요하게 생각합니다.
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">🎯</div>
            <div class="card-title">핵심 목표</div>
            <div class="card-text">
                완벽한 영어보다 먼저 필요한 것은
                <b>두려움 없이 듣고 말해 보는 경험</b>입니다.
                <br><br>
                한 단어, 한 문장씩 천천히 익히며
                영어를 사용할 수 있다는 자신감을 기릅니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =========================
# Main Features
# =========================
st.markdown('<div class="section-title">🧭 Survival English의 핵심 활동</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">🔊</div>
            <div class="card-title">듣기</div>
            <div class="card-text">
                단어와 문장을 반복해서 들으며
                영어 소리와 리듬에 익숙해집니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">🗣️</div>
            <div class="card-title">말하기</div>
            <div class="card-text">
                들은 표현을 직접 따라 말하며
                영어를 입에 붙이는 연습을 합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">🎵</div>
            <div class="card-title">노래</div>
            <div class="card-text">
                익숙한 노래와 영상으로
                영어 표현을 더 재미있게 만납니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">📖</div>
            <div class="card-title">읽기</div>
            <div class="card-text">
                짧고 쉬운 글을 읽으며
                배운 단어와 문장을 다시 확인합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =========================
# Learning Flow
# =========================
st.markdown('<div class="section-title">🪄 학습 흐름</div>', unsafe_allow_html=True)

flow1, flow2, flow3 = st.columns(3)

with flow1:
    st.markdown(
        """
        <div class="flow-box">
            <div class="flow-title">1️⃣ 먼저 듣기</div>
            <div class="flow-text">
                영어 단어와 문장을 눈으로 보기 전에
                먼저 소리로 만나 봅니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with flow2:
    st.markdown(
        """
        <div class="flow-box">
            <div class="flow-title">2️⃣ 따라 말하기</div>
            <div class="flow-text">
                짧은 표현을 직접 말하면서
                발음과 문장 감각을 익힙니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with flow3:
    st.markdown(
        """
        <div class="flow-box">
            <div class="flow-title">3️⃣ 노래·읽기·퀴즈로 복습</div>
            <div class="flow-text">
                노래, 짧은 읽기, 간단한 퀴즈를 통해
                배운 표현을 다시 확인합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# Survival Message
# =========================
st.markdown(
    """
    <div class="message-box">
        <div class="message-title">💬 Survival Message</div>
        <div class="message-text">
            영어는 처음부터 완벽하게 말하는 것이 아닙니다.<br>
            쉬운 표현을 많이 듣고, 자주 따라 말하고,
            조금씩 사용할 수 있게 되는 것이 중요합니다.
            <br><br>
            <b>오늘도 한 단어, 한 문장씩.</b><br>
            듣고, 말하고, 다시 해 보면서 영어에 가까워져 봅시다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("")
st.caption("🌍 Survival English · Listening and Speaking First")
