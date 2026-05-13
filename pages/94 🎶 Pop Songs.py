import streamlit as st
import random

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

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
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

# -------------------------
# [데이터 빌드: 배경지식 및 스토리텔링 강화]
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 억압된 자아의 폭발과 진정한 자유</h3>
    <p><b>[심층 배경]</b> 이 노래는 주인공 엘사가 자신의 마법 능력이 온 세상에 드러난 후, 사람들의 시선을 피해 북쪽 산으로 도망치며 부르는 노래입니다. 어린 시절부터 "감추고(Conceal), 느끼지 마라(Don't feel)"는 교육을 받으며 타인의 기준에 맞춘 '착한 소녀'로 살아왔던 그녀가, 아이러니하게도 고립된 산속에서 비로소 <b>심리적 해방감</b>을 느끼는 과정을 보여줍니다.</p>
    <p><b>[학습 포인트]</b> 가사 중 "The cold never bothered me anyway"는 단순히 물리적 추위를 견딜 수 있다는 뜻을 넘어, 타인의 차가운 시선이나 사회적 편견이 더 이상 나를 아프게 하지 못한다는 <b>자존감의 회복</b>을 상징합니다. 또한 'Conceal'과 같은 단어는 비밀을 엄격히 지켜야 했던 그녀의 과거를 고스란히 담고 있습니다.</p>
    <p><b>[스토리텔링]</b> 발자국 하나 없는 하얀 눈 위에서 엘사는 자신만의 얼음 성을 쌓아 올립니다. 이는 과거의 구속(장갑, 왕관)을 벗어던지고 자신의 잠재력을 있는 그대로 인정하는 성인식과 같은 순간입니다. 이제 그녀는 더 이상 문을 닫고 숨어 지내는 소녀가 아니라, 폭풍을 다스리는 당당한 여왕으로 거듭납니다.</p>
    """
    full_lyrics = [
        ("The snow glows white on the mountain tonight, not a footprint to be seen", "오늘 밤 산엔 눈이 하얗게 빛나고, 발자국 하나 보이지 않네"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부쥐고 있어"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"),
        ("Don't let them in, don't let them see. Be the good girl you always have to be", "그들을 들여보내지 마, 보여주지 마. 늘 그랬듯 착한 소녀가 되어야 해"),
        ("Conceal, don't feel, don't let them know. Well, now they know!", "숨기고, 느끼지 말고, 모르게 해. 그런데 이제 그들이 알아버렸어!"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어"),
        ("Let it go, let it go! Turn away and slam the door!", "다 잊어, 이제 자유야! 돌아서서 문을 쾅 닫아버려!"),
        ("I don't care what they're going to say. Let the storm rage on", "그들이 뭐라 하든 상관없어. 폭풍아 계속 휘몰아쳐라"),
        ("The cold never bothered me anyway", "추위는 더 이상 나를 괴롭히지 못하니까")
    ]
    questions = [("1. 현재 엘사의 심경은?", ["공포", "해방감", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["드러내다", "숨기다", "공격하다"], "숨기다"), ("3. 'The cold never bothered me'의 실제 의미는?", ["난 감기에 안 걸린다", "추위(시선)는 상관없다", "눈이 싫다"], "추위(시선)는 상관없다")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거와 현재를 잇는 서글픈 응답하라</h3>
    <p><b>[심층 배경]</b> 25세의 아델이 과거의 자신과 그리고 과거에 상처를 주었던 연인에게 건네는 뒤늦은 안부 인사입니다. 노래 속 'California'는 단순히 장소를 의미하기보다, 화자가 현재 머물고 있는 물리적/심리적 거리를 상징합니다. 상대방은 이미 모든 것을 잊고 잘 지내고 있지만, 화자는 여전히 과거의 기억에서 벗어나지 못해 사과를 되풀이하고 있습니다.</p>
    <p><b>[학습 포인트]</b> "Hello from the other side"는 전화를 거는 상황뿐만 아니라, 다시는 돌아갈 수 없는 <b>'과거의 우리'와 '현재의 나' 사이의 단절</b>을 비유하는 아주 깊은 표현입니다. 'It don't matter'와 같은 구어체적 표현을 통해 아델 특유의 감성을 느낄 수 있습니다.</p>
    <p><b>[스토리텔링]</b> 수천 번(a thousand times) 전화를 걸었다는 가사는 그만큼 씻어내지 못한 미안함이 크다는 것을 의미합니다. 하지만 상대방은 전화를 받지 않거나 집에 없습니다. 이는 결국 사과란 상대방을 위해서가 아니라, 나의 죄책감을 덜기 위한 마지막 시도일 수도 있다는 서글픈 깨달음을 줍니다.</p>
    """
    full_lyrics = [
        ("Hello, it's me. I was wondering if after all these years you'd like to meet", "안녕, 나야. 이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me? I'm in California dreaming about who we used to be", "여보세요, 내 말 들리니? 난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done", "내 모든 일에 대해 미안하다고 말하려고 말야"),
        ("But when I call, you never seem to be home", "하지만 내가 전화할 때마다 넌 절대 집에 없는 것 같아"),
        ("Hello from the outside. At least I can say that I've tried", "외부에서 인사해. 적어도 내가 노력했다는 말은 할 수 있겠지"),
        ("To tell you I'm sorry for breaking your heart", "네 마음을 아프게 해서 미안하다고 말하기 위해서 말야"),
        ("But it don't matter, it clearly doesn't tear you apart anymore", "하지만 상관없겠지, 그게 더 이상 널 힘들게 하지 않는 게 분명하니까")
    ]
    questions = [("1. 화자가 전화를 거는 주된 목적은?", ["부탁", "사과", "자랑"], "사과"), ("2. 'a thousand times'가 의미하는 바는?", ["정확히 1000번", "간절함과 많은 시도", "번호 오기입"], "간절함과 많은 시도"), ("3. 상대방의 현재 상태는?", ["여전히 슬퍼함", "더 이상 아프지 않음", "화가 나 있음"], "더 이상 아프지 않음")]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 금지된 장벽을 넘는 자유의 비행</h3>
    <p><b>[심층 배경]</b> 성안의 억압적인 생활과 정략결혼의 압박 속에서 살던 자스민 공주에게, 알라딘은 '마법 양탄자'라는 수단을 통해 난생처음 성 밖의 진짜 세상을 보여줍니다. 이 곡은 단순히 로맨틱한 데이트를 넘어, <b>'보는 것(Seeing)'과 '아는 것(Knowing)'</b>의 차이를 이야기합니다. 궁전 안의 화려함이 전부인 줄 알았던 공주에게 세상은 훨씬 넓고 눈부신 곳임을 알려주는 순간입니다.</p>
    <p><b>[학습 포인트]</b> "Crystal clear"는 액체나 보석이 투명하다는 뜻도 있지만, 가사에서는 어떤 사실이나 상황이 <b>머릿속에서 아주 명확하게 이해됨</b>을 의미합니다. 또한 'Splendid', 'Dazzling' 같은 단어를 통해 세상의 아름다움을 묘사하는 풍부한 형용사를 배울 수 있습니다.</p>
    <p><b>[스토리텔링]</b> 구름 위를 날며 두 사람은 "안 돼(No)"라고 말하거나 어디로 가라고 명령하는 이가 없는 공간에 도달합니다. 이는 단순히 고도가 높은 곳으로 올라간 것이 아니라, <b>사회적 계급과 구속이 없는 이상향</b>에 도착했음을 뜻합니다. 자스민은 이제 '공주'라는 역할이 아닌 '나 자신'으로 세상을 바라보기 시작합니다.</p>
    """
    full_lyrics = [
        ("I can show you the world. Shining, shimmering, splendid", "당신에게 세상을 보여줄 수 있어요. 빛나고 어른거리며 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "말해봐요 공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes. Take you wonder by wonder", "당신의 눈을 뜨게 해 줄게요. 경이로운 곳들로 당신을 데려가 줄게요"),
        ("Over, sideways and under on a magic carpet ride", "마법 양탄자를 타고 위로, 옆으로, 아래로 가로지르며 말이죠"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 새롭고 환상적인 시야가 펼쳐져요"),
        ("No one to tell us 'No' or where to go, or say we're only dreaming", "누구도 안 된다거나 어디로 가라고 말 못 해요, 우리가 꿈꾸는 뿐이라 말하지도 못하죠"),
        ("A whole new world! A dazzling place I never knew", "완전히 새로운 세상! 내가 결코 알지 못했던 눈부신 곳이에요"),
        ("But when I'm way up here, it's crystal clear", "하지만 여기 높이 올라오니 모든 게 아주 명확해졌어요"),
        ("That now I'm in a whole new world with you", "지금 내가 당신과 함께 완전히 새로운 세상에 있다는 사실이요")
    ]
    questions = [("1. 두 사람이 타고 있는 것은?", ["양탄자", "빗자루", "구름"], "양탄자"), ("2. 'Crystal clear'의 문맥상 뜻은?", ["수정이 깨끗함", "매우 명확함", "유리가 투명함"], "매우 명확함"), ("3. 노래의 핵심 주제는?", ["여행의 위험성", "자유와 주체적인 삶", "왕실의 예절"], "자유와 주체적인 삶")]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 시련을 이겨내는 연대의 힘</h3>
    <p><b>[심층 배경]</b> 1961년 벤 E. 킹에 의해 발표된 이후, 전 세계적으로 가장 많이 리메이크된 명곡 중 하나입니다. 이 노래에서 말하는 '어두운 밤(Dark night)'이나 '무너지는 하늘(Sky tumble)'은 우리 인생에서 마주하는 경제적 위기, 사회적 차별, 개인적인 절망 등 모든 <b>시련</b>을 상징합니다.</p>
    <p><b>[학습 포인트]</b> "Just as long as"는 시간의 길이를 말하는 것이 아니라 <b>"~하는 한은"이라는 조건</b>을 나타내는 아주 중요한 숙어입니다. 즉, 다른 모든 것이 무너져도 '너만 곁에 있다면' 괜찮다는 확신을 담고 있습니다. 'Shed a tear'와 같은 관용구는 감정 표현 학습에 매우 유익합니다.</p>
    <p><b>[스토리텔링]</b> 산이 바다로 무너져 내리는 천재지변 속에서도 화자는 눈물을 흘리지 않겠다고 말합니다. 이는 인간이 가진 가장 강력한 무기는 물질적인 풍요가 아니라, 서로의 곁을 지켜주는 <b>신뢰와 사랑</b>임을 역설하고 있습니다. 단순한 사랑 노래를 넘어 우정과 인류애를 상징하는 곡으로 평가받습니다.</p>
    """
    full_lyrics = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "우리가 볼 수 있는 빛이라곤 저 달빛뿐일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요. 두려워하지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에, 내 곁에 서 있어 주기만 한다면요"),
        ("If the sky that we look upon should tumble and fall", "우리가 올려다보는 저 하늘이 무너져 내린다 해도"),
        ("Or the mountain should crumble to the sea", "혹은 저 산이 바다로 무너져 내린다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요. 눈물 한 방울 흘리지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에, 내 곁에 서 있어 주기만 한다면요")
    ]
    questions = [("1. 'Stand by me'의 핵심 의미는?", ["앞에 서라", "곁을 지켜달라", "일어서라"], "곁을 지켜달라"), ("2. 화자가 두려움을 느끼지 않는 조건은?", ["돈이 많을 때", "달빛이 밝을 때", "상대가 곁에 있을 때"], "상대가 곁에 있을 때"), ("3. 'Shed a tear'의 뜻은?", ["편지를 쓰다", "눈물을 흘리다", "화를 내다"], "눈물을 흘리다")]

