import streamlit as st
from pathlib import Path
from gtts import gTTS
import io

# =========================================================
# 기본 설정
# =========================================================
st.set_page_config(
    page_title="Fun English Reading",
    page_icon="🌈",
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
# 서술형 피드백 함수
# =========================================================
def detect_language(text):
    english_count = sum(1 for ch in text if ch.lower() in "abcdefghijklmnopqrstuvwxyz")
    korean_count = sum(1 for ch in text if "가" <= ch <= "힣")
    return "ko" if korean_count > english_count else "en"


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
    if "팀" in text or "협동" in text or "동료" in text:
        ideas.append("I should respect teamwork")
    if "실수" in text or "실패" in text:
        ideas.append("I should learn from mistakes")
    if "창의" in text or "상상" in text:
        ideas.append("I should think creatively")
    if "자연" in text or "여행" in text:
        ideas.append("I should learn from travel and nature")
    if "문화" in text or "역사" in text:
        ideas.append("I should respect culture and history")

    if not ideas:
        ideas = ["I should learn a positive attitude", "I should keep trying"]

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
    if "team" in lower_text:
        ideas.append("I should respect teamwork")
    if "mistake" in lower_text or "failure" in lower_text:
        ideas.append("I should learn from mistakes")
    if "creative" in lower_text or "idea" in lower_text:
        ideas.append("I should think creatively")
    if "travel" in lower_text or "nature" in lower_text:
        ideas.append("I should learn from travel and nature")
    if "culture" in lower_text or "history" in lower_text:
        ideas.append("I should respect culture and history")

    if not ideas:
        ideas = ["I should have a positive attitude", "I should keep trying"]

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
# 디자인
# =========================================================
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 8% 12%, rgba(244,114,182,0.18) 0, rgba(244,114,182,0.00) 26%),
        radial-gradient(circle at 92% 10%, rgba(134,239,172,0.22) 0, rgba(134,239,172,0.00) 28%),
        linear-gradient(180deg, #fff7fb 0%, #f7fff4 48%, #ecfdf5 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.96) 0%, rgba(255,241,247,0.98) 48%, rgba(236,253,245,0.98) 100%);
    color: #0f172a;
    padding: 34px 26px 30px 26px;
    border-radius: 34px;
    text-align: center;
    margin-bottom: 22px;
    border: 2px solid #fbcfe8;
    box-shadow: 0 16px 36px rgba(15,23,42,0.10);
}
.main-title:before {
    content: "🌸";
    position: absolute;
    left: 26px;
    top: 16px;
    font-size: 72px;
    opacity: 0.23;
}
.main-title:after {
    content: "🌿";
    position: absolute;
    right: 28px;
    bottom: 12px;
    font-size: 78px;
    opacity: 0.24;
}
.main-title h1 {
    margin: 0;
    font-size: 46px;
    font-weight: 950;
    letter-spacing: -0.8px;
    color: #be185d;
}
.main-title p {
    margin-top: 12px;
    font-size: 18px;
    color: #475569;
    font-weight: 800;
    line-height: 1.65;
}
.garden-line {
    margin-top: 18px;
    font-size: 26px;
    letter-spacing: 8px;
}

.info-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #ffffff 0%, #fff7fb 55%, #f0fdf4 100%);
    padding: 24px 26px;
    border-radius: 28px;
    border: 2px solid #fbcfe8;
    margin-bottom: 20px;
    box-shadow: 0 10px 24px rgba(15,23,42,0.08);
}
.info-card:after {
    content: "🌱";
    position: absolute;
    right: 22px;
    top: 18px;
    font-size: 46px;
    opacity: 0.22;
}
.info-card h2 {
    margin-top: 0;
    margin-bottom: 6px;
    color: #166534;
    font-size: 30px;
    font-weight: 950;
}
.info-card p {
    color: #475569;
    font-size: 17px;
    font-weight: 750;
}

