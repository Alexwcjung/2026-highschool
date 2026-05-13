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
    .block-container { padding-top: 1.5rem !important; }
    .guide-text { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; margin-bottom: 10px; display: block; }
    .info-box {
        background-color: #f8fafc; padding: 25px; border-radius: 12px;
        border: 1px solid #e2e8f0; line-height: 1.8; font-size: 1rem; margin-bottom: 20px;
    }
    .info-box h3 { font-size: 1.4rem; color: #4338ca; margin-bottom: 12px; border-bottom: 3px solid #6366f1; padding-bottom: 5px; }
    .lyrics-container {
        padding: 10px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f1f5f9; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 0.95rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.85rem; color: #64748b; }
    .result-box { padding: 15px; border-radius: 8px; margin-bottom: 10px; }
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
st.markdown('<span class="guide-text">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)
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

tab1, tab2, tab3 = st.tabs(["🎬 배경 학습", "📖 가사 & 6문 퀴즈", "🧩 순서 배열"])

# -------------------------
# 2. 곡별 상세 데이터 (6문제씩 수록)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go</h3>엘사가 억압에서 벗어나 자아를 찾는 과정을 그린 곡입니다."
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어요"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었죠, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마요, 보여주지 마요"),
        ("Be the good girl you always have to be", "늘 그래야만 했던 착한 소녀가 되세요"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마요, 모르게 하세요"),
        ("Well, now they know! Let it go, let it go!", "그런데 이제 그들이 알아버렸죠! 다 잊어버려요")
    ]
    questions = [
        ("1. 'Isolation'의 의미는?", ["고립", "화합"], "고립"),
        ("2. 'Howling'하는 것은 무엇인가요?", ["The wind", "The queen"], "The wind"),
        ("3. 엘사가 숨기려고 노력했던 것은?", ["마법 능력", "왕관"], "마법 능력"),
        ("4. 'Conceal'과 반대되는 의미는?", ["Reveal", "Hide"], "Reveal"),
        ("5. 'Good girl'이 되라는 말은 누구의 기대인가요?", ["사회와 타인", "엘사 자신"], "사회와 타인"),
        ("6. 'Let it go'의 가장 적절한 의도는?", ["현실 도피", "자유와 해방"], "자유와 해방")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello</h3>아델이 과거의 연인 혹은 자신의 모습에 건네는 사과와 안부입니다."
    lyrics_raw = [
        ("Hello, it's me. I was wondering if you'd like to meet", "안녕, 나야. 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything", "모든 것을 다시 짚어보기 위해서 말이야"),
        ("They say that time's supposed to heal ya", "시간이 모든 걸 치유해준다고들 하지만"),
        ("But I ain't done much healing", "난 별로 치유되지 않은 것 같아"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("When we were younger and free", "우리가 더 어리고 자유로웠던 그때를 말이야"),
        ("I've forgotten how it felt before the world fell at our feet", "세상이 우리 발아래 놓이기 전의 기분을 잊고 있었어")
    ]
    questions = [
        ("1. 화자가 연락을 한 방식은?", ["전화", "편지"], "전화"),
        ("2. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다"], "궁금해하다"),
        ("3. 시간이 해결해준다고 믿었던 것은?", ["상처의 치유", "돈 문제"], "상처의 치유"),
        ("4. 화자의 현재 위치는?", ["California", "London"], "California"),
        ("5. 'Younger and free'했던 시절은 언제인가요?", ["과거", "현재"], "과거"),
        ("6. 화자는 현재 충분히 치유되었나요?", ["아니오", "예"], "아니오")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = "<h3>✨ A Whole New World</h3>성안에 갇혀 있던 자스민이 알라딘과 함께 새로운 세상을 보는 장면입니다."
    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"),
        ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"),
        ("Over, sideways and under on a magic carpet ride", "마법 양탄자를 타고 위아래 옆으로 다니며"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠"),
        ("No one to tell us 'No' or where to go", "누구도 안 된다거나 어디로 가라고 말 못 해요")
    ]
    questions = [
        ("1. 무엇을 타고 이동 중인가요?", ["Magic carpet", "Horse"], "Magic carpet"),
        ("2. 'Splendid'의 뜻으로 적절한 것은?", ["훌륭한", "평범한"], "훌륭한"),
        ("3. 알라딘이 공주에게 묻는 것은?", ["마음의 결정", "보석의 위치"], "마음의 결정"),
        ("4. 'Point of view'의 뜻은?", ["관점/시야", "장소"], "관점/시야"),
        ("5. 새로운 세상에서 허락되지 않는 행동은?", ["간섭과 제제", "자유"], "간섭과 제제"),
        ("6. 이 노래의 전체적인 분위기는?", ["경이로움", "슬픔"], "경이로움")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h3>🤝 Stand By Me</h3>어떤 공포 속에서도 곁에 누군가 있다면 견딜 수 있다는 우정의 노래입니다."
    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("If the sky that we look upon should tumble and fall", "우리가 보는 저 하늘이 무너져 내린다 해도"),
        ("Or the mountain should crumble to the sea", "혹은 산이 무너져 바다로 가라앉는다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요"),
        ("Just as long as you stand, stand by me", "그저 당신이 내 곁에 있어 주기만 한다면요")
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
    bg_content = "<h3>🍂 Don't Know Why</h3>용기가 없어 떠나지 못했거나 다가가지 못한 것에 대한 잔잔한 후회입니다."
    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("When I saw the break of day", "새벽이 밝아오는 걸 보았을 때"),
        ("I wished that I could fly away", "난 멀리 날아가 버리고 싶었죠"),
        ("Instead of kneeling in the sand", "모래 위에 무릎 꿇고 있는 대신에"),
        ("Thinking of the things I did", "내가 했던 일들을 생각하면서요")
    ]
    questions = [
        ("1. 화자가 기다린 시간은 언제까지인가요?", ["해가 뜰 때까지", "밤새도록"], "해가 뜰 때까지"),
        ("2. 화자가 반복하는 말은?", ["왜 안 왔는지 모르겠다", "행복하다"], "왜 안 왔는지 모르겠다"),
        ("3. 'House of fun'에 남겨진 사람은?", ["You", "I"], "You"),
        ("4. 'Fly away'하고 싶은 이유는?", ["상황을 피하고 싶어서", "여행 가고 싶어서"], "상황을 피하고 싶어서"),
        ("5. 'Kneeling'의 의미는?", ["무릎 꿇기", "달리기"], "무릎 꿇기"),
        ("6. 노래 전체의 감정선은?", ["자책과 후회", "열정"], "자책과 후회")
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

if 'scrambled' not in st.session_state or st.session_state.get('last_song_v3') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song_v3 = song_choice

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
        with st.form(f"quiz_6_{song_choice}"):
            user_answers = []
            for i, (q, opts, ans) in enumerate(questions):
                user_ans = st.radio(q, opts, key=f"q6_{i}", index=None)
                user_answers.append(user_ans)
            
            if st.form_submit_button("퀴즈 정답 확인"):
                score = 0
                for i, (q, opts, ans) in enumerate(questions):
                    if user_answers[i] == ans: score += 1
                    else: st.error(f"X {i+1}번 오답: 정답은 [{ans}]")
                if score == 6: st.balloons(); st.success("6문제 모두 정답입니다! 완벽해요!")
                else: st.warning(f"총 6문제 중 {score}문제를 맞혔습니다.")
    with l_col:
        st.markdown("### 🎼 Lyrics Study")
        for eng, kor in processed_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.info("아래 버튼을 순서대로 클릭하여 가사를 완성한 후 '정답 제출' 버튼을 누르세요.")
    
    # 가사 선택 버튼
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        col = b_cols[0] if i % 2 == 0 else b_cols[1]
        is_sel = text in st.session_state.q3_cards
        if col.button(text, key=f"btn3_q6_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📝 나의 답안지")
    
    # 선택된 가사 리스트
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("삭제", key=f"del_q6_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    # 제출 및 결과
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 정답 제출 및 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.show_q3_result:
        st.markdown("### 🏁 채점 결과")
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
            st.success("축하합니다! 모든 순서를 정확하게 맞추셨습니다!")
        else:
            if st.button("다시 시도하기"):
                st.session_state.q3_cards = []
                st.session_state.show_q3_result = False
                st.rerun()
