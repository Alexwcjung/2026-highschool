st.subheader("🕵️ 가사 속 보물찾기 (Keyword Hunt)")
st.write("전체 가사에서 아래 단어들이 몇 번 나오는지 찾아보세요!")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("❄️ Snow")
with col2:
    st.info("👑 Queen")
with col3:
    st.info("🚪 Door")

st.success("팁: 가사 탭으로 돌아가서 눈을 크게 뜨고 찾아보세요! 👀")
