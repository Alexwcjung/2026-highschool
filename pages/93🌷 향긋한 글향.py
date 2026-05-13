import streamlit as st
from pathlib import Path
from gtts import gTTS
import io

# =========================================================
# 기본 설정
# =========================================================
st.set_page_config(
    page_title="English Reading",
    page_icon="📖",
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


def make_korean_to_english(text, topic_name):
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
    if "도전" in text:
        ideas.append("I should challenge myself")
    if "꿈" in text or "목표" in text:
        ideas.append("I should work hard for my dream")
    if "자연" in text or "여행" in text:
        ideas.append("I should enjoy nature and learn from travel")
    if "문화" in text or "역사" in text:
        ideas.append("I should respect culture and history")

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
        f"Through {topic_name}, I learned that {idea_sentence}. "
        f"I want to remember this lesson and apply it to my life."
    )


def improve_english_answer(text, topic_name):
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
    if "best" in lower_text:
        ideas.append("I should do my best")
    if "dream" in lower_text or "goal" in lower_text:
        ideas.append("I should keep working toward my dream")
    if "travel" in lower_text or "nature" in lower_text:
        ideas.append("I should learn from travel and nature")
    if "culture" in lower_text or "history" in lower_text:
        ideas.append("I should respect culture and history")

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
        f"Through {topic_name}, I learned that {idea_sentence}. "
        f"This lesson is meaningful because it can help me grow in my own life."
    )

