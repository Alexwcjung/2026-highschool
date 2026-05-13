import streamlit as st
import random
import string

# =========================
# 1. 기본 설정 및 디자인
# =========================
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(180deg, #ffffff 0%, #eef2ff 45%, #f8fafc 100%);
        color: #1e293b; 
    }
    .main-title {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        padding: 26px; 
        border-radius: 22px;
        text-align: center; 
        color: white; 
        margin-bottom: 25px;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.18);
    }
    .main-title h1 {
        margin: 0;
        font-size: 42px;
        font-weight: 900;
    }
    .big-label {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #1e3a8a !important;
        margin-bottom: 15px !important;
        display: block;
    }
    .info-box {
        background-color: #ffffff; 
        padding: 30px; 
        border-radius: 20px;
        border: 1px solid #cbd5e1; 
        line-height: 1.9; 
        margin-bottom: 25px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.10);
    }
    .info-box h3 { 
        color: #4338ca; 
        border-bottom: 3px solid #6366f1; 
        padding-bottom: 12px; 
        margin-top: 0; 
    }
    .info-box b { color: #1e3a8a; }
    .info-box p { font-size: 1.08rem; }
    .lyrics-container {
        padding: 12px 20px; 
        border-left: 5px solid #6366f1;
        margin-bottom: 10px; 
        background-color: #ffffff; 
        border-radius: 0 12px 12px 0;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
    }
    .eng-line { 
        font-size: 1.15rem; 
        font-weight: 700; 
        color: #1e3a8a; 
    }
    .kor-sub { 
        font-size: 0.95rem; 
        color: #64748b; 
    }
    div[data-testid="stRadio"] label {
        font-size: 1rem;
    }
    div[data-testid="stTabs"] button {
        font-size: 17px;
        font-weight: 800;
    }
    .stButton > button {
        border-radius: 13px;
        font-weight: 800;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 관리
# -------------------------
if "selected_song" not in st.session_state:
    st.session_state.selected_song = "1. Let It Go - Frozen OST"

if "submitted_step2" not in st.session_state:
    st.session_state.submitted_step2 = False

if "q3_cards" not in st.session_state:
    st.session_state.q3_cards = []

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"

if "show_q3_result" not in st.session_state:
    st.session_state.show_q3_result = False


def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    st.session_state.current_tab = "🎬 배경 학습"

    if "scrambled" in st.session_state:
        del st.session_state.scrambled

    # 곡을 바꿀 때 이전 퀴즈 선택값 제거
    for key in list(st.session_state.keys()):
        if key.startswith("q_sel_"):
            del st.session_state[key]


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
# 탭 수동 제어: key로 상태를 직접 저장
# 여기서 index와 수동 대입을 쓰지 않아야 탭 이동이 한 번에 인식됩니다.
# -------------------------
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]

selected_tab = st.radio(
    "",
    tabs_list,
    horizontal=True,
    label_visibility="collapsed",
    key="current_tab"
)

# -------------------------
# 곡별 데이터 설정
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"

    bg_content = """
    <h3>❄️ Let It Go: 숨겨야 했던 나를 드러내는 순간</h3>

    <p>
    이 노래는 영화 <b>Frozen</b>에서 엘사가 자신의 마법 능력을 더 이상 숨기지 않기로 결심하는 장면에 나옵니다.
    엘사는 어릴 때부터 모든 것을 얼리는 힘을 가지고 있었지만, 그 힘 때문에 다른 사람을 다치게 할까 봐 두려워했습니다.
    그래서 오랫동안 자신의 감정과 능력을 숨기며 살아왔습니다.
    </p>

    <p>
    대관식 날, 엘사의 마법이 사람들 앞에 드러나고 사람들은 그녀를 두려워합니다.
    엘사는 결국 왕국을 떠나 눈 덮인 산으로 도망갑니다.
    하지만 산 위에서 그녀는 처음으로 다른 사람의 시선을 벗어나 자유를 느낍니다.
    </p>

    <p>
    <b>핵심 메시지:</b> 이 노래는 단순히 “다 잊어버리자”는 뜻이 아니라,
    억눌렸던 자신을 받아들이고 진짜 나로 살아가려는 용기를 보여줍니다.
    학생들은 이 노래를 통해 <b>자기표현, 자유, 두려움 극복</b>이라는 주제를 생각해 볼 수 있습니다.
    </p>
    """

    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나고"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"),
        ("Be the good girl you always have to be", "늘 그랬듯 착한 소녀가 되어야 해"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 말고, 모르게 해"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어")
    ]

    questions = [
        ("1. 엘사의 현재 심경은?", ["해방감", "공포", "분노"], "해방감"),
        ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"),
        ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 추운 날씨", "겨울 왕국"], "사회적 시선"),
        ("4. 'Good girl'은 누구의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회"),
        ("5. 'Isolation'의 의미는?", ["고립/격리", "함께함", "승리"], "고립/격리"),
        ("6. 가사에서 폭풍(Storm)은 무엇을 비유하나요?", ["내면의 억눌린 감정", "실제 기상 악화", "자연의 힘"], "내면의 억눌린 감정")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"

    bg_content = """
    <h3>☎️ Hello: 지나간 관계에 건네는 늦은 사과</h3>

    <p>
    Adele의 <b>Hello</b>는 오래전에 멀어진 사람에게 다시 연락하는 마음을 담은 노래입니다.
    화자는 시간이 많이 지난 뒤에도 여전히 과거의 기억을 떠올립니다.
    전화를 걸지만, 상대방에게 제대로 닿지 않는 듯한 느낌이 반복됩니다.
    </p>

    <p>
    이 노래에서 “Hello”는 단순한 인사말이 아닙니다.
    그 안에는 <b>미안함, 후회, 그리움, 다시 말하고 싶은 마음</b>이 담겨 있습니다.
    화자는 과거의 자신을 돌아보며, 그때 하지 못했던 말을 이제라도 전하고 싶어 합니다.
    </p>

    <p>
    <b>핵심 메시지:</b> 사람은 누구나 지나간 관계나 선택에 대해 후회할 때가 있습니다.
    이 노래는 그런 감정을 솔직하게 마주하는 과정을 보여줍니다.
    학생들은 이 노래를 통해 <b>사과, 그리움, 후회, 감정 표현</b>과 관련된 영어 표현을 배울 수 있습니다.
    </p>
    """

    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side", "반대편에서 인사해"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야")
    ]

    questions = [
        ("1. 화자가 전화를 거는 주된 이유는?", ["사과하기 위해", "돈을 빌리기 위해", "자랑하기 위해"], "사과하기 위해"),
        ("2. 'a thousand times'의 속뜻은?", ["간절한 반복", "정확히 1,000번", "한 번만"], "간절한 반복"),
        ("3. 'California dreaming'은 무엇에 대한 비유인가요?", ["예전의 우리 모습", "여행 계획", "날씨"], "예전의 우리 모습"),
        ("4. 'The other side'는 무엇을 의미하나요?", ["이별 후의 현재 상태", "지구 반대편", "저세상"], "이별 후의 현재 상태"),
        ("5. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다", "길을 잃다"], "궁금해하다"),
        ("6. 노래의 전반적인 정서는?", ["그리움과 후회", "기쁨과 희망", "분노와 증오"], "그리움과 후회")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"

    bg_content = """
    <h3>✨ A Whole New World: 새로운 세상을 보는 용기</h3>

    <p>
    이 노래는 영화 <b>Aladdin</b>에서 알라딘과 자스민이 마법 양탄자를 타고 새로운 세상을 바라보는 장면에 나옵니다.
    자스민은 궁전 안에서 보호받으며 살았지만, 동시에 자유롭게 세상을 경험하지 못했습니다.
    알라딘은 그녀에게 궁전 밖의 넓은 세상을 보여줍니다.
    </p>

    <p>
    노래 속 “A Whole New World”는 단순히 새로운 장소를 뜻하지 않습니다.
    그것은 <b>새로운 시야, 새로운 경험, 스스로 선택하는 삶</b>을 의미합니다.
    자스민은 이 장면을 통해 자신이 몰랐던 세상을 보고, 자신의 마음이 원하는 방향을 생각하게 됩니다.
    </p>

    <p>
    <b>핵심 메시지:</b> 새로운 세상을 만난다는 것은 단순히 여행을 떠나는 것이 아니라,
    내 생각과 시야가 넓어지는 경험입니다.
    학생들은 이 노래를 통해 <b>도전, 자유, 새로운 관점, 주체적인 선택</b>이라는 주제를 배울 수 있습니다.
    </p>
    """

    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 어른거리며 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"),
        ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠")
    ]

    questions = [
        ("1. 'Crystal clear'의 문맥상 의미는?", ["아주 명확한", "유리처럼 딱딱한", "차가운"], "아주 명확한"),
        ("2. 노래의 핵심 주제는?", ["자유와 새로운 시각", "성안에서의 안전", "마법 양탄자 수리"], "자유와 새로운 시각"),
        ("3. 'Splendid'의 뜻은?", ["화려한/훌륭한", "평범한", "어두운"], "화려한/훌륭한"),
        ("4. 알라딘이 공주에게 묻는 '마음의 결정'은 무엇을 뜻하나?", ["주체적인 삶", "결혼 결정", "외출 허락"], "주체적인 삶"),
        ("5. 'Wonder by wonder'는 어떤 느낌을 주나요?", ["끊임없는 감동", "지루함", "공포"], "끊임없는 감동"),
        ("6. 'Fantastic point of view'는 무엇을 의미하나요?", ["환상적인 시야", "가짜 뉴스", "어지러움"], "환상적인 시야")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"

    bg_content = """
    <h3>🤝 Stand By Me: 힘든 순간에도 곁에 있어 주는 사람</h3>

    <p>
    <b>Stand By Me</b>는 어려운 상황에서도 누군가가 내 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다.
    노래 속에는 어두운 밤, 무너지는 하늘, 흔들리는 땅 같은 표현이 나옵니다.
    이것들은 실제 자연 현상이라기보다 인생에서 만나는 <b>불안, 위기, 두려움</b>을 상징합니다.
    </p>

    <p>
    하지만 화자는 그런 상황 속에서도 “네가 내 곁에 있어 준다면 두렵지 않다”고 말합니다.
    여기서 중요한 것은 큰 해결책이 아닙니다.
    그저 옆에 있어 주는 것, 함께 버텨 주는 것만으로도 사람에게 큰 힘이 될 수 있다는 뜻입니다.
    </p>

    <p>
    <b>핵심 메시지:</b> 이 노래는 우정, 신뢰, 지지의 가치를 보여줍니다.
    학생들은 이 노래를 통해 <b>친구를 지지하는 말, 어려울 때 함께하는 태도, 관계의 소중함</b>을 배울 수 있습니다.
    </p>
    """

    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("If the sky that we look upon should tumble and fall", "우리가 보는 저 하늘이 무너져 내린다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요")
    ]

    questions = [
        ("1. 화자가 두렵지 않은 조건은?", ["누군가 곁에 있을 때", "돈이 많을 때", "해가 뜰 때"], "누군가 곁에 있을 때"),
        ("2. 'Shed a tear'의 뜻은?", ["눈물을 흘리다", "미소를 짓다", "소리를 지르다"], "눈물을 흘리다"),
        ("3. 'Tumble and fall'은 무엇을 상징하나요?", ["큰 시련이나 재앙", "가을 낙엽", "잠들기"], "큰 시련이나 재앙"),
        ("4. 'The night is dark'는 어떤 상황을 비유하나요?", ["인생의 힘든 시기", "실제 취침 시간", "정전 상황"], "인생의 힘든 시기"),
        ("5. 'Stand by me'의 핵심 의미는?", ["지지와 동행", "옆에 서 있기만 하기", "길 비켜주기"], "지지와 동행"),
        ("6. 'The moon is the only light'가 주는 느낌은?", ["희망의 끈", "절대적인 어둠", "화려함"], "희망의 끈")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"

    bg_content = """
    <h3>🍂 Don't Know Why: 망설임 뒤에 남은 후회</h3>

    <p>
    Norah Jones의 <b>Don't Know Why</b>는 조용하고 부드러운 분위기의 노래이지만,
    그 안에는 깊은 후회와 쓸쓸함이 담겨 있습니다.
    화자는 어떤 사람에게 가지 못했고, 시간이 지난 뒤에도 왜 그때 가지 않았는지 스스로에게 묻습니다.
    </p>

    <p>
    이 노래의 핵심 감정은 <b>망설임</b>입니다.
    가고 싶었지만 가지 못했고, 말하고 싶었지만 말하지 못한 마음이 노래 전체에 흐릅니다.
    그래서 반복되는 “I don't know why”는 단순히 이유를 모른다는 뜻이 아니라,
    자신의 선택을 계속 되돌아보는 마음을 보여줍니다.
    </p>

    <p>
    <b>핵심 메시지:</b> 때로는 용기를 내지 못한 선택이 오래 마음에 남을 수 있습니다.
    이 노래는 조용한 멜로디를 통해 <b>후회, 망설임, 그리움, 놓친 기회</b>를 표현합니다.
    학생들은 이 노래를 통해 감정을 은근하게 표현하는 영어를 배울 수 있습니다.
    </p>
    """

    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 올 때 난 멀리 날아가 버리고 싶었죠"),
        ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"),
        ("I feel as empty as a drum, I don't know why I didn't come", "텅 빈 드럼처럼 공허해요")
    ]

    questions = [
        ("1. 이 노래의 지배적인 감정은?", ["후회와 아쉬움", "분노와 원망", "기쁨"], "후회와 아쉬움"),
        ("2. 'Drenched in wine'은 무엇을 비유하나?", ["슬픔에 젖은 마음", "즐거운 파티", "갈증"], "슬픔에 젖은 마음"),
        ("3. 'A bag of bones'는 어떤 상태인가?", ["무기력하고 야윈 상태", "건강한 상태", "무거운 상태"], "무기력하고 야윈 상태"),
        ("4. 화자가 약속에 가지 않은 진짜 이유는?", ["망설임과 두려움", "길을 잃어서", "약속을 잊어서"], "망설임과 두려움"),
        ("5. 'Empty as a drum'은 무엇을 강조하나?", ["내면의 공허함", "시끄러운 소리", "음악적 재능"], "내면의 공허함"),
        ("6. 가사가 계속 반복되는 이유는?", ["자책하는 마음의 강조", "단어 암기", "시간 때우기"], "자책하는 마음의 강조")
    ]

