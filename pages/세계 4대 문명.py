import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="세계 4대 문명 학습",
    page_icon="🏺",
    layout="wide"
)

# =====================================================
# 세계 4대 문명 데이터
# =====================================================
CIVILIZATIONS = [
    {
        "name_ko": "메소포타미아 문명",
        "name_en": "Mesopotamian Civilization",
        "emoji": "🏺",
        "region": "티그리스강과 유프라테스강 사이",
        "river": "티그리스강 · 유프라테스강",
        "modern": "이라크 일대",
        "period": "기원전 약 3500년경",
        "lat": 33.3,
        "lon": 44.4,
        "color": "#f97316",
        "keywords": ["쐐기문자", "도시국가", "함무라비 법전", "지구라트"],
        "summary": "강 사이의 비옥한 땅에서 도시가 발달했고, 쐐기문자와 법전 등 인류 초기 문명의 중요한 특징이 나타났습니다.",
        "easy": "두 강 사이에서 시작된 문명입니다. 글자와 법, 도시가 발달했습니다."
    },
    {
        "name_ko": "이집트 문명",
        "name_en": "Egyptian Civilization",
        "emoji": "🔺",
        "region": "나일강 유역",
        "river": "나일강",
        "modern": "이집트 일대",
        "period": "기원전 약 3000년경",
        "lat": 26.8,
        "lon": 30.8,
        "color": "#eab308",
        "keywords": ["피라미드", "파라오", "상형문자", "미라"],
        "summary": "나일강의 규칙적인 범람을 바탕으로 농업이 발달했고, 강력한 왕권과 피라미드, 상형문자가 발달했습니다.",
        "easy": "나일강 주변에서 시작된 문명입니다. 피라미드와 파라오로 유명합니다."
    },
    {
        "name_ko": "인더스 문명",
        "name_en": "Indus Valley Civilization",
        "emoji": "🧱",
        "region": "인더스강 유역",
        "river": "인더스강",
        "modern": "파키스탄 · 인도 북서부 일대",
        "period": "기원전 약 2500년경",
        "lat": 27.3,
        "lon": 68.1,
        "color": "#22c55e",
        "keywords": ["하라파", "모헨조다로", "계획도시", "배수시설"],
        "summary": "인더스강 주변에서 발달했으며, 하라파와 모헨조다로 같은 계획도시와 뛰어난 배수시설이 특징입니다.",
        "easy": "인더스강 주변에서 시작된 문명입니다. 도시 설계와 배수시설이 발달했습니다."
    },
    {
        "name_ko": "중국 문명",
        "name_en": "Chinese Civilization",
        "emoji": "🐉",
        "region": "황허강 유역",
        "river": "황허강",
        "modern": "중국 북부 일대",
        "period": "기원전 약 2000년경",
        "lat": 35.0,
        "lon": 110.0,
        "color": "#ef4444",
        "keywords": ["황허", "갑골문", "은나라", "청동기"],
        "summary": "황허강 유역에서 발달했으며, 갑골문과 청동기 문화, 초기 왕조 국가의 형성이 특징입니다.",
        "easy": "황허강 주변에서 시작된 문명입니다. 갑골문과 청동기 문화가 발달했습니다."
    },
]

RIVERS = [
    {"name": "티그리스강\nTigris", "lat": 33.5, "lon": 44.0},
    {"name": "유프라테스강\nEuphrates", "lat": 34.5, "lon": 41.5},
    {"name": "나일강\nNile", "lat": 23.5, "lon": 31.0},
    {"name": "인더스강\nIndus", "lat": 28.5, "lon": 69.0},
    {"name": "황허강\nYellow River", "lat": 35.5, "lon": 110.0},
]

# =====================================================
# 세션 상태
# =====================================================
if "quiz_item" not in st.session_state:
    st.session_state.quiz_item = random.choice(CIVILIZATIONS)

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0


