import streamlit as st
import random

st.set_page_config(
    page_title="중국 역사와 근현대사",
    page_icon="🐉",
    layout="wide"
)

# =====================================================
# 전체 흐름
# =====================================================
HISTORY_FLOW = [
    {
        "name": "선사·신화 시대",
        "emoji": "🪨",
        "years": "문자 기록 이전 ~ 전설 시대",
        "one": "황하 문명과 전설 속 성군",
    },
    {
        "name": "하·상·주",
        "emoji": "🏺",
        "years": "기원전 약 21세기 ~ 기원전 256년",
        "one": "초기 왕조와 봉건 질서",
    },
    {
        "name": "춘추전국",
        "emoji": "⚔️",
        "years": "기원전 770년 ~ 기원전 221년",
        "one": "제후국 경쟁과 제자백가",
    },
    {
        "name": "진",
        "emoji": "🧱",
        "years": "기원전 221년 ~ 기원전 206년",
        "one": "중국 최초의 통일 제국",
    },
    {
        "name": "한",
        "emoji": "🐎",
        "years": "기원전 202년 ~ 220년",
        "one": "유교 국가 기틀과 실크로드",
    },
    {
        "name": "위진남북조",
        "emoji": "🌫️",
        "years": "220년 ~ 589년",
        "one": "분열과 민족 이동",
    },
    {
        "name": "수·당",
        "emoji": "🌏",
        "years": "581년 ~ 907년",
        "one": "재통일과 국제적 문화",
    },
    {
        "name": "송·원",
        "emoji": "📚",
        "years": "960년 ~ 1368년",
        "one": "상업 발달과 몽골 제국",
    },
    {
        "name": "명·청",
        "emoji": "🏯",
        "years": "1368년 ~ 1912년",
        "one": "황제 지배의 마지막 전성기와 쇠퇴",
    },
    {
        "name": "근현대",
        "emoji": "🇨🇳",
        "years": "1840년 아편전쟁 이후 ~ 현재",
        "one": "제국의 붕괴와 현대 국가 형성",
    },
]

