import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="우리나라 역사 한눈에 보기",
    page_icon="🇰🇷",
    layout="wide"
)

# =====================================================
# 우리나라 역사 핵심 데이터
# =====================================================
PERIODS = [
    {
        "name": "선사 시대",
        "emoji": "🪨",
        "time": "문자가 사용되기 전",
        "years": "구석기 · 신석기 · 청동기",
        "summary": "사람들이 도구를 만들고 사냥, 채집, 농사를 시작하던 시기입니다.",
        "keywords": ["뗀석기", "간석기", "농경 시작", "고인돌"],
        "color": "#78716c",
        "easy": "문자가 없던 시기, 도구와 농사가 시작된 시대"
    },
    {
        "name": "고조선",
        "emoji": "🐻",
        "time": "기원전 2333년 전설적 건국",
        "years": "우리 역사상 첫 국가",
        "summary": "단군왕검이 세웠다고 전해지는 우리나라 최초의 국가입니다. 청동기 문화를 바탕으로 성장했습니다.",
        "keywords": ["단군왕검", "홍익인간", "청동기", "8조법"],
        "color": "#a16207",
        "easy": "우리나라 최초의 국가"
    },
    {
        "name": "삼국 시대",
        "emoji": "⚔️",
        "time": "기원전 1세기경 ~ 7세기",
        "years": "고구려 · 백제 · 신라",
        "summary": "고구려, 백제, 신라가 서로 경쟁하며 성장한 시대입니다. 각 나라는 독자적인 문화와 제도를 발전시켰습니다.",
        "keywords": ["고구려", "백제", "신라", "불교 수용"],
        "color": "#dc2626",
        "easy": "고구려·백제·신라가 경쟁한 시대"
    },
    {
        "name": "통일 신라와 발해",
        "emoji": "🌅",
        "time": "7세기 후반 ~ 10세기",
        "years": "남북국 시대",
        "summary": "신라가 삼국을 통일한 뒤 남쪽에는 통일 신라, 북쪽에는 고구려를 계승한 발해가 발전했습니다.",
        "keywords": ["통일 신라", "발해", "불국사", "석굴암"],
        "color": "#ea580c",
        "easy": "남쪽 통일 신라, 북쪽 발해가 있던 시대"
    },
    {
        "name": "고려",
        "emoji": "📜",
        "time": "918년 ~ 1392년",
        "years": "왕건 건국",
        "summary": "왕건이 세운 나라로, 불교 문화가 발달했고 세계적으로 뛰어난 금속활자와 팔만대장경을 남겼습니다.",
        "keywords": ["왕건", "불교", "팔만대장경", "금속활자"],
        "color": "#2563eb",
        "easy": "불교 문화와 금속활자가 발달한 나라"
    },
    {
        "name": "조선",
        "emoji": "👑",
        "time": "1392년 ~ 1897년",
        "years": "이성계 건국",
        "summary": "유교를 바탕으로 한 나라입니다. 세종대왕 때 훈민정음이 창제되었고, 과학과 문화도 크게 발전했습니다.",
        "keywords": ["이성계", "유교", "세종대왕", "훈민정음"],
        "color": "#16a34a",
        "easy": "훈민정음이 만들어진 유교 중심의 나라"
    },
    {
        "name": "대한제국",
        "emoji": "🦅",
        "time": "1897년 ~ 1910년",
        "years": "고종 황제",
        "summary": "조선이 나라 이름을 대한제국으로 바꾸고 근대 국가로 나아가려 했던 시기입니다.",
        "keywords": ["고종", "황제", "광무개혁", "근대화"],
        "color": "#9333ea",
        "easy": "근대 국가로 나아가려 했던 시기"
    },
    {
        "name": "일제 강점기",
        "emoji": "🕯️",
        "time": "1910년 ~ 1945년",
        "years": "독립운동의 시대",
        "summary": "일본의 지배를 받았지만, 수많은 사람들이 나라를 되찾기 위해 독립운동을 펼쳤습니다.",
        "keywords": ["3·1운동", "대한민국 임시정부", "독립운동", "광복"],
        "color": "#475569",
        "easy": "나라를 되찾기 위한 독립운동의 시대"
    },
    {
        "name": "대한민국",
        "emoji": "🇰🇷",
        "time": "1948년 ~ 현재",
        "years": "대한민국 정부 수립 이후",
        "summary": "1948년 대한민국 정부가 수립되었습니다. 전쟁과 어려움을 겪었지만 민주주의와 경제 발전을 이루어 왔습니다.",
        "keywords": ["정부 수립", "6·25 전쟁", "민주화", "경제 발전"],
        "color": "#0284c7",
        "easy": "민주주의와 경제 발전을 이루어 온 현재의 우리나라"
    },
]

