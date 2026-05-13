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
# Step 2 채점 상태 저장용
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
# 4. 곡별 데이터 (1절 가사 및 6개 퀴즈)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go: 억압된 여왕의 화려한 해방</h3><p>엘사가 자신의 능력을 인정하고 자유를 찾는 과정을 담고 있습니다.</p>"
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산에는 눈이 하얗게 빛나고"),
        ("Not a footprint to be seen", "발자국 하나 보이지 않네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 휘몰아치는 폭풍처럼 바람이 울부짖고 있죠"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어요, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"),
        ("Be the good girl you always have to be", "언제나 그래야만 했던 착한 소녀가 되어라"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 모르게 해"),
        ("Well, now they know!", "그렇지만, 이제 그들도 알아버렸어!"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더 이상 억누를 수 없어"),
        ("Let it go, let it go! Turn away and slam the door", "다 잊어, 다 잊어! 뒤돌아서 문을 쾅 닫아버려"),
        ("I don't care what they're going to say", "그들이 뭐라고 하든 상관없어"),
        ("Let the storm rage on, the cold never bothered me anyway", "폭풍아 계속 몰아쳐라, 어차피 추위는 날 괴롭히지 못하니까")
    ]
    questions = [
        ("1. 엘사가 현재 있는 장소의 특징은?", ["사람이 많다", "발자국조차 없는 고립된 곳", "꽃이 피어있다"], "발자국조차 없는 고립된 곳"),
        ("2. 'swirling storm inside'는 무엇을 비유하나요?", ["실제 눈보라", "엘사 내면의 혼란스러운 감정", "마법 도구"], "엘사 내면의 혼란스러운 감정"),
        ("3. 가문의 가르침이었던 'Conceal'의 의미는?", ["숨기다/감추다", "나누다", "노래하다"], "숨기다/감추다"),
        ("4. 'Let it go'의 문맥상 의미로 가장 적절한 것은?", ["물건을 던지다", "억눌렀던 것을 놓아주다", "도망치다"], "억눌렀던 것을 놓아주다"),
        ("5. 'Slam the door'는 어떤 태도를 보여주나요?", ["다시 돌아가고 싶은 마음", "과거와의 단호한 단절", "실수"], "과거와의 단호한 단절"),
        ("6. 'The cold never bothered me anyway'의 속뜻은?", ["추워서 떨고 있다", "타인의 시선에 상처받지 않음", "여름을 기다림"], "타인의 시선에 상처받지 않음")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello: 과거의 나에게 건네는 안부</h3><p>과거의 연인 혹은 과거의 자신에게 건네는 사과와 그리움을 담은 곡입니다.</p>"
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 세월이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything", "모든 것을 하나하나 짚어보면서 말이야"),
        ("They say that time's supposed to heal ya, but I ain't done much healing", "시간이 해결해 준다고들 하지만, 난 별로 치유되지 않은 것 같아"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("When we were younger and free", "우리가 더 젊고 자유로웠을 때를"),
        ("I've forgotten how it felt before the world fell at our feet", "세상이 우리 발아래 있기 전의 기분이 어땠인지 잊어버렸어"),
        ("There's such a difference between us", "우리 사이엔 큰 차이가 생겼고"),
        ("And a million miles", "수백만 마일의 거리감이 느껴져")
    ]
    questions = [
        ("1. 화자가 상대방을 만나서 하고 싶은 것은?", ["돈 갚기", "모든 일을 함께 짚어보기", "연애 상담"], "모든 일을 함께 짚어보기"),
        ("2. 'Time's supposed to heal ya'에 대한 화자의 생각은?", ["동의한다", "난 별로 치유되지 않았다", "시간은 중요하지 않다"], "난 별로 치유되지 않았다"),
        ("3. 'California dreaming'은 무엇을 그리워하나?", ["미국 여행", "젊고 자유로웠던 과거의 우리", "현재의 성공"], "젊고 자유로웠던 과거의 우리"),
        ("4. 'The world fell at our feet'의 의미는?", ["세상이 망했다", "모든 성공이 우리 앞에 있었다", "지진이 났다"], "모든 성공이 우리 앞에 있었다"),
        ("5. 현재 두 사람 사이의 거리감을 나타낸 단어는?", ["A million miles", "A small gap", "Next door"], "A million miles"),
        ("6. 이 노래의 지배적인 정서는 무엇인가요?", ["기쁨", "증오", "그리움과 후회"], "그리움과 후회")
    ]
# (3, 4, 5번 곡 데이터 생략 - 위 구조와 동일하게 유지됨)

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
        st.markdown("### 💡 Comprehension Quiz")
        
        # 폼 내부에서 사용자 선택값 받기
        with st.form(key=f"quiz_form_{song_choice}"):
            user_answers = []
            for i, (q, opts, ans) in enumerate(questions):
                user_choice = st.radio(q, opts, index=None, key=f"q_radio_{song_choice}_{i}")
                user_answers.append(user_choice)
            
            submit_btn = st.form_submit_button("채점하기")
            if submit_btn:
                st.session_state.quiz_submitted = True

        # 채점 결과 출력 (폼 외부 또는 하단)
        if st.session_state.quiz_submitted:
            st.markdown("---")
            score = 0
            for i, (q, opts, ans) in enumerate(questions):
                user_ans = user_answers[i]
                if user_ans == ans:
                    st.success(f"**Q{i+1} 정답!** (선택: {user_ans})")
                    score += 1
                else:
                    st.error(f"**Q{i+1} 오답** (선택: {user_ans if user_ans else '미선택'} / 정답: {ans})")
            
            st.info(f"총 {len(questions)}문제 중 {score}문제를 맞히셨습니다!")
            if score == len(questions): st.balloons()

    with col_l:
        st.markdown("### 🎼 Full Lyrics (1절)")
        for i, (eng, kor) in enumerate(lyrics_raw):
            label = list(string.ascii_lowercase)[i] if i < 26 else str(i)
            st.markdown(f'''
                <div class="lyrics-container">
                    <div class="eng-line">({label}) {eng}</div>
                    <div class="kor-sub">{kor}</div>
                </div>
            ''', unsafe_allow_html=True)

elif selected_tab == "🧩 순서 배열":
    # 가사 가공 (알파벳 기호 붙이기)
    full_lyrics_labeled = []
    for i, (eng, kor) in enumerate(lyrics_raw):
        label = list(string.ascii_lowercase)[i] if i < 26 else str(i)
        full_lyrics_labeled.append(f"({label}) {eng}")
    
    correct_order = full_lyrics_labeled
    
    if 'scrambled' not in st.session_state or st.session_state.get('last_song_id') != song_choice:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))
        st.session_state.last_song_id = song_choice

    st.subheader("🧩 가사 순서대로 클릭하세요")
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[i % 2]).button(text, key=f"puz_{song_choice}_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()

    st.divider()
    st.write("📝 **나의 배열:**")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del_{song_choice}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 채점", type="primary", use_container_width=True):
            all_correct = True
            for i, user_s in enumerate(st.session_state.q3_cards):
                if user_s == correct_order[i]: st.success(f"{i+1}번: Correct!")
                else:
                    st.error(f"{i+1}번: Wrong (정답: {correct_order[i]})")
                    all_correct = False
            if all_correct: st.balloons()