def next_question():
    st.session_state.quiz_item = random.choice(CIVILIZATIONS)
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
        background: linear-gradient(135deg, #fff7ed 0%, #fef3c7 45%, #fee2e2 100%);
        border: 1.5px solid #fed7aa;
        border-radius: 28px;
        padding: 26px 30px;
        margin-bottom: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.07);
    }
    .title-box h1 {
        margin: 0;
        font-size: 40px;
        font-weight: 900;
        color: #0f172a;
    }
    .title-box p {
        margin-top: 10px;
        font-size: 18px;
        color: #334155;
        font-weight: 700;
        line-height: 1.6;
    }
    .civil-card {
        background: white;
        border: 1.5px solid #e2e8f0;
        border-radius: 24px;
        padding: 18px 20px;
        min-height: 290px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin-bottom: 14px;
    }
    .civil-card h3 {
        margin: 0 0 10px 0;
        font-size: 23px;
        font-weight: 900;
        color: #111827;
    }
    .civil-card p {
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
        border-radius: 18px;
        padding: 15px 18px;
        margin-bottom: 12px;
        color: #334155;
        font-weight: 750;
        line-height: 1.6;
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
            font-size: 29px;
        }
        .title-box p {
            font-size: 15px;
        }
        .civil-card {
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
        <h1>🏺 세계 4대 문명 학습 자료</h1>
        <p>
            메소포타미아, 이집트, 인더스, 중국 문명을 지도와 카드로 익혀 봅시다.<br>
            핵심은 <b>큰 강 주변에서 농업과 도시가 발달했다</b>는 점입니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 탭 구성
# =====================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "🗺️ 지도 보기",
    "🏺 문명 카드",
    "🕰️ 비교 정리",
    "🎮 확인 퀴즈"
])

# =====================================================
# 탭 1 지도 보기
# =====================================================
with tab1:
    st.markdown("### 🗺️ 4대 문명은 어디에서 시작되었을까요?")

    col1, col2, col3 = st.columns(3)
    with col1:
        show_civ = st.checkbox("문명 위치 보기", value=True)
    with col2:
        show_rivers = st.checkbox("강 이름 보기", value=True)
    with col3:
        show_label = st.checkbox("문명 설명 보기", value=True)

    fig = go.Figure()

    if show_civ:
        fig.add_trace(go.Scattergeo(
            lon=[c["lon"] for c in CIVILIZATIONS],
            lat=[c["lat"] for c in CIVILIZATIONS],
            mode="markers+text",
            marker=dict(
                size=28,
                color=[c["color"] for c in CIVILIZATIONS],
                line=dict(width=2, color="white"),
                opacity=0.9
            ),
            text=[f"{c['emoji']} {c['name_ko']}" for c in CIVILIZATIONS],
            textposition="top center",
            textfont=dict(size=15, color="#111827"),
            hovertext=[
                f"{c['name_ko']}<br>{c['name_en']}<br>강: {c['river']}<br>현재 위치: {c['modern']}<br>{c['period']}"
                for c in CIVILIZATIONS
            ],
            hoverinfo="text",
            name="4대 문명"
        ))

    if show_rivers:
        fig.add_trace(go.Scattergeo(
            lon=[r["lon"] for r in RIVERS],
            lat=[r["lat"] for r in RIVERS],
            mode="markers+text",
            marker=dict(size=6, color="#2563eb", opacity=0.75),
            text=[r["name"] for r in RIVERS],
            textfont=dict(size=12, color="#1d4ed8"),
            textposition="bottom center",
            hoverinfo="skip",
            name="주요 강"
        ))

    fig.update_layout(
        height=640,
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.01,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255,255,255,0.8)"
        ),
        geo=dict(
            projection_type="natural earth",
            showland=True,
            landcolor="#f8fafc",
            showocean=True,
            oceancolor="#dbeafe",
            showcountries=True,
            countrycolor="#94a3b8",
            coastlinecolor="#475569",
            showcoastlines=True,
            showframe=False,
            lataxis=dict(showgrid=True, gridcolor="#e2e8f0"),
            lonaxis=dict(showgrid=True, gridcolor="#e2e8f0"),
            center=dict(lat=25, lon=60),
            projection_scale=1.25
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"scrollZoom": True, "displaylogo": False}
    )

    if show_label:
        st.markdown(
            """
            <div class="mini-box">
            ✅ 4대 문명은 대부분 <b>큰 강 주변</b>에서 시작되었습니다.<br>
            강은 농사에 필요한 물을 제공했고, 사람들은 강 주변에 모여 마을과 도시를 만들었습니다.<br>
            그래서 문명을 배울 때는 항상 <b>문명 이름 + 강 이름 + 현재 위치</b>를 함께 외우면 좋습니다.
            </div>
            """,
            unsafe_allow_html=True
        )

