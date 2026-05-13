import streamlit as st
from pathlib import Path
from gtts import gTTS
import io

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Celebrity English Reading",
    page_icon="🌟",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

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
# CSS
# =========================
st.markdown("""
<style>
.main-title {
    background: linear-gradient(135deg, #14532d, #16a34a);
    color: white;
    padding: 28px;
    border-radius: 24px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}
.person-card {
    background: #f8fafc;
    padding: 20px;
    border-radius: 20px;
    border: 2px solid #e2e8f0;
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
.korean-card {
    background: linear-gradient(135deg, #fffdf2, #fff3c4);
    padding: 24px;
    border-radius: 20px;
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
.activity-box {
    background: linear-gradient(135deg, #e3f2fd, #ffffff);
    padding: 22px;
    border-radius: 20px;
    border: 2px solid #42a5f5;
    margin-bottom: 16px;
}
.big-word {
    font-size: 25px;
    font-weight: 800;
    color: #14532d;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 인물별 자료
# =========================
people_data = {
    "⚽ Ronaldo": {
        "title": "Soccer Talk with Ronaldo",
        "subtitle": "Practice, confidence, and never giving up",
        "video_url": "여기에_로날도_유튜브_링크",
        "image_path": BASE_DIR / "images" / "ronaldo.png",
        "dialogue": [
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
        ],
        "key_expressions": [
            "Do you like soccer?",
            "Who is your favorite player?",
            "What position do you play?",
            "Practice is very important.",
            "Believe in yourself.",
            "Never give up."
        ],
        "mission": [
            ("Do you like ______?", "soccer"),
            ("Who is your favorite ______?", "player"),
            ("I usually play ______.", "forward"),
            ("Believe in ______.", "yourself"),
            ("Never give ______.", "up")
        ]
    },

    # =========================
    # 나중에 다른 인물 추가 예시
    # =========================
    "🏀 Jordan": {
        "title": "Basketball Talk with Jordan",
        "subtitle": "Dreams, practice, and confidence",
        "video_url": "여기에_조던_유튜브_링크",
        "image_path": BASE_DIR / "images" / "jordan.png",
        "dialogue": [
            ("Jordan", "Hi! Do you like basketball?", "안녕! 너는 농구를 좋아하니?"),
            ("Me", "Yes, I do. I really like basketball.", "응, 좋아해. 나는 농구를 정말 좋아해."),
            ("Jordan", "What is your dream?", "네 꿈은 무엇이니?"),
            ("Me", "I want to be a great player.", "저는 훌륭한 선수가 되고 싶어요."),
            ("Jordan", "Then practice every day and believe in yourself.", "그렇다면 매일 연습하고 너 자신을 믿어."),
            ("Me", "I will do my best.", "최선을 다할게요."),
            ("Jordan", "Good. Never give up.", "좋아. 절대 포기하지 마.")
        ],
        "key_expressions": [
            "Do you like basketball?",
            "What is your dream?",
            "I want to be a great player.",
            "Practice every day.",
            "Believe in yourself.",
            "Never give up."
        ],
        "mission": [
            ("Do you like ______?", "basketball"),
            ("What is your ______?", "dream"),
            ("I want to be a great ______.", "player"),
            ("Believe in ______.", "yourself"),
            ("Never give ______.", "up")
        ]
    }
}

# =========================
# 제목
# =========================
st.markdown("""
<div class="main-title">
    <h1>🌟 Celebrity English Reading</h1>
    <p style="font-size:22px;">Choose a person and practice English with video, image, reading, listening, and activities.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# 인물 선택
# =========================
person_name = st.selectbox(
    "👤 인물을 선택하세요",
    list(people_data.keys())
)

data = people_data[person_name]

dialogue = data["dialogue"]
full_english = "\n".join([f"{speaker}: {eng}" for speaker, eng, kor in dialogue])
full_korean = "\n".join([f"{speaker}: {kor}" for speaker, eng, kor in dialogue])

# =========================
# 인물 소개 카드
# =========================
st.markdown(f"""
<div class="person-card">
    <h2>{data["title"]}</h2>
    <p style="font-size:20px;">{data["subtitle"]}</p>
</div>
""", unsafe_allow_html=True)

# =========================
# 4개 탭
# =========================
tab_video, tab_image, tab_reading, tab_activity = st.tabs([
    "🎬 동영상",
    "🖼️ 그림",
    "📖 Reading",
    "🎮 활동"
])

# =========================
# 1. 동영상 탭
# =========================
with tab_video:
    st.markdown(f"## 🎬 {data['title']} Video")

    video_url = data["video_url"]

    if video_url.startswith("http"):
        st.video(video_url)
    else:
        st.info("아직 동영상 링크가 없습니다. people_data 안의 video_url에 유튜브 링크를 넣으세요.")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Before Watching</div>
    <p style="font-size:20px;">영상을 보기 전에 생각해 봅시다.</p>
    <ul style="font-size:20px; line-height:1.8;">
        <li>이 인물은 어떤 분야에서 유명한가요?</li>
        <li>이 인물에게 어떤 질문을 해 보고 싶나요?</li>
        <li>오늘 배울 핵심 표현은 무엇일까요?</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =========================
# 2. 그림 탭
# =========================
with tab_image:
    st.markdown(f"## 🖼️ {data['title']} Image")

    image_path = data["image_path"]

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"이미지 파일을 찾을 수 없습니다: {image_path}")
        st.info("예: pages/images/ronaldo.png 또는 pages/images/jordan.png 경로를 확인하세요.")

    st.markdown("### 그림 보고 말해보기")

    for exp in data["key_expressions"][:4]:
        st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================
