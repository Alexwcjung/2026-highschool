import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="일상 문장구조 말하기 훈련",
    page_icon="🎙️",
    layout="wide"
)

# =========================================================
# 데이터
# - 일상단어 400 느낌의 어휘를 활용
# - 2문장 이상 / 조금 더 길고 / 약간 복잡한 문장
# - 기능은 생존 문장 말하기 훈련 형태
# =========================================================
PRACTICE_ITEMS = [
    {
        "cat": "🏫 학교생활",
        "ko": "나는 오늘 수학 과제가 있어. 그래서 도서관에서 교과서와 공책을 사용할 거야.",
        "blank": "I have a ______ assignment today, so I will use my ______ and ______ in the ______.",
        "answer": "I have a math assignment today, so I will use my textbook and notebook in the library.",
        "hint": "math / textbook / notebook / library",
        "emoji": "📚"
    },
    {
        "cat": "🏫 학교생활",
        "ko": "우리 모둠은 과학 프로젝트를 준비하고 있어. 내일 발표가 있어서 조금 긴장돼.",
        "blank": "Our group is preparing a ______ project, and I am a little ______ because we have a ______ tomorrow.",
        "answer": "Our group is preparing a science project, and I am a little nervous because we have a presentation tomorrow.",
        "hint": "science / nervous / presentation",
        "emoji": "🧪"
    },
    {
        "cat": "🏫 학교생활",
        "ko": "나는 복도에서 친구를 만났어. 우리는 점심시간 전에 일정표를 확인했어.",
        "blank": "I met my ______ in the ______, and we checked the ______ before lunch time.",
        "answer": "I met my friend in the hallway, and we checked the schedule before lunch time.",
        "hint": "friend / hallway / schedule",
        "emoji": "🏫"
    },
    {
        "cat": "✏️ 교실 활동",
        "ko": "문장을 공책에 베껴 쓰고 중요한 단어에 밑줄을 치세요. 그런 다음 답을 확인하세요.",
        "blank": "______ the sentence in your notebook and ______ the important words. Then ______ your answer.",
        "answer": "Copy the sentence in your notebook and underline the important words. Then check your answer.",
        "hint": "Copy / underline / check",
        "emoji": "✏️"
    },
    {
        "cat": "✏️ 교실 활동",
        "ko": "선생님이 설명한 뒤에 우리는 예시를 비교했어. 그리고 짝과 답을 토론했어.",
        "blank": "After the teacher ______ it, we ______ the examples and ______ the answer with a partner.",
        "answer": "After the teacher explained it, we compared the examples and discussed the answer with a partner.",
        "hint": "explained / compared / discussed",
        "emoji": "🧑‍🏫"
    },
    {
        "cat": "✏️ 교실 활동",
        "ko": "철자를 말하고 단어를 반복해 주세요. 발음이 어렵다면 천천히 다시 말해도 됩니다.",
        "blank": "Please ______ the word and ______ it. If the pronunciation is difficult, you can say it ______ again.",
        "answer": "Please spell the word and repeat it. If the pronunciation is difficult, you can say it slowly again.",
        "hint": "spell / repeat / slowly",
        "emoji": "🔁"
    },
    {
        "cat": "🏠 집과 생활",
        "ko": "나는 거실에서 텔레비전을 보고 있었어. 하지만 냉장고 안에 음식이 없어서 부엌으로 갔어.",
        "blank": "I was watching ______ in the living room, but there was no ______ in the refrigerator, so I went to the ______.",
        "answer": "I was watching television in the living room, but there was no food in the refrigerator, so I went to the kitchen.",
        "hint": "television / food / kitchen",
        "emoji": "🏠"
    },
    {
        "cat": "🏠 집과 생활",
        "ko": "내 방에는 담요와 베개가 있어. 나는 피곤해서 일찍 자고 싶어.",
        "blank": "There is a ______ and a ______ in my bedroom, and I want to sleep ______ because I am tired.",
        "answer": "There is a blanket and a pillow in my bedroom, and I want to sleep early because I am tired.",
        "hint": "blanket / pillow / early",
        "emoji": "🛏️"
    },
    {
        "cat": "🏠 집과 생활",
        "ko": "쓰레기를 버리고 손을 비누로 씻어 주세요. 그런 다음 수건으로 손을 말리세요.",
        "blank": "Please throw away the ______ and wash your hands with ______. Then dry your hands with a ______.",
        "answer": "Please throw away the trash and wash your hands with soap. Then dry your hands with a towel.",
        "hint": "trash / soap / towel",
        "emoji": "🧼"
    },
    {
        "cat": "🌅 하루 일과",
        "ko": "나는 보통 아침에 일찍 일어나. 학교에 가기 전에 샤워하고 옷을 입어.",
        "blank": "I usually ______ early in the morning. I take a ______ and get dressed before I go to ______.",
        "answer": "I usually get up early in the morning. I take a shower and get dressed before I go to school.",
        "hint": "get up / shower / school",
        "emoji": "🌅"
    },
    {
        "cat": "🌅 하루 일과",
        "ko": "주말에는 늦게 일어나지만 평일에는 항상 일찍 출발해. 버스가 자주 붐비기 때문이야.",
        "blank": "I wake up late on ______, but I always leave early on ______ because the bus is often crowded.",
        "answer": "I wake up late on weekends, but I always leave early on weekdays because the bus is often crowded.",
        "hint": "weekends / weekdays",
        "emoji": "🚌"
    },
    {
        "cat": "🌅 하루 일과",
        "ko": "나는 숙제를 끝낸 뒤에 조금 쉬어. 가끔은 음악을 들으면서 긴장을 풀어.",
        "blank": "After I finish my ______, I relax for a while. Sometimes I listen to ______ to feel ______.",
        "answer": "After I finish my homework, I relax for a while. Sometimes I listen to music to feel calm.",
        "hint": "homework / music / calm",
        "emoji": "🎧"
    },
    {
        "cat": "🎮 취미와 여가",
        "ko": "내 취미는 영화 보기야. 시간이 있으면 친구와 영화를 보고 감상에 대해 이야기해.",
        "blank": "My ______ is watching movies. If I have free time, I watch a movie with my ______ and talk about it.",
        "answer": "My hobby is watching movies. If I have free time, I watch a movie with my friend and talk about it.",
        "hint": "hobby / friend",
        "emoji": "🎬"
    },
    {
        "cat": "🎮 취미와 여가",
        "ko": "그녀는 사진 촬영을 좋아해. 그래서 주말마다 공원에서 사진을 찍어.",
        "blank": "She likes ______, so she takes pictures in the ______ every weekend.",
        "answer": "She likes photography, so she takes pictures in the park every weekend.",
        "hint": "photography / park",
        "emoji": "📷"
    },
    {
        "cat": "🎮 취미와 여가",
        "ko": "나는 캠핑을 좋아하지만 오늘은 날씨가 나빠. 그래서 집에서 소설을 읽을 거야.",
        "blank": "I like ______, but the weather is bad today, so I will read a ______ at home.",
        "answer": "I like camping, but the weather is bad today, so I will read a novel at home.",
        "hint": "camping / novel",
        "emoji": "🏕️"
    },
    {
        "cat": "⚽ 운동과 활동",
        "ko": "우리는 방과 후에 축구를 할 거야. 경기장에 늦지 않도록 제시간에 도착해야 해.",
        "blank": "We will play ______ after school, and we should arrive at the ______ on time.",
        "answer": "We will play soccer after school, and we should arrive at the field on time.",
        "hint": "soccer / field",
        "emoji": "⚽"
    },
    {
        "cat": "⚽ 운동과 활동",
        "ko": "그는 농구 경기에 나가고 싶어 해. 하지만 무릎이 아파서 오늘은 쉬어야 해.",
        "blank": "He wants to join the ______ match, but his knee hurts, so he should ______ today.",
        "answer": "He wants to join the basketball match, but his knee hurts, so he should rest today.",
        "hint": "basketball / rest",
        "emoji": "🏀"
    },
    {
        "cat": "⚽ 운동과 활동",
        "ko": "코치가 운동장에서 우리에게 설명했어. 우리는 다음 대회를 위해 매일 연습할 거야.",
        "blank": "The ______ explained it to us on the field, and we will ______ every day for the next competition.",
        "answer": "The coach explained it to us on the field, and we will practice every day for the next competition.",
        "hint": "coach / practice",
        "emoji": "🏟️"
    },
    {
        "cat": "🌦️ 날씨와 계절",
        "ko": "오늘은 비가 오고 바람이 불어. 그래서 우산과 비옷이 필요해.",
        "blank": "It is ______ and ______ today, so I need an umbrella and a raincoat.",
        "answer": "It is rainy and windy today, so I need an umbrella and a raincoat.",
        "hint": "rainy / windy",
        "emoji": "🌧️"
    },
    {
        "cat": "🌦️ 날씨와 계절",
        "ko": "겨울에는 날씨가 춥지만 나는 눈 오는 날을 좋아해. 눈사람을 만들 수 있기 때문이야.",
        "blank": "It is cold in ______, but I like snowy days because I can make a ______.",
        "answer": "It is cold in winter, but I like snowy days because I can make a snowman.",
        "hint": "winter / snowman",
        "emoji": "⛄"
    },
    {
        "cat": "🌦️ 날씨와 계절",
        "ko": "일기예보를 확인해 주세요. 오후에는 폭풍우가 올 수 있어서 밖에 나가면 조심해야 해요.",
        "blank": "Please check the weather ______. It may be ______ in the afternoon, so be careful outside.",
        "answer": "Please check the weather forecast. It may be stormy in the afternoon, so be careful outside.",
        "hint": "forecast / stormy",
        "emoji": "🌩️"
    },
    {
        "cat": "🍽️ 식당과 주문",
        "ko": "나는 식당에서 메뉴를 보고 있어. 매운 음식은 괜찮지만 너무 비싼 요리는 원하지 않아.",
        "blank": "I am looking at the ______ in the restaurant. Spicy food is okay, but I do not want an expensive ______.",
        "answer": "I am looking at the menu in the restaurant. Spicy food is okay, but I do not want an expensive dish.",
        "hint": "menu / dish",
        "emoji": "🍽️"
    },
    {
        "cat": "🍽️ 식당과 주문",
        "ko": "계산서를 가져다 주세요. 영수증도 필요해요. 왜냐하면 비용을 확인해야 하기 때문이에요.",
        "blank": "Please bring the ______ and the ______ because I need to check the price.",
        "answer": "Please bring the bill and the receipt because I need to check the price.",
        "hint": "bill / receipt",
        "emoji": "🧾"
    },
    {
        "cat": "🍽️ 식당과 주문",
        "ko": "그녀는 샐러드를 주문했고 나는 수프를 주문했어. 우리는 식사 후에 디저트를 먹을 거야.",
        "blank": "She ordered a ______ and I ordered soup. We will have ______ after the meal.",
        "answer": "She ordered a salad and I ordered soup. We will have dessert after the meal.",
        "hint": "salad / dessert",
        "emoji": "🥗"
    },
    {
        "cat": "🛍️ 쇼핑과 가격",
        "ko": "이 재킷은 너무 비싸. 할인 쿠폰이 있으면 나는 그것을 살 수 있어.",
        "blank": "This jacket is too ______. If I have a discount ______, I can buy it.",
        "answer": "This jacket is too expensive. If I have a discount coupon, I can buy it.",
        "hint": "expensive / coupon",
        "emoji": "🛍️"
    },
    {
        "cat": "🛍️ 쇼핑과 가격",
        "ko": "계산원이 거스름돈을 줬어. 나는 영수증을 확인하고 가방에 넣었어.",
        "blank": "The ______ gave me change, and I checked the ______ before I put it in my bag.",
        "answer": "The cashier gave me change, and I checked the receipt before I put it in my bag.",
        "hint": "cashier / receipt",
        "emoji": "💵"
    },
    {
        "cat": "🛍️ 쇼핑과 가격",
        "ko": "색깔은 좋지만 사이즈가 맞지 않아. 그래서 교환이나 환불을 요청할 거야.",
        "blank": "The color is good, but the ______ is not right, so I will ask for an ______ or a refund.",
        "answer": "The color is good, but the size is not right, so I will ask for an exchange or a refund.",
        "hint": "size / exchange",
        "emoji": "👕"
    },
    {
        "cat": "🚇 교통과 길 찾기",
        "ko": "나는 길을 잃었어. 지하철역에 가려면 어느 방향으로 가야 하는지 알고 싶어.",
        "blank": "I am ______, and I want to know which direction I should go to get to the ______ station.",
        "answer": "I am lost, and I want to know which direction I should go to get to the subway station.",
        "hint": "lost / subway",
        "emoji": "🚇"
    },
    {
        "cat": "🚇 교통과 길 찾기",
        "ko": "버스 정류장은 모퉁이 근처에 있어. 횡단보도를 건넌 뒤에 오른쪽으로 가세요.",
        "blank": "The bus stop is near the ______. Cross the crosswalk and then go ______.",
        "answer": "The bus stop is near the corner. Cross the crosswalk and then go right.",
        "hint": "corner / right",
        "emoji": "🚏"
    },
    {
        "cat": "🚇 교통과 길 찾기",
        "ko": "공항에 가려면 터미널에서 갈아타야 해. 시간이 없으니 빨리 움직여야 해.",
        "blank": "To get to the ______, you need to transfer at the terminal. We do not have much time, so we should move ______.",
        "answer": "To get to the airport, you need to transfer at the terminal. We do not have much time, so we should move quickly.",
        "hint": "airport / quickly",
        "emoji": "✈️"
    },
    {
        "cat": "🧳 여행과 숙박",
        "ko": "나는 호텔 예약을 확인하고 싶어. 여권과 짐은 내 배낭 안에 있어.",
        "blank": "I want to check my hotel ______. My passport and luggage are in my ______.",
        "answer": "I want to check my hotel reservation. My passport and luggage are in my backpack.",
        "hint": "reservation / backpack",
        "emoji": "🧳"
    },
    {
        "cat": "🧳 여행과 숙박",
        "ko": "우리는 현지 박물관을 방문할 거야. 유명한 기념품도 사고 싶어.",
        "blank": "We will visit a local ______, and I also want to buy a famous ______.",
        "answer": "We will visit a local museum, and I also want to buy a famous souvenir.",
        "hint": "museum / souvenir",
        "emoji": "🏛️"
    },
    {
        "cat": "🧳 여행과 숙박",
        "ko": "체크인 시간이 늦었지만 직원이 우리를 도와줬어. 그래서 우리는 방에 들어갈 수 있었어.",
        "blank": "The check-in time was ______, but the staff helped us, so we could enter the ______.",
        "answer": "The check-in time was late, but the staff helped us, so we could enter the room.",
        "hint": "late / room",
        "emoji": "🏨"
    },
    {
        "cat": "😊 감정 표현",
        "ko": "나는 발표 전에 긴장했지만 끝난 뒤에는 자랑스러웠어. 친구들이 내게 박수를 쳤기 때문이야.",
        "blank": "I was ______ before the presentation, but I felt ______ after it because my friends clapped for me.",
        "answer": "I was nervous before the presentation, but I felt proud after it because my friends clapped for me.",
        "hint": "nervous / proud",
        "emoji": "👏"
    },
    {
        "cat": "😊 감정 표현",
        "ko": "그는 시험 결과에 실망했어. 하지만 선생님의 조언을 듣고 다시 희망을 가졌어.",
        "blank": "He was ______ with the test result, but he felt ______ again after listening to the teacher's advice.",
        "answer": "He was disappointed with the test result, but he felt hopeful again after listening to the teacher's advice.",
        "hint": "disappointed / hopeful",
        "emoji": "😊"
    },
    {
        "cat": "😊 감정 표현",
        "ko": "나는 혼자 있어서 외로웠어. 그래서 친구에게 메시지를 보내고 함께 산책했어.",
        "blank": "I felt ______ because I was alone, so I sent a ______ to my friend and walked together.",
        "answer": "I felt lonely because I was alone, so I sent a message to my friend and walked together.",
        "hint": "lonely / message",
        "emoji": "💬"
    },
    {
        "cat": "📱 미디어와 스마트폰",
        "ko": "내 스마트폰 배터리가 거의 없어. 와이파이 비밀번호를 찾으면 친구에게 메시지를 보낼 수 있어.",
        "blank": "My smartphone ______ is almost dead. If I find the Wi-Fi ______, I can send a message to my friend.",
        "answer": "My smartphone battery is almost dead. If I find the Wi-Fi password, I can send a message to my friend.",
        "hint": "battery / password",
        "emoji": "📱"
    },
    {
        "cat": "📱 미디어와 스마트폰",
        "ko": "나는 웹사이트에서 뉴스를 검색했어. 그런 다음 중요한 게시물에 댓글을 달았어.",
        "blank": "I searched for ______ on the website, and then I wrote a ______ on an important post.",
        "answer": "I searched for news on the website, and then I wrote a comment on an important post.",
        "hint": "news / comment",
        "emoji": "🌐"
    },
    {
        "cat": "📱 미디어와 스마트폰",
        "ko": "영상 통화가 끊겼어. 화면이 멈췄고 인터넷 연결도 좋지 않았어.",
        "blank": "The video call stopped. The ______ froze, and the internet connection was not ______.",
        "answer": "The video call stopped. The screen froze, and the internet connection was not good.",
        "hint": "screen / good",
        "emoji": "📹"
    },
    {
        "cat": "🌈 직업과 미래",
        "ko": "나는 미래에 기술자가 되고 싶어. 그래서 공장에서 필요한 기술과 경험을 배우고 있어.",
        "blank": "I want to become an ______ in the future, so I am learning the skills and ______ needed in a factory.",
        "answer": "I want to become an engineer in the future, so I am learning the skills and experience needed in a factory.",
        "hint": "engineer / experience",
        "emoji": "🛠️"
    },
    {
        "cat": "🌈 직업과 미래",
        "ko": "그녀는 요리사가 되는 것이 꿈이야. 면접 전에 자신의 목표를 분명하게 설명하려고 해.",
        "blank": "Her dream is to become a ______, and she wants to explain her ______ clearly before the interview.",
        "answer": "Her dream is to become a chef, and she wants to explain her goal clearly before the interview.",
        "hint": "chef / goal",
        "emoji": "👩‍🍳"
    },
    {
        "cat": "🌈 직업과 미래",
        "ko": "나는 소방관을 존경해. 위험한 상황에서도 사람들을 돕기 때문이야.",
        "blank": "I respect ______ because they help people even in ______ situations.",
        "answer": "I respect firefighters because they help people even in dangerous situations.",
        "hint": "firefighters / dangerous",
        "emoji": "🚒"
    },
]

