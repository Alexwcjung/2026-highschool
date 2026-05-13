import streamlit as st
from pathlib import Path

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Soccer Talk with Ronaldo",
    page_icon="⚽",
    layout="wide"
)

# 현재 파일 기준 경로
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "images" / "ronaldo.png"

# =========================
# 제목
# =========================
st.markdown("""
# ⚽ Soccer Talk with Ronaldo
### English Reading & Speaking Practice
""")

# =========================
# 탭 구성
# =========================
tab_video, tab_image, tab_reading = st.tabs([
    "🎬 동영상 보기",
    "🖼️ 그림 보기",
    "📖 Reading 자료"
])

# =========================
# 1. 동영상 탭
# =========================
with tab_video:
    st.markdown("## 🎬 Watch the Video")

    # 유튜브 링크가 있으면 여기에 넣기
    video_url = "여기에_유튜브_링크_넣기"

    if video_url.startswith("http"):
        st.video(video_url)
    else:
        st.info("여기에 유튜브 링크를 넣으면 동영상이 뜹니다.")

    st.markdown("""
    예시:
    ```python
    video_url = "https://www.youtube.com/watch?v=영상ID"
    ```
    """)

# =========================
# 2. 그림 탭
# =========================
with tab_image:
    st.markdown("## 🖼️ Infographic")

    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.error(f"이미지 파일을 찾을 수 없습니다: {IMAGE_PATH}")

# =========================
# 3. Reading 자료 탭
# =========================
with tab_reading:
    st.markdown("## 📖 Reading Practice")

    st.markdown("""
<div style="
    background: linear-gradient(135deg, #f7fff7, #e8f5e9);
    padding: 24px;
    border-radius: 20px;
    border: 2px solid #2e7d32;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    font-size: 21px;
    line-height: 1.8;
">

<b>Ronaldo:</b> Hi! Do you like soccer?<br><br>

<b>Me:</b> Yes, I do. I really like soccer.<br><br>

<b>Ronaldo:</b> That’s great. Who is your favorite player?<br><br>

<b>Me:</b> You are my favorite player, Ronaldo.<br><br>

<b>Ronaldo:</b> Thank you. Why do you like me?<br><br>

<b>Me:</b> Because you are fast, strong, and hardworking.<br><br>

<b>Ronaldo:</b> I’m happy to hear that. Do you play soccer?<br><br>

<b>Me:</b> Yes, I do. I play soccer with my friends.<br><br>

<b>Ronaldo:</b> What position do you play?<br><br>

<b>Me:</b> I usually play forward.<br><br>

<b>Ronaldo:</b> Nice. Do you practice every day?<br><br>

<b>Me:</b> Not every day, but I try to practice often.<br><br>

<b>Ronaldo:</b> Practice is very important. You must keep going.<br><br>

<b>Me:</b> Sometimes I get tired.<br><br>

<b>Ronaldo:</b> That’s okay. Everyone gets tired sometimes.<br><br>

<b>Me:</b> What should I do when I feel tired?<br><br>

<b>Ronaldo:</b> Rest a little, and then try again.<br><br>

<b>Me:</b> I want to be a great player like you.<br><br>

<b>Ronaldo:</b> Believe in yourself. Never give up.<br><br>

<b>Me:</b> Thank you, Ronaldo. I will do my best.<br><br>

<b>Ronaldo:</b> Good! I believe in you. Keep practicing!

</div>
""", unsafe_allow_html=True)

    st.markdown("### ⭐ Key Message")

    st.success(
        "Practice is very important. Everyone gets tired sometimes, "
        "but if you rest and try again, you can improve. Believe in yourself and never give up!"
    )
