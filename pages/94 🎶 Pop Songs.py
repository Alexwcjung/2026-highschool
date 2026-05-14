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
        background-color: #f8fafc; padding: 25px; border-radius: 15px;
        border: 2px solid #6366f1; text-align: center; color: #4338ca; margin-bottom: 25px;
    }
    .info-box {
        background-color: #f1f5f9; padding: 30px; border-radius: 15px;
        border: 1px solid #cbd5e1; line-height: 1.8; margin-bottom: 25px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 3px solid #6366f1; padding-bottom: 12px; margin-top: 0; }
    .lyrics-container {
        padding: 12px 20px; border-left: 5px solid #6366f1;
        margin-bottom: 10px; background-color: #f8fafc; border-radius: 0 10px 10px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. 세션 상태 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'quiz_submitted' not in st.session_state: st.session_state.quiz_submitted = False

# -------------------------
# 3. 상단 컨트롤
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]

def sync_song():
    st.session_state.q3_cards = []
    st.session_state.quiz_submitted = False
    if 'scrambled' in st.session_state: del st.session_state.scrambled

song_choice = st.selectbox("👉 학습할 노래를 선택하세요", song_options, 
                           index=song_options.index(st.session_state.selected_song),
                           on_change=sync_song, key="song_selector")
st.session_state.selected_song = song_choice

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("학습 단계", tabs_list, horizontal=True, key="current_tab")

# -------------------------
# 4. 곡별 데이터 (1절 처음부터 순서대로 6문장 구성)
# -------------------------
# =========================
# 노래 선택에 따른 데이터 설정
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
            "options": [
                "A person from the past",
                "A new teacher",
                "A famous singer",
                "A stranger in California"
            ],
            "answer": "A person from the past"
        },
        {
            "q": "2. What does the speaker mainly want to say?",
            "options": [
                "Thank you",
                "I'm sorry",
                "Good luck",
                "Happy birthday"
            ],
            "answer": "I'm sorry"
        },
        {
            "q": "3. What do people say time is supposed to do?",
            "options": [
                "Heal people",
                "Make people rich",
                "Stop sadness forever",
                "Change the past"
            ],
            "answer": "Heal people"
        },
        {
            "q": "4. Where is the speaker dreaming?",
            "options": [
                "London",
                "California",
                "New York",
                "Paris"
            ],
            "answer": "California"
        },
        {
            "q": "5. What does the speaker say about calling?",
            "options": [
                "The speaker called many times",
                "The speaker never called",
                "The speaker called only once",
                "The speaker forgot the number"
            ],
            "answer": "The speaker called many times"
        },
        {
            "q": "6. What is the main feeling of the song?",
            "options": [
                "Regret and apology",
                "Excitement and joy",
                "Anger and revenge",
                "Hope for a vacation"
            ],
            "answer": "Regret and apology"
        },
    ]


# =========================
# 탭 구성
# 순서 배열 탭 삭제
# =========================

tab1, tab2 = st.tabs([
    "🎬 1. Background & Video",
    "🎵 2. Full Lyrics & Quiz"
])


# =========================
# 1번째 탭: 노래 소개 + 영상
# =========================

with tab1:
    st.markdown(bg_content, unsafe_allow_html=True)

    st.markdown("### 🎬 Music Video")
    st.video(video_url)


# =========================
# 2번째 탭: 전체 가사 + 이해도 문제
# =========================

