import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os
import json
import countryinfo

st.set_page_config(
    page_title="세계 지도 학습 자료",
    page_icon="🌍",
    layout="wide"
)

# =====================================================
# 기본 라벨 데이터
# =====================================================
CONTINENTS = [
    {"name": "북아메리카\nNorth America", "lat": 50, "lon": -105},
    {"name": "남아메리카\nSouth America", "lat": -18, "lon": -60},
    {"name": "유럽\nEurope", "lat": 54, "lon": 15},
    {"name": "아프리카\nAfrica", "lat": 5, "lon": 20},
    {"name": "아시아\nAsia", "lat": 40, "lon": 90},
    {"name": "오세아니아\nOceania", "lat": -25, "lon": 135},
    {"name": "남극\nAntarctica", "lat": -78, "lon": 20},
]

SEAS = [
    {"name": "태평양\nPacific Ocean", "lat": 8, "lon": -155},
    {"name": "태평양\nPacific Ocean", "lat": 5, "lon": 160},
    {"name": "대서양\nAtlantic Ocean", "lat": 10, "lon": -35},
    {"name": "인도양\nIndian Ocean", "lat": -20, "lon": 80},
    {"name": "북극해\nArctic Ocean", "lat": 78, "lon": 0},
    {"name": "남극해\nSouthern Ocean", "lat": -58, "lon": 80},
    {"name": "홍해\nRed Sea", "lat": 20, "lon": 38},
    {"name": "지중해\nMediterranean Sea", "lat": 35, "lon": 18},
    {"name": "흑해\nBlack Sea", "lat": 43, "lon": 35},
    {"name": "카리브해\nCaribbean Sea", "lat": 15, "lon": -75},
    {"name": "아라비아해\nArabian Sea", "lat": 16, "lon": 64},
    {"name": "벵골만\nBay of Bengal", "lat": 15, "lon": 88},
    {"name": "남중국해\nSouth China Sea", "lat": 14, "lon": 114},
    {"name": "동중국해\nEast China Sea", "lat": 28, "lon": 125},
    {"name": "서해\nYellow Sea", "lat": 35, "lon": 123},
    {"name": "동해/일본해\nEast Sea / Sea of Japan", "lat": 40, "lon": 136},
    {"name": "필리핀해\nPhilippine Sea", "lat": 20, "lon": 135},
    {"name": "베링해\nBering Sea", "lat": 58, "lon": -176},
    {"name": "산호해\nCoral Sea", "lat": -18, "lon": 155},
    {"name": "태즈먼해\nTasman Sea", "lat": -38, "lon": 158},
    {"name": "노르웨이해\nNorwegian Sea", "lat": 68, "lon": 3},
    {"name": "발트해\nBaltic Sea", "lat": 58, "lon": 20},
    {"name": "카스피해\nCaspian Sea", "lat": 41, "lon": 51},
    {"name": "페르시아만\nPersian Gulf", "lat": 26, "lon": 52},
    {"name": "멕시코만\nGulf of Mexico", "lat": 24, "lon": -90},
    {"name": "허드슨만\nHudson Bay", "lat": 60, "lon": -85},
    {"name": "기니만\nGulf of Guinea", "lat": 0, "lon": 2},
    {"name": "아덴만\nGulf of Aden", "lat": 13, "lon": 48},
    {"name": "안다만해\nAndaman Sea", "lat": 11, "lon": 96},
    {"name": "자와해\nJava Sea", "lat": -6, "lon": 112},
    {"name": "아라푸라해\nArafura Sea", "lat": -10, "lon": 136},
    {"name": "래브라도해\nLabrador Sea", "lat": 58, "lon": -50},
]