# 3. Reading 탭
# =========================
with tab_reading:
    st.markdown(f"## 📖 {data['title']} Reading")

    # 영어 지문
    reading_html = '<div class="reading-card">'
    for speaker, eng, kor in dialogue:
        reading_html += f"<b>{speaker}:</b> {eng}<br><br>"
    reading_html += "</div>"

    st.markdown(reading_html, unsafe_allow_html=True)

    st.markdown("---")

    # Reading 안에 듣기와 한국어 해석 버튼
    col1, col2 = st.columns(2)

    with col1:
        show_listening = st.button("🎧 듣기 열기 / Listening", use_container_width=True)

    with col2:
        show_korean = st.button("🇰🇷 한국어 해석 열기", use_container_width=True)

    # 버튼 상태 저장
    if "show_listening" not in st.session_state:
        st.session_state.show_listening = False

    if "show_korean" not in st.session_state:
        st.session_state.show_korean = False

    if show_listening:
        st.session_state.show_listening = not st.session_state.show_listening

    if show_korean:
        st.session_state.show_korean = not st.session_state.show_korean

    # 듣기 영역
    if st.session_state.show_listening:
        st.markdown("### 🎧 전체 대화 듣기")
        audio_full = make_tts(full_english, lang="en")
        st.audio(audio_full, format="audio/mp3")

        st.markdown("### 한 문장씩 듣기")

        for i, (speaker, eng, kor) in enumerate(dialogue, start=1):
            with st.expander(f"{i}. {speaker}: {eng}"):
                st.audio(make_tts(eng, lang="en"), format="audio/mp3")
                st.caption(kor)

    # 한국어 해석 영역
    if st.session_state.show_korean:
        st.markdown("### 🇰🇷 한국어 해석")

        korean_html = '<div class="korean-card">'
        for speaker, eng, kor in dialogue:
            korean_html += f"<b>{speaker}:</b> {kor}<br><br>"
        korean_html += "</div>"

        st.markdown(korean_html, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### ⭐ Key Expressions")

    col_a, col_b = st.columns(2)

    half = len(data["key_expressions"]) // 2

    with col_a:
        for exp in data["key_expressions"][:half]:
            st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

    with col_b:
        for exp in data["key_expressions"][half:]:
            st.markdown(f'<div class="expression">{exp}</div>', unsafe_allow_html=True)

# =========================
# 4. 활동 탭
# =========================
with tab_activity:
    st.markdown(f"## 🎮 {data['title']} Activities")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 1. 빈칸 채우기</div>
    <p style="font-size:20px;">Reading에서 본 표현을 떠올리며 빈칸을 채워 봅시다.</p>
</div>
""", unsafe_allow_html=True)

    answers = []

    for i, (question, answer) in enumerate(data["mission"], start=1):
        user_answer = st.text_input(f"{i}. {question}", key=f"{person_name}_mission_{i}")
        answers.append((user_answer, answer))

    if st.button("정답 확인", key=f"{person_name}_check"):
        score = 0

        for i, (user_answer, answer) in enumerate(answers, start=1):
            if user_answer.strip().lower() == answer.lower():
                score += 1
                st.success(f"{i}번 정답!")
            else:
                st.error(f"{i}번 정답: {answer}")

        st.markdown(f"## 점수: {score} / {len(answers)}")

        if score == len(answers):
            st.balloons()
            st.success("완벽합니다! Great job! 🏆")
        elif score >= len(answers) // 2:
            st.info("좋아요! 조금만 더 연습하면 됩니다.")
        else:
            st.warning("괜찮아요. Reading을 다시 보고 도전해 봅시다.")

    st.markdown("---")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 2. 나만의 문장 만들기</div>
    <p style="font-size:20px;">오늘 배운 표현을 사용해서 나만의 문장을 만들어 봅시다.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="expression">My favorite person is __________.</div>
<div class="expression">I like him/her because __________.</div>
<div class="expression">I want to be __________.</div>
<div class="expression">When I feel tired, I __________.</div>
<div class="expression">I will never give up because __________.</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 3. 오늘의 한 문장</div>
    <p style="font-size:20px;">오늘 가장 마음에 드는 문장 하나를 골라 크게 읽어 봅시다.</p>
</div>
""", unsafe_allow_html=True)

    selected_sentence = st.selectbox(
        "오늘의 문장을 고르세요",
        data["key_expressions"],
        key=f"{person_name}_sentence"
    )

    st.success(selected_sentence)

    if st.button("선택한 문장 듣기", key=f"{person_name}_sentence_audio"):
        st.audio(make_tts(selected_sentence, lang="en"), format="audio/mp3")
