import streamlit as st
from pathlib import Path
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Soccer Talk with Ronaldo",
    page_icon="⚽",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "images" / "ronaldo.png"

# =========================
# CSS
# =========================
st.markdown("""
<style>
.main-title {
    background: linear-gradient(135deg, #0b6623, #1b8f3a);
    padding: 28px;
    border-radius: 24px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}
.sub-title {
    font-size: 22px;
    opacity: 0.95;
}
.card {
    background: #ffffff;
    padding: 24px;
    border-radius: 22px;
    border: 2px solid #e0e0e0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}
.reading-card {
    background: linear-gradient(135deg, #f7fff7, #e8f5e9);
    padding: 26px;
    border-radius: 22px;
    border: 2px solid #2e7d32;
    font-size: 21px;
    line-height: 1.85;
}
.kr-card {
    background: linear-gradient(135deg, #fffdf2, #fff3c4);
    padding: 26px;
    border-radius: 22px;
    border: 2px solid #d6a400;
    font-size: 20px;
    line-height: 1.8;
}
.expression {
    background: #f1f8e9;
    padding: 14px 18px;
    border-radius: 16px;
    border-left: 7px solid #2e7d32;
    margin-bottom: 12px;
    font-size: 20px;
}
.mission-box {
    background: linear-gradient(135deg, #e3f2fd, #ffffff);
    padding: 22px;
    border-radius: 20px;
    border: 2px solid #42a5f5;
    margin-bottom: 15px;
}
.big-word {
    font-size: 26px;
    font-weight: 800;
    color: #0b6623;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 자료
# =========================
dialogue = [
    ("Ronaldo", "Hi! Do you like soccer?", "안녕! 너는 축구를 좋아하니?"),
    ("Me", "Yes, I do. I really like soccer.", "응, 좋아해. 나는 축구를 정말 좋아해."),
    ("Ronaldo", "That’s great. Who is your favorite player?", "멋지다. 네가 가장 좋아하는 선수는 누구니?"),
    ("Me", "You are my favorite player, Ronaldo.", "로날도, 당신이 제가 가장 좋아하는 선수예요."),
    ("Ronaldo", "Thank you. Why do you like me?", "고마워. 왜 나를 좋아하니?"),
    ("Me", "Because you are fast, strong, and hardworking.", "당신은 빠르고, 강하고, 성실하기 때문이에요."),
    ("Ronaldo", "I’m happy to hear that. Do you play soccer?", "그 말을 들으니 기쁘구나. 너도 축구를 하니?"),
    ("Me", "Yes, I do. I play soccer with my friends.", "네, 해요. 친구들과 축구를 해요."),
    ("Ronaldo", "What position do you play?", "너는 어떤 포지션을 맡니?"),
    ("Me", "I usually play forward.", "저는 보통 공격수를 맡아요."),
    ("Ronaldo", "Nice. Do you practice every day?", "좋아. 매일 연습하니?"),
    ("Me", "Not every day, but I try to practice often.", "매일은 아니지만, 자주 연습하려고 노력해요."),
    ("Ronaldo", "Practice is very important. You must keep going.", "연습은 매우 중요해. 계속해 나가야 해."),
    ("Me", "Sometimes I get tired.", "가끔은 지쳐요."),
    ("Ronaldo", "That’s okay. Everyone gets tired sometimes.", "괜찮아. 누구나 가끔은 지칠 때가 있어."),
    ("Me", "What should I do when I feel tired?", "제가 지칠 때는 어떻게 해야 할까요?"),
    ("Ronaldo", "Rest a little, and then try again.", "조금 쉬고, 다시 도전해 봐."),
    ("Me", "I want to be a great player like you.", "저도 당신처럼 훌륭한 선수가 되고 싶어요."),
    ("Ronaldo", "Believe in yourself. Never give up.", "너 자신을 믿어. 절대 포기하지 마."),
    ("Me", "Thank you, Ronaldo. I will do my best.", "고마워요, 로날도. 최선을 다할게요."),
    ("Ronaldo", "Good! I believe in you. Keep practicing!", "좋아! 나는 너를 믿어. 계속 연습해!")
]

full_english = "\n".join([f"{speaker}: {eng}" for speaker, eng, kor in dialogue])
full_korean = "\n".join([f"{speaker}: {kor}" for speaker, eng, kor in dialogue])

# =========================
# TTS 함수
# =========================
@st.cache_data
def make_tts(text, lang="en"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()

# =========================
# 제목
# =========================
st.markdown("""
<div class="main-title">
    <h1>⚽ Soccer Talk with Ronaldo</h1>
    <div class="sub-title">English Reading · Listening · Speaking Practice</div>
</div>
""", unsafe_allow_html=True)

# =========================
# 탭
# =========================
tab_video, tab_image, tab_reading, tab_listening, tab_korean, tab_mission = st.tabs([
    "🎬 동영상 보기",
    "🖼️ 그림 보기",
    "📖 Reading",
    "🎧 Listening",
    "🇰🇷 한국어 해석",
    "🎮 미션 활동"
])

# =========================
# 1. 동영상 보기
# =========================
with tab_video:
    st.markdown("## 🎬 Watch First")

    video_url = "여기에_유튜브_링크_넣기"

    if video_url.startswith("http"):
        st.video(video_url)
    else:
        st.info("여기에 유튜브 링크를 넣으면 동영상이 뜹니다.")

    st.markdown("""
<div class="card">
<h3>오늘의 질문</h3>
<p style="font-size:20px;">영상을 보면서 생각해 봅시다.</p>
<ul style="font-size:20px; line-height:1.8;">
<li>로날도는 학생에게 어떤 조언을 해 주나요?</li>
<li>학생은 왜 로날도를 좋아하나요?</li>
<li>지쳤을 때 우리는 어떻게 해야 할까요?</li>
</ul>
</div>
""", unsafe_allow_html=True)

# =========================
# 2. 그림 보기
# =========================
with tab_image:
    st.markdown("## 🖼️ Infographic")

    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.error(f"이미지 파일을 찾을 수 없습니다: {IMAGE_PATH}")

    st.markdown("""
<div class="card">
<h3>그림 보고 말해보기</h3>
<p style="font-size:20px;">그림을 보고 영어로 한 문장씩 말해 봅시다.</p>
<div class="expression">I like soccer.</div>
<div class="expression">My favorite player is Ronaldo.</div>
<div class="expression">I want to be a great player.</div>
<div class="expression">I will never give up.</div>
</div>
""", unsafe_allow_html=True)

# =========================
# 3. Reading
# =========================
with tab_reading:
    st.markdown("## 📖 Reading Practice")

    st.markdown("""
<div class="reading-card">
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

    st.markdown("### ⭐ 핵심 표현")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="expression">Do you like soccer?</div>', unsafe_allow_html=True)
        st.markdown('<div class="expression">Who is your favorite player?</div>', unsafe_allow_html=True)
        st.markdown('<div class="expression">What position do you play?</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="expression">Practice is very important.</div>', unsafe_allow_html=True)
        st.markdown('<div class="expression">Believe in yourself.</div>', unsafe_allow_html=True)
        st.markdown('<div class="expression">Never give up.</div>', unsafe_allow_html=True)

# =========================
# 4. Listening
# =========================
with tab_listening:
    st.markdown("## 🎧 Listening Practice")

    st.markdown("""
<div class="card">
<h3>전체 대화 듣기</h3>
<p style="font-size:20px;">먼저 전체 대화를 듣고, 아는 표현을 찾아보세요.</p>
</div>
""", unsafe_allow_html=True)

    audio_full = make_tts(full_english, lang="en")
    st.audio(audio_full, format="audio/mp3")

    st.markdown("### 한 문장씩 듣기")

    for i, (speaker, eng, kor) in enumerate(dialogue, start=1):
        with st.expander(f"{i}. {speaker}: {eng}"):
            st.audio(make_tts(eng, lang="en"), format="audio/mp3")
            st.caption(kor)

# =========================
# 5. 한국어 해석
# =========================
with tab_korean:
    st.markdown("## 🇰🇷 한국어 해석")

    st.markdown("""
<div class="kr-card">
<b>Ronaldo:</b> 안녕! 너는 축구를 좋아하니?<br><br>
<b>Me:</b> 응, 좋아해. 나는 축구를 정말 좋아해.<br><br>

<b>Ronaldo:</b> 멋지다. 네가 가장 좋아하는 선수는 누구니?<br><br>
<b>Me:</b> 로날도, 당신이 제가 가장 좋아하는 선수예요.<br><br>

<b>Ronaldo:</b> 고마워. 왜 나를 좋아하니?<br><br>
<b>Me:</b> 당신은 빠르고, 강하고, 성실하기 때문이에요.<br><br>

<b>Ronaldo:</b> 그 말을 들으니 기쁘구나. 너도 축구를 하니?<br><br>
<b>Me:</b> 네, 해요. 친구들과 축구를 해요.<br><br>

<b>Ronaldo:</b> 너는 어떤 포지션을 맡니?<br><br>
<b>Me:</b> 저는 보통 공격수를 맡아요.<br><br>

<b>Ronaldo:</b> 좋아. 매일 연습하니?<br><br>
<b>Me:</b> 매일은 아니지만, 자주 연습하려고 노력해요.<br><br>

<b>Ronaldo:</b> 연습은 매우 중요해. 계속해 나가야 해.<br><br>
<b>Me:</b> 가끔은 지쳐요.<br><br>

<b>Ronaldo:</b> 괜찮아. 누구나 가끔은 지칠 때가 있어.<br><br>
<b>Me:</b> 제가 지칠 때는 어떻게 해야 할까요?<br><br>

<b>Ronaldo:</b> 조금 쉬고, 다시 도전해 봐.<br><br>
<b>Me:</b> 저도 당신처럼 훌륭한 선수가 되고 싶어요.<br><br>

<b>Ronaldo:</b> 너 자신을 믿어. 절대 포기하지 마.<br><br>
<b>Me:</b> 고마워요, 로날도. 최선을 다할게요.<br><br>

<b>Ronaldo:</b> 좋아! 나는 너를 믿어. 계속 연습해!
</div>
""", unsafe_allow_html=True)

# =========================
# 6. 미션 활동
# =========================
with tab_mission:
    st.markdown("## 🎮 Mission Activities")

    st.markdown("""
<div class="mission-box">
<div class="big-word">Mission 1. 빈칸 채우기</div>
<p style="font-size:20px;">아래 문장을 완성해 보세요.</p>
</div>
""", unsafe_allow_html=True)

    q1 = st.text_input("1. Do you like ______?")
    q2 = st.text_input("2. Who is your favorite ______?")
    q3 = st.text_input("3. I usually play ______.")
    q4 = st.text_input("4. Believe in ______.")
    q5 = st.text_input("5. Never give ______.")

    if st.button("정답 확인"):
        score = 0

        if q1.strip().lower() == "soccer":
            score += 1
            st.success("1번 정답!")
        else:
            st.error("1번: soccer")

        if q2.strip().lower() == "player":
            score += 1
            st.success("2번 정답!")
        else:
            st.error("2번: player")

        if q3.strip().lower() == "forward":
            score += 1
            st.success("3번 정답!")
        else:
            st.error("3번: forward")

        if q4.strip().lower() == "yourself":
            score += 1
            st.success("4번 정답!")
        else:
            st.error("4번: yourself")

        if q5.strip().lower() == "up":
            score += 1
            st.success("5번 정답!")
        else:
            st.error("5번: up")

        st.markdown(f"## 점수: {score} / 5")

        if score == 5:
            st.balloons()
            st.success("완벽합니다! You are a champion! 🏆")
        elif score >= 3:
            st.info("좋아요! 조금만 더 연습하면 됩니다.")
        else:
            st.warning("괜찮아요. 듣고 다시 도전해 봅시다.")

    st.markdown("---")

    st.markdown("""
<div class="mission-box">
<div class="big-word">Mission 2. 나만의 문장 만들기</div>
<p style="font-size:20px;">아래 문장을 나에게 맞게 바꿔 말해 보세요.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="expression">My favorite player is __________.</div>
<div class="expression">I usually play __________.</div>
<div class="expression">When I feel tired, I __________.</div>
<div class="expression">I want to be __________.</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
<div class="mission-box">
<div class="big-word">Mission 3. 오늘의 메시지</div>
<p style="font-size:20px;">오늘 배운 문장 중 하나를 골라 크게 읽어 봅시다.</p>
</div>
""", unsafe_allow_html=True)

    st.success("Believe in yourself. Never give up. Keep practicing!")