# =========================================================
# 디자인
# =========================================================
st.markdown(
    """
    <style>
    @media (max-width: 640px) {
        #speaking-app {
            padding: 10px !important;
            border-radius: 20px !important;
        }
        #speaking-app #blankSentence {
            font-size: 20px !important;
            padding: 13px 12px !important;
            margin-bottom: 8px !important;
            line-height: 1.45 !important;
        }
        #speaking-app #koPrompt {
            font-size: 19px !important;
            margin-bottom: 8px !important;
            line-height: 1.35 !important;
        }
        #speaking-app #transcriptBox {
            font-size: 17px !important;
            line-height: 1.45 !important;
        }
        #speaking-app #micBtn {
            width: 78px !important;
            height: 78px !important;
            font-size: 27px !important;
        }
        #speaking-app #hintBtn,
        #speaking-app #answerBtn,
        #speaking-app #listenBtn,
        #speaking-app #nextBtn {
            padding: 8px 12px !important;
            font-size: 13px !important;
        }
        #speaking-app #hintBox {
            font-size: 13px !important;
            padding: 6px 8px !important;
            line-height: 1.25 !important;
            max-width: 100% !important;
            overflow-wrap: anywhere !important;
            word-break: break-word !important;
            white-space: normal !important;
            box-sizing: border-box !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 말하기 훈련 컴포넌트
# =========================================================
def speaking_practice_component(items):
    items_json = json.dumps(items, ensure_ascii=False)

    html = r"""
    <div id="speaking-app" style="
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #eff6ff 0%, #fdf4ff 35%, #fff7ed 68%, #f0fdf4 100%);
        border: 2px solid #c4b5fd;
        border-radius: 34px;
        padding: 24px;
        box-shadow: 0 12px 28px rgba(124,58,237,0.12);
    ">
        <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-bottom:18px;">
            <label style="font-weight:900; color:#334155;">주제 선택</label>
            <select id="categorySelect" style="
                padding: 10px 14px;
                border-radius: 999px;
                border: 1.5px solid #bae6fd;
                font-size: 15px;
                font-weight: 800;
                color: #0f172a;
                background: white;
            "></select>

            <button id="randomBtn" style="
                border: 1.5px solid #c7d2fe;
                background: white;
                color: #3730a3;
                border-radius: 999px;
                padding: 10px 15px;
                font-weight: 900;
                cursor: pointer;
            ">🎲 랜덤</button>

            <button id="resetBtn" style="
                border: 1.5px solid #fed7aa;
                background: #fff7ed;
                color: #9a3412;
                border-radius: 999px;
                padding: 10px 15px;
                font-weight: 900;
                cursor: pointer;
            ">🔄 점수 초기화</button>
        </div>

        <div style="
            background:white;
            border-radius:26px;
            padding:24px;
            border:1.5px solid #e0f2fe;
            box-shadow:0 5px 16px rgba(0,0,0,0.055);
        ">
            <div style="display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; margin-bottom:14px;">
                <div id="categoryLabel" style="
                    display:inline-block;
                    background:linear-gradient(135deg,#dbeafe,#ede9fe);
                    color:#3730a3;
                    border-radius:999px;
                    padding:8px 14px;
                    font-size:15px;
                    font-weight:900;
                    border:1.5px solid #c4b5fd;
                "></div>

                <div id="scoreLabel" style="
                    display:inline-block;
                    background:linear-gradient(135deg,#dcfce7,#fef9c3);
                    color:#166534;
                    border-radius:999px;
                    padding:8px 14px;
                    font-size:15px;
                    font-weight:900;
                    border:1.5px solid #86efac;
                ">정답 0개</div>
            </div>

            <div style="
                font-size: 26px;
                font-weight: 900;
                color: #111827;
                line-height: 1.35;
                margin-bottom: 10px;
            " id="koPrompt">
                한국어 상황
            </div>

            <div style="
                background: linear-gradient(135deg, #ffffff 0%, #eff6ff 45%, #fdf4ff 100%);
                border: 2px solid #c4b5fd;
                border-radius: 24px;
                padding: 18px 16px;
                margin-bottom: 12px;
                font-size: 28px;
                font-weight: 900;
                color: #1f2937;
                line-height: 1.55;
                box-shadow: 0 6px 16px rgba(99,102,241,0.08);
                word-break: break-word;
            " id="blankSentence">
                I am ______.
            </div>

            <div style="
                background:linear-gradient(135deg,#eef2ff,#fdf2f8);
                border:1.5px solid #c4b5fd;
                border-radius:20px;
                padding:14px 16px;
                margin-bottom:12px;
                min-height:52px;
                box-shadow: 0 4px 12px rgba(124,58,237,0.08);
            ">
                <div id="transcriptBox" style="
                    font-size:23px;
                    font-weight:900;
                    color:#4c1d95;
                    line-height:1.6;
                    min-height:32px;
                    word-break: break-word;
                "></div>
            </div>

            <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center; justify-content:center; margin-bottom:12px;">
                <button id="hintBtn" style="
                    border:1.5px solid #fcd34d;
                    background:linear-gradient(135deg,#fef3c7,#fde68a);
                    color:#92400e;
                    border-radius:999px;
                    padding:10px 16px;
                    font-weight:900;
                    cursor:pointer;
                    box-shadow:0 4px 10px rgba(245,158,11,0.14);
                ">💡 힌트</button>

                <button id="micBtn" style="
                    border:4px solid rgba(255,255,255,0.95);
                    background: linear-gradient(135deg, #8b5cf6, #ec4899);
                    color:white;
                    border-radius:999px;
                    width:100px;
                    height:100px;
                    font-weight:900;
                    cursor:pointer;
                    font-size:36px;
                    box-shadow:0 12px 26px rgba(124,58,237,0.26);
                    flex: 0 0 auto;
                ">🎙️</button>

                <button id="answerBtn" style="
                    display:none;
                    border:1.5px solid #86efac;
                    background:linear-gradient(135deg,#dcfce7,#f0fdf4);
                    color:#166534;
                    border-radius:999px;
                    padding:10px 16px;
                    font-weight:900;
                    cursor:pointer;
                    box-shadow:0 4px 10px rgba(34,197,94,0.12);
                ">👀 정답</button>

                <button id="listenBtn" style="
                    display:none;
                    border:1.5px solid #93c5fd;
                    background:linear-gradient(135deg,#dbeafe,#eff6ff);
                    color:#1d4ed8;
                    border-radius:999px;
                    padding:10px 16px;
                    font-weight:900;
                    cursor:pointer;
                    box-shadow:0 4px 10px rgba(59,130,246,0.12);
                ">🔊 듣기</button>

                <button id="nextBtn" style="
                    border:1.5px solid #c4b5fd;
                    background:linear-gradient(135deg,#ede9fe,#eef2ff);
                    color:#5b21b6;
                    border-radius:999px;
                    padding:10px 16px;
                    font-weight:900;
                    cursor:pointer;
                    font-size:16px;
                    box-shadow:0 4px 10px rgba(124,58,237,0.12);
                ">➡️ 다음</button>
            </div>

            <div id="hintBox" style="
                display:none;
                background:linear-gradient(135deg,#fff7ed,#fffbeb);
                border:1.5px solid #fbbf24;
                color:#92400e;
                border-radius:14px;
                padding:7px 10px;
                margin-top:6px;
                margin-bottom:6px;
                font-size:16px;
                font-weight:900;
                line-height:1.25;
                word-break:break-word;
                overflow-wrap:anywhere;
                white-space:normal;
                max-width:100%;
                box-sizing:border-box;
                box-shadow: 0 3px 8px rgba(251,191,36,0.10);
            "></div>

            <div id="resultBox" style="
                display:none;
                margin-top:8px;
                font-size:15px;
                font-weight:800;
                color:#64748b;
            "></div>
        </div>

        <div style="
            margin-top:14px;
            color:#64748b;
            font-size:13px;
            line-height:1.6;
            font-weight:700;
        ">
            ※ Chrome 계열 브라우저에서 음성 인식이 가장 잘 작동합니다.<br>
            ※ 마이크 권한 요청이 나오면 허용을 눌러 주세요.
        </div>
    </div>

    <script>
    const ITEMS = __ITEMS_JSON__;

    let currentList = [];
    let currentIndex = 0;
    let currentItem = null;
    let score = 0;
    let alreadyCorrect = false;
    let isListening = false;
    let recognitionTimeout = null;

    const categorySelect = document.getElementById("categorySelect");
    const randomBtn = document.getElementById("randomBtn");
    const resetBtn = document.getElementById("resetBtn");
    const categoryLabel = document.getElementById("categoryLabel");
    const scoreLabel = document.getElementById("scoreLabel");
    const koPrompt = document.getElementById("koPrompt");
    const blankSentence = document.getElementById("blankSentence");
    const hintBox = document.getElementById("hintBox");
    const hintBtn = document.getElementById("hintBtn");
    const listenBtn = document.getElementById("listenBtn");
    const answerBtn = document.getElementById("answerBtn");
    const micBtn = document.getElementById("micBtn");
    const nextBtn = document.getElementById("nextBtn");
    const transcriptBox = document.getElementById("transcriptBox");
    const resultBox = document.getElementById("resultBox");

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition = null;

    function uniqueCategories() {
        const cats = ["전체"];
        ITEMS.forEach(item => {
            if (!cats.includes(item.cat)) cats.push(item.cat);
        });
        return cats;
    }

    function initCategories() {
        const cats = uniqueCategories();
        categorySelect.innerHTML = "";
        cats.forEach(cat => {
            const option = document.createElement("option");
            option.value = cat;
            option.innerText = cat;
            categorySelect.appendChild(option);
        });
    }

    function getFilteredItems() {
        const selected = categorySelect.value;
        if (selected === "전체") return ITEMS.slice();
        return ITEMS.filter(item => item.cat === selected);
    }

    function shuffleArray(arr) {
        const copied = arr.slice();
        for (let i = copied.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [copied[i], copied[j]] = [copied[j], copied[i]];
        }
        return copied;
    }

    function normalizeText(text) {
        return String(text || "")
            .toLowerCase()
            .replace(/\bi'm\b/g, "i am")
            .replace(/\bim\b/g, "i am")
            .replace(/\byou're\b/g, "you are")
            .replace(/\bhe's\b/g, "he is")
            .replace(/\bshe's\b/g, "she is")
            .replace(/\bit's\b/g, "it is")
            .replace(/\bwe're\b/g, "we are")
            .replace(/\bthey're\b/g, "they are")
            .replace(/\bdon't\b/g, "do not")
            .replace(/\bdoesn't\b/g, "does not")
            .replace(/\bdidn't\b/g, "did not")
            .replace(/\bcan't\b/g, "cannot")
            .replace(/\bcant\b/g, "cannot")
            .replace(/\bi'll\b/g, "i will")
            .replace(/\byou'll\b/g, "you will")
            .replace(/\bhe'll\b/g, "he will")
            .replace(/\bshe'll\b/g, "she will")
            .replace(/[.,!?;:'"’‘“”]/g, "")
            .replace(/-/g, " ")
            .replace(/\s+/g, " ")
            .trim();
    }

    function wordsOnly(text) {
        return normalizeText(text).split(" ").filter(w => w.length > 0);
    }

    function editDistance(a, b) {
        a = String(a || "");
        b = String(b || "");
        const dp = Array.from({ length: a.length + 1 }, () => Array(b.length + 1).fill(0));

        for (let i = 0; i <= a.length; i++) dp[i][0] = i;
        for (let j = 0; j <= b.length; j++) dp[0][j] = j;

        for (let i = 1; i <= a.length; i++) {
            for (let j = 1; j <= b.length; j++) {
                const cost = a[i - 1] === b[j - 1] ? 0 : 1;
                dp[i][j] = Math.min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + cost
                );
            }
        }
        return dp[a.length][b.length];
    }

    function wordSimilarity(a, b) {
        if (!a || !b) return 0;
        if (a === b) return 1;
        const dist = editDistance(a, b);
        return 1 - (dist / Math.max(a.length, b.length));
    }

    function soundKey(text) {
        return normalizeText(text)
            .replace(/[^a-z]/g, "")
            .replace(/tion/g, "shun")
            .replace(/sion/g, "shun")
            .replace(/th/g, "d")
            .replace(/ph/g, "f")
            .replace(/gh/g, "g")
            .replace(/ck/g, "k")
            .replace(/qu/g, "kw")
            .replace(/x/g, "ks")
            .replace(/c/g, "k")
            .replace(/q/g, "k")
            .replace(/z/g, "s")
            .replace(/v/g, "b")
            .replace(/r/g, "l")
            .replace(/ee/g, "i")
            .replace(/ea/g, "i")
            .replace(/ie/g, "i")
            .replace(/ei/g, "i")
            .replace(/oo/g, "u")
            .replace(/ou/g, "u")
            .replace(/ow/g, "o")
            .replace(/oa/g, "o")
            .replace(/ai/g, "e")
            .replace(/ay/g, "e")
            .replace(/[aeiouy]/g, "")
            .replace(/(.)\1+/g, "$1");
    }

    function aliasMatch(spokenWord, answerWord) {
        const sw = normalizeText(spokenWord).replace(/\s+/g, "");
        const aw = normalizeText(answerWord).replace(/\s+/g, "");

        const aliases = {
            "i": ["i", "eye", "ai"],
            "you": ["you", "u", "yew"],
            "he": ["he", "hi"],
            "she": ["she", "see", "sea"],
            "we": ["we", "wee"],
            "they": ["they", "day"],
            "one": ["one", "won"],
            "two": ["two", "to", "too"],
            "three": ["three", "tree"],
            "four": ["four", "for"],
            "eight": ["eight", "ate"],
            "here": ["here", "hear"],
            "there": ["there", "their"],
            "right": ["right", "write"],
            "wait": ["wait", "weight"],
            "know": ["know", "no"],
            "okay": ["okay", "ok"],
            "phone": ["phone", "fone"],
            "coffee": ["coffee", "coffe"],
            "please": ["please", "plz"]
        };

        if (!aliases[aw]) return false;
        return aliases[aw].includes(sw);
    }

    function isUnderstandableWord(spokenWord, answerWord) {
        const sw = normalizeText(spokenWord).replace(/\s+/g, "");
        const aw = normalizeText(answerWord).replace(/\s+/g, "");

        if (!sw || !aw) return false;
        if (sw === aw) return true;
        if (aliasMatch(sw, aw)) return true;

        const dist = editDistance(sw, aw);
        const sim = wordSimilarity(sw, aw);
        const soundSw = soundKey(sw);
        const soundAw = soundKey(aw);

        const sameFirst = sw.charAt(0) === aw.charAt(0);
        const sameFirstTwo = sw.slice(0, 2) === aw.slice(0, 2);
        const soundSame = soundSw && soundAw && soundSw === soundAw;
        const soundSameFirst = soundSw && soundAw && soundSw.charAt(0) === soundAw.charAt(0);

        if (!sameFirst && !soundSameFirst && sim < 0.78) return false;
        if (soundSame) return true;

        if (aw.length <= 2) return sim >= 0.9;
        if (aw.length <= 4) return (sameFirst || soundSameFirst) && (dist <= 1 || sim >= 0.74);
        if (aw.length <= 6) return (sameFirst || soundSameFirst || sameFirstTwo) && (dist <= 2 || sim >= 0.72);

        return (sameFirst || soundSameFirst || sameFirstTwo) && (dist <= 3 || sim >= 0.68);
    }

    function isCloseEnough(spoken, answer) {
        const s = normalizeText(spoken);
        const a = normalizeText(answer);

        if (!s || !a) return false;
        if (s === a) return true;

        const spokenWords = wordsOnly(s);
        const answerWords = wordsOnly(a);

        if (spokenWords.length === 0 || answerWords.length === 0) return false;

        let matched = 0;
        let used = new Array(spokenWords.length).fill(false);

        for (let aw of answerWords) {
            let found = false;
            for (let i = 0; i < spokenWords.length; i++) {
                if (used[i]) continue;
                if (isUnderstandableWord(spokenWords[i], aw)) {
                    used[i] = true;
                    found = true;
                    break;
                }
            }
            if (found) matched += 1;
        }

        const ratio = matched / answerWords.length;

        // 긴 문장은 ASR 누락이 생길 수 있어 65% 이상 핵심 단어가 맞으면 통과
        return ratio >= 0.65;
    }

    function isCorrectSpeech(spoken, answer) {
        return isCloseEnough(spoken, answer);
    }

    function escapeHtml(text) {
        return String(text || "")
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    function makeTwoLetterHint(answerWord) {
        if (!answerWord) return "";

        return String(answerWord).split("/").map(part => {
            return part.trim().split(" ").map(word => {
                const clean = word.trim();
                if (clean.length <= 2) return clean;
                return clean.slice(0, 2) + "_".repeat(Math.min(clean.length - 2, 6));
            }).join(" ");
        }).join(" / ");
    }

    function makeBlankSentenceHtml(blankText) {
        const parts = String(blankText || "").split(/(______)/g);

        return parts.map(part => {
            if (part === "______") {
                return "<span style='display:inline-block; min-width:120px; height:42px; vertical-align:middle; background:#e0f2fe; border-radius:14px; margin:0 6px; border:1.5px solid #bae6fd;'></span>";
            }

            return escapeHtml(part);
        }).join("");
    }

    function makeFilledBlankSentenceHtml(blankText, hintText) {
        const answers = String(hintText || "")
            .split("/")
            .map(x => x.trim())
            .filter(x => x.length > 0);

        let blankIndex = 0;
        const parts = String(blankText || "").split(/(______)/g);

        return parts.map(part => {
            if (part === "______") {
                const fill = answers[blankIndex] || "";
                blankIndex += 1;

                return "<span style='display:inline-block; min-width:96px; vertical-align:middle; background:#dcfce7; color:#166534; border-radius:14px; margin:0 6px; padding:4px 12px; border:1.5px solid #86efac; font-weight:900; box-shadow:0 3px 8px rgba(34,197,94,0.10);'>"
                    + escapeHtml(fill) +
                    "</span>";
            }

            return escapeHtml(part);
        }).join("");
    }

    function updateScore() {
        scoreLabel.innerText = "정답 " + score + "개";
    }

    function resetMicState() {
        isListening = false;
        if (recognitionTimeout) {
            clearTimeout(recognitionTimeout);
            recognitionTimeout = null;
        }
        micBtn.disabled = false;
        micBtn.style.opacity = "1";
        micBtn.style.pointerEvents = "auto";
        micBtn.innerText = "🎙️";
    }

    function stopRecognition() {
        if (recognitionTimeout) {
            clearTimeout(recognitionTimeout);
            recognitionTimeout = null;
        }
        if (recognition) {
            try { recognition.onresult = null; } catch (e) {}
            try { recognition.onerror = null; } catch (e) {}
            try { recognition.onend = null; } catch (e) {}
            try { recognition.stop(); } catch (e) {}
            try { recognition.abort(); } catch (e) {}
            recognition = null;
        }
        resetMicState();
    }

    function speak(text) {
        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "en-US";
        utterance.rate = 0.82;
        utterance.pitch = 1.05;

        const voices = window.speechSynthesis.getVoices();
        const preferred = voices.find(v =>
            v.lang && v.lang.toLowerCase().startsWith("en") &&
            /(samantha|jenny|aria|zira|google us english|karen|victoria|female)/i.test(v.name)
        );
        if (preferred) utterance.voice = preferred;

        window.speechSynthesis.speak(utterance);
    }

    function loadQuestion(index = 0) {
        if (currentList.length === 0) {
            currentList = getFilteredItems();
        }

        if (index >= currentList.length) index = 0;
        if (index < 0) index = currentList.length - 1;

        currentIndex = index;
        currentItem = currentList[currentIndex];
        alreadyCorrect = false;

        categoryLabel.innerText = currentItem.cat + " · " + (currentIndex + 1) + " / " + currentList.length;
        const emoji = currentItem.emoji || "🎙️";
        koPrompt.innerHTML =
            "<span style='font-size:42px; margin-right:10px; vertical-align:middle;'>" + emoji + "</span>" +
            "<span style='vertical-align:middle;'>" + currentItem.ko + "</span>";

        blankSentence.innerHTML = makeBlankSentenceHtml(currentItem.blank);
        hintBox.style.display = "none";
        hintBox.innerText = "";
        transcriptBox.innerText = "";

        resetMicState();
        hintBtn.style.display = "inline-block";
        micBtn.style.display = "inline-block";
        answerBtn.style.display = "none";
        listenBtn.style.display = "none";
        nextBtn.style.display = "inline-block";

        resultBox.style.display = "none";
        resultBox.innerText = "";
        updateScore();
    }

    function goNextQuestion() {
        stopRecognition();
        window.speechSynthesis.cancel();
        loadQuestion(currentIndex + 1);
    }

    function checkSpeech(spokenText) {
        if (!currentItem) return;

        const recognized = String(spokenText || "").trim();

        if (isCorrectSpeech(recognized, currentItem.answer)) {
            if (!alreadyCorrect) {
                score += 1;
                alreadyCorrect = true;
            }

            updateScore();

            transcriptBox.innerHTML =
                "<span style='color:#4c1d95;'>" + escapeHtml(recognized || currentItem.answer) + "</span> " +
                "<span style='color:#166534;'>✅ 정답입니다</span>";

            blankSentence.innerHTML = makeFilledBlankSentenceHtml(currentItem.blank, currentItem.hint);

            hintBox.style.display = "none";
            answerBtn.style.display = "none";
            listenBtn.style.display = "inline-block";
            nextBtn.style.display = "inline-block";

            resultBox.style.display = "none";
            resultBox.innerText = "";

            speak(currentItem.answer);
        } else {
            transcriptBox.innerHTML =
                "<span style='color:#991b1b;'>" + escapeHtml(recognized || "인식 실패") + "</span> " +
                "<span style='color:#991b1b;'>❌</span>";

            hintBox.style.display = "block";
            hintBox.innerText = "힌트: " + makeTwoLetterHint(currentItem.hint);

            answerBtn.style.display = "inline-block";
            listenBtn.style.display = "none";
            nextBtn.style.display = "inline-block";

            resultBox.style.display = "block";
            resultBox.style.color = "#92400e";
            resultBox.innerText = "힌트를 보고 다시 연습해 보세요.";
        }
    }

    async function startRecognition() {
        if (!SpeechRecognition) {
            transcriptBox.innerText = "Chrome에서 열어 주세요.";
            return;
        }

        if (!currentItem || alreadyCorrect) return;

        stopRecognition();

        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                stream.getTracks().forEach(track => track.stop());
            } catch (err) {
                transcriptBox.innerText = "마이크 허용 후 다시 눌러 주세요.";
                resetMicState();
                return;
            }
        }

        window.speechSynthesis.cancel();

        try {
            recognition = new SpeechRecognition();
            recognition.lang = "en-US";
            recognition.interimResults = true;
            recognition.continuous = false;
            recognition.maxAlternatives = 5;

            isListening = true;
            micBtn.disabled = true;
            micBtn.style.opacity = "0.78";
            micBtn.innerText = "👂";
            resultBox.style.display = "none";
            resultBox.innerText = "";
            transcriptBox.innerText = "";

            recognitionTimeout = setTimeout(function() {
                if (isListening) {
                    try { recognition.stop(); } catch (e) {}
                    resetMicState();
                }
            }, 9000);

            recognition.onresult = function(event) {
                let spokenText = "";
                let hasFinal = false;

                for (let i = 0; i < event.results.length; i++) {
                    let piece = event.results[i][0].transcript.trim();

                    // 여러 후보 중 정답에 가까운 후보가 있으면 그걸 사용
                    for (let j = 0; j < event.results[i].length; j++) {
                        const alt = event.results[i][j].transcript.trim();
                        if (isCorrectSpeech(alt, currentItem.answer)) {
                            piece = alt;
                            break;
                        }
                    }

                    if (piece) {
                        spokenText += (spokenText ? " " : "") + piece;
                    }
                    if (event.results[i].isFinal) {
                        hasFinal = true;
                    }
                }

                transcriptBox.innerText = spokenText;

                if (hasFinal) {
                    stopRecognition();
                    checkSpeech(spokenText);
                }
            };

            recognition.onerror = function(event) {
                stopRecognition();

                if (event.error === "not-allowed" || event.error === "service-not-allowed") {
                    transcriptBox.innerText = "마이크 허용 후 다시 눌러 주세요.";
                } else {
                    transcriptBox.innerText = "인식 실패";
                    hintBox.style.display = "block";
                    hintBox.innerText = "힌트: " + makeTwoLetterHint(currentItem.hint);
                    answerBtn.style.display = "inline-block";
                    nextBtn.style.display = "inline-block";
                    resultBox.style.display = "block";
                    resultBox.style.color = "#64748b";
                    resultBox.innerText = "다시 누르거나 다음 문제로 넘어갈 수 있습니다.";
                }
            };

            recognition.onend = function() {
                resetMicState();
            };

            recognition.start();
        } catch (err) {
            stopRecognition();
            transcriptBox.innerText = "다시 눌러 주세요.";
        }
    }

    categorySelect.addEventListener("change", function() {
        stopRecognition();
        currentList = getFilteredItems();
        currentIndex = 0;
        loadQuestion(0);
    });

    randomBtn.addEventListener("click", function() {
        stopRecognition();
        currentList = shuffleArray(getFilteredItems());
        loadQuestion(0);
    });

    resetBtn.addEventListener("click", function() {
        stopRecognition();
        score = 0;
        alreadyCorrect = false;
        updateScore();
        resultBox.style.display = "none";
        resultBox.innerText = "";
        loadQuestion(0);
    });

    hintBtn.addEventListener("click", function() {
        hintBox.style.display = "block";
        hintBox.innerText = makeTwoLetterHint(currentItem.hint);
    });

    listenBtn.addEventListener("click", function() {
        speak(currentItem.answer);
    });

    answerBtn.addEventListener("click", function() {
        if (!currentItem) return;
        blankSentence.innerHTML = makeFilledBlankSentenceHtml(currentItem.blank, currentItem.hint);
        transcriptBox.innerHTML = "<span style='color:#166534;'>" + escapeHtml(currentItem.answer) + "</span>";
        listenBtn.style.display = "inline-block";
        nextBtn.style.display = "inline-block";
        speak(currentItem.answer);

        resultBox.style.display = "block";
        resultBox.style.color = "#166534";
        resultBox.innerText = "빈칸에 들어간 단어를 보고 다시 말하면 정답으로 인정됩니다.";
    });

    micBtn.addEventListener("click", startRecognition);

    nextBtn.addEventListener("click", function() {
        goNextQuestion();
    });

    initCategories();
    currentList = getFilteredItems();
    updateScore();
    loadQuestion(0);
    </script>
    """

    html = html.replace("__ITEMS_JSON__", items_json)
    components.html(html, height=880, scrolling=True)


speaking_practice_component(PRACTICE_ITEMS)
