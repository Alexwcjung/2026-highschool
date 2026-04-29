import streamlit as st
from gtts import gTTS
import io
import streamlit.components.v1 as components
import html

st.set_page_config(page_title="문장 구조 말하기 문제", page_icon="🎤", layout="centered")

# =========================================================
# 디자인 CSS
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #fffdfc;
    }

    .title-box {
        background: linear-gradient(135deg, #fff7ed 0%, #fffdf7 50%, #eef7ff 100%);
        padding: 32px 28px;
        border-radius: 30px;
        margin-bottom: 26px;
        box-shadow: 0 10px 26px rgba(80, 80, 120, 0.12);
        text-align: center;
        border: 1.5px solid #fed7aa;
    }

    .title-box h1 {
        color: #334155;
        margin-bottom: 10px;
        font-size: 36px;
        font-weight: 900;
    }

    .title-box p {
        color: #64748b;
        font-size: 19px;
        margin: 0;
        line-height: 1.7;
    }

    .guide-card {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 24px;
        padding: 22px 24px;
        margin: 16px 0 24px 0;
        box-shadow: 0 5px 16px rgba(0,0,0,0.055);
        border: 1.5px solid #edf2ff;
    }

    .guide-card p {
        font-size: 20px;
        line-height: 1.75;
        color: #374151;
        margin: 0;
    }

    .practice-card {
        background: linear-gradient(135deg, #ffffff, #fff7ed);
        border-radius: 30px;
        padding: 34px 28px;
        margin: 20px 0;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        border: 1.5px solid #fed7aa;
        text-align: center;
    }

    .practice-card .category {
        font-size: 19px;
        color: #9a3412;
        font-weight: 900;
        margin-bottom: 14px;
    }

    .practice-card .label {
        font-size: 21px;
        color: #475569;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .practice-card .korean {
        font-size: 34px;
        color: #111827;
        font-weight: 900;
        margin: 14px 0;
        line-height: 1.45;
    }

    .answer-card {
        background: linear-gradient(135deg, #eef7ff, #ffffff);
        border-radius: 26px;
        padding: 28px 24px;
        margin: 20px 0;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
        border: 1.5px solid #dbeafe;
        text-align: center;
    }

    .answer-card p {
        font-size: 21px;
        color: #475569;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .answer-card h2 {
        color: #2563eb;
        font-size: 36px;
        font-weight: 900;
        margin: 8px 0;
        line-height: 1.35;
    }

    div[data-testid="stAlert"] {
        border-radius: 18px;
        font-size: 18px;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 800;
        padding: 0.45rem 1.1rem;
        border: 1.5px solid #d9e7ff;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        color: #2563eb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 제목
# =========================================================
st.markdown(
    """
    <div class="title-box">
        <h1>🎤 문장 구조 말하기 문제</h1>
        <p>한국어 문장을 보고 영어로 말하면 문장 카드가 팡! 터집니다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("사용 방법: ① 문법 선택 → ② 한국어 문장 보고 영어로 말하기 → ③ 카드 터뜨리기 → ④ 정답과 발음 확인")

st.markdown(
    """
    <div class="guide-card">
        <p>
            처음에는 <b>영어 정답이 보이지 않습니다.</b><br>
            한국어 문장만 보고 먼저 영어로 말해 보세요.<br>
            정확하게 말하면 아래 카드가 <b>팡!</b> 하고 터집니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# TTS 함수
# =========================================================
def make_tts_audio(text):
    tts = gTTS(text=text, lang="en", tld="com")
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# =========================================================
# 말하기 문제
# =========================================================
speaking_questions = [
    {"category": "🌱 Be동사", "korean": "나는 학생이다.", "sentence": "I am a student."},
    {"category": "🌱 Be동사", "korean": "그녀는 행복하다.", "sentence": "She is happy."},
    {"category": "🌱 Be동사", "korean": "그는 친절하다.", "sentence": "He is kind."},
    {"category": "🌱 Be동사", "korean": "그들은 바쁘다.", "sentence": "They are busy."},
    {"category": "🌱 Be동사", "korean": "우리는 학생들이다.", "sentence": "We are students."},

    {"category": "🏃 현재진행형", "korean": "나는 점심을 먹고 있다.", "sentence": "I am eating lunch."},
    {"category": "🏃 현재진행형", "korean": "그녀는 책을 읽고 있다.", "sentence": "She is reading a book."},
    {"category": "🏃 현재진행형", "korean": "그들은 축구를 하고 있다.", "sentence": "They are playing soccer."},
    {"category": "🏃 현재진행형", "korean": "그는 음악을 듣고 있다.", "sentence": "He is listening to music."},
    {"category": "🏃 현재진행형", "korean": "우리는 영어를 공부하고 있다.", "sentence": "We are studying English."},

    {"category": "🚀 미래형 will", "korean": "나는 영어를 공부할 것이다.", "sentence": "I will study English."},
    {"category": "🚀 미래형 will", "korean": "그녀는 나에게 전화할 것이다.", "sentence": "She will call me."},
    {"category": "🚀 미래형 will", "korean": "우리는 부산에 갈 것이다.", "sentence": "We will go to Busan."},
    {"category": "🚀 미래형 will", "korean": "그는 축구를 할 것이다.", "sentence": "He will play soccer."},

    {"category": "🚀 미래형 be going to", "korean": "나는 영어를 공부할 예정이다.", "sentence": "I am going to study English."},
    {"category": "🚀 미래형 be going to", "korean": "그녀는 나에게 전화할 예정이다.", "sentence": "She is going to call me."},
    {"category": "🚀 미래형 be going to", "korean": "우리는 부산에 갈 예정이다.", "sentence": "We are going to go to Busan."},
    {"category": "🚀 미래형 be going to", "korean": "그들은 축구를 할 예정이다.", "sentence": "They are going to play soccer."},

    {"category": "🕰️ 과거형", "korean": "나는 어제 축구를 했다.", "sentence": "I played soccer yesterday."},
    {"category": "🕰️ 과거형", "korean": "그녀는 학교에 걸어갔다.", "sentence": "She walked to school."},
    {"category": "🕰️ 과거형", "korean": "우리는 방을 청소했다.", "sentence": "We cleaned the room."},
    {"category": "🕰️ 과거형", "korean": "나는 어제 점심을 먹었다.", "sentence": "I ate lunch yesterday."},
    {"category": "🕰️ 과거형", "korean": "그는 학교에 갔다.", "sentence": "He went to school."},

    {"category": "❌ 부정문", "korean": "나는 학생이 아니다.", "sentence": "I am not a student."},
    {"category": "❌ 부정문", "korean": "그녀는 행복하지 않다.", "sentence": "She is not happy."},
    {"category": "❌ 부정문", "korean": "그들은 바쁘지 않다.", "sentence": "They are not busy."},
    {"category": "❌ 부정문", "korean": "나는 커피를 좋아하지 않는다.", "sentence": "I do not like coffee."},
    {"category": "❌ 부정문", "korean": "그는 축구를 하지 않는다.", "sentence": "He does not play soccer."},
    {"category": "❌ 부정문", "korean": "그들은 어제 학교에 가지 않았다.", "sentence": "They did not go to school yesterday."},

    {"category": "❓ 의문문", "korean": "너는 학생이니?", "sentence": "Are you a student?"},
    {"category": "❓ 의문문", "korean": "그녀는 행복하니?", "sentence": "Is she happy?"},
    {"category": "❓ 의문문", "korean": "그들은 교실에 있니?", "sentence": "Are they in the classroom?"},
    {"category": "❓ 의문문", "korean": "너는 커피를 좋아하니?", "sentence": "Do you like coffee?"},
    {"category": "❓ 의문문", "korean": "그는 축구를 하니?", "sentence": "Does he play soccer?"},
    {"category": "❓ 의문문", "korean": "그들은 어제 학교에 갔니?", "sentence": "Did they go to school yesterday?"},

    {"category": "🕵️ 의문사 의문문", "korean": "너는 무엇을 좋아하니?", "sentence": "What do you like?"},
    {"category": "🕵️ 의문사 의문문", "korean": "너는 언제 일어나니?", "sentence": "When do you get up?"},
    {"category": "🕵️ 의문사 의문문", "korean": "너는 어디에 사니?", "sentence": "Where do you live?"},
    {"category": "🕵️ 의문사 의문문", "korean": "너는 왜 행복하니?", "sentence": "Why are you happy?"},
    {"category": "🕵️ 의문사 의문문", "korean": "너는 어떻게 학교에 가니?", "sentence": "How do you go to school?"},
    {"category": "🕵️ 의문사 의문문", "korean": "그는 누구니?", "sentence": "Who is he?"},
]

# =========================================================
# 선택 영역
# =========================================================
categories = ["전체"] + sorted(list(set([q["category"] for q in speaking_questions])))

selected_category = st.selectbox(
    "연습할 문법을 고르세요.",
    categories
)

if selected_category == "전체":
    filtered_questions = speaking_questions
else:
    filtered_questions = [
        q for q in speaking_questions
        if q["category"] == selected_category
    ]

question_labels = [
    f"{i + 1}. {q['korean']}"
    for i, q in enumerate(filtered_questions)
]

selected_label = st.selectbox(
    "연습할 문제를 고르세요.",
    question_labels
)

selected_index = question_labels.index(selected_label)
current_q = filtered_questions[selected_index]

# 문제를 바꾸면 정답 다시 숨기기
question_key = current_q["category"] + current_q["korean"]

if "last_question_key" not in st.session_state:
    st.session_state.last_question_key = question_key

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if st.session_state.last_question_key != question_key:
    st.session_state.show_answer = False
    st.session_state.last_question_key = question_key

st.markdown("---")

# =========================================================
# 문제 카드: 한국어만 제시
# =========================================================
st.markdown(
    f"""
    <div class="practice-card">
        <p class="category">{current_q["category"]}</p>
        <p class="label">한국어 문장</p>
        <div class="korean">{current_q["korean"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="guide-card">
        <p>
            위 한국어 문장을 보고 <b>영어로 먼저 말해 보세요.</b><br>
            아래의 <b>🎤 말하기 시작</b> 버튼을 누르고 정확히 말하면 카드가 터집니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 말해서 터뜨리기 HTML
# =========================================================
target_sentence = current_q["sentence"]
safe_target = html.escape(target_sentence)
safe_korean = html.escape(current_q["korean"])

speech_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: transparent;
    }}

    .game-wrap {{
        width: 100%;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #fff7ed, #eef7ff);
        border: 2px solid #fed7aa;
        border-radius: 30px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.08);
        padding: 28px 18px;
        box-sizing: border-box;
        position: relative;
        overflow: hidden;
    }}

    .hint {{
        font-size: 18px;
        font-weight: 800;
        color: #64748b;
        margin-bottom: 16px;
        text-align: center;
        line-height: 1.5;
    }}

    .bubble {{
        background: white;
        border: 4px solid #ffd6ea;
        border-radius: 999px;
        min-width: 230px;
        max-width: 90%;
        padding: 24px 30px;
        text-align: center;
        box-shadow: 0 10px 24px rgba(0,0,0,0.14);
        font-size: 26px;
        font-weight: 900;
        color: #334155;
        line-height: 1.45;
        transition: all 0.25s ease;
    }}

    .bubble.pop {{
        animation: pop 0.55s forwards;
    }}

    @keyframes pop {{
        0% {{
            transform: scale(1);
            opacity: 1;
        }}
        45% {{
            transform: scale(1.45) rotate(4deg);
            opacity: 0.9;
        }}
        100% {{
            transform: scale(0);
            opacity: 0;
        }}
    }}

    .btn {{
        margin-top: 24px;
        border: none;
        border-radius: 999px;
        padding: 14px 28px;
        font-size: 21px;
        font-weight: 900;
        color: white;
        background: linear-gradient(135deg, #ff7eb3, #ffb86c);
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
    }}

    .btn:active {{
        transform: scale(0.96);
    }}

    .status {{
        margin-top: 18px;
        font-size: 18px;
        font-weight: 800;
        color: #475569;
        text-align: center;
        min-height: 28px;
    }}

    .success {{
        color: #16a34a;
        font-size: 24px;
        font-weight: 900;
        margin-top: 18px;
        display: none;
        text-align: center;
    }}

    .effect {{
        position: absolute;
        font-size: 44px;
        animation: floatUp 0.8s forwards;
        pointer-events: none;
    }}

    @keyframes floatUp {{
        0% {{
            opacity: 1;
            transform: translateY(0) scale(1);
        }}
        100% {{
            opacity: 0;
            transform: translateY(-70px) scale(1.6);
        }}
    }}
</style>
</head>

<body>
<div class="game-wrap">
    <div class="hint">🎯 한국어 문장: {safe_korean}</div>

    <div id="bubble" class="bubble">
        영어로 말하면<br>팡! 터져요 🎈
    </div>

    <button class="btn" onclick="startRecognition()">🎤 말하기 시작</button>

    <div id="status" class="status">마이크 버튼을 누르고 영어 문장을 말해 보세요.</div>
    <div id="success" class="success">🎉 성공! 잘했어요!</div>
</div>

<script>
const target = "{safe_target}".toLowerCase();

function normalizeText(text) {{
    return text
        .toLowerCase()
        .replace(/[.,!?]/g, "")
        .replace(/\\s+/g, " ")
        .trim();
}}

function similarityCheck(spoken, target) {{
    let s = normalizeText(spoken);
    let t = normalizeText(target);

    if (s.includes(t)) {{
        return true;
    }}

    let targetWords = t.split(" ");
    let spokenWords = s.split(" ");

    let matched = 0;
    for (let word of targetWords) {{
        if (spokenWords.includes(word)) {{
            matched++;
        }}
    }}

    let ratio = matched / targetWords.length;

    // 너무 엄격하지 않게 70% 이상 맞으면 성공
    return ratio >= 0.7;
}}

function showEffects() {{
    const wrap = document.querySelector(".game-wrap");
    const icons = ["💥", "✨", "🎉", "⭐", "👏", "🌟"];

    for (let i = 0; i < 12; i++) {{
        const e = document.createElement("div");
        e.className = "effect";
        e.innerText = icons[Math.floor(Math.random() * icons.length)];
        e.style.left = Math.random() * 85 + 5 + "%";
        e.style.top = Math.random() * 50 + 20 + "%";
        wrap.appendChild(e);

        setTimeout(() => {{
            e.remove();
        }}, 850);
    }}
}}

function startRecognition() {{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const status = document.getElementById("status");
    const bubble = document.getElementById("bubble");
    const success = document.getElementById("success");

    if (!SpeechRecognition) {{
        status.innerText = "❌ 이 브라우저는 음성 인식을 지원하지 않습니다. Chrome으로 접속해 주세요.";
        return;
    }}

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = true;

    status.innerText = "🎧 듣는 중입니다. 영어로 말해 보세요!";

    recognition.onresult = function(event) {{
        let transcript = "";

        for (let i = event.resultIndex; i < event.results.length; i++) {{
            transcript += event.results[i][0].transcript;
        }}

        status.innerText = "🗣️ 인식된 말: " + transcript;

        if (similarityCheck(transcript, target)) {{
            bubble.classList.add("pop");
            success.style.display = "block";
            status.innerText = "✅ 정답으로 인식되었습니다!";
            showEffects();

            setTimeout(() => {{
                bubble.innerHTML = "🎉 성공!";
                bubble.style.opacity = "1";
                bubble.style.transform = "scale(1)";
                bubble.classList.remove("pop");
            }}, 600);

            recognition.stop();
        }}
    }};

    recognition.onerror = function(event) {{
        status.innerText = "⚠️ 마이크 오류: " + event.error;
    }};

    recognition.onend = function() {{
        if (success.style.display !== "block") {{
            status.innerText += " / 다시 시도해 보세요.";
        }}
    }};

    recognition.start();
}}
</script>
</body>
</html>
"""

components.html(speech_html, height=380)

st.markdown("---")

# =========================================================
# 정답 보기 + 원어민 발음
# =========================================================
if st.button("✅ 정답 보기"):
    st.session_state.show_answer = True

if st.session_state.show_answer:
    st.markdown(
        f"""
        <div class="answer-card">
            <p>정답 문장</p>
            <h2>{current_q["sentence"]}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🔊 원어민 발음")

    audio = make_tts_audio(current_q["sentence"])
    st.audio(audio, format="audio/mp3")

st.markdown("---")

# =========================================================
# 버튼
# =========================================================
col1, col2 = st.columns(2)

with col1:
    if st.button("🙈 정답 가리기"):
        st.session_state.show_answer = False
        st.rerun()

with col2:
    if st.button("🔄 다시 연습하기"):
        st.session_state.show_answer = False
        st.rerun()