with tab2:
    st.markdown("## 🎵 Full Lyrics")

    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #fff7ed, #fef3c7);
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #fed7aa;
            margin-bottom: 18px;
        ">
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
            <div style="
                background:white;
                padding:12px 14px;
                border-radius:14px;
                margin-bottom:8px;
                border:1px solid #e5e7eb;
                box-shadow:0 2px 6px rgba(0,0,0,0.04);
            ">
                <div style="font-size:17px; font-weight:700; color:#111827;">
                    {eng}
                </div>
                <div style="font-size:15px; color:#4b5563; margin-top:4px;">
                    {kor}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown("## 📝 Understanding Check")

    st.markdown(
        """
        <div style="
            background:#f0f9ff;
            padding:15px;
            border-radius:15px;
            border:1px solid #bae6fd;
            margin-bottom:16px;
        ">
            <b>전체 가사를 읽은 뒤 문제를 풀어 봅시다.</b><br>
            화자의 감정, 노래의 상황, 반복되는 표현을 중심으로 생각하면 됩니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    score = 0
    user_answers = []

    with st.form("comprehension_quiz_form"):
        for i, item in enumerate(comprehension_questions):
            st.markdown(f"### {item['q']}")

            answer = st.radio(
                "Choose the best answer.",
                item["options"],
                key=f"comp_quiz_{song_choice}_{i}",
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
            <div style="
                background:linear-gradient(135deg,#dcfce7,#bbf7d0);
                padding:18px;
                border-radius:18px;
                border:1px solid #86efac;
                margin-top:18px;
                text-align:center;
            ">
                <h2 style="margin:0;">Your Score: {score} / {len(comprehension_questions)}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

            
elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = "<h3>✨ A Whole New World: 성벽을 넘는 자유의 비행</h3>"
    lyrics_full = [
        ("I can show you the world, shining, shimmering, splendid", "당신에게 세상을 보여줄 수 있어요, 빛나고 반짝이며 화려한 세상을"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes, take you wonder by wonder", "당신의 눈을 뜨게 해 줄게요, 경이로운 곳들로 데려가 줄게요"),
        ("Over, sideways and under on a magic carpet ride", "마법 양탄자를 타고 위아래 옆으로 누비며"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠"),
        ("No one to tell us 'No', or where to go, or say we're only dreaming", "아무도 우리에게 안 된다거나 어디로 가라고, 혹은 꿈일 뿐이라고 말하지 않아요")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h3>🤝 Stand By Me: 시련 속에서도 변치 않는 연대</h3>"
    lyrics_full = [
        ("When the night has come and the land is dark", "밤이 찾아오고 대지가 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid, oh, I won't be afraid", "난 두렵지 않을 거예요, 정말 두렵지 않아요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("So darling, darling, stand by me, oh, stand by me", "그러니 그대여, 내 곁에 서 주세요, 내 곁에 있어 줘요"),
        ("If the sky that we look upon should tumble and fall", "우리가 바라보는 저 하늘이 무너져 내린다고 해도")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = "<h3>🍂 Don't Know Why: 망설임이 남긴 쓸쓸한 후회</h3>"
    lyrics_full = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("I don't know why I didn't come, I don't know why I didn't come", "왜 가지 않았는지 모르겠어요, 정말 모르겠어요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 밝아올 때 난 멀리 날아가 버리고 싶었죠"),
        ("Instead of kneeling in the sand, catching teardrops in my hand", "모래 위에 무릎 꿇고 손바닥으로 눈물을 받는 대신에요")
    ]

# 퀴즈는 공통 문항 유지 (내용이 1절에 포함됨)
questions = [
    ("1. 가사 내용상 화자의 현재 감정은?", ["기쁨", "슬픔/고민", "분노"], "슬픔/고민"),
    ("2. 가사 첫 부분의 시간적 배경은?", ["아침", "밤/새벽", "낮"], "밤/새벽")
]

# -------------------------
# 5. 탭별 화면 출력
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
    col_v, col_l = st.columns([1, 1.2])
    with col_v:
        st.video(video_url)
        st.divider()
        st.markdown("### 💡 Quick Check")
        with st.form(key=f"quiz_form_{song_choice}"):
            user_answers = []
            for i, (q, opts, ans) in enumerate(questions):
                user_choice = st.radio(q, opts, index=None, key=f"q_radio_{song_choice}_{i}")
                user_answers.append(user_choice)
            if st.form_submit_button("채점하기"):
                st.session_state.quiz_submitted = True
        if st.session_state.quiz_submitted:
            st.info("정답을 확인하고 다음 단계로 넘어가세요!")
    with col_l:
        st.markdown("### 🎼 First Verse (처음~6문장)")
        for i, (eng, kor) in enumerate(lyrics_full):
            label = list(string.ascii_lowercase)[i]
            st.markdown(f'''
                <div class="lyrics-container">
                    <div class="eng-line">({label}) {eng}</div>
                    <div class="kor-sub">{kor}</div>
                </div>
            ''', unsafe_allow_html=True)

elif selected_tab == "🧩 순서 배열":
    # 1절 처음부터 순서대로 6개 라벨링
    correct_order = [f"({list(string.ascii_lowercase)[i]}) {eng}" for i, (eng, kor) in enumerate(lyrics_full)]
    
    if 'scrambled' not in st.session_state or st.session_state.get('last_song_id') != song_choice:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))
        st.session_state.last_song_id = song_choice

    st.subheader("🧩 가사 순서대로 클릭하세요 (1절 도입부부터)")
    st.caption("가사 앞의 (a) (b) (c)... 기호를 참고하여 노래가 흐르는 순서대로 버튼을 누르세요.")
    
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[i % 2]).button(text, key=f"puz_{song_choice}_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()

    st.divider()
    st.write("📝 **내가 배열한 순서:**")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del_{song_choice}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == 6:
        if st.button("🚩 최종 채점 하기", type="primary", use_container_width=True):
            all_correct = True
            for i, user_s in enumerate(st.session_state.q3_cards):
                if user_s == correct_order[i]: st.success(f"{i+1}번: 정답!")
                else:
                    st.error(f"{i+1}번: 오답 (정답: {correct_order[i]})")
                    all_correct = False
            if all_correct: st.balloons()
