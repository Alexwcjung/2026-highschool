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
    .big-label {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #1e3a8a !important;
        margin-bottom: 15px !important;
        display: block;
    }
    .info-box {
        background-color: #f1f5f9; padding: 35px; border-radius: 15px;
        border: 1px solid #cbd5e1; line-height: 2.0; margin-bottom: 25px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 3px solid #6366f1; padding-bottom: 12px; margin-top: 0; font-size: 1.6rem; }
    .info-box b { color: #1e3a8a; font-size: 1.1rem; }
    .info-box p { margin-bottom: 15px; font-size: 1.05rem; color: #334155; }
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

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

# -------------------------
# 곡별 데이터 설정 (대폭 보강된 배경 지식)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 완벽함을 강요받는 사회에서의 탈출</h3>
    <p><b>[작품 배경]</b> 디즈니 애니메이션 '겨울왕국'의 엘사는 태어날 때부터 통제할 수 없는 강력한 마법 능력을 가졌습니다. 그녀의 부모는 능력을 숨기라고 가르쳤고, 엘사는 평생을 자신을 억누르며 '착한 소녀(Good girl)'로 살기 위해 고군분투했습니다. 이 곡은 그녀의 비밀이 온 세상에 탄로나고, 모든 것을 내려놓은 뒤 홀로 북쪽 산으로 향하며 부르는 노래입니다.</p>
    <p><b>[문학적 해석]</b> 노래 초반부의 '고립된 왕국'은 엘사의 심리적 폐쇄성을 상징합니다. 하지만 곡이 진행될수록 엘사는 자신의 능력을 더 이상 '저주'가 아닌 '자아의 일부'로 받아들입니다. 가사 속 <b>"Conceal, don't feel"</b>은 감정을 억압해야 했던 과거를, <b>"Let it go"</b>는 타인의 시선에서 해방되어 진정한 자신의 모습으로 살겠다는 선언을 담고 있습니다.</p>
    <p><b>[핵심 메시지]</b> 이 곡은 전 세계적으로 <b>'자기 수용(Self-Acceptance)'</b>의 찬가가 되었습니다. "추위는 더 이상 나를 괴롭히지 못한다"는 선언은, 나를 옥죄던 세상의 차가운 편견조차 나의 자존감을 꺾을 수 없음을 시사합니다.</p>
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
        ("1. 엘사가 현재 주요 심경은?", ["해방감", "공포", "분노"], "해방감"),
        ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"),
        ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 날씨", "겨울 휴가"], "사회적 시선"),
        ("4. 'Good girl'은 무엇의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회"),
        ("5. 'Isolation'의 정확한 뜻은?", ["고립/격리", "함께함", "승리"], "고립/격리"),
        ("6. 'Storm inside'는 무엇의 비유인가요?", ["억눌린 감정", "마법 능력", "기상 이변"], "억눌린 감정")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 상처와 조우하는 용기</h3>
    <p><b>[작품 배경]</b> 아델(Adele)의 3집 앨범 '25'의 타이틀곡인 이 노래는 전 세계 28개국 차트 1위를 휩쓸었습니다. 아델은 이 곡이 단순히 헤어진 연인에게 보내는 편지가 아니라, <b>'과거의 자신과 화해하고 싶은 마음'</b>을 담았다고 밝혔습니다. 나이가 들면서 잊고 지냈던 소중한 사람들, 그리고 한때 순수했던 예전의 나에게 건네는 안부입니다.</p>
    <p><b>[문학적 해석]</b> <b>"Hello from the other side"</b>라는 표현은 중의적입니다. 물리적으로는 전화기 너머를 뜻하지만, 은유적으로는 '성장이 끝난 현재의 나'가 '미숙했던 과거의 나'를 바라보는 경계를 의미합니다. 수천 번 전화했다는 가사는 결코 닿을 수 없는 시간의 간극에 대한 안타까움과 후회를 극적으로 보여줍니다.</p>
    <p><b>[핵심 메시지]</b> 아델은 이 노래를 통해 누구나 가슴 한구석에 품고 있는 '미안함'을 대변합니다. 상대가 전화를 받지 않더라도, 사과를 전하려 노력했다는 사실만으로도 화자는 치유를 얻습니다.</p>
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
    <h3>✨ A Whole New World: 금기된 성벽을 넘어선 새로운 시야</h3>
    <p><b>[작품 배경]</b> 애니메이션 '알라딘'의 하이라이트 곡입니다. 성안에 갇혀 자신의 운명을 주체적으로 결정하지 못했던 자스민 공주에게, 거리의 부랑자였던 알라딘이 마법 양탄자를 통해 성벽 너머의 진짜 세상을 보여줍니다. 두 사람이 밤하늘을 가로지르며 느끼는 해방감과 로맨스를 담고 있습니다.</p>
    <p><b>[문학적 해석]</b> 이 노래에서 '새로운 세상'은 단순한 풍경이 아니라 <b>'주체적인 삶'</b>을 의미합니다. "Let your heart decide(당신의 마음이 결정하게 하세요)"라는 알라딘의 제안은 타인의 규칙에 얽매여 살던 공주에게 큰 울림을 줍니다. 하늘 높이 올라갔을 때 모든 것이 <b>'Crystal clear(수정처럼 명확한)'</b>해졌다는 가사는, 높은 곳에서 내려다볼 때 비로소 자신의 삶을 객관적으로 바라볼 수 있게 되었음을 시사합니다.</p>
    <p><b>[핵심 메시지]</b> 익숙한 환경을 벗어나는 용기가 우리에게 얼마나 더 넓은 세상을 보여주는지에 대한 찬가입니다.</p>
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
    <h3>🤝 Stand By Me: 절망의 끝에서 빛나는 신뢰의 힘</h3>
    <p><b>[작품 배경]</b> 1961년 벤 E. 킹이 발표한 이 곡은 인종차별과 갈등이 심했던 당시 미국 사회에 큰 위로를 주었습니다. 성경의 시편에서 영감을 얻은 가사는, 세상이 아무리 험난하고 어두워도 서로를 지지해주는 사람만 있다면 두려움 없이 나아갈 수 있다는 메시지를 전달합니다.</p>
    <p><b>[문학적 해석]</b> 노래 전반부의 <b>"Night has come(밤이 왔다)"</b>과 <b>"Land is dark(땅이 어둡다)"</b>는 인생에서 마주하는 절망적인 시기나 사회적 혼란을 상징합니다. 하늘이 무너져 내리는(Tumble and fall) 극단적인 상황에서도 "내 곁에 서 달라(Stand by me)"는 부탁은, 물질적 도움이 아닌 정서적 연대가 인간을 구원한다는 점을 강조합니다.</p>
    <p><b>[핵심 메시지]</b> 'Stand by'라는 단어는 단순히 옆에 서 있는 것이 아니라, <b>'어떤 고난이 있어도 당신의 편이 되겠다'</b>는 숭고한 약속입니다. 이 곡은 영화, 시위 현장, 축제 등 연대가 필요한 모든 곳에서 불리고 있습니다.</p>
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
    <h3>🍂 Don't Know Why: 망설임의 미학, 그리고 짙은 후회</h3>
    <p><b>[작품 배경]</b> 노라 존스(Norah Jones)의 데뷔 앨범 타이틀곡으로, 2003년 그래미 시상식을 휩쓴 재즈 팝의 명곡입니다. 이 곡은 연인과의 약속 장소에 가지 못한 여자가 새벽녘에 홀로 느끼는 상실감과 자책을 노래합니다. 특별한 사건보다는 <b>'미묘한 감정의 파동'</b>을 다루는 것이 특징입니다.</p>
    <p><b>[문학적 해석]</b> <b>"I feel as empty as a drum(드럼처럼 공허하다)"</b>이라는 은유는 가슴 깊은 곳에서 울리는 공허함을 탁월하게 묘사합니다. 화자는 해가 뜰 때까지 기다렸지만, 결국 약속 장소인 'House of fun(축제의 집)'으로 가지 않았습니다. 왜 가지 않았는지 스스로도 명확히 설명하지 못하는(I don't know why) 모습은, 사랑 앞에서 두려움을 느끼는 인간의 나약함을 잘 보여줍니다.</p>
    <p><b>[핵심 메시지]</b> 인생에는 용기를 내야 할 순간이 있지만, 그 순간을 놓쳤을 때 남는 것은 영원한 후회와 "왜 그랬을까?"라는 물음뿐임을 담담하게 이야기합니다.</p>
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
# 가사 및 순서 가공
# -------------------------
alphabet = list(string.ascii_lowercase)
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 화면 출력 (레이아웃 엄격 유지)
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
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