else: # 5. Don't Know Why - Norah Jones
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임 끝에 놓쳐버린 사랑의 여운</h3>
    <p><b>[심층 배경]</b> 2000년대 초반 전 세계를 사로잡은 노라 존스의 대표곡으로, 재즈와 팝이 절묘하게 섞인 서정적인 곡입니다. 이 노래는 잡을 수 있었던 인연을 <b>망설임과 두려움</b> 때문에 놓쳐버린 후 느끼는 공허함을 담고 있습니다. 왜 그때 다가가지 못했는지(I don't know why I didn't come) 스스로에게 묻는 쓸쓸한 독백과도 같습니다.</p>
    <p><b>[학습 포인트]</b> "Drenched in wine"이나 "Bag of bones"와 같은 표현은 매우 문학적인 비유입니다. 'Drenched'는 흠뻑 젖었다는 뜻으로, 슬픔에 잠긴 마음을 술에 빗대어 표현한 것입니다. 'A bag of bones'는 몹시 야위고 힘없는 상태를 의미하며, 상실감으로 인해 기력을 잃은 화자의 모습을 시각적으로 보여줍니다.</p>
    <p><b>[스토리텔링]</b> 해가 뜰 때까지 기다렸지만 정작 약속 장소에는 나가지 못한 화자. 모래 위에 무릎을 꿇고 눈물을 훔치는 그녀의 모습은 후회로 가득 차 있습니다. "마음은 비어있는 드럼처럼 공허하다"는 가사는 소중한 사람을 잃은 뒤 찾아오는 <b>지독한 외로움</b>을 소리로 시각화한 멋진 표현입니다.</p>
    """
    full_lyrics = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 밝아오는 걸 보며, 난 멀리 날아가 버리고 싶었죠"),
        ("Instead of kneeling in the sand, catching tear-drops in my hand", "모래 위에 무릎 꿇고 손으로 눈물을 훔치는 대신 말예요"),
        ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"),
        ("But I'll be a bag of bones, driving down the road alone", "난 그저 뼈만 남은 사람처럼 홀로 길을 달려가겠죠"),
        ("I feel as empty as a drum, I don't know why I didn't come", "텅 빈 드럼처럼 공허해요, 내가 왜 가지 않았는지 모르겠어요")
    ]
    questions = [
        ("1. 'I don't know why I didn't come'의 정서는?", ["분노", "후회와 아쉬움", "기쁨"], "후회와 아쉬움"),
        ("2. 'Drenched'의 의미로 알맞은 것은?", ["바싹 마른", "흠뻑 젖은", "차갑게 식은"], "흠뻑 젖은"),
        ("3. 'Empty as a drum'은 무엇을 비유하는가?", ["시끄러운 소리", "마음의 공허함", "악기 연주"], "마음의 공허함")
    ]

# -------------------------
# 공통 데이터 처리 및 UI 출력
# -------------------------
correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

tab1, tab2, tab3 = st.tabs(["1. 🎬 배경 학습", "2. 📖 가사 & 퀴즈", "3. 🧩 순서 배열"])

with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: st.video(video_url)

with tab2:
    col_v, col_l = st.columns([1, 1.2])
    with col_v:
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
            if st.form_submit_button("정답 확인"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col_l:
        st.markdown("### 🎼 Full Lyrics")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 문장 순서 맞추기")
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
            if user_s == correct_order[i]: st.success(f"{i+1}: Perfect!")
            else:
                st.error(f"{i+1}: Wrong Order (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
