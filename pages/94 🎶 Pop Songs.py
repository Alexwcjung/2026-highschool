import streamlit as st

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Lyrics & Translation: Let It Go",
    page_icon="❄️",
    layout="wide"
)

# =========================
# 디자인 최적화 (가사/해석 가독성)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; } 
    .title-box {
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 30px;
    }
    .lyrics-container {
        background-color: #1e293b;
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #38bdf8;
        line-height: 1.8;
    }
    .eng-line {
        font-size: 1.4rem;
        font-weight: bold;
        color: #f1f5f9;
        margin-top: 15px;
    }
    .kor-sub {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-bottom: 10px;
        font-family: 'Nanum Gothic', sans-serif;
    }
    .chorus-tag {
        color: #fbbf24;
        font-size: 0.9rem;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>❄️ Let It Go: Full Translation</h1><p>영상과 함께 전체 가사의 의미를 확인해 보세요.</p></div>', unsafe_allow_html=True)

# =========================
# 메인 레이아웃
# =========================
col_v, col_l = st.columns([1, 1.2])

with col_v:
    st.subheader("🎬 Watch Video")
    st.video("https://www.youtube.com/watch?v=L0MK7qz13bU")
    st.info("💡 왼쪽 영상을 재생하고 오른쪽의 해석과 함께 감상하세요.")

with col_l:
    st.subheader("📜 Lyrics & Korean Subtitles")
    
    # 전체 가사 및 해석 데이터
    lyrics_data = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산에는 하얀 눈이 빛나고"),
        ("Not a footprint to be seen", "발자국 하나 보이지 않네"),
        ("A kingdom of isolation", "고립된 이 왕국에서"),
        ("And it looks like I'm the queen", "내가 이곳의 여왕이 된 것 같아"),
        
        ("The wind is howling like this swirling storm inside", "바람은 내 안의 휘몰아치는 폭풍처럼 울부짖고"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었어, 하늘은 내가 노력했다는 걸 알 거야"),
        
        ("Don't let them in, don't let them see", "아무도 들여보내지 마, 아무것도 보여주지 마"),
        ("Be the good girl you always have to be", "언제나 그랬듯 착한 소녀가 되어야 해"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마, 그들이 알게 하지 마"),
        ("Well, now they know!", "그런데 이제 그들이 알아버렸어!"),
        
        ("Let it go, let it go", "다 잊어, 이제 다 잊어"),
        ("Can't hold it back anymore", "더 이상 참을 수 없어"),
        ("Let it go, let it go", "다 잊어, 다 던져버려"),
        ("Turn away and slam the door!", "뒤돌아서 문을 쾅 닫아버릴 거야"),
        
        ("I don't care what they're going to say", "남들이 무슨 말을 하든 상관없어"),
        ("Let the storm rage on", "폭풍아 계속 몰아쳐라"),
        ("The cold never bothered me anyway", "추위는 더 이상 나를 괴롭히지 못하니까")
    ]

    # 가사 출력 루프
    with st.container():
        for eng, kor in lyrics_data:
            # 후렴구 구분
            if eng == "Let it go, let it go":
                st.markdown('<div class="chorus-tag">── Chorus ──</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="eng-line">{eng}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="kor-sub">{kor}</div>', unsafe_allow_html=True)

    st.divider()
    st.caption("겨울왕국(Frozen) OST - Let It Go (1절)")