# -------------------------
# 가사 가공
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

if "scrambled" not in st.session_state or st.session_state.get("last_song") != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 화면 출력
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)

    v1, v2, v3 = st.columns([1, 4, 1])
    with v2:
        st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
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

            if st.form_submit_button("정답 확인 및 채점"):
                st.session_state.submitted_step2 = True
                st.rerun()

    with col_l:
        st.markdown("### 🎼 Full Lyrics")

        for eng, kor in full_lyrics:
            st.markdown(
                f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>',
                unsafe_allow_html=True
            )

elif selected_tab == "🧩 순서 배열":
    st.subheader("🧩 가사 순서대로 클릭하세요")
    st.caption("a, b, c... 순서를 참고해서 클릭하세요.")

    b_cols = st.columns(2)

    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards

        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(
            text,
            key=f"btn3_{i}",
            use_container_width=True,
            disabled=is_sel
        ):
            st.session_state.q3_cards.append(text)
            st.rerun()

    st.divider()

    st.markdown("### 내가 선택한 순서")

    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.92, 0.08])
        c1.info(f"{idx + 1}: {card}")

        if c2.button("🗑️", key=f"del3_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    c_reset, c_result = st.columns(2)

    with c_reset:
        if st.button("다시 섞기", use_container_width=True):
            st.session_state.q3_cards = []
            st.session_state.scrambled = random.sample(correct_order, len(correct_order))
            st.session_state.show_q3_result = False
            st.rerun()

    with c_result:
        if len(st.session_state.q3_cards) == len(correct_order):
            if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
                st.session_state.show_q3_result = True
                st.rerun()
        else:
            st.info(f"{len(st.session_state.q3_cards)} / {len(correct_order)} 선택 완료")

    if st.session_state.get("show_q3_result"):
        all_correct = True

        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]:
                st.success(f"Step {i + 1}: Perfect!")
            else:
                st.error(f"Step {i + 1}: Wrong / 정답: {correct_order[i]}")
                all_correct = False

        if all_correct:
            st.balloons()
            st.success("🎉 완벽합니다!")
