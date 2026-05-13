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
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go: 억압된 여왕의 화려한 해방</h3>"
    lyrics_full = [
        ("The snow glows white on the mountain tonight, not a footprint to be seen", "오늘 밤 산에는 눈이 하얗게 빛나고, 발자국 하나 보이지 않네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 휘몰아치는 폭풍처럼 바람이 울부짖고 있죠"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어요, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see, be the good girl you always have to be", "그들을 들이지 마, 보여주지 마, 언제나 그래야만 했던 착한 소녀가 되어라"),
        ("Conceal, don't feel, don't let them know, well now they know!", "숨기고, 느끼지 마, 알리지 마, 그런데 이제 그들이 알아버렸어!")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello: 과거의 나에게 건네는 안부</h3>"
    lyrics_full = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 세월이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything, they say that time's supposed to heal ya", "모든 걸 짚어보기 위해, 시간이 치유해 줄 거라 다들 말하지만"),
        ("But I ain't done much healing", "난 별로 치유되지 않은 것 같아"),
        ("Hello, can you hear me? I'm in California dreaming", "여보세요, 들리니? 난 캘리포니아에서 꿈을 꾸고 있어"),
        ("About who we used to be when we were younger and free", "우리가 더 어리고 자유로웠던 시절의 모습에 대해")
    ]

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
