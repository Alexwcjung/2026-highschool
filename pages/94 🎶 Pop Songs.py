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
    .eng-line { font-size: 1.15rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.95rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. 세션 상태 초기화 (핵심: 위젯과 직접 연결할 key 설정)
# -------------------------
if 'selected_song' not in st.session_state:
    st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"
if 'q3_cards' not in st.session_state:
    st.session_state.q3_cards = []
if 'submitted_step2' not in st.session_state:
    st.session_state.submitted_step2 = False

# -------------------------
# 3. 사이드바/상단 컨트롤 (곡 선택 및 탭)
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)

song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]

# 곡 선택 (on_change를 사용하여 즉시 반영)
def on_song_change():
    st.session_state.q3_cards = []
    st.session_state.submitted_step2 = False
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state: del st.session_state.scrambled

song_choice = st.selectbox("👉 학습할 노래를 선택하세요", song_options, 
                           index=song_options.index(st.session_state.selected_song),
                           on_change=on_song_change, key="selected_song")

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
# 탭 메뉴 (key를 지정하여 세션 상태와 완전 동기화)
selected_tab = st.radio("학습 단계", tabs_list, horizontal=True, key="current_tab")

# -------------------------
# 4. 곡별 데이터 설정 (풍부한 줄거리 및 서사)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 모든 속박을 얼려버리는 해방의 서사</h3>
    <p><b>[줄거리]</b> 아렌델의 장녀 엘사는 손에 닿는 모든 것을 얼리는 저주 같은 능력을 타고났습니다. 동생 안나를 다치게 한 트라우마로 10년 넘게 방 안에 갇혀 "숨기고, 느끼지 마라(Conceal, don't feel)"는 부모님의 가르침 아래 스스로를 억압합니다. 하지만 대관식 날 정체가 탄로나고, 그녀는 홀로 설산으로 도망쳐 자신만의 얼음 성을 짓기 시작합니다.</p>
    <p><b>[곡의 깊이]</b> 이 곡은 엘사가 '착한 아이'라는 사회적 가면을 벗어던지는 심리적 임계점을 상징합니다. 산으로 올라가며 부르는 가사는 처음엔 두려움에 떨지만, 후반부로 갈수록 "추위는 더 이상 나를 괴롭히지 못한다"며 자신의 결점을 최고의 능력으로 승화시키는 당당함을 보여줍니다. 단순한 주제가를 넘어 전 세계적인 '자아 해방'의 아이콘이 된 곡입니다.</p>
    """
    lyrics_raw = [("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나고"), ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"), ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"), ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"), ("Don't let them in, don't let them see", "그들을 들여보내지 마, 보여주지 마"), ("Be the good girl you always have to be", "늘 그랬듯 착한 소녀가 되어야 해"), ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 말고, 모르게 해"), ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어")]
    questions = [("1. 엘사의 현재 심경은?", ["해방감", "공포", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다", "나누다"], "숨기다"), ("3. 'The cold'가 상징하는 것은?", ["사회적 시선", "실제 추운 날씨", "겨울 왕국"], "사회적 시선"), ("4. 'Good girl'은 누구의 기대를 의미하나요?", ["타인과 사회", "엘사 자신", "안나"], "타인과 사회")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 모든 인연에게 건네는 통곡의 안부</h3>
    <p><b>[줄거리]</b> 노래는 낡은 전화기로 누군가에게 전화를 거는 주인공의 모습으로 시작됩니다. 이별한 지 수년이 지났지만, 화자는 여전히 과거의 상처와 미안함에서 완전히 벗어나지 못했습니다. 그녀는 상대방에게 사과하고 싶어 수천 번 전화를 걸지만, 정작 상대방은 이제 그녀의 목소리를 기억하지 못하거나 더 이상 안부를 궁금해하지 않습니다.</p>
    <p><b>[곡의 깊이]</b> 아델은 이 곡이 연인뿐만 아니라 나이가 들며 소홀해진 친구들, 그리고 '20대의 아델' 자신에게 건네는 작별 인사라고 말했습니다. 'The other side'는 단지 지리적인 반대편이 아니라, '이미 어른이 되어버린 현재'와 '서툴렀던 과거' 사이의 건널 수 없는 강을 의미합니다. 상실을 인정하고 비로소 작별을 고하는 성숙한 치유의 과정이 담겨 있습니다.</p>
    """
    lyrics_raw = [("Hello, it's me", "안녕, 나야"), ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"), ("Hello, can you hear me?", "여보세요, 내 말 들리니?"), ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"), ("Hello from the other side", "반대편에서 인사해"), ("I must've called a thousand times", "수천 번은 전화했을 거야")]
    questions = [("1. 화자가 전화를 거는 주된 이유는?", ["사과하기 위해", "돈을 빌리기 위해", "자랑하기 위해"], "사과하기 위해"), ("2. 'a thousand times'의 속뜻은?", ["간절한 반복", "정확히 1,000번", "한 번만"], "간절한 반복")]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 금기된 담장을 넘어선 자유의 비행</h3>
    <p><b>[줄거리]</b> 아그라바 왕국의 자스민 공주는 법도에 얽매여 성 밖으로 나갈 수 없는 처지입니다. 가난한 좀도둑이었지만 램프의 요정 지니를 만나 왕자로 변신한 알라딘은 마법 양탄자를 타고 그녀의 창가에 나타납니다. "나를 믿느냐"는 그의 물음에 자스민은 손을 잡고, 두 사람은 난생처음 보는 밤하늘과 세계의 절경을 마주하게 됩니다.</p>
    <p><b>[곡의 깊이]</b> 이 곡은 단순한 로맨틱 듀엣을 넘어 '계급'과 '편견'의 벽을 허무는 순간을 노래합니다. 자스민에게 '새로운 세상'은 아름다운 풍경이기도 하지만, 자신이 스스로 인생을 결정할 수 있는 '주체적인 삶'을 뜻합니다. 가사 속 'Fantastic point of view'는 사랑하는 사람과 함께할 때 비로소 열리는 새로운 가치관과 시야를 의미합니다.</p>
    """
    lyrics_raw = [("I can show you the world", "당신에게 세상을 보여줄 수 있어요"), ("Shining, shimmering, splendid", "빛나고 어른거리며 화려한 세상을요"), ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"), ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"), ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"), ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠")]
    questions = [("1. 노래의 핵심 주제는?", ["자유와 새로운 시각", "성안에서의 안전", "마법 양탄자 수리"], "자유와 새로운 시각"), ("2. 'Splendid'의 뜻은?", ["화려한/훌륭한", "평범한", "어두운"], "화려한/훌륭한")]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 세상이 무너져도 변치 않을 곁의 약속</h3>
    <p><b>[줄거리/배경]</b> 벤 E. 킹의 소울 명곡이자 동명의 성장 영화 테마곡입니다. 영화는 죽은 친구의 시신을 찾아 떠나는 네 소년의 짧지만 강렬한 여행을 다룹니다. 그 과정에서 소년들은 가정 폭력, 가난, 미래에 대한 불안을 마주하지만 서로가 곁에 있다는 사실만으로 공포를 극복해 나갑니다.</p>
    <p><b>[곡의 깊이]</b> 가사는 '하늘이 무너지고 산이 바다로 흘러내리는' 종말론적인 공포를 가정합니다. 하지만 화자는 "당신이 내 곁에 서 있다면 울지 않겠다"고 단언합니다. 여기서 'Stand by me'는 단순히 옆에 있는 행위가 아니라, 비바람이 몰아칠 때 함께 맞아주는 숭고한 '연대'를 뜻합니다. 인종 차별과 혼란의 시기였던 60년대 미국 사회에 큰 울림을 준 평화와 우정의 찬가입니다.</p>
    """
    lyrics_raw = [("When the night has come and the land is dark", "밤이 찾아오고 세상이 어두워질 때"), ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"), ("No, I won't be afraid, oh, I won't be afraid", "난 두렵지 않을 거예요"), ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"), ("So darling, darling, stand by me", "그러니 그대여, 내 곁에 서 주세요")]
    questions = [("1. 'The land is dark'가 의미하는 상황은?", ["절망적인 상황", "정전된 상태", "밤잠을 자는 시간"], "절망적인 상황"), ("2. 화자가 두려움을 극복할 수 있는 조건은?", ["상대방이 곁에 있어 주는 것", "날이 밝아오는 것", "산에 올라가는 것"], "상대방이 곁에 있어 주는 것")]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임의 파도가 휩쓸고 간 빈자리</h3>
    <p><b>[줄거리]</b> 노라 존스의 이 곡은 아주 미묘한 후회를 다룹니다. 어떤 장소에 가기로 했거나, 누군가에게 진심을 전하기로 했던 약속의 밤, 화자는 알 수 없는 이유로 끝내 발걸음을 옮기지 않았습니다. 다음 날 아침, 해가 떠오르는 것을 보며 화자는 가지 못한 길과 놓쳐버린 사람에 대한 쓸쓸함을 나른하게 고백합니다.</p>
    <p><b>[곡의 깊이]</b> 인간은 가끔 왜 그런 선택을 했는지 스스로도 모를 때가 있습니다. 'I don't know why'라는 가사가 반복되는 것은 그 복잡한 자기 자책을 의미합니다. 'Empty as a drum'은 사랑이 떠나간 뒤의 허탈함을 소리통이 빈 악기인 드럼에 비유한 명표현입니다. 재즈 특유의 절제된 선율 속에 숨겨진 짙은 고독과 아쉬움을 담은 현대의 고전입니다.</p>
    """
    lyrics_raw = [("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"), ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"), ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"), ("When I saw the break of day, I wished that I could fly away", "새벽이 올 때 난 멀리 날아가 버리고 싶었죠")]
    questions = [("1. 이 노래의 지배적인 감정은?", ["후회와 아쉬움", "분노와 원망", "기쁨"], "후회와 아쉬움"), ("2. 'Empty as a drum'은 무엇을 강조하나?", ["내면의 공허함", "시끄러운 소리", "음악적 재능"], "내면의 공허함")]

# -------------------------
# 5. 가사 가공 (순서 섞기 유지)
# -------------------------
alphabet = list(string.ascii_lowercase)
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in full_lyrics]

if 'scrambled' not in st.session_state or st.session_state.get('last_song_val') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song_val = song_choice

# -------------------------
# 6. 탭별 출력 로직
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
                st.radio(q, opts, index=None, key=f"q_sel_{i}")
            if st.form_submit_button("채점하기"):
                st.session_state.submitted_step2 = True
        
        if st.session_state.submitted_step2:
            st.info("정답을 확인하며 다시 읽어보세요!")

    with col_l:
        st.markdown("### 🎼 Full Lyrics")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

elif selected_tab == "🧩 순서 배열":
    st.subheader("🧩 가사 순서대로 클릭하세요")
    
    # 클릭 시 화면 튕김을 방지하기 위해 컨테이너 내부에서만 동작
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        # 버튼 클릭 시 세션에 즉시 추가 (st.rerun 없이도 Streamlit 위젯 키로 상태 유지)
        if (b_cols[i % 2]).button(text, key=f"btn_{song_choice}_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()

    st.divider()
    st.write("📝 **배열 중인 가사:**")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 결과 확인", type="primary", use_container_width=True):
            all_correct = True
            for i, user_s in enumerate(st.session_state.q3_cards):
                if user_s == correct_order[i]: st.success(f"{i+1}번 문장: 정답!")
                else:
                    st.error(f"{i+1}번 문장: 오답 (정답: {correct_order[i]})")
                    all_correct = False
            if all_correct: st.balloons()
