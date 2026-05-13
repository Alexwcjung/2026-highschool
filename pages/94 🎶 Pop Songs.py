import streamlit as st
import random
import string

# =========================
# 1. 스타일 및 레이아웃 설정
# =========================
st.set_page_config(page_title="Music English Master", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    .info-box {
        background-color: #f1f5f9; padding: 25px; border-radius: 15px;
        border-left: 8px solid #4338ca; line-height: 1.8; font-size: 1.05rem; margin-bottom: 25px;
    }
    .info-box h2 { color: #1e3a8a; margin-bottom: 15px; font-weight: 800; }
    .lyrics-container {
        padding: 12px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 초기화 및 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'show_q3_result' not in st.session_state: st.session_state.show_q3_result = False

def reset_data():
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state: del st.session_state.scrambled

# -------------------------
# 곡 선택 섹션
# -------------------------
song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]
song_choice = st.sidebar.selectbox("🎵 학습할 노래 선택", song_options)

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

tab1, tab2, tab3 = st.tabs(["🎬 상세 배경 학습", "📖 가사 1절 & 6문 퀴즈", "🧩 순서 배열"])

# -------------------------
# 2. 곡별 데이터베이스 (5곡 전체)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h2>❄️ Let It Go: 억압의 사슬을 끊고 진정한 자신으로</h2>
    아렌델 왕국의 공주 <b>엘사</b>는 모든 것을 얼려버리는 마법 능력을 저주라 여기며 <b>"감추고, 느끼지 말라"</b>는 교육을 받았습니다. 하지만 대관식 날 정체가 탄로 난 후 북쪽 산으로 도망쳐, 더 이상 타인의 시선에 갇히지 않고 <b>자신의 힘을 긍정하며 자유를 선언</b>하는 곡입니다.
    """
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나네요"),
        ("Not a footprint to be seen", "발자국 하나 보이지 않아요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같네요"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어요"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었죠, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마요, 보여주지 마요"),
        ("Be the good girl you always have to be", "늘 그래야만 했던 착한 소녀가 되세요"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마요, 모르게 하세요"),
        ("Well, now they know!", "그런데 이제 그들이 알아버렸죠!"),
        ("Let it go, let it go, can't hold it back anymore", "다 잊어버려요, 더 이상 참지 않을 거예요")
    ]
    questions = [
        ("1. 'Footprint'가 보이지 않는 이유는?", ["눈이 많이 내려서", "아무도 없어서"], "아무도 없어서"),
        ("2. 'Howling'하는 것은 무엇인가요?", ["The wind", "The queen"], "The wind"),
        ("3. 'Isolation'의 의미는?", ["고립", "화합"], "고립"),
        ("4. 'Conceal'과 반대되는 의미는?", ["Reveal", "Hide"], "Reveal"),
        ("5. 'Good girl'이 되라는 말은 누구의 기대인가요?", ["사회와 타인", "엘사 자신"], "사회와 타인"),
        ("6. 'Let it go'의 가장 적절한 의도는?", ["현실 도피", "자유와 해방"], "자유와 해방")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h2>☎️ Hello: 과거의 상처와 마주하는 용기</h2>
    아델(Adele)의 이 곡은 과거의 연인, 혹은 과거의 자신에게 건네는 뒤늦은 인사입니다. 시간이 모든 걸 해결해 줄 거라 믿었지만, 여전히 남아있는 미안함과 공허함을 전화기 너머로 고백하는 성숙한 감정을 담고 있습니다.
    """
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything", "모든 것을 다시 짚어보기 위해서 말이야"),
        ("They say that time's supposed to heal ya", "시간이 모든 걸 치유해준다고들 하지만"),
        ("But I ain't done much healing", "난 별로 치유되지 않은 것 같아"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("When we were younger and free", "우리가 더 어리고 자유로웠던 그때를 말이야"),
        ("I've forgotten how it felt before the world fell at our feet", "세상이 우리 발아래 놓이기 전의 기분을 잊고 있었어"),
        ("There's such a difference between us", "우리 사이엔 너무나 큰 차이가 있네")
    ]
    questions = [
        ("1. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다"], "궁금해하다"),
        ("2. 시간이 해결해준다고 믿었던 것은?", ["상처의 치유", "돈 문제"], "상처의 치유"),
        ("3. 화자의 현재 위치는?", ["California", "London"], "California"),
        ("4. 'Younger and free'했던 시절은?", ["과거", "현재"], "과거"),
        ("5. 화자가 만나고 싶어 하는 목적은?", ["모든 걸 되짚어보기", "다시 사귀기"], "모든 걸 되짚어보기"),
        ("6. 화자는 현재 충분히 치유되었나요?", ["아니오", "예"], "아니오")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h2>✨ A Whole New World: 성벽을 넘어 마주한 자유</h2>
    자스민 공주는 궁궐이라는 황금 감옥 안에서 살고 있었습니다. 알라딘과 함께 마법 양탄자를 타고 처음으로 세상을 내려다보며, 타인이 정해준 삶이 아닌 <b>직접 보고 느끼는 주체적인 삶</b>의 기쁨을 노래합니다.
    """
    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 결정하게 둔 게 언제였나요?"),
        ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"),
        ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"),
        ("Over, sideways and under on a magic carpet ride", "마법 양탄자를 타고 위아래 옆으로 다니며"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠"),
        ("No one to tell us 'No' or where to go", "누구도 안 된다거나 어디로 가라고 말 못 해요"),
        ("Or say we're only dreaming", "혹은 우리가 꿈을 꾸는 뿐이라고 말 못 하죠"),
        ("A whole new world, a dazzling place I never knew", "완전히 새로운 세상, 내가 결코 몰랐던 눈부신 곳이에요")
    ]
    questions = [
        ("1. 무엇을 타고 이동 중인가요?", ["Magic carpet", "Horse"], "Magic carpet"),
        ("2. 'Splendid'의 뜻으로 적절한 것은?", ["훌륭한/화려한", "평범한"], "훌륭한/화려한"),
        ("3. 알라딘이 공주에게 묻는 것은?", ["마음의 결정", "보석의 위치"], "마음의 결정"),
        ("4. 'Point of view'의 뜻은?", ["관점/시야", "장소"], "관점/시야"),
        ("5. 'Dazzling'의 의미는?", ["눈부신", "어두운"], "눈부신"),
        ("6. 이 노래의 핵심 키워드는?", ["자유와 경이로움", "두려움"], "자유와 경이로움")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h2>🤝 Stand By Me: 시련을 이기는 연대의 힘</h2>
    인생의 밤이 오고 하늘이 무너져 내리는 극한의 상황에서도, 곁에 누군가 서 있어 준다면 두렵지 않다는 메시지를 담고 있습니다. 1961년 발표 이후 전 세계에서 <b>우정과 신뢰</b>를 상징하는 곡으로 불리고 있습니다.
    """
    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("So darling, darling, stand by me. Oh, stand by me", "그러니 그대여, 내 곁에 서 주세요"),
        ("If the sky that we look upon should tumble and fall", "우리가 보는 저 하늘이 무너져 내린다 해도"),
        ("Or the mountain should crumble to the sea", "혹은 산이 무너져 바다로 가라앉는다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요"),
        ("Just as long as you stand, stand by me", "그저 당신이 내 곁에 있어 주기만 한다면요"),
        ("Whenever you're in trouble, won't you stand by me?", "당신이 어려움에 처할 때면 내 곁에 서 주지 않을래요?")
    ]
    questions = [
        ("1. 배경이 되는 시간대는?", ["Night", "Day"], "Night"),
        ("2. 유일한 빛은 무엇인가요?", ["Moon", "Sun"], "Moon"),
        ("3. 'Afraid'하지 않는 조건은?", ["당신이 곁에 있을 때", "돈이 많을 때"], "당신이 곁에 있을 때"),
        ("4. 'Tumble and fall'은 무엇을 의미하나요?", ["심각한 시련", "즐거운 축제"], "심각한 시련"),
        ("5. 'Crumble'의 의미는?", ["허물어지다", "치솟다"], "허물어지다"),
        ("6. 'Stand by me'의 알맞은 해석은?", ["내 곁을 지켜줘", "옆에 서서 기다려"], "내 곁을 지켜줘")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h2>🍂 Don't Know Why: 망설임과 늦어버린 후회</h2>
    사랑하는 이에게 갈 기회가 있었음에도 용기가 없어 가지 못했던 순간을 노래합니다. 해가 뜰 때까지 기다렸지만 결국 움직이지 못했던 자신에 대한 알 수 없는 원망과 쓸쓸함이 담긴 재즈 명곡입니다.
    """
    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("When I saw the break of day", "새벽이 밝아오는 걸 보았을 때"),
        ("I wished that I could fly away", "난 멀리 날아가 버리고 싶었죠"),
        ("Instead of kneeling in the sand", "모래 위에 무릎 꿇고 있는 대신에"),
        ("Thinking of the things I did", "내가 했던 일들을 생각하면서요"),
        ("My heart is drenched in wine", "내 마음은 와인에 흠뻑 젖어 있고"),
        ("But you'll be on my mind forever", "당신은 내 마음속에 영원히 남아있겠죠")
    ]
    questions = [
        ("1. 화자가 기다린 시간은?", ["해가 뜰 때까지", "밤새도록"], "해가 뜰 때까지"),
        ("2. 화자의 현재 주된 감정은?", ["후회", "자신감"], "후회"),
        ("3. 'House of fun'에 남겨진 대상은?", ["You(상대방)", "I(나)"], "You(상대방)"),
        ("4. 'Fly away'는 무엇을 뜻하나요?", ["현실 회피", "비행기 여행"], "현실 회피"),
        ("5. 'Drenched'의 의미는?", ["흠뻑 젖은", "바짝 마른"], "흠뻑 젖은"),
        ("6. 'On my mind'의 뜻은?", ["잊지 못하고 생각나는", "머리가 아픈"], "잊지 못하고 생각나는")
    ]

# -------------------------
# 공통 로직: 가사 가공 및 순서 생성
# -------------------------
processed_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = f"L{i+1:02d}"
    processed_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in processed_lyrics]

if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 3. 탭별 화면 출력
# -------------------------
with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

with tab2:
    v_col, l_col = st.columns([1, 1.4])
    with v_col:
        st.video(video_url)
        st.markdown("---")
        st.markdown("### ✍️ 가사 내용 확인 퀴즈 (6문제)")
        with st.form(key=f"quiz_form_{song_choice}"):
            user_answers = []
            for i, (q, opts, ans) in enumerate(questions):
                u_ans = st.radio(q, opts, key=f"r_{song_choice}_{i}", index=None)
                user_answers.append(u_ans)
            
            if st.form_submit_button("퀴즈 정답 확인"):
                score = 0
                for i, (q, opts, ans) in enumerate(questions):
                    if user_answers[i] == ans: score += 1
                    else: st.error(f"X {i+1}번 오답: 정답은 [{ans}]")
                if score == 6: st.balloons(); st.success("모든 문제를 맞혔습니다!")
                else: st.warning(f"6문제 중 {score}문제를 맞혔습니다.")
    
    with l_col:
        st.markdown("### 🎼 가사 1절 전체 학습")
        for eng, kor in processed_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.info("아래 가사 조각들을 1절 순서에 맞게 하나씩 클릭하세요.")
    cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        col_idx = i % 2
        is_sel = text in st.session_state.q3_cards
        if cols[col_idx].button(text, key=f"btn_{song_choice}_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📝 나의 선택 순서")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.85, 0.15])
        c1.info(f"{idx+1}: {card}")
        if c2.button("삭제", key=f"del_{song_choice}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 정답 제출 및 채점 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.show_q3_result:
        st.markdown("### 🏁 채점 결과 (정답과 비교)")
        all_correct = True
        for i in range(len(correct_order)):
            u_v = st.session_state.q3_cards[i]
            a_v = correct_order[i]
            if u_v == a_v:
                st.success(f"**{i+1}번:** 정답! ✅  \n{u_v}")
            else:
                st.error(f"**{i+1}번:** 오답! ❌  \n내 선택: {u_v}  \n**정답: {a_v}**")
                all_correct = False
        
        if all_correct: st.balloons(); st.success("축하합니다! 가사 순서를 완벽하게 맞혔습니다.")
        if st.button("다시 도전하기"): reset_data(); st.rerun()
