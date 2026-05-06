import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="우리나라 역사와 근현대사",
    page_icon="🇰🇷",
    layout="wide"
)

# =====================================================
# 역사 큰 흐름
# =====================================================
HISTORY_FLOW = [
    {
        "name": "선사",
        "emoji": "🪨",
        "period": "문자 이전",
        "one": "도구와 농사가 시작됨",
        "keywords": ["뗀석기", "간석기", "농경", "고인돌"],
        "color": "#78716c"
    },
    {
        "name": "고조선",
        "emoji": "🐻",
        "period": "첫 국가",
        "one": "우리나라 최초의 국가",
        "keywords": ["단군왕검", "홍익인간", "청동기", "8조법"],
        "color": "#a16207"
    },
    {
        "name": "삼국",
        "emoji": "⚔️",
        "period": "고구려·백제·신라",
        "one": "세 나라가 경쟁하며 성장",
        "keywords": ["고구려", "백제", "신라", "불교"],
        "color": "#dc2626"
    },
    {
        "name": "남북국",
        "emoji": "🌅",
        "period": "통일 신라·발해",
        "one": "남쪽 통일 신라, 북쪽 발해",
        "keywords": ["통일 신라", "발해", "불국사", "석굴암"],
        "color": "#ea580c"
    },
    {
        "name": "고려",
        "emoji": "📜",
        "period": "918~1392",
        "one": "불교 문화와 금속활자",
        "keywords": ["왕건", "불교", "팔만대장경", "금속활자"],
        "color": "#2563eb"
    },
    {
        "name": "조선",
        "emoji": "👑",
        "period": "1392~1897",
        "one": "유교 정치와 훈민정음",
        "keywords": ["이성계", "유교", "세종대왕", "훈민정음"],
        "color": "#16a34a"
    },
    {
        "name": "근현대",
        "emoji": "🇰🇷",
        "period": "개항 이후~현재",
        "one": "독립, 전쟁, 산업화, 민주화",
        "keywords": ["개항", "독립운동", "대한민국", "민주화"],
        "color": "#0284c7"
    },
]

MODERN_STEPS = [
    {
        "title": "개항",
        "period": "1876년 이후",
        "emoji": "🚢",
        "summary": "강화도 조약 이후 조선은 외국과 본격적으로 관계를 맺기 시작했습니다.",
        "keywords": ["강화도 조약", "개항", "근대 문물"],
        "color": "#0ea5e9"
    },
    {
        "title": "대한제국",
        "period": "1897~1910",
        "emoji": "🦅",
        "summary": "고종은 대한제국을 선포하고 근대 국가로 나아가기 위한 개혁을 추진했습니다.",
        "keywords": ["고종", "황제", "광무개혁"],
        "color": "#9333ea"
    },
    {
        "title": "일제 강점기",
        "period": "1910~1945",
        "emoji": "🕯️",
        "summary": "일본의 식민 지배를 받았지만, 국내외에서 독립운동이 이어졌습니다.",
        "keywords": ["3·1운동", "대한민국 임시정부", "독립운동"],
        "color": "#475569"
    },
    {
        "title": "광복과 정부 수립",
        "period": "1945~1948",
        "emoji": "🌅",
        "summary": "1945년 광복을 맞았고, 1948년 대한민국 정부가 수립되었습니다.",
        "keywords": ["광복", "정부 수립", "분단"],
        "color": "#f59e0b"
    },
    {
        "title": "6·25 전쟁",
        "period": "1950~1953",
        "emoji": "🪖",
        "summary": "전쟁으로 큰 피해를 입었고, 휴전 이후 남북 분단이 계속되었습니다.",
        "keywords": ["6·25 전쟁", "휴전", "분단"],
        "color": "#991b1b"
    },
    {
        "title": "산업화",
        "period": "1960~1980년대",
        "emoji": "🏭",
        "summary": "수출과 제조업 중심으로 경제가 빠르게 성장했습니다.",
        "keywords": ["경제 개발", "수출", "새마을운동"],
        "color": "#ea580c"
    },
    {
        "title": "민주화",
        "period": "1980~1990년대",
        "emoji": "🗳️",
        "summary": "시민들의 노력으로 대통령 직선제와 민주주의 발전이 이루어졌습니다.",
        "keywords": ["5·18", "6월 민주항쟁", "직선제"],
        "color": "#16a34a"
    },
    {
        "title": "오늘날 대한민국",
        "period": "2000년대 이후",
        "emoji": "🌐",
        "summary": "민주주의, 경제, 기술, 문화가 발전하며 세계와 활발히 연결되고 있습니다.",
        "keywords": ["IT", "K-문화", "세계화"],
        "color": "#2563eb"
    },
]

