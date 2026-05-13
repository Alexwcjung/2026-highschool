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
if 'selected_song' not in st.session_state: st.session_state.selected_song = "Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    st.session_state.current_tab = "🎬 배경 학습" # 곡 변경 시 탭 초기화
    if 'scrambled' in st.session_state: del st.session_state.scrambled

# -------------------------
# 상단 곡 선택 메뉴
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)

song_options = [
    "Let It Go - Frozen OST", 
    "Hello - Adele", 
    "A Whole New World - Aladdin OST",
    "Stand By Me - Ben E. King",
    "Don't Know Why - Norah Jones"
]
song_choice = st.selectbox("", song_options, label_visibility="collapsed")

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# 탭 수동 제어 (곡 변경 시 첫 탭으로 이동하기 위함)
# -------------------------
tabs = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs, index=tabs.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

# -------------------------
# 데이터 빌드
# -------------------------
if "Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go: 억압된 자아의 폭발과 진정한 자유</h3><p><b>[심층 배경]</b> 엘사가 사회적 억압을 벗어나 자신의 능력을 인정하는 해방의 순간을 노래합니다.</p>"
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
    questions = [("1. 엘사의 심경은?", ["공포", "해방감", "분노"], "해방감"), ("2. 'Conceal'의 뜻은?", ["드러내다", "숨기다", "공격하다"], "숨기다"), ("3. 'The cold never bothered me'의 의미는?", ["감기에 안 걸린다", "시선은 상관없다", "눈이 싫다"], "시선은 상관없다")]

elif "Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello: 과거와 현재를 잇는 안부</h3><p><b>[심층 배경]</b> 과거의 연인과 자신에게 건네는 뒤늦은 사과와 안부를 담은 곡입니다.</p>"
    full_lyrics = [
        ("Hello, it's me. I was wondering if after all these years you'd like to meet", "안녕, 나야. 이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me? I'm in California dreaming about who we used to be", "여보세요, 내 말 들리니? 난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done", "내 모든 일에 대해 미안하다고 말하려고 말야"),
        ("But when I call, you never seem to be home", "하지만 내가 전화할 때마다 넌 절대 집에 없는 것 같아")
    ]
    questions = [("1. 전화의 목적은?", ["부탁", "사과", "자랑"], "사과"), ("2. 'a thousand times'의 의미는?", ["정확히 1000번", "간절함", "실수"], "간절함")]

elif "Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임 끝에 놓쳐버린 사랑의 여운</h3>
    <p><b>[심층 배경]</b> 잡을 수 있었던 인연을 망설임과 두려움 때문에 놓쳐버린 후 느끼는 공허함을 담고 있습니다.</p>
    <p><b>[스토리텔링]</b> 해가 뜰 때까지 기다렸지만 정작 약속 장소에는 나가지 못한 화자. 모래 위에 무릎을 꿇고 눈물을 훔치는 그녀의 모습은 후회로 가득 차 있습니다.</p>
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
        ("1. 이 노래의 지배적인 정서는 무엇인가요?", ["분노와 원망", "후회와 아쉬움", "기대와 설렘"], "후회와 아쉬움"),
        ("2. 'Drenched in wine'은 어떤 상태를 비유하나요?", ["파티를 즐기는 모습", "슬픔에 깊이 잠긴 마음", "포도 농사를 짓는 상황"], "슬픔에 깊이 잠긴 마음"),
        ("3. 'A bag of bones'가 의미하는 화자의 모습은?", ["기운이 넘치는 상태", "상실감으로 야위고 무기력한 상태", "가방을 들고 여행 가는 상태"], "상실감으로 야위고 무기력한 상태"),
        ("4. 화자가 'house of fun'에 가지 않은 이유는 무엇으로 추측되나요?", ["길을 잃어서", "마음의 망설임과 두려움", "상대방이 오지 말라고 해서"], "마음의 망설임과 두려움"),
        ("5. 'Empty as a drum'은 무엇을 강조하기 위한 표현인가요?", ["드럼 소리의 웅장함", "지독한 내면의 공허함", "음악에 대한 열정"], "지독한 내면의 공허함"),
        ("6. 'I don't know why I didn't come'이라는 반복구의 효과는?", ["자신의 행동에 대한 확신", "이유를 알 수 없는 답답함과 자책", "상대방을 향한 질문"], "이유를 알 수 없는 답답함과 자책")
    ]
else: # A Whole New World, Stand By Me 등 생략 (구조는 동일)
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h3>배경 학습 내용</h3>"
    full_lyrics = [("Lyrics English", "가사 한국어")]
    questions = [("Question?", ["A", "B"], "A")]

# -------------------------
# 화면 출력 제어
# -------------------------
correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

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
