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
    .guide-text { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; margin-bottom: 10px; display: block; }
    .info-box {
        background-color: #f1f5f9; padding: 30px; border-radius: 15px;
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
# 세션 상태 관리
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
st.markdown('<span class="guide-text">🎵 학습할 노래를 선택하세요 (1절 전체 가사 수록)</span>', unsafe_allow_html=True)
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

tab1, tab2, tab3 = st.tabs(["🎬 상세 배경 학습", "📖 가사 1절 & 6문 퀴즈", "🧩 순서 배열"])

# -------------------------
# 2. 곡별 풍부한 배경 및 1절 가사 데이터
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h2>❄️ Let It Go: 억압의 사슬을 끊고 진정한 자신으로</h2>
    아렌델 왕국의 공주 <b>엘사</b>는 모든 것을 얼려버리는 마법 능력을 가지고 태어났습니다. 하지만 부모님은 이를 저주라 여겨 엘사에게 <b>"감추고, 느끼지 말라(Conceal, don't feel)"</b>고 가르치며 세상으로부터 격리시킵니다. 
    <br><br>성인이 되어 대관식을 치르던 날, 실수로 능력이 탄로 난 엘사는 사람들의 두려움 섞인 시선을 피해 북쪽 산으로 도망칩니다. 이 곡은 그곳에서 홀로 남겨진 엘사가 더 이상 남의 눈치를 보지 않고, <b>자신의 힘을 마음껏 펼치며 자유를 선언하는 순간</b>을 담고 있습니다. 
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
    세계적인 디바 <b>아델(Adele)</b>의 'Hello'는 단순한 이별 노래를 넘어선 성찰의 기록입니다. 
    곡의 주인공은 수년이 흐른 뒤, 과거에 상처를 주었던 연인에게 전화를 겁니다. <b>"시간이 해결해줄 줄 알았지만, 난 여전히 치유되지 않았다"</b>고 고백하는 가사는 많은 이들의 공감을 불러일으켰습니다.
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
        ("There's such a difference between us and a million miles", "우리 사이엔 큰 차이와 수백만 마일의 거리가 있네")
    ]
    questions = [
        ("1. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다"], "궁금해하다"),
        ("2. 시간이 해결해준다고 믿었던 것은?", ["상처의 치유", "돈 문제"], "상처의 치유"),
        ("3. 화자의 현재 위치는?", ["California", "London"], "California"),
        ("4. 'Younger and free'했던 시절은 언제인가요?", ["과거", "현재"], "과거"),
        ("5. 'A million miles'가 상징하는 것은?", ["물리적/심리적 거리", "비행기 거리"], "물리적/심리적 거리"),
        ("6. 화자는 현재 충분히 치유되었나요?", ["아니오", "예"], "아니오")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h2>✨ A Whole New World: 편견의 성벽을 넘어</h2>
    아그라바 왕국의 <b>자스민 공주</b>는 높은 성벽 안에서 정해진 운명대로 살아야 하는 자신의 삶에 답답함을 느낍니다. 그때 알라딘이 마법 양탄자를 타고 그녀를 찾아옵니다. 
    이 곡은 두 사람이 세상을 처음으로 목격할 때 흐르는 듀엣곡으로, <b>주체적인 삶</b>의 가치를 일깨워줍니다.
    """
    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
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
        ("2. 'Splendid'의 뜻으로 적절한 것은?", ["훌륭한", "평범한"], "훌륭한"),
        ("3. 알라딘이 공주에게 묻는 것은?", ["마음의 결정", "보석의 위치"], "마음의 결정"),
        ("4. 'Point of view'의 뜻은?", ["관점/시야", "장소"], "관점/시야"),
        ("5. 'Dazzling'의 의미는?", ["눈부신", "어두운"], "눈부신"),
        ("6. 이 노래의 전체적인 분위기는?", ["경이로움과 자유", "슬픔"], "경이로움과 자유")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h2>🤝 Stand By Me: 두려움을 이기는 연대의 힘</h2>
    1961년 발표된 벤 E. 킹의 이 곡은 시대를 초월해 사랑받는 <b>우정과 연대</b>의 송가입니다. 
    "밤이 오고 땅이 어두워지며 달빛만이 유일한 빛일 때"라는 배경은 우리가 인생에서 마주하는 <b>시련과 공포</b>를 의미합니다. 하지만 곁을 지켜주는 존재만 있다면 이겨낼 수 있다는 메시지를 담고 있습니다.
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
        ("3. 'Afraid'의 감정을 느끼지 않는 조건은?", ["당신이 곁에 있을 때", "돈을 가졌을 때"], "당신이 곁에 있을 때"),
        ("4. 'Tumble and fall'하는 주체는?", ["The sky", "The moon"], "The sky"),
        ("5. 'Crumble'의 의미는?", ["허물어지다", "솟아오르다"], "허물어지다"),
        ("6. 'Shed a tear'의 뜻은?", ["눈물을 흘리다", "미소 짓다"], "눈물을 흘리다")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h2>🍂 Don't Know Why: 망설임 끝에 남겨진 공허함</h2>
    재즈 팝의 여왕 <b>노라 존스</b>의 곡으로, 전 세계적인 히트를 기록했습니다. 
    이 노래는 사랑하는 사람과의 약속 혹은 어떤 결단의 순간에 <b>용기 내지 못하고 가지 않았던 한 사람</b>의 내면을 그리고 있습니다. 망설임 끝에 찾아온 '알 수 없는 후회'가 주제입니다.
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
        ("1. 화자가 기다린 시간은 언제까지인가요?", ["해가 뜰 때까지", "밤새도록"], "해가 뜰 때까지"),
        ("2. 화자가 반복하는 말은?", ["왜 안 왔는지 모르겠다", "행복하다"], "왜 안 왔는지 모르겠다"),
        ("3. 'House of fun'에 남겨진 사람은?", ["You", "I"], "You"),
        ("4. 'Fly away'하고 싶은 이유는?", ["상황을 피하고 싶어서", "여행 가고 싶어서"], "상황을 피하고 싶어서"),
        ("5. 'Kneeling'의 의미는?", ["무릎 꿇기", "달리기"], "무릎 꿇기"),
        ("6. 'On my mind'의 뜻은?", ["마음/생각 속에", "머리 위에"], "마음/생각 속에")
    ]

# -------------------------
# 가사 데이터 가공
# -------------------------
alphabet = list(string.ascii_lowercase)
processed_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    processed_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in processed_lyrics]

if 'scrambled' not in st.session_state or st.session_state.get('last_song_final') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song_final = song_choice

# -------------------------
# 3. 탭별 출력
# -------------------------
with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

with tab2:
    v_col, l_col = st.columns([1, 1.4])
    with v_col:
        st.video(video_url)
        st.markdown("---")
        st.markdown("### ✍️ Comprehension Quiz (6)")
        with st.form(f"quiz_6_final_{song_choice}"):
            user_answers = []
            for i, (q, opts, ans) in enumerate(questions):
                user_ans = st.radio(q, opts, key=f"q6_fin_{i}", index=None)
                user_answers.append(user_ans)
            
            if st.form_submit_button("퀴즈 정답 확인"):
                score = 0
                for i, (q, opts, ans) in enumerate(questions):
                    if user_answers[i] == ans: score += 1
                    else: st.error(f"X {i+1}번 오답: 정답은 [{ans}]")
                if score == 6: st.balloons(); st.success("6문제 모두 정답입니다! 완벽해요!")
                else: st.warning(f"총 6문제 중 {score}문제를 맞혔습니다.")
    with l_col:
        st.markdown("### 🎼 Lyrics Study (Verse 1)")
        for eng, kor in processed_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.info("아래 가사 조각들을 1절 순서에 맞게 클릭하세요.")
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        col = b_cols[0] if i % 2 == 0 else b_cols[1]
        is_sel = text in st.session_state.q3_cards
        if col.button(text, key=f"btn3_fin_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📝 나의 제출 답안")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("삭제", key=f"del_fin_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 정답 제출 및 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.show_q3_result:
        st.markdown("### 🏁 채점 및 정답 비교")
        all_correct = True
        for i in range(len(correct_order)):
            user_s = st.session_state.q3_cards[i]
            actual_s = correct_order[i]
            if user_s == actual_s:
                st.success(f"**Step {i+1}: Correct!** ✅  \n{user_s}")
            else:
                st.error(f"**Step {i+1}: Wrong!** ❌  \n나의 선택: {user_s}  \n**정답: {actual_s}**")
                all_correct = False
        
        if all_correct:
            st.balloons()
            st.success("대단합니다! 1절 가사 전체 순서를 완벽하게 맞추셨습니다!")
        else:
            if st.button("처음부터 다시 시도"):
                st.session_state.q3_cards = []
                st.session_state.show_q3_result = False
                st.rerun()
