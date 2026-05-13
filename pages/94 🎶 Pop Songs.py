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
    .info-box h3 { color: #4338ca; border-bottom: 2px solid #cbd5e1; padding-bottom: 10px; margin-top: 0; }
    .lyrics-container {
        padding: 8px 15px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f8fafc; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1.1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.9rem; color: #64748b; }
    .highlight { color: #4338ca; font-weight: 700; }
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
# [데이터 빌드 - 풍부해진 줄거리 버전]
# -------------------------
if song_choice == "Let It Go - Frozen OST":
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = """
    <h3>❄️ Let It Go: 완벽한 착한 소녀를 벗어던지다</h3>
    <p><b>[전체 줄거리]</b> 아렌델 왕국의 장녀 엘사는 태어날 때부터 손에 닿는 모든 것을 얼려버리는 강력하고 신비로운 마법을 가지고 태어났습니다. 하지만 어린 시절, 마법으로 동생 안나를 놀아주다 실수로 안나의 머리에 상처를 입히는 사고가 발생합니다. 이 일로 큰 충격을 받은 부모님은 엘사의 힘을 외부와 격리시키고, 엘사에게 "자신의 감정을 숨기고 마법을 억누르라"고 가르칩니다. 엘사는 동생마저 멀리한 채 장갑을 끼고 방 안에서만 평생을 고립되어 살아갑니다.</p>
    <p>세월이 흘러 부모님이 돌아가신 후 여왕 대관식이 열리던 날, 사소한 말다툼 끝에 통제력을 잃은 엘사의 마법이 온 세상 사람들 앞에서 폭발합니다. 사람들은 그녀를 '괴물'이라며 두려워하고, 엘사는 공포에 질려 북쪽 산으로 홀로 도망칩니다. </p>
    <p><b>[곡의 배경과 의미]</b> 이 곡은 고립된 눈산에서 홀로 남겨진 엘사가 부르는 노래입니다. 처음에는 두려움에 떨지만, 곧 <b>누구도 자신을 감시하지 않는 이곳이야말로 진정한 자유를 누릴 수 있는 곳</b>임을 깨닫습니다. "Conceal, don't feel"이라는 평생의 제약을 던져버리고, 자신의 잠재력을 마음껏 발산하며 얼음 성을 짓는 이 장면은 자아를 찾아가는 해방감을 상징합니다.</p>
    """
    # (가사 및 퀴즈 데이터 생략/기존과 동일)
    full_lyrics = [("The snow glows white on the mountain tonight...", "오늘 밤 산엔 눈이 하얗게 빛나고..."), ("...", "...")] # 실제 코드엔 전체 가사 포함

elif song_choice == "Hello - Adele":
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = """
    <h3>☎️ Hello: 닿지 않는 과거에 건네는 간절한 사과</h3>
    <p><b>[곡의 배경과 정서]</b> 아델의 'Hello'는 단순히 헤어진 연인에 대한 그리움을 넘어, <span class="highlight">세월의 흐름과 관계의 상실</span>에 대한 깊은 성찰을 담고 있습니다. 곡 속의 주인공은 화려한 도시 생활 속에서도 마음 한구석에 해결되지 않은 과거의 '미안함'을 품고 살아갑니다. 오랜 시간이 흘러 이제는 상대방의 번호조차 맞는지 확신할 수 없지만, 주인공은 용기를 내어 전화를 겁니다.</p>
    <p><b>[풍부한 서사]</b> 가사 속에서 주인공은 "우리가 어리고 자유로웠던 시절"을 회상합니다. 세상이 우리 발밑에 있었고 영원할 것 같았던 그때, 주인공은 상대방에게 큰 상처를 남기고 떠났습니다. 이제 어른이 된 주인공은 그 상처를 보듬기 위해 "반대편(The other side)"에서 전화를 겁니다. </p>
    <p><b>[노래의 의미]</b> "수천 번을 전화했다"는 표현은 물리적인 통화 횟수라기보다, <b>매일 밤 마음속으로 수만 번 되뇌었던 사과의 진심</b>을 뜻합니다. 비록 상대방은 이미 삶을 회복하여 전화를 받지 않거나 응답이 없지만, 주인공은 이 일방적인 고백을 통해 비로소 스스로의 죄책감에서 벗어나고자 하는 처절한 성장을 보여줍니다.</p>
    """
    # (데이터 생략)

else: # A Whole New World
    video_url = "https://www.youtube.com/watch?v=eitDnP0_83k"
    bg_content = """
    <h3>✨ A Whole New World: 성벽 너머, 새로운 운명을 향한 비행</h3>
    <p><b>[전체 줄거리]</b> 아그라바 왕국의 시장에서 좀도둑으로 살아가던 알라딘은 변장을 하고 성 밖으로 탈출한 자스민 공주를 우연히 도와주며 첫눈에 반하게 됩니다. 하지만 신분의 벽은 높기만 했죠. 알라딘은 램프의 요정 지니를 만나 '알리 왕자'로 변신한 뒤, 수많은 구혼자들에게 지쳐있던 자스민을 찾아갑니다.</p>
    <p>자스민 공주는 평생 궁궐이라는 화려한 감옥에 갇혀, 법률에 따라 사랑하지도 않는 왕자와 결혼해야 하는 운명에 처해 있었습니다. 알라딘은 그런 그녀에게 "나를 믿나요?"라고 물으며 마법 양탄자를 내밉니다. </p>
    <p><b>[곡의 배경과 의미]</b> 이 노래는 두 사람이 양탄자를 타고 구름 위와 세계 곳곳의 유적지를 누비며 부르는 환상적인 듀엣곡입니다. 단순히 아름다운 경치를 감상하는 노래가 아닙니다. <b>"A Whole New World"는 자스민에게는 '억압으로부터의 탈출'을, 알라딘에게는 '진실한 사랑'을 의미합니다.</b> 처음으로 자신의 눈으로 직접 세상을 마주하게 된 자스민과, 그녀에게 넓은 세상을 선물한 알라딘의 교감은 "누구도 우리에게 안 된다고 말할 수 없는" 주체적인 삶에 대한 찬가입니다.</p>
    """
    # (데이터 생략)

# (기존 full_lyrics, questions, scrambled_order 빌드 로직은 이전과 동일하게 유지)
# ... [중략] ...

# -------------------------
# 탭 구성
# -------------------------
tab1, tab2, tab3 = st.tabs(["🎬 STEP 1. 배경 학습", "📖 STEP 2. 전체 가사 & 퀴즈", "🧩 STEP 3. 1절 순서 배열"])

with tab1:
    v1, v2, v3 = st.columns([1, 4, 1])
    with v2: 
        st.video(video_url)
    # 영상 아래로 풍부해진 설명 배치
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)

# ... [이후 STEP 2, 3 로직 동일] ...
