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
# TTS 함수
# =========================================================
@st.cache_data
def make_tts(text, lang="en"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()

# =========================================================
# CSS 디자인
# =========================================================
st.markdown("""
<style>
.main-title {
    background: linear-gradient(135deg, #14532d, #16a34a);
    color: white;
    padding: 28px;
    border-radius: 24px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}
.person-card {
    background: #f8fafc;
    padding: 20px;
    border-radius: 20px;
    border: 2px solid #e2e8f0;
    margin-bottom: 18px;
}
.reading-card {
    background: linear-gradient(135deg, #f7fff7, #e8f5e9);
    padding: 26px;
    border-radius: 22px;
    border: 2px solid #2e7d32;
    font-size: 21px;
    line-height: 1.85;
}
.korean-card {
    background: linear-gradient(135deg, #fffdf2, #fff3c4);
    padding: 24px;
    border-radius: 20px;
    border: 2px solid #d6a400;
    font-size: 20px;
    line-height: 1.8;
}
.expression {
    background: #f1f8e9;
    padding: 14px 18px;
    border-radius: 16px;
    border-left: 7px solid #2e7d32;
    margin-bottom: 12px;
    font-size: 20px;
}
.activity-box {
    background: linear-gradient(135deg, #e3f2fd, #ffffff);
    padding: 22px;
    border-radius: 20px;
    border: 2px solid #42a5f5;
    margin-bottom: 16px;
}
.big-word {
    font-size: 25px;
    font-weight: 800;
    color: #14532d;
}
.small-guide {
    font-size: 18px;
    line-height: 1.7;
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

    # =====================================================
    # 다른 인물 추가 예시
    # 이미지를 쓰려면 pages/images/jordan.png 파일을 올리면 됩니다.
    # =====================================================
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
# 서술형 답변 변환/확장 함수
# =========================================================
def detect_language(text):
    english_count = sum(1 for ch in text if ch.lower() in "abcdefghijklmnopqrstuvwxyz")
    korean_count = sum(1 for ch in text if "가" <= ch <= "힣")

    if korean_count > english_count:
        return "ko"
    return "en"


def make_korean_to_english(text, person_name_clean):
    """
    학생이 한국어로 적었을 때 영어 문장으로 바꾸기
    완전한 AI 번역은 아니지만, 수업용으로 자연스러운 영어 예시를 만들어 줍니다.
    """

    lower_text = text.lower()

    ideas = []

    if "포기" in text:
        ideas.append("I should not give up easily")
    if "연습" in text or "훈련" in text or "연습" in lower_text:
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
        ideas.append("I should learn a positive attitude from this person")
        ideas.append("I should try harder in my own life")

    if len(ideas) == 1:
        idea_sentence = ideas[0]
    elif len(ideas) == 2:
        idea_sentence = ideas[0] + " and " + ideas[1]
    else:
        idea_sentence = ", ".join(ideas[:-1]) + ", and " + ideas[-1]

    improved = (
        f"Through {person_name_clean}, I learned that {idea_sentence}. "
        f"Even when something is difficult, I should keep going and trust myself. "
        f"I want to apply this lesson to my own life and become a better person."
    )

    return improved


def improve_english_answer(text, person_name_clean):
    """
    학생이 영어로 적었을 때 문법을 조금 다듬고 내용을 풍부하게 만들어 주기
    규칙 기반으로 수업용 예시 문장을 생성합니다.
    """

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
        ideas.append("I should keep trying in difficult situations")

    if len(ideas) == 1:
        idea_sentence = ideas[0]
    elif len(ideas) == 2:
        idea_sentence = ideas[0] + " and " + ideas[1]
    else:
        idea_sentence = ", ".join(ideas[:-1]) + ", and " + ideas[-1]

    improved = (
        f"Through {person_name_clean}, I learned that {idea_sentence}. "
        f"This lesson is important because everyone faces difficult moments. "
        f"When I feel tired or discouraged, I will remember this message and try again. "
        f"I want to become a person who keeps growing through effort and confidence."
    )

    return improved

# =========================================================
# 제목
# =========================================================
st.markdown("""
<div class="main-title">
    <h1>🌟 Celebrity English Reading</h1>
    <p style="font-size:22px;">
    Choose a person and practice English with video, image, reading, listening, translation, and activities.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 인물 선택
# =========================================================
person_name = st.selectbox(
    "👤 인물을 선택하세요",
    list(people_data.keys())
)

data = people_data[person_name]
dialogue = data["dialogue"]

full_english = "\n".join([f"{speaker}: {eng}" for speaker, eng, kor in dialogue])
full_korean = "\n".join([f"{speaker}: {kor}" for speaker, eng, kor in dialogue])

# =========================================================
# 인물 소개 카드
# =========================================================
st.markdown(f"""
<div class="person-card">
    <h2>{data["title"]}</h2>
    <p style="font-size:20px;">{data["subtitle"]}</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 4개 탭
# =========================================================
tab_video, tab_image, tab_reading, tab_activity = st.tabs([
    "🎬 동영상",
    "🖼️ 그림",
    "📖 Reading",
    "✍️ 활동"
])

# =========================================================
# 1. 동영상 탭
# =========================================================
with tab_video:
    st.markdown(f"## 🎬 {data['title']} Video")

    video_url = data["video_url"]

    if video_url.startswith("http"):
        st.video(video_url)
    else:
        st.info("아직 동영상 링크가 없습니다. people_data 안의 video_url에 유튜브 링크를 넣으세요.")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Before Watching</div>
    <p class="small-guide">영상을 보기 전에 생각해 봅시다.</p>
    <ul class="small-guide">
        <li>이 인물은 어떤 분야에서 유명한가요?</li>
        <li>이 인물에게 어떤 질문을 해 보고 싶나요?</li>
        <li>오늘 배울 핵심 표현은 무엇일까요?</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 2. 그림 탭
# =========================================================
with tab_image:
    st.markdown(f"## 🖼️ {data['title']} Image")

    image_path = data["image_path"]

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"이미지 파일을 찾을 수 없습니다: {image_path}")
        st.info("예: 현재 파일이 pages 폴더 안에 있다면 이미지는 pages/images/ronaldo.png 형태로 넣으세요.")

    st.markdown("### 그림 보고 말해보기")

    for exp in data["key_expressions"][:4]:
        st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================================================
# 3. Reading 탭
# Reading 안에 듣기와 한국어 해석 버튼 포함
# =========================================================
with tab_reading:
    st.markdown(f"## 📖 {data['title']} Reading")

    # 영어 지문
    reading_html = '<div class="reading-card">'
    for speaker, eng, kor in dialogue:
        reading_html += f"<b>{speaker}:</b> {eng}<br><br>"
    reading_html += "</div>"

    st.markdown(reading_html, unsafe_allow_html=True)

    st.markdown("---")

    # 버튼 상태 저장
    listening_key = f"{person_name}_show_listening"
    korean_key = f"{person_name}_show_korean"

    if listening_key not in st.session_state:
        st.session_state[listening_key] = False

    if korean_key not in st.session_state:
        st.session_state[korean_key] = False

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎧 듣기 열기 / 닫기", use_container_width=True, key=f"{person_name}_listening_btn"):
            st.session_state[listening_key] = not st.session_state[listening_key]

    with col2:
        if st.button("🇰🇷 한국어 해석 열기 / 닫기", use_container_width=True, key=f"{person_name}_korean_btn"):
            st.session_state[korean_key] = not st.session_state[korean_key]

    # 듣기 영역
    if st.session_state[listening_key]:
        st.markdown("### 🎧 전체 대화 듣기")
        st.audio(make_tts(full_english, lang="en"), format="audio/mp3")

        st.markdown("### 한 문장씩 듣기")

        for i, (speaker, eng, kor) in enumerate(dialogue, start=1):
            with st.expander(f"{i}. {speaker}: {eng}"):
                st.audio(make_tts(eng, lang="en"), format="audio/mp3")
                st.caption(kor)

    # 한국어 해석 영역
    if st.session_state[korean_key]:
        st.markdown("### 🇰🇷 한국어 해석")

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
# 4. 활동 탭
# 이해 문제 3개 + 서술형 1개 + 자동 피드백
# =========================================================
with tab_activity:
    st.markdown(f"## ✍️ {data['title']} Activities")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 1. Reading Check</div>
    <p class="small-guide">Reading 내용을 잘 이해했는지 확인해 봅시다.</p>
</div>
""", unsafe_allow_html=True)

    comprehension_questions = data["comprehension_questions"]

    user_choices = []

    for i, q in enumerate(comprehension_questions, start=1):
        choice = st.radio(
            q["question"],
            q["options"],
            key=f"{person_name}_reading_check_{i}"
        )
        user_choices.append((choice, q["answer"]))

    if st.button("✅ 이해 문제 정답 확인", key=f"{person_name}_reading_check_button"):
        score = 0

        for i, (choice, answer) in enumerate(user_choices, start=1):
            if choice == answer:
                score += 1
                st.success(f"{i}번 정답입니다.")
            else:
                st.error(f"{i}번 정답은 **{answer}** 입니다.")

        st.markdown(f"### 점수: {score} / {len(comprehension_questions)}")

        if score == len(comprehension_questions):
            st.balloons()
            st.success("완벽합니다! Reading 내용을 잘 이해했습니다. 🏆")
        elif score >= 2:
            st.info("좋습니다. 거의 다 이해했습니다.")
        else:
            st.warning("괜찮습니다. Reading을 다시 읽고 도전해 봅시다.")

    st.markdown("---")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 2. Reflection Writing</div>
    <p class="small-guide">
    이 인물을 통해 본인이 배울 점을 적어 봅시다.<br>
    영어로 써도 되고, 한국어로 써도 됩니다.
    </p>
</div>
""", unsafe_allow_html=True)

    reflection = st.text_area(
        f"✍️ {data['reflection_prompt']}",
        placeholder=(
            "영어 또는 한국어로 적어 보세요.\n\n"
            f"예: {data['reflection_example_en']}\n"
            f"예: {data['reflection_example_ko']}"
        ),
        height=180,
        key=f"{person_name}_reflection"
    )

    if st.button("💬 피드백 받기", key=f"{person_name}_reflection_feedback"):
        text = reflection.strip()

        if text == "":
            st.warning("먼저 자신의 생각을 한 문장 이상 적어 주세요.")

        else:
            person_name_clean = person_name.split(" ", 1)[-1]
            answer_lang = detect_language(text)

            st.markdown("### 💬 Feedback")

            # =================================================
            # 한국어로 적은 경우: 영어로 바꾸기
            # =================================================
            if answer_lang == "ko":
                st.success("한국어로 자신의 생각을 잘 표현했습니다.")
                st.info("아래처럼 영어 문장으로 바꾸어 볼 수 있습니다.")

                translated_answer = make_korean_to_english(text, person_name_clean)

                st.markdown("#### 🇰🇷 내가 쓴 내용")
                st.write(text)

                st.markdown("#### 🇺🇸 영어로 바꾸면")
                st.success(translated_answer)

                if len(text) >= 30:
                    st.info("내용이 충분히 구체적입니다. 자신의 생각과 배울 점이 잘 드러납니다.")
                else:
                    st.warning("조금 더 구체적으로 쓰면 좋습니다. 예를 들어, 왜 그렇게 생각했는지 한 문장을 더 추가해 보세요.")

                if (
                    "포기" in text
                    or "연습" in text
                    or "노력" in text
                    or "믿" in text
                    or "최선" in text
                    or "성실" in text
                    or "꾸준" in text
                ):
                    st.success("오늘 지문의 핵심 메시지와 잘 연결했습니다.")
                else:
                    st.info("연습, 자신감, 포기하지 않는 태도, 꾸준함과 연결하면 더 좋은 답이 됩니다.")

                st.markdown("#### ✍️ 조금 더 풍부한 영어 답변 예시")
                st.write(
                    translated_answer
                    + " I also learned that success does not come in one day. "
                    + "Small effort every day can make a big difference."
                )

            # =================================================
            # 영어로 적은 경우: 문법/내용을 다듬고 풍부하게 만들기
            # =================================================
            else:
                st.success("영어로 자신의 생각을 표현한 점이 좋습니다.")
                st.info("아래처럼 문장을 조금 더 자연스럽고 풍부하게 다듬을 수 있습니다.")

                improved_answer = improve_english_answer(text, person_name_clean)

                st.markdown("#### ✍️ 내가 쓴 영어")
                st.write(text)

                st.markdown("#### 🌟 다듬은 영어 답변")
                st.success(improved_answer)

                if len(text.split()) >= 10:
                    st.info("문장의 길이도 좋습니다. 자신의 생각을 비교적 구체적으로 표현했습니다.")
                else:
                    st.warning("좋은 시작입니다. 이유를 한 문장 더 추가하면 더 좋은 답이 됩니다.")

                if "because" in text.lower():
                    st.success("because를 사용해서 이유를 설명한 점이 좋습니다.")
                else:
                    st.info("because를 사용해서 이유를 덧붙이면 글이 더 논리적으로 보입니다.")

                if (
                    "believe" in text.lower()
                    or "practice" in text.lower()
                    or "never give up" in text.lower()
                    or "do my best" in text.lower()
                    or "hardworking" in text.lower()
                ):
                    st.success("오늘 배운 핵심 표현이나 핵심 메시지를 잘 활용했습니다.")
                else:
                    st.info("believe in yourself, practice, never give up, do my best 같은 표현을 넣어 보면 더 좋습니다.")

                st.markdown("#### 📌 추천 표현")
                st.markdown("""
- I learned that I should believe in myself.
- I should never give up even when I feel tired.
- Practice is important because it helps me improve.
- I want to do my best every day.
""")

            st.markdown("---")
            st.success(
                "좋습니다. 이 활동은 지문 속 인물의 태도를 내 삶과 연결해 보는 것이 핵심입니다."
            )