EVENTS = [
    {"year": -2333, "label": "고조선 건국 전설", "period": "고조선", "display": "기원전 2333년"},
    {"year": 372, "label": "고구려 불교 수용", "period": "삼국 시대", "display": "372년"},
    {"year": 660, "label": "백제 멸망", "period": "삼국 시대", "display": "660년"},
    {"year": 668, "label": "고구려 멸망", "period": "삼국 시대", "display": "668년"},
    {"year": 698, "label": "발해 건국", "period": "통일 신라와 발해", "display": "698년"},
    {"year": 918, "label": "고려 건국", "period": "고려", "display": "918년"},
    {"year": 1236, "label": "팔만대장경 제작 시작", "period": "고려", "display": "1236년"},
    {"year": 1392, "label": "조선 건국", "period": "조선", "display": "1392년"},
    {"year": 1443, "label": "훈민정음 창제", "period": "조선", "display": "1443년"},
    {"year": 1592, "label": "임진왜란 시작", "period": "조선", "display": "1592년"},
    {"year": 1897, "label": "대한제국 선포", "period": "대한제국", "display": "1897년"},
    {"year": 1910, "label": "일제 강점기 시작", "period": "일제 강점기", "display": "1910년"},
    {"year": 1919, "label": "3·1운동", "period": "일제 강점기", "display": "1919년"},
    {"year": 1945, "label": "광복", "period": "대한민국", "display": "1945년"},
    {"year": 1948, "label": "대한민국 정부 수립", "period": "대한민국", "display": "1948년"},
    {"year": 1950, "label": "6·25 전쟁 시작", "period": "대한민국", "display": "1950년"},
    {"year": 1987, "label": "6월 민주항쟁", "period": "대한민국", "display": "1987년"},
]

# =====================================================
# 세션 상태
# =====================================================
if "quiz_item" not in st.session_state:
    st.session_state.quiz_item = random.choice(PERIODS)

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0


def next_question():
    st.session_state.quiz_item = random.choice(PERIODS)
    st.session_state.quiz_answered = False
    st.session_state.quiz_result = ""


def reset_score():
    st.session_state.score = 0
    st.session_state.total = 0
    next_question()


