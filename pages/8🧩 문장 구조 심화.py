
import streamlit as st

st.set_page_config(page_title="기초 문법 확장", page_icon="🌟", layout="centered")

# =========================================================
# 전체 디자인 CSS
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #fffdfc;
    }

    .title-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #fff7ed 50%, #f7fee7 100%);
        padding: 34px 30px;
        border-radius: 32px;
        margin-bottom: 28px;
        box-shadow: 0 10px 26px rgba(80, 80, 120, 0.12);
        text-align: center;
        border: 1.5px solid #e0f2fe;
    }

    .title-box h1 {
        color: #334155;
        margin-bottom: 10px;
        font-size: 38px;
        font-weight: 900;
    }

    .title-box p {
        color: #64748b;
        font-size: 19px;
        margin: 0;
        line-height: 1.7;
    }

    .grammar-card {
        border-radius: 30px;
        padding: 28px 30px;
        margin: 20px 0 26px 0;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        border: 1.5px solid rgba(255,255,255,0.9);
    }

    .grammar-card h3 {
        margin-top: 0;
        font-size: 27px;
        font-weight: 900;
    }

    .grammar-card p {
        font-size: 21px;
        line-height: 1.85;
        color: #374151;
    }

    .formula-box {
        background: rgba(255,255,255,0.85);
        padding: 18px 20px;
        border-radius: 22px;
        font-size: 27px;
        font-weight: 900;
        text-align: center;
        margin-top: 16px;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.9);
    }

    .example-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
        padding: 20px 22px;
        border-radius: 22px;
        margin: 16px 0;
        box-shadow: 0 5px 14px rgba(0,0,0,0.055);
        font-size: 20px;
        line-height: 1.85;
        border: 1.5px solid #e8f0ff;
        color: #334155;
    }

    .example-box b {
        color: #2563eb;
    }

    .mini-card {
        background: linear-gradient(135deg, #ffffff 0%, #fbfdff 100%);
        border-radius: 24px;
        padding: 22px 24px;
        margin: 14px 0;
        box-shadow: 0 5px 16px rgba(0,0,0,0.055);
        border: 1.5px solid #edf2ff;
    }

    .mini-card h4 {
        margin-top: 0;
        color: #2563eb;
        font-size: 22px;
        font-weight: 900;
    }

    .mini-card p {
        font-size: 20px;
        line-height: 1.75;
        color: #374151;
    }

    .word-chip {
        display: inline-block;
        background: linear-gradient(135deg, #eef6ff, #ffffff);
        border: 1.5px solid #cfe2ff;
        border-radius: 999px;
        padding: 9px 16px;
        margin: 6px;
        font-size: 18px;
        font-weight: 800;
        color: #1f4e79;
        box-shadow: 0 3px 8px rgba(31,78,121,0.08);
    }

    button[data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 800;
    }

    div[data-testid="stAlert"] {
        border-radius: 18px;
        font-size: 18px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        padding: 0.45rem 1.1rem;
        border: 1.5px solid #d9e7ff;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        color: #2563eb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 상단 제목
# =========================================================
st.markdown(
    """
    <div class="title-box">
        <h1>🌟 기초 문법 확장</h1>
        <p>can, 명령문, There is / are, 전치사, 비교급을 차근차근 익혀 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

tabs = st.tabs([
    "💪 can 조동사",
    "📢 명령문",
    "📍 There is / are",
    "🧭 전치사",
    "⚖️ 비교급"
])


# =========================================================
# Tab 1: can 조동사
# =========================================================
with tabs[0]:
    st.subheader("💪 can 조동사")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#eef6ff,#ffffff);">
            <h3 style="color:#1d4ed8;">💪 can이란?</h3>
            <p>
                <b>can</b>은 <b>‘~할 수 있다’</b>라는 뜻입니다.
            </p>
            <p>
                내가 할 수 있는 일, 친구가 할 수 있는 일, 가능한 일을 말할 때 씁니다.
            </p>
            <div class="formula-box" style="color:#1d4ed8;">
                can + 동사원형
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 1. can으로 말하기")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>can 뒤에는 동사의 기본 모양</b>을 씁니다.</p>
            <p>can swims ❌ / can swim ✅</p>
        </div>

        <div class="example-box">
            I <b>can swim</b>.<br>
            → 나는 수영할 수 있다.
        </div>

        <div class="example-box">
            She <b>can sing</b>.<br>
            → 그녀는 노래할 수 있다.
        </div>

        <div class="example-box">
            They <b>can play</b> soccer.<br>
            → 그들은 축구를 할 수 있다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 2. can의 부정문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>cannot / can't + 동사원형</b></p>
            <p><b>cannot</b>은 <b>~할 수 없다</b>라는 뜻입니다.</p>
        </div>

        <div class="example-box">
            I <b>cannot swim</b>.<br>
            → 나는 수영할 수 없다.
        </div>

        <div class="example-box">
            He <b>can't speak</b> English.<br>
            → 그는 영어를 말할 수 없다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 3. can의 의문문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>Can + 주어 + 동사원형 ~ ?</b></p>
            <p>질문할 때는 <b>Can</b>을 문장 앞으로 보냅니다.</p>
        </div>

        <div class="example-box">
            You can swim.<br>
            ↓<br>
            <b>Can you swim?</b><br>
            → 너는 수영할 수 있니?
        </div>

        <div class="example-box">
            She can play the piano.<br>
            ↓<br>
            <b>Can she play</b> the piano?<br>
            → 그녀는 피아노를 칠 수 있니?
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: can 뒤에는 항상 동사원형을 씁니다. 예: can plays ❌ / can play ✅")


# =========================================================
# Tab 2: 명령문
# =========================================================
with tabs[1]:
    st.subheader("📢 명령문")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fff7ed,#ffffff);">
            <h3 style="color:#c2410c;">📢 명령문이란?</h3>
            <p>
                <b>명령문</b>은 상대방에게 <b>무엇을 하라고 말하는 문장</b>입니다.
            </p>
            <p>
                교실 영어, 안내문, 규칙을 말할 때 자주 씁니다.
            </p>
            <div class="formula-box" style="color:#c2410c;">
                동사원형으로 시작
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 1. 긍정 명령문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>동사원형 ~.</b></p>
            <p>주어 You를 쓰지 않고, 바로 동사로 시작합니다.</p>
        </div>

        <div class="example-box">
            <b>Open</b> the door.<br>
            → 문을 열어라.
        </div>

        <div class="example-box">
            <b>Listen</b> carefully.<br>
            → 주의 깊게 들어라.
        </div>

        <div class="example-box">
            <b>Stand</b> up.<br>
            → 일어서라.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 2. 부정 명령문")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>Don't + 동사원형 ~.</b></p>
            <p><b>~하지 마라</b>라고 말할 때 씁니다.</p>
        </div>

        <div class="example-box">
            <b>Don't run</b> in the classroom.<br>
            → 교실에서 뛰지 마라.
        </div>

        <div class="example-box">
            <b>Don't touch</b> this.<br>
            → 이것을 만지지 마라.
        </div>

        <div class="example-box">
            <b>Don't be</b> late.<br>
            → 늦지 마라.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: 명령문은 보통 주어 You를 생략하고 동사원형으로 시작합니다.")


# =========================================================
# Tab 3: There is / There are
# =========================================================
with tabs[2]:
    st.subheader("📍 There is / There are")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#ecfdf5,#ffffff);">
            <h3 style="color:#047857;">📍 There is / There are란?</h3>
            <p>
                <b>There is / There are</b>는 <b>‘~이 있다’</b>라는 뜻입니다.
            </p>
            <p>
                사람이나 물건이 어디에 있는지 말할 때 자주 씁니다.
            </p>
            <div class="formula-box" style="color:#047857;">
                There is + 1개 / There are + 2개 이상
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 1. There is")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>There is + 하나</b></p>
            <p>한 사람 또는 한 물건이 있을 때 씁니다.</p>
        </div>

        <div class="example-box">
            <b>There is</b> a book on the desk.<br>
            → 책상 위에 책 한 권이 있다.
        </div>

        <div class="example-box">
            <b>There is</b> a student in the classroom.<br>
            → 교실에 학생 한 명이 있다.
        </div>

        <div class="example-box">
            <b>There is</b> a dog under the table.<br>
            → 탁자 아래에 개 한 마리가 있다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 2. There are")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>There are + 두 개 이상</b></p>
            <p>사람이나 물건이 2개 이상 있을 때 씁니다.</p>
        </div>

        <div class="example-box">
            <b>There are</b> two books on the desk.<br>
            → 책상 위에 책 두 권이 있다.
        </div>

        <div class="example-box">
            <b>There are</b> three students in the classroom.<br>
            → 교실에 학생 세 명이 있다.
        </div>

        <div class="example-box">
            <b>There are</b> many cars on the street.<br>
            → 거리에 많은 자동차들이 있다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: 하나면 There is, 두 개 이상이면 There are를 씁니다.")


# =========================================================
# Tab 4: 전치사
# =========================================================
with tabs[3]:
    st.subheader("🧭 전치사")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#f5f3ff,#ffffff);">
            <h3 style="color:#6d28d9;">🧭 전치사란?</h3>
            <p>
                <b>전치사</b>는 사람이나 물건의 <b>위치, 방향, 시간</b> 등을 알려주는 말입니다.
            </p>
            <p>
                기초 단계에서는 먼저 <b>위치 전치사</b>를 익히면 좋습니다.
            </p>
            <div class="formula-box" style="color:#6d28d9;">
                in / on / under / next to / behind / in front of
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 자주 쓰는 위치 전치사")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>in</b> = ~안에</p>
            <p><b>on</b> = ~위에</p>
            <p><b>under</b> = ~아래에</p>
            <p><b>next to</b> = ~옆에</p>
            <p><b>behind</b> = ~뒤에</p>
            <p><b>in front of</b> = ~앞에</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 예문으로 익히기")

    st.markdown(
        """
        <div class="example-box">
            The cat is <b>in</b> the box.<br>
            → 고양이는 상자 안에 있다.
        </div>

        <div class="example-box">
            The book is <b>on</b> the desk.<br>
            → 책은 책상 위에 있다.
        </div>

        <div class="example-box">
            The ball is <b>under</b> the chair.<br>
            → 공은 의자 아래에 있다.
        </div>

        <div class="example-box">
            The school is <b>next to</b> the park.<br>
            → 학교는 공원 옆에 있다.
        </div>

        <div class="example-box">
            The dog is <b>behind</b> the door.<br>
            → 개는 문 뒤에 있다.
        </div>

        <div class="example-box">
            The bus stop is <b>in front of</b> the school.<br>
            → 버스 정류장은 학교 앞에 있다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: 전치사는 그림이나 교실 물건을 보면서 연습하면 훨씬 쉽게 익힐 수 있습니다.")


# =========================================================
# Tab 5: 비교급
# =========================================================
with tabs[4]:
    st.subheader("⚖️ 비교급")

    st.markdown(
        """
        <div class="grammar-card" style="background:linear-gradient(135deg,#fff1f2,#ffffff);">
            <h3 style="color:#be123c;">⚖️ 비교급이란?</h3>
            <p>
                <b>비교급</b>은 두 사람이나 두 물건을 비교할 때 씁니다.
            </p>
            <p>
                <b>더 크다, 더 빠르다, 더 쉽다</b>처럼 차이를 말할 수 있습니다.
            </p>
            <div class="formula-box" style="color:#be123c;">
                비교급 + than
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 1. 짧은 형용사: -er 붙이기")

    st.markdown(
        """
        <div class="mini-card">
            <p>짧은 형용사는 보통 뒤에 <b>-er</b>을 붙입니다.</p>
            <p>tall → taller / fast → faster / small → smaller</p>
        </div>

        <div class="example-box">
            Tom is <b>taller than</b> Mina.<br>
            → Tom은 Mina보다 키가 더 크다.
        </div>

        <div class="example-box">
            This car is <b>faster than</b> that car.<br>
            → 이 차는 저 차보다 더 빠르다.
        </div>

        <div class="example-box">
            My bag is <b>smaller than</b> your bag.<br>
            → 내 가방은 네 가방보다 더 작다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 2. 긴 형용사: more 붙이기")

    st.markdown(
        """
        <div class="mini-card">
            <p>긴 형용사는 앞에 <b>more</b>를 붙이는 경우가 많습니다.</p>
            <p>beautiful → more beautiful / interesting → more interesting</p>
        </div>

        <div class="example-box">
            This book is <b>more interesting than</b> that book.<br>
            → 이 책은 저 책보다 더 재미있다.
        </div>

        <div class="example-box">
            This flower is <b>more beautiful than</b> that flower.<br>
            → 이 꽃은 저 꽃보다 더 아름답다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ✅ 3. 자주 쓰는 불규칙 비교급")

    st.markdown(
        """
        <div class="mini-card">
            <p><b>good → better</b> = 더 좋은</p>
            <p><b>bad → worse</b> = 더 나쁜</p>
            <p><b>many / much → more</b> = 더 많은</p>
        </div>

        <div class="example-box">
            This is <b>better than</b> that.<br>
            → 이것은 저것보다 더 좋다.
        </div>

        <div class="example-box">
            I have <b>more</b> books than you.<br>
            → 나는 너보다 책을 더 많이 가지고 있다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Tip: 비교할 때는 보통 than을 함께 씁니다. 예: taller than, faster than, more interesting than")
