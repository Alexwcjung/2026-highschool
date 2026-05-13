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
    background: linear-gradient(180deg, #f8fafc 0%, #eef7f0 100%);
}
.main-title {
    background: linear-gradient(135deg, #064e3b, #16a34a);
    color: white;
    padding: 24px;
    border-radius: 24px;
    text-align: center;
    margin-bottom: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}
.main-title h1 {
    margin: 0;
    font-size: 42px;
}
.info-card {
    background: white;
    padding: 20px 22px;
    border-radius: 22px;
    border: 1px solid #dbeafe;
    margin-bottom: 18px;
    box-shadow: 0 4px 14px rgba(15,23,42,0.08);
}
.info-card h2 {
    margin-top: 0;
    color: #14532d;
}
.reading-card {
    background: white;
    padding: 28px;
    border-radius: 24px;
    border: 2px solid #bbf7d0;
    font-size: 21px;
    line-height: 1.85;
    box-shadow: 0 5px 16px rgba(15,23,42,0.08);
}
.korean-card {
    background: #fffbeb;
    padding: 26px;
    border-radius: 22px;
    border: 2px solid #fde68a;
    font-size: 20px;
    line-height: 1.75;
}
.expression {
    background: linear-gradient(135deg, #ecfdf5, #ffffff);
    padding: 13px 15px;
    border-radius: 14px;
    margin-bottom: 10px;
    font-size: 19px;
    border-left: 6px solid #22c55e;
}
.section-box {
    background: white;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 12px rgba(15,23,42,0.06);
    margin-bottom: 16px;
}
div[data-testid="stTabs"] button {
    font-size: 18px;
    font-weight: 700;
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
                ("Ronaldo", "I am happy to hear that. Do you play soccer?", "그 말을 들으니 기쁘구나. 너도 축구를 하니?"),
                ("Me", "Yes, I play soccer with my friends.", "네, 친구들과 축구를 해요."),
                ("Ronaldo", "What position do you play?", "너는 어떤 포지션을 맡니?"),
                ("Me", "I usually play forward.", "저는 보통 공격수를 맡아요."),
                ("Ronaldo", "Nice. Do you practice every day?", "좋아. 매일 연습하니?"),
                ("Me", "Not every day, but I try to practice often.", "매일은 아니지만 자주 연습하려고 노력해요."),
                ("Ronaldo", "Practice is very important. You must keep going.", "연습은 매우 중요해. 계속해 나가야 해."),
                ("Me", "Sometimes I get tired.", "가끔은 지쳐요."),
                ("Ronaldo", "That is okay. Everyone gets tired sometimes.", "괜찮아. 누구나 가끔은 지칠 때가 있어."),
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
                "What position do you play?",
                "Practice is very important.",
                "Believe in yourself.",
                "Never give up."
            ],
            "questions": [
                ("1. What sport does the student like?", ["Soccer", "Baseball", "Tennis", "Basketball"], "Soccer"),
                ("2. What position does the student usually play?", ["Forward", "Goalkeeper", "Defender", "Coach"], "Forward"),
                ("3. What advice does Ronaldo give?", ["Never give up", "Stop practicing", "Sleep all day", "Play alone"], "Never give up")
            ],
            "reflection_prompt": "Ronaldo를 통해 내가 배울 점은 무엇인가요?"
        },

        "🏀 Jordan": {
            "title": "Basketball Talk with Jordan",
            "subtitle": "Dreams, mistakes, and effort",
            "video_url": "여기에_조던_유튜브_링크",
            "image_path": BASE_DIR / "images" / "jordan.png",
            "dialogue": [
                ("Jordan", "Hi! Do you like basketball?", "안녕! 너는 농구를 좋아하니?"),
                ("Me", "Yes, I do. I love basketball.", "네, 좋아해요. 저는 농구를 정말 좋아해요."),
                ("Jordan", "That is great. Do you play often?", "멋지다. 자주 농구를 하니?"),
                ("Me", "I play after school with my friends.", "방과 후에 친구들과 농구를 해요."),
                ("Jordan", "What is your dream?", "네 꿈은 무엇이니?"),
                ("Me", "I want to be a great player.", "저는 훌륭한 선수가 되고 싶어요."),
                ("Jordan", "Then you need practice and confidence.", "그렇다면 연습과 자신감이 필요해."),
                ("Me", "Sometimes I miss easy shots.", "가끔 쉬운 슛도 놓쳐요."),
                ("Jordan", "That happens to everyone. Mistakes are part of learning.", "그건 누구에게나 일어나. 실수는 배움의 일부야."),
                ("Me", "Did you make mistakes too?", "당신도 실수를 했나요?"),
                ("Jordan", "Of course. I failed many times, but I kept trying.", "물론이지. 나는 여러 번 실패했지만 계속 노력했어."),
                ("Me", "I feel better when I hear that.", "그 말을 들으니 마음이 나아져요."),
                ("Jordan", "Do not be afraid of failure. Learn from it.", "실패를 두려워하지 마. 실패에서 배워."),
                ("Me", "I will practice more and learn from mistakes.", "더 연습하고 실수에서 배우겠습니다."),
                ("Jordan", "Good. Work hard and believe in yourself.", "좋아. 열심히 노력하고 너 자신을 믿어."),
                ("Me", "Thank you. I will keep trying.", "감사합니다. 계속 노력할게요."),
                ("Jordan", "Remember, effort can turn failure into growth.", "기억해. 노력은 실패를 성장으로 바꿀 수 있어.")
            ],
            "key_expressions": [
                "What is your dream?",
                "Mistakes are part of learning.",
                "Do not be afraid of failure.",
                "Learn from mistakes.",
                "Believe in yourself."
            ],
            "questions": [
                ("1. What sport does the student like?", ["Basketball", "Soccer", "Baseball", "Golf"], "Basketball"),
                ("2. What does the student sometimes miss?", ["Easy shots", "Breakfast", "The bus", "Homework"], "Easy shots"),
                ("3. What does Jordan say about mistakes?", ["They are part of learning", "They are always terrible", "They never happen", "They are not useful"], "They are part of learning")
            ],
            "reflection_prompt": "Jordan을 통해 내가 배울 점은 무엇인가요?"
        },

        "⚽ Son Heung-min": {
            "title": "Talk with Son Heung-min",
            "subtitle": "Teamwork and humility",
            "video_url": "여기에_손흥민_유튜브_링크",
            "image_path": BASE_DIR / "images" / "son.png",
            "dialogue": [
                ("Son", "Hi! Do you enjoy playing soccer with your friends?", "안녕! 친구들과 축구하는 것을 즐기니?"),
                ("Me", "Yes, I do. I like playing as a team.", "네. 저는 한 팀으로 경기하는 것을 좋아해요."),
                ("Son", "That is great. Soccer is not only about one player.", "좋아. 축구는 한 사람만의 경기가 아니야."),
                ("Me", "What is important in a team?", "팀에서 중요한 것은 무엇인가요?"),
                ("Son", "Respect, communication, and hard work are important.", "존중, 소통, 노력이 중요해."),
                ("Me", "Sometimes I want to score alone.", "가끔은 혼자 골을 넣고 싶어요."),
                ("Son", "Scoring is good, but helping your team is also important.", "골을 넣는 것도 좋지만, 팀을 돕는 것도 중요해."),
                ("Me", "How can I help my team?", "어떻게 하면 팀에 도움이 될 수 있을까요?"),
                ("Son", "Listen to your teammates and move together.", "동료들의 말을 듣고 함께 움직여."),
                ("Me", "I sometimes get angry when we lose.", "질 때 가끔 화가 나요."),
                ("Son", "That can happen. But a good player stays humble.", "그럴 수 있어. 하지만 좋은 선수는 겸손함을 잃지 않아."),
                ("Me", "I want to be a good teammate.", "좋은 팀원이 되고 싶어요."),
                ("Son", "Then encourage others and do your best until the end.", "그렇다면 다른 사람을 격려하고 끝까지 최선을 다해."),
                ("Me", "I will remember teamwork and respect.", "팀워크와 존중을 기억할게요."),
                ("Son", "Good. Great teams are made by great attitudes.", "좋아. 훌륭한 팀은 훌륭한 태도로 만들어져.")
            ],
            "key_expressions": [
                "I like playing as a team.",
                "What is important in a team?",
                "Respect is important.",
                "Listen to your teammates.",
                "Do your best until the end."
            ],
            "questions": [
                ("1. What does the student like?", ["Playing as a team", "Playing alone", "Watching TV", "Sleeping"], "Playing as a team"),
                ("2. What is important in a team?", ["Respect and communication", "Only speed", "Only money", "Silence"], "Respect and communication"),
                ("3. What should a good player stay?", ["Humble", "Angry", "Lazy", "Silent"], "Humble")
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
                ("IU", "Then you need to listen to your heart.", "그렇다면 너의 마음에 귀 기울여야 해."),
                ("Me", "Sometimes I do not know what I feel.", "가끔은 제가 무엇을 느끼는지 잘 모르겠어요."),
                ("IU", "That is okay. Write one small sentence first.", "괜찮아. 먼저 짧은 문장 하나를 써 봐."),
                ("Me", "Can a small sentence become a song?", "짧은 문장이 노래가 될 수 있나요?"),
                ("IU", "Yes. Honest feelings can become powerful words.", "그럼. 솔직한 감정은 힘 있는 말이 될 수 있어."),
                ("Me", "I am shy about showing my writing.", "제 글을 보여주는 것이 부끄러워요."),
                ("IU", "Many people feel that way. But sincerity touches people.", "많은 사람들이 그렇게 느껴. 하지만 진심은 사람들에게 닿아."),
                ("Me", "I will try to express myself.", "저도 제 자신을 표현해 볼게요."),
                ("IU", "Good. Be honest, keep writing, and trust your voice.", "좋아. 솔직해지고, 계속 쓰고, 너의 목소리를 믿어.")
            ],
            "key_expressions": [
                "Music makes me happy.",
                "A good song can comfort people.",
                "Listen to your heart.",
                "Express myself.",
                "Trust your voice."
            ],
            "questions": [
                ("1. What makes the student happy?", ["Music", "Math", "Rain", "Homework"], "Music"),
                ("2. What kind of songs does the student like?", ["Songs with warm messages", "Very noisy songs", "Songs without words", "Only fast songs"], "Songs with warm messages"),
                ("3. What can honest feelings become?", ["Powerful words", "A problem", "A mistake", "A game"], "Powerful words")
            ],
            "reflection_prompt": "IU를 통해 내가 배울 점은 무엇인가요?"
        },

        "🎤 BTS Jungkook": {
            "title": "Music Talk with Jungkook",
            "subtitle": "Practice, stage, and growth",
            "video_url": "여기에_정국_유튜브_링크",
            "image_path": BASE_DIR / "images" / "jungkook.png",
            "dialogue": [
                ("Jungkook", "Hi! Do you like music and dancing?", "안녕! 너는 음악과 춤을 좋아하니?"),
                ("Me", "Yes, I do. I like singing and watching performances.", "네. 저는 노래하는 것과 공연 보는 것을 좋아해요."),
                ("Jungkook", "That is great. Performing can be exciting, but it takes a lot of practice.", "멋지다. 공연은 신날 수 있지만 많은 연습이 필요해."),
                ("Me", "Do you practice every day?", "매일 연습하나요?"),
                ("Jungkook", "I try to practice often. Small practice every day can make a big difference.", "자주 연습하려고 해. 매일의 작은 연습이 큰 차이를 만들 수 있어."),
                ("Me", "Sometimes I feel nervous in front of people.", "가끔 사람들 앞에서 긴장돼요."),
                ("Jungkook", "That is natural. Even performers can feel nervous before a stage.", "그건 자연스러운 일이야. 공연자들도 무대 전에 긴장할 수 있어."),
                ("Me", "How can I become more confident?", "어떻게 하면 더 자신감을 가질 수 있을까요?"),
                ("Jungkook", "Prepare well, breathe slowly, and focus on the message you want to share.", "잘 준비하고, 천천히 숨 쉬고, 네가 전하고 싶은 메시지에 집중해."),
                ("Me", "I worry that I am not talented enough.", "제가 충분히 재능이 없을까 봐 걱정돼요."),
                ("Jungkook", "Talent is helpful, but effort and attitude are also very important.", "재능도 도움이 되지만 노력과 태도도 매우 중요해."),
                ("Me", "I want to improve little by little.", "조금씩 발전하고 싶어요."),
                ("Jungkook", "That is the right mindset. Do not compare yourself too much with others.", "그게 좋은 마음가짐이야. 다른 사람과 너무 많이 비교하지 마."),
                ("Me", "I will focus on my own growth.", "제 성장에 집중할게요."),
                ("Jungkook", "Good. Keep practicing, enjoy the process, and trust your own voice.", "좋아. 계속 연습하고, 과정을 즐기고, 너만의 목소리를 믿어.")
            ],
            "key_expressions": [
                "Small practice can make a big difference.",
                "I feel nervous.",
                "How can I become more confident?",
                "Effort and attitude are important.",
                "Focus on my own growth.",
                "Trust your own voice."
            ],
            "questions": [
                ("1. What does the student like?", ["Singing and watching performances", "Only sleeping", "Cooking alone", "Reading maps"], "Singing and watching performances"),
                ("2. What can small practice do?", ["Make a big difference", "Make people forget everything", "Stop growth", "Make practice useless"], "Make a big difference"),
                ("3. What does Jungkook tell the student to trust?", ["Your own voice", "Only luck", "A computer", "Other people's opinions"], "Your own voice")
            ],
            "reflection_prompt": "Jungkook을 통해 내가 배울 점은 무엇인가요?"
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
                ("Me", "I feel amazed when I look down.", "아래를 내려다보니 정말 경이로워요."),
                ("Guide", "This place was made over a very long time.", "이곳은 아주 오랜 시간에 걸쳐 만들어졌어요."),
                ("Me", "How long did it take?", "얼마나 오래 걸렸나요?"),
                ("Guide", "It took millions of years for nature to shape this canyon.", "자연이 이 협곡을 만드는 데 수백만 년이 걸렸어요."),
                ("Me", "That makes me respect nature more.", "그 말을 들으니 자연을 더 존중하게 돼요."),
                ("Guide", "Yes. Nature is powerful, but it also needs our care.", "맞아요. 자연은 강하지만 우리의 보살핌도 필요해요."),
                ("Me", "I want to protect nature.", "저는 자연을 보호하고 싶어요."),
                ("Guide", "That is a good attitude. Small actions can help the earth.", "좋은 태도예요. 작은 행동이 지구에 도움이 될 수 있어요.")
            ],
            "key_expressions": [
                "It is huge and beautiful.",
                "I feel amazed.",
                "Nature is powerful.",
                "Protect nature.",
                "Small actions can help the earth."
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
                ("Me", "It feels busy and exciting.", "바쁘고 신나게 느껴져요."),
                ("Guide", "New York is often called a city of dreams.", "뉴욕은 종종 꿈의 도시라고 불려요."),
                ("Me", "Why do people come here?", "사람들은 왜 이곳에 오나요?"),
                ("Guide", "Many people come here to study, work, create, and challenge themselves.", "많은 사람들이 공부하고, 일하고, 창작하고, 도전하기 위해 이곳에 와요."),
                ("Me", "That sounds inspiring.", "그 말이 영감을 줘요."),
                ("Guide", "A big city can be difficult, but it can also give people new chances.", "큰 도시는 힘들 수 있지만 사람들에게 새로운 기회를 주기도 해요."),
                ("Me", "I want to follow my dream too.", "저도 제 꿈을 따라가고 싶어요."),
                ("Guide", "Then keep learning and do not be afraid of new places.", "그렇다면 계속 배우고 새로운 곳을 두려워하지 마세요.")
            ],
            "key_expressions": [
                "There are so many people.",
                "Many cultures live here.",
                "It feels exciting.",
                "Challenge yourself.",
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
                ("Me", "I can see old buildings and traditional colors.", "오래된 건물과 전통적인 색을 볼 수 있어요."),
                ("Guide", "Yes. Places like this help us remember the past.", "맞아요. 이런 장소는 우리가 과거를 기억하도록 도와줘요."),
                ("Me", "Why is history important?", "역사는 왜 중요한가요?"),
                ("Guide", "History helps us understand who we are.", "역사는 우리가 누구인지 이해하도록 도와줍니다."),
                ("Me", "I want to learn more about Korean culture.", "한국 문화에 대해 더 배우고 싶어요."),
                ("Guide", "That is a good idea. Culture connects people across time.", "좋은 생각이에요. 문화는 시간을 넘어 사람들을 연결합니다."),
                ("Me", "I will respect our culture.", "우리 문화를 존중하겠습니다."),
                ("Guide", "Good. When we understand the past, we can build a better future.", "좋아요. 과거를 이해할 때 더 나은 미래를 만들 수 있어요.")
            ],
            "key_expressions": [
                "This palace is beautiful.",
                "It shows history and culture.",
                "Learn more about history.",
                "Respect our culture.",
                "Build a better future."
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
