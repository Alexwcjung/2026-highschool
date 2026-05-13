import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(page_title="Frozen Class", page_icon="❄️", layout="wide")

# =========================
# 고대비 라이트 디자인
# =========================
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }
    .main-title { background-color: #f0f9ff; padding: 20px; border-radius: 15px; border: 2px solid #0ea5e9; text-align: center; color: #0369a1; }
    .card-box { background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px dashed #0ea5e9; margin-bottom: 10px; font-weight: bold; color: #1e3a8a; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"><h1>❄️ Let It Go: Story & Lyrics</h1></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📺 STEP 1. 배경 이해", "📜 STEP 2. 전체 가사", "🧩 STEP 3. 가사 순서 맞추기"])

# -------------------------
# STEP 1: 영상 & 줄거리
# -------------------------
with tab1:
    col_v, col_t = st.columns([1.2, 1])
    with col_v:
        st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    with col_t:
        st.subheader("📖 엘사의 이야기")
        st.info("비밀을 들켜버린 엘사가 산으로 도망쳐 자유를 찾는 내용이에요.")
        st.markdown("**Q. 주인공의 심정은 어떻게 변했을까요?**")
        st.write("답답함(Conceal) ➡️ 자유로움(Let it go!)")

# -------------------------
# STEP 2: 전체 가사 (1절 코러스 전부)
# -------------------------
with tab2:
    st.subheader("📜 가사 읽어보기 (English & Korean)")
    lyrics_list = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
        ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
        ("A kingdom of isolation", "고립된 이 왕국에서"),
        ("And it looks like I'm the queen", "내가 이곳의 여왕이 된 것 같아"),
        ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
        ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
        ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
        ("Can't hold it back anymore", "더 이상 참을 수 없어")
    ]
    for eng, kor in lyrics_list:
        st.markdown(f"**{eng}**  \n<small style='color:gray'>{kor}</small>", unsafe_allow_html=True)

# -------------------------
# STEP 3: 가사 카드 순서 맞추기 (Scramble Game)
# -------------------------
with tab3:
    st.subheader("🧩 가사 카드 순서 맞추기")
    st.write("노래의 흐름대로 문장을 골라 순서를 완성해 보세요!")[cite: 1]

    # 정답 순서
    correct_order = [
        "1. The snow glows white on the mountain",
        "2. A kingdom of isolation",
        "3. Don't let them in, don't let them see",
        "4. Let it go, let it go!"
    ]
    
    # 뒤섞인 옵션
    scrambled_options = [
        "4. Let it go, let it go!",
        "2. A kingdom of isolation",
        "1. The snow glows white on the mountain",
        "3. Don't let them in, don't let them see"
    ]

    st.markdown('<div class="card-box">보기를 클릭하여 노래 순서대로 나열하세요.</div>', unsafe_allow_html=True)
    
    # 학생이 선택하는 창
    user_sort = st.multiselect("가사 카드를 순서대로 선택하세요:", scrambled_options)[cite: 1]

    if user_sort:
        st.write("---")
        st.write("**내가 만든 순서:**")
        for idx, sentence in enumerate(user_sort):
            st.write(f"{idx+1}. {sentence}")

        if user_sort == correct_order:
            st.balloons()
            st.success("🎉 완벽합니다! 노래의 흐름을 모두 이해했어요!")
        elif len(user_sort) == len(correct_order):
            st.error("순서가 조금 틀린 것 같아요. 다시 한번 들어볼까요?")
