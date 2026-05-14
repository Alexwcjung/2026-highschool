import streamlit as st

st.set_page_config(
    page_title="Survival English",
    page_icon="🌸",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #fff7fb 0%, #f8fffb 45%, #ffffff 100%);
    }

    .hero-box {
        background: linear-gradient(135deg, #0f766e 0%, #14b8a6 55%, #f9a8d4 100%);
        padding: 42px 34px;
        border-radius: 30px;
        color: white;
        box-shadow: 0 12px 32px rgba(15, 118, 110, 0.22);
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }

    .hero-box::after {
        content: "🌸";
        position: absolute;
        right: 28px;
        top: 18px;
        font-size: 88px;
        opacity: 0.22;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 900;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 20px;
        line-height: 1.6;
        font-weight: 500;
        opacity: 0.96;
    }

    .pill {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 15px;
        font-weight: 800;
        margin-right: 8px;
        margin-top: 18px;
    }

    .section-title {
        font-size: 27px;
        font-weight: 900;
        color: #0f172a;
        margin-top: 14px;
        margin-bottom: 14px;
    }

    .card {
        background: white;
        padding: 24px 22px;
        border-radius: 26px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.07);
        height: 100%;
    }

    .card-icon {
        font-size: 36px;
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

    .mini-box {
        background: linear-gradient(135deg, #ecfdf5 0%, #fff7fb 100%);
        padding: 22px;
        border-radius: 24px;
        border: 1px solid #bbf7d0;
        box-shadow: 0 8px 20px rgba(20, 184, 166, 0.1);
    }

    .mini-title {
        font-size: 22px;
        font-weight: 900;
        color: #0f766e;
        margin-bottom: 8px;
    }

    .mini-text {
        font-size: 17px;
        line-height: 1.8;
        color: #334155;
    }

    .flower-line {
        text-align: center;
        font-size: 25px;
        margin: 22px 0;
        opacity: 0.85;
    }

    @media (max-width: 768px) {
        .hero-box {
            padding: 32px 22px;
            border-radius: 24px;
        }

        .hero-title {
            font-size: 35px;
        }

        .hero-subtitle {
            font-size: 17px;
        }

        .section-title {
            font-size: 23px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Hero
# =========================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🌍 Survival English</div>
        <div class="hero-subtitle">
            쉬운 영어를 먼저 듣고, 짧게 말하며 익히는 공간
        </div>
        <div>
            <span class="pill">🔊 듣기 먼저</span>
            <span class="pill">🗣️ 말하기 먼저</span>
            <span class="pill">🌱 쉬운 표현부터</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# Main Focus
# =========================
st.markdown('<div class="section-title">🌱 Survival English의 중심</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">🔊</div>
            <div class="card-title">듣기</div>
            <div class="card-text">
                단어와 문장을 반복해서 들으며 영어 소리에 익숙해집니다.
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
                들은 표현을 직접 따라 말하며 영어를 입에 붙입니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="card-icon">📖</div>
            <div class="card-title">읽기와 확인</div>
            <div class="card-text">
                짧은 글과 간단한 활동으로 배운 표현을 다시 확인합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="flower-line">🌸 🌿 🌸</div>', unsafe_allow_html=True)

# =========================
# Extra
# =========================
left, right = st.columns([1.1, 1])

with left:
    st.markdown(
        """
        <div class="mini-box">
            <div class="mini-title">🎵 노래도 함께</div>
            <div class="mini-text">
                영어 노래와 영상은 흥미를 높이기 위한 활동으로 활용합니다.
                익숙한 멜로디를 통해 표현을 더 자연스럽게 만날 수 있습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        """
        <div class="mini-box">
            <div class="mini-title">💬 오늘의 메시지</div>
            <div class="mini-text">
                완벽하지 않아도 괜찮습니다.<br>
                한 단어씩 듣고, 한 문장씩 말하면 됩니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.caption("🌸 Survival English · Listening and Speaking First")