# =====================================================
# 대한민국 역대 대통령
# '업적'은 논쟁적일 수 있어 수업에서는 '주요 내용 / 특징'으로 표현
# =====================================================
PRESIDENTS = [
    {
        "order": "1~3대",
        "name": "이승만",
        "term": "1948~1960",
        "main": "대한민국 초대 대통령",
        "points": ["대한민국 정부 수립", "6·25 전쟁 시기 국정 운영", "반공 체제 강화"],
        "note": "장기 집권과 3·15 부정선거 이후 4·19 혁명으로 하야",
        "color": "#64748b"
    },
    {
        "order": "4대",
        "name": "윤보선",
        "term": "1960~1962",
        "main": "4·19 혁명 이후 제2공화국 대통령",
        "points": ["의원내각제 시기 대통령", "장면 내각과 함께 제2공화국 운영"],
        "note": "5·16 군사정변 이후 정치적 영향력 약화",
        "color": "#94a3b8"
    },
    {
        "order": "5~9대",
        "name": "박정희",
        "term": "1963~1979",
        "main": "산업화와 경제 개발 추진",
        "points": ["경제 개발 5개년 계획", "수출 중심 산업화", "새마을운동", "경부고속도로 건설"],
        "note": "유신 체제와 장기 집권, 민주주의 억압에 대한 비판",
        "color": "#dc2626"
    },
    {
        "order": "10대",
        "name": "최규하",
        "term": "1979~1980",
        "main": "박정희 사망 이후 과도기 대통령",
        "points": ["과도기 국정 운영", "서울의 봄 시기 대통령"],
        "note": "신군부 등장 이후 짧은 기간 재임",
        "color": "#64748b"
    },
    {
        "order": "11~12대",
        "name": "전두환",
        "term": "1980~1988",
        "main": "제5공화국 대통령",
        "points": ["제5공화국 출범", "1986 아시안게임 개최", "1988 서울올림픽 준비"],
        "note": "5·18 민주화운동 유혈 진압과 권위주의 통치에 대한 비판",
        "color": "#7f1d1d"
    },
    {
        "order": "13대",
        "name": "노태우",
        "term": "1988~1993",
        "main": "직선제 개헌 이후 첫 대통령",
        "points": ["1988 서울올림픽 개최", "북방외교", "남북 기본합의서 채택"],
        "note": "군사정권 출신이라는 점과 정치자금 문제에 대한 비판",
        "color": "#f97316"
    },
    {
        "order": "14대",
        "name": "김영삼",
        "term": "1993~1998",
        "main": "문민정부 출범",
        "points": ["금융실명제", "하나회 해체", "지방자치 확대"],
        "note": "임기 말 외환위기 발생",
        "color": "#eab308"
    },
    {
        "order": "15대",
        "name": "김대중",
        "term": "1998~2003",
        "main": "외환위기 극복과 남북 화해 추진",
        "points": ["외환위기 극복 노력", "햇볕정책", "남북정상회담", "노벨평화상 수상"],
        "note": "대북 송금 문제와 정책 평가를 둘러싼 논쟁",
        "color": "#22c55e"
    },
    {
        "order": "16대",
        "name": "노무현",
        "term": "2003~2008",
        "main": "참여정부와 권위주의 문화 완화",
        "points": ["권위주의 완화", "지방분권 추진", "전자정부 발전", "한미 FTA 추진"],
        "note": "정책 추진 방식과 정치 갈등에 대한 논쟁",
        "color": "#3b82f6"
    },
    {
        "order": "17대",
        "name": "이명박",
        "term": "2008~2013",
        "main": "경제 성장과 인프라 사업 강조",
        "points": ["글로벌 금융위기 대응", "G20 서울 정상회의", "4대강 사업"],
        "note": "4대강 사업과 자원외교 등에 대한 논쟁",
        "color": "#2563eb"
    },
    {
        "order": "18대",
        "name": "박근혜",
        "term": "2013~2017",
        "main": "첫 여성 대통령",
        "points": ["문화융성 정책", "창조경제 정책", "복지 정책 확대 시도"],
        "note": "국정농단 사건으로 탄핵 및 파면",
        "color": "#9333ea"
    },
    {
        "order": "19대",
        "name": "문재인",
        "term": "2017~2022",
        "main": "촛불 이후 정부 출범",
        "points": ["남북정상회담", "코로나19 대응", "소득주도성장 정책", "검찰개혁 추진"],
        "note": "부동산 정책과 소득주도성장 평가를 둘러싼 논쟁",
        "color": "#0ea5e9"
    },
    {
        "order": "20대",
        "name": "윤석열",
        "term": "2022~현재",
        "main": "검찰총장 출신 대통령",
        "points": ["한미일 안보 협력 강화", "노동·연금·교육 개혁 추진", "원전 정책 전환"],
        "note": "정책 방향과 정치적 갈등에 대한 다양한 평가가 존재",
        "color": "#0f766e"
    },
]