RIVERS = [
    {"name": "나일강\nNile", "lat": 18, "lon": 31},
    {"name": "콩고강\nCongo", "lat": -2, "lon": 21},
    {"name": "니제르강\nNiger", "lat": 11, "lon": 5},
    {"name": "잠베지강\nZambezi", "lat": -16, "lon": 28},
    {"name": "오렌지강\nOrange", "lat": -29, "lon": 22},
    {"name": "아마존강\nAmazon", "lat": -3, "lon": -60},
    {"name": "오리노코강\nOrinoco", "lat": 7, "lon": -65},
    {"name": "파라나강\nParaná", "lat": -25, "lon": -58},
    {"name": "미시시피강\nMississippi", "lat": 35, "lon": -90},
    {"name": "미주리강\nMissouri", "lat": 45, "lon": -101},
    {"name": "리오그란데강\nRio Grande", "lat": 28, "lon": -102},
    {"name": "세인트로렌스강\nSt. Lawrence", "lat": 47, "lon": -71},
    {"name": "유콘강\nYukon", "lat": 64, "lon": -155},
    {"name": "매켄지강\nMackenzie", "lat": 64, "lon": -122},
    {"name": "다뉴브강\nDanube", "lat": 46, "lon": 20},
    {"name": "라인강\nRhine", "lat": 50, "lon": 7},
    {"name": "볼가강\nVolga", "lat": 55, "lon": 45},
    {"name": "드네프르강\nDnieper", "lat": 49, "lon": 32},
    {"name": "우랄강\nUral", "lat": 49, "lon": 51},
    {"name": "템스강\nThames", "lat": 51.5, "lon": 0},
    {"name": "세느강\nSeine", "lat": 48.7, "lon": 2.5},
    {"name": "티그리스강\nTigris", "lat": 33, "lon": 44},
    {"name": "유프라테스강\nEuphrates", "lat": 34, "lon": 41},
    {"name": "인더스강\nIndus", "lat": 29, "lon": 70},
    {"name": "갠지스강\nGanges", "lat": 25, "lon": 83},
    {"name": "브라마푸트라강\nBrahmaputra", "lat": 25, "lon": 91},
    {"name": "양쯔강\nYangtze", "lat": 30, "lon": 112},
    {"name": "황허\nYellow River", "lat": 35, "lon": 110},
    {"name": "메콩강\nMekong", "lat": 16, "lon": 105},
    {"name": "이라와디강\nIrrawaddy", "lat": 19, "lon": 96},
    {"name": "오비강\nOb", "lat": 61, "lon": 72},
    {"name": "예니세이강\nYenisei", "lat": 64, "lon": 92},
    {"name": "레나강\nLena", "lat": 64, "lon": 125},
    {"name": "아무르강\nAmur", "lat": 49, "lon": 134},
    {"name": "머리강\nMurray", "lat": -34, "lon": 142},
]

# =====================================================
# 전체 나라 이름 불러오기
# countryinfo 패키지 내부 데이터 사용 (오프라인 가능)
# =====================================================
@st.cache_data
def load_all_countries():
    data_dir = os.path.join(os.path.dirname(countryinfo.__file__), "data")
    rows = []

    for filename in os.listdir(data_dir):
        if not filename.endswith('.json'):
            continue

        path = os.path.join(data_dir, filename)
        try:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)

            name = data.get('name')
            iso = (data.get('ISO') or {}).get('alpha3')
            latlng = data.get('latlng')
            region = data.get('region', '')
            capital = data.get('capital', '')

            if name and iso and isinstance(latlng, list) and len(latlng) >= 2:
                rows.append({
                    "name": name,
                    "iso": iso,
                    "lat": float(latlng[0]),
                    "lon": float(latlng[1]),
                    "region": region,
                    "capital": capital,
                })
        except Exception:
            continue

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.drop_duplicates(subset=["iso"]).sort_values("name").reset_index(drop=True)
    return df

countries_df = load_all_countries()

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
        <p>
            대륙 이름, 세부 바다 이름, 강 이름, 나라 이름을 한 지도에서 함께 볼 수 있습니다.<br>
            체크박스로 원하는 정보만 켜고 끌 수 있습니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 옵션
# =====================================================
row1 = st.columns(4)
with row1[0]:
    show_continents = st.checkbox("대륙 이름 보기", value=True)
with row1[1]:
    show_seas = st.checkbox("바다 이름 보기", value=True)
with row1[2]:
    show_rivers = st.checkbox("강 이름 보기", value=False)