# =====================================================
# 스타일
# =====================================================
st.markdown(
    """
    <style>
    .title-box {
        background: linear-gradient(135deg, #eff6ff 0%, #ffffff 45%, #fee2e2 100%);
        border: 1.5px solid #bfdbfe;
        border-radius: 30px;
        padding: 28px 32px;
        margin-bottom: 20px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
    }
    .title-box h1 {
        margin: 0;
        font-size: 42px;
        font-weight: 900;
        color: #0f172a;
    }
    .title-box p {
        margin-top: 10px;
        font-size: 18px;
        color: #334155;
        font-weight: 750;
        line-height: 1.65;
    }
    .concept-box {
        background: linear-gradient(135deg, #fff7ed 0%, #fef3c7 100%);
        border: 1.5px solid #fed7aa;
        border-radius: 26px;
        padding: 22px 24px;
        margin-bottom: 18px;
        box-shadow: 0 5px 16px rgba(0,0,0,0.05);
    }
    .concept-box h2 {
        margin: 0 0 10px 0;
        font-size: 28px;
        color: #9a3412;
        font-weight: 900;
    }
    .concept-box p {
        margin: 0;
        font-size: 18px;
        line-height: 1.7;
        color: #334155;
        font-weight: 750;
    }
    .period-card {
        background: white;
        border: 1.5px solid #e2e8f0;
        border-radius: 24px;
        padding: 18px 20px;
        min-height: 315px;
        box-shadow: 0 5px 16px rgba(0,0,0,0.055);
        margin-bottom: 16px;
    }
    .period-card h3 {
        margin: 0 0 10px 0;
        font-size: 24px;
        font-weight: 900;
        color: #111827;
    }
    .period-card p {
        font-size: 15px;
        color: #334155;
        line-height: 1.65;
        font-weight: 650;
    }
    .tag {
        display: inline-block;
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        color: #334155;
        border-radius: 999px;
        padding: 5px 10px;
        margin: 3px;
        font-size: 13px;
        font-weight: 800;
    }
    .mini-box {
        background: #f8fafc;
        border: 1.5px solid #e2e8f0;
        border-radius: 20px;
        padding: 16px 18px;
        margin-bottom: 14px;
        color: #334155;
        font-weight: 750;
        line-height: 1.65;
    }
    .quiz-box {
        background: #eff6ff;
        border: 1.5px solid #bfdbfe;
        border-radius: 24px;
        padding: 20px;
        margin-top: 10px;
        margin-bottom: 16px;
        text-align: center;
        font-size: 24px;
        color: #1e3a8a;
        font-weight: 900;
    }
    @media (max-width: 768px) {
        .title-box {
            padding: 20px 18px;
            border-radius: 22px;
        }
        .title-box h1 {
            font-size: 30px;
        }
        .title-box p {
            font-size: 15px;
        }
        .concept-box h2 {
            font-size: 23px;
        }
        .concept-box p {
            font-size: 15px;
        }
        .period-card {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-box">
        <h1>🇰🇷 우리나라 역사 한눈에 보기</h1>
        <p>
            선사 시대부터 대한민국까지, 우리 역사의 큰 흐름을 쉽고 간단하게 정리해 봅시다.<br>
            핵심은 <b>나라의 변화, 문화의 발전, 독립과 민주주의의 과정</b>을 순서대로 이해하는 것입니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 탭 구성
# =====================================================
tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "📘 역사란?",
    "🕰️ 연표 보기",
    "🏛️ 시대 카드",
    "📌 한눈에 정리",
    "🎮 확인 퀴즈"
])

# =====================================================
# 탭 0 역사란?
# =====================================================
with tab0:
    st.markdown(
        """
        <div class="concept-box">
            <h2>📘 역사란 무엇일까요?</h2>
            <p>
                역사는 과거 사람들이 살아온 이야기입니다. 
                단순히 옛날 일을 외우는 것이 아니라, <b>사람들이 어떤 선택을 했고, 그 선택이 오늘날 우리 삶에 어떤 영향을 주었는지</b> 이해하는 공부입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="mini-box">
            <h3>🧭 시간의 흐름</h3>
            역사는 순서가 중요합니다.<br>
            어떤 일이 먼저 일어났고, 그 뒤에 어떤 변화가 생겼는지 살펴봅니다.
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="mini-box">
            <h3>👥 사람들의 삶</h3>
            왕이나 전쟁만 보는 것이 아니라, 당시 사람들이 어떻게 먹고 살았는지도 살펴봅니다.
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="mini-box">
            <h3>🌱 오늘과 연결</h3>
            한글, 문화재, 민주주의, 독립운동처럼 오늘날 우리 삶과 연결되는 내용을 배웁니다.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 🧒 학생용 한 줄 정리")
    st.markdown(
        """
        <div class="mini-box">
        <b>역사 = 과거 사람들의 삶을 통해 오늘의 우리를 이해하는 공부</b>
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# 탭 1 연표 보기
# =====================================================
with tab1:
    st.markdown("### 🕰️ 우리나라 역사 주요 사건 연표")

    fig = go.Figure()

    colors = []
    for e in EVENTS:
        matched = next((p for p in PERIODS if p["name"] == e["period"]), None)
        colors.append(matched["color"] if matched else "#64748b")

    fig.add_trace(go.Scatter(
        x=[e["year"] for e in EVENTS],
        y=[1 for _ in EVENTS],
        mode="markers+text",
        marker=dict(
            size=18,
            color=colors,
            line=dict(width=2, color="white")
        ),
        text=[f"{e['display']}<br>{e['label']}" for e in EVENTS],
        textposition="top center",
        hovertext=[f"{e['display']}<br>{e['label']}<br>{e['period']}" for e in EVENTS],
        hoverinfo="text",
        name="주요 사건"
    ))

    fig.update_layout(
        height=420,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        xaxis=dict(
            title="연도",
            zeroline=True,
            zerolinecolor="#94a3b8",
            gridcolor="#e2e8f0"
        ),
        yaxis=dict(
            visible=False,
            range=[0.6, 1.6]
        ),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff"
    )

    st.plotly_chart(fig, use_container_width=True, config={"displaylogo": False})

    st.markdown(
        """
        <div class="mini-box">
        ✅ 연표는 역사를 <b>순서</b>로 이해하게 도와줍니다.<br>
        사건 하나하나를 따로 외우기보다, <b>어떤 나라가 먼저 있었고 어떤 변화가 이어졌는지</b> 흐름으로 보는 것이 중요합니다.
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# 탭 2 시대 카드
# =====================================================
with tab2:
    st.markdown("### 🏛️ 시대별 핵심 카드")

    cols = st.columns(3)

    for i, p in enumerate(PERIODS):
        with cols[i % 3]:
            tags = "".join([f"<span class='tag'>{kw}</span>" for kw in p["keywords"]])
            st.markdown(
                f"""
                <div class="period-card">
                    <h3>{p['emoji']} {p['name']}</h3>
                    <p><b>시기:</b> {p['time']}</p>
                    <p><b>핵심:</b> {p['years']}</p>
                    <p><b>설명:</b><br>{p['summary']}</p>
                    <div>{tags}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# 탭 3 한눈에 정리
# =====================================================
with tab3:
    st.markdown("### 📌 우리나라 역사 큰 흐름")

    rows = []
    for p in PERIODS:
        rows.append({
            "시대": p["name"],
            "시기": p["time"],
            "핵심": p["years"],
            "키워드": ", ".join(p["keywords"])
        })

    st.dataframe(rows, use_container_width=True, hide_index=True)

    st.markdown("### 🧠 흐름 암기 문장")
    st.markdown(
        """
        <div class="mini-box">
        <b>선사 시대</b>에는 도구와 농사가 시작되었고,<br>
        <b>고조선</b>은 우리나라 최초의 국가로 전해지며,<br>
        <b>삼국 시대</b>에는 고구려·백제·신라가 경쟁했습니다.<br>
        이후 <b>통일 신라와 발해</b>, <b>고려</b>, <b>조선</b>을 거쳐,<br>
        <b>대한제국</b>과 <b>일제 강점기</b>를 지나 오늘날 <b>대한민국</b>으로 이어졌습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🔑 아주 짧은 암기 공식")
    st.markdown(
        """
        <div class="mini-box">
        <b>선사 → 고조선 → 삼국 → 통일 신라·발해 → 고려 → 조선 → 대한제국 → 일제 강점기 → 대한민국</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 💬 수업 질문")
    st.markdown(
        """
        - 역사를 순서대로 배우는 이유는 무엇일까?
        - 우리나라 최초의 국가는 무엇이라고 배웠을까?
        - 조선 시대에 훈민정음이 만들어진 이유는 무엇일까?
        - 일제 강점기 사람들이 독립운동을 한 이유는 무엇일까?
        - 오늘날 대한민국과 연결되는 역사적 사건은 무엇일까?
        """
    )

# =====================================================
# 탭 4 확인 퀴즈
# =====================================================
with tab4:
    st.markdown("### 🎮 우리나라 역사 확인 퀴즈")

    score_col1, score_col2, score_col3 = st.columns(3)
    with score_col1:
        st.metric("점수", f"{st.session_state.score} / {st.session_state.total}")
    with score_col2:
        acc = 0
        if st.session_state.total > 0:
            acc = round(st.session_state.score / st.session_state.total * 100)
        st.metric("정답률", f"{acc}%")
    with score_col3:
        if st.button("🔄 점수 초기화", use_container_width=True):
            reset_score()
            st.rerun()

    quiz_modes = ["시대 설명 맞추기", "키워드 맞추기", "순서 맞추기"]
    quiz_mode = st.radio("퀴즈 유형", quiz_modes, horizontal=True)

    item = st.session_state.quiz_item

    if quiz_mode == "시대 설명 맞추기":
        question = f"다음 설명에 해당하는 시대는 무엇일까요?<br><br>“{item['easy']}”"
        correct_answer = item["name"]
        options = [p["name"] for p in PERIODS]
        options = random.sample(options, 4) if item["name"] in options else random.sample(options + [item["name"]], 4)
        if correct_answer not in options:
            options[0] = correct_answer

    elif quiz_mode == "키워드 맞추기":
        keyword = random.choice(item["keywords"])
        question = f"다음 키워드와 관련 깊은 시대는 무엇일까요?<br><br>“{keyword}”"
        correct_answer = item["name"]
        options = [p["name"] for p in PERIODS]
        options = random.sample(options, 4)
        if correct_answer not in options:
            options[0] = correct_answer

    else:
        question = "다음 중 우리나라 역사 흐름의 순서로 맞는 것은 무엇일까요?"
        correct_answer = "고조선 → 삼국 시대 → 고려 → 조선 → 대한민국"
        options = [
            "고조선 → 삼국 시대 → 고려 → 조선 → 대한민국",
            "조선 → 고조선 → 삼국 시대 → 고려 → 대한민국",
            "삼국 시대 → 고조선 → 조선 → 고려 → 대한민국",
            "대한민국 → 조선 → 고려 → 삼국 시대 → 고조선"
        ]

    st.markdown(
        f"""
        <div class="quiz-box">
            {question}
        </div>
        """,
        unsafe_allow_html=True
    )

    random.seed(item["name"] + quiz_mode + str(st.session_state.total))
    options = options[:]
    random.shuffle(options)

    opt_cols = st.columns(2)
    for i, option in enumerate(options):
        with opt_cols[i % 2]:
            if st.button(option, key=f"{quiz_mode}_{option}_{i}", use_container_width=True, disabled=st.session_state.quiz_answered):
                st.session_state.quiz_answered = True
                st.session_state.total += 1

                if option == correct_answer:
                    st.session_state.score += 1
                    st.session_state.quiz_result = f"✅ 정답입니다! {correct_answer}"
                else:
                    st.session_state.quiz_result = f"❌ 아쉬워요. 정답은 `{correct_answer}`입니다."

                st.rerun()

    if st.session_state.quiz_result:
        if st.session_state.quiz_result.startswith("✅"):
            st.success(st.session_state.quiz_result)
        else:
            st.error(st.session_state.quiz_result)

    if st.button("➡️ 다음 문제", use_container_width=True):
        next_question()
        st.rerun()

st.caption("필요 패키지: streamlit, plotly")
