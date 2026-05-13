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
        border: 1px solid #cbd5e1; line-height: 1.8; margin-bottom: 25px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 3px solid #6366f1; padding-bottom: 12px; margin-top: 0; }
    .info-box p { margin-bottom: 15px; font-size: 1.05rem; }
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
if 'selected_song' not in st.session_state: 
    st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'current_tab' not in st.session_state: 
    st.session_state.current_tab = "🎬 배경 학습"
if 'submitted_step2' not in st.session_state: 
    st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: 
    st.session_state.q3_cards = []

# -------------------------
# 상단 곡 선택 메뉴
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]

song_choice = st.selectbox("👉 학습할 노래를 선택하세요", song_options, index=song_options.index(st.session_state.selected_song))

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state: del st.session_state.scrambled
    st.rerun()

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("학습 단계", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True)
st.session_state.current_tab = selected_tab

# -------------------------
# 곡별 데이터 설정 (줄거리 및 배경 대폭 강화)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 완벽해야 했던 여왕의 화려한 탈출</h3>
    <p><b>[줄거리]</b> 아렌델 왕국의 후계자 엘사는 태어날 때부터 모든 것을 얼려버리는 마법 능력을 가지고 있었습니다. 어린 시절 사고로 동생 안나를 다치게 한 후, 엘사는 부모님의 엄격한 훈육 아래 자신의 능력을 부정하고 감추며 살아왔습니다. 하지만 대관식 날, 예기치 못한 사고로 능력이 세상에 드러나게 되고, 사람들의 겁에 질린 시선을 뒤로한 채 엘사는 북쪽 산으로 도망칩니다.</p>
    <p><b>[곡의 의미]</b> 이 노래는 엘사가 아무도 없는 설산에서 비로소 '숨길 필요가 없다'는 사실을 깨달으며 부르는 곡입니다. 가사의 <b>'Conceal, don't feel'</b>은 그녀가 평생을 지켜온 억압의 가훈이었으나, 노래가 진행되며 그녀는 성을 짓고 옷을 바꾸며 <b>'Let it go(다 잊어버려, 놓아버려)'</b>라고 선언합니다. 완벽한 여왕이 아닌, 자유로운 자아로서의 첫발을 내딛는 순간입니다.</p>
    """
    lyrics_raw = [("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나고"), ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"), ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"), ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"), ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"), ("Be the good girl you always have to be", "늘 그랬듯 착한 소녀가 되어야 해"), ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 말고, 모르게 해"), ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어")]
    questions = [("1. 엘사의 현재 심경은?", ["해방감", "공포", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"), ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 추운 날씨", "겨울 왕국"], "사회적 시선"), ("4. 'Good girl'은 누구의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회"), ("5. 'Isolation'의 의미는?", ["고립/격리", "함께함", "승리"], "고립/격리"), ("6. 가사에서 폭풍(Storm)은 무엇을 비유하나요?", ["내면의 억눌린 감정", "실제 기상 악화", "자연의 힘"], "내면의 억눌린 감정")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 나, 그리고 너에게 건네는 뒤늦은 안부</h3>
    <p><b>[줄거리]</b> 노래의 화자는 이별 후 수년이 지난 시점에서 과거의 연인에게 전화를 겁니다. 하지만 상대방은 전화를 받지 않거나, 화자가 기대하는 대답을 들려주지 않습니다. 화자는 여전히 과거의 추억과 미안함 속에 살고 있지만, 시간은 무심하게 흘러버렸음을 깨닫습니다.</p>
    <p><b>[곡의 의미]</b> 아델은 이 곡이 단순히 헤어진 연인만을 향한 것이 아니라, 연락이 끊긴 친구들, 소원해진 가족, 그리고 무엇보다 <b>'어리고 서툴렀던 과거의 자신'</b>에게 건네는 화해의 메시지라고 설명합니다. <b>'Hello from the other side'</b>는 물리적인 거리가 아닌, 돌이킬 수 없는 시간의 강을 건너온 현재의 위치에서 보내는 간절한 외침입니다.</p>
    """
    lyrics_raw = [("Hello, it's me", "안녕, 나야"), ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"), ("Hello, can you hear me?", "여보세요, 내 말 들리니?"), ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"), ("Hello from the other side", "반대편에서 인사해"), ("I must've called a thousand times", "수천 번은 전화했을 거야")]
    questions = [("1. 화자가 전화를 거는 주된 이유는?", ["사과하기 위해", "돈을 빌리기 위해", "자랑하기 위해"], "사과하기 위해"), ("2. 'a thousand times'의 속뜻은?", ["간절한 반복", "정확히 1,000번", "한 번만"], "간절한 반복"), ("3. 'California dreaming'은 무엇에 대한 비유인가요?", ["예전의 우리 모습", "여행 계획", "날씨"], "예전의 우리 모습"), ("4. 'The other side'는 무엇을 의미하나요?", ["이별 후의 현재 상태", "지구 반대편", "저세상"], "이별 후의 현재 상태"), ("5. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다", "길을 잃다"], "궁금해하다"), ("6. 노래의 전반적인 정서는?", ["그리움과 후회", "기쁨과 희망", "분노와 증오"], "그리움과 후회")]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 성벽을 넘어 처음 마주한 진짜 세상</h3>
    <p><b>[줄거리]</b> 아그라바 왕국의 공주 자스민은 성안에서의 안락하지만 통제된 삶에 답답함을 느낍니다. 왕실의 법도에 따라 억지로 결혼해야 하는 처지에 놓인 그녀 앞에, 마법사로 변장한 가난한 청년 알라딘이 마법 양탄자를 타고 나타납니다. 그는 그녀에게 "나를 믿느냐"고 묻고, 두 사람은 성벽 밖 넓은 세상을 향해 날아오릅니다.</p>
    <p><b>[곡의 의미]</b> 이 곡은 두 사람이 구름 위를 날며 이집트의 피라미드와 그리스의 신전 등을 목격할 때 부르는 듀엣곡입니다. 여기서 <b>'Whole New World'</b>는 단순히 아름다운 풍경만을 의미하지 않습니다. 누군가의 딸, 누군가의 아내가 아닌 <b>'나 자신'</b>으로 살 수 있는 자유로운 세상을 의미합니다. 자스민이 알라딘에게 마음을 여는 결정적인 계기가 되는 곡입니다.</p>
    """
    lyrics_raw = [("I can show you the world", "당신에게 세상을 보여줄 수 있어요"), ("Shining, shimmering, splendid", "빛나고 어른거리며 화려한 세상을요"), ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"), ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"), ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"), ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠")]
    questions = [("1. 'Crystal clear'의 문맥상 의미는?", ["아주 명확한", "유리처럼 딱딱한", "차가운"], "아주 명확한"), ("2. 노래의 핵심 주제는?", ["자유와 새로운 시각", "성안에서의 안전", "마법 양탄자 수리"], "자유와 새로운 시각"), ("3. 'Splendid'의 뜻은?", ["화려한/훌륭한", "평범한", "어두운"], "화려한/훌륭한"), ("4. 알라딘이 공주에게 묻는 '마음의 결정'은 무엇을 뜻하나?", ["주체적인 삶", "결혼 결정", "외출 허락"], "주체적인 삶"), ("5. 'Wonder by wonder'는 어떤 느낌을 주나요?", ["끊임없는 감동", "지루함", "공포"], "끊임없는 감동"), ("6. 'Fantastic point of view'는 무엇을 의미하나요?", ["환상적인 시야", "가짜 뉴스", "어지러움"], "환상적인 시야")]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 어떤 재앙 앞에서도 무너지지 않는 곁</h3>
    <p><b>[줄거리/배경]</b> 벤 E. 킹의 이 곡은 1961년 발표된 이후, 1986년 동명의 영화 '스탠 바이 미'의 주제곡으로 쓰이며 다시 한번 큰 사랑을 받았습니다. 영화는 네 명의 어린 소년이 기찻길을 따라 모험을 떠나며 겪는 우정과 성장을 다룹니다. 인생의 가장 순수했던 시절, 서로가 서로의 버팀목이 되어주었던 기억을 관통하는 노래입니다.</p>
    <p><b>[곡의 의미]</b> 가사 속 <b>'The land is dark'</b>나 <b>'Sky tumble and fall'</b>은 우리가 인생에서 마주할 수 있는 거대한 불행이나 공포를 상징합니다. 화자는 세상을 덮칠 것 같은 어둠 앞에서도 오직 당신이 곁에 있다면(Stand by me) 절대 울지 않고 버틸 수 있다고 노래합니다. 사랑을 넘어선 인간적인 신뢰와 연대의 힘을 보여주는 최고의 명곡입니다.</p>
    """
    lyrics_raw = [("When the night has come and the land is dark", "밤이 찾아오고 세상이 어두워질 때"), ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"), ("No, I won't be afraid, oh, I won't be afraid", "난 두렵지 않을 거예요"), ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"), ("So darling, darling, stand by me", "그러니 그대여, 내 곁에 서 주세요"), ("Oh, stand by me", "내 곁에 있어 줘요"), ("Oh, stand, stand by me, stand by me", "내 곁에, 내 곁에 서 주세요"), ("If the sky that we look upon should tumble and fall", "우리가 바라보는 저 하늘이 무너져 내리고"), ("Or the mountains should crumble to the sea", "저 산들이 부서져 바다로 흘러내린다 해도"), ("I won't cry, I won't cry, no, I won't shed a tear", "난 울지 않을 거예요, 눈물 한 방울 흘리지 않겠어요"), ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요")]
    questions = [("1. 'The land is dark'가 의미하는 상황은?", ["절망적인 상황", "정전된 상태", "밤잠을 자는 시간"], "절망적인 상황"), ("2. 'Shed a tear'의 올바른 의미는?", ["눈물을 흘리다", "미소를 짓다", "소리를 지르다"], "눈물을 흘리다"), ("3. 가사 중 '하늘이 무너지는 것'은 무엇을 비유하나요?", ["거대한 시련이나 재앙", "자연 현상", "기상 악화"], "거대한 시련이나 재앙"), ("4. 화자가 두려움을 극복할 수 있는 유일한 조건은?", ["상대방이 곁에 있어 주는 것", "날이 밝아오는 것", "산에 올라가는 것"], "상대방이 곁에 있어 주는 것"), ("5. 'Crumble'의 뜻으로 가장 적절한 것은?", ["바스러지다/무너지다", "단단해지다", "솟아오르다"], "바스러지다/무너지다"), ("6. 이 노래의 핵심 메시지는 무엇인가요?", ["우정과 연대의 소중함", "자연 보호의 필요성", "이별의 아픔"], "우정과 연대의 소중함")]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 가지 못한 길에 대한 고요한 후회</h3>
    <p><b>[줄거리/상황]</b> 노라 존스의 나른한 목소리가 돋보이는 이 곡은, 누군가와의 약속 혹은 관계를 앞두고 '가지 않기로' 결정한 뒤 찾아오는 후회를 담고 있습니다. 화자는 새벽 해가 뜰 때까지 깨어있으며, 왜 자신이 그곳에 가지 않았는지 스스로에게 묻지만 명확한 답을 찾지 못합니다.</p>
    <p><b>[곡의 의미]</b> <b>'I don't know why I didn't come'</b>이라는 반복되는 구절은 인간의 복잡한 심리를 대변합니다. 두려움 때문이었는지, 혹은 귀찮음이었는지 알 수 없지만, 그 한 번의 망설임 때문에 소중한 인연을 놓치고 맙니다. <b>'Empty as a drum'</b>이라는 표현처럼, 북의 속이 텅 비어 있듯 화자의 내면도 공허함만 남았음을 강조하는 노래입니다.</p>
    """
    lyrics_raw = [("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"), ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"), ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"), ("When I saw the break of day, I wished that I could fly away", "새벽이 올 때 난 멀리 날아가 버리고 싶었죠"), ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"), ("I feel as empty as a drum, I don't know why I didn't come", "텅 빈 드럼처럼 공허해요")]
    questions = [("1. 이 노래의 지배적인 감정은?", ["후회와 아쉬움", "분노와 원망", "기쁨"], "후회와 아쉬움"), ("2. 'Drenched in wine'은 무엇을 비유하나?", ["슬픔에 젖은 마음", "즐거운 파티", "갈증"], "슬픔에 젖은 마음"), ("3. 'A bag of bones'는 어떤 상태인가?", ["무기력하고 야윈 상태", "건강한 상태", "무거운 상태"], "무기력하고 야윈 상태"), ("4. 화자가 약속에 가지 않은 진짜 이유는?", ["망설임과 두려움", "길을 잃어서", "약속을 잊어서"], "망설임과 두려움"), ("5. 'Empty as a drum'은 무엇을 강조하나?", ["내면의 공허함", "시끄러운 소리", "음악적 재능"], "내면의 공허함"), ("6. 가사가 계속 반복되는 이유는?", ["자책하는 마음의 강조", "단어 암기", "시간 때우기"], "자책하는 마음의 강조")]

# -------------------------
# 가사 데이터 가공
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
# 화면 출력 (메인 로직)
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
    # 컨테이너를 사용하여 위젯 상태가 변경되어도 뷰가 튕기는 현상 최소화
    puzzle_container = st.container()
    with puzzle_container:
        st.subheader("🧩 가사 순서대로 클릭하세요 (a, b, c... 순서)")
        
        # 버튼 영역
        b_cols = st.columns(2)
        for i, text in enumerate(st.session_state.scrambled):
            is_sel = text in st.session_state.q3_cards
            col_idx = 0 if i % 2 == 0 else 1
            # 고유한 키 값을 사용하여 버튼 클릭 시 튕김 방지
            if b_cols[col_idx].button(text, key=f"btn_{song_choice}_{i}", use_container_width=True, disabled=is_sel):
                st.session_state.q3_cards.append(text)
                st.rerun()
        
        st.divider()
        st.write("📝 **내가 배열한 순서:**")
        
        # 선택된 카드 리스트 표시
        for idx, card in enumerate(st.session_state.q3_cards):
            c1, c2 = st.columns([0.9, 0.1])
            c1.info(f"{idx+1}: {card}")
            if c2.button("🗑️", key=f"del_{song_choice}_{idx}"):
                st.session_state.q3_cards.pop(idx)
                st.rerun()
        
        # 결과 확인 버튼
        if len(st.session_state.q3_cards) == len(correct_order):
            if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True, key=f"res_btn_{song_choice}"):
                st.session_state.show_q3_result = True
                st.rerun()
        
        if st.session_state.get('show_q3_result'):
            all_correct = True
            for i, user_s in enumerate(st.session_state.q3_cards):
                if i < len(correct_order) and user_s == correct_order[i]:
                    st.success(f"Line {i+1}: Perfect!")
                else:
                    st.error(f"Line {i+1}: Wrong (정답: {correct_order[i]})")
                    all_correct = False
            if all_correct:
                st.balloons()
