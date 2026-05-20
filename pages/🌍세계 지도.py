import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
import json
import random

try:
    import countryinfo
    COUNTRYINFO_AVAILABLE = True
except Exception:
    COUNTRYINFO_AVAILABLE = False

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
# 퀴즈용 나라 데이터
# flag 포함
# =====================================================
QUIZ_COUNTRIES = [
    {"ko": "대한민국", "en": "South Korea", "iso": "KOR", "continent": "아시아", "flag": "🇰🇷"},
    {"ko": "일본", "en": "Japan", "iso": "JPN", "continent": "아시아", "flag": "🇯🇵"},
    {"ko": "중국", "en": "China", "iso": "CHN", "continent": "아시아", "flag": "🇨🇳"},
    {"ko": "인도", "en": "India", "iso": "IND", "continent": "아시아", "flag": "🇮🇳"},
    {"ko": "태국", "en": "Thailand", "iso": "THA", "continent": "아시아", "flag": "🇹🇭"},
    {"ko": "베트남", "en": "Vietnam", "iso": "VNM", "continent": "아시아", "flag": "🇻🇳"},
    {"ko": "필리핀", "en": "Philippines", "iso": "PHL", "continent": "아시아", "flag": "🇵🇭"},
    {"ko": "인도네시아", "en": "Indonesia", "iso": "IDN", "continent": "아시아", "flag": "🇮🇩"},
    {"ko": "사우디아라비아", "en": "Saudi Arabia", "iso": "SAU", "continent": "아시아", "flag": "🇸🇦"},
    {"ko": "튀르키예", "en": "Turkey", "iso": "TUR", "continent": "아시아/유럽", "flag": "🇹🇷"},
    {"ko": "영국", "en": "United Kingdom", "iso": "GBR", "continent": "유럽", "flag": "🇬🇧"},
    {"ko": "프랑스", "en": "France", "iso": "FRA", "continent": "유럽", "flag": "🇫🇷"},
    {"ko": "독일", "en": "Germany", "iso": "DEU", "continent": "유럽", "flag": "🇩🇪"},
    {"ko": "이탈리아", "en": "Italy", "iso": "ITA", "continent": "유럽", "flag": "🇮🇹"},
    {"ko": "스페인", "en": "Spain", "iso": "ESP", "continent": "유럽", "flag": "🇪🇸"},
    {"ko": "포르투갈", "en": "Portugal", "iso": "PRT", "continent": "유럽", "flag": "🇵🇹"},
    {"ko": "그리스", "en": "Greece", "iso": "GRC", "continent": "유럽", "flag": "🇬🇷"},
    {"ko": "러시아", "en": "Russia", "iso": "RUS", "continent": "유럽/아시아", "flag": "🇷🇺"},
    {"ko": "미국", "en": "United States", "iso": "USA", "continent": "북아메리카", "flag": "🇺🇸"},
    {"ko": "캐나다", "en": "Canada", "iso": "CAN", "continent": "북아메리카", "flag": "🇨🇦"},
    {"ko": "멕시코", "en": "Mexico", "iso": "MEX", "continent": "북아메리카", "flag": "🇲🇽"},
    {"ko": "쿠바", "en": "Cuba", "iso": "CUB", "continent": "북아메리카", "flag": "🇨🇺"},
    {"ko": "브라질", "en": "Brazil", "iso": "BRA", "continent": "남아메리카", "flag": "🇧🇷"},
    {"ko": "아르헨티나", "en": "Argentina", "iso": "ARG", "continent": "남아메리카", "flag": "🇦🇷"},
    {"ko": "칠레", "en": "Chile", "iso": "CHL", "continent": "남아메리카", "flag": "🇨🇱"},
    {"ko": "페루", "en": "Peru", "iso": "PER", "continent": "남아메리카", "flag": "🇵🇪"},
    {"ko": "콜롬비아", "en": "Colombia", "iso": "COL", "continent": "남아메리카", "flag": "🇨🇴"},
    {"ko": "이집트", "en": "Egypt", "iso": "EGY", "continent": "아프리카", "flag": "🇪🇬"},
    {"ko": "남아프리카공화국", "en": "South Africa", "iso": "ZAF", "continent": "아프리카", "flag": "🇿🇦"},
    {"ko": "케냐", "en": "Kenya", "iso": "KEN", "continent": "아프리카", "flag": "🇰🇪"},
    {"ko": "나이지리아", "en": "Nigeria", "iso": "NGA", "continent": "아프리카", "flag": "🇳🇬"},
    {"ko": "모로코", "en": "Morocco", "iso": "MAR", "continent": "아프리카", "flag": "🇲🇦"},
    {"ko": "호주", "en": "Australia", "iso": "AUS", "continent": "오세아니아", "flag": "🇦🇺"},
    {"ko": "뉴질랜드", "en": "New Zealand", "iso": "NZL", "continent": "오세아니아", "flag": "🇳🇿"},
]
# =====================================================
# 1번 탭: 나라 맞추기 퀴즈
# =====================================================
with tab_quiz:

    if st.session_state.quiz_finished:
        st.markdown(
            f"""
            <div class="sparkle-box">
                <div class="sparkle-line">🎉 🌍 🎉</div>
                퀴즈 완료!<br>
                최종 정답: {st.session_state.quiz_correct_count} / {QUIZ_LENGTH}
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🔁 10문제 다시 풀기", use_container_width=True):
            st.session_state.quiz_finished = False
            start_new_quiz()
            st.rerun()

        st.stop()

    current = st.session_state.quiz_current

    map_data = pd.DataFrame([
        {
            "iso_alpha": current["iso"],
            "country": f"{current['ko']} / {current['en']}",
            "value": 1
        }
    ])

    qfig = px.choropleth(
        map_data,
        locations="iso_alpha",
        color="value",
        hover_name="country",
        color_continuous_scale=[[0, "#93c5fd"], [1, "#1d4ed8"]],
        projection="natural earth"
    )

    qfig.update_layout(
        height=720,
        margin=dict(l=0, r=0, t=0, b=0),
        coloraxis_showscale=False,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#475569",
            showcountries=True,
            countrycolor="#cbd5e1",
            showland=True,
            landcolor="#f8fafc",
            showocean=True,
            oceancolor="#e0f2fe",
            projection_type="natural earth"
        )
    )

    map_col, next_col = st.columns([5.2, 1])

    with map_col:
        st.plotly_chart(qfig, use_container_width=True, config={"displaylogo": False})

    with next_col:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        if st.session_state.quiz_answered:
            next_label = "➡️\n다음" if st.session_state.quiz_index < QUIZ_LENGTH - 1 else "🏁\n결과"
            if st.button(next_label, use_container_width=True, key="next_button_side"):
                next_quiz_question()
                st.rerun()
        else:
            st.markdown(
                """
                <div class="next-guide">
                    정답을 맞히면<br>➡️ 다음 버튼
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("## 정답을 골라 보세요")

    option_cols = st.columns(2)
    option_labels = ["A", "B", "C", "D"]

    safe_options = [
        o for o in st.session_state.get("quiz_options", [])
        if isinstance(o, dict) and o.get("iso")
    ]

    if len(safe_options) != 4:
        st.warning("퀴즈 선택지에 오류가 있어 새 문제를 다시 불러옵니다.")
        make_current_options()
        st.rerun()

    for i, option in enumerate(safe_options):
        with option_cols[i % 2]:
            ko_name = option.get("ko", "")
            en_name = option.get("en", "")
            iso_code = option.get("iso", str(i))
            button_label = f"{option_labels[i]}.  {ko_name}  /  {en_name}"
            if st.button(
                button_label,
                key=f"quiz_option_{i}_{iso_code}_{st.session_state.get('quiz_total', 0)}",
                use_container_width=True,
                disabled=st.session_state.quiz_answered
            ):
                check_quiz_answer(option)
                st.rerun()

    if st.session_state.quiz_result:
        if st.session_state.quiz_correct_flag:
            st.balloons()
            st.markdown(
                f"""
                <div class="sparkle-box">
                    <div class="sparkle-line">✨ 🎉 💥 🌟 ✨</div>
                    반짝! 정답입니다!<br>
                    {st.session_state.quiz_result}<br>
                    <span style="font-size:20px; color:#15803d;">대륙: {current.get('continent', '')}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="result-card">
                    {st.session_state.quiz_result}<br>
                    <span style="font-size:18px; color:#64748b;">같은 문제를 다시 풀어 보세요.</span>
                </div>
                """,
                unsafe_allow_html=True
            )


# =====================================================
# 2번 탭: 수업용 정리
# =====================================================
with tab_summary:
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

    st.markdown("---")
    st.markdown("### 🎮 나라 맞추기 퀴즈 활용 방법")
    st.markdown(
        """
        - `나라 맞추기 퀴즈` 탭에서 지도에 색칠된 나라의 이름을 고릅니다.
        - 정답을 맞히면 다음 문제로 넘어갈 수 있습니다.
        - 전체 세계지도, 바다, 강 이름은 `세계 지도 지식용` 탭에서 참고 자료로 확인합니다.
        - 정답을 맞히면 풍선과 반짝이는 축하 효과가 나옵니다.
        """
    )

st.caption("필요한 패키지: streamlit, plotly, pandas, countryinfo")
