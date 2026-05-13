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
# 처음 실행 시 초기값 설정
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []

def sync_data():
    """곡이 바뀔 때 퀴즈 진행도만 초기화 (탭은 유지)"""
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

# 곡 선택 selectbox
song_choice = st.selectbox("", song_options, index=song_options.index(st.session_state.selected_song), label_visibility="collapsed")

# 곡이 바뀌었을 때만 데이터 동기화 (탭 상태 'current_tab'은 건드리지 않음)
if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    sync_data()
    st.rerun()

# 탭 메뉴 (라디오 버튼이 세션 상태와 연동됨)
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab # 현재 탭 저장

# -------------------------
# 곡별 데이터 설정 (배경 설명 강화)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 억압된 자아의 화려한 해방</h3>
    <p>이 곡은 디즈니 애니메이션 <b>'겨울왕국(Frozen)'</b>의 절정 부분에서 엘사가 자신의 마법 능력을 숨기며 살아야 했던 과거의 굴레를 벗어던질 때 부르는 노래입니다.</p>
    <ul>
        <li><b>심리적 배경:</b> 엘사는 타인의 시선과 사회적 기대(Be the good girl) 때문에 본모습을 감추고 고립(Isolation)을 택했으나, 결국 자신의 능력을 받아들이며 진정한 자유를 선언합니다.</li>
        <li><b>언어적 포인트:</b> 'Let it go'는 '내버려 두다', '다 잊어버리다', '해방시키다' 등 중의적인 의미로 쓰이며, 억눌린 감정의 폭발을 표현합니다.</li>
        <li><b>메시지:</b> 완벽해야 한다는 강박에서 벗어나 불완전한 자신이라도 당당하게 드러내자는 현대적인 자아 존중의 메시지를 담고 있습니다.</li>
    </ul>
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
    questions = [("1. 엘사의 현재 심경은?", ["해방감", "공포", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"), ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 추운 날씨", "겨울 왕국"], "사회적 시선"), ("4. 'Good girl'은 누구의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회"), ("5. 'Isolation'의 의미는?", ["고립/격리", "함께함", "승리"], "고립/격리"), ("6. 가사에서 폭풍(Storm)은 무엇을 비유하나요?", ["내면의 억눌린 감정", "실제 기상 악화", "자연의 힘"], "내면의 억눌린 감정")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 연인을 향한 뒤늦은 고백과 치유</h3>
    <p>영국 가수 <b>아델(Adele)</b>의 복귀작이자 전 세계적인 히트곡으로, 오랜 시간이 흐른 뒤 과거의 연인에게 안부를 묻는 가슴 저린 발라드입니다.</p>
    <ul>
        <li><b>작곡 배경:</b> 아델은 이 곡이 특정 개인에 대한 노래라기보다, 자기 자신을 포함하여 과거에 상처 주었던 모든 이들에게 건네는 '작별과 사과'의 의미라고 밝혔습니다.</li>
        <li><b>정서적 특징:</b> 'The other side'라는 표현을 통해 현재와 과거, 혹은 서로 다른 삶을 살게 된 두 사람 사이의 보이지 않는 장벽을 은유합니다.</li>
        <li><b>학습 포인트:</b> 과거의 습관을 나타내는 'used to be'와 간절함을 강조하는 'a thousand times' 등 감성적인 영어 표현이 가득합니다.</li>
    </ul>
    """
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side", "반대편에서 인사해"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야")
    ]
    questions = [("1. 화자가 전화를 거는 주된 이유는?", ["사과하기 위해", "돈을 빌리기 위해", "자랑하기 위해"], "사과하기 위해"), ("2. 'a thousand times'의 속뜻은?", ["간절한 반복", "정확히 1,000번", "한 번만"], "간절한 반복"), ("3. 'California dreaming'은 무엇에 대한 비유인가요?", ["예전의 우리 모습", "여행 계획", "날씨"], "예전의 우리 모습"), ("4. 'The other side'는 무엇을 의미하나요?", ["이별 후의 현재 상태", "지구 반대편", "저세상"], "이별 후의 현재 상태"), ("5. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다", "길을 잃다"], "궁금해하다"), ("6. 노래의 전반적인 정서는?", ["그리움과 후회", "기쁨과 희망", "분노와 증오"], "그리움과 후회")]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 금지된 장벽을 넘어선 새로운 시야</h3>
    <p>애니메이션 <b>'알라딘(Aladdin)'</b>의 삽입곡으로, 성안에 갇혀 지내던 자스민 공주가 마법 양탄자를 타고 처음으로 세상을 마주하는 경이로운 순간을 담고 있습니다.</p>
    <ul>
        <li><b>주제 의식:</b> 단순히 풍경을 구경하는 것을 넘어, 타인이 정해준 삶의 궤도를 벗어나 스스로 선택하는 '주체적인 삶'과 '자유'를 상징합니다.</li>
        <li><b>가사의 묘미:</b> 'Shining, shimmering, splendid'처럼 's' 발음을 반복하여 밤하늘의 반짝임을 청각적으로 묘사한 가사가 일품입니다.</li>
        <li><b>메시지:</b> 마음의 눈을 뜨면(Open your eyes) 지금까지 알지 못했던 완전히 새로운 세상이 우리를 기다리고 있다는 희망을 줍니다.</li>
    </ul>
    """
    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 어른거리며 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"),
        ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠")
    ]
    questions = [("1. 'Crystal clear'의 문맥상 의미는?", ["아주 명확한", "유리처럼 딱딱한", "차가운"], "아주 명확한"), ("2. 노래의 핵심 주제는?", ["자유와 새로운 시각", "성안에서의 안전", "마법 양탄자 수리"], "자유와 새로운 시각"), ("3. 'Splendid'의 뜻은?", ["화려한/훌륭한", "평범한", "어두운"], "화려한/훌륭한"), ("4. 알라딘이 공주에게 묻는 '마음의 결정'은 무엇을 뜻하나?", ["주체적인 삶", "결혼 결정", "외출 허락"], "주체적인 삶"), ("5. 'Wonder by wonder'는 어떤 느낌을 주나요?", ["끊임없는 감동", "지루함", "공포"], "끊임없는 감동"), ("6. 'Fantastic point of view'는 무엇을 의미하나요?", ["환상적인 시야", "가짜 뉴스", "어지러움"], "환상적인 시야")]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 변치 않는 연대와 지지의 찬가</h3>
    <p>1961년 <b>벤 E. 킹(Ben E. King)</b>이 발표한 이 곡은 반세기가 넘도록 사랑받는 소울의 고전이며, 동명의 영화로도 유명합니다.</p>
    <ul>
        <li><b>상징적 비유:</b> '하늘이 무너지고(Sky tumble and fall)', '산이 바다로 흘러내려도(Mountains crumble to the sea)' 같은 극단적인 자연재해를 가정하여, 그 어떤 시련 앞에서도 굴하지 않는 신뢰를 표현합니다.</li>
        <li><b>역사적 가치:</b> 흑인 인권 운동 당시 연대와 화합을 상징하는 노래로도 불렸으며, 현대에 와서는 우정과 사랑의 보편적 가치를 전달합니다.</li>
        <li><b>언어적 포인트:</b> 'Stand by someone'은 물리적으로 곁에 서 있다는 뜻을 넘어 '지지하다', '편을 들다'라는 중요한 숙어로 쓰입니다.</li>
    </ul>
    """
    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 찾아오고 세상이 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid, oh, I won't be afraid", "난 두렵지 않을 거예요, 정말 두렵지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("So darling, darling, stand by me", "그러니 그대여, 내 곁에 서 주세요"),
        ("Oh, stand by me", "내 곁에 있어 줘요"),
        ("Oh, stand, stand by me, stand by me", "내 곁에, 내 곁에 서 주세요"),
        ("If the sky that we look upon should tumble and fall", "우리가 바라보는 저 하늘이 무너져 내리고"),
        ("Or the mountains should crumble to the sea", "저 산들이 부서져 바다로 흘러내린다 해도"),
        ("I won't cry, I won't cry, no, I won't shed a tear", "난 울지 않을 거예요, 울지 않아요, 눈물 한 방울 흘리지 않겠어요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요")
    ]
    questions = [("1. 'The land is dark'가 의미하는 상황은?", ["절망적인 상황", "정전된 상태", "밤잠을 자는 시간"], "절망적인 상황"), ("2. 'Shed a tear'의 올바른 의미는?", ["눈물을 흘리다", "미소를 짓다", "소리를 지르다"], "눈물을 흘리다"), ("3. 가사 중 '하늘이 무너지는 것'은 무엇을 비유하나요?", ["거대한 시련이나 재앙", "자연 현상", "기상 악화"], "거대한 시련이나 재앙"), ("4. 화자가 두려움을 극복할 수 있는 유일한 조건은?", ["상대방이 곁에 있어 주는 것", "날이 밝아오는 것", "산에 올라가는 것"], "상대방이 곁에 있어 주는 것"), ("5. 'Crumble'의 뜻으로 가장 적절한 것은?", ["바스러지다/무너지다", "단단해지다", "솟아오르다"], "바스러지다/무너지다"), ("6. 이 노래의 핵심 메시지는 무엇인가요?", ["우정과 연대의 소중함", "자연 보호의 필요성", "이별의 아픔"], "우정과 연대의 소중함")]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임이 남긴 쓸쓸한 공허함</h3>
    <p>재즈 보컬리스트 <b>노라 존스(Norah Jones)</b>의 데뷔 앨범 타이틀곡으로, 8개의 그래미 상을 휩쓴 현대 재즈의 명곡입니다.</p>
    <ul>
        <li><b>정서적 배경:</b> 분명히 가고 싶었지만 용기가 부족해서, 혹은 알 수 없는 망설임 때문에 소중한 사람을 놓쳐버린 후의 허무함을 노래합니다.</li>
        <li><b>음악적 특징:</b> 노라 존스의 나른하고 차분한 목소리는 후회로 가득 찬 마음을 절제된 감정으로 표현하며 감동을 더합니다.</li>
        <li><b>비유적 표현:</b> 'Empty as a drum(드럼처럼 텅 빈)', 'Drenched in wine(와인에 흠뻑 젖은)' 등 마음의 상태를 사물과 현상에 빗대어 깊은 울림을 줍니다.</li>
    </ul>
    """
    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 올 때 난 멀리 날아가 버리고 싶었죠"),
        ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"),
        ("I feel as empty as a drum, I don't know why I didn't come", "텅 빈 드럼처럼 공허해요")
    ]
    questions = [("1. 이 노래의 지배적인 감정은?", ["후회와 아쉬움", "분노와 원망", "기쁨"], "후회와 아쉬움"), ("2. 'Drenched in wine'은 무엇을 비유하나?", ["슬픔에 젖은 마음", "즐거운 파티", "갈증"], "슬픔에 젖은 마음"), ("3. 'A bag of bones'는 어떤 상태인가?", ["무기력하고 야윈 상태", "건강한 상태", "무거운 상태"], "무기력하고 야윈 상태"), ("4. 화자가 약속에 가지 않은 진짜 이유는?", ["망설임과 두려움", "길을 잃어서", "약속을 잊어서"], "망설임과 두려움"), ("5. 'Empty as a drum'은 무엇을 강조하나?", ["내면의 공허함", "시끄러운 소리", "음악적 재능"], "내면의 공허함"), ("6. 가사가 계속 반복되는 이유는?", ["자책하는 마음의 강조", "단어 암기", "시간 때우기"], "자책하는 마음의 강조")]

# -------------------------
# 가사 가공 및 순서 섞기
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
# 화면 출력
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: st.video(video_url)

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
            if i < len(correct_order) and user_s == correct_order[i]: st.success(f"Step {i+1}: Perfect!")
            else:
                st.error(f"Step {i+1}: Wrong (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
