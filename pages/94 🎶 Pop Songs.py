import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Lyrics Training: Lion King",
    page_icon="🎤",
    layout="wide"
)

# =========================
# 고급 CSS 디자인 (Lyrics Training 스타일)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } /* 다크 모드 스타일 */
    .title-box {
        background: linear-gradient(90deg, #1e40af, #7e22ce);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    /* 가사 박스: 스크롤 가능하고 가독성 높게 */
    .lyrics-window {
        background-color: #1e293b;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #334155;
        height: 550px;
        overflow-y: auto;
        line-height: 2.5;
        font-size: 1.25rem;
        font-family: 'Courier New', monospace;
        color: #cbd5e1;
    }
    .highlight {
        background-color: #eab308;
        color: #000;
        padding: 2px 8px;
        border-radius: 5px;
        font-weight: bold;
        margin: 0 3px;
    }
    .stRadio > div { flex-direction: row; gap: 15px; } /* 선택지 가로 정렬 */
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>🎤 Lyrics Training: Can You Feel the Love Tonight</h1></div>', unsafe_allow_html=True)

# =========================
# 데이터 설정 (가사 지점별 문제)
# =========================
# 정답 리스트: surrender, world, worrier, wanderer, far, vagabonds, learn, turn, outdoors, voyager, yours, best
options = [
    ["surrender", "surprise", "sunlight"], # 1
    ["wave", "world", "word"],             # 2
    ["warrior", "worrier", "worker"],      # 3
    ["wanderer", "wonderer", "winner"],    # 4
    ["fast", "far", "fair"],               # 5
    ["vacation", "vagabonds", "victory"],  # 6
    ["learn", "lean", "leave"],            # 7
    ["time", "tune", "turn"],              # 8
    ["outdoors", "outdoorsy", "outside"],  # 9
    ["voyager", "voter", "voice"],         # 10
    ["yours", "young", "years"],           # 11
    ["best", "beast", "blast"]             # 12
]

# =========================
# 메인 레이아웃
# =========================
tab_play, tab_score = st.tabs(["🎮 Game Mode", "📊 Result"])

with tab_play:
    col_vid, col_lyric = st.columns([1, 1.2])

    with col_vid:
        st.subheader("📺 Watch Video")
        st.video("https://www.youtube.com/watch?v=25QyCxVkXwQ")
        
        st.markdown("---")
        st.markdown("### ⌨️ 빈칸을 채워주세요!")
        
        # 실제 입력을 받는 구역 (스크롤하며 풀기 좋게)
        u1 = st.selectbox("Q1", options[0], key="u1")
        u2 = st.selectbox("Q2", options[1], key="u2")
        u3 = st.selectbox("Q3", options[2], key="u3")
        u4 = st.selectbox("Q4", options[3], key="u4")
        u5 = st.selectbox("Q5", options[4], key="u5")
        u6 = st.selectbox("Q6", options[5], key="u6")

    with col_lyric:
        st.subheader("📜 Fill in the Blanks")
        # 가사 전체 출력 (음영 처리)
        lyrics_content = """
        <div class="lyrics-window">
        There's a calm <span class="highlight">1</span><br>
        To the rush of day<br>
        When the heat of the rolling <span class="highlight">2</span><br>
        Can be turned away<br>
        And enchanted moment<br>
        And it sees me through<br>
        It's enough for this restless <span class="highlight">3</span><br>
        Just to be with you<br><br>
        And can you feel the love tonight?<br>
        It is where we are<br>
        It's enough for this wide-eyed <span class="highlight">4</span><br>
        That we got this <span class="highlight">5</span><br>
        And can you feel the love tonight?<br>
        How it's laid to rest?<br>
        It's enough to make kings and <span class="highlight">6</span><br>
        Believe the very best<br><br>
        There's a time for everyone<br>
        If they only learn... (이하 생략)
        </div>
        """
        st.markdown(lyrics_content, unsafe_allow_html=True)
        
        if st.button("Check Answers", use_container_width=True):
            st.toast("채점 완료! Result 탭을 확인하세요.")

with tab_score:
    st.subheader("📊 Your Performance")
    # 채점 로직
    user_answers = [u1, u2, u3, u4, u5, u6]
    correct_answers = ["surrender", "world", "worrier", "wanderer", "far", "vagabonds"]
    
    score = sum(1 for ua, ca in zip(user_answers, correct_answers) if ua == ca)
    
    col_a, col_b = st.columns(2)
    col_a.metric("Correct", f"{score} / 6")
    col_b.progress(score / 6)
    
    if score == 6:
        st.balloons()
        st.success("You are a Pop Song Master! 🏆")
    else:
        st.info("Keep practicing! 가사를 다시 보며 들어보세요.")
