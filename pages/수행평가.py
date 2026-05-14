# =========================
# 5. 사진 묘사하기
# =========================
st.subheader("5. 사진 묘사하기")

# 사진 크기 줄이기
left_col, center_col, right_col = st.columns([1.3, 1.8, 1.3])

with center_col:
    st.image(
        "pages/images/수행평가 그림.png",
        caption="Describe the picture.",
        use_container_width=True
    )

st.info("⏱️ 20초 안에 사진을 묘사해 봅시다.")

picture_script = """
There are many people in the street.
I can see trees and buildings too.
Some people are riding bikes and some are sitting in chairs.
They look happy.
"""

st.markdown("### 📢 사진 묘사 전체 듣기")
st.caption("오디오 바를 움직이면 앞뒤로 이동할 수 있습니다.")

make_audio_player(picture_script, "picture_full", speed)

# ✅ 3번, 4번과 같은 글씨 크기로 사진 묘사 대본 표시
st.markdown("### There are many people in the street.")
st.markdown("### I can see trees and buildings too.")
st.markdown("### Some people are riding bikes and some are sitting in chairs.")
st.markdown("### They look happy.")