# =====================================================
# 고대~청 설명
# - 건국 인물은 별도 탭으로 분리하지 않고, 2번째 탭에 함께 표시합니다.
# =====================================================
PREMODERN_PERIODS = [
    {
        "name": "선사·신화 시대",
        "emoji": "🪨",
        "years": "문자 기록 이전 ~ 전설 시대",
        "period": "황하 문명과 전설 속 성군",
        "founders": [
            {
                "person": "황제",
                "role": "중국 문명의 시조로 여겨지는 전설적 인물",
                "explain": "중국인들이 자신의 문화적 뿌리를 설명할 때 자주 언급하는 상징적 인물입니다."
            },
            {
                "person": "요·순",
                "role": "이상적인 성군으로 전해지는 인물",
                "explain": "덕으로 나라를 다스리고 훌륭한 인물에게 왕위를 넘겼다는 이야기가 전해집니다."
            }
        ],
        "core": "황하 유역을 중심으로 농경이 발달하고, 중국 문명의 기초가 형성되었다고 설명되는 시기입니다.",
        "details": [
            "황하 유역은 중국 문명의 중요한 발상지로 여겨집니다.",
            "전설 속 황제는 중국 문명의 시조로 자주 언급됩니다.",
            "요와 순은 덕으로 나라를 다스린 이상적인 군주로 전해집니다.",
            "이 시기는 역사 기록보다 전설과 신화가 많이 섞여 있습니다."
        ],
        "keywords": ["황하 문명", "황제", "요", "순", "농경", "전설"]
    },
    {
        "name": "하·상·주",
        "emoji": "🏺",
        "years": "기원전 약 21세기 ~ 기원전 256년",
        "period": "초기 왕조의 성립",
        "founders": [
            {
                "person": "우왕",
                "role": "하나라 건국 인물로 전해짐",
                "explain": "홍수를 다스렸다는 이야기와 함께 하 왕조의 시작과 연결됩니다."
            },
            {
                "person": "탕왕",
                "role": "상나라 건국 인물",
                "explain": "하나라의 폭정을 무너뜨리고 상나라를 세운 인물로 전해집니다."
            },
            {
                "person": "무왕",
                "role": "주나라 건국 인물",
                "explain": "상나라를 무너뜨리고 주 왕조를 세웠으며, 봉건 제도와 연결됩니다."
            }
        ],
        "core": "초기 왕조가 등장하고, 청동기 문화와 봉건 질서가 발전한 시기입니다.",
        "details": [
            "하나라는 중국 최초의 왕조로 전해지지만, 전설적 성격도 강합니다.",
            "상나라는 갑골문과 청동기 문화로 잘 알려져 있습니다.",
            "주나라는 봉건 제도를 통해 넓은 지역을 다스렸습니다.",
            "주나라 말에는 왕권이 약해지고 제후들의 힘이 강해졌습니다."
        ],
        "keywords": ["하", "상", "주", "우왕", "탕왕", "무왕", "갑골문", "청동기", "봉건제"]
    },
    {
        "name": "춘추전국 시대",
        "emoji": "⚔️",
        "years": "기원전 770년 ~ 기원전 221년",
        "period": "제후국 경쟁과 사상 발전",
        "founders": [
            {
                "person": "공자",
                "role": "유가 사상의 대표 인물",
                "explain": "인의와 예를 중시했고, 이후 중국 정치와 교육에 큰 영향을 주었습니다."
            },
            {
                "person": "노자",
                "role": "도가 사상의 대표 인물",
                "explain": "자연스러운 삶과 무위자연을 강조한 인물로 알려져 있습니다."
            },
            {
                "person": "한비자",
                "role": "법가 사상의 대표 인물",
                "explain": "강한 법과 제도를 통해 나라를 다스려야 한다고 보았습니다."
            }
        ],
        "core": "여러 제후국이 경쟁하면서 전쟁이 많았지만, 동시에 다양한 사상이 꽃핀 시대입니다.",
        "details": [
            "주 왕실의 힘이 약해지고 여러 제후국이 서로 경쟁했습니다.",
            "철기 사용과 농업 생산력의 증가로 사회가 크게 변화했습니다.",
            "공자, 맹자, 노자, 장자, 한비자 등 여러 사상가가 등장했습니다.",
            "이 시기의 다양한 사상을 제자백가라고 부릅니다."
        ],
        "keywords": ["춘추", "전국", "제후국", "제자백가", "공자", "노자", "한비자", "철기"]
    },
    {
        "name": "진",
        "emoji": "🧱",
        "years": "기원전 221년 ~ 기원전 206년",
        "period": "중국 최초의 통일 제국",
        "founders": [
            {
                "person": "진시황",
                "role": "진나라 황제, 중국 최초 통일 제국의 군주",
                "explain": "전국 시대를 끝내고 중국을 통일했으며, 황제라는 칭호를 사용했습니다."
            }
        ],
        "core": "진시황이 중국을 통일하고 중앙집권 체제를 강하게 만든 시기입니다.",
        "details": [
            "진시황은 전국 시대를 끝내고 중국을 통일했습니다.",
            "문자, 화폐, 도량형을 통일하여 제국 운영의 기초를 마련했습니다.",
            "만리장성 건설과 엄격한 법가 통치로 유명합니다.",
            "강한 통치 방식 때문에 오래 지속되지는 못했습니다."
        ],
        "keywords": ["진시황", "중국 통일", "중앙집권", "문자 통일", "화폐 통일", "도량형", "만리장성", "법가"]
    },
    {
        "name": "한",
        "emoji": "🐎",
        "years": "기원전 202년 ~ 220년",
        "period": "유교 국가의 기틀",
        "founders": [
            {
                "person": "유방",
                "role": "한나라 건국 인물",
                "explain": "진나라 멸망 이후 항우와의 경쟁에서 승리하고 한나라를 세웠습니다."
            },
            {
                "person": "한 무제",
                "role": "한나라 전성기를 이끈 황제",
                "explain": "영토 확장과 유교 중심 통치 체제 확립에 중요한 역할을 했습니다."
            }
        ],
        "core": "유방이 세운 한나라는 유교를 국가 운영의 중요한 원리로 삼고, 실크로드를 통해 동서 교류를 확대했습니다.",
        "details": [
            "유방은 한나라를 세우고 제국을 안정시켰습니다.",
            "한 무제 시기에는 영토가 확장되고 국력이 강해졌습니다.",
            "유교가 국가 통치의 중요한 사상으로 자리 잡았습니다.",
            "장건의 서역 파견 이후 실크로드 교류가 활발해졌습니다."
        ],
        "keywords": ["유방", "한 무제", "유교", "장건", "실크로드", "서역", "중앙집권"]
    },
    {
        "name": "위진남북조",
        "emoji": "🌫️",
        "years": "220년 ~ 589년",
        "period": "분열과 민족 이동",
        "founders": [
            {
                "person": "조조",
                "role": "위나라 기반을 닦은 인물",
                "explain": "후한 말 혼란 속에서 북중국을 장악하고 위나라 성립의 기반을 마련했습니다."
            },
            {
                "person": "유비",
                "role": "촉한의 건국 인물",
                "explain": "삼국지의 주요 인물로, 촉한을 세웠습니다."
            },
            {
                "person": "손권",
                "role": "오나라의 건국 인물",
                "explain": "강남 지역을 기반으로 오나라를 세웠습니다."
            }
        ],
        "core": "한나라가 멸망한 뒤 중국이 여러 나라로 나뉘고, 북방 민족의 이동과 불교 확산이 활발했던 시기입니다.",
        "details": [
            "삼국 시대에는 위·촉·오가 경쟁했습니다.",
            "이후에도 남북으로 여러 왕조가 나뉘어 존재했습니다.",
            "북방 민족이 중국 북부에 들어와 새로운 왕조를 세웠습니다.",
            "불교가 널리 퍼지고 귀족 문화가 발달했습니다."
        ],
        "keywords": ["위", "촉", "오", "조조", "유비", "손권", "남북조", "불교", "민족 이동"]
    },
    {
        "name": "수·당",
        "emoji": "🌏",
        "years": "581년 ~ 907년",
        "period": "재통일과 국제적 문화",
        "founders": [
            {
                "person": "양견",
                "role": "수나라 건국 인물",
                "explain": "오랜 분열을 끝내고 중국을 다시 통일했습니다."
            },
            {
                "person": "이연",
                "role": "당나라 건국 인물",
                "explain": "수나라 말 혼란 속에서 당나라를 세웠습니다."
            },
            {
                "person": "당 태종",
                "role": "당나라 전성기의 기초를 닦은 황제",
                "explain": "정관의 치라고 불리는 안정된 정치를 이끌었습니다."
            }
        ],
        "core": "수나라가 중국을 재통일하고, 당나라는 국제적이고 개방적인 문화를 발전시킨 시기입니다.",
        "details": [
            "수나라는 오랜 분열을 끝내고 중국을 다시 통일했습니다.",
            "수 양제 때 대운하가 정비되었지만, 무리한 토목 공사와 전쟁으로 민심을 잃었습니다.",
            "당나라는 장안을 중심으로 국제적인 문화를 발전시켰습니다.",
            "당 태종 시기에는 정치가 안정되고 국력이 강해졌습니다.",
            "과거제가 발전하여 관리 선발 제도로 자리 잡았습니다."
        ],
        "keywords": ["수", "당", "양견", "이연", "당 태종", "대운하", "장안", "과거제", "국제 문화"]
    },
    {
        "name": "송·원",
        "emoji": "📚",
        "years": "960년 ~ 1368년",
        "period": "상업 발달과 몽골 제국",
        "founders": [
            {
                "person": "조광윤",
                "role": "송나라 건국 인물",
                "explain": "송나라를 세우고 문치주의적 통치의 기초를 마련했습니다."
            },
            {
                "person": "쿠빌라이 칸",
                "role": "원나라 건국 인물",
                "explain": "몽골 제국의 지배를 바탕으로 중국에 원나라를 세웠습니다."
            }
        ],
        "core": "송나라에서는 상업과 도시 문화가 발달했고, 원나라는 몽골족이 세운 세계 제국의 성격을 지녔습니다.",
        "details": [
            "송나라는 문치주의와 과거제를 중시했습니다.",
            "상업과 도시가 발달하고 화폐 경제가 성장했습니다.",
            "성리학이 발전하여 이후 동아시아 사상에 큰 영향을 주었습니다.",
            "원나라는 쿠빌라이 칸이 세운 왕조로, 몽골 제국과 연결되어 있었습니다.",
            "동서 교류가 활발해지고 마르코 폴로 같은 서양인도 중국을 방문했습니다."
        ],
        "keywords": ["송", "원", "조광윤", "쿠빌라이 칸", "문치주의", "상업", "성리학", "몽골", "동서 교류"]
    },
    {
        "name": "명·청",
        "emoji": "🏯",
        "years": "1368년 ~ 1912년",
        "period": "황제 지배의 마지막 전성기와 쇠퇴",
        "founders": [
            {
                "person": "주원장",
                "role": "명나라 건국 인물",
                "explain": "원나라를 몰아내고 한족 왕조인 명나라를 세웠습니다."
            },
            {
                "person": "누르하치",
                "role": "후금 건국 인물",
                "explain": "만주족 세력을 통합하여 청나라의 기반을 닦았습니다."
            },
            {
                "person": "홍타이지",
                "role": "청나라 국호를 사용한 인물",
                "explain": "후금을 청으로 바꾸고 청 왕조의 체제를 정비했습니다."
            }
        ],
        "core": "명나라는 한족 왕조로 황제권을 강화했고, 청나라는 만주족이 세운 왕조로 넓은 영토를 다스렸습니다.",
        "details": [
            "명나라는 주원장이 세웠고, 황제 중심의 통치를 강화했습니다.",
            "정화의 원정처럼 대외 교류가 이루어지기도 했습니다.",
            "청나라는 만주족이 세운 왕조로 강희제, 옹정제, 건륭제 시기에 전성기를 맞았습니다.",
            "청 말에는 아편전쟁과 서양 열강의 압력으로 위기를 겪었습니다.",
            "1911년 신해혁명 이후 청 왕조는 무너지고 황제 지배가 끝났습니다."
        ],
        "keywords": ["명", "청", "주원장", "누르하치", "홍타이지", "정화", "강희제", "건륭제", "아편전쟁", "신해혁명"]
    },
]

