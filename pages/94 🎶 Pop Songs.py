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
    .info-box {
        background-color: #f1f5f9; padding: 20px; border-radius: 12px;
        border: 1px solid #cbd5e1; line-height: 1.6; margin-bottom: 20px;
    }
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

song_choice = st.selectbox("학습할 노래를 선택하세요:", ["Let It Go - Frozen OST", "Hello - Adele"])

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# [데이터 빌드]
# -------------------------
if song_choice == "Let It Go - Frozen OST":
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "엘사가 자신의 마법을 더 이상 숨기지 않고 자유를 선언하며 얼음 성을 짓는 명장면입니다."
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
    questions = [
        ("1. 노래의 배경이 되는 장소는?", ["사람이 북적이는 마을", "아무도 없는 고립된 눈산", "따뜻한 성 안"], "아무도 없는 고립된 눈산"),
        ("2. 엘사가 숨기려고 노력했던 것은?", ["자신의 보물", "자신의 얼음 마법", "동생 안나의 비밀"], "자신의 얼음 마법"),
        ("3. 'Let it go'의 핵심 메시지는?", ["과거에 얽매이지 않는 자유", "다시 왕국으로 돌아가기", "친구를 찾아 떠나기"], "과거에 얽매이지 않는 자유"),
        ("4. 'The cold never bothered me'의 의미는?", ["감기에 걸렸다", "추위는 상관없다", "눈이 싫다"], "추위는 상관없다")
    ]
else:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "헤어진 연인에게 수년 만에 전화를 걸어 사과와 그리움을 전하는 노래입니다. 아델의 파워풀한 보컬과 명확한 발음이 특징입니다."
    # 1절 끝(첫 후렴 종료)까지의 긴 문장 구성
    full_lyrics = [
        ("Hello, it's me. I was wondering if after all these years you'd like to meet", "안녕, 나야. 이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("To go over everything. They say that time's supposed to heal ya, but I ain't done much healing", "모든 걸 되짚어보기 위해 말야. 시간은 모든 걸 치유한다지만 난 별로 치유되지 않았어"),
        ("Hello, can you hear me? I'm in California dreaming about who we used to be", "여보세요, 내 말 들리니? 난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("When we were younger and free. I've forgotten how it felt before the world fell at our feet", "우리가 더 어리고 자유로웠을 때 말야. 세상이 우리 발아래 무너지기 전 기분이 어땠는지 잊어버렸어"),
        ("There's such a difference between us and a million miles", "우리 사이엔 너무 큰 차이가 있고 수백만 마일의 거리가 있네"),
        ("Hello from the other side. I must've called a thousand times", "반대편에서 인사해. 수천 번은 전화했을 거야"),
        ("To tell you I'm sorry for everything that I've done. But when I call, you never seem to be home", "내가 했던 모든 일에 대해 미안하다고 말하려고. 하지만 내가 전화할 때 넌 절대 집에 없는 것 같아"),
        ("Hello from the outside. At least I can say that I've tried", "외부(밖)에서 인사해. 적어도 내가 노력했다는 말은 할 수 있겠지"),
        ("To tell you I'm sorry for breaking your heart", "네 마음을 아프게 해서 미안하다고 말하기 위해서 말야"),
        ("But it don't matter, it clearly doesn't tear you apart anymore", "하지만 상관없겠지, 그게 더 이상 널 힘들게(찢어지게) 하지 않는 게 분명하니까")
    ]
    questions = [
        ("1. 'I must've called a thousand times'의 뉘앙스는?", ["실제로 딱 1,000번 셌다", "아주 많이 연락했다는 강조", "전화기가 고장 났다"], "아주 많이 연락했다는 강조"),
        ("2. 화자가 치유(healing)에 대해 하는 말은?", ["시간 덕분에 다 나았다", "시간이 흘러도 별로 나아지지 않았다", "병원에 가야 한다"], "시간이 흘러도 별로 나아지지 않았다"),
        ("3. 'The other side'와 'The outside'는 무엇을 의미할까요?", ["옆집", "심리적/물리적으로 멀어진 현재의 위치", "외출 중인 상태"], "심리적/물리적으로 멀어진 현재의 위치"),
        ("4. 마지막 문장에서 화자가 깨달은 점은?", ["상대방도 나를 그리워한다", "상대방은 이제 더 이상 아파하지 않는다", "전화번호가 바뀌었다"], "상대방은 이제 더 이상 아파하지 않는다")
    ]

correct_order = [line[0] for line in full_lyrics]
# 퀴즈용 셔플 (순서 고정)
if song_choice == "Let It Go - Frozen OST":
    scrambled_order = [correct_order[3], correct_order[0], correct_order[7], correct_order[1], correct_order[5], correct_order[2], correct_order[8], correct_order[4], correct_order[6], correct_order[9]]
else:
    scrambled_order = [correct_order[5], correct_order[0], correct_order[9], correct_order[2], correct_order[7], correct_order[1], correct_order[8], correct_order[3], correct_order[6], correct_order[4]]

# -------------------------
# 탭 구성
# -------------------------
tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 배경 학습", "📖 STEP 2. 전체 가사 & 퀴즈", "🧩 STEP 3. 1절 순서 배열"])

with tab1:
    v1, v2, v3 = st.columns([1, 2, 1])
    with v2: st.video(video_url)
    st.markdown(f'<div class="info-box"><h3>📜 Song Story</h3>{bg_content}</div>', unsafe_allow_html=True)

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
    st.write("아래 문장들을 가사 순서대로 하나씩 클릭하세요!")
    
    b_cols = st.columns(2)
    for i, text in enumerate(scrambled_order):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(text, key=f"btn3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.session_state.show_q3_result = False
            st.rerun()

    st.divider()
    st.markdown("### 📥 내가 구성한 가사")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.92, 0.08])
        c1.info(f"{idx+1}: {card}")
        if c2.button("🗑️", key=f"del3_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.session_state.show_q3_result = False
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.get('show_q3_result'):
        st.markdown("### 📋 채점 리포트")
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]:
                st.success(f"Sentence {i+1}: Perfect!")
            else:
                st.error(f"Sentence {i+1}: Wrong Order")
                st.write(f"👉 **정답:** {correct_order[i]}")
                all_correct = False
        
        if all_correct:
            st.balloons()
            st.success(f"🎉 대단합니다! {song_choice} 1절을 완벽하게 마스터하셨네요!")