# =====================================================
# 세션 상태
# =====================================================
if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "quiz_mode" not in st.session_state:
    st.session_state.quiz_mode = "흐름 맞추기"

def make_quiz():
    mode = st.session_state.get("quiz_mode", "흐름 맞추기")

    if mode == "흐름 맞추기":
        question = "다음 중 우리나라 역사 흐름으로 가장 알맞은 것은?"
        correct = "선사 → 고조선 → 삼국 → 남북국 → 고려 → 조선 → 근현대"
        options = [
            correct,
            "조선 → 고려 → 삼국 → 고조선 → 대한민국",
            "삼국 → 선사 → 고려 → 조선 → 고조선",
            "대한민국 → 조선 → 고려 → 삼국 → 고조선"
        ]

    elif mode == "근현대사 맞추기":
        item = random.choice(MODERN_STEPS)
        question = f"다음 설명에 해당하는 근현대사 단계는?<br><br>“{item['summary']}”"
        correct = item["title"]
        options = [x["title"] for x in MODERN_STEPS]
        options = random.sample(options, 4)
        if correct not in options:
            options[0] = correct

    elif mode == "대통령 맞추기":
        item = random.choice(PRESIDENTS)
        point = random.choice(item["points"])
        question = f"다음 내용과 관련 깊은 대통령은?<br><br>“{point}”"
        correct = item["name"]
        options = [x["name"] for x in PRESIDENTS]
        options = random.sample(options, 4)
        if correct not in options:
            options[0] = correct

    else:
        item = random.choice(PRESIDENTS)
        question = f"{item['name']} 대통령의 재임 시기는?"
        correct = item["term"]
        options = [x["term"] for x in PRESIDENTS]
        options = random.sample(options, 4)
        if correct not in options:
            options[0] = correct

    random.shuffle(options)
    st.session_state.quiz_question = question
    st.session_state.quiz_correct = correct
    st.session_state.quiz_options = options
    st.session_state.quiz_answered = False
    st.session_state.quiz_result = ""

if "quiz_options" not in st.session_state:
    make_quiz()

