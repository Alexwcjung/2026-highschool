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
        background-color: #f1f5f9; padding: 25px; border-radius: 12px;
        border: 1px solid #cbd5e1; line-height: 1.8; margin-bottom: 20px;
    }
    .info-box h3 { color: #4338ca; border-bottom: 2px solid #cbd5e1; padding-bottom: 10px; margin-top: 0; }
    .lyrics-container {
        padding: 8px 15px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
    .highlight { color: #4338ca; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "Let It Go - Frozen OST"
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
    "Let It Go - Frozen OST", 
    "Hello - Adele", 
    "A Whole New World - Aladdin OST",
    "Stand By Me - Ben E. King"
]
song_choice = st.selectbox("", song_options, label_visibility="collapsed")

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# [데이터 빌드]
# -------------------------
if song_choice == "Let It Go - Frozen OST":
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 완벽한 착한 소녀를 벗어던지다</h3>
    <p><b>[전체 줄거리]</b> 아렌델 왕국의 장녀 엘사는 태어날 때부터 모든 것을 얼려버리는 강력한 마법을 가지고 태어났습니다. 어린 시절, 실수로 동생 안나를 다치게 한 후 엘사는 자신의 힘을 공포의 대상으로 여기게 됩니다. 부모님은 엘사에게 "자신의 감정을 숨기고 마법을 억누르라"고 가르쳤고, 그녀는 장갑 속에 손을 감춘 채 평생을 고립되어 살아갑니다.</p>
    <p>여왕 대관식 날, 억눌렸던 마법이 세상 사람들 앞에서 폭발하고 엘사는 '괴물'이라는 비난을 피해 북쪽 산으로 도망칩니다. 아무도 없는 눈산에 도착한 엘사는 비로소 평생 자신을 옥죄었던 "착한 소녀가 되어야 한다"는 강박을 벗어던집니다.</p>
    <p><b>[노래의 의미]</b> 이 곡은 엘사의 <span class="highlight">'해방'과 '자기 수용'</span>을 상징합니다. 과거의 두려움과 사람들의 시선을 뒤로하고, 자신의 마법으로 화려한 얼음 성을 짓는 과정은 억압받던 영혼이 비로소 자유를 찾는 위대한 선언입니다.</p>
    """
    full_lyrics = [
        ("The snow glows white on the mountain tonight, not a footprint to be seen", "오늘 밤 산엔 눈이 하얗게 빛나고, 발자국 하나 보이지 않네"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내 노력을 알 거야"),
        ("Don't let them in, don't let them see. Be the good girl you always have to be", "그들을 들여보내지 마, 보여주지 마. 늘 그랬듯 착한 소녀가 되어야 해"),
        ("Conceal, don't feel, don't let them know. Well, now they know!", "숨기고, 느끼지 말고, 모르게 해. 그런데 이제 그들이 알아버렸어!"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어, 이제 자유야! 더는 억누를 수 없어"),
        ("Let it go, let it go! Turn away and slam the door!", "다 잊어, 이제 자유야! 돌아서서 문을 쾅 닫아버려!"),
        ("I don't care what they're going to say. Let the storm rage on", "그들이 뭐라 하든 상관없어. 폭풍아 계속 휘몰아쳐라"),
        ("The cold never bothered me anyway", "추위는 더 이상 나를 괴롭히지 못하니까")
    ]
    questions = [("1. 배경 장소는?", ["마을", "고립된 눈산", "성 안"], "고립된 눈산"), ("2. 엘사가 숨긴 것은?", ["보물", "얼음 마법", "동생의 비밀"], "얼음 마법"), ("3. 핵심 메시지는?", ["자유", "복수", "친구 찾기"], "자유"), ("4. 'The cold never bothered me'?", ["감기 걸렸다", "추위는 상관없다", "눈이 싫다"], "추위는 상관없다")]

elif song_choice == "Hello - Adele":
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 닿지 않는 과거에 건네는 간절한 사과</h3>
    <p><b>[곡의 배경]</b> 아델의 'Hello'는 세월이 흐른 뒤, 과거에 상처를 주었던 인연에게 건네는 뒤늦은 사과를 담고 있습니다. 주인공은 캘리포니아의 화려한 삶 속에 있지만, 마음 한구석에는 여전히 해결되지 않은 과거의 후회가 남아 있습니다.</p>
    <p><b>[풍부한 서사]</b> 주인공은 "우리가 어리고 자유로웠던 시절"을 회상합니다. 세상이 우리 발밑에 있었고 영원할 것 같았던 그때, 미숙했던 주인공은 상대방에게 큰 상처를 남기고 떠났습니다. 이제 어른이 된 그녀는 도저히 닿을 수 없을 것 같은 과거의 인연에게 "Hello"라고 인사를 건넵니다.</p>
    <p><b>[노래의 의미]</b> "수천 번을 전화했다"는 말은 실제로 건 전화 횟수라기보다, <b>매일 밤 마음속으로 되뇌었던 사과의 진심</b>을 뜻합니다. 비록 상대방은 이미 삶을 회복하여 응답이 없지만, 주인공은 이 일방적인 고백을 통해 비로소 자신의 죄책감에서 벗어나고자 합니다.</p>
    """
    full_lyrics = [
        ("Hello, it's me. I was wondering if after all these years you'd like to meet", "안녕, 나야. 이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything. They say that time's supposed to heal ya, but I ain't done much healing", "모든 걸 되짚어보기 위해 말야. 시간은 치유해준다지만 난 별로 치유되지 않았어"),
        ("Hello, can you hear me? I'm in California dreaming about who we used to be", "여보세요, 내 말 들리니? 난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("When we were younger and free. I've forgotten how it felt before the world fell at our feet", "우리가 더 어리고 자유로웠을 때 말야. 세상이 무너지기 전 기분이 어땠는지 잊어버렸어"),
        ("There's such a difference between us and a million miles", "우리 사이엔 너무 큰 차이가 있고 수백만 마일의 거리가 있네"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done. But when I call, you never seem to be home", "내 모든 일에 대해 미안하다고 말하려고. 하지만 넌 절대 집에 없는 것 같아"),
        ("Hello from the outside. At least I can say that I've tried", "외부에서 인사해. 적어도 내가 노력했다는 말은 할 수 있겠지"),
        ("To tell you I'm sorry for breaking your heart", "네 마음을 아프게 해서 미안하다고 말하기 위해서 말야"),
        ("But it don't matter, it clearly doesn't tear you apart anymore", "하지만 상관없겠지, 그게 더 이상 널 힘들게 하지 않는 게 분명하니까")
    ]
    questions = [("1. 'thousand times'의 뜻은?", ["딱 1000번", "매우 많이 연락함", "번호 실수"], "매우 많이 연락함"), ("2. 치유(healing)에 대한 화자의 말?", ["다 나았다", "별로 치유 안 됐다", "행복하다"], "별로 치유 안 됐다"), ("3. 화자가 있는 장소는?", ["런던", "캘리포니아", "서울"], "캘리포니아"), ("4. 전화 목적은?", ["돈 빌리기", "사과하기", "다시 사귀기"], "사과하기")]

elif song_choice == "A Whole New World - Aladdin OST":
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 성벽 너머, 새로운 운명을 향한 비행</h3>
    <p><b>[전체 줄거리]</b> 아그라바 왕국의 시장에서 좀도둑으로 살아가던 알라딘은 신분을 숨기고 탈출한 자스민 공주를 우연히 도와주며 사랑에 빠집니다. 하지만 신분의 벽 때문에 다가가지 못하다가, 지니의 도움으로 '알리 왕자'로 변신해 그녀를 찾아갑니다.</p>
    <p>자스민 공주는 평생 궁궐이라는 감옥에 갇혀 법률에 따라 사랑하지도 않는 왕자와 결혼해야 하는 운명에 절망하고 있었습니다. 알라딘은 그런 그녀에게 "나를 믿나요?"라고 물으며 마법 양탄자에 태워 성 밖으로 데려갑니다.</p>
    <p><b>[노래의 의미]</b> 이 곡은 두 사람이 밤하늘을 날며 부르는 환상적인 듀엣곡입니다. 여기서 <span class="highlight">"완전히 새로운 세상"</span>이란 단순히 화려한 풍경이 아니라, <b>타인의 통제에서 벗어나 스스로 선택하고 사랑할 수 있는 자유로운 삶</b>을 의미합니다. 자스민이 처음으로 마주한 세상의 광활함은 그녀의 인생이 바뀔 것임을 예고합니다.</p>
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
        ("That now I'm in a whole new world with you", "지금 내가 당신과 함께 완전히 새로운 세상에 있다는 사실이요"),
        ("(Now I'm in a whole new world with you)", "(이제 당신과 함께 새로운 세상에 있네요)")
    ]
    questions = [("1. 이동 수단은?", ["마차", "양탄자", "코끼리"], "양탄자"), ("2. 'A whole new world'?", ["오래된 가게", "새로운 세상", "감옥"], "새로운 세상"), ("3. 'Crystal clear'?", ["수정이 깨끗함", "매우 명확함", "유리가 반짝임"], "매우 명확함"), ("4. 알라딘의 질문은?", ["배고픈지", "마음의 결정을 따랐는지", "이름이 뭔지"], "마음의 결정을 따랐는지")]

else: # Stand By Me
    video_url = "https://www.youtube.com/watch?v=hwZNL7QVJjE"
    bg_content = """
    <h3>🤝 Stand By Me: 어둠 속에서도 든든한 연대의 힘</h3>
    <p><b>[배경 설명]</b> 1961년 베릴 E. 킹이 발표한 이 곡은 대중음악 역사상 가장 위대한 곡 중 하나로 꼽힙니다. 흑인 영가에서 영감을 받아 만들어진 이 노래는, 이후 동명의 영화(1986)의 주제곡으로 쓰이며 '우정과 연대'의 상징이 되었습니다.</p>
    <p><b>[풍부한 서사]</b> 노래의 배경은 칠흑 같은 어둠이 깔린 밤입니다. 땅은 어둡고 달빛만이 유일한 빛인 두려운 상황이죠. 하늘이 무너져 내리고 산이 바다로 무너져 내리는 천재지변 같은 시련이 닥칠지라도, 주인공은 "울지 않겠다"고 다짐합니다. </p>
    <p><b>[노래의 의미]</b> 이 노래에서 <span class="highlight">"Stand By Me(내 곁에 서 있어줘)"</span>는 단순한 물리적 거리가 아니라, 고난을 함께 이겨내자는 <b>'신뢰와 지지'</b>를 의미합니다. 친구, 연인, 혹은 공동체 등 우리가 의지할 수 있는 누군가가 곁에 있다면 그 어떤 세상의 종말 같은 위협도 두렵지 않다는 인간애의 메시지를 담고 있습니다.</p>
    """
    full_lyrics = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "우리가 볼 수 있는 빛이라곤 저 달빛뿐일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요. 두려워하지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에, 내 곁에 서 있어 주기만 한다면요"),
        ("If the sky that we look upon should tumble and fall", "우리가 올려다보는 저 하늘이 무너져 내린다 해도"),
        ("Or the mountain should crumble to the sea", "혹은 저 산이 바다로 무너져 내린다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요. 눈물 한 방울 흘리지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에, 내 곁에 서 있어 주기만 한다면요"),
        ("Whenever you're in trouble won't you stand by me", "당신이 곤경에 처할 때마다 내 곁에 서 있어 주겠어요?"),
        ("Oh, stand by me, won't you stand by me", "내 곁에 서 주세요, 내 곁에 서 주지 않겠어요?")
    ]
    questions = [("1. 유일한 빛(only light)은?", ["햇빛", "달빛", "별빛"], "달빛"), ("2. 'Tumble and fall' 하는 것은?", ["산", "하늘", "나무"], "하늘"), ("3. 'Shed a tear'의 뜻은?", ["웃다", "노래하다", "눈물을 흘리다"], "눈물을 흘리다"), ("4. 'Stand by me'의 의미는?", ["멀리 떠나다", "내 곁에 있어주다", "일어서다"], "내 곁에 있어주다")]

# 공통 데이터 처리
correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 탭 구성 (번호 추가)
# -------------------------
tab1, tab2, tab3 = st.tabs(["1. 🎬 배경 학습", "2. 📖 전체 가사 & 퀴즈", "3. 🧩 순서 배열"])

with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: 
        st.video(video_url)

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
            if st.form_submit_button("정답 확인 및 채점"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col_l:
        st.markdown("### 🎼 Full Lyrics (Section 1)")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 1절 전체 문장 순서 맞추기")
    st.write("가사 순서대로 클릭하세요!")
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(text, key=f"btn3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.session_state.show_q3_result = False
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
                st.error(f"{i+1}: Wrong Order")
                st.write(f"👉 **정답:** {correct_order[i]}")
                all_correct = False
        if all_correct: st.balloons()