# =====================================================
# 근현대사 세부 단계
# =====================================================
MODERN_STEPS = [
    {
        "title": "아편전쟁과 불평등 조약",
        "years": "1840년 ~ 1842년",
        "emoji": "🚢",
        "summary": "청나라는 영국과의 아편전쟁에서 패배하고 난징조약을 맺었습니다.",
        "details": [
            "아편 무역 문제와 무역 갈등이 전쟁의 배경이 되었습니다.",
            "난징조약으로 홍콩을 영국에 넘기고 항구를 개방했습니다.",
            "이후 중국은 서양 열강의 압력을 크게 받게 되었습니다."
        ],
        "keywords": ["아편전쟁", "난징조약", "홍콩", "불평등 조약"]
    },
    {
        "title": "태평천국 운동",
        "years": "1851년 ~ 1864년",
        "emoji": "🔥",
        "summary": "청 말 사회 혼란 속에서 대규모 농민 반란이 일어났습니다.",
        "details": [
            "홍수전이 태평천국을 세우고 청 왕조에 맞섰습니다.",
            "토지 균등과 새로운 사회 질서를 내세웠습니다.",
            "오랜 내전으로 중국 사회에 큰 피해가 발생했습니다."
        ],
        "keywords": ["태평천국", "홍수전", "농민 반란", "청 말 혼란"]
    },
    {
        "title": "양무운동과 변법자강운동",
        "years": "19세기 후반",
        "emoji": "⚙️",
        "summary": "청나라는 서양 기술을 받아들여 나라를 강화하려 했습니다.",
        "details": [
            "양무운동은 서양의 군사 기술과 산업 기술을 받아들이려 했습니다.",
            "변법자강운동은 제도 개혁까지 추진하려 했습니다.",
            "그러나 보수 세력의 반대와 한계로 큰 성과를 내지 못했습니다."
        ],
        "keywords": ["양무운동", "변법자강운동", "서양 기술", "개혁"]
    },
    {
        "title": "신해혁명과 중화민국",
        "years": "1911년 ~ 1912년",
        "emoji": "🌅",
        "summary": "신해혁명으로 청 왕조가 무너지고 중화민국이 세워졌습니다.",
        "details": [
            "쑨원은 혁명 운동의 상징적 지도자였습니다.",
            "황제 지배가 끝나고 공화국 체제가 시작되었습니다.",
            "하지만 이후 군벌의 분열과 정치 혼란이 계속되었습니다."
        ],
        "keywords": ["신해혁명", "쑨원", "중화민국", "공화국", "청 멸망"]
    },
    {
        "title": "5·4 운동",
        "years": "1919년",
        "emoji": "📣",
        "summary": "학생과 지식인들이 제국주의와 낡은 질서에 반대하며 새로운 문화를 요구했습니다.",
        "details": [
            "베이징 학생들을 중심으로 반제국주의 운동이 일어났습니다.",
            "민주주의와 과학을 강조하는 신문화 운동과 연결되었습니다.",
            "중국 현대 사상과 정치 운동에 큰 영향을 주었습니다."
        ],
        "keywords": ["5·4 운동", "반제국주의", "신문화 운동", "민주주의", "과학"]
    },
    {
        "title": "국공내전과 중화인민공화국 수립",
        "years": "1927년 ~ 1949년",
        "emoji": "🪖",
        "summary": "국민당과 공산당의 대립 끝에 1949년 중화인민공화국이 수립되었습니다.",
        "details": [
            "국민당과 공산당은 협력과 대립을 반복했습니다.",
            "일본의 침략에 맞서는 항일 전쟁도 중요한 배경이었습니다.",
            "1949년 마오쩌둥은 중화인민공화국 수립을 선언했습니다.",
            "장제스의 국민당 정부는 타이완으로 이동했습니다."
        ],
        "keywords": ["국공내전", "국민당", "공산당", "마오쩌둥", "장제스", "중화인민공화국", "타이완"]
    },
    {
        "title": "대약진운동과 문화대혁명",
        "years": "1958년 ~ 1976년",
        "emoji": "🌪️",
        "summary": "급진적인 사회주의 정책과 정치 운동으로 큰 혼란이 발생했습니다.",
        "details": [
            "대약진운동은 빠른 경제 성장을 목표로 했지만 큰 실패와 피해를 낳았습니다.",
            "문화대혁명은 사회와 문화, 교육, 정치에 큰 혼란을 가져왔습니다.",
            "이 시기는 현대 중국사에서 매우 중요한 반성의 대상입니다."
        ],
        "keywords": ["대약진운동", "문화대혁명", "마오쩌둥", "사회 혼란"]
    },
    {
        "title": "개혁개방",
        "years": "1978년 이후",
        "emoji": "🏭",
        "summary": "덩샤오핑을 중심으로 시장 요소를 받아들이며 경제 성장이 시작되었습니다.",
        "details": [
            "농촌과 도시에서 경제 개혁이 추진되었습니다.",
            "외국 자본과 기술을 받아들이고 특구가 만들어졌습니다.",
            "중국 경제는 빠르게 성장하며 세계 경제와 깊이 연결되었습니다."
        ],
        "keywords": ["개혁개방", "덩샤오핑", "경제특구", "시장 경제", "경제 성장"]
    },
    {
        "title": "오늘날 중국",
        "years": "2000년대 이후",
        "emoji": "🌐",
        "summary": "중국은 세계 경제와 국제 정치에서 큰 영향력을 가진 국가가 되었습니다.",
        "details": [
            "제조업, 기술, 무역, 인프라 분야에서 큰 성장을 이루었습니다.",
            "세계 여러 나라와 경제적으로 밀접하게 연결되어 있습니다.",
            "경제 성장, 사회 안정, 국제 관계, 인권과 표현의 자유 문제 등 다양한 과제를 안고 있습니다."
        ],
        "keywords": ["세계 경제", "기술 발전", "무역", "국제 관계", "현대 중국"]
    },
]

