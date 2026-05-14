import streamlit as st
import random
import string

# =========================
# 1. 기본 설정 및 디자인
# =========================
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }

    .main-title {
        background-color: #f8fafc;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #6366f1;
        text-align: center;
        color: #4338ca;
        margin-bottom: 25px;
    }

    .info-box {
        background-color: #f1f5f9;
        padding: 24px;
        border-radius: 15px;
        border: 1px solid #cbd5e1;
        line-height: 1.8;
        margin-bottom: 25px;
    }

    .info-box h3 {
        color: #4338ca;
        border-bottom: 3px solid #6366f1;
        padding-bottom: 12px;
        margin-top: 0;
    }

    .lyrics-container {
        padding: 12px 20px;
        border-left: 5px solid #6366f1;
        margin-bottom: 10px;
        background-color: #f8fafc;
        border-radius: 0 10px 10px 0;
    }

    .eng-line {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e3a8a;
    }

    .kor-sub {
        font-size: 0.9rem;
        color: #64748b;
        margin-top: 4px;
    }

    .quiz-box {
        background-color: #f0f9ff;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #bae6fd;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #86efac;
        margin-top: 18px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# 2. 세션 상태 관리
# =========================
if "selected_song" not in st.session_state:
    st.session_state.selected_song = "1. Let It Go - Frozen OST"

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False


# =========================
# 3. 상단 제목 및 컨트롤
# =========================
st.markdown(
    '<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>',
    unsafe_allow_html=True
)

song_options = [
    "1. Let It Go - Frozen OST",
    "2. Hello - Adele",
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]

def sync_song():
    st.session_state.quiz_submitted = False

song_choice = st.selectbox(
    "👉 학습할 노래를 선택하세요",
    song_options,
    index=song_options.index(st.session_state.selected_song),
    on_change=sync_song,
    key="song_selector"
)

st.session_state.selected_song = song_choice

# 순서 배열 삭제함
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈"]

selected_tab = st.radio(
    "학습 단계",
    tabs_list,
    horizontal=True,
    key="current_tab"
)


# =========================
# 4. 곡별 데이터 설정
# =========================

if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"

    bg_content = """
    <h3>❄️ Let It Go: 억압된 여왕의 해방</h3>
    <p>
    <b>Let It Go</b>는 영화 <i>Frozen</i>의 대표곡으로,
    엘사가 더 이상 자신의 능력과 감정을 숨기지 않고 스스로를 받아들이는 장면에서 나오는 노래입니다.
    </p>
    """

    lyrics_full = [
        ("The snow glows white on the mountain tonight, not a footprint to be seen", "오늘 밤 산에는 눈이 하얗게 빛나고, 발자국 하나 보이지 않네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 휘몰아치는 폭풍처럼 바람이 울부짖고 있죠"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어요, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see, be the good girl you always have to be", "그들을 들이지 마, 보여주지 마, 언제나 그래야만 했던 착한 소녀가 되어라"),
        ("Conceal, don't feel, don't let them know, well now they know!", "숨기고, 느끼지 마, 알리지 마, 그런데 이제 그들이 알아버렸어!"),
    ]

    comprehension_questions = [
        {
            "q": "1. Who sings this song in the movie?",
            "options": ["Elsa", "Anna", "Olaf", "Kristoff"],
            "answer": "Elsa"
        },
        {
            "q": "2. What is the main feeling of the song?",
            "options": ["Freedom", "Hunger", "Fear of school", "Anger at friends"],
            "answer": "Freedom"
        },
        {
            "q": "3. What does Elsa stop doing?",
            "options": ["Hiding herself", "Eating food", "Going outside", "Talking to animals"],
            "answer": "Hiding herself"
        },
        {
            "q": "4. What is the setting of the song?",
            "options": ["A snowy mountain", "A beach", "A city street", "A classroom"],
            "answer": "A snowy mountain"
        },
        {
            "q": "5. What does 'conceal' mean?",
            "options": ["Hide", "Run", "Sing", "Smile"],
            "answer": "Hide"
        },
        {
            "q": "6. What does Elsa finally accept?",
            "options": ["Her power and identity", "Her homework", "Her bicycle", "Her new shoes"],
            "answer": "Her power and identity"
        },
    ]


elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"

    bg_content = """
    <h3>☎️ Hello: 과거의 누군가에게 건네는 안부</h3>
    <p>
    Adele의 <b>Hello</b>는 오랜 시간이 지난 뒤, 과거의 누군가에게 다시 연락하고 싶은 마음을 담은 노래입니다.
    화자는 미안함과 후회를 느끼며 상대에게 사과하고 싶어 합니다.
    </p>
    """

    lyrics_full = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years", "이 모든 세월이 흐른 뒤에 궁금했어"),
        ("You'd like to meet,", "네가 만나고 싶어 할지"),
        ("to go over everything", "모든 일을 다시 이야기해 보기 위해"),
        ("They say that time's", "사람들은 시간이"),
        ("supposed to heal ya", "너를 치유해 줄 거라고 말해"),
        ("But I ain't done much healing", "하지만 나는 별로 치유되지 않았어"),

        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming", "나는 캘리포니아에서 꿈꾸고 있어"),
        ("about who we used to be", "예전의 우리 모습에 대해"),
        ("When we were younger and free", "우리가 더 어리고 자유로웠을 때"),
        ("I've forgotten how it felt before", "나는 예전의 그 느낌을 잊어버렸어"),
        ("the world fell at our feet", "세상이 우리 발아래 있는 것 같았던 그때를"),
        ("There's such a difference between us", "우리 사이에는 너무 큰 차이가 있어"),
        ("And a million miles", "그리고 백만 마일만큼의 거리도 있어"),

        ("Hello from the other side", "저편에서 안녕이라고 말해"),
        ("I must've called a thousand times to tell you", "너에게 말하려고 천 번은 전화했을 거야"),
        ("I'm sorry, for everything that I've done", "내가 했던 모든 일에 대해 미안해"),
        ("But when I call you never seem to be home", "하지만 내가 전화할 때 너는 집에 없는 것 같아"),

        ("Hello from the outside", "바깥쪽에서 안녕이라고 말해"),
        ("At least I can say that I've tried to tell you", "적어도 너에게 말하려고 노력했다고는 말할 수 있어"),
        ("I'm sorry, for breaking your heart", "네 마음을 아프게 해서 미안해"),
        ("But it don't matter, it clearly doesn't tear you apart anymore", "하지만 이제는 상관없는 것 같아. 더 이상 너를 아프게 하지 않는 것 같아"),

        ("Hello, how are you?", "안녕, 어떻게 지내?"),
        ("It's so typical of me to talk about myself", "내 이야기만 하는 건 참 나답지"),
        ("I'm sorry, I hope that you're well", "미안해, 네가 잘 지내길 바라"),
        ("Did you ever make it out of that town", "너는 그 마을을 벗어났니?"),
        ("Where nothing ever happened?", "아무 일도 일어나지 않던 그곳에서?"),
        ("It's no secret that the both of us are running out of time", "우리 둘 다 시간이 얼마 남지 않았다는 건 비밀도 아니야"),

        ("Hello from the other side", "저편에서 안녕이라고 말해"),
        ("I must've called a thousand times to tell you", "너에게 말하려고 천 번은 전화했을 거야"),
        ("I'm sorry, for everything that I've done", "내가 했던 모든 일에 대해 미안해"),
        ("But when I call you never seem to be home", "하지만 내가 전화할 때 너는 집에 없는 것 같아"),

        ("Hello from the outside", "바깥쪽에서 안녕이라고 말해"),
        ("At least I can say that I've tried to tell you", "적어도 너에게 말하려고 노력했다고는 말할 수 있어"),
        ("I'm sorry, for breaking your heart", "네 마음을 아프게 해서 미안해"),
        ("But it don't matter, it clearly doesn't tear you apart anymore", "하지만 이제는 상관없는 것 같아. 더 이상 너를 아프게 하지 않는 것 같아"),

        ("Ooooohh, anymore", "오, 더 이상"),
        ("Ooooohh, anymore", "오, 더 이상"),
        ("Ooooohh, anymore", "오, 더 이상"),
        ("Anymore", "더 이상"),

        ("Hello from the other side", "저편에서 안녕이라고 말해"),
        ("I must've called a thousand times to tell you", "너에게 말하려고 천 번은 전화했을 거야"),
        ("I'm sorry, for everything that I've done", "내가 했던 모든 일에 대해 미안해"),
        ("But when I call you never seem to be home", "하지만 내가 전화할 때 너는 집에 없는 것 같아"),

        ("Hello from the outside", "바깥쪽에서 안녕이라고 말해"),
        ("At least I can say that I've tried to tell you", "적어도 너에게 말하려고 노력했다고는 말할 수 있어"),
        ("I'm sorry, for breaking your heart", "네 마음을 아프게 해서 미안해"),
        ("But it don't matter, it clearly doesn't tear you apart anymore", "하지만 이제는 상관없는 것 같아. 더 이상 너를 아프게 하지 않는 것 같아"),
    ]

    comprehension_questions = [
        {
            "q": "1. Who is the speaker trying to contact?",
            "options": ["A person from the past", "A new teacher", "A famous singer", "A stranger in California"],
            "answer": "A person from the past"
        },
        {
            "q": "2. What does the speaker mainly want to say?",
            "options": ["Thank you", "I'm sorry", "Good luck", "Happy birthday"],
            "answer": "I'm sorry"
        },
        {
            "q": "3. What do people say time is supposed to do?",
            "options": ["Heal people", "Make people rich", "Stop sadness forever", "Change the past"],
            "answer": "Heal people"
        },
        {
            "q": "4. Where is the speaker dreaming?",
            "options": ["London", "California", "New York", "Paris"],
            "answer": "California"
        },
        {
            "q": "5. What does the speaker say about calling?",
            "options": ["The speaker called many times", "The speaker never called", "The speaker called only once", "The speaker forgot the number"],
            "answer": "The speaker called many times"
        },
        {
            "q": "6. What is the main feeling of the song?",
            "options": ["Regret and apology", "Excitement and joy", "Anger and revenge", "Hope for a vacation"],
            "answer": "Regret and apology"
        },
    ]


elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"

    bg_content = """
    <h3>🕌 A Whole New World: 새로운 세상으로 떠나는 여행</h3>
    <p>
    <b>A Whole New World</b>는 영화 <i>Aladdin</i>의 대표곡으로,
    알라딘과 자스민이 마법 양탄자를 타고 새로운 세상을 바라보는 장면에서 나오는 노래입니다.
    </p>
    """

    lyrics_full = [
        ("I can show you the world", "내가 너에게 세상을 보여 줄 수 있어"),
        ("Shining, shimmering, splendid", "빛나고, 반짝이고, 눈부신 세상"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 원하는 대로 한 게 언제였나요?"),
        ("I can open your eyes", "내가 너의 눈을 뜨게 해 줄 수 있어"),
        ("Take you wonder by wonder", "놀라운 곳에서 또 다른 놀라운 곳으로 데려가며"),
        ("Over, sideways and under on a magic carpet ride", "마법 양탄자를 타고 위로, 옆으로, 아래로 날아가며"),
    ]

    comprehension_questions = [
        {
            "q": "1. What can the speaker show?",
            "options": ["The world", "A classroom", "A book", "A phone"],
            "answer": "The world"
        },
        {
            "q": "2. Who is the speaker talking to?",
            "options": ["A princess", "A teacher", "A king", "A student"],
            "answer": "A princess"
        },
        {
            "q": "3. What do they ride?",
            "options": ["A magic carpet", "A train", "A bicycle", "A boat"],
            "answer": "A magic carpet"
        },
        {
            "q": "4. What is the feeling of the song?",
            "options": ["Wonder and excitement", "Fear and anger", "Sadness and regret", "Boredom"],
            "answer": "Wonder and excitement"
        },
        {
            "q": "5. What does 'splendid' mean?",
            "options": ["Wonderful", "Small", "Dark", "Slow"],
            "answer": "Wonderful"
        },
        {
            "q": "6. What is the song mainly about?",
            "options": ["Discovering a new world", "Taking a test", "Buying food", "Cleaning a room"],
            "answer": "Discovering a new world"
        },
    ]


elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=hwZNL7QVJjE"

    bg_content = """
    <h3>🤝 Stand By Me: 곁에 있어 주는 힘</h3>
    <p>
    <b>Stand By Me</b>는 힘들고 어두운 순간에도 누군가가 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다.
    단순한 표현이 반복되어 학생들이 따라 부르기 좋습니다.
    </p>
    """

    lyrics_full = [
        ("When the night has come", "밤이 찾아오고"),
        ("And the land is dark", "세상이 어두워지고"),
        ("And the moon is the only light we'll see", "달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid", "아니, 나는 두려워하지 않을 거야"),
        ("Oh, I won't be afraid", "오, 나는 두려워하지 않을 거야"),
        ("Just as long as you stand, stand by me", "네가 내 곁에 있어 준다면"),
    ]

    comprehension_questions = [
        {
            "q": "1. When does the song begin?",
            "options": ["At night", "In the morning", "At school", "At lunch"],
            "answer": "At night"
        },
        {
            "q": "2. What is the only light they see?",
            "options": ["The moon", "The sun", "A phone", "A candle"],
            "answer": "The moon"
        },
        {
            "q": "3. What does the speaker say about fear?",
            "options": ["I won't be afraid", "I am always afraid", "I like fear", "I fear school"],
            "answer": "I won't be afraid"
        },
        {
            "q": "4. What does 'stand by me' mean?",
            "options": ["Stay with me", "Run away", "Sit down", "Go home"],
            "answer": "Stay with me"
        },
        {
            "q": "5. What is the main theme?",
            "options": ["Support and friendship", "Shopping", "Competition", "Cooking"],
            "answer": "Support and friendship"
        },
        {
            "q": "6. Why is the speaker not afraid?",
            "options": ["Because someone is with him", "Because he has money", "Because it is sunny", "Because he is sleeping"],
            "answer": "Because someone is with him"
        },
    ]


elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"

    bg_content = """
    <h3>🌙 Don't Know Why: 이유를 알 수 없는 마음</h3>
    <p>
    <b>Don't Know Why</b>는 조용하고 부드러운 분위기의 노래로,
    마음속 아쉬움과 설명하기 어려운 감정을 담고 있습니다.
    느린 속도의 노래라 듣기 활동에 활용하기 좋습니다.
    </p>
    """

    lyrics_full = [
        ("I waited 'til I saw the sun", "나는 해가 보일 때까지 기다렸어"),
        ("I don't know why I didn't come", "왜 내가 가지 않았는지 모르겠어"),
        ("I left you by the house of fun", "나는 너를 즐거움의 집 옆에 남겨 두었어"),
        ("I don't know why I didn't come", "왜 내가 가지 않았는지 모르겠어"),
        ("When I saw the break of day", "새벽이 밝아오는 것을 보았을 때"),
        ("I wished that I could fly away", "나는 날아가 버릴 수 있기를 바랐어"),
    ]

    comprehension_questions = [
        {
            "q": "1. What did the speaker wait for?",
            "options": ["The sun", "The bus", "A teacher", "A phone call"],
            "answer": "The sun"
        },
        {
            "q": "2. What does the speaker not know?",
            "options": ["Why she didn't come", "How to read", "Where school is", "What food to eat"],
            "answer": "Why she didn't come"
        },
        {
            "q": "3. What did the speaker wish?",
            "options": ["To fly away", "To sleep early", "To buy a car", "To study math"],
            "answer": "To fly away"
        },
        {
            "q": "4. What is the mood of the song?",
            "options": ["Quiet and regretful", "Angry and loud", "Fast and funny", "Excited and wild"],
            "answer": "Quiet and regretful"
        },
        {
            "q": "5. What does 'break of day' mean?",
            "options": ["Dawn", "Midnight", "Lunch time", "Winter"],
            "answer": "Dawn"
        },
        {
            "q": "6. What is repeated in the song?",
            "options": ["I don't know why I didn't come", "I love soccer", "Let it go", "Stand by me"],
            "answer": "I don't know why I didn't come"
        },
    ]


# =========================
# 5. 화면 출력
# =========================

if selected_tab == "🎬 배경 학습":
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown(bg_content, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🎬 Music Video")
    st.video(video_url)


elif selected_tab == "📖 가사 & 퀴즈":
    st.markdown("## 🎵 Full Lyrics")

    st.markdown(
        """
        <div class="quiz-box">
            <h3 style="margin-top:0;">📖 전체 가사를 먼저 읽어 봅시다</h3>
            <p style="font-size:16px; margin-bottom:0;">
            영어 가사와 한국어 뜻을 함께 보면서 노래의 내용을 이해해 봅시다.
            문제는 전체 가사를 다 읽은 뒤 아래에서 풀 수 있습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    for eng, kor in lyrics_full:
        st.markdown(
            f"""
            <div class="lyrics-container">
                <div class="eng-line">{eng}</div>
                <div class="kor-sub">{kor}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("## 📝 Understanding Check")

    st.markdown(
        """
        <div class="quiz-box">
            <b>전체 가사를 읽은 뒤 문제를 풀어 봅시다.</b><br>
            화자의 감정, 노래의 상황, 반복되는 표현을 중심으로 생각하면 됩니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    score = 0
    user_answers = []

    safe_song_key = (
        song_choice
        .replace(" ", "_")
        .replace(".", "")
        .replace("-", "_")
        .replace("'", "")
    )

    with st.form(f"comprehension_quiz_form_{safe_song_key}"):
        for i, item in enumerate(comprehension_questions):
            st.markdown(f"### {item['q']}")

            answer = st.radio(
                "Choose the best answer.",
                item["options"],
                key=f"comp_quiz_{safe_song_key}_{i}",
                label_visibility="collapsed"
            )

            user_answers.append(answer)

        submitted = st.form_submit_button("✅ Submit Answers")

    if submitted:
        st.markdown("## 📌 Results")

        for i, item in enumerate(comprehension_questions):
            correct = item["answer"]
            user_answer = user_answers[i]

            if user_answer == correct:
                score += 1
                st.success(f"{i+1}. Correct! ✅")
            else:
                st.error(f"{i+1}. Wrong ❌")
                st.markdown(f"정답: **{correct}**")

        st.markdown(
            f"""
            <div class="score-box">
                <h2 style="margin:0;">Your Score: {score} / {len(comprehension_questions)}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
