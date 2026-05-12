import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="생존 문장구조 2 말하기 테스트",
    page_icon="🛠️",
    layout="wide"
)

# =========================================================
# 데이터
# =========================================================
PRACTICE_ITEMS = [{'cat': '💪 할 수 있는 일 말하기',
  'ko': '나는 영어를 조금 말할 수 있어. 그래서 너를 도와줄 수 있어.',
  'blank': 'I can speak ______ a little, so I can ______ you.',
  'answer': 'I can speak English a little, so I can help you.',
  'hint': 'English / help',
  'emoji': '🤝'},
 {'cat': '💪 할 수 있는 일 말하기',
  'ko': '나는 지금 갈 수 없어. 하지만 여기서 기다릴 수 있어.',
  'blank': 'I cannot ______ now, but I can ______ here.',
  'answer': 'I cannot go now, but I can wait here.',
  'hint': 'go / wait',
  'emoji': '⏳'},
 {'cat': '💪 할 수 있는 일 말하기',
  'ko': '너는 천천히 말할 수 있니? 나는 잘 이해할 수 없어.',
  'blank': 'Can you speak ______? I cannot ______ well.',
  'answer': 'Can you speak slowly? I cannot understand well.',
  'hint': 'slowly / understand',
  'emoji': '🗣️'},
 {'cat': '💪 할 수 있는 일 말하기',
  'ko': '나는 지도를 읽을 수 있어. 그래서 역을 찾을 수 있어.',
  'blank': 'I can ______ a map, so I can ______ the station.',
  'answer': 'I can read a map, so I can find the station.',
  'hint': 'read / find',
  'emoji': '🗺️'},
 {'cat': '💪 할 수 있는 일 말하기',
  'ko': '그는 수영할 수 없어. 그래서 그는 도움이 필요해.',
  'blank': 'He cannot ______, so he needs ______.',
  'answer': 'He cannot swim, so he needs help.',
  'hint': 'swim / help',
  'emoji': '🏊'},
 {'cat': '💪 할 수 있는 일 말하기',
  'ko': '우리는 오늘 공부할 수 있어. 하지만 오래 머물 수는 없어.',
  'blank': 'We can ______ today, but we cannot ______ long.',
  'answer': 'We can study today, but we cannot stay long.',
  'hint': 'study / stay',
  'emoji': '📚'},
 {'cat': '📢 부탁하고 지시하기',
  'ko': '문을 열어 주세요. 안에 들어오지 마세요.',
  'blank': '______ the door, please. Do not ______ inside.',
  'answer': 'Open the door, please. Do not come inside.',
  'hint': 'Open / come',
  'emoji': '🚪'},
 {'cat': '📢 부탁하고 지시하기',
  'ko': '천천히 말해 주세요. 나는 잘 이해하지 못해요.',
  'blank': '______ slowly, please. I do not ______ well.',
  'answer': 'Speak slowly, please. I do not understand well.',
  'hint': 'Speak / understand',
  'emoji': '🙏'},
 {'cat': '📢 부탁하고 지시하기',
  'ko': '여기에 앉으세요. 그리고 이름을 쓰세요.',
  'blank': '______ here, and ______ your name.',
  'answer': 'Sit here, and write your name.',
  'hint': 'Sit / write',
  'emoji': '✏️'},
 {'cat': '📢 부탁하고 지시하기',
  'ko': '조심하세요. 길을 건너지 마세요.',
  'blank': 'Be ______. Do not ______ the street.',
  'answer': 'Be careful. Do not cross the street.',
  'hint': 'careful / cross',
  'emoji': '⚠️'},
 {'cat': '📢 부탁하고 지시하기',
  'ko': '다시 말해 주세요. 그러면 내가 따라 말할게요.',
  'blank': '______ it again, and I will ______ it.',
  'answer': 'Say it again, and I will repeat it.',
  'hint': 'Say / repeat',
  'emoji': '🔁'},
 {'cat': '📢 부탁하고 지시하기',
  'ko': '칠판을 보세요. 답을 확인하세요.',
  'blank': '______ at the board, and ______ your answer.',
  'answer': 'Look at the board, and check your answer.',
  'hint': 'Look / check',
  'emoji': '🧑\u200d🏫'},
 {'cat': '📍 어디에 있는지 말하기',
  'ko': '책상 위에 책 한 권이 있어. 그 옆에 연필 두 자루가 있어.',
  'blank': 'There is a ______ on the desk, and there are two ______ next to it.',
  'answer': 'There is a book on the desk, and there are two pencils next to it.',
  'hint': 'book / pencils',
  'emoji': '📚'},
 {'cat': '📍 어디에 있는지 말하기',
  'ko': '교실에 학생들이 많이 있어. 하지만 선생님은 없어.',
  'blank': 'There are many ______ in the classroom, but there is no ______.',
  'answer': 'There are many students in the classroom, but there is no teacher.',
  'hint': 'students / teacher',
  'emoji': '🏫'},
 {'cat': '📍 어디에 있는지 말하기',
  'ko': '근처에 가게가 하나 있어. 그래서 물을 살 수 있어.',
  'blank': 'There is a ______ nearby, so I can buy ______.',
  'answer': 'There is a store nearby, so I can buy water.',
  'hint': 'store / water',
  'emoji': '🏪'},
 {'cat': '📍 어디에 있는지 말하기',
  'ko': '거리에 자동차가 많아. 그래서 조심해야 해.',
  'blank': 'There are many ______ on the street, so be ______.',
  'answer': 'There are many cars on the street, so be careful.',
  'hint': 'cars / careful',
  'emoji': '🚗'},
 {'cat': '📍 어디에 있는지 말하기',
  'ko': '탁자 아래에 가방이 있어. 그 안에 휴대전화가 있어.',
  'blank': 'There is a ______ under the table. There is a ______ in it.',
  'answer': 'There is a bag under the table. There is a phone in it.',
  'hint': 'bag / phone',
  'emoji': '🎒'},
 {'cat': '📍 어디에 있는지 말하기',
  'ko': '역 앞에 버스가 있어. 하지만 택시는 없어.',
  'blank': 'There is a ______ in front of the station, but there is no ______.',
  'answer': 'There is a bus in front of the station, but there is no taxi.',
  'hint': 'bus / taxi',
  'emoji': '🚌'},
 {'cat': '🧭 위치 자세히 말하기',
  'ko': '내 가방은 의자 아래에 있어. 내 휴대전화는 책상 위에 있어.',
  'blank': 'My bag is ______ the chair, and my phone is ______ the desk.',
  'answer': 'My bag is under the chair, and my phone is on the desk.',
  'hint': 'under / on',
  'emoji': '📱'},
 {'cat': '🧭 위치 자세히 말하기',
  'ko': '화장실은 가게 옆에 있어. 병원은 역 뒤에 있어.',
  'blank': 'The bathroom is ______ the store. The hospital is ______ the station.',
  'answer': 'The bathroom is next to the store. The hospital is behind the station.',
  'hint': 'next to / behind',
  'emoji': '🚻'},
 {'cat': '🧭 위치 자세히 말하기',
  'ko': '버스 정류장은 학교 앞에 있어. 나는 거기서 기다릴 거야.',
  'blank': 'The bus stop is ______ the school, and I will ______ there.',
  'answer': 'The bus stop is in front of the school, and I will wait there.',
  'hint': 'in front of / wait',
  'emoji': '🚏'},
 {'cat': '🧭 위치 자세히 말하기',
  'ko': '고양이는 상자 안에 있어. 개는 문 뒤에 있어.',
  'blank': 'The cat is ______ the box, and the dog is ______ the door.',
  'answer': 'The cat is in the box, and the dog is behind the door.',
  'hint': 'in / behind',
  'emoji': '🐱'},
 {'cat': '🧭 위치 자세히 말하기',
  'ko': '내 친구는 공원 옆에 있어. 나는 그를 찾을 수 있어.',
  'blank': 'My friend is ______ the park, so I can ______ him.',
  'answer': 'My friend is next to the park, so I can find him.',
  'hint': 'next to / find',
  'emoji': '🌳'},
 {'cat': '🧭 위치 자세히 말하기',
  'ko': '내 표는 가방 안에 있어. 하지만 열쇠는 탁자 위에 있어.',
  'blank': 'My ticket is ______ my bag, but my key is ______ the table.',
  'answer': 'My ticket is in my bag, but my key is on the table.',
  'hint': 'in / on',
  'emoji': '🎫'},
 {'cat': '💭 원하는 것 말하기',
  'ko': '나는 물을 원해. 왜냐하면 목이 말라.',
  'blank': 'I want ______ because I am ______.',
  'answer': 'I want water because I am thirsty.',
  'hint': 'water / thirsty',
  'emoji': '💧'},
 {'cat': '💭 원하는 것 말하기',
  'ko': '그녀는 새 휴대전화를 원해. 하지만 돈이 없어.',
  'blank': 'She wants a new ______, but she has no ______.',
  'answer': 'She wants a new phone, but she has no money.',
  'hint': 'phone / money',
  'emoji': '📱'},
 {'cat': '💭 원하는 것 말하기',
  'ko': '우리는 음식을 원해. 그리고 쉴 곳도 원해.',
  'blank': 'We want ______, and we want a place to ______.',
  'answer': 'We want food, and we want a place to rest.',
  'hint': 'food / rest',
  'emoji': '🍽️'},
 {'cat': '💭 원하는 것 말하기',
  'ko': '그들은 택시를 원해. 왜냐하면 버스가 없기 때문이야.',
  'blank': 'They want a ______ because there is no ______.',
  'answer': 'They want a taxi because there is no bus.',
  'hint': 'taxi / bus',
  'emoji': '🚕'},
 {'cat': '💭 원하는 것 말하기',
  'ko': '나는 이걸 원하지 않아. 나는 저걸 원해.',
  'blank': 'I do not ______ this. I ______ that.',
  'answer': 'I do not want this. I want that.',
  'hint': 'want / want',
  'emoji': '👉'},
 {'cat': '💭 원하는 것 말하기',
  'ko': '그는 커피를 원해. 하지만 나는 주스를 원해.',
  'blank': 'He wants ______, but I want ______.',
  'answer': 'He wants coffee, but I want juice.',
  'hint': 'coffee / juice',
  'emoji': '☕'},
 {'cat': '🚀 하고 싶은 일 말하기',
  'ko': '나는 집에 가고 싶어. 왜냐하면 피곤해.',
  'blank': 'I want to ______ home because I am ______.',
  'answer': 'I want to go home because I am tired.',
  'hint': 'go / tired',
  'emoji': '🏠'},
 {'cat': '🚀 하고 싶은 일 말하기',
  'ko': '그녀는 물을 마시고 싶어. 왜냐하면 목이 말라.',
  'blank': 'She wants to ______ water because she is ______.',
  'answer': 'She wants to drink water because she is thirsty.',
  'hint': 'drink / thirsty',
  'emoji': '🥤'},
 {'cat': '🚀 하고 싶은 일 말하기',
  'ko': '우리는 영어를 공부하고 싶어. 그래서 매일 연습해.',
  'blank': 'We want to ______ English, so we ______ every day.',
  'answer': 'We want to study English, so we practice every day.',
  'hint': 'study / practice',
  'emoji': '📘'},
 {'cat': '🚀 하고 싶은 일 말하기',
  'ko': '나는 피자를 먹고 싶어. 하지만 돈이 없어.',
  'blank': 'I want to ______ pizza, but I have no ______.',
  'answer': 'I want to eat pizza, but I have no money.',
  'hint': 'eat / money',
  'emoji': '🍕'},
 {'cat': '🚀 하고 싶은 일 말하기',
  'ko': '그는 자전거를 타고 싶어. 하지만 비가 와.',
  'blank': 'He wants to ______ a bike, but it is ______.',
  'answer': 'He wants to ride a bike, but it is raining.',
  'hint': 'ride / raining',
  'emoji': '🚲'},
 {'cat': '🚀 하고 싶은 일 말하기',
  'ko': '나는 너를 돕고 싶어. 그래서 여기에 있을게.',
  'blank': 'I want to ______ you, so I will ______ here.',
  'answer': 'I want to help you, so I will stay here.',
  'hint': 'help / stay',
  'emoji': '🤗'},
 {'cat': '🎒 가진 것 말하기',
  'ko': '나는 표가 있어. 그래서 역에 갈 수 있어.',
  'blank': 'I have a ______, so I can go to the ______.',
  'answer': 'I have a ticket, so I can go to the station.',
  'hint': 'ticket / station',
  'emoji': '🎫'},
 {'cat': '🎒 가진 것 말하기',
  'ko': '그는 돈이 없어. 그래서 물을 살 수 없어.',
  'blank': 'He has no ______, so he cannot buy ______.',
  'answer': 'He has no money, so he cannot buy water.',
  'hint': 'money / water',
  'emoji': '💸'},
 {'cat': '🎒 가진 것 말하기',
  'ko': '그녀는 새 자전거가 있어. 하지만 헬멧은 없어.',
  'blank': 'She has a new ______, but she does not have a ______.',
  'answer': 'She has a new bike, but she does not have a helmet.',
  'hint': 'bike / helmet',
  'emoji': '🚴'},
 {'cat': '🎒 가진 것 말하기',
  'ko': '우리는 지도가 있어. 그래서 길을 찾을 수 있어.',
  'blank': 'We have a ______, so we can find the ______.',
  'answer': 'We have a map, so we can find the way.',
  'hint': 'map / way',
  'emoji': '🗺️'},
 {'cat': '🎒 가진 것 말하기',
  'ko': '내 친구는 휴대전화가 있어. 나는 그에게 전화할 수 있어.',
  'blank': 'My friend has a ______, so I can ______ him.',
  'answer': 'My friend has a phone, so I can call him.',
  'hint': 'phone / call',
  'emoji': '📞'},
 {'cat': '🎒 가진 것 말하기',
  'ko': '나는 시간이 없어. 하지만 너를 도와주고 싶어.',
  'blank': 'I have no ______, but I want to ______ you.',
  'answer': 'I have no time, but I want to help you.',
  'hint': 'time / help',
  'emoji': '⏰'},
 {'cat': '🔗 이유와 조건 붙이기',
  'ko': '나는 배고파서 음식을 원해.',
  'blank': 'I want ______ because I am ______.',
  'answer': 'I want food because I am hungry.',
  'hint': 'food / hungry',
  'emoji': '🍽️'},
 {'cat': '🔗 이유와 조건 붙이기',
  'ko': '비가 오면 나는 집에 있을 거야.',
  'blank': 'If it ______, I will ______ home.',
  'answer': 'If it rains, I will stay home.',
  'hint': 'rains / stay',
  'emoji': '🌧️'},
 {'cat': '🔗 이유와 조건 붙이기',
  'ko': '나는 피곤하지만 공부할 거야.',
  'blank': 'I am ______, but I will ______.',
  'answer': 'I am tired, but I will study.',
  'hint': 'tired / study',
  'emoji': '📚'},
 {'cat': '🔗 이유와 조건 붙이기',
  'ko': '나는 목이 말라서 물을 마시고 싶어.',
  'blank': 'I am ______, so I want to ______ water.',
  'answer': 'I am thirsty, so I want to drink water.',
  'hint': 'thirsty / drink',
  'emoji': '💧'},
 {'cat': '🔗 이유와 조건 붙이기',
  'ko': '네가 도움이 필요하면 내가 도와줄 수 있어.',
  'blank': 'If you need ______, I can ______ you.',
  'answer': 'If you need help, I can help you.',
  'hint': 'help / help',
  'emoji': '🆘'},
 {'cat': '🔗 이유와 조건 붙이기',
  'ko': '나는 영어를 좋아해. 왜냐하면 재미있기 때문이야.',
  'blank': 'I like ______ because it is ______.',
  'answer': 'I like English because it is fun.',
  'hint': 'English / fun',
  'emoji': '😊'}]

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
            line-height: 1.35 !important;
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
            line-height: 1.2 !important;
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
            <label style="font-weight:900; color:#334155;">문장 구조 2 선택</label>
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
                font-size: 30px;
                font-weight: 900;
                color: #1f2937;
                line-height: 1.45;
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
                    font-size:24px;
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
                    display:none;
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

            <div id="answerBox" style="display:none;"></div>

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
    let autoNextTimer = null;

    const categorySelect = document.getElementById("categorySelect");
    const randomBtn = document.getElementById("randomBtn");
    const resetBtn = document.getElementById("resetBtn");
    const categoryLabel = document.getElementById("categoryLabel");
    const scoreLabel = document.getElementById("scoreLabel");
    const koPrompt = document.getElementById("koPrompt");
    const blankSentence = document.getElementById("blankSentence");
    const hintBox = document.getElementById("hintBox");
    const answerBox = document.getElementById("answerBox");
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

    function makeTwoLetterHint(answerWord) {
        if (!answerWord) return "";

        return answerWord.split(" ").map(word => {
            const clean = word.trim();
            if (clean.length <= 2) return clean;
            return clean.slice(0, 2) + "_".repeat(clean.length - 2);
        }).join(" ");
    }

    function normalizeText(text) {
        return text
            .toLowerCase()
            // 축약형을 먼저 풀어 줌
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
            .replace(/\s+/g, " ")
            .trim();
    }

    function wordsOnly(text) {
        return normalizeText(text)
            .split(" ")
            .filter(w => w.length > 0);
    }

    function editDistance(a, b) {
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
        const maxLen = Math.max(a.length, b.length);

        return 1 - (dist / maxLen);
    }

    function isSmallRecognitionMistake(spokenWord, answerWord) {
        if (!spokenWord || !answerWord) return false;
        if (spokenWord === answerWord) return true;

        const dist = editDistance(spokenWord, answerWord);
        const maxLen = Math.max(spokenWord.length, answerWord.length);
        const sim = wordSimilarity(spokenWord, answerWord);

        // 아주 짧은 단어는 엄격하게 채점
        // 예: I, a, am, go, do, is, it 등
        if (answerWord.length <= 2) {
            return dist === 0;
        }

        // 3~4글자 단어는 1글자 정도만 허용
        // 예: sick → sik, cold → col 정도는 허용
        // 하지만 완전히 다른 단어는 오답
        if (answerWord.length <= 4) {
            return dist <= 1 && sim >= 0.75;
        }

        // 5글자 이상 단어는 음성 인식 오류를 조금 더 허용
        // 예: hungry → hungri, thirsty → thursty 정도 허용
        if (answerWord.length >= 5) {
            return dist <= 1 || sim >= 0.82;
        }

        return false;
    }

    function isCloseEnough(spoken, answer) {
        const s = normalizeText(spoken);
        const a = normalizeText(answer);

        if (!s || !a) return false;

        // 완전히 같으면 바로 정답
        if (s === a) return true;

        const spokenWords = wordsOnly(s);
        const answerWords = wordsOnly(a);

        // 단어 개수가 다르면 오답
        // 예: "hungry"만 말함 → 오답
        // 예: "I hungry" → 오답
        if (spokenWords.length !== answerWords.length) {
            return false;
        }

        let weakMatchCount = 0;

        for (let i = 0; i < answerWords.length; i++) {
            const sw = spokenWords[i];
            const aw = answerWords[i];

            if (sw === aw) {
                continue;
            }

            if (isSmallRecognitionMistake(sw, aw)) {
                weakMatchCount += 1;
                continue;
            }

            // 한 단어라도 완전히 다르면 오답
            // 예: I am tired ≠ I am hungry
            return false;
        }

        // 짧은 문장에서 애매하게 맞은 단어가 너무 많으면 오답
        // 예: 3~4단어 문장에서 2단어 이상이 부정확하면 오답
        if (answerWords.length <= 4 && weakMatchCount >= 2) {
            return false;
        }

        // 긴 문장에서도 절반 가까이 애매하면 오답
        if (answerWords.length >= 5 && weakMatchCount >= Math.ceil(answerWords.length / 2)) {
            return false;
        }

        return true;
    }

    function isCorrectSpeech(spoken, answer) {
        return isCloseEnough(spoken, answer);
    }

    function escapeHtml(text) {
        return text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    function highlightTranscript(spoken, answer) {
        const spokenWordsRaw = spoken.trim().split(/\s+/).filter(w => w.length > 0);
        const spokenWordsNorm = wordsOnly(spoken);
        const answerWordsNorm = wordsOnly(answer);

        if (spokenWordsRaw.length === 0) {
            return "아직 말하지 않았습니다.";
        }

        let html = "";

        for (let i = 0; i < spokenWordsRaw.length; i++) {
            const raw = escapeHtml(spokenWordsRaw[i]);
            const norm = spokenWordsNorm[i] || "";
            const target = answerWordsNorm[i] || "";

            let bg = "#fee2e2";
            let color = "#991b1b";
            let border = "#fecaca";

            if (isSmallRecognitionMistake(norm, target)) {
                bg = "#dcfce7";
                color = "#166534";
                border = "#bbf7d0";
            }

            html += "<span style='display:inline-block; margin:3px 4px; padding:5px 9px; border-radius:999px; background:" +
                    bg + "; color:" + color + "; border:1px solid " + border + "; font-weight:900;'>" +
                    raw + "</span>";
        }

        if (spokenWordsNorm.length < answerWordsNorm.length) {
            const missing = answerWordsNorm.slice(spokenWordsNorm.length);
            missing.forEach(w => {
                html += "<span style='display:inline-block; margin:3px 4px; padding:5px 9px; border-radius:999px; background:#f1f5f9; color:#64748b; border:1px dashed #cbd5e1; font-weight:900;'>"
                        + w + "</span>";
            });
        }

        return html;
    }


    function makeBlankSentenceHtml(blankText) {
        const parts = blankText.split(/(______)/g);

        return parts.map(part => {
            if (part === "______") {
                return "<span style='display:inline-block; min-width:120px; height:42px; vertical-align:middle; background:#e0f2fe; border-radius:14px; margin:0 6px; border:1.5px solid #bae6fd;'></span>";
            }

            return escapeHtml(part);
        }).join("");
    }

    function makeSpokenSentenceHtml(spoken, answer) {
        const spokenWordsRaw = spoken.trim().split(/\s+/).filter(w => w.length > 0);
        const spokenWordsNorm = wordsOnly(spoken);
        const answerWordsNorm = wordsOnly(answer);

        if (spokenWordsRaw.length === 0) {
            return makeBlankSentenceHtml(currentItem.blank);
        }

        let html = "";

        for (let i = 0; i < spokenWordsRaw.length; i++) {
            const raw = escapeHtml(spokenWordsRaw[i]);
            const norm = spokenWordsNorm[i] || "";
            const target = answerWordsNorm[i] || "";

            let bg = "#fee2e2";
            let color = "#991b1b";
            let border = "#fecaca";

            if (isSmallRecognitionMistake(norm, target)) {
                bg = "#dcfce7";
                color = "#166534";
                border = "#bbf7d0";
            }

            html += "<span style='display:inline-block; margin:4px 5px; padding:6px 11px; border-radius:999px; background:" +
                    bg + "; color:" + color + "; border:1px solid " + border + "; font-weight:900;'>" +
                    raw + "</span>";
        }

        if (spokenWordsNorm.length < answerWordsNorm.length) {
            const missing = answerWordsNorm.slice(spokenWordsNorm.length);
            missing.forEach(w => {
                html += "<span style='display:inline-block; margin:4px 5px; padding:6px 11px; border-radius:999px; background:#f1f5f9; color:#94a3b8; border:1px dashed #cbd5e1; font-weight:900;'>"
                        + w + "</span>";
            });
        }

        return html;
    }

    function makeAnswerSentenceHtml(answer) {
        return answer.split(/\s+/).map(word => {
            return "<span style='display:inline-block; margin:4px 5px; padding:6px 11px; border-radius:999px; background:#dcfce7; color:#166534; border:1px solid #bbf7d0; font-weight:900;'>" +
                    escapeHtml(word) + "</span>";
        }).join("");
    }


    function updateScore() {
        scoreLabel.innerText = "정답 " + score + "개";
    }

    function loadQuestion(index = 0) {
        if (currentList.length === 0) {
            currentList = getFilteredItems();
        }

        if (index >= currentList.length) index = 0;
        if (index < 0) index = currentList.length - 1;

        if (autoNextTimer) {
            clearTimeout(autoNextTimer);
            autoNextTimer = null;
        }

        currentIndex = index;
        currentItem = currentList[currentIndex];
        alreadyCorrect = false;

        categoryLabel.innerText = currentItem.cat + " · " + (currentIndex + 1) + " / " + currentList.length;
        const emoji = currentItem.emoji || "🛟";
        koPrompt.innerHTML =
            "<span style='font-size:42px; margin-right:10px; vertical-align:middle;'>" + emoji + "</span>" +
            "<span style='vertical-align:middle;'>" + currentItem.ko + "</span>";
        blankSentence.innerText = currentItem.blank;
        hintBox.style.display = "none";
        answerBox.style.display = "none";
        hintBox.innerText = "";
        answerBox.innerText = "";
        transcriptBox.innerText = "";

        // 처음에는 힌트와 말하기 버튼만 보이게 함
        hintBtn.style.display = "inline-block";
        micBtn.style.display = "inline-block";
        answerBtn.style.display = "none";
        listenBtn.style.display = "none";
        nextBtn.style.display = "none";

        resultBox.style.display = "none";
        resultBox.innerText = "";
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

    function goNextQuestion() {
        if (autoNextTimer) {
            clearTimeout(autoNextTimer);
            autoNextTimer = null;
        }
        loadQuestion(currentIndex + 1);
    }

    function checkSpeech(spokenText) {
        if (isCorrectSpeech(spokenText, currentItem.answer)) {
            if (!alreadyCorrect) {
                score += 1;
                alreadyCorrect = true;
            }

            updateScore();

            resultBox.style.display = "block";
            resultBox.style.color = "#166534";
            resultBox.innerText = "정답입니다! 다음 문제로 넘어갑니다.";

            answerBox.style.display = "none";
            transcriptBox.innerText = currentItem.answer;

            answerBtn.style.display = "none";
            listenBtn.style.display = "inline-block";
            nextBtn.style.display = "inline-block";

            speak(currentItem.answer);

            autoNextTimer = setTimeout(function() {
                if (alreadyCorrect) {
                    goNextQuestion();
                }
            }, 1000);
        } else {
            resultBox.style.display = "block";
            resultBox.style.color = "#991b1b";
            resultBox.innerText = "아직 정답으로 인식되지 않았습니다. 다시 말하거나, 정답을 보고 연습한 뒤 다시 말해 보세요.";

            // 틀린 경우에는 정답 개수에 포함하지 않음
            // 대신 정답을 보고 다시 말해서 맞히면 그때 정답으로 인정함
            answerBtn.style.display = "inline-block";
            listenBtn.style.display = "none";
            nextBtn.style.display = "inline-block";
        }
    }

    async function startRecognition() {
        if (!SpeechRecognition) {
            transcriptBox.innerText = "Chrome에서 열어 주세요.";
            return;
        }

        // 모바일에서 먼저 마이크 권한 요청
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                stream.getTracks().forEach(track => track.stop());
            } catch (err) {
                transcriptBox.innerText = "마이크 허용 후 다시 눌러 주세요.";
                return;
            }
        }

        window.speechSynthesis.cancel();

        recognition = new SpeechRecognition();
        recognition.lang = "en-US";
        recognition.interimResults = true;
        recognition.continuous = false;
        recognition.maxAlternatives = 3;

        micBtn.innerText = "👂";
        resultBox.style.display = "none";
        resultBox.innerText = "";
        transcriptBox.innerText = "";

        recognition.onresult = function(event) {
            let spokenText = "";
            let hasFinal = false;

            for (let i = 0; i < event.results.length; i++) {
                const piece = event.results[i][0].transcript.trim();
                if (piece) {
                    spokenText += (spokenText ? " " : "") + piece;
                }
                if (event.results[i].isFinal) {
                    hasFinal = true;
                }
            }

            transcriptBox.innerText = spokenText;

            if (hasFinal) {
                checkSpeech(spokenText);
            }
        };

        recognition.onerror = function(event) {
            if (event.error === "not-allowed" || event.error === "service-not-allowed") {
                transcriptBox.innerText = "마이크 허용 후 다시 눌러 주세요.";
            } else if (event.error === "no-speech") {
                transcriptBox.innerText = "인식하지 못했습니다. 다시 말하거나 다음 문제로 넘어갈 수 있습니다.";
                answerBtn.style.display = "inline-block";
                nextBtn.style.display = "inline-block";
                resultBox.style.display = "block";
                resultBox.style.color = "#64748b";
                resultBox.innerText = "인식 실패는 정답 개수에 포함되지 않습니다.";
            } else {
                transcriptBox.innerText = "인식이 잘 되지 않았습니다. 다시 말하거나 다음 문제로 넘어갈 수 있습니다.";
                answerBtn.style.display = "inline-block";
                nextBtn.style.display = "inline-block";
                resultBox.style.display = "block";
                resultBox.style.color = "#64748b";
                resultBox.innerText = "인식 실패는 정답 개수에 포함되지 않습니다.";
            }
            micBtn.innerText = "🎙️";
        };

        recognition.onend = function() {
            micBtn.innerText = "🎙️";
        };

        try {
            recognition.start();
        } catch (err) {
            transcriptBox.innerText = "다시 눌러 주세요.";
            micBtn.innerText = "🎙️";
        }
    }

    categorySelect.addEventListener("change", function() {
        currentList = getFilteredItems();
        currentIndex = 0;
        loadQuestion(0);
    });

    randomBtn.addEventListener("click", function() {
        currentList = shuffleArray(getFilteredItems());
        loadQuestion(0);
    });

    resetBtn.addEventListener("click", function() {
        score = 0;
        alreadyCorrect = false;
        updateScore();
        resultBox.style.display = "none";
        resultBox.innerText = "";
    });

    hintBtn.addEventListener("click", function() {
        hintBox.style.display = "block";
        hintBox.innerText = makeTwoLetterHint(currentItem.hint);
    });

    listenBtn.addEventListener("click", function() {
        speak(currentItem.answer);
    });

    answerBtn.addEventListener("click", function() {
        answerBox.style.display = "none";
        transcriptBox.innerText = currentItem.answer;
        listenBtn.style.display = "inline-block";
        nextBtn.style.display = "inline-block";
        speak(currentItem.answer);

        resultBox.style.display = "block";
        resultBox.style.color = "#166534";
        resultBox.innerText = "정답을 듣고 다시 말해 보세요. 다시 정확히 말하면 정답으로 인정됩니다.";
    });

    micBtn.addEventListener("click", startRecognition);

    nextBtn.addEventListener("click", function() {
        // 정답을 말하지 않고 넘어가면 정답 개수에는 포함하지 않음
        goNextQuestion();
    });

    initCategories();
    currentList = getFilteredItems();
    updateScore();
    loadQuestion(0);
    </script>
    """

    html = html.replace("__ITEMS_JSON__", items_json)
    components.html(html, height=840)


speaking_practice_component(PRACTICE_ITEMS)