# =====================================================
# 주요 인물 정리
# =====================================================
IMPORTANT_PEOPLE = [
    {
        "name": "황제",
        "period": "선사·신화 시대",
        "main": "중국 문명의 시조로 여겨지는 전설적 인물",
        "points": ["중국 문화의 기원 설명", "전설적 존재", "황하 문명과 연결"],
        "note": "역사 기록이라기보다 문화적 상징으로 이해하는 것이 좋습니다."
    },
    {
        "name": "공자",
        "period": "춘추 시대",
        "main": "유가 사상의 대표 인물",
        "points": ["인의와 예 강조", "교육 중시", "동아시아 정치와 윤리에 큰 영향"],
        "note": "중국뿐 아니라 한국, 일본, 베트남에도 큰 영향을 주었습니다."
    },
    {
        "name": "진시황",
        "period": "진",
        "main": "중국 최초 통일 제국의 황제",
        "points": ["중국 통일", "문자·화폐·도량형 통일", "만리장성"],
        "note": "통일의 업적과 강압적 통치가 함께 평가됩니다."
    },
    {
        "name": "유방",
        "period": "한",
        "main": "한나라 건국 인물",
        "points": ["한나라 건국", "항우와의 경쟁에서 승리", "제국 안정"],
        "note": "평민 출신 황제로 자주 설명됩니다."
    },
    {
        "name": "한 무제",
        "period": "한",
        "main": "한나라 전성기를 이끈 황제",
        "points": ["영토 확장", "유교 통치 강화", "실크로드 교류 확대"],
        "note": "강한 국가 운영과 대외 확장의 대표 인물입니다."
    },
    {
        "name": "조조",
        "period": "위진남북조",
        "main": "위나라 기반을 닦은 인물",
        "points": ["후한 말 북중국 장악", "삼국 시대 핵심 인물", "정치와 군사 능력"],
        "note": "소설 『삼국지연의』의 이미지와 실제 역사 인물은 구분할 필요가 있습니다."
    },
    {
        "name": "당 태종",
        "period": "당",
        "main": "당나라 전성기의 기초를 닦은 황제",
        "points": ["정관의 치", "정치 안정", "국제적 당 문화 발전"],
        "note": "중국사에서 이상적인 군주 중 한 명으로 자주 언급됩니다."
    },
    {
        "name": "쿠빌라이 칸",
        "period": "원",
        "main": "원나라 건국 인물",
        "points": ["몽골 제국과 중국 지배 연결", "원나라 수립", "동서 교류 확대"],
        "note": "몽골 제국의 세계사적 흐름과 함께 이해하면 좋습니다."
    },
    {
        "name": "주원장",
        "period": "명",
        "main": "명나라 건국 인물",
        "points": ["원나라를 몰아냄", "명나라 건국", "황제권 강화"],
        "note": "가난한 출신에서 황제가 된 인물로 알려져 있습니다."
    },
    {
        "name": "누르하치",
        "period": "청",
        "main": "청나라의 기반을 닦은 인물",
        "points": ["만주족 세력 통합", "후금 건국", "팔기제 정비"],
        "note": "청나라 성립의 출발점이 되는 인물입니다."
    },
    {
        "name": "쑨원",
        "period": "근대",
        "main": "중화민국 건국의 아버지로 불리는 인물",
        "points": ["신해혁명", "삼민주의", "공화정 추진"],
        "note": "현대 중국과 타이완 모두에서 중요한 인물로 평가됩니다."
    },
    {
        "name": "마오쩌둥",
        "period": "현대",
        "main": "중화인민공화국 수립의 중심 인물",
        "points": ["공산당 지도자", "1949년 중화인민공화국 수립", "대약진운동과 문화대혁명"],
        "note": "중국 현대사의 핵심 인물이지만 정책의 성과와 피해를 함께 보아야 합니다."
    },
    {
        "name": "덩샤오핑",
        "period": "현대",
        "main": "개혁개방을 이끈 지도자",
        "points": ["1978년 이후 개혁개방", "경제특구", "시장 요소 도입"],
        "note": "오늘날 중국 경제 성장의 방향을 만든 인물로 자주 설명됩니다."
    },
]

