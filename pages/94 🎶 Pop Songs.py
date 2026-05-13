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

# 탭 수동 제어
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

# -------------------------
# 곡별 데이터 설정
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go: 억압된 자아의 해방</h3><p>엘사가 타인의 시선에서 벗어나 진정한 자유를 찾는 과정을 담고 있습니다.</p>"
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
    bg_content = "<h3>☎️ Hello: 과거를 향한 뒤늦은 안부</h3><p>미안함과 그리움을 담아 과거의 연인에게 건네는 메시지입니다.</p>"
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
    bg_content = "<h3>✨ A Whole New World: 금지된 장벽을 넘는 자유</h3><p>새로운 시야와 자유에 대한 노래입니다.</p>"
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
    bg_content = "<h3>🤝 Stand By Me: 신뢰와 연대의 힘</h3><p>이 곡은 1961년 발표된 벤 E. 킹의 명곡으로, 어떤 시련 속에서도 곁을 지켜주는 사람이 있다면 두려울 것이 없다는 믿음을 노래합니다.</p>"
    # 1절 전체 가사 및 코러스 포함
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
    questions = [
        ("1. 'The land is dark'가 의미하는 상황은?", ["절망적인 상황", "정전된 상태", "밤잠을 자는 시간"], "절망적인 상황"),
        ("2. 'Shed a tear'의 올바른 의미는?", ["눈물을 흘리다", "미소를 짓다", "소리를 지르다"], "눈물을 흘리다"),
        ("3. 가사 중 '하늘이 무너지는 것'은 무엇을 비유하나요?", ["거대한 시련이나 재앙", "자연 현상", "기상 악화"], "거대한 시련이나 재앙"),
        ("4. 화자가 두려움을 극복할 수 있는 유일한 조건은?", ["상대방이 곁에 있어 주는 것", "날이 밝아오는 것", "산에 올라가는 것"], "상대방이 곁에 있어 주는 것"),
        ("5. 'Crumble'의 뜻으로 가장 적절한 것은?", ["바스러지다/무너지다", "단단해지다", "솟아오르다"], "바스러지다/무너지다"),
        ("6. 이 노래의 핵심 메시지는 무엇인가요?", ["우정과 연대의 소중함", "자연 보호의 필요성", "이별의 아픔"], "우정과 연대의 소중함")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = "<h3>🍂 Don't Know Why: 망설임 끝에 놓친 사랑</h3><p>용기가 없어 다가지 못한 인연에 대한 쓸쓸한 후회입니다.</p>"
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
        st.markdown("### 🎼 Full Lyrics (Verse 1 & Chorus)")
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
