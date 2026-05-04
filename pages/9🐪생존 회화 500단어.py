import streamlit as st
from gtts import gTTS
import io
import random
import base64
import uuid
import re
import json
import html
import streamlit.components.v1 as components

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Survival English 500",
    page_icon="🛟",
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
        background: linear-gradient(135deg, #ecfeff 0%, #fef3c7 50%, #fce7f3 100%);
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
        background: linear-gradient(135deg, #0ea5e9 0%, #8b5cf6 50%, #ec4899 100%);
        color: white;
        padding: 22px 26px;
        border-radius: 24px;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(14,165,233,0.25);
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
        border: 1px solid #e0f2fe;
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
        color: #0369a1;
        background: #e0f2fe;
        border-radius: 999px;
        padding: 5px 9px;
        text-align: center;
    }

    .word-text {
        min-width: 170px;
        font-size: 25px;
        font-weight: 900;
        color: #111827;
        white-space: nowrap;
    }

    .meaning-text {
        font-size: 19px;
        font-weight: 800;
        color: #374151;
        margin-left: 8px;
        white-space: nowrap;
        line-height: 42px;
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
        border: 1px solid #e9d5ff;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    }

    .quiz-number {
        display: inline-block;
        background: #dcfce7;
        color: #166534;
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

    .small-muted {
        font-size: 14px;
        color: #6b7280;
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
        border-color: #0ea5e9;
        color: #0ea5e9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 상단 제목
# =========================
st.markdown("<div class='main-title'>🛟 Survival English 500</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>생존 회화에 꼭 필요한 문장과 단어를 듣고, 따라 하고, 퀴즈로 익혀 봅시다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🌟 오늘의 학습 방식</div>
        <div class="hero-text">
            • 각 테마는 <b>오늘의 생존 대화</b>로 시작합니다.<br>
            • 대화를 듣고, 바로 아래에서 핵심 단어를 익힙니다.<br>
            • 단어 발음은 <b>20번 반복</b>됩니다.<br>
            • <b>중지 버튼</b>을 누르면 반복 발음이 바로 멈춥니다.<br>
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


# =========================
# 단어용 HTML 오디오 플레이어
# =========================
def html_word_audio_player(label, text, repeat_count=20, pause_ms=1500, height=42):
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
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; gap:6px; height:36px;">
            <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

            <button id="{play_btn_id}" style="
                background: linear-gradient(135deg, #fce7f3, #dbeafe);
                border: 1px solid #e9d5ff;
                border-radius: 999px;
                padding: 5px 8px;
                font-weight: 800;
                font-size: 12px;
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
                padding: 5px 8px;
                font-weight: 800;
                font-size: 12px;
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

            const channel = new BroadcastChannel("survival_english_audio_channel");

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
        height=42
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
        <div style="font-family: Arial, sans-serif; display:flex; align-items:center; gap:6px; height:42px;">
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

            const channel = new BroadcastChannel("survival_english_audio_channel");

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
# 생존 회화 500 테마별 단어
# =========================
word_themes = {
    "🧍 나와 사람": [
        {"word": "I", "meaning": "나"},
        {"word": "you", "meaning": "너, 당신"},
        {"word": "he", "meaning": "그"},
        {"word": "she", "meaning": "그녀"},
        {"word": "we", "meaning": "우리"},
        {"word": "they", "meaning": "그들"},
        {"word": "friend", "meaning": "친구"},
        {"word": "teacher", "meaning": "선생님"},
        {"word": "student", "meaning": "학생"},
        {"word": "classmate", "meaning": "반 친구"},
        {"word": "family", "meaning": "가족"},
        {"word": "father", "meaning": "아버지"},
        {"word": "mother", "meaning": "어머니"},
        {"word": "brother", "meaning": "형제, 남자 형제"},
        {"word": "sister", "meaning": "자매, 여자 형제"},
        {"word": "name", "meaning": "이름"},
        {"word": "person", "meaning": "사람"},
        {"word": "man", "meaning": "남자"},
        {"word": "woman", "meaning": "여자"},
        {"word": "child", "meaning": "아이"},
    ],

    "🏃 기본 동작": [
        {"word": "go", "meaning": "가다"},
        {"word": "come", "meaning": "오다"},
        {"word": "walk", "meaning": "걷다"},
        {"word": "run", "meaning": "달리다"},
        {"word": "sit", "meaning": "앉다"},
        {"word": "stand", "meaning": "서다"},
        {"word": "stop", "meaning": "멈추다"},
        {"word": "start", "meaning": "시작하다"},
        {"word": "open", "meaning": "열다"},
        {"word": "close", "meaning": "닫다"},
        {"word": "eat", "meaning": "먹다"},
        {"word": "drink", "meaning": "마시다"},
        {"word": "sleep", "meaning": "자다"},
        {"word": "study", "meaning": "공부하다"},
        {"word": "read", "meaning": "읽다"},
        {"word": "write", "meaning": "쓰다"},
        {"word": "listen", "meaning": "듣다"},
        {"word": "speak", "meaning": "말하다"},
        {"word": "help", "meaning": "돕다"},
        {"word": "wait", "meaning": "기다리다"},
    ],

    "💖 감정·몸 상태": [
        {"word": "happy", "meaning": "행복한"},
        {"word": "sad", "meaning": "슬픈"},
        {"word": "angry", "meaning": "화난"},
        {"word": "tired", "meaning": "피곤한"},
        {"word": "hungry", "meaning": "배고픈"},
        {"word": "thirsty", "meaning": "목마른"},
        {"word": "sick", "meaning": "아픈"},
        {"word": "okay", "meaning": "괜찮은"},
        {"word": "fine", "meaning": "괜찮은"},
        {"word": "cold", "meaning": "추운, 차가운"},
        {"word": "hot", "meaning": "더운, 뜨거운"},
        {"word": "pain", "meaning": "통증"},
        {"word": "headache", "meaning": "두통"},
        {"word": "stomachache", "meaning": "복통"},
        {"word": "fever", "meaning": "열"},
        {"word": "hurt", "meaning": "아프다, 다치다"},
        {"word": "good", "meaning": "좋은"},
        {"word": "bad", "meaning": "나쁜"},
        {"word": "worried", "meaning": "걱정하는"},
        {"word": "scared", "meaning": "무서워하는"},
    ],

    "🍎 음식·물": [
        {"word": "food", "meaning": "음식"},
        {"word": "water", "meaning": "물"},
        {"word": "rice", "meaning": "밥, 쌀"},
        {"word": "bread", "meaning": "빵"},
        {"word": "milk", "meaning": "우유"},
        {"word": "juice", "meaning": "주스"},
        {"word": "coffee", "meaning": "커피"},
        {"word": "tea", "meaning": "차"},
        {"word": "apple", "meaning": "사과"},
        {"word": "banana", "meaning": "바나나"},
        {"word": "egg", "meaning": "달걀"},
        {"word": "meat", "meaning": "고기"},
        {"word": "chicken", "meaning": "닭고기, 닭"},
        {"word": "fish", "meaning": "생선, 물고기"},
        {"word": "breakfast", "meaning": "아침 식사"},
        {"word": "lunch", "meaning": "점심 식사"},
        {"word": "dinner", "meaning": "저녁 식사"},
        {"word": "snack", "meaning": "간식"},
        {"word": "medicine", "meaning": "약"},
        {"word": "hospital", "meaning": "병원"},
    ],

    "🚗 장소·이동": [
        {"word": "home", "meaning": "집"},
        {"word": "school", "meaning": "학교"},
        {"word": "classroom", "meaning": "교실"},
        {"word": "bathroom", "meaning": "화장실"},
        {"word": "hospital", "meaning": "병원"},
        {"word": "store", "meaning": "가게"},
        {"word": "station", "meaning": "역"},
        {"word": "bus", "meaning": "버스"},
        {"word": "car", "meaning": "자동차"},
        {"word": "taxi", "meaning": "택시"},
        {"word": "train", "meaning": "기차"},
        {"word": "bike", "meaning": "자전거"},
        {"word": "road", "meaning": "도로"},
        {"word": "street", "meaning": "거리"},
        {"word": "here", "meaning": "여기"},
        {"word": "there", "meaning": "거기"},
        {"word": "near", "meaning": "가까운"},
        {"word": "far", "meaning": "먼"},
        {"word": "left", "meaning": "왼쪽"},
        {"word": "right", "meaning": "오른쪽, 맞는"},
    ],

    "⏰ 시간·숫자": [
        {"word": "time", "meaning": "시간"},
        {"word": "now", "meaning": "지금"},
        {"word": "today", "meaning": "오늘"},
        {"word": "tomorrow", "meaning": "내일"},
        {"word": "yesterday", "meaning": "어제"},
        {"word": "morning", "meaning": "아침"},
        {"word": "afternoon", "meaning": "오후"},
        {"word": "evening", "meaning": "저녁"},
        {"word": "night", "meaning": "밤"},
        {"word": "early", "meaning": "이른"},
        {"word": "late", "meaning": "늦은"},
        {"word": "one", "meaning": "하나"},
        {"word": "two", "meaning": "둘"},
        {"word": "three", "meaning": "셋"},
        {"word": "four", "meaning": "넷"},
        {"word": "five", "meaning": "다섯"},
        {"word": "six", "meaning": "여섯"},
        {"word": "seven", "meaning": "일곱"},
        {"word": "eight", "meaning": "여덟"},
        {"word": "ten", "meaning": "열"},
    ],

    "🎒 물건·돈": [
        {"word": "bag", "meaning": "가방"},
        {"word": "phone", "meaning": "전화기"},
        {"word": "book", "meaning": "책"},
        {"word": "notebook", "meaning": "공책"},
        {"word": "pen", "meaning": "펜"},
        {"word": "pencil", "meaning": "연필"},
        {"word": "desk", "meaning": "책상"},
        {"word": "chair", "meaning": "의자"},
        {"word": "door", "meaning": "문"},
        {"word": "window", "meaning": "창문"},
        {"word": "key", "meaning": "열쇠"},
        {"word": "money", "meaning": "돈"},
        {"word": "card", "meaning": "카드"},
        {"word": "ticket", "meaning": "표, 티켓"},
        {"word": "clothes", "meaning": "옷"},
        {"word": "shoes", "meaning": "신발"},
        {"word": "hat", "meaning": "모자"},
        {"word": "watch", "meaning": "시계"},
        {"word": "cup", "meaning": "컵"},
        {"word": "bottle", "meaning": "병"},
    ],

    "🆘 도움 요청": [
        {"word": "help", "meaning": "도움, 돕다"},
        {"word": "please", "meaning": "부디, 제발"},
        {"word": "sorry", "meaning": "미안합니다"},
        {"word": "excuse me", "meaning": "실례합니다"},
        {"word": "again", "meaning": "다시"},
        {"word": "slowly", "meaning": "천천히"},
        {"word": "understand", "meaning": "이해하다"},
        {"word": "question", "meaning": "질문"},
        {"word": "problem", "meaning": "문제"},
        {"word": "need", "meaning": "필요하다"},
        {"word": "want", "meaning": "원하다"},
        {"word": "know", "meaning": "알다"},
        {"word": "say", "meaning": "말하다"},
        {"word": "tell", "meaning": "말하다, 알려주다"},
        {"word": "ask", "meaning": "묻다"},
        {"word": "answer", "meaning": "대답, 답"},
        {"word": "repeat", "meaning": "반복하다"},
        {"word": "speak", "meaning": "말하다"},
        {"word": "look", "meaning": "보다"},
        {"word": "listen", "meaning": "듣다"},
    ],
}


# =========================
# 단어별 이모지
# =========================
WORD_EMOJIS = {
    "I": "🙋", "you": "👉", "he": "👦", "she": "👧", "we": "👥", "they": "👥",
    "friend": "🤝", "teacher": "👩‍🏫", "student": "🧑‍🎓", "classmate": "👫", "family": "👨‍👩‍👧",
    "father": "👨", "mother": "👩", "brother": "👦", "sister": "👧", "name": "🏷️",
    "person": "🧍", "man": "👨", "woman": "👩", "child": "🧒",

    "go": "➡️", "come": "⬅️", "walk": "🚶", "run": "🏃", "sit": "🪑", "stand": "🧍",
    "stop": "🛑", "start": "▶️", "open": "📂", "close": "📕", "eat": "🍽️", "drink": "🥤",
    "sleep": "😴", "study": "📚", "read": "📖", "write": "✏️", "listen": "👂", "speak": "🗣️",
    "help": "🆘", "wait": "⏳",

    "happy": "😊", "sad": "😢", "angry": "😠", "tired": "🥱", "hungry": "😋", "thirsty": "🥤",
    "sick": "🤒", "okay": "👌", "fine": "🙂", "cold": "🥶", "hot": "🥵", "pain": "🤕",
    "headache": "🤯", "stomachache": "🤢", "fever": "🌡️", "hurt": "🩹", "good": "👍", "bad": "👎",
    "worried": "😟", "scared": "😨",

    "food": "🍽️", "water": "💧", "rice": "🍚", "bread": "🍞", "milk": "🥛", "juice": "🧃",
    "coffee": "☕", "tea": "🍵", "apple": "🍎", "banana": "🍌", "egg": "🥚", "meat": "🥩",
    "chicken": "🍗", "fish": "🐟", "breakfast": "🍳", "lunch": "🍱", "dinner": "🍽️", "snack": "🍪",
    "medicine": "💊", "hospital": "🏥",

    "home": "🏠", "school": "🏫", "classroom": "🧑‍🏫", "bathroom": "🚻", "store": "🏪", "station": "🚉",
    "bus": "🚌", "car": "🚗", "taxi": "🚕", "train": "🚆", "bike": "🚲", "road": "🛣️",
    "street": "🏙️", "here": "📍", "there": "📌", "near": "↔️", "far": "🌁", "left": "⬅️", "right": "➡️",

    "time": "⏰", "now": "🕒", "today": "📅", "tomorrow": "➡️📅", "yesterday": "⬅️📅",
    "morning": "🌅", "afternoon": "☀️", "evening": "🌆", "night": "🌙", "early": "🐓", "late": "🌃",
    "one": "1️⃣", "two": "2️⃣", "three": "3️⃣", "four": "4️⃣", "five": "5️⃣", "six": "6️⃣",
    "seven": "7️⃣", "eight": "8️⃣", "ten": "🔟",

    "bag": "🎒", "phone": "📱", "book": "📘", "notebook": "📓", "pen": "🖊️", "pencil": "✏️",
    "desk": "🪑", "chair": "🪑", "door": "🚪", "window": "🪟", "key": "🔑", "money": "💵",
    "card": "💳", "ticket": "🎫", "clothes": "👕", "shoes": "👟", "hat": "🧢", "watch": "⌚",
    "cup": "☕", "bottle": "🍼",

    "please": "🙏", "sorry": "🙇", "excuse me": "🙋", "again": "🔁", "slowly": "🐢",
    "understand": "💡", "question": "❓", "problem": "⚠️", "need": "📌", "want": "✨",
    "know": "🧠", "say": "💬", "tell": "📣", "ask": "❔", "answer": "✅",
    "repeat": "🔁", "look": "👀",
}


def get_word_emoji(word):
    return WORD_EMOJIS.get(word, "🌱")


# =========================
# 단어 한 줄 compact 플레이어
# =========================
def compact_word_row_audio_player(number, word, meaning, emoji, repeat_count=20, pause_ms=1500, height=60):
    """
    한 줄에 번호 / 영어 / 한국어 / 이모지 / 듣기·중지 버튼을 모두 붙여서 보여줍니다.
    """
    audio_bytes = make_tts_audio(word)
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    audio_id = f"audio_{uuid.uuid4().hex}"
    play_btn_id = f"play_btn_{uuid.uuid4().hex}"
    stop_btn_id = f"stop_btn_{uuid.uuid4().hex}"
    status_id = f"status_{uuid.uuid4().hex}"
    player_id = f"player_{uuid.uuid4().hex}"

    safe_word_js = json.dumps(word)
    safe_player_id = json.dumps(player_id)
    safe_word_html = html.escape(str(word))
    safe_meaning_html = html.escape(str(meaning))
    safe_emoji_html = html.escape(str(emoji))

    html_code = f"""
    <div style="
        font-family: Arial, sans-serif;
        display:flex;
        align-items:center;
        gap:16px;
        height:50px;
        padding:7px 14px;
        border:1px solid #e0f2fe;
        border-radius:14px;
        background:white;
        box-shadow:0 2px 7px rgba(0,0,0,0.035);
        overflow:hidden;
    ">
        <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_base64}"></audio>

        <span style="
            min-width:30px;
            background:#e0f2fe;
            color:#0369a1;
            border-radius:999px;
            padding:4px 8px;
            font-size:12px;
            font-weight:900;
            text-align:center;
            line-height:20px;
        ">{number}</span>

        <span style="
            min-width:135px;
            max-width:185px;
            font-size:20px;
            font-weight:900;
            color:#111827;
            white-space:nowrap;
            overflow:hidden;
            text-overflow:ellipsis;
        ">{safe_word_html}</span>

        <span style="
            min-width:125px;
            max-width:210px;
            font-size:16px;
            font-weight:800;
            color:#374151;
            white-space:nowrap;
            overflow:hidden;
            text-overflow:ellipsis;
        ">{safe_meaning_html}</span>

        <span style="
            font-size:23px;
            min-width:42px;
            text-align:center;
            line-height:22px;
        ">{safe_emoji_html}</span>

        <button id="{play_btn_id}" style="
            background:linear-gradient(135deg, #fce7f3, #dbeafe);
            border:1px solid #e9d5ff;
            border-radius:999px;
            padding:7px 13px;
            font-weight:800;
            font-size:13px;
            color:#374151;
            cursor:pointer;
            white-space:nowrap;
            line-height:18px;
        ">🔊 듣기</button>

        <button id="{stop_btn_id}" style="
            background:#fff7ed;
            border:1px solid #fed7aa;
            border-radius:999px;
            padding:7px 13px;
            font-weight:800;
            font-size:13px;
            color:#9a3412;
            cursor:pointer;
            white-space:nowrap;
            line-height:18px;
        ">⏹ 중지</button>

        <span id="{status_id}" style="
            font-size:11px;
            color:#075985;
            font-weight:700;
            white-space:nowrap;
            min-width:46px;
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
        const wordText = {safe_word_js};
        const playerId = {safe_player_id};
        const channel = new BroadcastChannel("survival_english_audio_channel");

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
            playBtn.innerText = "🔊 듣기";
            status.innerText = showMessage ? "중지" : "";
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
                playBtn.innerText = "🔊 듣기";
                return;
            }}
            audio.currentTime = 0;
            audio.play().then(() => {{
                count += 1;
                status.innerText = count + "/" + maxCount;
            }}).catch((error) => {{
                status.innerText = "다시";
                playBtn.disabled = false;
                playBtn.innerText = "🔊 듣기";
            }});
        }}

        audio.addEventListener("ended", function() {{
            if (isStopped) return;
            if (count < maxCount) {{
                timer = setTimeout(playOnce, pauseMs);
            }} else {{
                status.innerText = "완료";
                playBtn.disabled = false;
                playBtn.innerText = "🔊 듣기";
            }}
        }});

        playBtn.addEventListener("click", function() {{
            channel.postMessage({{ type: "STOP_OTHERS", playerId: playerId }});
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
    """
    components.html(html_code, height=height)

# =========================
# 오늘의 생존 대화
# =========================
theme_dialogues = {
    "🧍 나와 사람": [
        {"en": "A: Hello. What is your name?", "ko": "A: 안녕. 네 이름은 뭐니?"},
        {"en": "B: My name is Alex.", "ko": "B: 내 이름은 Alex야."},
        {"en": "A: Are you a student?", "ko": "A: 너는 학생이니?"},
        {"en": "B: Yes, I am a student.", "ko": "B: 응, 나는 학생이야."},
        {"en": "A: Is he your friend?", "ko": "A: 그는 네 친구니?"},
        {"en": "B: Yes, he is my friend.", "ko": "B: 응, 그는 내 친구야."},
    ],

    "🏃 기본 동작": [
        {"en": "A: Can you come here?", "ko": "A: 여기로 올 수 있니?"},
        {"en": "B: Yes, I can come.", "ko": "B: 응, 갈 수 있어."},
        {"en": "A: Please sit down.", "ko": "A: 앉아 주세요."},
        {"en": "B: Okay. I will sit down.", "ko": "B: 좋아요. 앉을게요."},
        {"en": "A: Can you help me?", "ko": "A: 나를 도와줄 수 있니?"},
        {"en": "B: Yes, I can help you.", "ko": "B: 응, 도와줄 수 있어."},
    ],

    "💖 감정·몸 상태": [
        {"en": "A: Are you okay?", "ko": "A: 너 괜찮니?"},
        {"en": "B: No, I am tired.", "ko": "B: 아니, 나는 피곤해."},
        {"en": "A: Are you hungry?", "ko": "A: 너 배고프니?"},
        {"en": "B: Yes, I am hungry.", "ko": "B: 응, 나는 배고파."},
        {"en": "A: Are you sick?", "ko": "A: 너 아프니?"},
        {"en": "B: Yes, I am sick.", "ko": "B: 응, 나는 아파."},
    ],

    "🍎 음식·물": [
        {"en": "A: Are you thirsty?", "ko": "A: 너 목마르니?"},
        {"en": "B: Yes, I need water.", "ko": "B: 응, 나는 물이 필요해."},
        {"en": "A: Do you want food?", "ko": "A: 음식이 필요하니?"},
        {"en": "B: Yes, I want food.", "ko": "B: 응, 나는 음식이 필요해."},
        {"en": "A: Do you like apples?", "ko": "A: 너는 사과를 좋아하니?"},
        {"en": "B: Yes, I like apples.", "ko": "B: 응, 나는 사과를 좋아해."},
    ],

    "🚗 장소·이동": [
        {"en": "A: Where is the bathroom?", "ko": "A: 화장실은 어디에 있나요?"},
        {"en": "B: It is near here.", "ko": "B: 여기 근처에 있어요."},
        {"en": "A: I want to go home.", "ko": "A: 나는 집에 가고 싶어요."},
        {"en": "B: You can go by bus.", "ko": "B: 버스로 갈 수 있어요."},
        {"en": "A: Where is the station?", "ko": "A: 역은 어디에 있나요?"},
        {"en": "B: It is not far.", "ko": "B: 멀지 않아요."},
    ],

    "⏰ 시간·숫자": [
        {"en": "A: What time is it?", "ko": "A: 지금 몇 시니?"},
        {"en": "B: It is three.", "ko": "B: 3시야."},
        {"en": "A: Is it morning?", "ko": "A: 아침이니?"},
        {"en": "B: No, it is afternoon.", "ko": "B: 아니, 오후야."},
        {"en": "A: Do you study today?", "ko": "A: 너는 오늘 공부하니?"},
        {"en": "B: Yes, I study today.", "ko": "B: 응, 나는 오늘 공부해."},
    ],

    "🎒 물건·돈": [
        {"en": "A: Where is my phone?", "ko": "A: 내 전화기는 어디에 있니?"},
        {"en": "B: It is in your bag.", "ko": "B: 네 가방 안에 있어."},
        {"en": "A: Do you have money?", "ko": "A: 너 돈 있니?"},
        {"en": "B: No, I do not have money.", "ko": "B: 아니, 돈이 없어."},
        {"en": "A: Is this your book?", "ko": "A: 이것은 네 책이니?"},
        {"en": "B: Yes, it is my book.", "ko": "B: 응, 그것은 내 책이야."},
    ],

    "🆘 도움 요청": [
        {"en": "A: Excuse me.", "ko": "A: 실례합니다."},
        {"en": "B: Yes?", "ko": "B: 네?"},
        {"en": "A: I don't understand.", "ko": "A: 이해하지 못했어요."},
        {"en": "B: Okay. I will say it again.", "ko": "B: 알겠어요. 다시 말할게요."},
        {"en": "A: Please speak slowly.", "ko": "A: 천천히 말해 주세요."},
        {"en": "B: Sure. I can help you.", "ko": "B: 물론이죠. 도와줄 수 있어요."},
    ],
}

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
        wrong_options = random.sample(distractors, 3)

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
# 오늘의 생존 대화 보여주기
# =========================
def show_dialogue(theme_name):
    dialogue = theme_dialogues.get(theme_name, [])

    if not dialogue:
        return

    st.markdown('<div class="dialogue-box">', unsafe_allow_html=True)
    st.markdown('<div class="dialogue-title">💬 오늘의 생존 대화</div>', unsafe_allow_html=True)

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
    st.write("생존 회화에 꼭 필요한 단어를 듣고 익혀 보세요.")

    for idx, item in enumerate(theme_words):
        st.markdown('<div class="word-card">', unsafe_allow_html=True)

        # Daily English 코드의 크기감과 간격을 적용하되,
        # 내용은 Survival English 500 그대로 유지합니다.
        # 순서: 영어 단어 → 한국어 뜻 → 이모지 → 듣기/중지
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
                "🔊 발음 듣기",
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
            st.success("🌈 완벽합니다! 이 테마의 생존 단어를 모두 잘 기억하고 있습니다.")

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
                    "🔊 발음 다시 듣기",
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
                    "🔊 발음 다시 듣기",
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
tabs = st.tabs(list(word_themes.keys()))

for tab, theme_name in zip(tabs, word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]

        st.markdown(
            f"""
            <div class="theme-header">
                <div class="theme-title">{theme_name}</div>
                <div class="theme-desc">이 테마에는 {len(theme_words)}개의 생존 단어가 있습니다. 먼저 대화를 듣고, 핵심 단어를 익혀 봅시다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 오늘의 생존 문장은 항상 대화로 맨 위에 배치
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
