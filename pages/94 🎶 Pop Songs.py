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
# 2. 곡별 데이터 (배경 & 가사)
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h2>❄️ Let It Go: 억압의 사슬을 끊고 진정한 자신으로</h2>
    아렌델 왕국의 공주 <b>엘사</b>는 모든 것을 얼려버리는 마법 능력을 가지고 태어났습니다. 하지만 부모님은 이를 저주라 여겨 엘사에게 <b>"감추고, 느끼지 말라(Conceal, don't feel)"</b>고 가르치며 세상으로부터 격리시킵니다. 
    <br><br>성인이 되어 대관식을 치르던 날, 실수로 능력이 탄로 난 엘사는 사람들의 두려움 섞인 시선을 피해 북쪽 산으로 도망칩니다. 이 곡은 그곳에서 홀로 남겨진 엘사가 더 이상 남의 눈치를 보지 않고, 자신의 힘을 마음껏 펼치며 자유를 선언하는 순간을 담고 있습니다. 
    <br><br>차가운 눈 산은 이제 고립의 장소가 아닌, 엘사만의 왕국이 됩니다. "내버려 둬(Let it go)"라는 외침은 과거의 두려움과 결별하고 주체적인 삶을 살겠다는 강력한 의지의 표명입니다.
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
    세계적인 디바 <b>아델(Adele)</b>의 'Hello'는 단순한 이별 노래를 넘어선 성찰의 기록입니다. 아델은 이 곡이 <b>"과거의 모든 사람과 나 자신에게 건네는 인사"</b>라고 설명했습니다. 
    <br><br>곡의 주인공은 수년이 흐른 뒤, 과거에 상처를 주었던 연인에게 전화를 겁니다. 상대방은 이미 그 일을 잊었거나 더 이상 화가 나 있지 않을 수도 있지만, 주인공은 자신의 미안함을 전달함으로써 비로소 과거로부터 자유로워지길 원합니다. 
    <br><br>시간이 모든 걸 해결해 줄 거라 믿었지만 여전히 아픈 마음을 담백하고 웅장하게 표현한 곡입니다.
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
        ("4. 'Younger and free'했던 시절은 언제인가요?", ["과거", "현재"], "과거"),
        ("5. 화자는 상대방과 만나서 무엇을 하고 싶어 하나요?", ["모든 걸 되짚어보기", "돈 빌리기"], "모든 걸 되짚어보기"),
        ("6. 화자는 현재 충분히 치유되었나요?", ["아니오", "예"], "아니오")
    ]

# [중략] 다른 곡들도 위와 같은 패턴으로 배경 학습 내용을 풍부하게 채워 넣으시면 됩니다.
else: # 임시 방어 코드
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h2>🎵 준비 중인 곡입니다</h2>내용을 추가해 주세요."
    lyrics_raw = [("Lyrics will be updated", "가사가 업데이트될 예정입니다")] * 10
    questions = [("Q", ["A", "B"], "A")] * 6

# -------------------------
# 가사 데이터 인덱싱 (안전하게 처리)
# -------------------------
processed_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = f"L{i+1:02d}" # alphabet 대신 L01, L02 형태로 안전하게 생성
    processed_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in processed_lyrics]

# 섞인 가사 세션 저장
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

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
        # 폼 ID에 곡 이름을 넣어 충돌 방지
        with st.form(key=f"quiz_form_{song_choice}"):
            user_answers = []
            for i, (q, opts, ans) in enumerate(questions):
                user_ans = st.radio(q, opts, key=f"radio_{song_choice}_{i}", index=None)
                user_answers.append(user_ans)
            
            if st.form_submit_button("퀴즈 정답 확인"):
                score = 0
                for i, (q, opts, ans) in enumerate(questions):
                    if user_answers[i] == ans: score += 1
                    else: st.error(f"X {i+1}번 오답: 정답은 [{ans}]")
                if score == 6: st.balloons(); st.success("Perfect! 완벽합니다.")
    with l_col:
        st.markdown("### 🎼 Lyrics Study (Verse 1)")
        for eng, kor in processed_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.info("아래 가사 조각을 순서대로 클릭하세요.")
    cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        col_idx = i % 2
        is_selected = text in st.session_state.q3_cards
        if cols[col_idx].button(text, key=f"btn_{song_choice}_{i}", use_container_width=True, disabled=is_selected):
            st.session_state.q3_cards.append(text)
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📝 제출 순서")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.85, 0.15])
        c1.warning(f"{idx+1}: {card}")
        if c2.button("취소", key=f"del_{song_choice}_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.show_q3_result:
        st.markdown("### 🏁 채점 결과")
        all_correct = True
        for i in range(len(correct_order)):
            u_val = st.session_state.q3_cards[i]
            a_val = correct_order[i]
            if u_val == a_val:
                st.success(f"Step {i+1}: Correct! ✅")
            else:
                st.error(f"Step {i+1}: Wrong! ❌ (정답: {a_val})")
                all_correct = False
        
        if all_correct: st.balloons(); st.success("모든 순서를 맞췄습니다!")
        if st.button("다시 하기"): reset_data(); st.rerun()
