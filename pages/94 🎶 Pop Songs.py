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
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 상태 관리 (데이터 초기화 함수)
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'show_q3_result' not in st.session_state: st.session_state.show_q3_result = False

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    if 'scrambled' in st.session_state: del st.session_state.scrambled

# -------------------------
# 상단 곡 선택 메뉴 (곡 앞에 번호 1, 2, 3, 4 부여)
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
st.markdown('<span class="big-label">👉 학습할 노래를 선택하세요</span>', unsafe_allow_html=True)
song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King"
]
song_choice = st.selectbox("노래 선택", song_options, label_visibility="collapsed", key="main_song_select")

# 곡이 바뀌면 데이터 리셋
if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# -------------------------
# [곡별 데이터 구성]
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go</h3><p>모든 것을 얼려버리는 마법을 숨기며 살아온 엘사의 자유를 향한 선언입니다.</p>"
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
        ("1. 엘사의 현재 심경은?", ["공포", "해방감", "분노"], "해방감"),
        ("2. 'Conceal'의 뜻은?", ["드러내다", "숨기다", "공격하다"], "숨기다"),
        ("3. 'them'은 누구를 의미하나?", ["산짐승", "사람들", "나쁜 마법사"], "사람들"),
        ("4. 'The cold never bothered me'의 의미?", ["감기 걸렸다", "추위는 상관없다", "눈이 싫다"], "추위는 상관없다"),
        ("5. 엘사가 있는 장소의 특징은?", ["사람이 많다", "고립되어 있다", "따뜻하다"], "고립되어 있다"),
        ("6. 'Let it go'의 뜻은?", ["다 잊어버려", "그걸 내게 줘", "멀리 가버려"], "다 잊어버려")
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello</h3><p>세월이 흐른 뒤, 과거의 인연에게 건네는 뒤늦은 사과와 진심을 담고 있습니다.</p>"
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
    questions = [
        ("1. 전화를 거는 주된 목적은?", ["부탁", "사과", "조르기"], "사과"),
        ("2. 'a thousand times'의 의미?", ["정확히 1000번", "간절함", "번호 오기입"], "간절함"),
        ("3. 'California'는?", ["현재 위치", "고향", "여행 계획"], "현재 위치"),
        ("4. 'The other side'가 비유하는 것은?", ["죽음의 세계", "멀어진 현재 상태", "지구 반대편"], "멀어진 현재 상태"),
        ("5. 상대방은 현재 어떤가?", ["슬퍼함", "더 이상 아프지 않음", "전화기 꺼짐"], "더 이상 아프지 않음"),
        ("6. 'Time's supposed to heal ya'의 뜻?", ["시간이 약이다", "시간을 멈추고 싶다", "시간이 빠르다"], "시간이 약이다")
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = "<h3>✨ A Whole New World</h3><p>마법 양탄자를 타고 자유와 주체적인 삶을 마주하는 경이로운 순간입니다.</p>"
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
    questions = [
        ("1. 두 사람이 타고 있는 수단은?", ["양탄자", "빗자루", "구름"], "양탄자"),
        ("2. 'Let your heart decide'의 의미?", ["심장 수술", "마음이 시키는 대로", "이성적 판단"], "마음이 시키는 대로"),
        ("3. 'A whole new world'가 상징하는 것은?", ["우주", "자유와 주체적 삶", "이민"], "자유와 주체적 삶"),
        ("4. 'Crystal clear'의 뜻?", ["수정 깨끗함", "매우 명확함", "유리 같다"], "매우 명확함"),
        ("5. 자스민이 느끼는 기분은?", ["두려움", "경이로움", "지루함"], "경이로움"),
        ("6. 'No one to tell us 'No''의 의미?", ["대답 없음", "아무도 간섭 못 함", "모두 예라고 함"], "아무도 간섭 못 함")
    ]

else: # Stand By Me
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h3>🤝 Stand By Me</h3><p>어떤 시련이 닥칠지라도 곁에 의지할 누군가가 있다면 두렵지 않다는 메시지입니다.</p>"
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
    questions = [
        ("1. 노래의 시간적 배경은?", ["한낮", "해질녘", "한밤중"], "한밤중"),
        ("2. 'Stand by me'의 의미는?", ["내 앞에 서라", "내 곁을 지켜달라", "일어서라"], "내 곁을 지켜달라"),
        ("3. 화자가 두렵지 않은 조건은?", ["돈", "달빛", "상대방이 곁에 있을 때"], "상대방이 곁에 있을 때"),
        ("4. 'Shed a tear'의 뜻은?", ["편지", "눈물 흘리기", "화내기"], "눈물 흘리기"),
        ("5. 시련 비유가 아닌 것은?", ["밤", "하늘 무너짐", "달빛"], "달빛"),
        ("6. 'Just as long as'의 뜻은?", ["~하는 한", "오랫동안", "길이 같음"], "~하는 한")
    ]

# 가사 섞기 로직
correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))

# -------------------------
# 탭 구성 (고유 키 적용하여 에러 방지)
# -------------------------
tab1, tab2, tab3 = st.tabs(["1. 🎬 배경 학습", "2. 📖 전체 가사 & 퀴즈", "3. 🧩 순서 배열"])

with tab1:
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: 
        st.video(video_url, key="vid_tab1") # 고유 키: vid_tab1

with tab2:
    col_v, col_l = st.columns([1, 1.2])
    with col_v:
        # 2번 탭 영상 (고유 키: vid_tab2)
        st.video(video_url, key="vid_tab2")
        st.divider()
        st.markdown("### 💡 Comprehension Quiz (6문항)")
        # 폼 내부의 위젯도 유니크 키가 필요함
        with st.form(key=f"quiz_form_{song_choice}"):
            for i, (q, opts, ans) in enumerate(questions):
                q_label = q
                if st.session_state.submitted_step2:
                    user_val = st.session_state.get(f"q_ans_{i}")
                    if user_val == ans:
                        q_label += " ✅"
                    else:
                        q_label += f" ❌ (정답: {ans})"
                st.radio(q_label, opts, index=None, key=f"q_ans_{i}")
            
            if st.form_submit_button("정답 확인"):
                st.session_state.submitted_step2 = True
                st.rerun()
    with col_l:
        st.markdown("### 🎼 가사 확인 (Section 1)")
        for eng, kor in full_lyrics:
            st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 1절 문장 순서 맞추기")
    st.write("가사 순서대로 아래 버튼을 클릭하세요!")
    
    # 버튼 배열
    b_cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if (b_cols[0] if i % 2 == 0 else b_cols[1]).button(text, key=f"scr_btn_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.session_state.show_q3_result = False
            st.rerun()
            
    st.divider()
    # 선택된 카드 목록 표시
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}: {card}")
        if c2.button("❌", key=f"del_card_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
            
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("🚩 최종 결과 확인", type="primary", use_container_width=True, key="chk_res_btn"):
            st.session_state.show_q3_result = True
            st.rerun()

    if st.session_state.show_q3_result:
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]:
                st.success(f"{i+1}: Perfect!")
            else:
                st.error(f"{i+1}: Wrong Order (정답: {correct_order[i]})")
                all_correct = False
        if all_correct:
            st.balloons()
