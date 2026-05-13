import streamlit as st
import random
import string

# =========================
# 1. 스타일 최적화
# =========================
st.set_page_config(page_title="Music English Master", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 1rem !important; }
    
    .guide-text {
        font-size: 1.1rem; font-weight: 700; color: #1e3a8a;
        margin-bottom: 10px; display: block;
    }
    
    .info-box {
        background-color: #f8fafc; padding: 25px; border-radius: 12px;
        border: 1px solid #e2e8f0; line-height: 1.8; font-size: 1rem; margin-bottom: 20px;
    }
    .info-box h3 { font-size: 1.4rem; color: #4338ca; margin-bottom: 12px; border-bottom: 3px solid #6366f1; padding-bottom: 5px; }
    .info-box b { color: #1e3a8a; }
    .info-box i { color: #475569; font-style: normal; display: block; margin-top: 10px; padding-left: 10px; border-left: 2px solid #cbd5e1; }
    
    .lyrics-container {
        padding: 12px; border-left: 4px solid #6366f1;
        margin-bottom: 10px; background-color: #f1f5f9; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.05rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    st.session_state.current_tab = "🎬 배경 학습"
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

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

# -------------------------
# 곡별 풍부한 데이터 설정
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 억압된 자아의 화려한 해방</h3>
    <p>디즈니 애니메이션 <b>'겨울왕국(Frozen)'</b>의 절정부에서 엘사가 부르는 곡입니다. 엘사는 태어날 때부터 가진 강력한 마법 능력을 '저주'라 생각하며 평생을 숨기고 절제하며 살아왔습니다. 하지만 자신의 능력이 세상에 드러나자, 그녀는 비로소 사회적 기대와 '착한 소녀'라는 프레임을 벗어던지고 북쪽 산으로 향합니다.</p>
    <b>[핵심 서사]</b> 이 노래는 단순한 가출이 아니라, <b>자기 수용(Self-Acceptance)</b>의 과정을 상징합니다. 가사 속 "The cold never bothered me anyway"는 물리적 추위가 아니라 타인의 차가운 시선조차 더 이상 나를 흔들 수 없다는 강력한 자존감을 의미합니다.
    <i>💡 <b>영어 포인트:</b> 'Conceal, don't feel'이라는 반복구는 엘사가 평생 받아온 억압적인 교육을 단적으로 보여줍니다.</i>
    """
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어요"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었죠, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마요, 보여주지 마요"),
        ("Be the good girl you always have to be", "늘 그래야만 했던 착한 소녀가 되세요"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마요, 모르게 하세요"),
        ("Let it go, let it go! Can't hold it back anymore", "다 잊어버려요! 더는 억누를 수 없어요")
    ]
    questions = [
        ("1. 엘사가 현재 느끼는 감정은?", ["자유와 해방", "공포와 절망", "분노"], "자유와 해방"),
        ("2. 'Conceal'의 의미는?", ["숨기다", "드러내다", "공유하다"], "숨기다"),
        ("3. 'The cold'가 비유하는 것은?", ["사회적 시선", "실제 날씨", "겨울 휴가"], "사회적 시선"),
        ("4. 'Good girl'은 무엇을 상징하나요?", ["타인의 기대", "자신의 본 모습", "동생 안나"], "타인의 기대"),
        ("5. 'Isolation'의 뜻은?", ["고립/격리", "함께함", "승리"], "고립/격리"),
        ("6. 'Storm inside'는 무엇을 비유하나요?", ["억눌린 감정", "마법의 힘", "기상 이변"], "억눌린 감정")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 과거의 나, 그리고 너에게 건네는 사과</h3>
    <p>아델(Adele)의 3집 앨범 25의 타이틀곡입니다. 이 노래는 이별한 연인에게 전화를 거는 상황을 담고 있지만, 더 깊게는 <b>'시간의 흐름'</b>과 <b>'후회'</b>에 대해 이야기합니다. 아델은 이 곡이 과거의 자신을 포함해 자신이 상처를 주었던 모든 사람에게 건네는 화해의 메시지라고 설명했습니다.</p>
    <b>[핵심 서사]</b> "Hello from the other side"라는 가사는 단순히 전화기 너머를 뜻하는 것이 아니라, 돌아갈 수 없는 <b>과거와 현재 사이의 보이지 않는 벽</b>을 상징합니다. 수천 번 전화를 걸었다는 고백은 결코 닿을 수 없는 사과에 대한 간절함과 고통을 극대화합니다.
    <i>💡 <b>영어 포인트:</b> 'I was wondering if...'는 아주 정중하고 조심스럽게 무언가를 물어볼 때 쓰는 표현으로, 화자의 미안함이 잘 묻어납니다.</i>
    """
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "이 모든 시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("Hello, can you hear me?", "여보세요, 내 말 들리니?"),
        ("I'm in California dreaming about who we used to be", "난 캘리포니아에서 예전의 우리 모습을 꿈꾸고 있어"),
        ("Hello from the other side", "반대편에서 인사해"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야")
    ]
    questions = [
        ("1. 화자가 전화를 거는 이유는?", ["미안함을 전하려고", "돈을 빌리려고", "복수하려고"], "미안함을 전하려고"),
        ("2. 'a thousand times'의 의미는?", ["간절한 반복", "정확히 1,000번", "단 한 번"], "간절한 반복"),
        ("3. 'Other side'는 무엇을 뜻하나?", ["이별 후의 현재 상태", "지구 반대편", "저세상"], "이별 후의 현재 상태"),
        ("4. 노래의 분위기는?", ["그리움과 후회", "환희와 희망", "무관심"], "그리움과 후회"),
        ("5. 'Wondering'의 뜻은?", ["궁금해하다", "확신하다", "무시하다"], "궁금해하다"),
        ("6. 'who we used to be'는 무엇인가?", ["과거의 우리 모습", "미래의 우리", "지금의 나"], "과거의 우리 모습")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 금기된 성벽을 넘어선 자유</h3>
    <p>영화 <b>'알라딘(Aladdin)'</b>에서 알라딘과 자스민 공주가 마법 양탄자를 타고 밤하늘을 날며 부르는 로맨틱한 곡입니다. 성안에 갇혀 세상 구경을 하지 못했던 공주에게 알라딘은 '완전히 새로운 세상'을 선물합니다.</p>
    <b>[핵심 서사]</b> 이 곡은 단순한 로맨스를 넘어 <b>시각의 확장(Expansion of Perspective)</b>을 노래합니다. "Let your heart decide"라는 가사는 타인에 의해 결정되는 삶이 아닌, 스스로의 의지로 세상을 바라보겠다는 자스민의 변화를 보여줍니다. 둘에게 펼쳐진 밤하늘은 경계가 없는 무한한 가능성을 의미합니다.
    <i>💡 <b>영어 포인트:</b> 'Shining, shimmering, splendid'처럼 유사한 소리의 형용사를 나열하여 세상을 마주한 경이로움을 강조합니다.</i>
    """
    lyrics_raw = [
        ("I can show you the world", "당신에게 세상을 보여줄 수 있어요"),
        ("Shining, shimmering, splendid", "빛나고 어른거리며 화려한 세상을요"),
        ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 마음이 가는 대로 결정했던 게 언제였나요?"),
        ("I can open your eyes", "당신의 눈을 뜨게 해 줄게요"),
        ("Take you wonder by wonder", "경이로운 곳들로 데려가 줄게요"),
        ("A whole new world! A new fantastic point of view", "완전히 새로운 세상! 환상적인 새로운 시야죠")
    ]
    questions = [
        ("1. 'Crystal clear'의 문맥적 의미는?", ["아주 명확한", "차가운", "딱딱한"], "아주 명확한"),
        ("2. 노래의 주제와 가장 가까운 것은?", ["자유와 새로운 시각", "성벽의 안전함", "양탄자의 속도"], "자유와 새로운 시각"),
        ("3. 'Splendid'의 뜻은?", ["화려한/훌륭한", "평범한", "어두운"], "화려한/훌륭한"),
        ("4. 알라딘이 강조하는 것은 무엇인가?", ["주체적인 결정", "공주의 외모", "성안의 보물"], "주체적인 결정"),
        ("5. 'Wonder by wonder'가 주는 느낌은?", ["끊임없는 감동", "지루함", "두려움"], "끊임없는 감동"),
        ("6. 'Fantastic point of view'의 의미는?", ["환상적인 시야", "거짓된 생각", "어지러운 풍경"], "환상적인 시야")
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = """
    <h3>🤝 Stand By Me: 어둠 속에서 빛나는 연대와 신뢰</h3>
    <p>벤 E. 킹(Ben E. King)의 명곡으로, 수많은 아티스트들이 리메이크한 전 세계적인 찬가입니다. 시편에서 영감을 얻은 이 곡은 인생의 험난한 시기를 견디게 해주는 <b>'곁에 있는 사람'</b>에 대한 깊은 신뢰를 담고 있습니다.</p>
    <b>[핵심 서사]</b> 노래 속 "The night has come"이나 "The sky should tumble and fall"은 인생에서 마주하는 거대한 시련과 재앙을 뜻합니다. 하지만 화자는 달빛만이 유일한 빛인 절망적인 상황에서도 두려워하지 않겠다고 선언합니다. 그 이유는 오직 하나, "당신이 내 곁에 서 있기 때문"입니다.
    <i>💡 <b>영어 포인트:</b> 'Stand by someone'은 단순히 옆에 서 있는 것이 아니라 '어려운 상황에서도 지지하고 편이 되어주다'라는 강력한 수거입니다.</i>
    """
    lyrics_raw = [
        ("When the night has come and the land is dark", "밤이 오고 사방이 어두워질 때"),
        ("And the moon is the only light we'll see", "저 달빛만이 우리가 볼 수 있는 유일한 빛일 때"),
        ("No, I won't be afraid. Oh, I won't be afraid", "난 두렵지 않을 거예요"),
        ("Just as long as you stand, stand by me", "당신이 내 곁에 서 있어 주기만 한다면요"),
        ("If the sky that we look upon should tumble and fall", "우리가 보는 저 하늘이 무너져 내린다 해도"),
        ("I won't cry, I won't cry. No, I won't shed a tear", "난 울지 않을 거예요")
    ]
    questions = [
        ("1. 화자가 두려움을 이기는 원동력은?", ["함께하는 사람", "밝은 햇빛", "많은 재산"], "함께하는 사람"),
        ("2. 'Shed a tear'의 뜻은?", ["눈물을 흘리다", "미소 짓다", "소리 지르다"], "눈물을 흘리다"),
        ("3. 'Tumble and fall'은 무엇을 상징하나?", ["거대한 시련", "계절의 변화", "낮잠"], "거대한 시련"),
        ("4. 'The night'는 어떤 상황을 비유하나?", ["인생의 고난", "실제 밤 시간", "정전"], "인생의 고난"),
        ("5. 'Stand by me'의 핵심 의미는?", ["지지와 동행", "옆에 서 있기", "길 비켜주기"], "지지와 동행"),
        ("6. 'Only light'인 달빛은 무엇을 의미하나?", ["마지막 희망", "절대적 어둠", "인공 조명"], "마지막 희망")
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = """
    <h3>🍂 Don't Know Why: 망설임 끝에 놓쳐버린 인연의 무게</h3>
    <p>노라 존스(Norah Jones)의 데뷔 앨범 타이틀곡으로, 9개의 그래미상을 휩쓴 명곡입니다. 이 곡은 잡을 수 있었던 인연을 <b>막연한 두려움과 망설임</b> 때문에 놓아버린 후 느끼는 공허함을 재즈풍의 선율에 담아냈습니다.</p>
    <b>[핵심 서사]</b> 가사에서 화자는 "내가 왜 가지 않았는지 모르겠다"고 반복하며 자책합니다. 상대는 'House of fun(축제의 집)'에 있었지만, 화자는 그곳으로 향하지 못하고 새벽까지 홀로 해를 기다립니다. "My heart is drenched in wine(내 마음은 술에 젖었다)"이나 "Empty as a drum(드럼처럼 텅 빈)" 같은 표현은 상실감으로 인해 피폐해진 내면을 문학적으로 묘사합니다.
    <i>💡 <b>영어 포인트:</b> 'I don't know why'의 반복은 후회하는 마음의 지독한 굴레를 상징합니다.</i>
    """
    lyrics_raw = [
        ("I waited 'til I saw the sun", "난 해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "내가 왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 축제의 집 근처에 남겨둔 채로요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 올 때 난 멀리 날아가 버리고 싶었죠"),
        ("My heart is drenched in wine, but you'll be on my mind forever", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요"),
        ("I feel as empty as a drum, I don't know why I didn't come", "텅 빈 드럼처럼 공허해요")
    ]
    questions = [
        ("1. 이 노래의 지배적인 정서는?", ["후회와 아쉬움", "기쁨", "분노"], "후회와 아쉬움"),
        ("2. 'Drenched in wine'이 비유하는 것은?", ["슬픔에 푹 젖은 마음", "즐거운 파티", "갈증"], "슬픔에 푹 젖은 마음"),
        ("3. 'Bag of bones'는 어떤 상태인가?", ["무기력하고 야윈 모습", "건강한 모습", "무거운 짐"], "무기력하고 야윈 모습"),
        ("4. 화자가 약속 장소에 가지 않은 이유는?", ["알 수 없는 망설임", "약속을 잊음", "상대의 거절"], "알 수 없는 망설임"),
        ("5. 'Empty as a drum'은 무엇을 강조하나?", ["내면의 공허함", "악기 연주 실력", "소음"], "내면의 공허함"),
        ("6. 'I don't know why' 반복의 효과는?", ["후회의 감정 극대화", "단어 공부", "시간 채우기"], "후회의 감정 극대화")
    ]

# -------------------------
# 가사/순서 가공 (a, b, c...)
# -------------------------
alphabet = list(string.ascii_lowercase)
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 화면 출력
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
    st.video(video_url)
    st.divider()
    for eng, kor in full_lyrics:
        st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)
    st.divider()
    st.markdown("### 💡 Comprehension Quiz")
    with st.form(f"q_{song_choice}"):
        for i, (q, opts, ans) in enumerate(questions):
            q_text = q
            if st.session_state.submitted_step2:
                user_val = st.session_state.get(f"qs_{i}")
                q_text += " ✅" if user_val == ans else f" 🔍 ({ans})"
            st.radio(q_text, opts, index=None, key=f"qs_{i}")
        if st.form_submit_button("채점하기"):
            st.session_state.submitted_step2 = True
            st.rerun()

elif selected_tab == "🧩 순서 배열":
    st.info("가사 순서(a, b, c...)대로 클릭하여 문장을 완성하세요!")
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if st.button(text, key=f"b3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    st.divider()
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.85, 0.15])
        c1.write(f"{idx+1}: {card}")
        if c2.button("X", key=f"d3_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
    
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()
            
    if st.session_state.get('show_q3_result'):
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"{i+1}: OK")
            else:
                st.error(f"{i+1}: NO (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
