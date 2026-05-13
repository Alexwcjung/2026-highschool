import streamlit as st

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
    /* 선택 박스 라벨 글씨 크기 조정 */
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
    .info-box h3 { color: #4338ca; border-bottom: 2px solid #cbd5e1; padding-bottom: 10px; }
    .lyrics-container {
        padding: 8px 15px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
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

# -------------------------
# 상단 곡 선택 메뉴 (글씨 크게 변경)
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)

# HTML 커스텀 라벨 사용
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)
song_choice = st.selectbox("", 
                           ["Let It Go - Frozen OST", "Hello - Adele", "A Whole New World - Aladdin OST"],
                           label_visibility="collapsed")

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
    <p><b>❄️ 영화 '겨울왕국(Frozen)'의 핵심 장면입니다.</b></p>
    <p>주인공 엘사는 태어날 때부터 모든 것을 얼려버리는 마법을 숨기며 평생을 억눌려 살아왔습니다. 하지만 마법이 세상에 드러나자 북쪽 산으로 도망쳐, <b>더 이상 남의 시선을 신경 쓰지 않고 자신의 본모습을 받아들이며 자유를 선언하는 순간</b>을 노래합니다.</p>
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
    correct_order = [line[0] for line in full_lyrics]
    scrambled_order = [correct_order[3], correct_order[0], correct_order[7], correct_order[1], correct_order[5], correct_order[2], correct_order[8], correct_order[4], correct_order[6], correct_order[9]]

elif song_choice == "Hello - Adele":
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <p><b>☎️ 아델(Adele)의 깊은 감성이 담긴 곡입니다.</b></p>
    <p>오랜 시간이 흐른 뒤, 주인공은 전 연인에게 전화를 걸어 "Hello"라고 인사를 건넵니다. 단순히 상대를 그리워하는 것을 넘어, <b>과거의 잘못에 대해 미안함을 전하고 스스로와 화해하고 싶어 하는 간절함</b>을 노래하고 있습니다.</p>
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
    correct_order = [line[0] for line in full_lyrics]
    scrambled_order = [correct_order[5], correct_order[0], correct_order[9], correct_order[2], correct_order[7], correct_order[1], correct_order[8], correct_order[3], correct_order[6], correct_order[4]]

else: # A Whole New World
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <p><b>✨ 애니메이션 '알라딘'의 경이로운 비행 장면입니다.</b></p>
    <p>알라딘은 마법 양탄자를 이용해 성 안에만 갇혀 지내던 자스민 공주에게 성 밖의 광활한 세상을 보여줍니다. <b>처음 느껴보는 자유로움과 설레는 사랑</b>을 밤하늘을 날며 노래하는 아름다운 듀엣곡입니다.</p>
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
    correct_order = [line[0] for line in full_lyrics]
    scrambled_order = [correct_order[4], correct_order[1], correct_order[8], correct_order[0], correct_order[7], correct_order[2], correct_order[9], correct_order[3], correct_order[6], correct_order[5]]

# -------------------------
# 탭 구성
# -------------------------
tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 배경 학습", "📖 STEP 2. 전체 가사 & 퀴즈", "🧩 STEP 3. 1절 순서 배열"])

with tab1:
    st.markdown(f'<div class="info-box"><h3>📜 Song Story: {song_choice}</h3>{bg_content}</div>', unsafe_allow_html=True)
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
    for i, text in enumerate(scrambled_order):
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
