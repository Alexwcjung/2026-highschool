import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="세계 지도 학습",
    page_icon="🌍",
    layout="wide"
)

# =====================================================
# 대륙 이름 위치
# =====================================================
CONTINENTS = [
    {"name": "북아메리카\nNorth America", "lat": 50, "lon": -105},
    {"name": "남아메리카\nSouth America", "lat": -18, "lon": -60},
    {"name": "유럽\nEurope", "lat": 52, "lon": 15},
    {"name": "아프리카\nAfrica", "lat": 5, "lon": 20},
    {"name": "아시아\nAsia", "lat": 38, "lon": 90},
    {"name": "오세아니아\nOceania", "lat": -25, "lon": 135},
    {"name": "남극\nAntarctica", "lat": -78, "lon": 20},
]

# =====================================================
# 바다 이름 위치
# =====================================================
OCEANS = [
    {"name": "태평양\nPacific Ocean", "lat": 5, "lon": -155},
    {"name": "태평양\nPacific Ocean", "lat": 5, "lon": 160},
    {"name": "대서양\nAtlantic Ocean", "lat": 10, "lon": -35},
    {"name": "인도양\nIndian Ocean", "lat": -20, "lon": 80},
    {"name": "북극해\nArctic Ocean", "lat": 78, "lon": 0},
    {"name": "남극해\nSouthern Ocean", "lat": -60, "lon": 80},
]

