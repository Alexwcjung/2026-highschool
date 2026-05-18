
import streamlit as st
import random
import html
import re
import time

# =========================================================
# Pop Song English Learning App
# 5 tabs:
# 1. Background
# 2. Lyrics & Quiz
# 3. Key Expression Meaning Game
# 4. Sentence Matching Game
# 5. Reflective Writing
# =========================================================

st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
.stApp { background-color:#ffffff; color:#1e293b; }
.main-title {
    background: linear-gradient(135deg,#eef2ff,#f0f9ff,#fdf2f8);
    padding: 25px;
    border-radius: 18px;
    border: 2px solid #6366f1;
    text-align: center;
    color: #3730a3;
    margin-bottom: 22px;
}
.info-box {
    background-color:#f8fafc;
    padding:24px;
    border-radius:18px;
    border:1px solid #cbd5e1;
    line-height:1.9;
    margin-bottom:22px;
}
.info-box h3 {
    color:#4338ca;
    border-bottom:3px solid #6366f1;
    padding-bottom:10px;
}
.lyrics-container {
    padding:14px 20px;
    border-left:5px solid #6366f1;
    margin-bottom:10px;
    background-color:#f8fafc;
    border-radius:0 12px 12px 0;
}
.eng-line { font-size:1.08rem; font-weight:800; color:#1e3a8a; }
.kor-sub { font-size:0.95rem; color:#64748b; margin-top:5px; line-height:1.6; }
.quiz-box {
    background-color:#f0f9ff;
    padding:20px;
    border-radius:18px;
    border:1px solid #bae6fd;
    margin-top:22px;
    margin-bottom:20px;
}
.score-box {
    background:linear-gradient(135deg,#dcfce7,#bbf7d0);
    padding:18px;
    border-radius:18px;
    border:1px solid #86efac;
    margin-top:18px;
    text-align:center;
    font-size:1.15rem;
    font-weight:900;
}
.wrong-box {
    background:#fff7ed;
    padding:15px;
    border-radius:14px;
    border:1px solid #fdba74;
    margin-top:10px;
}
.game-card {
    background:linear-gradient(135deg,#eef2ff,#f8fafc);
    border:1px solid #c7d2fe;
    border-radius:18px;
    padding:20px;
    margin-bottom:18px;
}
.big-guide {
    font-size:1.12rem;
    font-weight:800;
    color:#475569;
    line-height:1.7;
}
.matching-box {
    background:linear-gradient(135deg,#eef2ff 0%,#f0f9ff 50%,#fdf2f8 100%);
    padding:24px;
    border-radius:20px;
    border:1px solid #c7d2fe;
    margin-top:18px;
    margin-bottom:22px;
}
.matching-title {
    font-size:2rem;
    font-weight:900;
    color:#4338ca;
    margin-bottom:10px;
}
.selected-card-notice {
    background-color:#fef3c7;
    padding:14px 16px;
    border-radius:14px;
    border:1px solid #facc15;
    color:#92400e;
    font-size:1.05rem;
    font-weight:900;
    margin-bottom:16px;
}
.feedback-ko {
    background:#fefce8;
    border:1px solid #fde68a;
    padding:18px;
    border-radius:16px;
    line-height:1.8;
    margin-top:14px;
}
.feedback-en {
    background:#eff6ff;
    border:1px solid #bfdbfe;
    padding:18px;
    border-radius:16px;
    line-height:1.8;
    margin-top:14px;
}
.advice-box {
    background:#f0fdf4;
    border:1px solid #bbf7d0;
    padding:18px;
    border-radius:16px;
    line-height:1.8;
    margin-top:14px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# Utility functions
# =========================================================

def clean_text_for_display(text: str) -> str:
    return html.escape(str(text).strip())

def safe_key(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9가-힣_]+", "_", text)

def shuffle_options(options, seed):
    rng = random.Random(seed)
    options = list(options)
    rng.shuffle(options)
    return options

def try_translate_ko_to_en(korean_text: str) -> str:
    """
    한국어 피드백을 영어로 번역합니다.
    deep-translator가 설치되어 있으면 실제 번역을 시도하고,
    실패하면 자연스러운 영어 피드백 템플릿으로 대체합니다.
    영어 피드백 안에 학생의 한국어 답변을 그대로 끼워 넣지 않습니다.
    """
    korean_text = str(korean_text).strip()
    if not korean_text:
        return ""

    try:
        from deep_translator import GoogleTranslator
        translated = GoogleTranslator(source="ko", target="en").translate(korean_text)
        translated = str(translated).strip()

        # 번역 결과에 한글이 섞여 있으면 학생 답변이 그대로 들어간 것으로 보고 대체합니다.
        if re.search(r"[가-힣]", translated):
            raise ValueError("Korean text remained in English translation.")

        return translated
    except Exception:
        return (
            "Your writing expresses a personal memory and emotion in a thoughtful way. "
            "It does not simply describe what happened; it shows how the song helped you look back "
            "on your own relationships, choices, and feelings. To make your writing stronger, "
            "add one specific moment, one clear feeling, and one lesson you learned from the experience."
        )

def make_polished_feedback(song_title: str, question: str, student_answer: str):
    """
    학생 답변을 평가하는 방식이 아니라,
    학생이 쓴 내용을 바탕으로 한국어 문단을 조금 더 풍부하게 다듬고,
    그 한국어 문단을 영어로 번역해 줍니다.
    마지막에는 쓰기 조언만 제시합니다.

    주의:
    - 영어 번역에는 학생의 한국어 원문을 그대로 섞어 넣지 않습니다.
    - deep-translator가 설치되어 있으면 번역을 시도합니다.
    - 번역 실패 시에는 한국어가 섞이지 않는 안전한 영어 문단을 제공합니다.
    """
    answer = str(student_answer).strip()
    question = str(question).strip()

    # 너무 짧은 답변일 때도 학생 답변을 바탕으로 자연스럽게 확장
    if len(answer) < 10:
        polished_ko = (
            "이 노래를 들으며 아직 생각을 길게 정리하지는 못했지만, "
            "마음속에 떠오르는 감정이 있다는 점이 중요합니다. "
            "노래 속 화자의 마음처럼, 나에게도 쉽게 말하지 못한 기억이나 "
            "다시 생각해 보고 싶은 순간이 있을 수 있습니다. "
            "그 감정을 조금 더 자세히 들여다보면, 단순한 감상이 아니라 "
            "나 자신을 이해하는 글로 발전할 수 있습니다."
        )
    else:
        # 학생 원문을 그대로 베끼기보다, “학생이 쓴 내용”으로 받아 자연스럽게 문단화
        polished_ko = (
            f"이 노래를 들으며 나는 다음과 같은 생각을 하게 되었습니다. "
            f"{answer} "
            f"이 경험은 단순히 지나간 일을 떠올리는 데서 끝나지 않습니다. "
            f"그때의 감정과 지금의 마음을 함께 돌아보게 하며, "
            f"사람과의 관계가 언제나 쉽지만은 않다는 사실도 생각하게 합니다. "
            f"노래 속 화자가 처음으로 돌아가고 싶어 하거나, 누군가에게 미안함과 그리움을 전하려는 것처럼, "
            f"나 역시 과거의 한 장면을 다시 바라보며 그때 미처 표현하지 못했던 마음을 생각해 볼 수 있었습니다. "
            f"이런 성찰은 나의 감정을 더 깊이 이해하고, 앞으로의 관계를 조금 더 성숙하게 바라보는 계기가 됩니다."
        )

    # The Scientist 관련 질문이면 조금 더 관계·그리움 중심으로 다듬기
    if ("Scientist" in song_title or "그리운" in question or "옛" in question or "처음" in question or "관계" in question) and len(answer) >= 10:
        polished_ko = (
            f"이 노래를 들으며 나는 과거의 관계와 그때의 감정을 다시 떠올리게 되었습니다. "
            f"{answer} "
            f"그 기억은 단순한 추억이라기보다, 마음을 쉽게 열지 못했던 순간과 "
            f"서로를 충분히 이해하지 못했던 시간을 돌아보게 합니다. "
            f"노래 속 화자가 ‘처음으로 돌아가고 싶다’고 말하는 것처럼, "
            f"나 역시 그때로 돌아간다면 조금 더 솔직하게 말하고, 상대의 마음을 더 천천히 이해하려 했을 것 같습니다. "
            f"결국 이 노래는 사랑이나 관계가 생각처럼 쉽지 않지만, "
            f"그 어려움 속에서도 우리는 자신의 감정과 선택을 배울 수 있다는 점을 느끼게 해 줍니다."
        )

    english_translation = try_translate_ko_to_en(polished_ko)

    # 번역 실패 또는 번역 결과에 한국어가 남아 있을 경우 안전한 영어 문단으로 대체
    if re.search(r"[가-힣]", english_translation):
        english_translation = (
            "While listening to this song, I looked back on a past relationship and the emotions I felt at that time. "
            "The memory was not just a simple memory; it helped me think about moments when it was difficult to open my heart "
            "and when two people could not fully understand each other. Like the speaker in the song who wants to go back to the start, "
            "I also wondered what I might say or do differently if I could return to that moment. In the end, this song reminds me that "
            "love and relationships are not always easy, but they can help us understand our feelings and grow as a person."
        )

    advice = (
        "쓰기 조언: 글을 더 좋게 만들고 싶다면 ① 떠오른 사람이나 장면, ② 그때의 감정, ③ 지금 돌아보며 깨달은 점을 차례로 써 보세요. "
        "영어로 쓸 때는 다음 구조를 활용하면 좋습니다: "
        "While listening to this song, I thought about ~. / At that time, I felt ~ because ~. / Looking back now, I realize that ~."
    )

    return polished_ko, english_translation, advice


# =========================================================
# Song data
# =========================================================

SONGS = {
    "1. Let It Go - Frozen OST": {
        "video_url": "https://www.youtube.com/watch?v=RgGRyssdJvw",
        "bg": """
        <h3>❄️ Let It Go: 숨겨 왔던 자신을 받아들이는 순간</h3>
        <p><b>Let It Go</b>는 영화 <i>Frozen</i>의 대표곡으로, 엘사가 더 이상 자신의 능력과 감정을 숨기지 않고 스스로를 받아들이는 장면에서 나오는 노래입니다.</p>
        <p>이 노래는 단순히 모든 것을 잊겠다는 뜻이 아니라, 두려움과 타인의 시선에서 벗어나 자기 자신을 인정하는 과정을 보여 줍니다.</p>
        """,
        "lyrics": [
            ("The snow glows white on the mountain tonight / Not a footprint to be seen", "오늘 밤 산 위에는 눈이 하얗게 빛나고 / 발자국 하나 보이지 않아요"),
            ("A kingdom of isolation / And it looks like I'm the queen", "고립된 왕국 / 그리고 내가 그곳의 여왕인 것 같아요"),
            ("Conceal, don't feel, don't let them know / Well, now they know", "숨기고, 느끼지 말고, 알게 하지 마 / 하지만 이제 그들이 알아버렸어요"),
            ("Let it go, let it go / Can't hold it back anymore", "놓아버려, 놓아버려 / 더 이상 억누를 수 없어"),
            ("I don't care what they're going to say / Let the storm rage on", "사람들이 뭐라고 하든 상관없어 / 폭풍이 계속 몰아치게 둬"),
            ("The cold never bothered me anyway", "어차피 추위는 나를 괴롭힌 적이 없으니까"),
            ("It's time to see what I can do / To test the limits and break through", "이제 내가 무엇을 할 수 있는지 볼 시간이야 / 한계를 시험하고 깨고 나아갈 시간이야"),
            ("No right, no wrong, no rules for me / I'm free", "옳고 그름도, 나를 묶는 규칙도 없어 / 나는 자유로워"),
            ("I'm never going back, the past is in the past", "나는 절대 돌아가지 않아, 과거는 과거일 뿐이야"),
            ("That perfect girl is gone", "그 완벽한 소녀는 이제 없어"),
        ],
        "quiz": [
            ("이 노래를 부르는 인물은 누구인가요?", ["Anna", "Olaf", "Elsa", "Kristoff"], "Elsa"),
            ("엘사가 더 이상 하지 않으려는 것은 무엇인가요?", ["자신을 숨기는 것", "학교에 가는 것", "노래하는 것", "운동하는 것"], "자신을 숨기는 것"),
            ("이 노래의 중심 감정은 무엇인가요?", ["자유와 해방감", "질투", "배고픔", "지루함"], "자유와 해방감"),
            ("'conceal'의 뜻은 무엇인가요?", ["숨기다", "달리다", "웃다", "먹다"], "숨기다"),
            ("'The past is in the past'의 뜻은 무엇인가요?", ["과거는 과거일 뿐이다", "과거로 돌아가자", "과거가 제일 중요하다", "과거를 만들자"], "과거는 과거일 뿐이다"),
        ],
        "key_expressions": [
            ("Let it go", "놓아버려"),
            ("Can't hold it back anymore", "더 이상 억누를 수 없어"),
            ("Conceal, don't feel", "숨기고, 느끼지 마"),
            ("Let the storm rage on", "폭풍이 계속 몰아치게 둬"),
            ("I'm free", "나는 자유로워"),
            ("The past is in the past", "과거는 과거일 뿐이야"),
            ("Here I stand", "나는 여기 서 있어"),
            ("The cold never bothered me anyway", "어차피 추위는 나를 괴롭힌 적이 없어"),
            ("Test the limits", "한계를 시험하다"),
            ("Break through", "뚫고 나아가다"),
        ],
        "matching": [
            ("Let it go", "놓아버려"),
            ("Can't hold it back anymore", "더 이상 억누를 수 없어"),
            ("I'm free", "나는 자유로워"),
            ("The past is in the past", "과거는 과거일 뿐이야"),
            ("Here I stand", "나는 여기 서 있어"),
            ("The cold never bothered me anyway", "어차피 추위는 나를 괴롭힌 적이 없어"),
        ],
        "reflect_questions": [
            "다른 사람의 시선 때문에 나 자신을 숨긴 적이 있나요?",
            "내가 더 이상 붙잡고 싶지 않은 두려움이나 걱정은 무엇인가요?",
            "이 노래처럼 ‘나는 자유로워’라고 말하고 싶은 순간은 언제인가요?",
        ],
    },

    "2. Hello - Adele": {
        "video_url": "https://www.youtube.com/watch?v=h7NBamHcX58",
        "bg": """
        <h3>☎️ Hello: 과거의 누군가에게 건네는 늦은 안부</h3>
        <p>Adele의 <b>Hello</b>는 시간이 흐른 뒤 과거의 누군가에게 다시 연락하고 싶은 마음, 미안함, 후회, 치유되지 않은 감정을 담은 노래입니다.</p>
        """,
        "lyrics": [
            ("Hello, it's me / I was wondering if after all these years you'd like to meet", "안녕, 나야 / 이 모든 세월이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
            ("They say that time's supposed to heal ya / But I ain't done much healing", "사람들은 시간이 치유해 준다고 하지만 / 나는 별로 치유되지 않은 것 같아"),
            ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
            ("I'm in California dreaming about who we used to be", "나는 캘리포니아에서 예전의 우리 모습을 떠올리고 있어"),
            ("There's such a difference between us / And a million miles", "우리 사이에는 큰 차이가 있고 / 아주 먼 거리도 있어"),
            ("Hello from the other side", "저편에서 안녕이라고 말해"),
            ("I'm sorry, for everything that I've done", "내가 했던 모든 일에 대해 미안해"),
            ("At least I can say that I've tried", "적어도 나는 노력했다고 말할 수 있어"),
            ("I'm sorry, for breaking your heart", "네 마음을 아프게 해서 미안해"),
            ("I hope that you're well", "네가 잘 지내길 바라"),
        ],
        "quiz": [
            ("화자가 가장 말하고 싶어 하는 것은 무엇인가요?", ["미안하다는 말", "축하한다는 말", "화났다는 말", "떠나자는 말"], "미안하다는 말"),
            ("사람들은 시간이 무엇을 해 준다고 말하나요?", ["상처를 치유해 준다", "돈을 벌게 해 준다", "과거를 지운다", "노래하게 한다"], "상처를 치유해 준다"),
            ("'I tried'는 어떤 의미인가요?", ["노력했다", "잊었다", "웃었다", "떠났다"], "노력했다"),
            ("이 노래의 중심 감정은 무엇인가요?", ["후회와 사과", "분노와 복수", "승리와 환호", "농담과 웃음"], "후회와 사과"),
            ("'the other side'는 무엇을 상징할 수 있나요?", ["멀어진 시간과 마음의 거리", "교실 반대편", "무대 왼쪽", "집 앞"], "멀어진 시간과 마음의 거리"),
        ],
        "key_expressions": [
            ("Hello, it's me", "안녕, 나야"),
            ("After all these years", "이 모든 세월이 흐른 뒤에"),
            ("Time's supposed to heal you", "시간이 너를 치유해 줄 거라고 여겨진다"),
            ("Can you hear me?", "내 말 들리니?"),
            ("Who we used to be", "예전의 우리 모습"),
            ("Hello from the other side", "저편에서 전하는 안녕"),
            ("I must've called a thousand times", "정말 여러 번 전화했을 거야"),
            ("I'm sorry", "미안해"),
            ("At least I can say that I've tried", "적어도 노력했다고 말할 수 있어"),
            ("I hope that you're well", "네가 잘 지내길 바라"),
        ],
        "matching": [
            ("Hello, it's me", "안녕, 나야"),
            ("I'm sorry", "미안해"),
            ("I tried", "나는 노력했어"),
            ("Hello from the other side", "저편에서 안녕이라고 말해"),
            ("Can you hear me?", "내 말 들리니?"),
            ("I hope that you're well", "네가 잘 지내길 바라"),
        ],
        "reflect_questions": [
            "오랫동안 연락하지 못했지만 다시 이야기하고 싶은 사람이 있나요?",
            "누군가에게 미안하다고 말하지 못했던 경험이 있나요?",
            "시간이 지나면서 치유된 감정이나 아직 남아 있는 감정이 있나요?",
        ],
    },

    "3. A Whole New World - Aladdin OST": {
        "video_url": "https://www.youtube.com/watch?v=9FJssSUxI88",
        "bg": """
        <h3>🕌 A Whole New World: 새로운 세상을 바라보는 순간</h3>
        <p><b>A Whole New World</b>는 알라딘과 자스민이 마법 양탄자를 타고 새로운 세상과 자유를 경험하는 장면의 노래입니다.</p>
        """,
        "lyrics": [
            ("I can show you the world / Shining, shimmering, splendid", "내가 너에게 세상을 보여 줄 수 있어 / 빛나고 반짝이는 눈부신 세상을"),
            ("Tell me, princess, now when did you last let your heart decide?", "말해 봐요, 공주님, 마지막으로 마음이 선택하게 둔 때가 언제였나요?"),
            ("I can open your eyes", "내가 너의 눈을 뜨게 해 줄 수 있어"),
            ("Take you wonder by wonder", "놀라움에서 또 다른 놀라움으로 데려가며"),
            ("A whole new world", "완전히 새로운 세상"),
            ("A new fantastic point of view", "새롭고 환상적인 관점"),
            ("No one to tell us no / Or where to go", "아무도 우리에게 안 된다고 하거나 어디로 가라고 하지 않아"),
            ("Unbelievable sights / Indescribable feeling", "믿기 어려운 풍경들 / 말로 표현할 수 없는 감정"),
            ("Don't you dare close your eyes", "절대 눈 감지 마"),
            ("With new horizons to pursue", "따라갈 새로운 지평선들이 있고"),
        ],
        "quiz": [
            ("두 사람은 무엇을 타고 있나요?", ["마법 양탄자", "기차", "자전거", "배"], "마법 양탄자"),
            ("'A whole new world'가 상징하는 것은 무엇인가요?", ["새로운 시선과 경험", "낡은 방", "어려운 시험", "혼자 있는 시간"], "새로운 시선과 경험"),
            ("'point of view'의 뜻은 무엇인가요?", ["관점", "속도", "약속", "문"], "관점"),
            ("노래의 중심 감정은 무엇인가요?", ["설렘과 자유로움", "후회와 슬픔", "분노와 복수", "지루함"], "설렘과 자유로움"),
            ("'Don't you dare close your eyes'는 어떤 의미인가요?", ["절대 눈 감지 마", "지금 자도 돼", "천천히 걸어", "말하지 마"], "절대 눈 감지 마"),
        ],
        "key_expressions": [
            ("I can show you the world", "내가 너에게 세상을 보여 줄 수 있어"),
            ("Shining, shimmering, splendid", "빛나고 반짝이고 눈부신"),
            ("Let your heart decide", "마음이 결정하게 하다"),
            ("Open your eyes", "눈을 뜨게 하다"),
            ("A whole new world", "완전히 새로운 세상"),
            ("Point of view", "관점"),
            ("No one to tell us no", "아무도 안 된다고 말하지 않음"),
            ("Unbelievable sights", "믿기 어려운 풍경들"),
            ("Indescribable feeling", "말로 표현할 수 없는 감정"),
            ("New horizons to pursue", "따라갈 새로운 지평선들"),
        ],
        "matching": [
            ("I can show you the world", "내가 너에게 세상을 보여 줄 수 있어"),
            ("A whole new world", "완전히 새로운 세상"),
            ("A new fantastic point of view", "새롭고 환상적인 시선"),
            ("Don't you dare close your eyes", "절대 눈 감지 마"),
            ("Open your eyes", "눈을 떠 봐"),
            ("Every turn a surprise", "방향을 틀 때마다 놀라움이 있어"),
        ],
        "reflect_questions": [
            "내가 경험해 보고 싶은 ‘완전히 새로운 세상’은 무엇인가요?",
            "누군가가 나에게 새로운 관점을 보여 준 적이 있나요?",
            "두려움보다 설렘이 더 컸던 경험이 있나요?",
        ],
    },

    "4. Stand By Me - Ben E. King": {
        "video_url": "https://www.youtube.com/watch?v=c5hDjpi_HM0",
        "bg": """
        <h3>🤝 Stand By Me: 곁에 있어 주는 힘</h3>
        <p><b>Stand By Me</b>는 어둡고 불안한 순간에도 누군가가 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다.</p>
        """,
        "lyrics": [
            ("When the night has come / And the land is dark", "밤이 찾아오고 / 세상이 어두워질 때"),
            ("And the moon is the only light we'll see", "달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
            ("No, I won't be afraid", "아니, 나는 두려워하지 않을 거야"),
            ("Just as long as you stand / Stand by me", "네가 곁에 있어 준다면 / 내 곁에 있어 준다면"),
            ("So darlin', darlin' / Stand by me", "그러니 사랑하는 사람아 / 내 곁에 있어 줘"),
            ("If the sky that we look upon / Should tumble and fall", "우리가 바라보는 하늘이 / 무너져 내린다 해도"),
            ("Or the mountain should crumble to the sea", "산이 부서져 바다로 무너져 내린다 해도"),
            ("I won't cry, I won't cry", "나는 울지 않을 거야, 울지 않을 거야"),
            ("No, I won't shed a tear", "아니, 눈물 한 방울도 흘리지 않을 거야"),
            ("Whenever you're in trouble / Won't you stand by me?", "네가 힘든 순간에 / 내 곁에 있어 주지 않을래?"),
        ],
        "quiz": [
            ("이 노래는 어떤 시간적 배경으로 시작하나요?", ["밤", "아침", "점심", "수업 시간"], "밤"),
            ("보이는 유일한 빛은 무엇인가요?", ["달빛", "햇빛", "휴대전화 불빛", "촛불"], "달빛"),
            ("'Stand by me'의 뜻은 무엇인가요?", ["내 곁에 있어 줘", "멀리 가", "앉아 있어", "집에 가"], "내 곁에 있어 줘"),
            ("화자가 두려워하지 않는 이유는 무엇인가요?", ["누군가가 곁에 있기 때문에", "돈이 많기 때문에", "날씨가 좋기 때문에", "잠을 자기 때문에"], "누군가가 곁에 있기 때문에"),
            ("'I won't shed a tear'의 뜻은 무엇인가요?", ["눈물 한 방울도 흘리지 않겠다", "많이 웃겠다", "멀리 떠나겠다", "잠을 자겠다"], "눈물 한 방울도 흘리지 않겠다"),
        ],
        "key_expressions": [
            ("Stand by me", "내 곁에 있어 줘"),
            ("The night has come", "밤이 찾아왔다"),
            ("The land is dark", "세상이 어둡다"),
            ("The only light", "유일한 빛"),
            ("I won't be afraid", "나는 두려워하지 않을 거야"),
            ("Just as long as", "~하는 한"),
            ("Tumble and fall", "무너져 내리다"),
            ("Crumble to the sea", "바다로 무너져 내리다"),
            ("I won't shed a tear", "눈물 한 방울도 흘리지 않을 거야"),
            ("Whenever you're in trouble", "네가 힘든 순간에는 언제든지"),
        ],
        "matching": [
            ("Stand by me", "내 곁에 있어 줘"),
            ("I won't be afraid", "나는 두려워하지 않을 거야"),
            ("I won't cry", "나는 울지 않을 거야"),
            ("Whenever you're in trouble", "네가 힘든 순간에는 언제든지"),
            ("The land is dark", "세상이 어두워"),
            ("The moon is the only light", "달빛만이 유일한 빛이야"),
        ],
        "reflect_questions": [
            "내가 힘들 때 곁에 있어 주었던 사람은 누구인가요?",
            "누군가에게 ‘내 곁에 있어 줘’라고 말하고 싶었던 순간이 있나요?",
            "나도 누군가에게 힘이 되어 준 경험이 있나요?",
        ],
    },

    "5. Don't Know Why - Norah Jones": {
        "video_url": "https://www.youtube.com/watch?v=nhLdJeLTM48",
        "bg": """
        <h3>🌙 Don't Know Why: 이유를 알 수 없는 마음</h3>
        <p><b>Don't Know Why</b>는 조용하고 부드러운 멜로디 속에 설명하기 어려운 아쉬움과 후회를 담고 있는 노래입니다.</p>
        """,
        "lyrics": [
            ("I waited 'til I saw the sun", "나는 해가 보일 때까지 기다렸어"),
            ("I don't know why I didn't come", "왜 내가 가지 않았는지 모르겠어"),
            ("I left you by the house of fun", "나는 너를 즐거움의 집 곁에 남겨 두었어"),
            ("When I saw the break of day", "새벽이 밝아오는 것을 보았을 때"),
            ("I wished that I could fly away", "나는 날아가 버릴 수 있기를 바랐어"),
            ("Instead of kneeling in the sand", "모래 위에 무릎 꿇고 있는 대신"),
            ("Catching tear-drops in my hand", "손으로 눈물방울을 받으며"),
            ("You'll be on my mind forever", "너는 영원히 내 마음속에 있을 거야"),
            ("Driving down the road alone", "혼자 길을 따라 운전하며"),
            ("I feel as empty as a drum", "나는 북처럼 텅 빈 기분이야"),
        ],
        "quiz": [
            ("화자는 무엇을 볼 때까지 기다렸나요?", ["해", "버스", "선생님", "전화"], "해"),
            ("화자가 계속 모르겠다고 말하는 것은 무엇인가요?", ["왜 자신이 가지 않았는지", "무엇을 먹을지", "학교가 어디인지", "어떻게 읽는지"], "왜 자신이 가지 않았는지"),
            ("'break of day'의 뜻은 무엇인가요?", ["새벽", "한밤중", "점심시간", "겨울"], "새벽"),
            ("노래의 분위기는 어떤가요?", ["조용하고 후회스러운 분위기", "화나고 시끄러운 분위기", "빠르고 웃긴 분위기", "신나는 분위기"], "조용하고 후회스러운 분위기"),
            ("'empty as a drum'은 어떤 감정에 가깝나요?", ["공허함", "자신감", "배부름", "분노"], "공허함"),
        ],
        "key_expressions": [
            ("I don't know why", "나는 왜 그런지 모르겠어"),
            ("I didn't come", "나는 가지 않았어"),
            ("The break of day", "새벽"),
            ("I wished that I could fly away", "나는 날아가 버릴 수 있기를 바랐어"),
            ("Tear-drops", "눈물방울"),
            ("On my mind", "마음속에 있는"),
            ("Forever", "영원히"),
            ("Endless sea", "끝없는 바다"),
            ("Driving down the road alone", "혼자 길을 따라 운전하며"),
            ("Empty as a drum", "북처럼 텅 빈"),
        ],
        "matching": [
            ("I don't know why", "나는 왜 그런지 모르겠어"),
            ("I wished that I could fly away", "나는 날아가 버릴 수 있기를 바랐어"),
            ("You'll be on my mind forever", "너는 영원히 내 마음속에 있을 거야"),
            ("I feel as empty as a drum", "나는 북처럼 텅 빈 기분이야"),
            ("I waited till I saw the sun", "나는 해가 보일 때까지 기다렸어"),
            ("Driving down the road alone", "혼자 길을 따라 운전하며"),
        ],
        "reflect_questions": [
            "왜 그랬는지 스스로도 잘 설명할 수 없는 선택을 한 적이 있나요?",
            "마음속에 오래 남아 있는 사람이나 기억이 있나요?",
            "후회가 남는 일을 지금 다시 바라본다면 어떤 생각이 드나요?",
        ],
    },

    "6. Fix You - Coldplay": {
        "video_url": "https://www.youtube.com/watch?v=Z0IZ3MjGFEo",
        "bg": """
        <h3>💡 Fix You: 힘든 순간에 건네는 위로</h3>
        <p>Coldplay의 <b>Fix You</b>는 실패, 상실, 지침, 슬픔을 겪는 사람에게 따뜻한 위로를 건네는 노래입니다.</p>
        """,
        "lyrics": [
            ("When you try your best, but you don't succeed", "네가 최선을 다했지만 성공하지 못할 때"),
            ("When you get what you want, but not what you need", "원하는 것을 얻었지만 정작 필요한 것은 얻지 못할 때"),
            ("When you feel so tired, but you can't sleep", "너무 지쳤지만 잠들 수 없을 때"),
            ("Stuck in reverse", "거꾸로 갇혀 있는 것처럼 느껴질 때"),
            ("When you lose something you can't replace", "대신할 수 없는 무언가를 잃었을 때"),
            ("Could it be worse?", "이보다 더 나쁠 수 있을까?"),
            ("Lights will guide you home", "빛이 너를 집으로 인도할 거야"),
            ("And ignite your bones", "그리고 네 안의 힘을 다시 밝혀 줄 거야"),
            ("And I will try to fix you", "그리고 나는 너를 다시 일으켜 주려고 노력할 거야"),
            ("I promise you I will learn from my mistakes", "나는 내 실수에서 배우겠다고 약속할게"),
        ],
        "quiz": [
            ("이 노래는 어떤 사람을 위로하나요?", ["힘들고 지친 사람", "여행을 떠나는 사람", "운동을 시작한 사람", "시험 보는 사람"], "힘들고 지친 사람"),
            ("'try your best'의 뜻은 무엇인가요?", ["최선을 다하다", "잠을 자다", "숨다", "잊다"], "최선을 다하다"),
            ("want와 need의 차이로 알맞은 것은?", ["want는 원하는 것, need는 정말 필요한 것", "둘은 항상 같다", "want는 필요 없는 것", "need는 노래하는 것"], "want는 원하는 것, need는 정말 필요한 것"),
            ("'Lights will guide you home'은 무엇을 상징하나요?", ["희망과 방향", "가게 간판", "휴대전화 불빛", "자동차 헤드라이트만"], "희망과 방향"),
            ("이 노래의 중심 감정은 무엇인가요?", ["위로와 희망", "분노와 복수", "웃음과 장난", "경쟁과 승리"], "위로와 희망"),
        ],
        "key_expressions": [
            ("Try your best", "최선을 다하다"),
            ("Don't succeed", "성공하지 못하다"),
            ("What you want", "네가 원하는 것"),
            ("What you need", "네게 필요한 것"),
            ("Stuck in reverse", "거꾸로 갇힌 듯한"),
            ("Tears stream down your face", "눈물이 얼굴을 타고 흐르다"),
            ("You can't replace", "대신할 수 없다"),
            ("Lights will guide you home", "빛이 너를 집으로 인도할 거야"),
            ("Ignite your bones", "네 안의 힘을 다시 밝혀 주다"),
            ("Learn from my mistakes", "내 실수에서 배우다"),
        ],
        "matching": [
            ("When you try your best", "네가 최선을 다할 때"),
            ("Lights will guide you home", "빛이 너를 집으로 인도할 거야"),
            ("I will try to fix you", "나는 너를 다시 일으켜 주려고 노력할 거야"),
            ("If you never try, you'll never know", "시도하지 않으면 절대 알 수 없어"),
            ("Tears stream down your face", "눈물이 네 얼굴을 타고 흘러내려"),
            ("I will learn from my mistakes", "나는 내 실수에서 배울 거야"),
        ],
        "reflect_questions": [
            "최선을 다했지만 원하는 결과를 얻지 못했던 경험이 있나요?",
            "힘들 때 나를 다시 일으켜 준 사람이나 말이 있었나요?",
            "나도 누군가를 위로하거나 도와주고 싶었던 적이 있나요?",
        ],
    },

    "7. The Scientist - Coldplay": {
        "video_url": "https://www.youtube.com/watch?v=RB-RcX5DS5A",
        "bg": """
        <h3>🔬 The Scientist: 처음으로 돌아가고 싶은 마음</h3>
        <p>Coldplay의 <b>The Scientist</b>는 지나간 관계와 후회를 돌아보며, 처음으로 돌아가 다시 말하고 싶은 마음을 담은 노래입니다.</p>
        <p>노래 속 화자는 사랑과 이별을 과학처럼 분석하려 하지만, 마음은 숫자와 공식처럼 쉽게 설명되지 않는다는 것을 깨닫습니다.</p>
        """,
        "lyrics": [
            ("Come up to meet you, tell you I'm sorry", "너를 만나러 와서 미안하다고 말하려 해"),
            ("You don't know how lovely you are", "너는 네가 얼마나 사랑스러운지 몰라"),
            ("I had to find you", "나는 너를 찾아야 했어"),
            ("Tell you I need you", "네가 필요하다고 말해야 했어"),
            ("Tell you I set you apart", "네가 나에게 특별하다고 말해야 했어"),
            ("Tell me your secrets", "네 비밀을 말해 줘"),
            ("And ask me your questions", "그리고 내게 질문을 해 줘"),
            ("Oh, let's go back to the start", "오, 처음으로 돌아가자"),
            ("Running in circles", "빙빙 돌고 있어"),
            ("Coming up tails", "계속 좋지 않은 결과가 나와"),
            ("Heads on a science apart", "머리는 과학처럼 따로 떨어져 있어"),
            ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
            ("It's such a shame for us to part", "우리가 헤어진다는 건 정말 안타까운 일이야"),
            ("No one ever said it would be this hard", "아무도 이렇게 힘들 거라고 말하지 않았어"),
            ("Oh, take me back to the start", "오, 나를 처음으로 데려가 줘"),
            ("I was just guessing at numbers and figures", "나는 그저 숫자와 수치를 추측하고 있었어"),
            ("Pulling the puzzles apart", "퍼즐을 하나하나 떼어 내며"),
            ("Questions of science, science and progress", "과학의 질문들, 과학과 진보는"),
            ("Do not speak as loud as my heart", "내 마음만큼 크게 말하지 못해"),
            ("Tell me you love me", "나를 사랑한다고 말해 줘"),
            ("Come back and haunt me", "돌아와 나를 계속 맴돌아 줘"),
            ("Oh, and I rush to the start", "오, 나는 서둘러 처음으로 돌아가"),
            ("Running in circles", "빙빙 돌고 있어"),
            ("Chasing our tails", "우리의 꼬리를 쫓듯 같은 자리를 맴돌아"),
            ("Coming back as we are", "있는 그대로의 우리로 돌아오며"),
            ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
            ("Oh, it's such a shame for us to part", "오, 우리가 헤어진다는 건 정말 안타까운 일이야"),
            ("No one ever said it would be so hard", "아무도 이렇게 힘들 거라고 말하지 않았어"),
            ("I'm going back to the start", "나는 처음으로 돌아가고 있어"),
            ("Oh / Oh / Oh / Oh", "오 / 오 / 오 / 오"),
        ],
        "quiz": [
            ("화자가 상대에게 가장 먼저 말하고 싶은 것은 무엇인가요?", ["미안하다는 말", "축하한다는 말", "화났다는 말", "떠나자는 말"], "미안하다는 말"),
            ("'Let's go back to the start'의 의미는 무엇인가요?", ["처음으로 돌아가자", "학교로 가자", "과학을 공부하자", "집에 가자"], "처음으로 돌아가자"),
            ("'Nobody said it was easy'의 의미는 무엇인가요?", ["아무도 쉽다고 말하지 않았다", "모두 쉽다고 말했다", "과학은 쉽다", "사랑은 항상 쉽다"], "아무도 쉽다고 말하지 않았다"),
            ("'Do not speak as loud as my heart'는 어떤 뜻에 가깝나요?", ["이성과 과학보다 마음의 소리가 더 크다", "심장이 실제로 소리를 낸다", "과학이 가장 중요하다", "말을 하지 말라는 뜻이다"], "이성과 과학보다 마음의 소리가 더 크다"),
            ("이 노래의 중심 감정은 무엇인가요?", ["후회와 그리움", "분노와 복수", "승리와 환호", "웃음과 장난"], "후회와 그리움"),
        ],
        "key_expressions": [
            ("Tell you I'm sorry", "미안하다고 말하다"),
            ("How lovely you are", "네가 얼마나 사랑스러운지"),
            ("I had to find you", "나는 너를 찾아야 했어"),
            ("I need you", "네가 필요해"),
            ("I set you apart", "나는 너를 특별하게 여겨"),
            ("Tell me your secrets", "네 비밀을 말해 줘"),
            ("Let's go back to the start", "처음으로 돌아가자"),
            ("Running in circles", "빙빙 돌다"),
            ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
            ("Take me back to the start", "나를 처음으로 데려가 줘"),
        ],
        "matching": [
            ("Tell you I'm sorry", "미안하다고 말하다"),
            ("You don't know how lovely you are", "너는 네가 얼마나 사랑스러운지 몰라"),
            ("Tell you I need you", "네가 필요하다고 말하다"),
            ("Let's go back to the start", "처음으로 돌아가자"),
            ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
            ("I'm going back to the start", "나는 처음으로 돌아가고 있어"),
        ],
        "reflect_questions": [
            "당신도 가수처럼 그리운 옛 연인이나 다시 이야기하고 싶은 사람이 있나요?",
            "처음으로 돌아갈 수 있다면 다시 말하고 싶은 말은 무엇인가요?",
            "사랑이나 관계가 생각보다 쉽지 않았다고 느낀 경험이 있나요?",
        ],
    },
}


# =========================================================
# Session setup
# =========================================================

if "selected_song" not in st.session_state:
    st.session_state.selected_song = list(SONGS.keys())[0]

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"

def sync_song():
    for k in list(st.session_state.keys()):
        if k.startswith("quiz_") or k.startswith("keygame_") or k.startswith("match_") or k.startswith("reflect_"):
            del st.session_state[k]

st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)

song_options = list(SONGS.keys())
song_choice = st.selectbox(
    "👉 학습할 노래를 선택하세요",
    song_options,
    index=song_options.index(st.session_state.selected_song) if st.session_state.selected_song in song_options else 0,
    on_change=sync_song,
    key="song_selector"
)
st.session_state.selected_song = song_choice
data = SONGS[song_choice]

tabs_list = [
    "🎬 배경 학습",
    "📖 가사 & 퀴즈",
    "📝 Key Expression 뜻 맞추기",
    "🧩 문장 매칭 게임",
    "✍️ 생각 적기",
]

selected_tab = st.radio("학습 단계", tabs_list, horizontal=True, key="current_tab")


# =========================================================
# Tab 1: Background
# =========================================================

if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{data["bg"]}</div>', unsafe_allow_html=True)
    st.video(data["video_url"])
    st.info("노래를 듣기 전에 배경을 먼저 읽고, 화자의 감정과 상황을 생각해 보세요.")


# =========================================================
# Tab 2: Lyrics & Quiz
# =========================================================

elif selected_tab == "📖 가사 & 퀴즈":
    st.subheader("🎬 노래 영상")
    st.video(data["video_url"])
    st.markdown("---")

    st.subheader("📖 가사와 한국어 해석")
    for en, ko in data["lyrics"]:
        st.markdown(
            f"""
            <div class="lyrics-container">
                <div class="eng-line">{clean_text_for_display(en)}</div>
                <div class="kor-sub">{clean_text_for_display(ko)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("✅ 내용 이해 퀴즈")

    quiz_key = safe_key(song_choice)
    user_answers = []
    for i, (q, options, answer) in enumerate(data["quiz"], start=1):
        shuffled = shuffle_options(options, seed=f"{quiz_key}_quiz_{i}")
        picked = st.radio(
            f"{i}. {q}",
            shuffled,
            key=f"quiz_{quiz_key}_{i}",
            index=None
        )
        user_answers.append((q, picked, answer))

    col1, col2 = st.columns([1, 1])
    with col1:
        submit_quiz = st.button("정답 확인", key=f"quiz_submit_{quiz_key}", use_container_width=True)
    with col2:
        if st.button("다시 풀기", key=f"quiz_reset_{quiz_key}", use_container_width=True):
            for k in list(st.session_state.keys()):
                if k.startswith(f"quiz_{quiz_key}_"):
                    del st.session_state[k]
            st.rerun()

    if submit_quiz:
        score = sum(1 for _, picked, answer in user_answers if picked == answer)
        st.markdown(f'<div class="score-box">점수: {score} / {len(user_answers)}</div>', unsafe_allow_html=True)

        for idx, (q, picked, answer) in enumerate(user_answers, start=1):
            if picked == answer:
                st.success(f"{idx}번 정답입니다. ✅")
            else:
                st.markdown(
                    f"""
                    <div class="wrong-box">
                    <b>{idx}번</b> 다시 확인해 보세요.<br>
                    내가 고른 답: {clean_text_for_display(picked) if picked else "선택 안 함"}<br>
                    정답: <b>{clean_text_for_display(answer)}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# Tab 3: Key Expression Meaning Game
# =========================================================

elif selected_tab == "📝 Key Expression 뜻 맞추기":
    st.subheader("📝 Key Expression 뜻 맞추기")
    st.markdown(
        """
        <div class="game-card">
        <div class="big-guide">
        영어 핵심 표현을 보고 알맞은 한국어 뜻을 고르세요.<br>
        각 노래마다 중요한 표현 10개를 연습합니다.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    key_key = safe_key(song_choice)
    expressions = data["key_expressions"]
    all_korean_options = [ko for _, ko in expressions]

    user_answers = []
    for i, (en, ko) in enumerate(expressions, start=1):
        distractors = [x for x in all_korean_options if x != ko]
        rng = random.Random(f"{key_key}_{i}")
        wrongs = rng.sample(distractors, k=min(3, len(distractors)))
        options = wrongs + [ko]
        options = shuffle_options(options, seed=f"{key_key}_keygame_{i}")

        st.markdown(f"### {i}. {en}")
        picked = st.radio(
            "한국어 뜻을 고르세요.",
            options,
            key=f"keygame_{key_key}_{i}",
            index=None
        )
        user_answers.append((en, picked, ko))

    c1, c2 = st.columns(2)
    with c1:
        submit_key = st.button("Key Expression 정답 확인", key=f"keygame_submit_{key_key}", use_container_width=True)
    with c2:
        if st.button("Key Expression 다시 풀기", key=f"keygame_reset_{key_key}", use_container_width=True):
            for k in list(st.session_state.keys()):
                if k.startswith(f"keygame_{key_key}_"):
                    del st.session_state[k]
            st.rerun()

    if submit_key:
        score = sum(1 for _, picked, answer in user_answers if picked == answer)
        st.markdown(f'<div class="score-box">점수: {score} / {len(user_answers)}</div>', unsafe_allow_html=True)

        for idx, (en, picked, answer) in enumerate(user_answers, start=1):
            if picked == answer:
                st.success(f"{idx}번 정답 ✅  {en} = {answer}")
            else:
                st.error(f"{idx}번 오답 ❌  {en} = {answer}")


# =========================================================
# Tab 4: Sentence Matching Game
# =========================================================

elif selected_tab == "🧩 문장 매칭 게임":
    st.markdown(
        """
        <div class="matching-box">
            <div class="matching-title">🧩 문장 매칭 게임</div>
            <div class="big-guide">
            왼쪽 영어 표현과 오른쪽 한국어 뜻을 차례로 눌러 짝을 맞추세요.<br>
            기존 문장 매칭 게임은 그대로 마지막 탭에 유지했습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    match_key = safe_key(song_choice)
    pairs = [{"id": f"{match_key}_{i}", "en": en, "ko": ko} for i, (en, ko) in enumerate(data["matching"], start=1)]

    if f"match_done_{match_key}" not in st.session_state:
        st.session_state[f"match_done_{match_key}"] = []
    if f"match_selected_{match_key}" not in st.session_state:
        st.session_state[f"match_selected_{match_key}"] = None
    if f"match_message_{match_key}" not in st.session_state:
        st.session_state[f"match_message_{match_key}"] = ""

    done = st.session_state[f"match_done_{match_key}"]
    selected = st.session_state[f"match_selected_{match_key}"]

    en_cards = [{"id": p["id"], "text": p["en"], "kind": "en"} for p in pairs if p["id"] not in done]
    ko_cards = [{"id": p["id"], "text": p["ko"], "kind": "ko"} for p in pairs if p["id"] not in done]
    en_cards = shuffle_options(en_cards, seed=f"{match_key}_en")
    ko_cards = shuffle_options(ko_cards, seed=f"{match_key}_ko")

    if selected:
        st.markdown(
            f'<div class="selected-card-notice">선택됨: {clean_text_for_display(selected["text"])}</div>',
            unsafe_allow_html=True
        )

    msg = st.session_state[f"match_message_{match_key}"]
    if msg:
        st.info(msg)

    col_en, col_ko = st.columns(2)
    with col_en:
        st.markdown("### English")
        for card in en_cards:
            if st.button(card["text"], key=f"match_en_{match_key}_{card['id']}", use_container_width=True):
                if st.session_state[f"match_selected_{match_key}"] is None:
                    st.session_state[f"match_selected_{match_key}"] = card
                    st.session_state[f"match_message_{match_key}"] = "오른쪽에서 알맞은 한국어 뜻을 고르세요."
                else:
                    prev = st.session_state[f"match_selected_{match_key}"]
                    if prev["id"] == card["id"] and prev["kind"] != card["kind"]:
                        done.append(card["id"])
                        st.session_state[f"match_selected_{match_key}"] = None
                        st.session_state[f"match_message_{match_key}"] = "정답입니다! ✅"
                    else:
                        st.session_state[f"match_selected_{match_key}"] = card
                        st.session_state[f"match_message_{match_key}"] = "영어 표현을 다시 선택했습니다. 오른쪽 뜻을 고르세요."
                st.rerun()

    with col_ko:
        st.markdown("### Korean")
        for card in ko_cards:
            if st.button(card["text"], key=f"match_ko_{match_key}_{card['id']}", use_container_width=True):
                if st.session_state[f"match_selected_{match_key}"] is None:
                    st.session_state[f"match_selected_{match_key}"] = card
                    st.session_state[f"match_message_{match_key}"] = "왼쪽에서 알맞은 영어 표현을 고르세요."
                else:
                    prev = st.session_state[f"match_selected_{match_key}"]
                    if prev["id"] == card["id"] and prev["kind"] != card["kind"]:
                        done.append(card["id"])
                        st.session_state[f"match_selected_{match_key}"] = None
                        st.session_state[f"match_message_{match_key}"] = "정답입니다! ✅"
                    else:
                        st.session_state[f"match_selected_{match_key}"] = None
                        st.session_state[f"match_message_{match_key}"] = "아쉬워요. 다시 짝을 맞춰 보세요. ❌"
                st.rerun()

    st.progress(len(done) / len(pairs))
    st.write(f"맞춘 개수: {len(done)} / {len(pairs)}")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("매칭 게임 다시 시작", key=f"match_reset_{match_key}", use_container_width=True):
            st.session_state[f"match_done_{match_key}"] = []
            st.session_state[f"match_selected_{match_key}"] = None
            st.session_state[f"match_message_{match_key}"] = ""
            st.rerun()
    with c2:
        if len(done) == len(pairs):
            st.success("모든 문장을 맞췄습니다! 훌륭합니다. 🎉")


# =========================================================
# Tab 5: Reflective Writing
# =========================================================

elif selected_tab == "✍️ 생각 적기":
    st.subheader("✍️ 생각 적기: Reflective Writing")

    st.markdown(
        """
        <div class="game-card">
        <div class="big-guide">
        질문을 하나 고르고, 노래를 들으며 떠오른 생각을 자유롭게 적어 보세요.<br>
        답변을 제출하면 학생이 쓴 내용을 바탕으로 한국어 글을 조금 더 풍부하게 다듬고, 그 글을 자연스러운 영어로 번역해 줍니다.<br>
        맨 밑에는 글을 더 발전시키기 위한 쓰기 조언만 제시합니다.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    reflect_key = safe_key(song_choice)
    questions = data["reflect_questions"][:3]

    selected_question = st.radio(
        "질문을 선택하세요.",
        questions,
        key=f"reflect_question_{reflect_key}",
        index=0
    )

    answer = st.text_area(
        "내 생각을 적어 보세요.",
        placeholder="예: 이 노래를 들으며 예전에 좋아했던 사람이 떠올랐다. 그때는 내 마음을 잘 표현하지 못했고, 지금 생각하면 조금 아쉽다...",
        height=180,
        key=f"reflect_answer_{reflect_key}"
    )

    if st.button("피드백 받기", key=f"reflect_submit_{reflect_key}", use_container_width=True):
        if not answer.strip():
            st.warning("먼저 자신의 생각을 한두 문장이라도 적어 보세요.")
        else:
            ko_feedback, en_feedback, advice = make_polished_feedback(song_choice, selected_question, answer)

            st.markdown("### 🇰🇷 다듬은 한국어 글")
            st.markdown(
                f'<div class="feedback-ko">{clean_text_for_display(ko_feedback)}</div>',
                unsafe_allow_html=True
            )

            st.markdown("### 🇺🇸 English Translation")
            st.markdown(
                f'<div class="feedback-en">{clean_text_for_display(en_feedback)}</div>',
                unsafe_allow_html=True
            )

            st.markdown("### ✨ 쓰기 조언")
            st.markdown(
                f'<div class="advice-box">{clean_text_for_display(advice)}</div>',
                unsafe_allow_html=True
            )