# =====================================================
# 퀴즈
# =====================================================
if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "quiz_mode" not in st.session_state:
    st.session_state.quiz_mode = "흐름 맞추기"

def get_founder_quiz_items():
    items = []
    for period in PREMODERN_PERIODS:
        for founder in period.get("founders", []):
            items.append({
                "period": period["name"],
                "person": founder["person"],
                "role": founder["role"],
                "explain": founder["explain"]
            })
    return items

def make_quiz():
    mode = st.session_state.get("quiz_mode", "흐름 맞추기")

    if mode == "흐름 맞추기":
        question = "다음 중 중국 역사 흐름으로 가장 알맞은 것은?"
        correct = "선사·신화 → 하·상·주 → 춘추전국 → 진 → 한 → 위진남북조 → 수·당 → 송·원 → 명·청 → 근현대"
        options = [
            correct,
            "명·청 → 송·원 → 진 → 선사·신화 → 한",
            "한 → 진 → 춘추전국 → 수·당 → 하·상·주",
            "근현대 → 명·청 → 송·원 → 수·당 → 진"
        ]

    elif mode == "시대 설명 맞추기":
        item = random.choice(PREMODERN_PERIODS)
        question = f"다음 설명에 해당하는 시대는?<br><br>{item['core']}"
        correct = item["name"]
        options = [x["name"] for x in PREMODERN_PERIODS]
        options = random.sample(options, min(4, len(options)))
        if correct not in options:
            options[0] = correct

    elif mode == "건국 인물 맞추기":
        founder_items = get_founder_quiz_items()
        item = random.choice(founder_items)
        question = f"다음 설명에 해당하는 인물은?<br><br>{item['role']}<br>{item['explain']}"
        correct = item["person"]
        options = [x["person"] for x in founder_items]
        options = list(dict.fromkeys(options))
        options = random.sample(options, min(4, len(options)))
        if correct not in options:
            options[0] = correct

    elif mode == "연도 맞추기":
        all_items = PREMODERN_PERIODS + MODERN_STEPS
        item = random.choice(all_items)
        item_name = item.get("name", item.get("title", ""))
        question = f"{item_name}의 시기 또는 기간은?"
        correct = item["years"]
        options = [x["years"] for x in all_items]
        options = list(dict.fromkeys(options))
        options = random.sample(options, min(4, len(options)))
        if correct not in options:
            options[0] = correct

    elif mode == "근현대사 맞추기":
        item = random.choice(MODERN_STEPS)
        question = f"다음 설명에 해당하는 근현대사 단계는?<br><br>{item['summary']}"
        correct = item["title"]
        options = [x["title"] for x in MODERN_STEPS]
        options = random.sample(options, 4)
        if correct not in options:
            options[0] = correct

    elif mode == "주요 인물 맞추기":
        item = random.choice(IMPORTANT_PEOPLE)
        point = random.choice(item["points"])
        question = f"다음 내용과 관련 깊은 인물은?<br><br>{point}"
        correct = item["name"]
        options = [x["name"] for x in IMPORTANT_PEOPLE]
        options = random.sample(options, 4)
        if correct not in options:
            options[0] = correct

    else:
        item = random.choice(IMPORTANT_PEOPLE)
        question = f"{item['name']}과 가장 관련 깊은 시대는?"
        correct = item["period"]
        options = [x["period"] for x in IMPORTANT_PEOPLE]
        options = list(dict.fromkeys(options))
        options = random.sample(options, min(4, len(options)))
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
# 화면
# =====================================================
st.title("🐉 중국 역사와 근현대사")
st.caption("중국사의 큰 흐름, 왕조별 특징, 건국 인물, 근현대사를 한눈에 정리한 수업용 앱입니다.")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧭 큰 흐름",
    "🏛️ 고대~청",
    "🇨🇳 근현대사",
    "👤 주요 인물 정리",
    "📌 한눈에 정리",
    "🎮 확인 퀴즈"
])