def reset_score():
    st.session_state.score = 0
    st.session_state.total = 0
    make_quiz()

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
    .title-box h1 { margin: 0; font-size: 42px; font-weight: 900; color: #0f172a; }
    .title-box p { margin-top: 10px; font-size: 18px; color: #334155; font-weight: 750; line-height: 1.65; }
    .flow-card, .modern-card, .pres-card {
        background: white;
        border: 1.5px solid #e2e8f0;
        border-radius: 24px;
        padding: 18px 20px;
        box-shadow: 0 5px 16px rgba(0,0,0,0.055);
        margin-bottom: 16px;
    }
    .flow-card { min-height: 210px; }
    .modern-card { min-height: 215px; }
    .pres-card { min-height: 300px; }
    .flow-card h3, .modern-card h3, .pres-card h3 {
        margin: 0 0 10px 0;
        font-size: 23px;
        font-weight: 900;
        color: #111827;
    }
    .flow-card p, .modern-card p, .pres-card p, .pres-card li {
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
    .timeline-box {
        display: flex;
        gap: 10px;
        overflow-x: auto;
        padding: 12px 4px 18px 4px;
        margin-bottom: 16px;
    }
    .timeline-item {
        min-width: 145px;
        border-radius: 22px;
        padding: 15px 12px;
        color: white;
        text-align: center;
        box-shadow: 0 5px 14px rgba(0,0,0,0.12);
    }
    .timeline-item .emoji { font-size: 31px; }
    .timeline-item .name { font-size: 18px; font-weight: 900; margin-top: 4px; }
    .timeline-item .one { font-size: 13px; font-weight: 750; margin-top: 7px; line-height: 1.35; }
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
        .title-box { padding: 20px 18px; border-radius: 22px; }
        .title-box h1 { font-size: 30px; }
        .title-box p { font-size: 15px; }
        .flow-card, .modern-card, .pres-card { min-height: auto; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-box">
        <h1>🇰🇷 우리나라 역사와 근현대사</h1>
        <p>
            우리 역사의 큰 흐름을 간단히 보고, 근현대사는 조금 더 자세히 살펴봅니다.<br>
            대통령별 주요 내용은 <b>성과와 한계를 함께</b> 간략하게 정리했습니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧭 큰 흐름",
    "🇰🇷 근현대사",
    "👤 대통령 정리",
    "📌 한눈에 정리",
    "🎮 확인 퀴즈"
])

# =====================================================
# 큰 흐름
# =====================================================
with tab1:
    st.markdown("### 🧭 우리나라 역사 큰 흐름")

    timeline_html = "<div class='timeline-box'>"
    for item in HISTORY_FLOW:
        timeline_html += f"""
        <div class='timeline-item' style='background:{item["color"]};'>
            <div class='emoji'>{item["emoji"]}</div>
            <div class='name'>{item["name"]}</div>
            <div class='one'>{item["one"]}</div>
        </div>
        """
    timeline_html += "</div>"
    st.markdown(timeline_html, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="mini-box">
        <b>선사 → 고조선 → 삼국 → 남북국 → 고려 → 조선 → 근현대</b><br>
        이렇게 먼저 큰 순서를 잡고, 근현대사는 다시 <b>개항 → 대한제국 → 일제 강점기 → 광복 → 전쟁 → 산업화 → 민주화 → 오늘날</b>로 나누어 보면 쉽습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(3)
    for i, item in enumerate(HISTORY_FLOW):
        with cols[i % 3]:
            tags = "".join([f"<span class='tag'>{kw}</span>" for kw in item["keywords"]])
            st.markdown(
                f"""
                <div class="flow-card">
                    <h3>{item['emoji']} {item['name']}</h3>
                    <p><b>시기:</b> {item['period']}</p>
                    <p><b>핵심:</b> {item['one']}</p>
                    <div>{tags}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# 근현대사
# =====================================================
with tab2:
    st.markdown("### 🇰🇷 근현대사 조금 더 자세히")

    cols = st.columns(4)
    for i, item in enumerate(MODERN_STEPS):
        with cols[i % 4]:
            tags = "".join([f"<span class='tag'>{kw}</span>" for kw in item["keywords"]])
            st.markdown(
                f"""
                <div class="modern-card" style="border-top: 8px solid {item['color']};">
                    <h3>{item['emoji']} {item['title']}</h3>
                    <p><b>시기:</b> {item['period']}</p>
                    <p>{item['summary']}</p>
                    <div>{tags}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# 대통령 정리
# =====================================================
with tab3:
    st.markdown("### 👤 대한민국 역대 대통령 주요 내용")

    st.markdown(
        """
        <div class="mini-box">
        ※ 대통령별 내용은 수업용으로 간단히 정리한 것입니다. 특정 인물에 대한 평가가 아니라, <b>주요 정책·사건·역사적 쟁점</b>을 함께 보는 것이 목적입니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(3)
    for i, p in enumerate(PRESIDENTS):
        with cols[i % 3]:
            points = "".join([f"<li>{x}</li>" for x in p["points"]])
            st.markdown(
                f"""
                <div class="pres-card" style="border-top: 8px solid {p['color']};">
                    <h3>{p['order']} {p['name']}</h3>
                    <p><b>재임:</b> {p['term']}</p>
                    <p><b>핵심:</b> {p['main']}</p>
                    <ul>{points}</ul>
                    <p><b>함께 볼 점:</b><br>{p['note']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# 한눈에 정리
# =====================================================
with tab4:
    st.markdown("### 📌 근현대사 핵심 흐름")

    rows = []
    for item in MODERN_STEPS:
        rows.append({
            "단계": item["title"],
            "시기": item["period"],
            "핵심 설명": item["summary"],
            "키워드": ", ".join(item["keywords"])
        })
    st.dataframe(rows, use_container_width=True, hide_index=True)

    st.markdown("### 👤 대통령 간단 표")
    pres_rows = []
    for p in PRESIDENTS:
        pres_rows.append({
            "대수": p["order"],
            "대통령": p["name"],
            "재임": p["term"],
            "핵심": p["main"]
        })
    st.dataframe(pres_rows, use_container_width=True, hide_index=True)

    st.markdown(
        """
        <div class="mini-box">
        <b>근현대사 암기 공식</b><br>
        개항 → 대한제국 → 일제 강점기 → 광복과 정부 수립 → 6·25 전쟁 → 산업화 → 민주화 → 오늘날 대한민국
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# 확인 퀴즈
# =====================================================
with tab5:
    st.markdown("### 🎮 우리나라 역사 확인 퀴즈")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("점수", f"{st.session_state.score} / {st.session_state.total}")
    with c2:
        acc = round(st.session_state.score / st.session_state.total * 100) if st.session_state.total > 0 else 0
        st.metric("정답률", f"{acc}%")
    with c3:
        if st.button("🔄 점수 초기화", use_container_width=True):
            reset_score()
            st.rerun()

    selected_mode = st.radio(
        "퀴즈 유형",
        ["흐름 맞추기", "근현대사 맞추기", "대통령 맞추기", "재임 시기 맞추기"],
        horizontal=True,
        key="history_quiz_radio"
    )

    if selected_mode != st.session_state.quiz_mode:
        st.session_state.quiz_mode = selected_mode
        make_quiz()
        st.rerun()

    st.markdown(
        f"""
        <div class="quiz-box">
            {st.session_state.quiz_question}
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(2)
    for i, option in enumerate(st.session_state.quiz_options):
        with cols[i % 2]:
            if st.button(
                option,
                key=f"history_quiz_{i}_{st.session_state.total}",
                use_container_width=True,
                disabled=st.session_state.quiz_answered
            ):
                st.session_state.quiz_answered = True
                st.session_state.total += 1

                if option == st.session_state.quiz_correct:
                    st.session_state.score += 1
                    st.session_state.quiz_result = f"✅ 정답입니다! {st.session_state.quiz_correct}"
                else:
                    st.session_state.quiz_result = f"❌ 아쉬워요. 정답은 `{st.session_state.quiz_correct}`입니다."

                st.rerun()

    if st.session_state.quiz_result:
        if st.session_state.quiz_result.startswith("✅"):
            st.success(st.session_state.quiz_result)
        else:
            st.error(st.session_state.quiz_result)

    if st.button("➡️ 다음 문제", use_container_width=True):
        make_quiz()
        st.rerun()

st.caption("필요 패키지: streamlit, plotly")