.fact-card {
    background: linear-gradient(135deg, #fff7fb 0%, #ffffff 45%, #f0fdf4 100%);
    padding: 22px;
    border-radius: 26px;
    border: 2px solid #fbcfe8;
    box-shadow: 0 8px 20px rgba(15,23,42,0.07);
    margin-bottom: 18px;
}
.fact-card h3 {
    margin-top: 0;
    color: #be185d;
    font-size: 25px;
    font-weight: 950;
}
.tag {
    display: inline-block;
    background: linear-gradient(135deg, #dcfce7 0%, #ffffff 100%);
    color: #166534;
    padding: 8px 13px;
    border-radius: 999px;
    font-weight: 900;
    margin-right: 8px;
    margin-bottom: 8px;
    border: 1.5px solid #bbf7d0;
    box-shadow: 0 3px 8px rgba(15,23,42,0.04);
}

.reading-card {
    background:
        linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(255,247,251,0.98) 100%);
    padding: 30px;
    border-radius: 30px;
    border: 2px solid #bfdbfe;
    font-size: 21px;
    line-height: 1.85;
    box-shadow: 0 10px 24px rgba(15,23,42,0.08);
}

.line-box {
    margin-bottom: 22px;
    padding-bottom: 14px;
    border-bottom: 1px dashed #e5e7eb;
}

.eng-line {
    font-size: 22px;
    font-weight: 850;
    color: #1d4ed8;
    line-height: 1.6;
}

.kor-line {
    margin-top: 6px;
    margin-left: 8px;
    padding-left: 12px;
    border-left: 5px solid #fde68a;
    font-size: 19px;
    font-weight: 700;
    color: #374151;
    line-height: 1.65;
    background: rgba(255, 251, 235, 0.65);
    border-radius: 10px;
    padding-top: 6px;
    padding-bottom: 6px;
}

.expression {
    background: linear-gradient(135deg, #ecfdf5 0%, #ffffff 100%);
    padding: 15px 17px;
    border-radius: 18px;
    margin-bottom: 10px;
    font-size: 19px;
    font-weight: 800;
    border-left: 8px solid #22c55e;
    box-shadow: 0 3px 10px rgba(15,23,42,0.05);
}

.section-box {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #ffffff 0%, #fff7fb 100%);
    padding: 20px 22px;
    border-radius: 24px;
    border: 1.5px solid #fbcfe8;
    box-shadow: 0 6px 16px rgba(15,23,42,0.07);
    margin-bottom: 16px;
}
.section-box h3 {
    margin: 0;
    color: #be185d;
    font-size: 24px;
    font-weight: 950;
}
.section-box:after {
    content: "🌿";
    position: absolute;
    right: 16px;
    top: 12px;
    font-size: 32px;
    opacity: 0.20;
}

div[data-testid="stTabs"] button {
    font-size: 18px;
    font-weight: 900;
    border-radius: 16px 16px 0 0;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #be185d;
}

.stButton > button {
    border-radius: 18px;
    font-weight: 900;
    border: 2px solid #bbf7d0;
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
    color: #14532d;
    box-shadow: 0 5px 14px rgba(15,23,42,0.08);
}
.stButton > button:hover {
    border: 2px solid #f9a8d4;
    background: linear-gradient(135deg, #fff7fb 0%, #ffffff 100%);
    color: #be185d;
}

div[role="radiogroup"] {
    background: rgba(255,255,255,0.72);
    padding: 12px 14px;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
}
textarea {
    border-radius: 18px !important;
}

div[data-testid="stImage"] img {
    border-radius: 26px;
    box-shadow: 0 10px 24px rgba(15,23,42,0.12);
}

@media (max-width: 768px) {
    .main-title {
        padding: 28px 18px 24px 18px;
        border-radius: 26px;
    }
    .main-title h1 {
        font-size: 34px;
    }
    .main-title p {
        font-size: 15px;
    }
    .reading-card {
        font-size: 18px;
        padding: 22px;
    }
    .eng-line {
        font-size: 19px;
    }
    .kor-line {
        font-size: 16px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 자료
# =========================================================
data_bank = {
    "인물": {
        "⚽ Ronaldo": {
            "title": "Soccer Talk with Ronaldo",
            "subtitle": "Practice, confidence, and professional habits",
            "video_url": "여기에_로날도_유튜브_링크",
            "image_path": BASE_DIR / "images" / "ronaldo.png",
            "facts": [
                "Portuguese soccer player",
                "Known for speed, powerful shooting, heading, and strict self-management",
                "Lesson: daily habits and clear goals"
            ],
            "dialogue": [
                ("Ronaldo", "Hi! Do you like soccer?", "안녕! 너는 축구를 좋아하니?"),
                ("Me", "Yes, I do. I really like soccer.", "응, 좋아해. 나는 축구를 정말 좋아해."),
                ("Ronaldo", "Who is your favorite player?", "네가 가장 좋아하는 선수는 누구니?"),
                ("Me", "You are my favorite player, Ronaldo.", "로날도, 당신이 제가 가장 좋아하는 선수예요."),
                ("Ronaldo", "Why do you like me?", "왜 나를 좋아하니?"),
                ("Me", "Because you are fast, strong, and hardworking.", "당신은 빠르고, 강하고, 성실하기 때문이에요."),
                ("Ronaldo", "Thank you. Talent is helpful, but daily habits are more important.", "고마워. 재능도 도움이 되지만 매일의 습관이 더 중요해."),
                ("Me", "What kind of habits do you mean?", "어떤 습관을 말하는 건가요?"),
                ("Ronaldo", "Training, sleeping well, eating carefully, and staying focused.", "훈련, 충분한 수면, 조심스러운 식단, 집중력을 말해."),
                ("Me", "That sounds difficult.", "어려워 보여요."),
                ("Ronaldo", "It is not easy, but small routines make you stronger.", "쉽지는 않지만 작은 루틴이 너를 더 강하게 만들어."),
                ("Me", "Sometimes I get tired and lose confidence.", "가끔은 지치고 자신감을 잃어요."),
                ("Ronaldo", "Everyone feels that way sometimes. Rest a little, and then try again.", "누구나 가끔 그렇게 느껴. 조금 쉬고 다시 도전해 봐."),
                ("Me", "I want to be a great player like you.", "저도 당신처럼 훌륭한 선수가 되고 싶어요."),
                ("Ronaldo", "Then practice with a clear goal. Do not just practice a lot. Practice smart.", "그렇다면 분명한 목표를 가지고 연습해. 많이만 하지 말고 똑똑하게 연습해."),
                ("Me", "I will set a goal and do my best.", "목표를 세우고 최선을 다할게요."),
                ("Ronaldo", "Good. Believe in yourself, keep practicing, and never give up.", "좋아. 너 자신을 믿고, 계속 연습하고, 절대 포기하지 마.")
            ],
            "key_expressions": [
                "Daily habits are important.",
                "Small routines make you stronger.",
                "Practice with a clear goal.",
                "Practice smart.",
                "Believe in yourself.",
                "Never give up."
            ],
            "questions": [
                ("1. What is Ronaldo known for?", ["Strict self-management", "Cooking", "Painting", "Writing novels"], "Strict self-management"),
                ("2. What habits does Ronaldo mention?", ["Training, sleeping well, and eating carefully", "Watching TV all day", "Never resting", "Playing games only"], "Training, sleeping well, and eating carefully"),
                ("3. How should the student practice?", ["With a clear goal", "Without thinking", "Only once a month", "Only when winning"], "With a clear goal")
            ],
            "reflection_prompt": "Ronaldo를 통해 내가 배울 점은 무엇인가요?"
        },

        "🏀 Jordan": {
            "title": "Basketball Talk with Jordan",
            "subtitle": "Failure, effort, and mental strength",
            "video_url": "여기에_조던_유튜브_링크",
            "image_path": BASE_DIR / "images" / "jordan.png",
            "facts": [
                "American basketball legend",
                "Won 6 NBA championships with the Chicago Bulls",
                "Known for strong competitiveness and clutch performances",
                "Famous lesson: failure can become motivation"
            ],
            "dialogue": [
                ("Jordan", "Hi! Do you like basketball?", "안녕! 너는 농구를 좋아하니?"),
                ("Me", "Yes, I do. I love basketball.", "네, 좋아해요. 저는 농구를 정말 좋아해요."),
                ("Jordan", "That is great. Do you know what I am famous for?", "멋지다. 내가 무엇으로 유명한지 아니?"),
                ("Me", "You are famous for winning many championships.", "많은 우승을 한 것으로 유명해요."),
                ("Jordan", "Yes. I won six NBA championships with the Chicago Bulls.", "맞아. 나는 시카고 불스와 함께 NBA 챔피언십에서 여섯 번 우승했어."),
                ("Me", "That is amazing. Were you always the best?", "정말 대단해요. 항상 최고였나요?"),
                ("Jordan", "No. I faced failure many times.", "아니. 나는 여러 번 실패를 겪었어."),
                ("Me", "Really? I thought great players never failed.", "정말요? 훌륭한 선수들은 실패하지 않는 줄 알았어요."),
                ("Jordan", "Great players fail, but they use failure as motivation.", "훌륭한 선수들도 실패해. 하지만 실패를 동기로 사용해."),
                ("Me", "I sometimes miss easy shots.", "저는 가끔 쉬운 슛도 놓쳐요."),
                ("Jordan", "That is normal. Missing a shot does not make you weak.", "그건 자연스러운 일이야. 슛을 놓친다고 약한 사람이 되는 건 아니야."),
                ("Me", "Then what should I do after a mistake?", "그럼 실수한 뒤에는 어떻게 해야 하나요?"),
                ("Jordan", "Think about why it happened, practice again, and take the next shot with confidence.", "왜 그런 일이 일어났는지 생각하고, 다시 연습하고, 다음 슛을 자신 있게 던져."),
                ("Me", "I heard you were very competitive.", "당신은 승부욕이 정말 강했다고 들었어요."),
                ("Jordan", "Yes. I wanted to win, but I also worked very hard to deserve winning.", "맞아. 나는 이기고 싶었지만, 이길 자격을 갖추기 위해 정말 열심히 노력했어."),
                ("Me", "So competitiveness is not just wanting to win?", "그러면 승부욕은 단순히 이기고 싶어 하는 것만은 아니네요?"),
                ("Jordan", "Right. Real competitiveness means preparation, focus, and responsibility.", "맞아. 진짜 승부욕은 준비, 집중, 책임감을 뜻해."),
                ("Me", "I want to have that kind of mindset.", "저도 그런 마음가짐을 갖고 싶어요."),
                ("Jordan", "Then practice hard, learn from failure, and never be afraid of the next challenge.", "그렇다면 열심히 연습하고, 실패에서 배우고, 다음 도전을 두려워하지 마."),
                ("Me", "I will remember that failure can become motivation.", "실패가 동기가 될 수 있다는 것을 기억할게요."),
                ("Jordan", "Good. Champions are made by effort, courage, and a strong mind.", "좋아. 챔피언은 노력, 용기, 강한 마음으로 만들어져.")
            ],
            "key_expressions": [
                "I won six NBA championships.",
                "Failure can become motivation.",
                "Take the next shot with confidence.",
                "Real competitiveness means preparation.",
                "Learn from failure.",
                "Never be afraid of the next challenge."
            ],
            "questions": [
                ("1. How many NBA championships did Jordan win with the Chicago Bulls?", ["Six", "Two", "Ten", "One"], "Six"),
                ("2. What does Jordan say great players use failure as?", ["Motivation", "An excuse", "A game", "A secret"], "Motivation"),
                ("3. What does real competitiveness mean?", ["Preparation, focus, and responsibility", "Only wanting to win", "Getting angry", "Never practicing"], "Preparation, focus, and responsibility")
            ],
            "reflection_prompt": "Jordan을 통해 내가 배울 점은 무엇인가요?"
        },

        "⚽ Son Heung-min": {
            "title": "Talk with Son Heung-min",
            "subtitle": "Teamwork, humility, and respect",
            "video_url": "여기에_손흥민_유튜브_링크",
            "image_path": BASE_DIR / "images" / "son.png",
            "facts": [
                "South Korean soccer star",
                "Known for speed, finishing, teamwork, and a humble attitude",
                "He trained very hard with his father when he was young",
                "Lesson: strong basics and discipline can build great skills"
            ],
            "dialogue": [
                ("Son", "Hi! Do you enjoy playing soccer with your friends?", "안녕! 친구들과 축구하는 것을 즐기니?"),
                ("Me", "Yes, I do. I like playing as a team.", "네. 저는 한 팀으로 경기하는 것을 좋아해요."),
                ("Son", "That is great. Soccer is not only about one player.", "좋아. 축구는 한 사람만의 경기가 아니야."),
                ("Me", "What is important in a team?", "팀에서 중요한 것은 무엇인가요?"),
                ("Son", "Respect, communication, and hard work are important.", "존중, 소통, 노력이 중요해."),
                ("Me", "I heard you trained very hard with your father.", "아버지와 정말 열심히 훈련했다고 들었어요."),
                ("Son", "Yes. When I was young, my father helped me build strong basics.", "맞아. 어릴 때 아버지는 내가 탄탄한 기본기를 만들도록 도와주셨어."),
                ("Me", "What kind of training did you do?", "어떤 훈련을 했나요?"),
                ("Son", "I practiced simple skills again and again, like ball control and shooting.", "볼 컨트롤과 슈팅 같은 기본 기술을 반복해서 연습했어."),
                ("Me", "That sounds boring sometimes.", "가끔은 지루했을 것 같아요."),
                ("Son", "It was not always fun, but basics become power in real games.", "항상 재미있지는 않았지만, 기본기는 실제 경기에서 힘이 돼."),
                ("Me", "Sometimes I want to score alone.", "가끔은 혼자 골을 넣고 싶어요."),
                ("Son", "Scoring is good, but helping your team is also important.", "골을 넣는 것도 좋지만, 팀을 돕는 것도 중요해."),
                ("Me", "How can I help my team?", "어떻게 하면 팀에 도움이 될 수 있을까요?"),
                ("Son", "Listen to your teammates and move together.", "동료들의 말을 듣고 함께 움직여."),
                ("Me", "I sometimes get angry when we lose.", "질 때 가끔 화가 나요."),
                ("Son", "That can happen. But a good player stays humble.", "그럴 수 있어. 하지만 좋은 선수는 겸손함을 잃지 않아."),
                ("Me", "Why is humility important?", "왜 겸손함이 중요한가요?"),
                ("Son", "Because it helps you learn from others and respect the team.", "겸손함은 다른 사람에게서 배우고 팀을 존중하게 도와주기 때문이야."),
                ("Me", "I will practice the basics and respect my team.", "기본기를 연습하고 팀을 존중할게요."),
                ("Son", "Good. Great players are built by discipline, teamwork, and attitude.", "좋아. 훌륭한 선수는 discipline, teamwork, attitude로 만들어져.")
            ],
            "key_expressions": [
                "Soccer is not only about one player.",
                "Build strong basics.",
                "Basics become power in real games.",
                "Listen to your teammates.",
                "Stay humble.",
                "Discipline, teamwork, and attitude are important."
            ],
            "questions": [
                ("1. Who helped Son build strong basics?", ["His father", "A singer", "A movie director", "A chef"], "His father"),
                ("2. What basic skills did Son practice?", ["Ball control and shooting", "Cooking and drawing", "Singing and dancing", "Sleeping and resting"], "Ball control and shooting"),
                ("3. What becomes power in real games?", ["Basics", "Only luck", "Noise", "A phone"], "Basics")
            ],
            "reflection_prompt": "Son Heung-min을 통해 내가 배울 점은 무엇인가요?"
        }
    }
}

# =========================================================
# 화면
# =========================================================
st.markdown("""
<div class="main-title">
    <h1>🌸 Fun English Reading 🌿</h1>
    <p>People · Places · Knowledge · English</p>
    <div class="garden-line">🌸 🌱 🌼 🌿 🌷</div>
</div>
""", unsafe_allow_html=True)

col_cat, col_topic = st.columns([1, 2])

with col_cat:
    category = st.selectbox("카테고리", list(data_bank.keys()))

with col_topic:
    topic_name = st.selectbox("주제 선택", list(data_bank[category].keys()))

data = data_bank[category][topic_name]
dialogue = data["dialogue"]
full_english = "\n".join([f"{speaker}: {eng}" for speaker, eng, kor in dialogue])

st.markdown(f"""
<div class="info-card">
    <h2>🌿 {data["title"]}</h2>
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
# 영어 한 문장 아래에 한국어 해석이 바로 나오도록 수정
# =========================================================
with tab_reading:
    st.markdown("## 📖 Reading")

    fact_html = '<div class="fact-card"><h3>💡 Quick Knowledge</h3>'
    for fact in data["facts"]:
        fact_html += f'<span class="tag">{fact}</span>'
    fact_html += "</div>"
    st.markdown(fact_html, unsafe_allow_html=True)

    reading_html = '<div class="reading-card">'

    for speaker, eng, kor in dialogue:
        reading_html += f"""
        <div class="line-box">
            <div class="eng-line">
                <b>{speaker}:</b> {eng}
            </div>
            <div class="kor-line">
                🇰🇷 {kor}
            </div>
        </div>
        """

    reading_html += "</div>"
    st.markdown(reading_html, unsafe_allow_html=True)

    st.markdown("---")

    listening_key = f"{category}_{topic_name}_show_listening"

    if listening_key not in st.session_state:
        st.session_state[listening_key] = False

    if st.button("🎧 듣기", use_container_width=True, key=f"{category}_{topic_name}_listening_btn"):
        st.session_state[listening_key] = not st.session_state[listening_key]

    if st.session_state[listening_key]:
        st.markdown("### 🎧 전체 듣기")
        st.audio(make_tts(full_english, lang="en"), format="audio/mp3")

        st.markdown("### 문장별 듣기")
        for i, (speaker, eng, kor) in enumerate(dialogue, start=1):
            with st.expander(f"{i}. {speaker}: {eng}"):
                st.audio(make_tts(eng, lang="en"), format="audio/mp3")

    st.markdown("---")
    st.markdown("### ⭐ Key Expressions")

    for exp in data["key_expressions"]:
        st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================================================
# 활동
# =========================================================
with tab_activity:
    st.markdown("## ✍️ 활동")

    st.markdown('<div class="section-box"><h3>1. Reading Check</h3></div>', unsafe_allow_html=True)

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

    st.markdown('<div class="section-box"><h3>2. Reflection Writing</h3></div>', unsafe_allow_html=True)

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
