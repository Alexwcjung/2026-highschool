import streamlit as st
import random
import string

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
        background-color: #f1f5f9; padding: 30px; border-radius: 15px;
        border: 1px solid #cbd5e1; line-height: 1.8; margin-bottom: 25px;
    }
    .lyrics-container {
        padding: 15px 20px; border-left: 5px solid #6366f1;
        margin-bottom: 12px; background-color: #f8fafc; border-radius: 0 10px 10px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. 세션 상태 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []

# -------------------------
# 3. 곡별 데이터 (여러 줄을 6개 덩어리로 묶음)
# -------------------------
def get_song_data(song_name):
    if "1. Let It Go" in song_name:
        return [
            ("The snow glows white on the mountain tonight, not a footprint to be seen.", "오늘 밤 산에는 눈이 하얗게 빛나고, 발자국 하나 보이지 않네요."),
            ("A kingdom of isolation, and it looks like I'm the queen.", "고립된 이 왕국에서 내가 마치 여왕인 것 같아요."),
            ("The wind is howling like this swirling storm inside. Couldn't keep it in, heaven knows I tried.", "내 안의 폭풍처럼 바람이 울부짖네요. 숨기려 했지만 하늘은 내 노력을 알 거예요."),
            ("Don't let them in, don't let them see. Be the good girl you always have to be.", "그들을 들이지 마, 보여주지 마. 언제나 그래야만 했던 착한 소녀가 되어라."),
            ("Conceal, don't feel, don't let them know. Well, now they know!", "숨기고, 느끼지 마, 알리지 마. 그런데 이제 그들이 알아버렸어!"),
            ("Let it go, let it go! Can't hold it back anymore.", "다 잊어, 이제 자유야! 더 이상 억누를 수 없어.")
        ]
    elif "2. Hello" in song_name:
        return [
            ("Hello, it's me. I was wondering if after all these years you'd like to meet.", "안녕, 나야. 이 모든 세월이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어."),
            ("To go over everything. They say that time's supposed to heal ya.", "모든 걸 짚어보기 위해. 시간이 치유해 줄 거라 다들 말하지만,"),
            ("But I ain't done much healing. Hello, can you hear me?", "난 별로 치유되지 않은 것 같아. 여보세요, 내 목소리 들리니?"),
            ("I'm in California dreaming about who we used to be.", "난 캘리포니아에서 우리가 예전에 어땠는지 꿈꾸고 있어."),
            ("When we were younger and free. I've forgotten how it felt before the world fell at our feet.", "우리가 더 어리고 자유로웠던 시절. 세상이 우리 발아래 있기 전의 기분이 어땠는지 잊어버렸어."),
            ("There's such a difference between us and a million miles.", "우리 사이엔 너무나 큰 차이와 수백만 마일의 거리감이 느껴져.")
        ]
    elif "3. A Whole New World" in song_name:
        return [
            ("I can show you the world. Shining, shimmering, splendid.", "당신에게 세상을 보여줄 수 있어요. 빛나고 반짝이며 화려한 세상을."),
            ("Tell me, princess, now when did you last let your heart decide?", "공주님, 마지막으로 당신의 마음이 결정하게 둔 게 언제였나요?"),
            ("I can open your eyes, take you wonder by wonder.", "당신의 눈을 뜨게 해서 경이로운 곳들로 하나씩 데려가 줄게요."),
            ("Over, sideways and under on a magic carpet ride.", "마법 양탄자를 타고 위아래, 옆으로 누비며 말이죠."),
            ("A whole new world! A new fantastic point of view.", "완전히 새로운 세상! 환상적인 새로운 시야예요."),
            ("No one to tell us 'No' or where to go, or say we're only dreaming.", "아무도 우리에게 안 된다거나 어디로 가라고, 혹은 꿈일 뿐이라고 말하지 않아요.")
        ]
    elif "4. Stand By Me" in song_name:
        return [
            ("When the night has come and the land is dark.", "밤이 찾아오고 대지가 어두워질 때."),
            ("And the moon is the only light we'll see.", "저 달빛이 우리가 볼 수 있는 유일한 빛일 때."),
            ("No, I won't be afraid. Oh, I won't be afraid.", "난 두렵지 않을 거예요. 정말 두렵지 않아요."),
            ("Just as long as you stand, stand by me.", "당신이 내 곁에 서 있어 주기만 한다면요."),
            ("So darling, darling, stand by me, oh, stand by me.", "그러니 그대여, 내 곁에 서 주세요. 내 곁에 있어 줘요."),
            ("If the sky that we look upon should tumble and fall.", "우리가 바라보는 저 하늘이 무너져 내린다고 해도.")
        ]
    else: # 5. Don't Know Why
        return [
            ("I waited 'til I saw the sun. I don't know why I didn't come.", "난 해가 뜰 때까지 기다렸어요. 내가 왜 가지 않았는지 모르겠어요."),
            ("I left you by the house of fun. I don't know why I didn't come.", "당신을 축제의 집 근처에 남겨둔 채로요. 왜 가지 않았는지 정말 모르겠어요."),
            ("When I saw the break of day, I wished that I could fly away.", "새벽이 밝아올 때 난 멀리 날아가 버리고 싶었죠."),
            ("Instead of kneeling in the sand, catching teardrops in my hand.", "모래 위에 무릎 꿇고 손바닥으로 눈물을 받는 대신에요."),
            ("My heart is drenched in wine, but you'll be on my mind forever.", "내 마음은 술에 흠뻑 젖었지만, 당신은 영원히 내 마음속에 있을 거예요."),
            ("Out across the endless sea, I would die in ecstasy.", "끝없는 바다 건너에서 난 황홀하게 죽을 수도 있었겠죠.")
        ]

# -------------------------
# 4. 상단 컨트롤 및 탭
# -------------------------
st.markdown('<div class="main-title"><h1>🎵 Pop Song English : Sequence Quiz</h1></div>', unsafe_allow_html=True)

song_choice = st.selectbox("👉 노래 선택", song_options := [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
])

# 곡 변경 시 초기화
if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    st.session_state.q3_cards = []
    if 'scrambled' in st.session_state: del st.session_state.scrambled

tab1, tab2, tab3 = st.tabs(["🎬 배경 학습", "📖 가사 확인", "🧩 순서 배열 (6문장)"])

current_lyrics = get_song_data(song_choice)

# -------------------------
# 5. 탭 구현
# -------------------------
with tab1:
    st.info("먼저 노래를 들으며 전체적인 분위기와 가사를 느껴보세요.")
    urls = {
        "1. Let It Go": "https://www.youtube.com/watch?v=L0MK7qz13bU",
        "2. Hello": "https://www.youtube.com/watch?v=YQHsXMglC9A",
        "3. A Whole New World": "https://www.youtube.com/watch?v=eitDnP0_83k",
        "4. Stand By Me": "https://www.youtube.com/watch?v=Us-TVg40ExM",
        "5. Don't Know Why": "https://www.youtube.com/watch?v=tO4dxvguQDk"
    }
    st.video(next(v for k, v in urls.items() if k in song_choice))

with tab2:
    st.markdown("### 🎼 First Verse Lyrics")
    for i, (eng, kor) in enumerate(current_lyrics):
        label = list(string.ascii_lowercase)[i]
        st.markdown(f'''
            <div class="lyrics-container">
                <div class="eng-line">({label}) {eng}</div>
                <div class="kor-sub">{kor}</div>
            </div>
        ''', unsafe_allow_html=True)

with tab3:
    st.subheader("🧩 가사 순서대로 클릭하세요")
    st.caption("가사 앞의 (a)~(f) 기호를 보고 노래 순서대로 버튼을 누르세요. 딱 6개입니다!")

    # 정답지 생성
    correct_order = [f"({list(string.ascii_lowercase)[i]}) {line[0]}" for i, line in enumerate(current_lyrics)]
    
    # 섞기 (세션 유지)
    if 'scrambled' not in st.session_state:
        st.session_state.scrambled = random.sample(correct_order, len(correct_order))

    # 버튼 인터페이스
    cols = st.columns(2)
    for i, text in enumerate(st.session_state.scrambled):
        is_selected = text in st.session_state.q3_cards
        if (cols[i % 2]).button(text, key=f"btn_{i}", use_container_width=True, disabled=is_selected):
            st.session_state.q3_cards.append(text)
            st.rerun()

    st.divider()
    
    # 선택된 목록
    st.write("📝 **내가 배열한 순서:**")
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.9, 0.1])
        c1.info(f"{idx+1}번: {card}")
        if c2.button("🗑️", key=f"del_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()

    # 결과 확인
    if len(st.session_state.q3_cards) == 6:
        if st.button("🚩 최종 채점 하기", type="primary", use_container_width=True):
            is_all_correct = True
            for i, user_pick in enumerate(st.session_state.q3_cards):
                if user_pick == correct_order[i]:
                    st.success(f"{i+1}번 문장: 정답입니다!")
                else:
                    st.error(f"{i+1}번 문장: 오답입니다. (원래 순서: {correct_order[i]})")
                    is_all_correct = False
            
            if is_all_correct:
                st.balloons()
                st.success("🎉 완벽합니다! 1절의 순서를 모두 맞히셨습니다!")
