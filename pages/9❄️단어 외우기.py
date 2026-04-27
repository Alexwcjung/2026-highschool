import streamlit as st
from gtts import gTTS
import io
import random

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Theme Vocabulary Practice",
    page_icon="📚",
    layout="wide"
)

st.title("📚 테마별 영어 단어 학습")
st.caption("중요한 기초 단어를 테마별로 익히고 퀴즈로 복습해 봅시다.")

# =========================
# 안내 박스
# =========================
st.markdown(
    """
    <div style="
        border-left: 6px solid #4f8df7;
        background-color: #f4f8ff;
        padding: 16px 18px;
        border-radius: 12px;
        margin-bottom: 22px;
        line-height: 1.7;
    ">
        <div style="font-size:20px; font-weight:900; margin-bottom:8px;">
            📌 학습 방법
        </div>
        <div>• 단어를 테마별로 묶어서 학습합니다.</div>
        <div>• 먼저 <b>단어 익히기</b>에서 뜻과 발음을 확인합니다.</div>
        <div>• 그다음 <b>퀴즈 풀기</b>에서 영어 단어를 보고 알맞은 뜻을 고릅니다.</div>
        <div>• 1차 제출 후 틀린 문제만 다시 풀 수 있습니다.</div>
        <div>• 2차 제출 후 정답을 확인할 수 있습니다.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS 함수
# =========================
@st.cache_data
def make_tts_audio(text, lang="en", tld="com"):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def audio_button(label, text, key):
    if st.button(label, key=key):
        audio_bytes = make_tts_audio(text)
        st.audio(audio_bytes, format="audio/mp3")


# =========================
# 테마별 단어 데이터
# =========================
word_themes = {
    "① 사람·관계": [
        {"word": "person", "meaning": "사람"},
        {"word": "man", "meaning": "남자"},
        {"word": "woman", "meaning": "여자"},
        {"word": "child", "meaning": "아이"},
        {"word": "baby", "meaning": "아기"},
        {"word": "boy", "meaning": "소년"},
        {"word": "girl", "meaning": "소녀"},
        {"word": "friend", "meaning": "친구"},
        {"word": "family", "meaning": "가족"},
        {"word": "parent", "meaning": "부모"},
        {"word": "father", "meaning": "아버지"},
        {"word": "mother", "meaning": "어머니"},
        {"word": "brother", "meaning": "형제, 남자 형제"},
        {"word": "sister", "meaning": "자매, 여자 형제"},
        {"word": "son", "meaning": "아들"},
        {"word": "daughter", "meaning": "딸"},
        {"word": "teacher", "meaning": "선생님"},
        {"word": "student", "meaning": "학생"},
        {"word": "classmate", "meaning": "반 친구"},
        {"word": "neighbor", "meaning": "이웃"},
        {"word": "customer", "meaning": "손님, 고객"},
        {"word": "worker", "meaning": "노동자, 직원"},
        {"word": "driver", "meaning": "운전자"},
        {"word": "doctor", "meaning": "의사"},
        {"word": "nurse", "meaning": "간호사"},
        {"word": "police officer", "meaning": "경찰관"},
        {"word": "owner", "meaning": "주인"},
        {"word": "guest", "meaning": "손님"},
        {"word": "team", "meaning": "팀, 무리"},
        {"word": "member", "meaning": "구성원"},
    ],

    "② 학교·교실": [
        {"word": "school", "meaning": "학교"},
        {"word": "class", "meaning": "수업, 학급"},
        {"word": "classroom", "meaning": "교실"},
        {"word": "lesson", "meaning": "수업, 과"},
        {"word": "homework", "meaning": "숙제"},
        {"word": "test", "meaning": "시험"},
        {"word": "exam", "meaning": "시험"},
        {"word": "quiz", "meaning": "퀴즈, 간단한 시험"},
        {"word": "question", "meaning": "질문, 문제"},
        {"word": "answer", "meaning": "대답, 정답"},
        {"word": "book", "meaning": "책"},
        {"word": "notebook", "meaning": "공책"},
        {"word": "paper", "meaning": "종이, 보고서"},
        {"word": "pen", "meaning": "펜"},
        {"word": "pencil", "meaning": "연필"},
        {"word": "desk", "meaning": "책상"},
        {"word": "chair", "meaning": "의자"},
        {"word": "board", "meaning": "칠판, 게시판"},
        {"word": "page", "meaning": "쪽, 페이지"},
        {"word": "word", "meaning": "단어, 말"},
        {"word": "sentence", "meaning": "문장"},
        {"word": "story", "meaning": "이야기"},
        {"word": "language", "meaning": "언어"},
        {"word": "English", "meaning": "영어"},
        {"word": "Korean", "meaning": "한국어"},
        {"word": "grade", "meaning": "성적, 학년"},
        {"word": "score", "meaning": "점수"},
        {"word": "rule", "meaning": "규칙"},
        {"word": "practice", "meaning": "연습하다, 연습"},
        {"word": "study", "meaning": "공부하다"},
    ],

    "③ 기본 동작 동사": [
        {"word": "go", "meaning": "가다"},
        {"word": "come", "meaning": "오다"},
        {"word": "walk", "meaning": "걷다"},
        {"word": "run", "meaning": "달리다"},
        {"word": "sit", "meaning": "앉다"},
        {"word": "stand", "meaning": "서다"},
        {"word": "stop", "meaning": "멈추다"},
        {"word": "start", "meaning": "시작하다"},
        {"word": "open", "meaning": "열다"},
        {"word": "close", "meaning": "닫다"},
        {"word": "make", "meaning": "만들다"},
        {"word": "do", "meaning": "하다"},
        {"word": "have", "meaning": "가지다, 먹다"},
        {"word": "get", "meaning": "얻다, 받다, 되다"},
        {"word": "take", "meaning": "가져가다, 타다"},
        {"word": "give", "meaning": "주다"},
        {"word": "put", "meaning": "놓다, 두다"},
        {"word": "bring", "meaning": "가져오다"},
        {"word": "use", "meaning": "사용하다"},
        {"word": "find", "meaning": "찾다"},
        {"word": "keep", "meaning": "유지하다, 보관하다"},
        {"word": "leave", "meaning": "떠나다, 남기다"},
        {"word": "move", "meaning": "움직이다, 이사하다"},
        {"word": "turn", "meaning": "돌다, 돌리다"},
        {"word": "wait", "meaning": "기다리다"},
        {"word": "help", "meaning": "돕다"},
        {"word": "try", "meaning": "시도하다"},
        {"word": "need", "meaning": "필요하다"},
        {"word": "want", "meaning": "원하다"},
        {"word": "like", "meaning": "좋아하다"},
    ],

    "④ 감정·성격": [
        {"word": "happy", "meaning": "행복한"},
        {"word": "sad", "meaning": "슬픈"},
        {"word": "angry", "meaning": "화난"},
        {"word": "tired", "meaning": "피곤한"},
        {"word": "hungry", "meaning": "배고픈"},
        {"word": "thirsty", "meaning": "목마른"},
        {"word": "excited", "meaning": "신난"},
        {"word": "bored", "meaning": "지루한"},
        {"word": "afraid", "meaning": "두려워하는"},
        {"word": "worried", "meaning": "걱정하는"},
        {"word": "proud", "meaning": "자랑스러워하는"},
        {"word": "kind", "meaning": "친절한"},
        {"word": "nice", "meaning": "좋은, 친절한"},
        {"word": "brave", "meaning": "용감한"},
        {"word": "honest", "meaning": "정직한"},
        {"word": "friendly", "meaning": "친근한"},
        {"word": "quiet", "meaning": "조용한"},
        {"word": "shy", "meaning": "수줍은"},
        {"word": "smart", "meaning": "똑똑한"},
        {"word": "strong", "meaning": "강한"},
        {"word": "weak", "meaning": "약한"},
        {"word": "careful", "meaning": "조심하는"},
        {"word": "lazy", "meaning": "게으른"},
        {"word": "busy", "meaning": "바쁜"},
        {"word": "ready", "meaning": "준비된"},
        {"word": "sorry", "meaning": "미안한"},
        {"word": "thankful", "meaning": "감사하는"},
        {"word": "lonely", "meaning": "외로운"},
        {"word": "nervous", "meaning": "긴장한"},
        {"word": "calm", "meaning": "차분한"},
    ],

    "⑤ 음식·건강": [
        {"word": "food", "meaning": "음식"},
        {"word": "rice", "meaning": "밥, 쌀"},
        {"word": "bread", "meaning": "빵"},
        {"word": "water", "meaning": "물"},
        {"word": "milk", "meaning": "우유"},
        {"word": "juice", "meaning": "주스"},
        {"word": "coffee", "meaning": "커피"},
        {"word": "tea", "meaning": "차"},
        {"word": "apple", "meaning": "사과"},
        {"word": "banana", "meaning": "바나나"},
        {"word": "egg", "meaning": "달걀"},
        {"word": "meat", "meaning": "고기"},
        {"word": "fish", "meaning": "생선, 물고기"},
        {"word": "chicken", "meaning": "닭고기, 닭"},
        {"word": "vegetable", "meaning": "채소"},
        {"word": "fruit", "meaning": "과일"},
        {"word": "breakfast", "meaning": "아침 식사"},
        {"word": "lunch", "meaning": "점심 식사"},
        {"word": "dinner", "meaning": "저녁 식사"},
        {"word": "snack", "meaning": "간식"},
        {"word": "healthy", "meaning": "건강한"},
        {"word": "sick", "meaning": "아픈"},
        {"word": "pain", "meaning": "통증"},
        {"word": "headache", "meaning": "두통"},
        {"word": "medicine", "meaning": "약"},
        {"word": "hospital", "meaning": "병원"},
        {"word": "exercise", "meaning": "운동하다, 운동"},
        {"word": "sleep", "meaning": "자다, 잠"},
        {"word": "rest", "meaning": "쉬다, 휴식"},
        {"word": "wash", "meaning": "씻다"},
    ],

    "⑥ 장소·이동": [
        {"word": "home", "meaning": "집"},
        {"word": "house", "meaning": "집"},
        {"word": "room", "meaning": "방"},
        {"word": "kitchen", "meaning": "부엌"},
        {"word": "bathroom", "meaning": "화장실, 욕실"},
        {"word": "door", "meaning": "문"},
        {"word": "window", "meaning": "창문"},
        {"word": "city", "meaning": "도시"},
        {"word": "town", "meaning": "마을"},
        {"word": "country", "meaning": "나라, 시골"},
        {"word": "street", "meaning": "거리"},
        {"word": "road", "meaning": "도로"},
        {"word": "park", "meaning": "공원"},
        {"word": "store", "meaning": "가게"},
        {"word": "market", "meaning": "시장"},
        {"word": "station", "meaning": "역"},
        {"word": "bus", "meaning": "버스"},
        {"word": "car", "meaning": "자동차"},
        {"word": "bike", "meaning": "자전거"},
        {"word": "train", "meaning": "기차"},
        {"word": "plane", "meaning": "비행기"},
        {"word": "ship", "meaning": "배"},
        {"word": "map", "meaning": "지도"},
        {"word": "place", "meaning": "장소"},
        {"word": "here", "meaning": "여기"},
        {"word": "there", "meaning": "거기"},
        {"word": "left", "meaning": "왼쪽"},
        {"word": "right", "meaning": "오른쪽, 맞는"},
        {"word": "near", "meaning": "가까운"},
        {"word": "far", "meaning": "먼"},
    ],
}

# =========================
# 전체 뜻 목록 만들기
# =========================
all_words = []
for theme_words in word_themes.values():
    all_words.extend(theme_words)

all_meanings = [item["meaning"] for item in all_words]


# =========================
# 보기 고정 랜덤 섞기
# =========================
def get_shuffled_options(theme_name, index, options):
    key = f"{theme_name}_options_{index}"

    if key not in st.session_state:
        shuffled = options[:]
        random.seed(f"{theme_name}_{index}")
        random.shuffle(shuffled)
        st.session_state[key] = shuffled

    return st.session_state[key]


# =========================
# 퀴즈 문항 만들기
# =========================
def make_quiz_items(theme_words, theme_name):
    quiz_items = []

    for idx, item in enumerate(theme_words):
        correct = item["meaning"]

        distractors = [m for m in all_meanings if m != correct]
        random.seed(f"{theme_name}_{item['word']}_{idx}")
        wrong_options = random.sample(distractors, 3)

        options = [correct] + wrong_options

        quiz_items.append({
            "word": item["word"],
            "answer": correct,
            "options": options
        })

    return quiz_items


# =========================
# 상태 초기화
# =========================
def init_state(theme_name):
    if f"{theme_name}_submitted1" not in st.session_state:
        st.session_state[f"{theme_name}_submitted1"] = False

    if f"{theme_name}_submitted2" not in st.session_state:
        st.session_state[f"{theme_name}_submitted2"] = False

    if f"{theme_name}_wrong" not in st.session_state:
        st.session_state[f"{theme_name}_wrong"] = []


def reset_theme(theme_name):
    keys_to_delete = []

    for key in st.session_state.keys():
        if key.startswith(theme_name):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del st.session_state[key]


# =========================
# 단어 익히기
# =========================
def show_word_cards(theme_words, theme_name):
    st.markdown("### 📖 단어 익히기")
    st.write("단어, 뜻, 발음을 먼저 확인하세요.")

    for idx, item in enumerate(theme_words):
        st.markdown("---")
        col1, col2, col3 = st.columns([1.2, 2, 1.2])

        with col1:
            st.markdown(f"### {idx + 1}. {item['word']}")

        with col2:
            st.markdown(f"**뜻:** {item['meaning']}")

        with col3:
            audio_button(
                "🔊 발음 듣기",
                item["word"],
                key=f"{theme_name}_learn_audio_{idx}"
            )


# =========================
# 퀴즈 풀기
# =========================
def show_quiz(theme_words, theme_name):
    init_state(theme_name)

    quiz_items = make_quiz_items(theme_words, theme_name)

    submitted1_key = f"{theme_name}_submitted1"
    submitted2_key = f"{theme_name}_submitted2"
    wrong_key = f"{theme_name}_wrong"

    if not st.session_state[submitted1_key]:
        st.markdown("### 📝 1차 퀴즈")
        st.write("영어 단어를 보고 알맞은 뜻을 고르세요.")

        for i, q in enumerate(quiz_items):
            st.markdown("---")
            st.markdown(f"### {i + 1}. {q['word']}")

            audio_button(
                "🔊 발음 듣기",
                q["word"],
                key=f"{theme_name}_quiz_audio1_{i}"
            )

            options = get_shuffled_options(theme_name, i, q["options"])

            st.radio(
                "뜻을 고르세요.",
                options,
                key=f"{theme_name}_q1_{i}"
            )

        if st.button("✅ 1차 제출하기", key=f"{theme_name}_submit1"):
            wrong = []

            for i, q in enumerate(quiz_items):
                user_answer = st.session_state.get(f"{theme_name}_q1_{i}")

                if user_answer != q["answer"]:
                    wrong.append(i)

            st.session_state[wrong_key] = wrong
            st.session_state[submitted1_key] = True
            st.rerun()

    elif st.session_state[submitted1_key] and not st.session_state[submitted2_key]:
        wrong = st.session_state[wrong_key]
        score = len(quiz_items) - len(wrong)

        st.success(f"🎉 1차 결과: {score} / {len(quiz_items)}점")

        if len(wrong) == 0:
            st.balloons()
            st.success("완벽합니다! 이 테마의 단어를 모두 잘 기억하고 있습니다.")

            if st.button("🔄 다시 풀기", key=f"{theme_name}_reset_all_correct"):
                reset_theme(theme_name)
                st.rerun()

        else:
            st.warning(f"틀린 단어 {len(wrong)}개를 다시 풀어 봅시다.")
            st.markdown("### 🔁 2차 퀴즈: 틀린 단어만 다시 풀기")

            for i in wrong:
                q = quiz_items[i]

                st.markdown("---")
                st.markdown(f"### {i + 1}. {q['word']}")

                audio_button(
                    "🔊 발음 다시 듣기",
                    q["word"],
                    key=f"{theme_name}_quiz_audio2_{i}"
                )

                options = get_shuffled_options(theme_name, i, q["options"])

                st.radio(
                    "뜻을 다시 고르세요.",
                    options,
                    key=f"{theme_name}_q2_{i}"
                )

            if st.button("✅ 2차 제출하기", key=f"{theme_name}_submit2"):
                st.session_state[submitted2_key] = True
                st.rerun()

    else:
        wrong = st.session_state[wrong_key]
        second_wrong = []

        for i in wrong:
            q = quiz_items[i]
            user_answer = st.session_state.get(f"{theme_name}_q2_{i}")

            if user_answer != q["answer"]:
                second_wrong.append(i)

        final_score = len(quiz_items) - len(second_wrong)

        st.success(f"🎉 최종 결과: {final_score} / {len(quiz_items)}점")

        if len(second_wrong) == 0:
            st.balloons()
            st.success("좋습니다! 틀렸던 단어까지 모두 다시 확인했습니다.")
        else:
            st.warning("아래 단어들은 다시 복습하면 좋습니다.")

        st.markdown("### ✅ 정답 확인")

        if len(wrong) == 0:
            st.info("틀린 문제가 없습니다.")
        else:
            for i in wrong:
                q = quiz_items[i]
                user1 = st.session_state.get(f"{theme_name}_q1_{i}")
                user2 = st.session_state.get(f"{theme_name}_q2_{i}")

                st.markdown("---")
                st.markdown(f"### {q['word']}")

                audio_button(
                    "🔊 발음 다시 듣기",
                    q["word"],
                    key=f"{theme_name}_answer_audio_{i}"
                )

                st.write(f"1차 선택: {user1}")
                st.write(f"2차 선택: {user2}")
                st.success(f"정답: {q['answer']}")

        if st.button("🔄 다시 풀기", key=f"{theme_name}_reset"):
            reset_theme(theme_name)
            st.rerun()


# =========================
# 탭 구성
# =========================
tabs = st.tabs(list(word_themes.keys()))

for tab, theme_name in zip(tabs, word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]

        st.subheader(theme_name)
        st.write(f"이 테마에는 **{len(theme_words)}개 단어**가 있습니다.")

        mode = st.radio(
            "학습 모드를 선택하세요.",
            ["📖 단어 익히기", "📝 퀴즈 풀기"],
            key=f"{theme_name}_mode",
            horizontal=True
        )

        if mode == "📖 단어 익히기":
            show_word_cards(theme_words, theme_name)
        else:
            show_quiz(theme_words, theme_name)