# =========================================================
# 단순 디자인
# =========================================================
st.markdown("""
<style>
.main-title {
    background: #14532d;
    color: white;
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 16px;
}
.info-card {
    background: #f8fafc;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    margin-bottom: 14px;
}
.reading-card {
    background: #f7fff7;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #86efac;
    font-size: 20px;
    line-height: 1.75;
}
.korean-card {
    background: #fffbea;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #facc15;
    font-size: 19px;
    line-height: 1.7;
}
.expression {
    background: #f1f8e9;
    padding: 10px 12px;
    border-radius: 10px;
    margin-bottom: 8px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 자료
# 이미지 파일은 pages/images 폴더에 넣으면 됩니다.
# 예: pages/images/ronaldo.png
# =========================================================
data_bank = {
    "인물": {
        "⚽ Ronaldo": {
            "title": "Soccer Talk with Ronaldo",
            "subtitle": "Practice and confidence",
            "video_url": "여기에_로날도_유튜브_링크",
            "image_path": BASE_DIR / "images" / "ronaldo.png",
            "dialogue": [
                ("Ronaldo", "Hi! Do you like soccer?", "안녕! 너는 축구를 좋아하니?"),
                ("Me", "Yes, I do. I really like soccer.", "응, 좋아해. 나는 축구를 정말 좋아해."),
                ("Ronaldo", "Who is your favorite player?", "네가 가장 좋아하는 선수는 누구니?"),
                ("Me", "You are my favorite player, Ronaldo.", "로날도, 당신이 제가 가장 좋아하는 선수예요."),
                ("Ronaldo", "Why do you like me?", "왜 나를 좋아하니?"),
                ("Me", "Because you are fast, strong, and hardworking.", "당신은 빠르고, 강하고, 성실하기 때문이에요."),
                ("Ronaldo", "Practice is very important. You must keep going.", "연습은 매우 중요해. 계속해 나가야 해."),
                ("Me", "Sometimes I get tired.", "가끔은 지쳐요."),
                ("Ronaldo", "Rest a little, and then try again.", "조금 쉬고, 다시 도전해 봐."),
                ("Me", "I will do my best.", "최선을 다할게요."),
                ("Ronaldo", "Good! Believe in yourself. Never give up.", "좋아! 너 자신을 믿어. 절대 포기하지 마.")
            ],
            "key_expressions": [
                "Do you like soccer?",
                "Who is your favorite player?",
                "Practice is very important.",
                "Believe in yourself.",
                "Never give up."
            ],
            "questions": [
                ("1. What sport does the student like?", ["Soccer", "Baseball", "Tennis", "Basketball"], "Soccer"),
                ("2. Why does the student like Ronaldo?", ["He is fast and hardworking", "He is a singer", "He is a teacher", "He is lazy"], "He is fast and hardworking"),
                ("3. What advice does Ronaldo give?", ["Never give up", "Stop practicing", "Sleep all day", "Play alone"], "Never give up")
            ],
            "reflection_prompt": "Ronaldo를 통해 내가 배울 점은 무엇인가요?"
        },

        "🏀 Jordan": {
            "title": "Basketball Talk with Jordan",
            "subtitle": "Dreams and effort",
            "video_url": "여기에_조던_유튜브_링크",
            "image_path": BASE_DIR / "images" / "jordan.png",
            "dialogue": [
                ("Jordan", "Hi! Do you like basketball?", "안녕! 너는 농구를 좋아하니?"),
                ("Me", "Yes, I do. I love basketball.", "네, 좋아해요. 저는 농구를 정말 좋아해요."),
                ("Jordan", "What is your dream?", "네 꿈은 무엇이니?"),
                ("Me", "I want to be a great player.", "저는 훌륭한 선수가 되고 싶어요."),
                ("Jordan", "Then you need practice and confidence.", "그렇다면 연습과 자신감이 필요해."),
                ("Me", "Sometimes I make many mistakes.", "가끔 실수를 많이 해요."),
                ("Jordan", "Mistakes are part of learning.", "실수는 배움의 일부야."),
                ("Me", "I will keep trying.", "계속 노력할게요."),
                ("Jordan", "Good. Work hard and believe in yourself.", "좋아. 열심히 노력하고 너 자신을 믿어.")
            ],
            "key_expressions": [
                "What is your dream?",
                "I want to be a great player.",
                "Mistakes are part of learning.",
                "Keep trying.",
                "Believe in yourself."
            ],
            "questions": [
                ("1. What sport does the student like?", ["Basketball", "Soccer", "Baseball", "Golf"], "Basketball"),
                ("2. What does the student want to be?", ["A great player", "A singer", "A doctor", "A cook"], "A great player"),
                ("3. What are mistakes?", ["Part of learning", "Always bad", "Not important", "A sport"], "Part of learning")
            ],
            "reflection_prompt": "Jordan을 통해 내가 배울 점은 무엇인가요?"
        },

        "⚽ Son Heung-min": {
            "title": "Talk with Son Heung-min",
            "subtitle": "Teamwork and humility",
            "video_url": "여기에_손흥민_유튜브_링크",
            "image_path": BASE_DIR / "images" / "son.png",
            "dialogue": [
                ("Son", "Hi! Do you enjoy playing with your friends?", "안녕! 친구들과 함께 경기하는 것을 즐기니?"),
                ("Me", "Yes, I do. I like playing as a team.", "네. 저는 한 팀으로 경기하는 것을 좋아해요."),
                ("Son", "That is great. Soccer is not only about one player.", "좋아. 축구는 한 사람만의 경기가 아니야."),
                ("Me", "What is important in a team?", "팀에서 중요한 것은 무엇인가요?"),
                ("Son", "Respect, communication, and hard work are important.", "존중, 소통, 노력이 중요해."),
                ("Me", "I want to help my team.", "저도 우리 팀에 도움이 되고 싶어요."),
                ("Son", "Then listen to others and do your best.", "그렇다면 다른 사람의 말을 듣고 최선을 다해."),
                ("Me", "Thank you. I will remember that.", "감사합니다. 기억할게요.")
            ],
            "key_expressions": [
                "I like playing as a team.",
                "What is important in a team?",
                "Respect is important.",
                "Do your best.",
                "Listen to others."
            ],
            "questions": [
                ("1. What does the student like?", ["Playing as a team", "Playing alone", "Watching TV", "Sleeping"], "Playing as a team"),
                ("2. What is important in a team?", ["Respect and communication", "Only speed", "Only money", "Silence"], "Respect and communication"),
                ("3. What advice does Son give?", ["Listen to others and do your best", "Never listen", "Give up", "Forget the team"], "Listen to others and do your best")
            ],
            "reflection_prompt": "Son Heung-min을 통해 내가 배울 점은 무엇인가요?"
        },

        "🎤 IU": {
            "title": "Music Talk with IU",
            "subtitle": "Creativity and sincerity",
            "video_url": "여기에_IU_유튜브_링크",
            "image_path": BASE_DIR / "images" / "iu.png",
            "dialogue": [
                ("IU", "Hi! Do you like music?", "안녕! 너는 음악을 좋아하니?"),
                ("Me", "Yes, I do. Music makes me happy.", "네. 음악은 저를 행복하게 해요."),
                ("IU", "That is wonderful. What kind of music do you like?", "멋지다. 어떤 음악을 좋아하니?"),
                ("Me", "I like songs with warm messages.", "저는 따뜻한 메시지가 있는 노래를 좋아해요."),
                ("IU", "A good song can comfort people.", "좋은 노래는 사람들을 위로할 수 있어."),
                ("Me", "I want to express my feelings better.", "저도 제 감정을 더 잘 표현하고 싶어요."),
                ("IU", "Be honest and keep writing.", "솔직해지고 계속 써 봐."),
                ("Me", "I will try to express myself.", "저도 제 자신을 표현해 볼게요.")
            ],
            "key_expressions": [
                "Music makes me happy.",
                "What kind of music do you like?",
                "A good song can comfort people.",
                "Be honest.",
                "Express myself."
            ],
            "questions": [
                ("1. What makes the student happy?", ["Music", "Math", "Rain", "Homework"], "Music"),
                ("2. What kind of songs does the student like?", ["Songs with warm messages", "Very noisy songs", "Songs without words", "Only fast songs"], "Songs with warm messages"),
                ("3. What advice does IU give?", ["Be honest and keep writing", "Stop writing", "Hide your feelings", "Never sing"], "Be honest and keep writing")
            ],
            "reflection_prompt": "IU를 통해 내가 배울 점은 무엇인가요?"
        },

        "👑 King Sejong": {
            "title": "Talk with King Sejong",
            "subtitle": "Learning and helping people",
            "video_url": "여기에_세종대왕_유튜브_링크",
            "image_path": BASE_DIR / "images" / "sejong.png",
            "dialogue": [
                ("King Sejong", "Hello. Do you think learning is important?", "안녕. 너는 배움이 중요하다고 생각하니?"),
                ("Me", "Yes, I do. Learning can change our lives.", "네. 배움은 우리의 삶을 바꿀 수 있어요."),
                ("King Sejong", "I wanted more people to read and write.", "나는 더 많은 사람들이 읽고 쓸 수 있기를 바랐단다."),
                ("Me", "That is amazing.", "정말 놀라워요."),
                ("King Sejong", "Knowledge should help people.", "지식은 사람들에게 도움이 되어야 해."),
                ("Me", "I want to use learning to help others.", "저도 배움을 통해 다른 사람들을 돕고 싶어요."),
                ("King Sejong", "That is a noble goal. Keep learning.", "그것은 훌륭한 목표구나. 계속 배워라.")
            ],
            "key_expressions": [
                "Learning is important.",
                "Learning can change our lives.",
                "Knowledge should help people.",
                "Help others.",
                "Keep learning."
            ],
            "questions": [
                ("1. What does the student think is important?", ["Learning", "Shopping", "Sleeping", "Noise"], "Learning"),
                ("2. What did King Sejong want people to do?", ["Read and write", "Stop learning", "Play games", "Forget books"], "Read and write"),
                ("3. What should knowledge do?", ["Help people", "Make people tired", "Disappear", "Stop people"], "Help people")
            ],
            "reflection_prompt": "King Sejong을 통해 내가 배울 점은 무엇인가요?"
        }
    },

    "장소": {
        "🏜️ Grand Canyon": {
            "title": "A Trip to the Grand Canyon",
            "subtitle": "Nature and wonder",
            "video_url": "여기에_그랜드캐니언_유튜브_링크",
            "image_path": BASE_DIR / "images" / "grand_canyon.png",
            "dialogue": [
                ("Guide", "Welcome to the Grand Canyon.", "그랜드캐니언에 오신 것을 환영합니다."),
                ("Me", "Wow, it is huge and beautiful.", "와, 정말 크고 아름다워요."),
                ("Guide", "Nature can make us feel small.", "자연은 우리를 작게 느끼게 할 수 있어요."),
                ("Me", "I feel amazed.", "정말 경이롭게 느껴져요."),
                ("Guide", "This place was made over a very long time.", "이곳은 아주 오랜 시간에 걸쳐 만들어졌어요."),
                ("Me", "I want to protect nature.", "저는 자연을 보호하고 싶어요.")
            ],
            "key_expressions": [
                "It is huge and beautiful.",
                "I feel amazed.",
                "Nature is powerful.",
                "Protect nature."
            ],
            "questions": [
                ("1. Where is the student?", ["Grand Canyon", "School", "Hospital", "Market"], "Grand Canyon"),
                ("2. How does the student feel?", ["Amazed", "Angry", "Bored", "Sleepy"], "Amazed"),
                ("3. What does the student want to protect?", ["Nature", "Money", "A phone", "A car"], "Nature")
            ],
            "reflection_prompt": "Grand Canyon을 통해 내가 배울 점은 무엇인가요?"
        },

        "🗽 New York": {
            "title": "A Visit to New York",
            "subtitle": "Dreams and diversity",
            "video_url": "여기에_뉴욕_유튜브_링크",
            "image_path": BASE_DIR / "images" / "new_york.png",
            "dialogue": [
                ("Guide", "Welcome to New York.", "뉴욕에 오신 것을 환영합니다."),
                ("Me", "There are so many people here.", "여기에는 정말 많은 사람들이 있어요."),
                ("Guide", "People from many cultures live here.", "다양한 문화의 사람들이 이곳에 살고 있어요."),
                ("Me", "It feels exciting.", "정말 신나요."),
                ("Guide", "New York is a city of dreams.", "뉴욕은 꿈의 도시예요."),
                ("Me", "I want to follow my dream too.", "저도 제 꿈을 따라가고 싶어요.")
            ],
            "key_expressions": [
                "There are so many people.",
                "Many cultures live here.",
                "It feels exciting.",
                "Follow my dream."
            ],
            "questions": [
                ("1. Where is the student?", ["New York", "Paris", "Seoul", "Tokyo"], "New York"),
                ("2. What kind of city is New York?", ["A city of dreams", "A small village", "A quiet farm", "A desert"], "A city of dreams"),
                ("3. What does the student want to follow?", ["My dream", "A bus", "A bird", "A map"], "My dream")
            ],
            "reflection_prompt": "New York을 통해 내가 배울 점은 무엇인가요?"
        },

        "🏯 Gyeongbokgung": {
            "title": "A Visit to Gyeongbokgung",
            "subtitle": "History and culture",
            "video_url": "여기에_경복궁_유튜브_링크",
            "image_path": BASE_DIR / "images" / "gyeongbokgung.png",
            "dialogue": [
                ("Guide", "Welcome to Gyeongbokgung.", "경복궁에 오신 것을 환영합니다."),
                ("Me", "This palace is beautiful.", "이 궁궐은 아름다워요."),
                ("Guide", "It shows Korean history and culture.", "이곳은 한국의 역사와 문화를 보여줍니다."),
                ("Me", "I want to learn more about history.", "역사에 대해 더 배우고 싶어요."),
                ("Guide", "History helps us understand who we are.", "역사는 우리가 누구인지 이해하도록 도와줍니다."),
                ("Me", "I will respect our culture.", "우리 문화를 존중하겠습니다.")
            ],
            "key_expressions": [
                "This palace is beautiful.",
                "It shows history and culture.",
                "Learn more about history.",
                "Respect our culture."
            ],
            "questions": [
                ("1. Where is the student?", ["Gyeongbokgung", "New York", "Grand Canyon", "A beach"], "Gyeongbokgung"),
                ("2. What does the palace show?", ["History and culture", "Sports and games", "Food and cars", "Music only"], "History and culture"),
                ("3. What will the student respect?", ["Our culture", "Noise", "A test", "A computer"], "Our culture")
            ],
            "reflection_prompt": "Gyeongbokgung을 통해 내가 배울 점은 무엇인가요?"
        }
    }
}

# =========================================================
# 화면
# =========================================================
st.markdown("""
<div class="main-title">
    <h1>📖 English Reading</h1>
</div>
""", unsafe_allow_html=True)

category = st.selectbox("카테고리", list(data_bank.keys()))
topic_name = st.selectbox("주제 선택", list(data_bank[category].keys()))

data = data_bank[category][topic_name]
dialogue = data["dialogue"]

full_english = "\n".join([f"{speaker}: {eng}" for speaker, eng, kor in dialogue])

st.markdown(f"""
<div class="info-card">
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
# 동영상
# =========================================================
with tab_video:
    st.markdown("## 🎬 동영상")

    video_url = data["video_url"]

    if video_url.startswith("http"):
        st.video(video_url)
    else:
        st.info("video_url에 유튜브 링크를 넣으세요.")

# =========================================================
# 그림
# =========================================================
with tab_image:
    st.markdown("## 🖼️ 그림")

    image_path = data["image_path"]

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"이미지 파일을 찾을 수 없습니다: {image_path}")