with tab1:
    st.subheader("🧭 중국 역사 큰 흐름")

    cols = st.columns(5)
    for i, item in enumerate(HISTORY_FLOW):
        with cols[i % 5]:
            with st.container(border=True):
                st.markdown(f"### {item['emoji']}")
                st.markdown(f"**{item['name']}**")
                st.caption(item["years"])
                st.markdown(item["one"])

    st.info("암기 순서: 선사·신화 → 하·상·주 → 춘추전국 → 진 → 한 → 위진남북조 → 수·당 → 송·원 → 명·청 → 근현대")

with tab2:
    st.subheader("🏛️ 고대부터 청나라까지")
    st.caption("건국 인물은 별도 탭으로 분리하지 않고, 각 시대 설명 안에 함께 넣었습니다.")

    for item in PREMODERN_PERIODS:
        with st.container(border=True):
            st.markdown(f"## {item['emoji']} {item['name']}")
            st.caption(item["years"])
            st.markdown(f"**구분:** {item['period']}")
            st.markdown(f"**핵심:** {item['core']}")

            if item.get("founders"):
                st.markdown("### 👑 건국·관련 인물")
                founder_cols = st.columns(min(3, len(item["founders"])))
                for idx, founder in enumerate(item["founders"]):
                    with founder_cols[idx % min(3, len(item["founders"]))]:
                        with st.container(border=True):
                            st.markdown(f"#### {founder['person']}")
                            st.markdown(f"**{founder['role']}**")
                            st.caption(founder["explain"])

            st.markdown("### 📖 설명")
            for d in item["details"]:
                st.markdown(f"- {d}")

            st.markdown("### 🔑 키워드")
            st.write(" · ".join(item["keywords"]))

