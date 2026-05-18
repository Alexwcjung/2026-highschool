import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="한국·중국·미국·영국 역사 학습",
    page_icon="🌏",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .title-box {
        background: linear-gradient(135deg, #eff6ff 0%, #fef3c7 50%, #fee2e2 100%);
        border: 1.5px solid #dbeafe;
        border-radius: 28px;
        padding: 28px 30px;
        margin-bottom: 20px;
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
        line-height: 1.7;
    }
    .intro-box {
        background: #ffffff;
        border: 1.5px solid #e2e8f0;
        border-radius: 24px;
        padding: 22px 24px;
        margin-bottom: 18px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .intro-box h2 {
        margin: 0 0 10px 0;
        color: #1e3a8a;
        font-size: 30px;
        font-weight: 900;
    }
    .intro-box p {
        font-size: 17px;
        line-height: 1.75;
        color: #334155;
        font-weight: 650;
    }
    .founder-box {
        background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);
        border: 1.5px solid #fed7aa;
        border-radius: 24px;
        padding: 20px 22px;
        margin-bottom: 18px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .founder-box h3 {
        margin: 0 0 10px 0;
        color: #9a3412;
        font-size: 25px;
        font-weight: 900;
    }
    .founder-box p {
        font-size: 16px;
        line-height: 1.7;
        color: #334155;
        font-weight: 650;
    }
    .section-title {
        font-size: 25px;
        font-weight: 900;
        color: #0f172a;
        margin: 24px 0 12px 0;
    }
    .period-card {
        background: white;
        border: 1.5px solid #e2e8f0;
        border-radius: 22px;
        padding: 18px 20px;
        margin-bottom: 14px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        min-height: 250px;
    }
    .period-card h3 {
        margin: 0 0 8px 0;
        color: #111827;
        font-size: 22px;
        font-weight: 900;
    }
    .period-card .time {
        color: #2563eb;
        font-size: 15px;
        font-weight: 900;
        margin-bottom: 8px;
    }
    .period-card p {
        color: #334155;
        font-size: 15.5px;
        line-height: 1.65;
        font-weight: 650;
    }
    .event-card {
        background: #f8fafc;
        border: 1.5px solid #cbd5e1;
        border-radius: 18px;
        padding: 15px 17px;
        margin-bottom: 12px;
        min-height: 150px;
    }
    .event-card h4 {
        margin: 0 0 7px 0;
        color: #1e293b;
        font-size: 18px;
        font-weight: 900;
    }
    .event-card .date {
        color: #be123c;
        font-size: 14px;
        font-weight: 900;
        margin-bottom: 7px;
    }
    .event-card p {
        color: #334155;
        font-size: 15px;
        line-height: 1.6;
        font-weight: 650;
        margin: 0;
    }
    .tag {
        display: inline-block;
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        color: #334155;
        border-radius: 999px;
        padding: 6px 11px;
        margin: 4px;
        font-size: 13px;
        font-weight: 800;
    }
    .summary-box {
        background: #ecfdf5;
        border: 1.5px solid #bbf7d0;
        border-radius: 22px;
        padding: 18px 20px;
        margin-top: 14px;
        margin-bottom: 18px;
        color: #14532d;
        font-size: 16px;
        line-height: 1.75;
        font-weight: 750;
    }
    @media (max-width: 768px) {
        .title-box h1 { font-size: 30px; }
        .title-box p { font-size: 15px; }
        .intro-box h2 { font-size: 24px; }
        .intro-box p, .founder-box p, .period-card p, .event-card p { font-size: 14.5px; }
        .period-card, .event-card { min-height: auto; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 데이터
# =========================
HISTORY_DATA = {
    "한국": {
        "emoji": "🇰🇷",
        "title": "우리나라 역사",
        "intro": """
        우리나라 역사는 고조선에서 시작하여 삼국 시대, 고려, 조선, 대한제국, 일제강점기,
        대한민국으로 이어집니다. 핵심은 한반도와 그 주변 지역에서 여러 나라가 세워지고,
        외세의 침략과 내부 변화 속에서도 고유한 문화와 정체성을 이어 왔다는 점입니다.
        """,
        "founders": [
            {
                "name": "단군왕검",
                "role": "고조선 건국 인물",
                "detail": "고조선을 세운 인물로 전해집니다. 단군 이야기는 신화적 요소가 있지만, 우리 역사에서 최초 국가의 시작을 상징합니다."
            },
            {
                "name": "왕건",
                "role": "고려 건국 인물",
                "detail": "후삼국 시대를 통일하고 고려를 세웠습니다. 지방 세력과의 연합을 통해 새 왕조의 기반을 마련했습니다."
            },
            {
                "name": "이성계",
                "role": "조선 건국 인물",
                "detail": "고려 말 혼란 속에서 조선을 세웠습니다. 조선은 유교를 바탕으로 정치와 사회 질서를 정비했습니다."
            }
        ],
        "periods": [
            {
                "name": "고조선",
                "time": "기원전 2333년경으로 전해짐",
                "summary": "우리 역사에서 최초의 국가로 설명됩니다. 청동기 문화를 바탕으로 성장했고, 단군왕검의 건국 이야기와 연결됩니다.",
                "keywords": ["단군왕검", "최초의 국가", "청동기", "8조법"]
            },
            {
                "name": "삼국 시대",
                "time": "기원전 1세기경 ~ 7세기",
                "summary": "고구려, 백제, 신라가 경쟁하며 발전한 시기입니다. 각 나라는 불교를 받아들이고, 왕권을 강화하며, 독자적인 문화를 만들었습니다.",
                "keywords": ["고구려", "백제", "신라", "불교", "왕권 강화"]
            },
            {
                "name": "통일 신라와 발해",
                "time": "7세기 후반 ~ 10세기",
                "summary": "신라는 삼국을 통일했고, 북쪽에서는 고구려 계승 의식을 가진 발해가 성장했습니다. 남북국 시대라고도 부릅니다.",
                "keywords": ["통일 신라", "발해", "남북국", "불국사", "해동성국"]
            },
            {
                "name": "고려",
                "time": "918년 ~ 1392년",
                "summary": "왕건이 세운 나라입니다. 불교 문화가 발달했고, 거란과 몽골의 침입을 겪었습니다. 팔만대장경과 금속 활자가 대표적입니다.",
                "keywords": ["왕건", "불교", "팔만대장경", "금속 활자", "몽골 침입"]
            },
            {
                "name": "조선",
                "time": "1392년 ~ 1897년",
                "summary": "이성계가 세운 나라입니다. 유교를 바탕으로 정치와 사회 질서를 세웠고, 세종대왕 때 훈민정음이 창제되었습니다.",
                "keywords": ["이성계", "유교", "세종대왕", "훈민정음", "임진왜란"]
            },
            {
                "name": "대한제국과 일제강점기",
                "time": "1897년 ~ 1945년",
                "summary": "대한제국은 근대 국가를 지향했지만, 일본의 침략으로 국권을 빼앗겼습니다. 이후 독립운동이 국내외에서 활발히 일어났습니다.",
                "keywords": ["대한제국", "고종", "국권 침탈", "3·1 운동", "독립운동"]
            },
            {
                "name": "대한민국",
                "time": "1948년 ~ 현재",
                "summary": "광복 이후 대한민국 정부가 수립되었습니다. 전쟁과 가난을 겪었지만 민주화와 경제 성장을 이루며 오늘날의 대한민국으로 발전했습니다.",
                "keywords": ["광복", "정부 수립", "6·25 전쟁", "민주화", "경제 성장"]
            }
        ],
        "events": [
            {"date": "기원전 2333년경", "name": "고조선 건국", "detail": "단군왕검이 고조선을 세웠다고 전해지며, 우리 역사에서 최초 국가의 출발로 설명됩니다."},
            {"date": "668년", "name": "신라의 삼국 통일", "detail": "신라가 백제와 고구려를 차례로 무너뜨리며 한반도 대부분을 통합했습니다."},
            {"date": "918년", "name": "고려 건국", "detail": "왕건이 고려를 세우고 후삼국을 통일하여 새로운 왕조를 열었습니다."},
            {"date": "1392년", "name": "조선 건국", "detail": "이성계가 조선을 세웠고, 조선은 유교 중심의 국가 체제를 발전시켰습니다."},
            {"date": "1443년 / 1446년", "name": "훈민정음 창제와 반포", "detail": "세종대왕이 백성을 위해 훈민정음을 만들고 반포했습니다."},
            {"date": "1592년", "name": "임진왜란", "detail": "일본이 조선을 침략했고, 조선은 의병과 수군의 활약으로 나라를 지켜냈습니다."},
            {"date": "1910년", "name": "국권 피탈", "detail": "대한제국이 일본에 나라의 주권을 빼앗기고 일제강점기가 시작되었습니다."},
            {"date": "1919년", "name": "3·1 운동", "detail": "전국적으로 독립을 요구하는 만세 운동이 일어났고, 대한민국 임시정부 수립에도 영향을 주었습니다."},
            {"date": "1945년", "name": "광복", "detail": "일본의 패망으로 우리나라는 식민 지배에서 벗어났습니다."},
            {"date": "1950년", "name": "6·25 전쟁", "detail": "한반도에서 전쟁이 일어나 큰 피해를 입었고, 이후 남북 분단이 굳어졌습니다."}
        ],
        "summary": """
        우리나라 역사의 큰 흐름은 <b>고조선의 건국 → 삼국의 성장 → 고려와 조선의 발전 → 근대의 위기와 독립운동 → 대한민국의 성장</b>으로 정리할 수 있습니다.
        건국 인물로는 고조선의 <b>단군왕검</b>, 고려의 <b>왕건</b>, 조선의 <b>이성계</b>가 중요합니다.
        """
    },

    "중국": {
        "emoji": "🇨🇳",
        "title": "중국 역사",
        "intro": """
        중국 역사는 황허 문명에서 시작하여 여러 왕조가 흥망을 거듭한 역사입니다.
        넓은 영토와 많은 인구를 바탕으로 강력한 중앙집권 국가가 자주 등장했고,
        유교, 법가, 과거제, 황제 중심의 통치 체제가 오랫동안 중요한 역할을 했습니다.
        """,
        "founders": [
            {
                "name": "우왕",
                "role": "하나라 건국 인물로 전해짐",
                "detail": "중국 고대 전승에서 하왕조를 세운 인물로 알려져 있습니다. 홍수를 다스린 이야기와 연결됩니다."
            },
            {
                "name": "진시황",
                "role": "중국 최초 통일 제국의 건국 인물",
                "detail": "기원전 221년에 여러 나라로 나뉘어 있던 중국을 통일하고 진나라를 세웠습니다. 문자, 화폐, 도량형을 통일했습니다."
            },
            {
                "name": "마오쩌둥",
                "role": "중화인민공화국 수립 인물",
                "detail": "1949년 중화인민공화국 수립을 선포했습니다. 현대 중국의 출발과 관련된 핵심 인물입니다."
            }
        ],
        "periods": [
            {
                "name": "황허 문명과 은·주",
                "time": "기원전 약 2000년경 ~ 기원전 256년",
                "summary": "황허강 유역에서 문명이 발달했습니다. 은나라의 갑골문과 청동기 문화, 주나라의 봉건제가 중요합니다.",
                "keywords": ["황허", "갑골문", "청동기", "은나라", "주나라"]
            },
            {
                "name": "춘추전국 시대",
                "time": "기원전 770년 ~ 기원전 221년",
                "summary": "여러 나라가 경쟁하던 시기입니다. 전쟁은 많았지만, 공자와 맹자 같은 사상가가 등장하고 제자백가 사상이 발달했습니다.",
                "keywords": ["춘추전국", "제자백가", "공자", "맹자", "법가"]
            },
            {
                "name": "진",
                "time": "기원전 221년 ~ 기원전 206년",
                "summary": "진시황이 중국을 최초로 통일했습니다. 중앙집권 체제, 문자·화폐·도량형 통일, 만리장성 축조가 대표적입니다.",
                "keywords": ["진시황", "중국 통일", "중앙집권", "만리장성", "도량형 통일"]
            },
            {
                "name": "한",
                "time": "기원전 202년 ~ 220년",
                "summary": "중국 고대 제국의 기초를 다진 왕조입니다. 유교가 국가 통치 이념으로 자리 잡았고, 실크로드 교류가 활발했습니다.",
                "keywords": ["한나라", "유교", "실크로드", "무제", "장건"]
            },
            {
                "name": "수·당",
                "time": "581년 ~ 907년",
                "summary": "수나라는 중국을 다시 통일했고, 당나라는 국제적이고 개방적인 문화를 발전시켰습니다. 과거제가 정비되었습니다.",
                "keywords": ["수나라", "당나라", "과거제", "장안", "국제 문화"]
            },
            {
                "name": "송·원·명·청",
                "time": "960년 ~ 1912년",
                "summary": "송은 경제와 문화가 발달했고, 원은 몽골족이 세운 제국입니다. 명과 청은 강력한 황제 중심 국가였지만 서양 세력과 충돌했습니다.",
                "keywords": ["송", "원", "명", "청", "몽골", "황제 정치"]
            },
            {
                "name": "근현대 중국",
                "time": "1912년 ~ 현재",
                "summary": "신해혁명으로 청나라가 무너지고 중화민국이 세워졌습니다. 이후 내전과 혁명을 거쳐 1949년 중화인민공화국이 수립되었습니다.",
                "keywords": ["신해혁명", "쑨원", "중화민국", "마오쩌둥", "중화인민공화국"]
            }
        ],
        "events": [
            {"date": "기원전 약 1600년경", "name": "은나라 성립", "detail": "갑골문과 청동기 문화가 발달한 중국 고대 왕조입니다."},
            {"date": "기원전 770년 이후", "name": "춘추전국 시대", "detail": "여러 나라가 경쟁하면서 전쟁이 계속되었고, 제자백가 사상이 발달했습니다."},
            {"date": "기원전 221년", "name": "진시황의 중국 통일", "detail": "진시황이 중국을 최초로 통일하고 중앙집권적 제국을 세웠습니다."},
            {"date": "기원전 202년", "name": "한나라 건국", "detail": "유방이 한나라를 세웠고, 이후 유교와 관료제가 발전했습니다."},
            {"date": "581년", "name": "수나라의 통일", "detail": "분열되었던 중국을 다시 통일하고 대운하 건설 등 국가 기반을 정비했습니다."},
            {"date": "618년", "name": "당나라 건국", "detail": "당나라는 동아시아 국제 질서와 문화 교류의 중심이 되었습니다."},
            {"date": "1271년", "name": "원나라 성립", "detail": "몽골족이 중국을 지배하며 동서 교류가 확대되었습니다."},
            {"date": "1911년", "name": "신해혁명", "detail": "청나라가 무너지고 황제 중심의 왕조 체제가 끝나는 계기가 되었습니다."},
            {"date": "1949년", "name": "중화인민공화국 수립", "detail": "마오쩌둥이 중화인민공화국 수립을 선포하며 현대 중국이 시작되었습니다."}
        ],
        "summary": """
        중국 역사의 핵심은 <b>황허 문명 → 여러 왕조의 흥망 → 진시황의 통일 → 유교와 황제 중심 체제 → 근현대 혁명</b>입니다.
        건국 인물로는 <b>우왕</b>, <b>진시황</b>, <b>마오쩌둥</b>을 함께 정리할 수 있습니다.
        """
    },

    "미국": {
        "emoji": "🇺🇸",
        "title": "미국 역사",
        "intro": """
        미국 역사는 유럽인의 이주와 식민지 건설, 독립전쟁, 헌법 제정, 서부 개척,
        남북전쟁, 산업화, 세계 강대국으로의 성장으로 이어집니다.
        미국 역사의 중요한 특징은 자유, 독립, 민주주의, 이민, 개척 정신입니다.
        """,
        "founders": [
            {
                "name": "조지 워싱턴",
                "role": "미국 건국의 아버지",
                "detail": "독립전쟁에서 대륙군 총사령관으로 활약했고, 미국의 초대 대통령이 되었습니다. 권력을 내려놓는 전통을 세웠습니다."
            },
            {
                "name": "토머스 제퍼슨",
                "role": "독립선언서 작성 중심 인물",
                "detail": "1776년 독립선언서 작성에 중요한 역할을 했습니다. 자유와 권리라는 미국 건국 이념을 표현한 인물입니다."
            },
            {
                "name": "벤저민 프랭클린",
                "role": "외교와 건국 과정의 핵심 인물",
                "detail": "프랑스의 지원을 이끌어 내는 데 기여했고, 미국 독립과 헌법 제정 과정에 참여했습니다."
            }
        ],
        "periods": [
            {
                "name": "영국 식민지 시대",
                "time": "1607년 ~ 1776년",
                "summary": "영국인들이 북아메리카 동부에 식민지를 세웠습니다. 시간이 지나며 식민지 주민들은 영국의 세금과 통제에 불만을 갖게 되었습니다.",
                "keywords": ["제임스타운", "13개 식민지", "영국", "이주", "세금 문제"]
            },
            {
                "name": "독립전쟁과 미국 건국",
                "time": "1775년 ~ 1783년",
                "summary": "13개 식민지는 영국으로부터 독립하기 위해 전쟁을 벌였습니다. 1776년 독립선언서가 발표되었고, 전쟁 후 미국이 독립했습니다.",
                "keywords": ["독립전쟁", "독립선언서", "1776년", "조지 워싱턴", "토머스 제퍼슨"]
            },
            {
                "name": "헌법 제정과 초기 공화국",
                "time": "1787년 이후",
                "summary": "미국 헌법이 만들어지고 대통령제와 연방제의 기초가 세워졌습니다. 국민이 대표를 뽑는 공화국 체제가 발전했습니다.",
                "keywords": ["헌법", "연방제", "대통령제", "공화국", "권력 분립"]
            },
            {
                "name": "서부 개척",
                "time": "19세기",
                "summary": "미국은 서쪽으로 영토를 확장했습니다. 개척 정신이 강조되었지만, 원주민의 땅을 빼앗고 갈등을 일으킨 어두운 면도 있었습니다.",
                "keywords": ["서부 개척", "개척 정신", "원주민", "영토 확장", "골드러시"]
            },
            {
                "name": "남북전쟁",
                "time": "1861년 ~ 1865년",
                "summary": "노예제를 둘러싸고 북부와 남부가 전쟁을 벌였습니다. 링컨 대통령은 노예 해방을 추진했고, 전쟁 후 미국은 다시 하나의 나라로 유지되었습니다.",
                "keywords": ["남북전쟁", "노예제", "링컨", "노예 해방", "연방 유지"]
            },
            {
                "name": "산업화와 세계 강대국",
                "time": "19세기 후반 ~ 20세기",
                "summary": "철도, 공장, 대기업이 성장하며 미국은 산업 강국이 되었습니다. 두 차례 세계대전을 거치며 세계적인 영향력을 가진 나라가 되었습니다.",
                "keywords": ["산업화", "철도", "이민", "세계대전", "강대국"]
            },
            {
                "name": "현대 미국",
                "time": "20세기 후반 ~ 현재",
                "summary": "냉전, 시민권 운동, 정보기술 발전을 거치며 미국은 정치·경제·문화적으로 큰 영향력을 가진 나라가 되었습니다.",
                "keywords": ["냉전", "시민권 운동", "마틴 루터 킹", "IT 산업", "다문화 사회"]
            }
        ],
        "events": [
            {"date": "1607년", "name": "제임스타운 건설", "detail": "영국이 북아메리카에 세운 대표적인 초기 식민지입니다."},
            {"date": "1773년", "name": "보스턴 차 사건", "detail": "영국의 세금 정책에 반발한 식민지 주민들이 차를 바다에 버린 사건입니다."},
            {"date": "1776년", "name": "독립선언서 발표", "detail": "13개 식민지가 영국으로부터 독립을 선언했습니다."},
            {"date": "1787년", "name": "미국 헌법 제정", "detail": "연방제, 대통령제, 권력 분립을 바탕으로 한 국가 체제가 마련되었습니다."},
            {"date": "1803년", "name": "루이지애나 매입", "detail": "미국 영토가 크게 확장되었고 서부 개척의 기반이 되었습니다."},
            {"date": "1861년 ~ 1865년", "name": "남북전쟁", "detail": "노예제와 연방 문제를 둘러싸고 북부와 남부가 전쟁을 벌였습니다."},
            {"date": "1863년", "name": "노예 해방 선언", "detail": "링컨 대통령이 노예 해방을 선언하며 전쟁의 의미가 확대되었습니다."},
            {"date": "1929년", "name": "대공황", "detail": "경제가 크게 침체되며 미국 사회와 세계 경제에 큰 영향을 주었습니다."},
            {"date": "1950~1960년대", "name": "시민권 운동", "detail": "흑인 차별에 맞서 평등한 권리를 요구하는 운동이 활발히 전개되었습니다."}
        ],
        "summary": """
        미국 역사의 흐름은 <b>식민지 → 독립전쟁 → 헌법과 공화국 → 서부 개척 → 남북전쟁 → 산업화와 세계 강대국</b>으로 정리할 수 있습니다.
        건국 인물로는 <b>조지 워싱턴</b>, <b>토머스 제퍼슨</b>, <b>벤저민 프랭클린</b>이 중요합니다.
        """
    },

    "영국": {
        "emoji": "🇬🇧",
        "title": "영국 역사",
        "intro": """
        영국 역사는 여러 민족의 이동과 왕국 형성, 의회 정치의 발달, 산업혁명,
        대영제국의 성장, 현대 입헌군주제로 이어집니다.
        영국의 중요한 특징은 왕권과 의회 사이의 갈등 속에서 의회 민주주의가 발전했다는 점입니다.
        """,
        "founders": [
            {
                "name": "앨프레드 대왕",
                "role": "잉글랜드 형성의 기초를 닦은 인물",
                "detail": "바이킹의 침입에 맞서 웨식스를 지켰고, 잉글랜드 통합의 기반을 마련한 인물로 평가됩니다."
            },
            {
                "name": "윌리엄 1세",
                "role": "노르만 왕조의 시작 인물",
                "detail": "1066년 노르만 정복을 통해 잉글랜드를 지배하게 되었고, 봉건제와 중앙 통치를 강화했습니다."
            },
            {
                "name": "헨리 7세",
                "role": "튜더 왕조의 시작 인물",
                "detail": "장미전쟁 이후 튜더 왕조를 열고 왕권을 안정시켰습니다. 이후 영국의 국가 체제가 점차 강화되었습니다."
            }
        ],
        "periods": [
            {
                "name": "고대 브리튼과 로마 지배",
                "time": "기원전 ~ 5세기",
                "summary": "브리튼섬에는 켈트족이 살고 있었고, 이후 로마 제국이 일부 지역을 지배했습니다. 로마의 도로와 도시 문화가 전해졌습니다.",
                "keywords": ["켈트족", "로마 제국", "브리튼", "도로", "도시"]
            },
            {
                "name": "앵글로색슨 왕국",
                "time": "5세기 ~ 1066년",
                "summary": "앵글족과 색슨족이 이주하여 여러 왕국을 세웠습니다. 앨프레드 대왕은 바이킹에 맞서고 잉글랜드 통합의 기초를 마련했습니다.",
                "keywords": ["앵글로색슨", "웨식스", "앨프레드 대왕", "바이킹", "잉글랜드"]
            },
            {
                "name": "노르만 정복",
                "time": "1066년",
                "summary": "노르망디 공작 윌리엄이 잉글랜드를 정복했습니다. 이후 봉건제와 성 건축, 프랑스 문화의 영향이 강해졌습니다.",
                "keywords": ["1066년", "윌리엄 1세", "노르만 정복", "봉건제", "성"]
            },
            {
                "name": "마그나 카르타와 의회 발전",
                "time": "1215년 이후",
                "summary": "마그나 카르타는 왕의 권력을 제한하는 중요한 문서였습니다. 이후 귀족과 시민의 대표가 참여하는 의회 정치가 점차 발달했습니다.",
                "keywords": ["마그나 카르타", "왕권 제한", "의회", "법의 지배", "시민 대표"]
            },
            {
                "name": "튜더 왕조와 종교개혁",
                "time": "1485년 ~ 1603년",
                "summary": "튜더 왕조 시기 왕권이 강화되었고, 헨리 8세 때 영국 국교회가 성립했습니다. 엘리자베스 1세 때 해상 활동이 활발해졌습니다.",
                "keywords": ["튜더 왕조", "헨리 8세", "영국 국교회", "엘리자베스 1세", "해상 활동"]
            },
            {
                "name": "시민혁명과 입헌정치",
                "time": "17세기",
                "summary": "왕권과 의회가 충돌했고, 청교도 혁명과 명예혁명을 거치며 의회의 권한이 강화되었습니다.",
                "keywords": ["청교도 혁명", "크롬웰", "명예혁명", "권리장전", "입헌군주제"]
            },
            {
                "name": "산업혁명과 대영제국",
                "time": "18세기 후반 ~ 20세기 초",
                "summary": "영국에서 산업혁명이 시작되어 공장제와 기계 생산이 발달했습니다. 이후 넓은 식민지를 가진 대영제국으로 성장했습니다.",
                "keywords": ["산업혁명", "증기기관", "공장", "식민지", "대영제국"]
            },
            {
                "name": "현대 영국",
                "time": "20세기 ~ 현재",
                "summary": "세계대전을 겪은 뒤 제국은 약화되었지만, 영국은 의회 민주주의와 문화, 금융 중심지로 영향력을 유지하고 있습니다.",
                "keywords": ["세계대전", "복지국가", "의회 민주주의", "영연방", "런던"]
            }
        ],
        "events": [
            {"date": "43년", "name": "로마의 브리튼 지배 시작", "detail": "로마 제국이 브리튼 일부를 지배하며 도시와 도로 문화가 전해졌습니다."},
            {"date": "878년경", "name": "앨프레드 대왕의 바이킹 격퇴", "detail": "앨프레드 대왕은 바이킹에 맞서 웨식스를 지키고 잉글랜드 통합의 기반을 마련했습니다."},
            {"date": "1066년", "name": "노르만 정복", "detail": "윌리엄 1세가 잉글랜드를 정복하고 노르만 왕조를 열었습니다."},
            {"date": "1215년", "name": "마그나 카르타", "detail": "왕의 권력을 제한하고 법의 지배 원리를 발전시키는 데 영향을 주었습니다."},
            {"date": "1534년", "name": "수장령", "detail": "헨리 8세가 영국 국교회의 수장이 되며 영국 종교개혁이 본격화되었습니다."},
            {"date": "1642년 ~ 1649년", "name": "청교도 혁명", "detail": "왕권과 의회가 충돌했고, 찰스 1세가 처형되는 큰 변화가 일어났습니다."},
            {"date": "1688년", "name": "명예혁명", "detail": "피를 거의 흘리지 않고 왕이 교체되었고, 의회의 권한이 강화되었습니다."},
            {"date": "1689년", "name": "권리장전", "detail": "왕권을 제한하고 의회 중심의 입헌군주제가 발전하는 계기가 되었습니다."},
            {"date": "18세기 후반", "name": "산업혁명", "detail": "증기기관과 공장제 생산이 발달하며 사회와 경제가 크게 바뀌었습니다."},
            {"date": "19세기", "name": "대영제국의 확대", "detail": "영국은 세계 여러 지역에 식민지를 두며 강력한 제국으로 성장했습니다."}
        ],
        "summary": """
        영국 역사는 <b>여러 민족의 이동 → 잉글랜드 형성 → 왕권과 의회의 갈등 → 입헌군주제 → 산업혁명과 대영제국</b>으로 정리할 수 있습니다.
        건국적 인물로는 <b>앨프레드 대왕</b>, <b>윌리엄 1세</b>, <b>헨리 7세</b>를 함께 볼 수 있습니다.
        """
    }
}

# =========================
# 출력 함수
# =========================
def show_history(country_name, data):
    st.markdown(
        f"""
        <div class="intro-box">
            <h2>{data['emoji']} {data['title']}</h2>
            <p>{data['intro']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='section-title'>👤 건국 인물 / 나라 형성의 핵심 인물</div>", unsafe_allow_html=True)
    for founder in data["founders"]:
        st.markdown(
            f"""
            <div class="founder-box">
                <h3>{founder['name']} — {founder['role']}</h3>
                <p>{founder['detail']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div class='section-title'>🕰️ 시대 흐름</div>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, period in enumerate(data["periods"]):
        with cols[i % 2]:
            tags = "".join([f"<span class='tag'>{kw}</span>" for kw in period["keywords"]])
            st.markdown(
                f"""
                <div class="period-card">
                    <h3>{period['name']}</h3>
                    <div class="time">{period['time']}</div>
                    <p>{period['summary']}</p>
                    <div>{tags}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div class='section-title'>📌 주요 사건</div>", unsafe_allow_html=True)
    event_cols = st.columns(2)
    for i, event in enumerate(data["events"]):
        with event_cols[i % 2]:
            st.markdown(
                f"""
                <div class="event-card">
                    <h4>{event['name']}</h4>
                    <div class="date">{event['date']}</div>
                    <p>{event['detail']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        f"""
        <div class="summary-box">
            <b>핵심 정리</b><br>
            {data['summary']}
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 제목
# =========================
st.markdown(
    """
    <div class="title-box">
        <h1>🌏 한국·중국·미국·영국 역사 학습</h1>
        <p>
            네 나라의 역사를 탭별로 살펴봅니다.<br>
            각 나라의 <b>건국 인물</b>, <b>시대 흐름</b>, <b>주요 사건</b>, <b>핵심 정리</b>를 한눈에 확인할 수 있습니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

tab_korea, tab_china, tab_usa, tab_uk = st.tabs([
    "🇰🇷 한국 역사",
    "🇨🇳 중국 역사",
    "🇺🇸 미국 역사",
    "🇬🇧 영국 역사"
])

with tab_korea:
    show_history("한국", HISTORY_DATA["한국"])

with tab_china:
    show_history("중국", HISTORY_DATA["중국"])

with tab_usa:
    show_history("미국", HISTORY_DATA["미국"])

with tab_uk:
    show_history("영국", HISTORY_DATA["영국"])

st.caption("필요 패키지: streamlit")