# =========================================================
# Reading
# =========================================================
with tab_reading:
    st.markdown("## 📖 Reading")

    reading_html = '<div class="reading-card">'
    for speaker, eng, kor in dialogue:
        reading_html += f"<b>{speaker}:</b> {eng}<br><br>"
    reading_html += "</div>"
    st.markdown(reading_html, unsafe_allow_html=True)

    st.markdown("---")

    listening_key = f"{category}_{topic_name}_show_listening"
    korean_key = f"{category}_{topic_name}_show_korean"

    if listening_key not in st.session_state:
        st.session_state[listening_key] = False

    if korean_key not in st.session_state:
        st.session_state[korean_key] = False

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎧 듣기", use_container_width=True, key=f"{category}_{topic_name}_listening_btn"):
            st.session_state[listening_key] = not st.session_state[listening_key]

    with col2:
        if st.button("🇰🇷 해석", use_container_width=True, key=f"{category}_{topic_name}_korean_btn"):
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

    for exp in data["key_expressions"]:
        st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================================================
# 활동
# =========================================================
with tab_activity:
    st.markdown("## ✍️ 활동")

    st.markdown("### 1. Reading Check")

    user_choices = []

    for i, (question, options, answer) in enumerate(data["questions"], start=1):
        choice = st.radio(
            question,
            options,
            key=f"{category}_{topic_name}_q{i}"
        )
        user_choices.append((choice, answer))

    if st.button("정답 확인", key=f"{category}_{topic_name}_check"):
        score = 0

        for i, (choice, answer) in enumerate(user_choices, start=1):
            if choice == answer:
                score += 1
                st.success(f"{i}번 정답")
            else:
                st.error(f"{i}번 정답: {answer}")

        st.markdown(f"### 점수: {score} / {len(data['questions'])}")

        if score == len(data["questions"]):
            st.balloons()
            st.success("잘했습니다!")
        elif score >= 2:
            st.info("좋습니다.")
        else:
            st.warning("Reading을 다시 읽어 봅시다.")

    st.markdown("---")

    st.markdown("### 2. Reflection Writing")

    reflection = st.text_area(
        data["reflection_prompt"],
        placeholder="영어 또는 한국어로 적어 보세요.",
        height=140,
        key=f"{category}_{topic_name}_reflection"
    )

    if st.button("피드백 받기", key=f"{category}_{topic_name}_feedback"):
        text = reflection.strip()

        if text == "":
            st.warning("먼저 답을 적어 주세요.")
        else:
            clean_name = topic_name.split(" ", 1)[-1]
            answer_lang = detect_language(text)

            if answer_lang == "ko":
                st.markdown("### 영어로 바꾸면")
                st.success(make_korean_to_english(text, clean_name))
            else:
                st.markdown("### 다듬은 영어")
                st.success(improve_english_answer(text, clean_name))

            st.markdown("### 추천 표현")
            st.write("I should keep trying. / I should believe in myself. / I learned something important.")
