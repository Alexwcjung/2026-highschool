import streamlit as st
from pathlib import Path
from gtts import gTTS
import io

# =========================================================
# 기본 설정
# =========================================================
st.set_page_config(
    page_title="Celebrity English Reading",
    page_icon="🌟",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

# =========================================================
# TTS
# =========================================================
@st.cache_data
def make_tts(text, lang="en"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()

# =========================================================
# 답변 언어 판별 및 피드백
# =========================================================
def detect_language(text):
    english_count = sum(1 for ch in text if ch.lower() in "abcdefghijklmnopqrstuvwxyz")
    korean_count = sum(1 for ch in text if "가" <= ch <= "힣")

    if korean_count > english_count:
        return "ko"
    return "en"


def make_korean_to_english(text, person_name_clean):
    ideas = []

    if "포기" in text:
        ideas.append("I should not give up easily")
    if "연습" in text or "훈련" in text:
        ideas.append("I should keep practicing")
    if "노력" in text or "최선" in text:
        ideas.append("I should do my best")
    if "믿" in text or "자신감" in text:
        ideas.append("I should believe in myself")
    if "성실" in text or "꾸준" in text:
        ideas.append("I should be hardworking and consistent")
    if "지치" in text or "힘들" in text or "피곤" in text:
        ideas.append("I can rest a little and try again when I feel tired")
    if "꿈" in text or "목표" in text:
        ideas.append("I should work hard for my dream")

    if len(ideas) == 0:
        ideas.append("I should learn a positive attitude")
        ideas.append("I should try harder in my own life")

    if len(ideas) == 1:
        idea_sentence = ideas[0]
    elif len(ideas) == 2:
        idea_sentence = ideas[0] + " and " + ideas[1]
    else:
        idea_sentence = ", ".join(ideas[:-1]) + ", and " + ideas[-1]

    return (
        f"Through {person_name_clean}, I learned that {idea_sentence}. "
        f"Even when something is difficult, I should keep going and trust myself."
    )


def improve_english_answer(text, person_name_clean):
    lower_text = text.lower()
    ideas = []

    if "give up" in lower_text:
        ideas.append("I should not give up easily")
    if "practice" in lower_text:
        ideas.append("I should keep practicing")
    if "believe" in lower_text:
        ideas.append("I should believe in myself")
    if "hard" in lower_text or "hardworking" in lower_text:
        ideas.append("I should work hard for my goal")
    if "tired" in lower_text:
        ideas.append("I can rest a little and try again when I feel tired")
    if "best" in lower_text:
        ideas.append("I should do my best")
    if "dream" in lower_text or "goal" in lower_text:
        ideas.append("I should keep working toward my dream")

    if len(ideas) == 0:
        ideas.append("I should have a positive attitude")
        ideas.append("I should keep trying")

    if len(ideas) == 1:
        idea_sentence = ideas[0]
    elif len(ideas) == 2:
        idea_sentence = ideas[0] + " and " + ideas[1]
    else:
        idea_sentence = ", ".join(ideas[:-1]) + ", and " + ideas[-1]

    return (
        f"Through {person_name_clean}, I learned that {idea_sentence}. "
        f"This lesson is important because everyone faces difficult moments. "
        f"I will remember this message and try again."
    )

# =========================================================
# 간단한 디자인
# =========================================================
st.markdown("""
<style>
.main-title {
    background: #14532d;
    color: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 18px;
}
.person-card {
    background: #f8fafc;
    padding: 16px;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    margin-bottom: 16px;
}
.reading-card {
    background: #f7fff7;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #86efac;
    font-size: 20px;
    line-height: 1.75;
}
.korean-card {
    background: #fffbea;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #facc15;
    font-size: 19px;
    line-height: 1.7;
}
.expression {
    background: #f1f8e9;
    padding: 12px 14px;
    border-radius: 12px;
    margin-bottom: 10px;
    font-size: 18px;
}
.simple-box {
    background: #f8fafc;
    padding: 16px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 인물별 자료
# =========================================================
people_data = {
    "⚽ Ronaldo": {
        "title": "Soccer Talk with Ronaldo",
        "subtitle": "Practice, confidence, and never giving up",
        "video_url": "여기에_로날도_유튜브_링크",
        "image_path": BASE_DIR / "images" / "ronaldo.png",

        "dialogue": [
            ("Ronaldo", "Hi! Do you like soccer?", "안녕! 너는 축구를 좋아하니?"),
            ("Me", "Yes, I do. I really like soccer.", "응, 좋아해. 나는 축구를 정말 좋아해."),
            ("Ronaldo", "That’s great. Who is your favorite player?", "멋지다. 네가 가장 좋아하는 선수는 누구니?"),
            ("Me", "You are my favorite player, Ronaldo.", "로날도, 당신이 제가 가장 좋아하는 선수예요."),
            ("Ronaldo", "Thank you. Why do you like me?", "고마워. 왜 나를 좋아하니?"),
            ("Me", "Because you are fast, strong, and hardworking.", "당신은 빠르고, 강하고, 성실하기 때문이에요."),
            ("Ronaldo", "I’m happy to hear that. Do you play soccer?", "그 말을 들으니 기쁘구나. 너도 축구를 하니?"),
            ("Me", "Yes, I do. I play soccer with my friends.", "네, 해요. 친구들과 축구를 해요."),
            ("Ronaldo", "What position do you play?", "너는 어떤 포지션을 맡니?"),
            ("Me", "I usually play forward.", "저는 보통 공격수를 맡아요."),
            ("Ronaldo", "Nice. Do you practice every day?", "좋아. 매일 연습하니?"),
            ("Me", "Not every day, but I try to practice often.", "매일은 아니지만, 자주 연습하려고 노력해요."),
            ("Ronaldo", "Practice is very important. You must keep going.", "연습은 매우 중요해. 계속해 나가야 해."),
            ("Me", "Sometimes I get tired.", "가끔은 지쳐요."),
            ("Ronaldo", "That’s okay. Everyone gets tired sometimes.", "괜찮아. 누구나 가끔은 지칠 때가 있어."),
            ("Me", "What should I do when I feel tired?", "제가 지칠 때는 어떻게 해야 할까요?"),
            ("Ronaldo", "Rest a little, and then try again.", "조금 쉬고, 다시 도전해 봐."),
            ("Me", "I want to be a great player like you.", "저도 당신처럼 훌륭한 선수가 되고 싶어요."),
            ("Ronaldo", "Believe in yourself. Never give up.", "너 자신을 믿어. 절대 포기하지 마."),
            ("Me", "Thank you, Ronaldo. I will do my best.", "고마워요, 로날도. 최선을 다할게요."),
            ("Ronaldo", "Good! I believe in you. Keep practicing!", "좋아! 나는 너를 믿어. 계속 연습해!")
        ],

        "key_expressions": [
            "Do you like soccer?",
            "Who is your favorite player?",
            "Why do you like me?",
            "What position do you play?",
            "Practice is very important.",
            "Believe in yourself.",
            "Never give up.",
            "Keep practicing!"
        ],

        "comprehension_questions": [
            {
                "question": "1. What sport does the student like?",
                "options": ["Baseball", "Soccer", "Basketball", "Tennis"],
                "answer": "Soccer"
            },
            {
                "question": "2. What position does the student usually play?",
                "options": ["Goalkeeper", "Defender", "Forward", "Coach"],
                "answer": "Forward"
            },
            {
                "question": "3. What advice does Ronaldo give?",
                "options": [
                    "Stop practicing",
                    "Believe in yourself and never give up",
                    "Do not play soccer",
                    "Practice only when you win"
                ],
                "answer": "Believe in yourself and never give up"
            }
        ],

        "reflection_prompt": "Ronaldo를 통해 내가 배울 점은 무엇인가요?",
        "reflection_example_en": "I learned that I should believe in myself and never give up because practice is very important.",
        "reflection_example_ko": "로날도를 보며 지쳐도 포기하지 않고 계속 연습하는 태도를 배워야겠다고 생각했다."
    },

    "🏀 Jordan": {
        "title": "Basketball Talk with Jordan",
        "subtitle": "Dreams, practice, and confidence",
        "video_url": "여기에_조던_유튜브_링크",
        "image_path": BASE_DIR / "images" / "jordan.png",

        "dialogue": [
            ("Jordan", "Hi! Do you like basketball?", "안녕! 너는 농구를 좋아하니?"),
            ("Me", "Yes, I do. I really like basketball.", "응, 좋아해. 나는 농구를 정말 좋아해."),
            ("Jordan", "What is your dream?", "네 꿈은 무엇이니?"),
            ("Me", "I want to be a great player.", "저는 훌륭한 선수가 되고 싶어요."),
            ("Jordan", "Then practice every day and believe in yourself.", "그렇다면 매일 연습하고 너 자신을 믿어."),
            ("Me", "I will do my best.", "최선을 다할게요."),
            ("Jordan", "Good. Never give up.", "좋아. 절대 포기하지 마.")
        ],

        "key_expressions": [
            "Do you like basketball?",
            "What is your dream?",
            "I want to be a great player.",
            "Practice every day.",
            "Believe in yourself.",
            "Never give up."
        ],

        "comprehension_questions": [
            {
                "question": "1. What sport does the student like?",
                "options": ["Soccer", "Basketball", "Baseball", "Tennis"],
                "answer": "Basketball"
            },
            {
                "question": "2. What does the student want to be?",
                "options": ["A great player", "A singer", "A teacher", "A doctor"],
                "answer": "A great player"
            },
            {
                "question": "3. What advice does Jordan give?",
                "options": [
                    "Practice every day and believe in yourself",
                    "Stop playing basketball",
                    "Sleep all day",
                    "Never practice"
                ],
                "answer": "Practice every day and believe in yourself"
            }
        ],

        "reflection_prompt": "Jordan을 통해 내가 배울 점은 무엇인가요?",
        "reflection_example_en": "I learned that I should practice every day and believe in myself.",
        "reflection_example_ko": "조던을 보며 매일 꾸준히 연습하고 자신을 믿는 태도를 배워야겠다고 생각했다."
    }
}

# =========================================================
# 화면 구성
# =========================================================
st.markdown("""
<div class="main-title">
    <h1>🌟 Celebrity English Reading</h1>
</div>
""", unsafe_allow_html=True)

person_name = st.selectbox(
    "인물 선택",
    list(people_data.keys())
)

data = people_data[person_name]
dialogue = data["dialogue"]

full_english = "\n".join([f"{speaker}: {eng}" for speaker, eng, kor in dialogue])
full_korean = "\n".join([f"{speaker}: {kor}" for speaker, eng, kor in dialogue])

st.markdown(f"""
<div class="person-card">
    <h2>{data["title"]}</h2>
    <p>{data["subtitle"]}</p>
</div>
""", unsafe_allow_html=True)

tab_video, tab_image, tab_reading, tab_activity = st.tabs([
    "🎬 동영상",
    "🖼️ 그림",
    "📖 Reading",
    "✍️ 활동"
])

# =========================================================
# 1. 동영상
# =========================================================
with tab_video:
    st.markdown("## 🎬 동영상")

    video_url = data["video_url"]

    if video_url.startswith("http"):
        st.video(video_url)
    else:
        st.info("video_url에 유튜브 링크를 넣으세요.")

# =========================================================
# 2. 그림
# =========================================================
with tab_image:
    st.markdown("## 🖼️ 그림")

    image_path = data["image_path"]

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"이미지 파일을 찾을 수 없습니다: {image_path}")

    st.markdown("### 핵심 문장")
    for exp in data["key_expressions"][:4]:
        st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================================================
# 3. Reading
# =========================================================
with tab_reading:
    st.markdown("## 📖 Reading")

    reading_html = '<div class="reading-card">'
    for speaker, eng, kor in dialogue:
        reading_html += f"<b>{speaker}:</b> {eng}<br><br>"
    reading_html += "</div>"

    st.markdown(reading_html, unsafe_allow_html=True)

    st.markdown("---")

    listening_key = f"{person_name}_show_listening"
    korean_key = f"{person_name}_show_korean"

    if listening_key not in st.session_state:
        st.session_state[listening_key] = False

    if korean_key not in st.session_state:
        st.session_state[korean_key] = False

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎧 듣기", use_container_width=True, key=f"{person_name}_listening_btn"):
            st.session_state[listening_key] = not st.session_state[listening_key]

    with col2:
        if st.button("🇰🇷 해석", use_container_width=True, key=f"{person_name}_korean_btn"):
            st.session_state[korean_key] = not st.session_state[korean_key]

    if st.session_state[listening_key]:
        st.markdown("### 🎧 전체 듣기")
        st.audio(make_tts(full_english, lang="en"), format="audio/mp3")

        st.markdown("### 문장별 듣기")
        for i, (speaker, eng, kor) in enumerate(dialogue, start=1):
            with st.expander(f"{i}. {speaker}: {eng}"):
                st.audio(make_tts(eng, lang="en"), format="audio/mp3")

    if st.session_state[korean_key]:
        st.markdown("### 🇰🇷 해석")

        korean_html = '<div class="korean-card">'
        for speaker, eng, kor in dialogue:
            korean_html += f"<b>{speaker}:</b> {kor}<br><br>"
        korean_html += "</div>"

        st.markdown(korean_html, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⭐ Key Expressions")

    col_a, col_b = st.columns(2)
    half = (len(data["key_expressions"]) + 1) // 2

    with col_a:
        for exp in data["key_expressions"][:half]:
            st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

    with col_b:
        for exp in data["key_expressions"][half:]:
            st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================================================
# 4. 활동
# =========================================================
with tab_activity:
    st.markdown("## ✍️ 활동")

    st.markdown('<div class="simple-box"><b>Reading Check</b></div>', unsafe_allow_html=True)

    comprehension_questions = data["comprehension_questions"]
    user_choices = []

    for i, q in enumerate(comprehension_questions, start=1):
        choice = st.radio(
            q["question"],
            q["options"],
            key=f"{person_name}_reading_check_{i}"
        )
        user_choices.append((choice, q["answer"]))

    if st.button("정답 확인", key=f"{person_name}_reading_check_button"):
        score = 0

        for i, (choice, answer) in enumerate(user_choices, start=1):
            if choice == answer:
                score += 1
                st.success(f"{i}번 정답")
            else:
                st.error(f"{i}번 정답: {answer}")

        st.markdown(f"### 점수: {score} / {len(comprehension_questions)}")

        if score == len(comprehension_questions):
            st.balloons()
            st.success("잘했습니다!")
        elif score >= 2:
            st.info("좋습니다.")
        else:
            st.warning("Reading을 다시 읽어 봅시다.")

    st.markdown("---")

    st.markdown('<div class="simple-box"><b>Reflection Writing</b></div>', unsafe_allow_html=True)

    reflection = st.text_area(
        data["reflection_prompt"],
        placeholder=(
            f"예: {data['reflection_example_en']}\n"
            f"예: {data['reflection_example_ko']}"
        ),
        height=150,
        key=f"{person_name}_reflection"
    )

    if st.button("피드백 받기", key=f"{person_name}_reflection_feedback"):
        text = reflection.strip()

        if text == "":
            st.warning("먼저 답을 적어 주세요.")

        else:
            person_name_clean = person_name.split(" ", 1)[-1]
            answer_lang = detect_language(text)

            if answer_lang == "ko":
                st.markdown("### 영어로 바꾸면")
                translated_answer = make_korean_to_english(text, person_name_clean)
                st.success(translated_answer)

                if len(text) < 30:
                    st.info("이유를 한 문장 더 쓰면 더 좋습니다.")
                else:
                    st.info("생각이 잘 드러납니다.")

            else:
                st.markdown("### 다듬은 영어")
                improved_answer = improve_english_answer(text, person_name_clean)
                st.success(improved_answer)

                if "because" not in text.lower():
                    st.info("because를 넣으면 이유가 더 분명해집니다.")
                else:
                    st.info("이유를 잘 설명했습니다.")

            st.markdown("### 추천 표현")
            st.write("I should believe in myself. / I should never give up. / I should keep practicing.")