with row1[3]:
    show_countries = st.checkbox("나라 이름 보기", value=False)

row2 = st.columns(4)
with row2[0]:
    country_font = st.slider("나라 이름 크기", 6, 18, 8)
with row2[1]:
    sea_font = st.slider("바다 이름 크기", 10, 24, 16)
with row2[2]:
    river_font = st.slider("강 이름 크기", 8, 20, 12)
with row2[3]:
    continent_font = st.slider("대륙 이름 크기", 14, 30, 22)

st.markdown(
    f"""
    <div class="info-box">
    ✅ <b>나라 이름</b>은 countryinfo 데이터 기준으로 <b>{len(countries_df)}개</b>를 불러옵니다.<br>
    ✅ 지도는 마우스로 확대/축소할 수 있고, 확대하면 나라 이름을 더 자세히 볼 수 있습니다.<br>
    ✅ Plotly 범례(legend)에서도 레이어를 클릭해서 보이기/숨기기를 할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 지도 생성
# =====================================================
fig = go.Figure()

# 대륙
fig.add_trace(go.Scattergeo(
    lon=[c["lon"] for c in CONTINENTS],
    lat=[c["lat"] for c in CONTINENTS],
    mode="text",
    text=[c["name"] for c in CONTINENTS],
    textfont=dict(size=continent_font, color="#7c2d12"),
    textposition="middle center",
    name="대륙",
    hoverinfo="skip",
    visible=show_continents
))

# 바다
fig.add_trace(go.Scattergeo(
    lon=[s["lon"] for s in SEAS],
    lat=[s["lat"] for s in SEAS],
    mode="text",
    text=[s["name"] for s in SEAS],
    textfont=dict(size=sea_font, color="#0369a1"),
    textposition="middle center",
    name="바다",
    hoverinfo="skip",
    visible=show_seas
))

# 강
fig.add_trace(go.Scattergeo(
    lon=[r["lon"] for r in RIVERS],
    lat=[r["lat"] for r in RIVERS],
    mode="markers+text",
    text=[r["name"] for r in RIVERS],
    textfont=dict(size=river_font, color="#1d4ed8"),
    textposition="top center",
    marker=dict(size=4, color="#60a5fa", opacity=0.7),
    name="강",
    hoverinfo="skip",
    visible=show_rivers
))

# 나라
if not countries_df.empty:
    fig.add_trace(go.Scattergeo(
        lon=countries_df["lon"],
        lat=countries_df["lat"],
        mode="markers+text",
        text=countries_df["name"],
        textfont=dict(size=country_font, color="#111827"),
        textposition="top center",
        marker=dict(size=3, color="#ef4444", opacity=0.65),
        name="나라",
        hovertext=[
            f"{row['name']}<br>Region: {row['region']}<br>Capital: {row['capital']}" if row['capital'] else f"{row['name']}<br>Region: {row['region']}"
            for _, row in countries_df.iterrows()
        ],
        hoverinfo="text",
        visible=show_countries
    ))

fig.update_layout(
    height=780,
    margin=dict(l=0, r=0, t=0, b=0),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.01,
        xanchor="left",
        x=0.01,
        bgcolor="rgba(255,255,255,0.75)"
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
        resolution=50,
    )
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "scrollZoom": True,
        "displaylogo": False
    }
)

# =====================================================
# 수업용 정리
# =====================================================
st.markdown("---")
st.markdown("## 📌 수업용 빠른 정리")

c1, c2 = st.columns(2)

with c1:
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

with c2:
    st.markdown(
        """
        ### 🌊 주요 바다 / 강 예시
        **바다**
        - 태평양 / Pacific Ocean
        - 대서양 / Atlantic Ocean
        - 인도양 / Indian Ocean
        - 홍해 / Red Sea
        - 지중해 / Mediterranean Sea

        **강**
        - 나일강 / Nile
        - 아마존강 / Amazon
        - 미시시피강 / Mississippi
        - 양쯔강 / Yangtze
        - 메콩강 / Mekong
        """
    )

st.caption("필요한 패키지: streamlit, plotly, pandas, countryinfo")
