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
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False

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
    st.session_state.submitted_step2 = False
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
    bg_content = """
    <h3>❄️ Let It Go: 억압된 여왕의 화려한 해방</h3>
    <p><b>[줄거리]</b> 아렌델 왕국의 엘사는 모든 것을 얼리는 능력을 숨기며 고립된 삶을 살았습니다. 대관식 날 정체가 탄로나 설산으로 도망친 그녀는, 비로소 누구의 시선도 신경 쓰지 않고 자신의 힘을 펼치며 얼음 성을 짓습니다.</p>
    <p><b>[서사]</b> 평생을 괴롭혔던 "착한 아이가 되어라"라는 강박을 버리고, "다 잊어(Let it go)"라고 외치며 진정한 자아를 찾는 과정을 담고 있습니다.</p>
    """
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
        ("4. 'Let it go'의 문맥상 의미로 가장 적절한 것은?", ["물건을 던지다", "억눌렀던 것을 놓아주다/자유로워지다", "도망치다"], "억눌렀던 것을 놓아주다/자유로워지다"),
        ("5. 'Slam the door'는 어떤 태도를 보여주나요?", ["다시 돌아가고 싶은 마음", "과거와의 단호한 단절", "실수"], "과거와의 단호한 단절"),
        ("6. 'The cold never bothered me anyway'에서 알 수 있는 엘사의 상태는?", ["추워서 떨고 있다", "타인의 차가운 시선에 더 이상 상처받지 않음", "여름을 기다림"], "타인의 차가운 시선에 더 이상 상처받지 않음")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 모든 나에게 건네는 안부</h3>
    <p><b>[줄거리]</b> 오랜 시간이 흐른 뒤 과거의 연인에게 전화를 거는 화자의 목소리로 시작됩니다. 수천 번 전화를 걸었지만 응답 없는 상대방을 보며, 화자는 과거의 미안함과 현재의 공허함을 노래합니다.</p>
    <p><b>[서사]</b> 아델은 이 곡이 '어른이 된 나'가 '어렸던 시절의 나'에게 보내는 작별 인사라고 설명했습니다. 돌이킬 수 없는 시간의 벽을 'The other side'로 비유했습니다.</p>
    """
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 세월이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything", "모든 것을 하나하나 짚어보면서 말이야"),
        ("They say that time's supposed to heal ya, but I ain't done much healing", "시간이 해결해 준다고들 하지만, 난 별로 치유되지 않은 것 같아"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("When we were younger and free", "우리가 더 젊고 자유로웠을 때를"),
        ("I've forgotten how it felt before the world fell at our feet", "세상이 우리 발아래 있기 전의 기분이 어땠는지 잊어버렸어"),
        ("There's such a difference between us", "우리 사이엔 큰 차이가 생겼고"),
        ("And a million miles", "수백만 마일의 거리감이 느껴져")
    ]
    questions = [
        ("1. 화자가 상대방을 만나서 하고 싶은 것은?", ["돈을 갚기", "모든 일을 함께 짚어보기", "새로운 연애 상담"], "모든 일을 함께 짚어보기"),
        ("2. 'Time's supposed to heal ya'에 대한 화자의 생각은?", ["동의한다", "시간이 흘러도 치유되지 않았다", "시간은 중요하지 않다"], "시간이 흘러도 치유되지 않았다"),
        ("3. 'California dreaming'은 무엇을 그리워하는 표현인가요?", ["미국 여행", "젊고 자유로웠던 과거의 우리", "현재의 성공"], "젊고 자유로웠던 과거의 우리"),
        ("4. 'The world fell at our feet'의 의미는?", ["세상이 망했다", "모든 성공과 기회가 우리 앞에 있었다", "지진이 났다"], "모든 성공과 기회가 우리 앞에 있었다"),
        ("5. 현재 두 사람 사이의 거리를 비유한 표현은?", ["A million miles", "A small gap", "Next door"], "A million miles"),
        ("6. 이 노래의 지배적인 정서는 무엇인가요?", ["기쁨과 희열", "분노와 증오", "그리움과 후회"], "그리움과 후회")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 성벽을 넘는 자유의 비행</h3>
    <p><b>[줄거리]</b> 왕궁에 갇혀 지내던 자스민 공주가 알라딘과 함께 마법 양탄자를 타고 밤하늘을 날며 생전 처음 보는 바깥세상을 구경하는 장면입니다.</p>
    <p><b>[서사]</b> 단순히 경치를 보는 것이 아니라, 타인이 정해준 삶이 아닌 스스로 결정하는 '자유로운 시야(Point of view)'를 갖게 되는 성장을 의미합니다.</p>
    """
    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 반짝이며 화려한 세상을"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"),
        ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"),
        ("Over, sideways and under on a magic carpet ride", "마법 양탄자를 타고 위아래 옆으로 누비며"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠"),
        ("No one to tell us 'No', or where to go", "아무도 우리에게 안 된다거나, 어디로 가라고 말하지 않아요"),
        ("Or say we're only dreaming", "그저 꿈일 뿐이라고 말하지도 않죠")
    ]
    questions = [
        ("1. 알라딘이 자스민 공주에게 묻는 '결정'의 주체는?", ["왕(아버지)", "자신의 마음(Your heart)", "지니"], "자신의 마음(Your heart)"),
        ("2. 'Shimmering'의 뜻으로 적절한 것은?", ["깜깜한", "희미하게 빛나는", "시끄러운"], "희미하게 빛나는"),
        ("3. 마법 양탄자를 타고 가는 모습을 묘사한 가사는?", ["Fast and slow", "Over, sideways and under", "Walk and run"], "Over, sideways and under"),
        ("4. 'A whole new world'가 상징하는 것은?", ["이민", "자유롭고 새로운 삶의 가능성", "가짜 세상"], "자유롭고 새로운 삶의 가능성"),
        ("5. 'Point of view'의 의미는?", ["장소", "시야/관점", "목소리"], "시야/관점"),
        ("6. 이 곳에서는 아무도 'No'라고 말하지 않는다는 것은 무엇을 뜻하나요?", ["억압과 통제가 없는 자유", "대화 금지", "거짓말"], "억압과 통제가 없는 자유")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 시련 속에서도 변치 않는 연대</h3>
    <p><b>[줄거리]</b> 험난한 세상을 살아가는 네 소년의 우정을 다룬 영화의 테마곡입니다. 어떤 어둠과 공포가 닥쳐도 곁에 누군가 있다면 이겨낼 수 있다는 믿음을 노래합니다.</p>
    <p><b>[서사]</b> 하늘이 무너지는 천재지변 같은 시련이 와도 '내 곁에 서 있어 달라(Stand by me)'는 간절한 부탁과 신뢰를 담고 있습니다.</p>
    """
    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 오고 대지가 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid, no, I won't be afraid", "난 두렵지 않을 거예요, 정말 두렵지 않아요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("So darling, darling, stand by me", "그러니 그대여, 내 곁에 서 주세요"),
        ("Oh, stand by me", "내 곁에 있어 줘요"),
        ("If the sky that we look upon should tumble and fall", "우리가 바라보는 저 하늘이 무너져 내리고"),
        ("Or the mountains should crumble to the sea", "저 산들이 부서져 바다로 흘러내린다 해도"),
        ("I won't cry, I won't cry, no, I won't shed a tear", "난 울지 않을 거예요, 눈물 한 방울 흘리지 않겠어요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요")
    ]
    questions = [
        ("1. 'The land is dark'는 무엇을 상징하나요?", ["잠잘 시간", "인생의 시련이나 절망", "정전"], "인생의 시련이나 절망"),
        ("2. 화자가 두려워하지 않는 유일한 조건은?", ["돈이 많은 것", "상대방이 곁에 있어 주는 것", "날씨가 좋은 것"], "상대방이 곁에 있어 주는 것"),
        ("3. 'Stand by me'의 올바른 의미는?", ["옆에 서서 구경하다", "어려울 때 지지하고 함께해주다", "일어서다"], "어려울 때 지지하고 함께해주다"),
        ("4. 'Tumble and fall'과 'Crumble'이 묘사하는 상황은?", ["거대한 재앙/무너짐", "축제", "자연 보호"], "거대한 재앙/무너짐"),
        ("5. 'Shed a tear'의 의미는?", ["눈물을 흘리다", "미소를 짓다", "노래하다"], "눈물을 흘리다"),
        ("6. 이 노래가 강조하는 가치는 무엇인가요?", ["신뢰와 연대", "개인주의", "자연의 위대함"], "신뢰와 연대")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임이 남긴 쓸쓸한 공허</h3>
    <p><b>[줄거리]</b> 사랑하는 사람에게 가야 했지만, 알 수 없는 망설임 때문에 가지 못한 뒤 찾아오는 후회를 담았습니다. 새벽 해가 뜨는 것을 보며 홀로 느끼는 고독을 노래합니다.</p>
    <p><b>[서사]</b> "왜 안 갔을까(I don't know why I didn't come)"라는 반복적인 물음을 통해 인간의 서툰 감정과 결정에 대한 아쉬움을 표현합니다.</p>
    """
    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("I don't know why I didn't come", "왜 가지 않았는지 정말 모르겠어요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 밝아올 때 난 멀리 날아가 버리고 싶었죠"),
        ("Instead of kneeling in the sand, catching teardrops in my hand", "모래 위에 무릎 꿇고 손바닥으로 눈물을 받는 대신에요"),
        ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"),
        ("Out across the endless sea, I would die in ecstasy", "끝없는 바다 건너에서 난 황홀하게 죽을 수도 있었겠죠"),
        ("But I'll be a bag of bones, waiting on the street alone", "하지만 난 그저 길거리에서 홀로 기다리는 앙상한 뼈가 되겠죠")
    ]
    questions = [
        ("1. 화자는 언제까지 기다렸나요?", ["밤새도록(해 뜰 때까지)", "한 시간", "잠시 동안"], "밤새도록(해 뜰 때까지)"),
        ("2. 'I don't know why I didn't come'에서 느껴지는 감정은?", ["자신감", "이유를 알 수 없는 후회", "기쁨"], "이유를 알 수 없는 후회"),
        ("3. 'Fly away'는 무엇을 하고 싶은 마음인가요?", ["여행", "현재의 고통스러운 상황에서 도피", "공연"], "현재의 고통스러운 상황에서 도피"),
        ("4. 'Drenched in wine'은 마음이 어떤 상태임을 비유하나요?", ["술에 취해 기분 좋음", "슬픔에 푹 잠겨 있음", "목이 마름"], "슬픔에 푹 잠겨 있음"),
        ("5. 'A bag of bones'가 묘사하는 화자의 모습은?", ["매우 건강한 모습", "기운 없이 야위고 초라한 모습", "무거운 짐을 든 모습"], "기운 없이 야위고 초라한 모습"),
        ("6. 화자는 누구를 영원히 생각할 것이라고 하나요?", ["가족", "가지 못해 놓쳐버린 당신", "나 자신"], "가지 못해 놓쳐버린 당신")
    ]

# -------------------------
# 가사 가공 및 배열 문제 생성
# -------------------------
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = list(string.ascii_lowercase)[i] if i < 26 else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in full_lyrics]

if 'scrambled' not in st.session_state or st.session_state.get('last_song_id') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song_id = song_choice

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
        with st.form(key=f"quiz_form_{song_choice}"):
            for i, (q, opts, ans) in enumerate(questions):
                st.radio(q, opts, index=None, key=f"q_key_{song_choice}_{i}")
            if st.form_submit_button("채점하기"):
                st.session_state.submitted_step2 = True
        
        if st.session_state.submitted_step2:
            st.info("정답을 확인하며 가사의 의미를 다시 되새겨 보세요!")

    with col_l:
        st.markdown("### 🎼 Full Lyrics (1절)")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

elif selected_tab == "🧩 순서 배열":
    st.subheader("🧩 가사 순서대로 클릭하세요 (a, b, c...)")
    
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[i % 2]).button(text, key=f"puz_{song_choice}_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()

    st.divider()
    st.write("📝 **현재 나의 배열:**")
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