# =====================================================
# 주요 나라 이름 위치
# 필요하면 여기에 계속 추가하면 됨
# =====================================================
COUNTRIES = [
    # Asia
    {"ko": "대한민국", "en": "South Korea", "lat": 36.5, "lon": 127.8, "continent": "아시아"},
    {"ko": "북한", "en": "North Korea", "lat": 40.3, "lon": 127.0, "continent": "아시아"},
    {"ko": "일본", "en": "Japan", "lat": 37.5, "lon": 138.0, "continent": "아시아"},
    {"ko": "중국", "en": "China", "lat": 35.8, "lon": 104.2, "continent": "아시아"},
    {"ko": "몽골", "en": "Mongolia", "lat": 46.8, "lon": 103.8, "continent": "아시아"},
    {"ko": "인도", "en": "India", "lat": 22.8, "lon": 78.9, "continent": "아시아"},
    {"ko": "태국", "en": "Thailand", "lat": 15.8, "lon": 101.0, "continent": "아시아"},
    {"ko": "베트남", "en": "Vietnam", "lat": 16.2, "lon": 107.8, "continent": "아시아"},
    {"ko": "필리핀", "en": "Philippines", "lat": 12.8, "lon": 122.8, "continent": "아시아"},
    {"ko": "인도네시아", "en": "Indonesia", "lat": -2.5, "lon": 118.0, "continent": "아시아"},
    {"ko": "말레이시아", "en": "Malaysia", "lat": 4.2, "lon": 102.0, "continent": "아시아"},
    {"ko": "싱가포르", "en": "Singapore", "lat": 1.3, "lon": 103.8, "continent": "아시아"},
    {"ko": "사우디아라비아", "en": "Saudi Arabia", "lat": 24.0, "lon": 45.0, "continent": "아시아"},
    {"ko": "이란", "en": "Iran", "lat": 32.0, "lon": 53.0, "continent": "아시아"},
    {"ko": "튀르키예", "en": "Turkey", "lat": 39.0, "lon": 35.0, "continent": "아시아/유럽"},

    # Europe
    {"ko": "영국", "en": "United Kingdom", "lat": 54.0, "lon": -2.5, "continent": "유럽"},
    {"ko": "아일랜드", "en": "Ireland", "lat": 53.2, "lon": -8.0, "continent": "유럽"},
    {"ko": "프랑스", "en": "France", "lat": 46.5, "lon": 2.2, "continent": "유럽"},
    {"ko": "독일", "en": "Germany", "lat": 51.0, "lon": 10.0, "continent": "유럽"},
    {"ko": "스페인", "en": "Spain", "lat": 40.2, "lon": -3.7, "continent": "유럽"},
    {"ko": "포르투갈", "en": "Portugal", "lat": 39.5, "lon": -8.0, "continent": "유럽"},
    {"ko": "이탈리아", "en": "Italy", "lat": 42.8, "lon": 12.5, "continent": "유럽"},
    {"ko": "그리스", "en": "Greece", "lat": 39.0, "lon": 22.0, "continent": "유럽"},
    {"ko": "노르웨이", "en": "Norway", "lat": 61.0, "lon": 8.0, "continent": "유럽"},
    {"ko": "스웨덴", "en": "Sweden", "lat": 62.0, "lon": 15.0, "continent": "유럽"},
    {"ko": "핀란드", "en": "Finland", "lat": 64.5, "lon": 26.0, "continent": "유럽"},
    {"ko": "폴란드", "en": "Poland", "lat": 52.0, "lon": 19.0, "continent": "유럽"},
    {"ko": "우크라이나", "en": "Ukraine", "lat": 49.0, "lon": 32.0, "continent": "유럽"},
    {"ko": "러시아", "en": "Russia", "lat": 60.0, "lon": 90.0, "continent": "유럽/아시아"},

    # Africa
    {"ko": "이집트", "en": "Egypt", "lat": 26.8, "lon": 30.8, "continent": "아프리카"},
    {"ko": "리비아", "en": "Libya", "lat": 27.0, "lon": 17.0, "continent": "아프리카"},
    {"ko": "알제리", "en": "Algeria", "lat": 28.0, "lon": 2.6, "continent": "아프리카"},
    {"ko": "모로코", "en": "Morocco", "lat": 31.8, "lon": -6.0, "continent": "아프리카"},
    {"ko": "나이지리아", "en": "Nigeria", "lat": 9.0, "lon": 8.0, "continent": "아프리카"},
    {"ko": "케냐", "en": "Kenya", "lat": 0.2, "lon": 37.9, "continent": "아프리카"},
    {"ko": "에티오피아", "en": "Ethiopia", "lat": 9.1, "lon": 40.5, "continent": "아프리카"},
    {"ko": "탄자니아", "en": "Tanzania", "lat": -6.3, "lon": 35.0, "continent": "아프리카"},
    {"ko": "남아프리카공화국", "en": "South Africa", "lat": -30.5, "lon": 24.0, "continent": "아프리카"},
    {"ko": "마다가스카르", "en": "Madagascar", "lat": -19.0, "lon": 46.5, "continent": "아프리카"},

    # North America
    {"ko": "캐나다", "en": "Canada", "lat": 57.0, "lon": -106.0, "continent": "북아메리카"},
    {"ko": "미국", "en": "United States", "lat": 39.5, "lon": -98.3, "continent": "북아메리카"},
    {"ko": "멕시코", "en": "Mexico", "lat": 23.6, "lon": -102.5, "continent": "북아메리카"},
    {"ko": "쿠바", "en": "Cuba", "lat": 21.5, "lon": -79.5, "continent": "북아메리카"},
    {"ko": "과테말라", "en": "Guatemala", "lat": 15.6, "lon": -90.2, "continent": "북아메리카"},
    {"ko": "파나마", "en": "Panama", "lat": 8.5, "lon": -80.0, "continent": "북아메리카"},

    # South America
    {"ko": "브라질", "en": "Brazil", "lat": -10.0, "lon": -55.0, "continent": "남아메리카"},
    {"ko": "아르헨티나", "en": "Argentina", "lat": -34.0, "lon": -64.0, "continent": "남아메리카"},
    {"ko": "칠레", "en": "Chile", "lat": -30.0, "lon": -71.0, "continent": "남아메리카"},
    {"ko": "페루", "en": "Peru", "lat": -9.2, "lon": -75.0, "continent": "남아메리카"},
    {"ko": "콜롬비아", "en": "Colombia", "lat": 4.5, "lon": -74.0, "continent": "남아메리카"},
    {"ko": "베네수엘라", "en": "Venezuela", "lat": 7.0, "lon": -66.0, "continent": "남아메리카"},
    {"ko": "볼리비아", "en": "Bolivia", "lat": -16.3, "lon": -64.7, "continent": "남아메리카"},

    # Oceania
    {"ko": "호주", "en": "Australia", "lat": -25.0, "lon": 133.0, "continent": "오세아니아"},
    {"ko": "뉴질랜드", "en": "New Zealand", "lat": -41.0, "lon": 174.0, "continent": "오세아니아"},
    {"ko": "파푸아뉴기니", "en": "Papua New Guinea", "lat": -6.3, "lon": 147.0, "continent": "오세아니아"},

    # Antarctica
    {"ko": "남극", "en": "Antarctica", "lat": -78.0, "lon": 20.0, "continent": "남극"},
]

