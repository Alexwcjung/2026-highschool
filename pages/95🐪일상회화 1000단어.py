import streamlit as st
from gtts import gTTS
import io
import random
import base64
import uuid
import re
import json
import streamlit.components.v1 as components

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Daily English 1000",
    page_icon="🌱",
    layout="wide"
)

# =========================
# CSS 디자인
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 44px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 4px;
    }

    .sub-title {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 24px;
    }

    .hero-box {
        background: linear-gradient(135deg, #dcfce7 0%, #e0f2fe 50%, #fef3c7 100%);
        border-radius: 26px;
        padding: 28px 30px;
        margin-bottom: 28px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
    }

    .hero-title {
        font-size: 27px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 10px;
    }

    .hero-text {
        font-size: 16px;
        color: #374151;
        line-height: 1.8;
    }

    .theme-header {
        background: linear-gradient(135deg, #22c55e 0%, #0ea5e9 50%, #8b5cf6 100%);
        color: white;
        padding: 22px 26px;
        border-radius: 24px;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(34,197,94,0.25);
    }

    .theme-title {
        font-size: 27px;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .theme-desc {
        font-size: 15px;
        opacity: 0.95;
    }

    .dialogue-box {
        background: #fefce8;
        border: 1px solid #fde68a;
        border-radius: 24px;
        padding: 20px 22px;
        margin-bottom: 24px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    .dialogue-title {
        font-size: 24px;
        font-weight: 900;
        color: #854d0e;
        margin-bottom: 14px;
    }

    .dialogue-line {
        font-size: 18px;
        font-weight: 900;
        color: #111827;
        margin-top: 10px;
    }

    .dialogue-meaning {
        font-size: 15px;
        color: #6b7280;
        margin-bottom: 5px;
    }

    .word-card {
        background: white;
        border-radius: 18px;
        padding: 10px 14px;
        margin-bottom: 8px;
        border: 1px solid #dcfce7;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }

    .word-row {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .word-number {
        min-width: 38px;
        font-size: 13px;
        font-weight: 900;
        color: #166534;
        background: #dcfce7;
        border-radius: 999px;
        padding: 5px 9px;
        text-align: center;
    }

    .word-text {
        min-width: 170px;
        font-size: 25px;
        font-weight: 900;
        color: #111827;
    }

    .meaning-text {
        font-size: 19px;
        font-weight: 800;
        color: #374151;
        margin-left: 8px;
    }

    .emoji-text {
        font-size: 25px;
        line-height: 1;
        text-align: center;
        padding-top: 2px;
    }

    .quiz-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 22px 24px;
        margin-bottom: 18px;
        border: 1px solid #dbeafe;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    }

    .quiz-number {
        display: inline-block;
        background: #dbeafe;
        color: #1d4ed8;
        padding: 6px 12px;
        border-radius: 999px;
        font-weight: 900;
        font-size: 13px;
        margin-bottom: 10px;
    }

    .quiz-word {
        font-size: 34px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 8px;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 24px;
        padding: 24px 26px;
        margin: 20px 0;
        border: 1px solid #bbf7d0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    .score-title {
        font-size: 27px;
        font-weight: 900;
        color: #14532d;
    }

    .wrong-box {
        background: #fff7ed;
        border-left: 6px solid #fb923c;
        border-radius: 18px;
        padding: 16px 18px;
        margin: 18px 0;
        color: #7c2d12;
        font-weight: 700;
    }

    .answer-box {
        background: #f8fafc;
        border-radius: 20px;
        padding: 18px 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }


    .cassette-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #eff6ff 50%, #fff7ed 100%);
        border: 1px solid #bbf7d0;
        border-radius: 24px;
        padding: 22px 24px;
        margin: 18px 0 18px 0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }

    .cassette-title {
        font-size: 25px;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 8px;
    }

    .cassette-text {
        font-size: 15px;
        color: #475569;
        line-height: 1.7;
        margin-bottom: 14px;
    }

    div[data-testid="stRadio"] > label {
        font-weight: 800;
        color: #374151;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        border: 1px solid #d1d5db;
        padding: 0.45rem 1rem;
    }

    .stButton > button:hover {
        border-color: #22c55e;
        color: #22c55e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 상단 제목
# =========================
st.markdown("<div class='main-title'>🌱 Daily English 1000</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>기초 일상대화에 필요한 단어와 문장을 듣고, 읽고, 퀴즈로 익혀 봅시다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🌟 오늘의 학습 방식</div>
        <div class="hero-text">
            • 각 테마는 <b>오늘의 일상 대화</b>로 시작합니다.<br>
            • 대화를 듣고, 아래에서 핵심 단어를 익힙니다.<br>
            • 단어 발음은 <b>20번 반복</b>됩니다.<br>
            • 맨 앞 <b>전체 카세트 듣기</b> 탭에서 전체 단어를 순서대로 복습할 수 있습니다.<br>
            • gTTS 오류를 막기 위해 전체 단어를 <b>10개씩 나누어</b> 카세트로 만듭니다.<br>
            • <b>중지 버튼</b>을 누르면 반복 발음이 바로 멈춥니다.<br>
            • 다른 단어 또는 대화 듣기를 누르면 <b>이전에 재생되던 소리는 자동으로 멈춥니다.</b><br>
            • 단어, 발음 버튼, 뜻이 한 줄에 가깝게 배치되어 빠르게 익힐 수 있습니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS 함수
# =========================
@st.cache_data
def make_tts_audio(text, lang="en", tld="com"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def remove_speaker_label(sentence):
    return re.sub(r"^[A-Z]:\s*", "", sentence).strip()


def make_dialogue_tts_text(dialogue):
    return " ".join([remove_speaker_label(item["en"]) for item in dialogue])


def get_word_emoji(word):
    """단어별로 최대한 어울리는 이모지를 붙입니다."""
    emoji_map = {
        # 학교생활
        "subject": "📚", "math": "➗", "science": "🔬", "history": "🏛️", "music": "🎵",
        "art": "🎨", "P.E.": "🏃", "club": "👥", "schedule": "🗓️", "semester": "🏫",
        "assignment": "📝", "project": "📁", "presentation": "🗣️", "report": "📄", "textbook": "📘",
        "workbook": "📗", "library": "📚", "cafeteria": "🍽️", "hallway": "🚶", "attendance": "✅",

        # 교실 활동
        "copy": "✍️", "repeat": "🔁", "underline": "〽️", "circle": "⭕", "choose": "☝️",
        "check": "✅", "match": "🧩", "complete": "🏁", "fill": "🖊️", "spell": "🔤",
        "pronounce": "🗣️", "review": "🔎", "explain": "💬", "describe": "🖼️", "compare": "⚖️",
        "discuss": "🗨️", "present": "📢", "take notes": "📝", "turn in": "📥", "hand out": "📤",

        # 집과 생활
        "living room": "🛋️", "bedroom": "🛏️", "kitchen": "🍳", "balcony": "🌇", "floor": "🧱",
        "wall": "🧱", "roof": "🏠", "garden": "🌷", "yard": "🌳", "sofa": "🛋️",
        "television": "📺", "refrigerator": "🧊", "microwave": "♨️", "blanket": "🛌", "pillow": "🛏️",
        "towel": "🧺", "soap": "🧼", "mirror": "🪞", "closet": "🚪", "trash": "🗑️",

        # 하루 일과
        "routine": "🔄", "wake up": "⏰", "get up": "🌅", "brush": "🪥", "shower": "🚿",
        "dress": "👕", "leave": "🚪", "arrive": "📍", "return": "↩️", "finish": "🏁",
        "relax": "😌", "weekday": "📅", "weekend": "🎉", "usually": "🔁", "often": "🔂",
        "sometimes": "🤔", "always": "♾️", "never": "🚫", "habit": "🔁", "lifestyle": "🌿",

        # 취미와 여가
        "hobby": "🎯", "movie": "🎬", "drama": "📺", "song": "🎵", "concert": "🎤",
        "dance": "💃", "drawing": "✏️", "painting": "🖌️", "comic": "💬", "novel": "📖",
        "photography": "📷", "cooking": "🍳", "baking": "🍞", "camping": "⛺", "hiking": "🥾",
        "fishing": "🎣", "free time": "🕒", "favorite": "⭐", "popular": "🔥", "relaxing": "😌",

        # 운동과 활동
        "soccer": "⚽", "baseball": "⚾", "basketball": "🏀", "volleyball": "🏐", "tennis": "🎾",
        "badminton": "🏸", "swimming": "🏊", "cycling": "🚴", "skating": "⛸️", "boxing": "🥊",
        "taekwondo": "🥋", "yoga": "🧘", "fitness": "💪", "field": "🏟️", "court": "🎾",
        "stadium": "🏟️", "coach": "📣", "match": "🏆", "competition": "🏁", "medal": "🏅",

        # 날씨와 계절
        "season": "🍂", "spring": "🌸", "summer": "☀️", "fall": "🍁", "winter": "❄️",
        "cloudy": "☁️", "rainy": "🌧️", "snowy": "🌨️", "windy": "🌬️", "stormy": "⛈️",
        "foggy": "🌫️", "dry": "🏜️", "wet": "💦", "humid": "💧", "temperature": "🌡️",
        "degree": "🌡️", "forecast": "📡", "umbrella": "☂️", "raincoat": "🧥", "rainbow": "🌈",

        # 자연과 환경
        "nature": "🌿", "environment": "🌎", "plant": "🌱", "forest": "🌲", "lake": "🏞️",
        "ocean": "🌊", "island": "🏝️", "desert": "🏜️", "farm": "🚜", "village": "🏘️",
        "leaf": "🍃", "root": "🌱", "stone": "🪨", "sand": "🏖️", "soil": "🌱",
        "plastic": "🥤", "recycle": "♻️", "protect": "🛡️", "pollution": "🏭",

        # 식당과 주문
        "restaurant": "🍽️", "menu": "📋", "seat": "💺", "waiter": "🤵", "waitress": "🤵‍♀️",
        "order": "🛎️", "dish": "🍛", "meal": "🍽️", "soup": "🍲", "salad": "🥗",
        "steak": "🥩", "pizza": "🍕", "pasta": "🍝", "burger": "🍔", "sandwich": "🥪",
        "dessert": "🍰", "spicy": "🌶️", "sweet": "🍬", "bill": "🧾", "receipt": "🧾",

        # 쇼핑과 가격
        "shop": "🏪", "market": "🛒", "mall": "🏬", "supermarket": "🛒", "cashier": "💁",
        "customer": "🧑", "price": "💰", "sale": "🏷️", "discount": "🔻", "coupon": "🎟️",
        "change": "💵", "coin": "🪙", "expensive": "💸", "cheap": "👍", "size": "📏",
        "color": "🎨", "brand": "🏷️", "exchange": "🔄", "refund": "↩️",

        # 옷과 외모
        "T-shirt": "👕", "pants": "👖", "jeans": "👖", "shorts": "🩳", "skirt": "👗",
        "dress": "👗", "jacket": "🧥", "coat": "🧥", "sweater": "🧶", "hoodie": "🧥",
        "uniform": "🎽", "socks": "🧦", "sneakers": "👟", "boots": "🥾", "sandals": "🩴",
        "scarf": "🧣", "gloves": "🧤", "belt": "👖", "glasses": "👓", "comfortable": "😌",

        # 교통과 길 찾기
        "bus stop": "🚏", "subway": "🚇", "airport": "✈️", "terminal": "🚌", "platform": "🚉",
        "route": "🗺️", "direction": "➡️", "straight": "⬆️", "corner": "↪️", "block": "🏙️",
        "traffic": "🚦", "crosswalk": "🚸", "sidewalk": "🚶", "bridge": "🌉", "tunnel": "🚇",
        "entrance": "🚪", "exit": "🚪", "transfer": "🔁", "lost": "😵", "guide": "🧭",

        # 여행과 숙박
        "travel": "✈️", "trip": "🧳", "vacation": "🏖️", "tourist": "📸", "passport": "🛂",
        "flight": "🛫", "hotel": "🏨", "motel": "🏩", "hostel": "🛏️", "reservation": "📅",
        "check in": "🔑", "check out": "👋", "luggage": "🧳", "suitcase": "🧳", "backpack": "🎒",
        "souvenir": "🎁", "museum": "🏛️", "famous": "⭐", "local": "📍",

        # 친구 관계
        "friendship": "🤝", "best friend": "👯", "teammate": "👥", "partner": "🤝", "message": "💬",
        "call": "📞", "chat": "💬", "invite": "✉️", "visit": "🏠", "meet": "🤝",
        "hang out": "🎉", "laugh": "😂", "share": "🤲", "trust": "🤝", "promise": "🤞",
        "secret": "🤫", "joke": "😄", "together": "👥", "alone": "🚶", "forgive": "🫶",

        # 감정 표현 확장
        "excited": "🤩", "nervous": "😬", "bored": "🥱", "surprised": "😲", "confused": "😕",
        "embarrassed": "😳", "proud": "😊", "disappointed": "😞", "lonely": "🥲", "relaxed": "😌",
        "calm": "🧘", "upset": "😟", "interested": "🧐", "satisfied": "😌", "thankful": "🙏",
        "hopeful": "🌟", "mood": "🙂", "stress": "😣", "confidence": "💪", "courage": "🦁",

        # 생각과 의견
        "think": "💭", "believe": "🙏", "guess": "🤔", "remember": "🧠", "forget": "💨",
        "mean": "💡", "agree": "👍", "disagree": "👎", "opinion": "💬", "idea": "💡",
        "reason": "❓", "example": "🔎", "fact": "✅", "choice": "☝️", "decision": "✅",
        "advice": "💡", "suggestion": "💬", "possible": "✅", "impossible": "🚫", "confusing": "😵",

        # 계획과 약속
        "plan": "📝", "appointment": "📅", "meeting": "👥", "date": "📆", "event": "🎪",
        "party": "🎉", "festival": "🎊", "deadline": "⏳", "calendar": "📅", "next week": "➡️",
        "join": "🙋", "prepare": "🎒", "decide": "✅", "cancel": "❌", "on time": "⏰",
        "available": "🟢", "reminder": "🔔",

        # 건강한 생활
        "health": "🩺", "body": "🧍", "eye": "👁️", "ear": "👂", "nose": "👃",
        "mouth": "👄", "tooth": "🦷", "hand": "✋", "arm": "💪", "leg": "🦵",
        "foot": "🦶", "stomach": "🤰", "back": "🔙", "heart": "❤️", "clinic": "🏥",
        "vitamin": "💊", "diet": "🥗", "cough": "😷", "flu": "🤒", "breathe": "🌬️",

        # 미디어와 스마트폰
        "smartphone": "📱", "screen": "🖥️", "app": "📲", "website": "🌐", "internet": "🌐",
        "Wi-Fi": "📶", "password": "🔐", "text": "💬", "video call": "📹", "gallery": "🖼️",
        "news": "📰", "channel": "📺", "post": "📝", "comment": "💬", "upload": "⬆️",
        "download": "⬇️", "search": "🔎", "click": "🖱️", "battery": "🔋", "notification": "🔔",

        # 직업과 미래
        "job": "💼", "work": "💼", "company": "🏢", "office": "🏢", "factory": "🏭",
        "engineer": "🛠️", "mechanic": "🔧", "chef": "👨‍🍳", "firefighter": "🚒", "farmer": "🚜",
        "designer": "🎨", "singer": "🎤", "actor": "🎭", "athlete": "🏃", "dream": "🌈",
        "future": "🔮", "goal": "🎯", "skill": "🛠️", "interview": "🎙️", "experience": "🌱",
    }
    return emoji_map.get(word, "🌱")


# =========================
# 단어용 HTML 오디오 플레이어
# =========================
def html_word_audio_player(label, text, repeat_count=20, pause_ms=1500, height=48):
    audio_bytes = make_tts_audio(text)
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    audio_id = f"audio_{uuid.uuid4().hex}"
    play_btn_id = f"play_btn_{uuid.uuid4().hex}"
    stop_btn_id = f"stop_btn_{uuid.uuid4().hex}"
    status_id = f"status_{uuid.uuid4().hex}"
    player_id = f"player_{uuid.uuid4().hex}"

    safe_label = json.dumps(label)
    safe_text = json.dumps(text)
    safe_player_id = json.dumps(player_id)

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; gap:6px; height:42px;">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #dcfce7, #dbeafe);
                border: 1px solid #bbf7d0;
                border-radius: 999px;
                padding: 6px 10px;
                font-weight: 800;
                font-size: 13px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.06);
                white-space: nowrap;
            ">
                {label}
            </button>

            <button id="{stop_btn_id}" style="
                background: #fff7ed;
                border: 1px solid #fed7aa;
                border-radius: 999px;
                padding: 6px 10px;
                font-weight: 800;
                font-size: 13px;
                color: #9a3412;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.04);
                white-space: nowrap;
            ">
                ⏹ 중지
            </button>

            <span id="{status_id}" style="
                font-size: 12px;
                color: #075985;
                font-weight: 700;
                white-space: nowrap;
            "></span>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");

            let count = 0;
            let timer = null;
            let isStopped = false;

            const maxCount = {repeat_count};
            const pauseMs = {pause_ms};
            const labelText = {safe_label};
            const wordText = {safe_text};
            const playerId = {safe_player_id};

            const channel = new BroadcastChannel("daily_english_audio_channel");

            function stopThisAudio(showMessage = false) {{
                isStopped = true;

                if (timer) {{
                    clearTimeout(timer);
                    timer = null;
                }}

                audio.pause();
                audio.currentTime = 0;
                count = 0;

                playBtn.disabled = false;
                playBtn.innerText = labelText;

                if (showMessage) {{
                    status.innerText = "중지됨";
                }} else {{
                    status.innerText = "";
                }}
            }}

            channel.onmessage = function(event) {{
                if (!event.data) return;

                if (event.data.type === "STOP_OTHERS" && event.data.playerId !== playerId) {{
                    stopThisAudio(false);
                }}
            }};

            function playOnce() {{
                if (isStopped) return;

                if (count >= maxCount) {{
                    status.innerText = "완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                    return;
                }}

                audio.currentTime = 0;

                audio.play().then(() => {{
                    count += 1;
                    status.innerText = count + "/" + maxCount;
                }}).catch((error) => {{
                    status.innerText = "다시 클릭";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }});
            }}

            audio.addEventListener("ended", function() {{
                if (isStopped) return;

                if (count < maxCount) {{
                    timer = setTimeout(playOnce, pauseMs);
                }} else {{
                    status.innerText = "완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }}
            }});

            playBtn.addEventListener("click", function() {{
                channel.postMessage({{
                    type: "STOP_OTHERS",
                    playerId: playerId
                }});

                stopThisAudio(false);

                isStopped = false;
                count = 0;
                playBtn.disabled = true;
                playBtn.innerText = "재생중";
                status.innerText = "시작";
                playOnce();
            }});

            stopBtn.addEventListener("click", function() {{
                stopThisAudio(true);
            }});
            </script>
        </div>
        """,
        height=height
    )


def audio_button(label, text, key=None):
    html_word_audio_player(
        label=label,
        text=text,
        repeat_count=20,
        pause_ms=1500,
        height=48
    )


# =========================
# 대화용 HTML 오디오 플레이어
# =========================
def html_dialogue_audio_player(label, dialogue_lines, line_pause_ms=1400, height=105):
    audio_data_list = []

    for line in dialogue_lines:
        clean_text = remove_speaker_label(line["en"])
        audio_bytes = make_tts_audio(clean_text)
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        audio_data_list.append({
            "text": clean_text,
            "src": f"data:audio/mp3;base64,{audio_base64}"
        })

    audio_json = json.dumps(audio_data_list)
    safe_label = json.dumps(label)

    audio_id = f"dialogue_audio_{uuid.uuid4().hex}"
    play_btn_id = f"dialogue_play_{uuid.uuid4().hex}"
    stop_btn_id = f"dialogue_stop_{uuid.uuid4().hex}"
    status_id = f"dialogue_status_{uuid.uuid4().hex}"
    player_id = f"dialogue_player_{uuid.uuid4().hex}"
    safe_player_id = json.dumps(player_id)

    components.html(
        f"""
        <div style="font-family: Arial, sans-serif;">
            <audio id="{audio_id}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #fef3c7, #dbeafe);
                border: 1px solid #fde68a;
                border-radius: 999px;
                padding: 9px 15px;
                font-weight: 800;
                font-size: 14px;
                color: #374151;
                cursor: pointer;
                box-shadow: 0 3px 8px rgba(0,0,0,0.08);
                margin-right: 6px;
            ">
                {label}
            </button>

            <button id="{stop_btn_id}" style="
                background: #fff7ed;
                border: 1px solid #fed7aa;
                border-radius: 999px;
                padding: 9px 15px;
                font-weight: 800;
                font-size: 14px;
                color: #9a3412;
                cursor: pointer;
                box-shadow: 0 3px 8px rgba(0,0,0,0.05);
            ">
                ⏹ 중지
            </button>

            <div id="{status_id}" style="
                margin-top: 8px;
                font-size: 13px;
                color: #075985;
                font-weight: 700;
            "></div>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");

            const dialogueAudios = {audio_json};
            const linePauseMs = {line_pause_ms};
            const labelText = {safe_label};
            const playerId = {safe_player_id};

            let index = 0;
            let timer = null;
            let isStopped = false;

            const channel = new BroadcastChannel("daily_english_audio_channel");

            function stopThisAudio(showMessage = false) {{
                isStopped = true;

                if (timer) {{
                    clearTimeout(timer);
                    timer = null;
                }}

                audio.pause();
                audio.currentTime = 0;
                index = 0;

                playBtn.disabled = false;
                playBtn.innerText = labelText;

                if (showMessage) {{
                    status.innerText = "⏹ 대화 듣기를 중지했습니다.";
                }} else {{
                    status.innerText = "";
                }}
            }}

            channel.onmessage = function(event) {{
                if (!event.data) return;

                if (event.data.type === "STOP_OTHERS" && event.data.playerId !== playerId) {{
                    stopThisAudio(false);
                }}
            }};

            function playCurrentLine() {{
                if (isStopped) return;

                if (index >= dialogueAudios.length) {{
                    status.innerText = "✅ 대화 재생 완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                    return;
                }}

                audio.src = dialogueAudios[index].src;
                audio.currentTime = 0;

                audio.play().then(() => {{
                    status.innerText = "🔊 대화 재생 중: " + (index + 1) + " / " + dialogueAudios.length;
                }}).catch((error) => {{
                    status.innerText = "⚠️ 소리 재생이 차단되었습니다. 버튼을 다시 눌러 주세요.";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }});
            }}

            audio.addEventListener("ended", function() {{
                if (isStopped) return;

                index += 1;

                if (index < dialogueAudios.length) {{
                    timer = setTimeout(playCurrentLine, linePauseMs);
                }} else {{
                    status.innerText = "✅ 대화 재생 완료";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }}
            }});

            playBtn.addEventListener("click", function() {{
                channel.postMessage({{
                    type: "STOP_OTHERS",
                    playerId: playerId
                }});

                stopThisAudio(false);

                isStopped = false;
                index = 0;
                playBtn.disabled = true;
                playBtn.innerText = "재생 중...";
                status.innerText = "🔊 대화 듣기를 시작합니다.";
                playCurrentLine();
            }});

            stopBtn.addEventListener("click", function() {{
                stopThisAudio(true);
            }});
            </script>
        </div>
        """,
        height=height
    )


# =========================
# Daily English 1000 테마별 단어
# =========================
word_themes = {
    "🏫 학교생활": [
        {"word": "subject", "meaning": "과목"},
        {"word": "math", "meaning": "수학"},
        {"word": "science", "meaning": "과학"},
        {"word": "history", "meaning": "역사"},
        {"word": "music", "meaning": "음악"},
        {"word": "art", "meaning": "미술"},
        {"word": "P.E.", "meaning": "체육"},
        {"word": "club", "meaning": "동아리"},
        {"word": "schedule", "meaning": "일정표"},
        {"word": "semester", "meaning": "학기"},
        {"word": "assignment", "meaning": "과제"},
        {"word": "project", "meaning": "프로젝트"},
        {"word": "presentation", "meaning": "발표"},
        {"word": "report", "meaning": "보고서"},
        {"word": "textbook", "meaning": "교과서"},
        {"word": "workbook", "meaning": "문제집"},
        {"word": "library", "meaning": "도서관"},
        {"word": "cafeteria", "meaning": "급식소, 식당"},
        {"word": "hallway", "meaning": "복도"},
        {"word": "attendance", "meaning": "출석"},
    ],

    "✏️ 교실 활동": [
        {"word": "copy", "meaning": "베껴 쓰다"},
        {"word": "repeat", "meaning": "반복하다"},
        {"word": "underline", "meaning": "밑줄 치다"},
        {"word": "circle", "meaning": "동그라미 치다"},
        {"word": "choose", "meaning": "고르다"},
        {"word": "check", "meaning": "확인하다"},
        {"word": "match", "meaning": "연결하다, 맞추다"},
        {"word": "complete", "meaning": "완성하다"},
        {"word": "fill", "meaning": "채우다"},
        {"word": "spell", "meaning": "철자를 말하다"},
        {"word": "pronounce", "meaning": "발음하다"},
        {"word": "review", "meaning": "복습하다"},
        {"word": "explain", "meaning": "설명하다"},
        {"word": "describe", "meaning": "묘사하다"},
        {"word": "compare", "meaning": "비교하다"},
        {"word": "discuss", "meaning": "토론하다"},
        {"word": "present", "meaning": "발표하다"},
        {"word": "take notes", "meaning": "필기하다"},
        {"word": "turn in", "meaning": "제출하다"},
        {"word": "hand out", "meaning": "나누어 주다"},
    ],

    "🏠 집과 생활": [
        {"word": "living room", "meaning": "거실"},
        {"word": "bedroom", "meaning": "침실"},
        {"word": "kitchen", "meaning": "부엌"},
        {"word": "balcony", "meaning": "발코니"},
        {"word": "floor", "meaning": "바닥, 층"},
        {"word": "wall", "meaning": "벽"},
        {"word": "roof", "meaning": "지붕"},
        {"word": "garden", "meaning": "정원"},
        {"word": "yard", "meaning": "마당"},
        {"word": "sofa", "meaning": "소파"},
        {"word": "television", "meaning": "텔레비전"},
        {"word": "refrigerator", "meaning": "냉장고"},
        {"word": "microwave", "meaning": "전자레인지"},
        {"word": "blanket", "meaning": "담요"},
        {"word": "pillow", "meaning": "베개"},
        {"word": "towel", "meaning": "수건"},
        {"word": "soap", "meaning": "비누"},
        {"word": "mirror", "meaning": "거울"},
        {"word": "closet", "meaning": "옷장"},
        {"word": "trash", "meaning": "쓰레기"},
    ],

    "🌅 하루 일과": [
        {"word": "routine", "meaning": "일과"},
        {"word": "wake up", "meaning": "잠에서 깨다"},
        {"word": "get up", "meaning": "일어나다"},
        {"word": "brush", "meaning": "닦다"},
        {"word": "shower", "meaning": "샤워하다"},
        {"word": "dress", "meaning": "옷을 입다"},
        {"word": "leave", "meaning": "떠나다"},
        {"word": "arrive", "meaning": "도착하다"},
        {"word": "return", "meaning": "돌아오다"},
        {"word": "finish", "meaning": "끝내다"},
        {"word": "relax", "meaning": "쉬다"},
        {"word": "weekday", "meaning": "평일"},
        {"word": "weekend", "meaning": "주말"},
        {"word": "usually", "meaning": "보통"},
        {"word": "often", "meaning": "자주"},
        {"word": "sometimes", "meaning": "가끔"},
        {"word": "always", "meaning": "항상"},
        {"word": "never", "meaning": "절대 ~않다"},
        {"word": "habit", "meaning": "습관"},
        {"word": "lifestyle", "meaning": "생활 방식"},
    ],

    "🎮 취미와 여가": [
        {"word": "hobby", "meaning": "취미"},
        {"word": "movie", "meaning": "영화"},
        {"word": "drama", "meaning": "드라마"},
        {"word": "song", "meaning": "노래"},
        {"word": "concert", "meaning": "콘서트"},
        {"word": "dance", "meaning": "춤"},
        {"word": "drawing", "meaning": "그림 그리기"},
        {"word": "painting", "meaning": "그림, 회화"},
        {"word": "comic", "meaning": "만화"},
        {"word": "novel", "meaning": "소설"},
        {"word": "photography", "meaning": "사진 촬영"},
        {"word": "cooking", "meaning": "요리"},
        {"word": "baking", "meaning": "빵 굽기"},
        {"word": "camping", "meaning": "캠핑"},
        {"word": "hiking", "meaning": "하이킹"},
        {"word": "fishing", "meaning": "낚시"},
        {"word": "free time", "meaning": "여가 시간"},
        {"word": "favorite", "meaning": "가장 좋아하는"},
        {"word": "popular", "meaning": "인기 있는"},
        {"word": "relaxing", "meaning": "편안한"},
    ],

    "⚽ 운동과 활동": [
        {"word": "soccer", "meaning": "축구"},
        {"word": "baseball", "meaning": "야구"},
        {"word": "basketball", "meaning": "농구"},
        {"word": "volleyball", "meaning": "배구"},
        {"word": "tennis", "meaning": "테니스"},
        {"word": "badminton", "meaning": "배드민턴"},
        {"word": "swimming", "meaning": "수영"},
        {"word": "cycling", "meaning": "자전거 타기"},
        {"word": "skating", "meaning": "스케이트 타기"},
        {"word": "boxing", "meaning": "복싱"},
        {"word": "taekwondo", "meaning": "태권도"},
        {"word": "yoga", "meaning": "요가"},
        {"word": "fitness", "meaning": "체력 운동"},
        {"word": "field", "meaning": "경기장, 들판"},
        {"word": "court", "meaning": "코트"},
        {"word": "stadium", "meaning": "경기장"},
        {"word": "coach", "meaning": "코치"},
        {"word": "match", "meaning": "경기"},
        {"word": "competition", "meaning": "대회"},
        {"word": "medal", "meaning": "메달"},
    ],

    "🌦️ 날씨와 계절": [
        {"word": "season", "meaning": "계절"},
        {"word": "spring", "meaning": "봄"},
        {"word": "summer", "meaning": "여름"},
        {"word": "fall", "meaning": "가을"},
        {"word": "winter", "meaning": "겨울"},
        {"word": "cloudy", "meaning": "흐린"},
        {"word": "rainy", "meaning": "비 오는"},
        {"word": "snowy", "meaning": "눈 오는"},
        {"word": "windy", "meaning": "바람 부는"},
        {"word": "stormy", "meaning": "폭풍우 치는"},
        {"word": "foggy", "meaning": "안개 낀"},
        {"word": "dry", "meaning": "건조한"},
        {"word": "wet", "meaning": "젖은"},
        {"word": "humid", "meaning": "습한"},
        {"word": "temperature", "meaning": "온도"},
        {"word": "degree", "meaning": "도"},
        {"word": "forecast", "meaning": "일기예보"},
        {"word": "umbrella", "meaning": "우산"},
        {"word": "raincoat", "meaning": "비옷"},
        {"word": "rainbow", "meaning": "무지개"},
    ],

    "🌳 자연과 환경": [
        {"word": "nature", "meaning": "자연"},
        {"word": "environment", "meaning": "환경"},
        {"word": "plant", "meaning": "식물"},
        {"word": "forest", "meaning": "숲"},
        {"word": "lake", "meaning": "호수"},
        {"word": "ocean", "meaning": "대양"},
        {"word": "island", "meaning": "섬"},
        {"word": "desert", "meaning": "사막"},
        {"word": "field", "meaning": "들판"},
        {"word": "farm", "meaning": "농장"},
        {"word": "village", "meaning": "마을"},
        {"word": "leaf", "meaning": "잎"},
        {"word": "root", "meaning": "뿌리"},
        {"word": "stone", "meaning": "돌"},
        {"word": "sand", "meaning": "모래"},
        {"word": "soil", "meaning": "흙"},
        {"word": "plastic", "meaning": "플라스틱"},
        {"word": "recycle", "meaning": "재활용하다"},
        {"word": "protect", "meaning": "보호하다"},
        {"word": "pollution", "meaning": "오염"},
    ],

    "🍽️ 식당과 주문": [
        {"word": "restaurant", "meaning": "식당"},
        {"word": "menu", "meaning": "메뉴"},
        {"word": "seat", "meaning": "자리"},
        {"word": "waiter", "meaning": "남자 종업원"},
        {"word": "waitress", "meaning": "여자 종업원"},
        {"word": "order", "meaning": "주문하다"},
        {"word": "dish", "meaning": "요리, 접시"},
        {"word": "meal", "meaning": "식사"},
        {"word": "soup", "meaning": "수프"},
        {"word": "salad", "meaning": "샐러드"},
        {"word": "steak", "meaning": "스테이크"},
        {"word": "pizza", "meaning": "피자"},
        {"word": "pasta", "meaning": "파스타"},
        {"word": "burger", "meaning": "버거"},
        {"word": "sandwich", "meaning": "샌드위치"},
        {"word": "dessert", "meaning": "디저트"},
        {"word": "spicy", "meaning": "매운"},
        {"word": "sweet", "meaning": "단"},
        {"word": "bill", "meaning": "계산서"},
        {"word": "receipt", "meaning": "영수증"},
    ],

    "🛍️ 쇼핑과 가격": [
        {"word": "shop", "meaning": "가게"},
        {"word": "market", "meaning": "시장"},
        {"word": "mall", "meaning": "쇼핑몰"},
        {"word": "supermarket", "meaning": "슈퍼마켓"},
        {"word": "cashier", "meaning": "계산원"},
        {"word": "customer", "meaning": "손님"},
        {"word": "price", "meaning": "가격"},
        {"word": "sale", "meaning": "할인 판매"},
        {"word": "discount", "meaning": "할인"},
        {"word": "coupon", "meaning": "쿠폰"},
        {"word": "change", "meaning": "거스름돈"},
        {"word": "coin", "meaning": "동전"},
        {"word": "bill", "meaning": "지폐, 계산서"},
        {"word": "expensive", "meaning": "비싼"},
        {"word": "cheap", "meaning": "싼"},
        {"word": "size", "meaning": "크기"},
        {"word": "color", "meaning": "색깔"},
        {"word": "brand", "meaning": "상표"},
        {"word": "exchange", "meaning": "교환하다"},
        {"word": "refund", "meaning": "환불"},
    ],

    "👕 옷과 외모": [
        {"word": "T-shirt", "meaning": "티셔츠"},
        {"word": "pants", "meaning": "바지"},
        {"word": "jeans", "meaning": "청바지"},
        {"word": "shorts", "meaning": "반바지"},
        {"word": "skirt", "meaning": "치마"},
        {"word": "dress", "meaning": "드레스, 원피스"},
        {"word": "jacket", "meaning": "재킷"},
        {"word": "coat", "meaning": "코트"},
        {"word": "sweater", "meaning": "스웨터"},
        {"word": "hoodie", "meaning": "후드티"},
        {"word": "uniform", "meaning": "교복, 제복"},
        {"word": "socks", "meaning": "양말"},
        {"word": "sneakers", "meaning": "운동화"},
        {"word": "boots", "meaning": "부츠"},
        {"word": "sandals", "meaning": "샌들"},
        {"word": "scarf", "meaning": "목도리"},
        {"word": "gloves", "meaning": "장갑"},
        {"word": "belt", "meaning": "벨트"},
        {"word": "glasses", "meaning": "안경"},
        {"word": "comfortable", "meaning": "편안한"},
    ],

    "🚇 교통과 길 찾기": [
        {"word": "bus stop", "meaning": "버스 정류장"},
        {"word": "subway", "meaning": "지하철"},
        {"word": "airport", "meaning": "공항"},
        {"word": "terminal", "meaning": "터미널"},
        {"word": "platform", "meaning": "승강장"},
        {"word": "route", "meaning": "경로"},
        {"word": "direction", "meaning": "방향"},
        {"word": "straight", "meaning": "똑바로"},
        {"word": "corner", "meaning": "모퉁이"},
        {"word": "block", "meaning": "구역, 블록"},
        {"word": "traffic", "meaning": "교통"},
        {"word": "crosswalk", "meaning": "횡단보도"},
        {"word": "sidewalk", "meaning": "인도"},
        {"word": "bridge", "meaning": "다리"},
        {"word": "tunnel", "meaning": "터널"},
        {"word": "entrance", "meaning": "입구"},
        {"word": "exit", "meaning": "출구"},
        {"word": "transfer", "meaning": "갈아타다"},
        {"word": "lost", "meaning": "길을 잃은"},
        {"word": "guide", "meaning": "안내하다, 안내자"},
    ],

    "🧳 여행과 숙박": [
        {"word": "travel", "meaning": "여행하다"},
        {"word": "trip", "meaning": "여행"},
        {"word": "vacation", "meaning": "방학, 휴가"},
        {"word": "tourist", "meaning": "관광객"},
        {"word": "guide", "meaning": "안내자"},
        {"word": "passport", "meaning": "여권"},
        {"word": "flight", "meaning": "항공편"},
        {"word": "hotel", "meaning": "호텔"},
        {"word": "motel", "meaning": "모텔"},
        {"word": "hostel", "meaning": "호스텔"},
        {"word": "reservation", "meaning": "예약"},
        {"word": "check in", "meaning": "체크인하다"},
        {"word": "check out", "meaning": "체크아웃하다"},
        {"word": "luggage", "meaning": "짐"},
        {"word": "suitcase", "meaning": "여행 가방"},
        {"word": "backpack", "meaning": "배낭"},
        {"word": "souvenir", "meaning": "기념품"},
        {"word": "museum", "meaning": "박물관"},
        {"word": "famous", "meaning": "유명한"},
        {"word": "local", "meaning": "현지의"},
    ],

    "👥 친구 관계": [
        {"word": "friendship", "meaning": "우정"},
        {"word": "best friend", "meaning": "가장 친한 친구"},
        {"word": "teammate", "meaning": "팀 동료"},
        {"word": "partner", "meaning": "짝, 파트너"},
        {"word": "message", "meaning": "메시지"},
        {"word": "call", "meaning": "전화하다"},
        {"word": "chat", "meaning": "채팅하다"},
        {"word": "invite", "meaning": "초대하다"},
        {"word": "visit", "meaning": "방문하다"},
        {"word": "meet", "meaning": "만나다"},
        {"word": "hang out", "meaning": "어울려 놀다"},
        {"word": "laugh", "meaning": "웃다"},
        {"word": "share", "meaning": "나누다, 공유하다"},
        {"word": "trust", "meaning": "믿다"},
        {"word": "promise", "meaning": "약속"},
        {"word": "secret", "meaning": "비밀"},
        {"word": "joke", "meaning": "농담"},
        {"word": "together", "meaning": "함께"},
        {"word": "alone", "meaning": "혼자"},
        {"word": "forgive", "meaning": "용서하다"},
    ],

    "😊 감정 표현 확장": [
        {"word": "excited", "meaning": "신난"},
        {"word": "nervous", "meaning": "긴장한"},
        {"word": "bored", "meaning": "지루한"},
        {"word": "surprised", "meaning": "놀란"},
        {"word": "confused", "meaning": "혼란스러운"},
        {"word": "embarrassed", "meaning": "당황한"},
        {"word": "proud", "meaning": "자랑스러운"},
        {"word": "disappointed", "meaning": "실망한"},
        {"word": "lonely", "meaning": "외로운"},
        {"word": "relaxed", "meaning": "편안한"},
        {"word": "calm", "meaning": "차분한"},
        {"word": "upset", "meaning": "속상한"},
        {"word": "interested", "meaning": "관심 있는"},
        {"word": "satisfied", "meaning": "만족한"},
        {"word": "thankful", "meaning": "감사하는"},
        {"word": "hopeful", "meaning": "희망적인"},
        {"word": "mood", "meaning": "기분"},
        {"word": "stress", "meaning": "스트레스"},
        {"word": "confidence", "meaning": "자신감"},
        {"word": "courage", "meaning": "용기"},
    ],

    "💭 생각과 의견": [
        {"word": "think", "meaning": "생각하다"},
        {"word": "believe", "meaning": "믿다"},
        {"word": "guess", "meaning": "추측하다"},
        {"word": "remember", "meaning": "기억하다"},
        {"word": "forget", "meaning": "잊다"},
        {"word": "mean", "meaning": "의미하다"},
        {"word": "agree", "meaning": "동의하다"},
        {"word": "disagree", "meaning": "동의하지 않다"},
        {"word": "opinion", "meaning": "의견"},
        {"word": "idea", "meaning": "생각, 아이디어"},
        {"word": "reason", "meaning": "이유"},
        {"word": "example", "meaning": "예시"},
        {"word": "fact", "meaning": "사실"},
        {"word": "choice", "meaning": "선택"},
        {"word": "decision", "meaning": "결정"},
        {"word": "advice", "meaning": "조언"},
        {"word": "suggestion", "meaning": "제안"},
        {"word": "possible", "meaning": "가능한"},
        {"word": "impossible", "meaning": "불가능한"},
        {"word": "confusing", "meaning": "혼란스러운"},
    ],

    "📅 계획과 약속": [
        {"word": "plan", "meaning": "계획"},
        {"word": "appointment", "meaning": "약속, 예약"},
        {"word": "promise", "meaning": "약속"},
        {"word": "meeting", "meaning": "모임, 회의"},
        {"word": "date", "meaning": "날짜, 데이트"},
        {"word": "event", "meaning": "행사"},
        {"word": "party", "meaning": "파티"},
        {"word": "festival", "meaning": "축제"},
        {"word": "deadline", "meaning": "마감일"},
        {"word": "calendar", "meaning": "달력"},
        {"word": "next week", "meaning": "다음 주"},
        {"word": "message", "meaning": "메시지"},
        {"word": "join", "meaning": "참여하다"},
        {"word": "prepare", "meaning": "준비하다"},
        {"word": "decide", "meaning": "결정하다"},
        {"word": "change", "meaning": "바꾸다"},
        {"word": "cancel", "meaning": "취소하다"},
        {"word": "on time", "meaning": "시간 맞춰"},
        {"word": "available", "meaning": "시간이 되는, 이용 가능한"},
        {"word": "reminder", "meaning": "알림"},
    ],

    "🩺 건강한 생활": [
        {"word": "health", "meaning": "건강"},
        {"word": "body", "meaning": "몸"},
        {"word": "eye", "meaning": "눈"},
        {"word": "ear", "meaning": "귀"},
        {"word": "nose", "meaning": "코"},
        {"word": "mouth", "meaning": "입"},
        {"word": "tooth", "meaning": "이"},
        {"word": "hand", "meaning": "손"},
        {"word": "arm", "meaning": "팔"},
        {"word": "leg", "meaning": "다리"},
        {"word": "foot", "meaning": "발"},
        {"word": "stomach", "meaning": "배, 위"},
        {"word": "back", "meaning": "등, 허리"},
        {"word": "heart", "meaning": "심장"},
        {"word": "clinic", "meaning": "의원, 진료소"},
        {"word": "vitamin", "meaning": "비타민"},
        {"word": "diet", "meaning": "식단"},
        {"word": "cough", "meaning": "기침"},
        {"word": "flu", "meaning": "독감"},
        {"word": "breathe", "meaning": "숨 쉬다"},
    ],

    "📱 미디어와 스마트폰": [
        {"word": "smartphone", "meaning": "스마트폰"},
        {"word": "screen", "meaning": "화면"},
        {"word": "app", "meaning": "앱"},
        {"word": "website", "meaning": "웹사이트"},
        {"word": "internet", "meaning": "인터넷"},
        {"word": "Wi-Fi", "meaning": "와이파이"},
        {"word": "password", "meaning": "비밀번호"},
        {"word": "text", "meaning": "문자 메시지"},
        {"word": "video call", "meaning": "영상 통화"},
        {"word": "gallery", "meaning": "사진첩"},
        {"word": "news", "meaning": "뉴스"},
        {"word": "channel", "meaning": "채널"},
        {"word": "post", "meaning": "게시물"},
        {"word": "comment", "meaning": "댓글"},
        {"word": "upload", "meaning": "업로드하다"},
        {"word": "download", "meaning": "다운로드하다"},
        {"word": "search", "meaning": "검색하다"},
        {"word": "click", "meaning": "클릭하다"},
        {"word": "battery", "meaning": "배터리"},
        {"word": "notification", "meaning": "알림"},
    ],

    "🌈 직업과 미래": [
        {"word": "job", "meaning": "직업"},
        {"word": "work", "meaning": "일하다"},
        {"word": "company", "meaning": "회사"},
        {"word": "office", "meaning": "사무실"},
        {"word": "factory", "meaning": "공장"},
        {"word": "engineer", "meaning": "기술자, 엔지니어"},
        {"word": "mechanic", "meaning": "정비사"},
        {"word": "chef", "meaning": "요리사"},
        {"word": "firefighter", "meaning": "소방관"},
        {"word": "farmer", "meaning": "농부"},
        {"word": "designer", "meaning": "디자이너"},
        {"word": "singer", "meaning": "가수"},
        {"word": "actor", "meaning": "배우"},
        {"word": "athlete", "meaning": "운동선수"},
        {"word": "dream", "meaning": "꿈"},
        {"word": "future", "meaning": "미래"},
        {"word": "goal", "meaning": "목표"},
        {"word": "skill", "meaning": "기술, 능력"},
        {"word": "interview", "meaning": "면접"},
        {"word": "experience", "meaning": "경험"},
    ],
}

# =========================
# 오늘의 일상 대화
# =========================
theme_dialogues = {
    "🏫 학교생활": [
        {"en": "A: What is your favorite subject?", "ko": "A: 네가 가장 좋아하는 과목은 뭐니?"},
        {"en": "B: My favorite subject is science.", "ko": "B: 내가 가장 좋아하는 과목은 과학이야."},
        {"en": "A: Do you have homework today?", "ko": "A: 오늘 숙제 있니?"},
        {"en": "B: Yes, I have a report.", "ko": "B: 응, 보고서가 있어."},
        {"en": "A: When is the presentation?", "ko": "A: 발표는 언제니?"},
        {"en": "B: It is next week.", "ko": "B: 다음 주야."},
    ],

    "✏️ 교실 활동": [
        {"en": "A: Please underline this word.", "ko": "A: 이 단어에 밑줄을 그어 주세요."},
        {"en": "B: Okay. I will underline it.", "ko": "B: 좋아요. 밑줄 칠게요."},
        {"en": "A: Can you repeat the sentence?", "ko": "A: 문장을 반복해 줄 수 있니?"},
        {"en": "B: Yes, I can repeat it.", "ko": "B: 네, 반복할 수 있어요."},
        {"en": "A: Please turn in your paper.", "ko": "A: 종이를 제출해 주세요."},
        {"en": "B: Sure. Here it is.", "ko": "B: 네. 여기 있어요."},
    ],

    "🏠 집과 생활": [
        {"en": "A: Where is your room?", "ko": "A: 네 방은 어디에 있니?"},
        {"en": "B: It is next to the living room.", "ko": "B: 거실 옆에 있어."},
        {"en": "A: Is your room clean?", "ko": "A: 네 방은 깨끗하니?"},
        {"en": "B: No, it is a little messy.", "ko": "B: 아니, 조금 지저분해."},
        {"en": "A: Can you clean it?", "ko": "A: 청소할 수 있니?"},
        {"en": "B: Yes, I can clean it today.", "ko": "B: 응, 오늘 청소할 수 있어."},
    ],

    "🌅 하루 일과": [
        {"en": "A: What time do you get up?", "ko": "A: 너는 몇 시에 일어나니?"},
        {"en": "B: I usually get up at seven.", "ko": "B: 나는 보통 7시에 일어나."},
        {"en": "A: What do you do after school?", "ko": "A: 방과 후에 무엇을 하니?"},
        {"en": "B: I relax and watch videos.", "ko": "B: 쉬면서 영상을 봐."},
        {"en": "A: Do you sleep early?", "ko": "A: 너는 일찍 자니?"},
        {"en": "B: No, I sometimes sleep late.", "ko": "B: 아니, 가끔 늦게 자."},
    ],

    "🎮 취미와 여가": [
        {"en": "A: What is your hobby?", "ko": "A: 네 취미는 뭐니?"},
        {"en": "B: My hobby is watching movies.", "ko": "B: 내 취미는 영화 보기야."},
        {"en": "A: Do you like music?", "ko": "A: 음악 좋아하니?"},
        {"en": "B: Yes, I like pop songs.", "ko": "B: 응, 나는 팝송을 좋아해."},
        {"en": "A: What do you do in your free time?", "ko": "A: 여가 시간에 무엇을 하니?"},
        {"en": "B: I play games and read comics.", "ko": "B: 게임하고 만화를 읽어."},
    ],

    "⚽ 운동과 활동": [
        {"en": "A: What sport do you like?", "ko": "A: 어떤 운동을 좋아하니?"},
        {"en": "B: I like tennis.", "ko": "B: 나는 테니스를 좋아해."},
        {"en": "A: Do you practice often?", "ko": "A: 자주 연습하니?"},
        {"en": "B: Yes, I practice after school.", "ko": "B: 응, 방과 후에 연습해."},
        {"en": "A: Did your team win?", "ko": "A: 너희 팀이 이겼니?"},
        {"en": "B: Yes, we won the match.", "ko": "B: 응, 우리는 경기에서 이겼어."},
    ],

    "🌦️ 날씨와 계절": [
        {"en": "A: How is the weather today?", "ko": "A: 오늘 날씨가 어때?"},
        {"en": "B: It is cloudy and windy.", "ko": "B: 흐리고 바람이 불어."},
        {"en": "A: Do you like winter?", "ko": "A: 겨울을 좋아하니?"},
        {"en": "B: No, I like spring.", "ko": "B: 아니, 나는 봄을 좋아해."},
        {"en": "A: Do you need an umbrella?", "ko": "A: 우산이 필요하니?"},
        {"en": "B: Yes, it may rain.", "ko": "B: 응, 비가 올지도 몰라."},
    ],

    "🌳 자연과 환경": [
        {"en": "A: Do you like nature?", "ko": "A: 자연을 좋아하니?"},
        {"en": "B: Yes, I like forests and lakes.", "ko": "B: 응, 나는 숲과 호수를 좋아해."},
        {"en": "A: What can we do for the environment?", "ko": "A: 환경을 위해 무엇을 할 수 있을까?"},
        {"en": "B: We can recycle plastic.", "ko": "B: 플라스틱을 재활용할 수 있어."},
        {"en": "A: Is pollution a problem?", "ko": "A: 오염은 문제니?"},
        {"en": "B: Yes, it is a big problem.", "ko": "B: 응, 큰 문제야."},
    ],

    "🍽️ 식당과 주문": [
        {"en": "A: Are you ready to order?", "ko": "A: 주문할 준비가 되셨나요?"},
        {"en": "B: Yes, I want pasta.", "ko": "B: 네, 파스타 주세요."},
        {"en": "A: Do you want a drink?", "ko": "A: 음료도 원하시나요?"},
        {"en": "B: Yes, I want juice.", "ko": "B: 네, 주스 주세요."},
        {"en": "A: How is the food?", "ko": "A: 음식은 어때요?"},
        {"en": "B: It is delicious.", "ko": "B: 맛있어요."},
    ],

    "🛍️ 쇼핑과 가격": [
        {"en": "A: Can I help you?", "ko": "A: 도와드릴까요?"},
        {"en": "B: Yes, I am looking for a bag.", "ko": "B: 네, 가방을 찾고 있어요."},
        {"en": "A: What color do you want?", "ko": "A: 어떤 색을 원하세요?"},
        {"en": "B: I want a black one.", "ko": "B: 검은색을 원해요."},
        {"en": "A: It is on sale today.", "ko": "A: 오늘 할인 중이에요."},
        {"en": "B: Great. I will buy it.", "ko": "B: 좋아요. 살게요."},
    ],

    "👕 옷과 외모": [
        {"en": "A: Do you like this jacket?", "ko": "A: 이 재킷 마음에 드니?"},
        {"en": "B: Yes, it looks comfortable.", "ko": "B: 응, 편해 보여."},
        {"en": "A: What size do you need?", "ko": "A: 어떤 사이즈가 필요하니?"},
        {"en": "B: I need a medium size.", "ko": "B: 중간 사이즈가 필요해."},
        {"en": "A: Are these sneakers new?", "ko": "A: 이 운동화는 새거니?"},
        {"en": "B: Yes, they are new.", "ko": "B: 응, 새거야."},
    ],

    "🚇 교통과 길 찾기": [
        {"en": "A: Where is the bus stop?", "ko": "A: 버스 정류장이 어디에 있나요?"},
        {"en": "B: Go straight and turn left.", "ko": "B: 똑바로 가서 왼쪽으로 도세요."},
        {"en": "A: Is the subway station far?", "ko": "A: 지하철역은 먼가요?"},
        {"en": "B: No, it is near here.", "ko": "B: 아니요, 여기 근처에 있어요."},
        {"en": "A: I think I am lost.", "ko": "A: 길을 잃은 것 같아요."},
        {"en": "B: I can help you.", "ko": "B: 제가 도와드릴 수 있어요."},
    ],

    "🧳 여행과 숙박": [
        {"en": "A: Do you have a reservation?", "ko": "A: 예약하셨나요?"},
        {"en": "B: Yes, I have a hotel reservation.", "ko": "B: 네, 호텔 예약이 있어요."},
        {"en": "A: May I see your passport?", "ko": "A: 여권을 볼 수 있을까요?"},
        {"en": "B: Sure. Here it is.", "ko": "B: 물론이죠. 여기 있어요."},
        {"en": "A: What time is check out?", "ko": "A: 체크아웃은 몇 시인가요?"},
        {"en": "B: It is at eleven.", "ko": "B: 11시입니다."},
    ],

    "👥 친구 관계": [
        {"en": "A: Do you want to hang out this weekend?", "ko": "A: 이번 주말에 같이 놀래?"},
        {"en": "B: Yes, that sounds fun.", "ko": "B: 응, 재미있겠다."},
        {"en": "A: Can I invite my friend?", "ko": "A: 내 친구도 초대해도 돼?"},
        {"en": "B: Sure. We can meet together.", "ko": "B: 물론이지. 같이 만날 수 있어."},
        {"en": "A: Thank you for helping me.", "ko": "A: 도와줘서 고마워."},
        {"en": "B: No problem. We are friends.", "ko": "B: 괜찮아. 우리는 친구잖아."},
    ],

    "😊 감정 표현 확장": [
        {"en": "A: You look nervous.", "ko": "A: 너 긴장해 보여."},
        {"en": "B: Yes, I have a presentation.", "ko": "B: 응, 발표가 있어."},
        {"en": "A: Don't worry. You can do it.", "ko": "A: 걱정하지 마. 너는 할 수 있어."},
        {"en": "B: Thank you. I feel better.", "ko": "B: 고마워. 기분이 나아졌어."},
        {"en": "A: Are you proud of yourself?", "ko": "A: 너 자신이 자랑스럽니?"},
        {"en": "B: Yes, I am proud.", "ko": "B: 응, 자랑스러워."},
    ],

    "💭 생각과 의견": [
        {"en": "A: What do you think about this idea?", "ko": "A: 이 생각에 대해 어떻게 생각하니?"},
        {"en": "B: I think it is useful.", "ko": "B: 유용하다고 생각해."},
        {"en": "A: Do you agree with me?", "ko": "A: 내 말에 동의하니?"},
        {"en": "B: Yes, I agree.", "ko": "B: 응, 동의해."},
        {"en": "A: Can you give me a reason?", "ko": "A: 이유를 말해 줄 수 있니?"},
        {"en": "B: Sure. It is simple and clear.", "ko": "B: 물론이지. 간단하고 명확해."},
    ],

    "📅 계획과 약속": [
        {"en": "A: Do you have plans this weekend?", "ko": "A: 이번 주말에 계획 있니?"},
        {"en": "B: Yes, I have a meeting.", "ko": "B: 응, 모임이 있어."},
        {"en": "A: Are you available tomorrow?", "ko": "A: 내일 시간 돼?"},
        {"en": "B: Yes, I am free in the afternoon.", "ko": "B: 응, 오후에 시간이 있어."},
        {"en": "A: Can we change the time?", "ko": "A: 시간을 바꿀 수 있을까?"},
        {"en": "B: Sure. No problem.", "ko": "B: 물론이지. 문제없어."},
    ],

    "🩺 건강한 생활": [
        {"en": "A: You look tired.", "ko": "A: 너 피곤해 보여."},
        {"en": "B: Yes, I did not sleep well.", "ko": "B: 응, 잠을 잘 못 잤어."},
        {"en": "A: You should rest.", "ko": "A: 쉬는 게 좋겠어."},
        {"en": "B: I know. I need more sleep.", "ko": "B: 알아. 잠이 더 필요해."},
        {"en": "A: Do you exercise often?", "ko": "A: 자주 운동하니?"},
        {"en": "B: Sometimes. I want to be healthy.", "ko": "B: 가끔. 건강해지고 싶어."},
    ],

    "📱 미디어와 스마트폰": [
        {"en": "A: What app do you use often?", "ko": "A: 어떤 앱을 자주 사용하니?"},
        {"en": "B: I often use a video app.", "ko": "B: 나는 영상 앱을 자주 사용해."},
        {"en": "A: Can you send me the link?", "ko": "A: 링크를 보내줄 수 있니?"},
        {"en": "B: Sure. I will send it now.", "ko": "B: 물론이지. 지금 보낼게."},
        {"en": "A: Is your battery low?", "ko": "A: 배터리가 부족하니?"},
        {"en": "B: Yes, I need to charge my phone.", "ko": "B: 응, 휴대폰을 충전해야 해."},
    ],

    "🌈 직업과 미래": [
        {"en": "A: What is your dream job?", "ko": "A: 네 꿈의 직업은 뭐니?"},
        {"en": "B: I want to be an engineer.", "ko": "B: 나는 엔지니어가 되고 싶어."},
        {"en": "A: What skill do you need?", "ko": "A: 어떤 기술이 필요하니?"},
        {"en": "B: I need computer skills.", "ko": "B: 컴퓨터 기술이 필요해."},
        {"en": "A: Do you have a goal?", "ko": "A: 목표가 있니?"},
        {"en": "B: Yes, I want to get a good job.", "ko": "B: 응, 좋은 직업을 얻고 싶어."},
    ],
}


# =========================
# 맨 앞 탭 전용 전체 카세트 듣기 기능
# =========================
def flatten_all_words():
    all_items = []
    number = 1

    for theme_name, theme_words in word_themes.items():
        for item in theme_words:
            all_items.append({
                "number": number,
                "theme": theme_name,
                "word": item["word"],
                "meaning": item["meaning"]
            })
            number += 1

    return all_items


def split_all_words_for_cassette(all_items, chunk_size=10):
    chunks = []

    for i in range(0, len(all_items), chunk_size):
        chunks.append(all_items[i:i + chunk_size])

    return chunks


def make_all_words_cassette_text(chunk):
    """
    gTTS 오류 방지를 위해 전체 단어 중 10개 정도만 짧게 만듭니다.
    한국어 뜻은 화면에만 보여 주고, 음성은 영어만 재생합니다.
    """
    lines = []
    lines.append("Daily English 1000.")
    lines.append("Listen and repeat.")
    lines.append("")

    for item in chunk:
        word = item["word"]
        lines.append(f"{word}.")
        lines.append(f"{word}.")
        lines.append("Repeat.")
        lines.append("")

    lines.append("Good job.")
    lines.append("Keep practicing.")

    return "\n".join(lines)


def cassette_audio_player(label, audio_bytes, height=145):
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    audio_id = f"cassette_audio_{uuid.uuid4().hex}"
    play_btn_id = f"cassette_play_{uuid.uuid4().hex}"
    pause_btn_id = f"cassette_pause_{uuid.uuid4().hex}"
    rewind_btn_id = f"cassette_rewind_{uuid.uuid4().hex}"
    forward_btn_id = f"cassette_forward_{uuid.uuid4().hex}"
    stop_btn_id = f"cassette_stop_{uuid.uuid4().hex}"
    status_id = f"cassette_status_{uuid.uuid4().hex}"
    progress_id = f"cassette_progress_{uuid.uuid4().hex}"
    player_id = f"cassette_player_{uuid.uuid4().hex}"

    safe_label = json.dumps(label)
    safe_player_id = json.dumps(player_id)

    components.html(
        f"""
        <div style="
            font-family: Arial, sans-serif;
            padding: 14px 16px;
            border-radius: 20px;
            background: linear-gradient(135deg, #f0fdf4, #eff6ff, #fff7ed);
            border: 1px solid #bbf7d0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        ">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <button id="{rewind_btn_id}" style="
                    background:#f8fafc;
                    border:1px solid #cbd5e1;
                    border-radius:999px;
                    padding:9px 14px;
                    font-weight:900;
                    font-size:14px;
                    color:#334155;
                    cursor:pointer;
                ">⏪ 10초 전</button>

                <button id="{play_btn_id}" style="
                    background: linear-gradient(135deg, #dcfce7, #dbeafe);
                    border: 1px solid #bbf7d0;
                    border-radius: 999px;
                    padding: 9px 16px;
                    font-weight: 900;
                    font-size: 14px;
                    color: #1f2937;
                    cursor: pointer;
                    box-shadow: 0 3px 8px rgba(0,0,0,0.08);
                ">
                    {label}
                </button>

                <button id="{pause_btn_id}" style="
                    background:#ecfeff;
                    border:1px solid #67e8f9;
                    border-radius:999px;
                    padding:9px 14px;
                    font-weight:900;
                    font-size:14px;
                    color:#155e75;
                    cursor:pointer;
                ">⏸ 일시정지</button>

                <button id="{forward_btn_id}" style="
                    background:#f8fafc;
                    border:1px solid #cbd5e1;
                    border-radius:999px;
                    padding:9px 14px;
                    font-weight:900;
                    font-size:14px;
                    color:#334155;
                    cursor:pointer;
                ">⏩ 10초 후</button>

                <button id="{stop_btn_id}" style="
                    background: #fff7ed;
                    border: 1px solid #fed7aa;
                    border-radius: 999px;
                    padding: 9px 14px;
                    font-weight: 900;
                    font-size: 14px;
                    color: #9a3412;
                    cursor: pointer;
                    box-shadow: 0 3px 8px rgba(0,0,0,0.05);
                ">
                    ⏹ 중지
                </button>

                <span id="{status_id}" style="
                    font-size: 13px;
                    color: #075985;
                    font-weight: 800;
                "></span>
            </div>

            <input id="{progress_id}" type="range" min="0" max="100" value="0" step="0.1" style="
                width:100%;
                margin-top:14px;
                cursor:pointer;
            ">

            <div style="
                margin-top: 6px;
                font-size: 12px;
                color: #64748b;
                font-weight: 700;
            ">
                ※ 진행 바를 움직여 원하는 부분으로 이동할 수 있습니다. 아래 단어 듣기나 대화 듣기를 누르면 이 카세트는 자동으로 중지됩니다.
            </div>

            <script>
            const audio = document.getElementById("{audio_id}");
            const playBtn = document.getElementById("{play_btn_id}");
            const pauseBtn = document.getElementById("{pause_btn_id}");
            const rewindBtn = document.getElementById("{rewind_btn_id}");
            const forwardBtn = document.getElementById("{forward_btn_id}");
            const stopBtn = document.getElementById("{stop_btn_id}");
            const status = document.getElementById("{status_id}");
            const progress = document.getElementById("{progress_id}");

            const labelText = {safe_label};
            const playerId = {safe_player_id};
            const channel = new BroadcastChannel("daily_english_audio_channel");

            function formatTime(seconds) {{
                if (isNaN(seconds)) return "0:00";
                const m = Math.floor(seconds / 60);
                const s = Math.floor(seconds % 60).toString().padStart(2, "0");
                return m + ":" + s;
            }}

            function updateStatus() {{
                status.innerText = formatTime(audio.currentTime) + " / " + formatTime(audio.duration);
            }}

            function stopThisAudio(showMessage = false) {{
                audio.pause();
                audio.currentTime = 0;
                progress.value = 0;
                playBtn.disabled = false;
                playBtn.innerText = labelText;
                status.innerText = showMessage ? "중지됨" : "";
            }}

            channel.onmessage = function(event) {{
                if (!event.data) return;

                if (event.data.type === "STOP_OTHERS" && event.data.playerId !== playerId) {{
                    stopThisAudio(false);
                }}
            }};

            playBtn.addEventListener("click", function() {{
                channel.postMessage({{
                    type: "STOP_OTHERS",
                    playerId: playerId
                }});

                playBtn.disabled = true;
                playBtn.innerText = "재생 중...";

                audio.play().then(() => {{
                    status.innerText = "카세트 재생 중";
                }}).catch((error) => {{
                    status.innerText = "다시 클릭";
                    playBtn.disabled = false;
                    playBtn.innerText = labelText;
                }});
            }});

            pauseBtn.addEventListener("click", function() {{
                audio.pause();
                playBtn.disabled = false;
                playBtn.innerText = "▶️ 이어 듣기";
                status.innerText = "일시정지 " + formatTime(audio.currentTime);
            }});

            rewindBtn.addEventListener("click", function() {{
                audio.currentTime = Math.max(0, audio.currentTime - 10);
                updateStatus();
            }});

            forwardBtn.addEventListener("click", function() {{
                if (!isNaN(audio.duration)) {{
                    audio.currentTime = Math.min(audio.duration, audio.currentTime + 10);
                    updateStatus();
                }}
            }});

            stopBtn.addEventListener("click", function() {{
                stopThisAudio(true);
            }});

            audio.addEventListener("timeupdate", function() {{
                if (!isNaN(audio.duration) && audio.duration > 0) {{
                    progress.value = (audio.currentTime / audio.duration) * 100;
                    updateStatus();
                }}
            }});

            progress.addEventListener("input", function() {{
                if (!isNaN(audio.duration) && audio.duration > 0) {{
                    audio.currentTime = (progress.value / 100) * audio.duration;
                    updateStatus();
                }}
            }});

            audio.addEventListener("ended", function() {{
                status.innerText = "완료";
                progress.value = 100;
                playBtn.disabled = false;
                playBtn.innerText = labelText;
            }});
            </script>
        </div>
        """,
        height=height
    )


def show_all_cassette_tab():
    st.markdown("## 🎧 전체 카세트 듣기")
    st.write("전체 단어를 처음부터 끝까지 순서대로 카세트처럼 복습합니다.")

    st.markdown(
        """
        <div class="cassette-box">
            <div class="cassette-title">📼 전체 단어 카세트</div>
            <div class="cassette-text">
                전체 1000개 단어를 순서대로 복습합니다.<br>
                gTTS 오류를 막기 위해 한 번에 10개 단어씩만 카세트로 만듭니다.<br>
                테마를 따로 고르지 않고, 전체 단어 순서대로 1~10번, 11~20번, 21~30번처럼 이어집니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    all_items = flatten_all_words()
    chunks = split_all_words_for_cassette(all_items, chunk_size=10)

    chunk_labels = []
    for idx, chunk in enumerate(chunks, start=1):
        start_num = chunk[0]["number"]
        end_num = chunk[-1]["number"]
        first_word = chunk[0]["word"]
        last_word = chunk[-1]["word"]
        chunk_labels.append(f"Part {idx}: {start_num}~{end_num}번 ({first_word} ~ {last_word})")

    selected_chunk_label = st.selectbox(
        "들을 구간을 선택하세요.",
        chunk_labels,
        key="all_cassette_chunk_select"
    )

    selected_chunk_index = chunk_labels.index(selected_chunk_label)
    selected_chunk = chunks[selected_chunk_index]

    st.markdown(f"### 🎧 {selected_chunk_label}")

    with st.expander("📜 이 구간 단어 보기"):
        for item in selected_chunk:
            st.markdown(
                f"**{item['number']}. {item['word']}** : {item['meaning']} "
                f"<span style='color:#94a3b8;'>({item['theme']})</span>",
                unsafe_allow_html=True
            )

    button_key = f"make_all_cassette_part_{selected_chunk_index}"

    if st.button("🎧 이 구간 카세트 만들기", key=button_key):
        st.session_state["all_cassette_ready"] = True
        st.session_state["all_cassette_chunk_index"] = selected_chunk_index

    if (
        st.session_state.get("all_cassette_ready", False)
        and st.session_state.get("all_cassette_chunk_index") == selected_chunk_index
    ):
        cassette_text = make_all_words_cassette_text(selected_chunk)
        cassette_audio = make_tts_audio(cassette_text, lang="en", tld="com")

        cassette_audio_player(
            "▶️ 전체 카세트 재생",
            cassette_audio,
            height=145
        )

        start_num = selected_chunk[0]["number"]
        end_num = selected_chunk[-1]["number"]

        st.download_button(
            label="⬇️ mp3 다운로드",
            data=cassette_audio,
            file_name=f"daily_english_1000_words_{start_num}_{end_num}_cassette.mp3",
            mime="audio/mp3",
            key=f"all_cassette_download_{selected_chunk_index}"
        )

# =========================
# 전체 뜻 목록 만들기
# =========================
all_words = []
for theme_words in word_themes.values():
    all_words.extend(theme_words)

all_meanings = [item["meaning"] for item in all_words]


# =========================
# 보기 고정 랜덤 섞기
# =========================
def get_shuffled_options(theme_name, index, options):
    key = f"{theme_name}_options_{index}"

    if key not in st.session_state:
        shuffled = options[:]
        random.seed(f"{theme_name}_{index}")
        random.shuffle(shuffled)
        st.session_state[key] = shuffled

    return st.session_state[key]


# =========================
# 퀴즈 문항 만들기
# =========================
def make_quiz_items(theme_words, theme_name):
    quiz_items = []

    for idx, item in enumerate(theme_words):
        correct = item["meaning"]
        distractors = [m for m in all_meanings if m != correct]
        random.seed(f"{theme_name}_{item['word']}_{idx}")

        if len(distractors) >= 3:
            wrong_options = random.sample(distractors, 3)
        else:
            wrong_options = distractors

        options = [correct] + wrong_options

        quiz_items.append({
            "word": item["word"],
            "answer": correct,
            "options": options
        })

    return quiz_items


# =========================
# 상태 초기화
# =========================
def init_state(theme_name):
    if f"{theme_name}_submitted1" not in st.session_state:
        st.session_state[f"{theme_name}_submitted1"] = False

    if f"{theme_name}_submitted2" not in st.session_state:
        st.session_state[f"{theme_name}_submitted2"] = False

    if f"{theme_name}_wrong" not in st.session_state:
        st.session_state[f"{theme_name}_wrong"] = []


def reset_theme(theme_name):
    keys_to_delete = []

    for key in st.session_state.keys():
        if key.startswith(theme_name):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del st.session_state[key]


# =========================
# 오늘의 일상 대화 보여주기
# =========================
def show_dialogue(theme_name):
    dialogue = theme_dialogues.get(theme_name, [])

    if not dialogue:
        return

    st.markdown('<div class="dialogue-box">', unsafe_allow_html=True)
    st.markdown('<div class="dialogue-title">💬 오늘의 일상 대화</div>', unsafe_allow_html=True)

    for line in dialogue:
        st.markdown(
            f"<div class='dialogue-line'>{line['en']}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='dialogue-meaning'>{line['ko']}</div>",
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    html_dialogue_audio_player(
        label="🔊 대화 듣기",
        dialogue_lines=dialogue,
        line_pause_ms=1400,
        height=105
    )

    dialogue_text = make_dialogue_tts_text(dialogue)
    dialogue_audio_bytes = make_tts_audio(dialogue_text)

    safe_file_name = re.sub(r"[^a-zA-Z0-9가-힣_]+", "_", theme_name)

    st.download_button(
        label="⬇️ 대화 듣기 파일 다운로드",
        data=dialogue_audio_bytes,
        file_name=f"{safe_file_name}_dialogue.mp3",
        mime="audio/mp3",
        key=f"{theme_name}_dialogue_download"
    )


# =========================
# 단어 익히기
# =========================
def show_word_cards(theme_words, theme_name):
    st.markdown("### 🌱 핵심 단어 익히기")
    st.write("기초 일상대화에 꼭 필요한 단어를 듣고 익혀 보세요.")

    for idx, item in enumerate(theme_words):
        st.markdown('<div class="word-card">', unsafe_allow_html=True)

        # 기존 크기감은 유지하면서: 영어 → 한국어 → 이모지 → 듣기/중지 순서
        col1, col2, col3, col4 = st.columns([1.25, 1.05, 0.35, 1.65])

        with col1:
            st.markdown(
                f"""
                <div class="word-row">
                    <div class="word-number">{idx + 1}</div>
                    <div class="word-text">{item['word']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div class='meaning-text'>{item['meaning']}</div>",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"<div class='emoji-text'>{get_word_emoji(item['word'])}</div>",
                unsafe_allow_html=True
            )

        with col4:
            audio_button(
                "🔊 듣기",
                item["word"],
                key=f"{theme_name}_learn_audio_{idx}"
            )

        st.markdown('</div>', unsafe_allow_html=True)


# =========================
# 퀴즈 풀기
# =========================
def show_quiz(theme_words, theme_name):
    init_state(theme_name)

    quiz_items = make_quiz_items(theme_words, theme_name)

    submitted1_key = f"{theme_name}_submitted1"
    submitted2_key = f"{theme_name}_submitted2"
    wrong_key = f"{theme_name}_wrong"

    if not st.session_state[submitted1_key]:
        st.markdown("### 🧸 1차 퀴즈")
        st.write("영어 단어를 보고 알맞은 뜻을 고르세요.")

        for i, q in enumerate(quiz_items):
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

            st.markdown(f"<div class='quiz-number'>🌟 Question {i + 1}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='quiz-word'>{q['word']}</div>", unsafe_allow_html=True)

            audio_button(
                "🔊 듣기",
                q["word"],
                key=f"{theme_name}_quiz_audio1_{i}"
            )

            options = get_shuffled_options(theme_name, i, q["options"])

            st.radio(
                "뜻을 고르세요.",
                options,
                key=f"{theme_name}_q1_{i}"
            )

            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("✅ 1차 제출하기", key=f"{theme_name}_submit1"):
            wrong = []

            for i, q in enumerate(quiz_items):
                user_answer = st.session_state.get(f"{theme_name}_q1_{i}")

                if user_answer != q["answer"]:
                    wrong.append(i)

            st.session_state[wrong_key] = wrong
            st.session_state[submitted1_key] = True
            st.rerun()

    elif st.session_state[submitted1_key] and not st.session_state[submitted2_key]:
        wrong = st.session_state[wrong_key]
        score = len(quiz_items) - len(wrong)

        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-title">🎉 1차 결과: {score} / {len(quiz_items)}점</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if len(wrong) == 0:
            st.balloons()
            st.success("🌈 완벽합니다! 이 테마의 일상 단어를 모두 잘 기억하고 있습니다.")

            if st.button("🔄 다시 풀기", key=f"{theme_name}_reset_all_correct"):
                reset_theme(theme_name)
                st.rerun()

        else:
            st.markdown(
                f"""
                <div class="wrong-box">
                    🍊 틀린 단어 {len(wrong)}개를 다시 풀어 봅시다.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 🔁 2차 퀴즈: 틀린 단어만 다시 풀기")

            for i in wrong:
                q = quiz_items[i]

                st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

                st.markdown(f"<div class='quiz-number'>🌟 Retry {i + 1}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='quiz-word'>{q['word']}</div>", unsafe_allow_html=True)

                audio_button(
                    "🔊 듣기",
                    q["word"],
                    key=f"{theme_name}_quiz_audio2_{i}"
                )

                options = get_shuffled_options(theme_name, i, q["options"])

                st.radio(
                    "뜻을 다시 고르세요.",
                    options,
                    key=f"{theme_name}_q2_{i}"
                )

                st.markdown('</div>', unsafe_allow_html=True)

            if st.button("✅ 2차 제출하기", key=f"{theme_name}_submit2"):
                st.session_state[submitted2_key] = True
                st.rerun()

    else:
        wrong = st.session_state[wrong_key]
        second_wrong = []

        for i in wrong:
            q = quiz_items[i]
            user_answer = st.session_state.get(f"{theme_name}_q2_{i}")

            if user_answer != q["answer"]:
                second_wrong.append(i)

        final_score = len(quiz_items) - len(second_wrong)

        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-title">🏆 최종 결과: {final_score} / {len(quiz_items)}점</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if len(second_wrong) == 0:
            st.balloons()
            st.success("💖 좋습니다! 틀렸던 단어까지 모두 다시 확인했습니다.")
        else:
            st.warning("🍊 아래 단어들은 다시 복습하면 좋습니다.")

        st.markdown("### ✅ 정답 확인")

        if len(wrong) == 0:
            st.info("틀린 문제가 없습니다.")
        else:
            for i in wrong:
                q = quiz_items[i]
                user1 = st.session_state.get(f"{theme_name}_q1_{i}")
                user2 = st.session_state.get(f"{theme_name}_q2_{i}")

                st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                st.markdown(f"### 🌱 {q['word']}")

                audio_button(
                    "🔊 듣기",
                    q["word"],
                    key=f"{theme_name}_answer_audio_{i}"
                )

                st.write(f"1차 선택: {user1}")
                st.write(f"2차 선택: {user2}")
                st.success(f"정답: {q['answer']}")
                st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🔄 다시 풀기", key=f"{theme_name}_reset"):
            reset_theme(theme_name)
            st.rerun()


# =========================
# 탭 구성
# =========================
tab_names = ["🎧 전체 카세트 듣기"] + list(word_themes.keys())
tabs = st.tabs(tab_names)

with tabs[0]:
    show_all_cassette_tab()

for tab, theme_name in zip(tabs[1:], word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]

        st.markdown(
            f"""
            <div class="theme-header">
                <div class="theme-title">{theme_name}</div>
                <div class="theme-desc">이 테마에는 {len(theme_words)}개의 일상 단어가 있습니다. 먼저 대화를 듣고, 핵심 단어를 익혀 봅시다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        show_dialogue(theme_name)

        mode = st.radio(
            "학습 모드를 선택하세요.",
            ["🌱 핵심 단어 익히기", "🧸 퀴즈 풀기"],
            key=f"{theme_name}_mode",
            horizontal=True
        )

        if mode == "🌱 핵심 단어 익히기":
            show_word_cards(theme_words, theme_name)
        else:
            show_quiz(theme_words, theme_name)
