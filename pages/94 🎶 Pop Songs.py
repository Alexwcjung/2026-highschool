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
        border: 1px solid #e2e8f0; line-height: 1.8; margin-bottom: 20px;
    }
    .info-box h3 { font-size: 1.4rem; color: #4338ca; margin-bottom: 12px; border-bottom: 3px solid #6366f1; padding-bottom: 5px; }
    .lyrics-container {
        padding: 10px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f1f5f9; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.85rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False

def reset_data():
    st.session_state.submitted_step2 = False
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

# 상단 탭 구성
tab1, tab2, tab3 = st.tabs(["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"])

# -------------------------
# 2. 곡별 풍부한 데이터 (1절 전체 분량)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go: 억압된 자아의 해방</h3>엘사가 자신의 마법 능력을 더 이상 숨기지 않고 진정한 자아를 찾아가는 과정을 담고 있습니다."
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
    questions = [("엘사의 현재 심경은?", ["해방감", "공포"], "해방감"), ("'Conceal'의 뜻은?", ["숨기다", "드러내다"], "숨기다")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello: 과거의 나에게 건네는 안부</h3>아델이 과거의 미숙했던 자신과 자신이 상처 주었던 사람들에게 건네는 화해의 메시지입니다."
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything", "모든 것을 짚어보기 위해서 말이야"),
        ("They say that time's supposed to heal ya", "시간이 모든 걸 치유해준다고들 하지만"),
        ("But I ain't done much healing", "난 별로 치유되지 않은 것 같아"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side", "반대편에서 인사해")
    ]
    questions = [("화자가 전화를 거는 이유는?", ["사과와 화해", "복수"], "사과와 화해")]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = "<h3>✨ A Whole New World: 시야의 확장</h3>알라딘과 자스민이 양탄자를 타고 성벽 너머의 자유로운 세상을 처음 마주하는 경이로움을 노래합니다."
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
    questions = [("'Crystal clear'의 의미는?", ["명확한", "차가운"], "명확한")]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h3>🤝 Stand By Me: 변치 않는 연대</h3>어떤 거대한 시련이 닥쳐도 곁에 있는 사람만 있다면 두렵지 않다는 신뢰를 노래합니다."
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
    questions = [("화자가 두려워하지 않는 이유는?", ["동행자가 있어서", "돈이 많아서"], "동행자가 있어서")]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = "<h3>🍂 Don't Know Why: 망설임의 후회</h3>약속 장소에 가지 못한 자책과 그로 인해 남겨진 공허함을 담담한 재즈 선율에 담았습니다."
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
    questions = [("노래의 분위기는?", ["후회와 고독", "희망"], "후회와 고독")]

# -------------------------
# 데이터 처리
# -------------------------
alphabet = list(string.ascii_lowercase)
processed_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    processed_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in processed_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 3. 화면 출력 (탭별 구성)
# -------------------------
with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

with tab2:
    # [수정] 영상 화면을 작게 조절 (1:2 비율의 컬럼 사용)
    v_col, l_col = st.columns([1, 1.5])
    with v_col:
        st.video(video_url)
        st.divider()
        st.markdown("### 💡 Quiz")
        with st.form(f"quiz_{song_choice}"):
            for i, (q, opts, ans) in enumerate(questions):
                st.radio(q, opts, key=f"q_{i}", index=None)
            if st.form_submit_button("채점하기"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with l_col:
        st.markdown("### 🎼 가사 해석")
        for eng, kor in processed_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.info("가사 순서(a, b, c...)를 생각하며 버튼을 클릭하세요!")
    # 버튼 배치
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        btn_col = b_cols[0] if i % 2 == 0 else b_cols[1]
        is_sel = text in st.session_state.q3_cards
        if btn_col.button(text, key=f"btn3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    
    st.divider()
    st.markdown("### 📝 정답지 완성 중...")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("X", key=f"del_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.get('show_q3_result'):
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"{i+1}: Correct! ✅")
            else:
                st.error(f"{i+1}: Wrong ❌ (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