# =====================================================
# 스타일
# =====================================================
st.markdown(
    """
    <style>
    .title-box {
        background: linear-gradient(135deg, #dbeafe 0%, #ecfeff 45%, #fef3c7 100%);
        border-radius: 28px;
        padding: 26px 30px;
        margin-bottom: 18px;
        border: 1.5px solid #bfdbfe;
        box-shadow: 0 8px 20px rgba(0,0,0,0.07);
    }
    .title-box h1 {
        margin: 0;
        font-size: 38px;
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
    .info-box {
        background: white;
        border: 1.5px solid #e2e8f0;
        border-radius: 20px;
        padding: 16px 18px;
        margin-bottom: 14px;
        font-size: 16px;
        font-weight: 700;
        color: #334155;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-box">
        <h1>🌍 세계 지도 학습 자료</h1>
        <p>대륙, 바다, 나라 이름을 지도에서 함께 확인해 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 옵션
# =====================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    show_continents = st.checkbox("대륙 이름 보기", value=True)

with col2:
    show_oceans = st.checkbox("바다 이름 보기", value=True)

with col3:
    show_countries = st.checkbox("나라 이름 보기", value=True)

with col4:
    language_mode = st.selectbox(
        "표시 언어",
        ["한국어 + 영어", "한국어", "영어"]
    )

st.markdown(
    """
    <div class="info-box">
    🖱️ 지도를 확대하면 나라 이름 위치를 더 자세히 볼 수 있습니다.  
    수업할 때는 먼저 <b>대륙·바다 이름</b>만 보여주고, 이후 <b>나라 이름</b>을 켜면 좋습니다.
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 지도 생성
# =====================================================
fig = go.Figure()

# 배경용 투명 점
fig.add_trace(go.Scattergeo(
    lon=[0],
    lat=[0],
    mode="markers",
    marker=dict(size=1, color="rgba(0,0,0,0)"),
    showlegend=False,
    hoverinfo="skip"
))

# 대륙 이름
if show_continents:
    fig.add_trace(go.Scattergeo(
        lon=[c["lon"] for c in CONTINENTS],
        lat=[c["lat"] for c in CONTINENTS],
        mode="text",
        text=[c["name"] for c in CONTINENTS],
        textfont=dict(size=22, color="#7c2d12"),
        textposition="middle center",
        name="대륙",
        hoverinfo="text"
    ))

# 바다 이름
if show_oceans:
    fig.add_trace(go.Scattergeo(
        lon=[o["lon"] for o in OCEANS],
        lat=[o["lat"] for o in OCEANS],
        mode="text",
        text=[o["name"] for o in OCEANS],
        textfont=dict(size=18, color="#0369a1"),
        textposition="middle center",
        name="바다",
        hoverinfo="text"
    ))

# 나라 이름
if show_countries:
    country_texts = []
    for c in COUNTRIES:
        if language_mode == "한국어 + 영어":
            country_texts.append(f"{c['ko']}<br>{c['en']}")
        elif language_mode == "한국어":
            country_texts.append(c["ko"])
        else:
            country_texts.append(c["en"])

    fig.add_trace(go.Scattergeo(
        lon=[c["lon"] for c in COUNTRIES],
        lat=[c["lat"] for c in COUNTRIES],
        mode="markers+text",
        text=country_texts,
        textfont=dict(size=9, color="#111827"),
        textposition="top center",
        marker=dict(
            size=5,
            color="#ef4444",
            opacity=0.75
        ),
        name="나라",
        hovertext=[
            f"{c['ko']} / {c['en']}<br>대륙: {c['continent']}"
            for c in COUNTRIES
        ],
        hoverinfo="text"
    ))

fig.update_layout(
    height=720,
    margin=dict(l=0, r=0, t=0, b=0),
    showlegend=False,
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
    )
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# 간단 학습 정리
# =====================================================
st.markdown("## 📌 수업용 기본 정리")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown(
        """
        ### 🌎 7대륙
        - 아시아 / Asia
        - 유럽 / Europe
        - 아프리카 / Africa
        - 북아메리카 / North America
        - 남아메리카 / South America
        - 오세아니아 / Oceania
        - 남극 / Antarctica
        """
    )

with col_b:
    st.markdown(
        """
        ### 🌊 주요 바다
        - 태평양 / Pacific Ocean
        - 대서양 / Atlantic Ocean
        - 인도양 / Indian Ocean
        - 북극해 / Arctic Ocean
        - 남극해 / Southern Ocean
        """
    )

# =====================================================
# 간단 확인 퀴즈
# =====================================================
st.markdown("---")
st.markdown("## 🎮 간단 확인 퀴즈")

quiz_type = st.radio(
    "퀴즈 종류",
    ["나라 → 대륙 맞추기", "영어 이름 맞추기"],
    horizontal=True
)

if "geo_quiz_item" not in st.session_state:
    st.session_state.geo_quiz_item = random.choice(COUNTRIES)

if "geo_quiz_answered" not in st.session_state:
    st.session_state.geo_quiz_answered = False

if "geo_quiz_result" not in st.session_state:
    st.session_state.geo_quiz_result = ""

item = st.session_state.geo_quiz_item

if quiz_type == "나라 → 대륙 맞추기":
    st.markdown(f"### `{item['ko']}`은 어느 대륙에 있을까요?")

    options = ["아시아", "유럽", "아프리카", "북아메리카", "남아메리카", "오세아니아"]
    random.shuffle(options)

    cols = st.columns(3)
    for i, option in enumerate(options):
        with cols[i % 3]:
            if st.button(option, use_container_width=True, disabled=st.session_state.geo_quiz_answered):
                st.session_state.geo_quiz_answered = True
                if option in item["continent"]:
                    st.session_state.geo_quiz_result = f"✅ 정답입니다! {item['ko']}은/는 {item['continent']}에 있습니다."
                else:
                    st.session_state.geo_quiz_result = f"❌ 정답은 {item['continent']}입니다."
                st.rerun()

else:
    st.markdown(f"### `{item['ko']}`의 영어 이름은 무엇일까요?")

    wrongs = random.sample([c for c in COUNTRIES if c["ko"] != item["ko"]], 3)
    options = wrongs + [item]
    random.shuffle(options)

    cols = st.columns(2)
    for i, option in enumerate(options):
        with cols[i % 2]:
            if st.button(option["en"], use_container_width=True, disabled=st.session_state.geo_quiz_answered):
                st.session_state.geo_quiz_answered = True
                if option["ko"] == item["ko"]:
                    st.session_state.geo_quiz_result = f"✅ 정답입니다! {item['ko']} = {item['en']}"
                else:
                    st.session_state.geo_quiz_result = f"❌ 정답은 {item['en']}입니다."
                st.rerun()

if st.session_state.geo_quiz_result:
    st.success(st.session_state.geo_quiz_result)

if st.button("➡️ 다음 문제", use_container_width=True):
    st.session_state.geo_quiz_item = random.choice(COUNTRIES)
    st.session_state.geo_quiz_answered = False
    st.session_state.geo_quiz_result = ""
    st.rerun()
