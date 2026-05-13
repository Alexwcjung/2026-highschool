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
# 상단 곡 선택 메뉴
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)
song_choice = st.selectbox("", ["Let It Go - Frozen OST", "Hello - Adele", "A Whole New World - Aladdin OST"], label_visibility="collapsed")

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
    <h3>❄️ Let It Go: 자유를 향한 외침</h3>
    <p><b>[줄거리]</b> 아렌델 왕국의 공주 엘사는 손에 닿는 모든 것을 얼려버리는 강력한 마법을 가지고 태어났습니다. 어린 시절 사고로 동생 안나를 다치게 한 후, 엘사는 자신의 힘이 괴물 같다고 느끼며 방 안에 스스로를 가둔 채 평생을 숨기며 살아왔습니다. "숨기고, 느끼지 마라(Conceal, don't feel)"는 부모님의 가르침은 그녀에게 거대한 족쇄였습니다.</p>
    <p>성인이 되어 여왕 대관식을 치르던 날, 통제할 수 없었던 마법이 온 세상에 드러나게 되고 사람들은 엘사를 괴물로 몰아붙입니다. 결국 엘사는 사람들을 피해 아무도 없는 북쪽 산으로 도망칩니다.</p>
    <p><b>[노래의 의미]</b> 이 곡은 바로 그 순간, 고립된 산속에서 엘사가 부르는 노래입니다. 더 이상 완벽한 여왕일 필요도, 자신의 마법을 숨길 필요도 없다는 것을 깨달은 엘사는 비로소 <b>자신의 본습을 긍정하며 억눌렸던 에너지를 폭발</b>시킵니다. "추위는 더 이상 나를 괴롭히지 못한다"는 선언과 함께 화려한 얼음 성을 짓는 장면은 영화사상 최고의 명장면으로 꼽힙니다.</p>
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
    <h3>☎️ Hello: 과거의 나에게 건네는 안부</h3>
    <p><b>[배경 설명]</b> 아델의 'Hello'는 단순히 이별한 연인을 그리워하는 노래를 넘어선 깊은 감정을 담고 있습니다. 아델은 이 곡이 <b>"자기 자신을 포함한 모든 사람에게 건네는 사과와 안부"</b>라고 설명했습니다.</p>
    <p>우리는 누구나 살면서 소중한 사람에게 상처를 주거나, 미숙했던 과거의 자신 때문에 후회하는 순간이 있습니다. 이 노래의 주인공은 아주 오랜 시간이 흐른 뒤, 도저히 닿을 수 없을 것 같은 과거의 인연에게 조심스럽게 전화를 겁니다. 캘리포니아의 화려함 속에 있지만, 마음은 여전히 그 시절의 우리를 꿈꾸고 있죠.</p>
    <p><b>[노래의 의미]</b> "Hello from the other side(반대편에서 인사해)"라는 가사는 물리적인 거리뿐만 아니라, 다시는 돌아갈 수 없는 '과거'와 '현재' 사이의 거대한 벽을 의미합니다. 상대방은 이미 상처를 잊고 평온해졌을지 모르지만, 주인공은 <b>수천 번의 전화를 걸어서라도 미안하다는 말을 전함으로써 자신의 아픈 과거를 매듭짓고자</b> 합니다.</p>
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
    <h3>✨ A Whole New World: 성벽 너머의 경이로움</h3>
    <p><b>[줄거리]</b> 아그라바 왕국의 가난하지만 마음 착한 좀도둑 알라딘은 우연히 시장에서 신분을 숨기고 나온 자스민 공주를 만나 사랑에 빠집니다. 하지만 법적으로 공주는 오직 왕자와만 결혼할 수 있었죠. 알라딘은 지니의 도움으로 왕자로 변신하여 성에 있는 자스민을 찾아갑니다.</p>
    <p>평생 성벽 안에 갇혀 정해진 삶만을 강요받던 자스민은 알라딘에 대해 반감을 품지만, 알라딘은 그녀에게 "나를 믿나요?(Do you trust me?)"라고 물으며 마법 양탄자에 태웁니다.</p>
    <p><b>[노래의 의미]</b> 이 곡은 두 사람이 양탄자를 타고 밤하늘을 가로지르며 부르는 듀엣곡입니다. <b>"완전히 새로운 세상"</b>이란 단순히 화려한 경치를 넘어, 누구의 방해도 받지 않고 자신의 의지대로 선택할 수 있는 '자유로운 삶'을 의미합니다. 자스민이 처음으로 성 밖의 세상을 보며 느낀 전율과 알라딘의 진심이 어우러져 디즈니 역사상 가장 로맨틱한 순간을 만들어냅니다.</p>
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
# 탭 구성 (공통 로직)
# -------------------------
tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 배경 학습", "📖 STEP 2. 전체 가사 & 퀴즈", "🧩 STEP 3. 1절 순서 배열"])

with tab1:
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: 
        st.video(video_url)
    # 영상 아래로 설명 이동 및 분량 강화
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)

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
