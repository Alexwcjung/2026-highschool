import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Pop Song Listening Activity",
    page_icon="🎵",
    layout="wide"
)

# =========================
# CSS 디자인 (음영 처리 및 레이아웃)
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #f8fafc;
}
.title-box {
    background: linear-gradient(135deg, #6366f1, #a855f7);
    padding: 25px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.lyrics-container {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    line-height: 2.8;
    font-size: 1.2rem;
    color: #1e293b;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.highlight-blank {
    background-color: #fef08a; /* 노란색 음영 */
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: bold;
    color: #c2410c;
    border: 1px dashed #f59e0b;
    margin: 0 4px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>🎵 Pop Song Listening Practice</h1><p>노래를 들으며 음영 처리된 빈칸(1~3)에 들어갈 단어를 골라보세요!</p></div>', unsafe_allow_html=True)

# =========================
# 메인 레이아웃 (영상 | 가사 및 문제)
# =========================
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("🎬 Watch & Listen")
    # 라이온킹 공식 영상 예시
    video_url = "https://www.youtube.com/watch?v=25QyCxVkXwQ"
    st.video(video_url)
    st.info("💡 노래를 재생하고 가사의 흐름에 맞춰 정답을 선택하세요.")

with col2:
    st.subheader("📜 Lyrics (Verse 1)")
    
    # 가사 내 빈칸 음영 처리 (HTML/CSS 사용)
    lyrics_html = """
    <div class="lyrics-container">
        There's a calm <span class="highlight-blank">( 1 )</span> <br>
        To the rush of day <br>
        When the heat of a rolling <span class="highlight-blank">( 2 )</span> <br>
        Can be turned away <br><br>
        An enchanted moment <br>
        And it sees me through <br>
        It's enough for this restless <span class="highlight-blank">( 3 )</span> <br>
        Just to be with you
    </div>
    """
    st.markdown(lyrics_html, unsafe_allow_html=True)
    
    st.write("---")
    
    # 퀴즈 섹션 (1~3번 보기 중 선택)
    st.markdown("### 🎧 빈칸 채우기 퀴즈")
    
    ans1 = st.radio("1번 빈칸에 들어갈 단어는?", ["surrender", "surprise", "summer"], horizontal=True, key="q1")
    ans2 = st.radio("2번 빈칸에 들어갈 단어는?", ["wind", "wave", "walk"], horizontal=True, key="q2")
    ans3 = st.radio("3번 빈칸에 들어갈 단어는?", ["winner", "water", "warrior"], horizontal=True, key="q3")

    if st.button("정답 확인하기", use_container_width=True):
        # 정답: surrender, wave, warrior
        score = 0
        
        if ans1 == "surrender": score += 1
        if ans2 == "wave": score += 1
        if ans3 == "warrior": score += 1
        
        if score == 3:
            st.balloons()
            st.success(f"Perfect! {score}/3 모두 맞혔습니다!")
        else:
            st.warning(f"다시 시도해보세요! 현재 점수: {score}/3")
            
        with st.expander("해설 및 정답 보기"):
            st.write("**1. surrender**: 굴복, 항복 (여기서는 평온하게 받아들임을 의미)")
            st.write("**2. wave**: 파도")
            st.write("**3. warrior**: 전사")
