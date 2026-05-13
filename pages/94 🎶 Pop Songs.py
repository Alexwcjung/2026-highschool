import streamlit as st
import random
import string

# =========================
# 1. 기본 설정 및 디자인 (레이아웃 유지)
# =========================
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title {
        background-color: #f8fafc; padding: 25px; border-radius: 15px;
        border: 2px solid #6366f1; text-align: center; color: #4338ca; margin-bottom: 25px;
    }
    .big-label {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #1e3a8a !important;
        margin-bottom: 15px !important;
        display: block;
    }
    .info-box {
        background-color: #f1f5f9; padding: 30px; border-radius: 15px;
        border: 1px solid #cbd5e1; line-height: 1.9; margin-bottom: 25px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 3px solid #6366f1; padding-bottom: 12px; margin-top: 0; }
    .info-box b { color: #1e3a8a; }
    .lyrics-container {
        padding: 12px 20px; border-left: 5px solid #6366f1;
        margin-bottom: 10px; background-color: #f8fafc; border-radius: 0 10px 10px 0;
    }
    .eng-line { font-size: 1.15rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.95rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    st.session_state.current_tab = "🎬 배경 학습"
    if 'scrambled' in st.session_state: del st.session_state.scrambled

# -------------------------
# 상단 곡 선택 메뉴
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]
song_choice = st.selectbox("", song_options, label_visibility="collapsed")

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# 탭 선택
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

# -------------------------
# 곡별 데이터 설정 (풍부한 배경지식 + 6문제 퀴즈)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 억압된 자아의 화려한 해방</h3>
    <p>디즈니 <b>'겨울왕국'</b>의 주인공 엘사가 자신의 마법 능력이 세상에 드러난 후, '착한 소녀'라는 사회적 굴레를 벗어던지며 부르는 곡입니다. 평생 "감추고(Conceal), 느끼지 마라(Don't feel)"는 교육을 받으며 능력을 억압해온 그녀가 비로소 <b>심리적 해방감</b>을 느끼는 과정을 보여줍니다.</p>
    <p><b>[서사 포인트]</b> 가사 속 "The cold never bothered me anyway"는 물리적 추위뿐만 아니라, 나를 향한 세상의 차가운 시선조차 더 이상 나를 흔들 수 없다는 <b>강력한 자존감</b>을 의미합니다.</p>
    """
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나고"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"),
        ("Conceal, don't feel, don't let them know. Well, now they know!", "숨기고, 느끼지 말고, 모르게 해. 그런데 이제 그들이 알아버렸어!"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어"),
        ("I don't care what they're going to say. Let the storm rage on", "그들이 뭐라 하든 상관없어. 폭풍아 계속 휘몰아쳐라")
    ]
    questions = [
        ("1. 엘사의 현재 주요 심경은?", ["해방감", "공포", "분노"], "해방감"),
        ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"),
        ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 날씨", "겨울 휴가"], "사회적 시선"),
        ("4. 'Good girl'은 무엇의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회"),
        ("5. 'Isolation'의 정확한 뜻은?", ["고립/격리", "함께함", "승리"], "고립/격리"),
        ("6. 'Storm inside'는 무엇의 비유인가요?", ["억눌린 감정", "마법 능력", "기상 이변"], "억눌린 감정")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거와 현재를 잇는 서글픈 안부</h3>
    <p>아델(Adele)이 과거의 자신과 상처를 주었던 연인에게 건네는 뒤늦은 사과입니다. 화자는 여전히 과거의 기억에서 완전히 벗어나지 못해 사과를 반복하고 있습니다.</p>
    <p><b>[서사 포인트]</b> "Hello from the other side"는 전화를 거는 물리적 상황과 더불어, 결코 돌아갈 수 없는 <b>'과거와 현재 사이의 단절'</b>을 비유적으로 표현합니다. 수천 번 전화를 걸었다는 고백은 미안함의 깊이를 나타냅니다.</p>
    """
    lyrics_raw = [
        ("Hello, it's me. I was wondering if you'd like to meet", "안녕, 나야. 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me? I'm dreaming about who we used to be", "내 말 들리니? 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done", "내 모든 일에 대해 미안하다고 말하려고 말야"),
        ("But when I call, you never seem to be home", "하지만 내가 전화할 때마다 넌 집에 없는 것 같아"),
        ("At least I can say that I've tried to tell you I'm sorry", "적어도 사과하기 위해 노력했다는 건 말할 수 있겠지")
    ]
    questions = [
        ("1. 화자가 전화를 거는 주된 이유는?", ["사과하기 위해", "부탁하려고", "자랑하려고"], "사과하기 위해"),
        ("2. 'a thousand times'의 함축 의미는?", ["간절한 마음", "정확한 횟수", "한 번만"], "간절한 마음"),
        ("3. 'California dreaming'은 무엇에 대한 비유?", ["예전의 우리 모습", "여행 계획", "날씨"], "예전의 우리 모습"),
        ("4. 'The other side'는 무엇을 의미하나요?", ["이별 후의 현재 상태", "지구 반대편", "저세상"], "이별 후의 현재 상태"),
        ("5. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다", "길을 잃다"], "궁금해하다"),
        ("6. 노래 전체의 지배적 감정은?", ["그리움과 후회", "기쁨과 희망", "분노"], "그리움과 후회")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 금지된 성벽을 넘는 자유</h3>
    <p>성안의 억압적인 생활에 갇혀있던 자스민 공주에게 알라딘이 마법 양탄자를 통해 진짜 세상을 보여주는 순간입니다.</p>
    <p><b>[서사 포인트]</b> 이 노래는 단순한 로맨스를 넘어 <b>'주체적인 자유와 새로운 시각'</b>을 상징합니다. "Let your heart decide"라는 말처럼 타인의 규칙이 아닌 자신의 마음이 이끄는 대로 세상을 바라보겠다는 의지가 담겨있습니다.</p>
    """
    lyrics_raw = [
        ("I can show you the world. Shining, shimmering, splendid", "당신에게 세상을 보여줄 수 있어요. 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes. Take you wonder by wonder", "당신의 눈을 뜨게 해 줄게요. 경이로운 곳들로 데려가 줄게요"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠"),
        ("No one to tell us 'No' or where to go", "누구도 안 된다거나 어디로 가라고 말 못 해요"),
        ("But when I'm way up here, it's crystal clear", "여기 높이 올라오니 모든 게 아주 명확해졌어요")
    ]
    questions = [
        ("1. 'Crystal clear'의 뜻은?", ["명확하다", "딱딱하다", "차갑다"], "명확하다"),
        ("2. 노래의 핵심 주제는?", ["자유와 시야의 확장", "순종적 태도", "양탄자 수리"], "자유와 시야의 확장"),
        ("3. 'Splendid'의 뜻은?", ["화려한/훌륭한", "평범한", "어두운"], "화려한/훌륭한"),
        ("4. 알라딘이 강조하는 삶의 방식은?", ["주체적인 결정", "공주의 의무", "성안의 보물"], "주체적인 결정"),
        ("5. 'Wonder by wonder'가 주는 느낌은?", ["끊임없는 감동", "지루함", "공포"], "끊임없는 감동"),
        ("6. 'Fantastic point of view'의 의미는?", ["환상적인 시야", "가짜 생각", "어지러움"], "환상적인 시야")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 어둠 속에서 빛나는 연대의 힘</h3>
    <p>인생의 '어두운 밤'과 같은 거대한 시련 속에서도 내 곁을 지켜주는 단 한 사람만 있다면 모든 것을 이겨낼 수 있다는 <b>신뢰와 우정</b>을 노래합니다.</p>
    <p><b>[서사 포인트]</b> "The moon is the only light"와 "The sky should tumble and fall"은 절망적인 상황을 비유하며, 그런 순간에도 '함께 서 있는(Stand by)' 존재가 있다면 눈물조차 흘리지 않겠다는 강력한 연대 의식을 보여줍니다.</p>
    """
    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "우리가 볼 수 있는 빛이라곤 저 달빛뿐일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요. 두려워하지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("If the sky that we look upon should tumble and fall", "우리가 올려다보는 저 하늘이 무너져 내린다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요. 눈물 한 방울 흘리지 않을 거예요")
    ]
    questions = [
        ("1. 화자가 두렵지 않은 전제 조건은?", ["누군가 곁에 있을 때", "돈이 많을 때", "해가 뜰 때"], "누군가 곁에 있을 때"),
        ("2. 'Shed a tear'의 뜻은?", ["눈물을 흘리다", "미소 짓다", "소리 지르다"], "눈물을 흘리다"),
        ("3. 'Tumble and fall'은 무엇을 상징하나요?", ["인생의 큰 시련", "가을 낙엽", "잠들기"], "인생의 큰 시련"),
        ("4. 'The night'가 비유하는 상황은?", ["힘든 고난의 시기", "실제 밤 시간", "정전"], "힘든 고난의 시기"),
        ("5. 'Stand by me'의 핵심 의미는?", ["지지와 동행", "옆에 서 있기", "길 비켜주기"], "지지와 동행"),
        ("6. 'The moon is the only light'는 어떤 느낌?", ["희망의 끈", "절대적 어둠", "화려함"], "희망의 끈")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임 끝에 놓쳐버린 사랑의 후회</h3>
    <p>잡을 수 있었던 인연을 알 수 없는 망설임과 두려움 때문에 놓쳐버린 후 느끼는 공허함을 담은 쓸쓸한 독백입니다.</p>
    <p><b>[서사 포인트]</b> 'Drenched in wine(술에 젖은 마음)'이나 'Empty as a drum(드럼처럼 텅 빈)'과 같은 은유를 통해 화자의 지독한 상실감을 시적으로 표현합니다. 왜 그때 다가지 못했는지 스스로에게 묻는 후회가 반복됩니다.</p>
    """
    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 밝아오는 걸 보며, 난 멀리 날아가 버리고 싶었죠"),
        ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"),
        ("I feel as empty as a drum, I don't know why I didn't come", "텅 빈 드럼처럼 공허해요, 내가 왜 가지 않았는지 모르겠어요")
    ]
    questions = [
        ("1. 노래의 전체적인 정서적 분위기는?", ["후회와 쓸쓸함", "분노와 격앙", "기쁨"], "후회와 쓸쓸함"),
        ("2. 'Drenched in wine'이 비유하는 상태는?", ["슬픔에 푹 젖은 마음", "즐거운 파티", "갈증"], "슬픔에 푹 젖은 마음"),
        ("3. 'A bag of bones'는 어떤 모습을 의미하나요?", ["야위고 기운 없는 상태", "튼튼한 골격", "무거운 짐"], "야위고 기운 없는 상태"),
        ("4. 화자가 약속에 나가지 않은 이유는?", ["알 수 없는 망설임", "약속을 잊음", "상대의 거절"], "알 수 없는 망설임"),
        ("5. 'Empty as a drum'은 무엇을 시각화했나요?", ["내면의 지독한 공허함", "악기 연주 실력", "소음"], "내면의 지독한 공허함"),
        ("6. 'I don't know why' 반복의 효과는?", ["자책하는 마음 강조", "단어 공부", "단순 후렴구"], "자책하는 마음 강조")
    ]

# -------------------------
# 가사 가공 (알파벳 기호 추가)
# -------------------------
alphabet = list(string.ascii_lowercase)
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

# -------------------------
# 순서 섞기 및 세션 관리
# -------------------------
correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 탭별 화면 출력 (레이아웃 유지)
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
    # 좌우 2분할 레이아웃
    col_left, col_right = st.columns([1, 1.2])
    
    with col_left:
        st.video(video_url)
        st.divider()
        st.markdown("### 💡 Comprehension Quiz")
        with st.form(f"quiz_{song_choice}"):
            for i, (q, opts, ans) in enumerate(questions):
                q_text = q
                if st.session_state.submitted_step2:
                    user_val = st.session_state.get(f"q_sel_{i}")
                    q_text += " ✅" if user_val == ans else f" 🔍 (정답: {ans})"
                st.radio(q_text, opts, index=None, key=f"q_sel_{i}")
            if st.form_submit_button("정답 확인 및 채점"):
                st.session_state.submitted_step2 = True
                st.rerun()
                
    with col_right:
        st.markdown("### 🎼 Full Lyrics")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

elif selected_tab == "🧩 순서 배열":
    st.subheader("🧩 가사 순서대로 클릭하세요 (a, b, c... 순서 참고)")
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(text, key=f"btn3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    st.divider()
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.92, 0.08])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del3_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()
    if st.session_state.get('show_q3_result'):
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"Step {i+1}: Perfect!")
            else:
                st.error(f"Step {i+1}: Wrong (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