# =====================================================
# 탭 2 문명 카드
# =====================================================
with tab2:
    st.markdown("### 🏺 문명별 핵심 카드")

    cols = st.columns(2)

    for i, c in enumerate(CIVILIZATIONS):
        with cols[i % 2]:
            tags = "".join([f"<span class='tag'>{kw}</span>" for kw in c["keywords"]])
            st.markdown(
                f"""
                <div class="civil-card">
                    <h3>{c['emoji']} {c['name_ko']}</h3>
                    <p><b>영어 이름:</b> {c['name_en']}</p>
                    <p><b>위치:</b> {c['region']}</p>
                    <p><b>현재 지역:</b> {c['modern']}</p>
                    <p><b>시기:</b> {c['period']}</p>
                    <p><b>핵심 설명:</b><br>{c['summary']}</p>
                    <div>{tags}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# 탭 3 비교 정리
# =====================================================
with tab3:
    st.markdown("### 🕰️ 한눈에 비교하기")

    rows = []
    for c in CIVILIZATIONS:
        rows.append({
            "문명": c["name_ko"],
            "강": c["river"],
            "현재 지역": c["modern"],
            "시기": c["period"],
            "핵심 키워드": ", ".join(c["keywords"])
        })

    st.dataframe(rows, use_container_width=True, hide_index=True)

    st.markdown("### 📌 학생용 암기 문장")
    st.markdown(
        """
        <div class="mini-box">
        1. <b>메소포타미아 문명</b>은 티그리스강과 유프라테스강 사이에서 발달했다.<br>
        2. <b>이집트 문명</b>은 나일강 주변에서 발달했다.<br>
        3. <b>인더스 문명</b>은 인더스강 주변에서 발달했다.<br>
        4. <b>중국 문명</b>은 황허강 주변에서 발달했다.<br><br>
        ➜ 세계 4대 문명의 공통점: <b>큰 강 주변에서 농업과 도시가 발달했다.</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧠 수업 질문")
    st.markdown(
        """
        - 왜 옛날 사람들은 강 주변에 모여 살았을까?
        - 강이 농업에 어떤 도움을 주었을까?
        - 문명이 생기려면 어떤 조건이 필요할까?
        - 오늘날에도 큰 강 주변에 큰 도시가 많을까?
        """
    )

# =====================================================
# 탭 4 확인 퀴즈
# =====================================================
with tab4:
    st.markdown("### 🎮 세계 4대 문명 확인 퀴즈")

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

    quiz_modes = ["강 이름 맞추기", "문명 이름 맞추기", "현재 지역 맞추기"]
    quiz_mode = st.radio("퀴즈 유형", quiz_modes, horizontal=True)

    item = st.session_state.quiz_item

    if quiz_mode == "강 이름 맞추기":
        question = f"{item['emoji']} {item['name_ko']}은/는 어떤 강 주변에서 발달했을까요?"
        correct_answer = item["river"]
        options = [c["river"] for c in CIVILIZATIONS]

    elif quiz_mode == "문명 이름 맞추기":
        question = f"'{item['river']}' 주변에서 발달한 문명은 무엇일까요?"
        correct_answer = item["name_ko"]
        options = [c["name_ko"] for c in CIVILIZATIONS]

    else:
        question = f"{item['emoji']} {item['name_ko']}의 현재 지역은 어디일까요?"
        correct_answer = item["modern"]
        options = [c["modern"] for c in CIVILIZATIONS]

    st.markdown(
        f"""
        <div class="quiz-box">
            {question}
        </div>
        """,
        unsafe_allow_html=True
    )

    random.seed(item["name_ko"] + quiz_mode)
    options = options[:]
    random.shuffle(options)

    opt_cols = st.columns(2)
    for i, option in enumerate(options):
        with opt_cols[i % 2]:
            if st.button(option, key=f"{quiz_mode}_{option}", use_container_width=True, disabled=st.session_state.quiz_answered):
                st.session_state.quiz_answered = True
                st.session_state.total += 1

                if option == correct_answer:
                    st.session_state.score += 1
                    st.session_state.quiz_result = f"✅ 정답입니다! {item['name_ko']} — {item['easy']}"
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