with tab3:
    st.subheader("🇨🇳 중국 근현대사 조금 더 자세히")

    cols = st.columns(3)
    for i, item in enumerate(MODERN_STEPS):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {item['emoji']} {item['title']}")
                st.caption(item["years"])
                st.markdown(item["summary"])
                for d in item["details"]:
                    st.markdown(f"- {d}")
                st.caption(" · ".join(item["keywords"]))

with tab4:
    st.subheader("👤 중국사 주요 인물 정리")
    st.warning("인물별 내용은 수업용 요약입니다. 업적만 외우기보다 시대적 배경과 함께 이해하는 것이 중요합니다.")

    cols = st.columns(3)
    for i, p in enumerate(IMPORTANT_PEOPLE):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {p['name']}")
                st.caption(p["period"])
                st.markdown(f"**핵심:** {p['main']}")
                st.markdown("**주요 내용**")
                for point in p["points"]:
                    st.markdown(f"- {point}")
                st.markdown(f"**함께 볼 점:** {p['note']}")

with tab5:
    st.subheader("📌 한눈에 정리")

    st.markdown("### 고대~청")
    st.dataframe(
        [
            {
                "시대": x["name"],
                "연도/시기": x["years"],
                "구분": x["period"],
                "건국·관련 인물": ", ".join([f["person"] for f in x.get("founders", [])]),
                "핵심": x["core"],
                "키워드": ", ".join(x["keywords"])
            }
            for x in PREMODERN_PERIODS
        ],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 건국·관련 인물")
    founder_rows = []
    for x in PREMODERN_PERIODS:
        for f in x.get("founders", []):
            founder_rows.append({
                "시대": x["name"],
                "인물": f["person"],
                "관련 내용": f["role"],
                "간단 설명": f["explain"]
            })

    st.dataframe(
        founder_rows,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 근현대사")
    st.dataframe(
        [
            {
                "단계": x["title"],
                "연도/시기": x["years"],
                "핵심 설명": x["summary"],
                "키워드": ", ".join(x["keywords"])
            }
            for x in MODERN_STEPS
        ],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 주요 인물")
    st.dataframe(
        [
            {
                "인물": p["name"],
                "시대": p["period"],
                "핵심": p["main"]
            }
            for p in IMPORTANT_PEOPLE
        ],
        use_container_width=True,
        hide_index=True
    )

with tab6:
    st.subheader("🎮 중국 역사 확인 퀴즈")

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
        ["흐름 맞추기", "시대 설명 맞추기", "건국 인물 맞추기", "연도 맞추기", "근현대사 맞추기", "주요 인물 맞추기", "인물 시대 맞추기"],
        horizontal=True,
        key="china_history_quiz_radio_v1"
    )

    if selected_mode != st.session_state.quiz_mode:
        st.session_state.quiz_mode = selected_mode
        make_quiz()
        st.rerun()

    st.markdown(f"### {st.session_state.quiz_question}", unsafe_allow_html=True)

    cols = st.columns(2)
    for i, option in enumerate(st.session_state.quiz_options):
        with cols[i % 2]:
            if st.button(
                option,
                key=f"china_history_quiz_v1_{i}_{st.session_state.total}",
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

st.caption("필요 패키지: streamlit")
