import streamlit as st
from gtts import gTTS
import io
import re
import html

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="Survival English Dialogues",
    page_icon="💬",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 1000;
        color: #111827;
        margin-bottom: 4px;
    }

    .sub-title {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 22px;
    }

    .dialogue-header {
        background: linear-gradient(135deg, #dbeafe 0%, #fce7f3 50%, #fef3c7 100%);
        border-radius: 26px;
        padding: 24px 28px;
        margin-bottom: 22px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
    }

    .dialogue-title {
        font-size: 33px;
        font-weight: 1000;
        color: #111827;
        margin-bottom: 8px;
    }

    .dialogue-desc {
        font-size: 17px;
        font-weight: 800;
        color: #374151;
        line-height: 1.6;
    }

    .line-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 14px 16px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }

    .en-line {
        font-size: 23px;
        font-weight: 900;
        color: #111827;
        line-height: 1.45;
    }

    .ko-line {
        font-size: 17px;
        font-weight: 700;
        color: #6b7280;
        margin-top: 6px;
        line-height: 1.5;
    }

    .word-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 14px 16px;
        margin-top: 14px;
        font-size: 15px;
        color: #475569;
        line-height: 1.7;
    }

    .audio-box {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1e3a8a;
        border-radius: 18px;
        padding: 14px 16px;
        margin: 10px 0 18px 0;
        font-size: 15px;
        font-weight: 800;
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        min-height: 48px;
        border: 1px solid #d1d5db;
    }

    .stButton > button:hover {
        border-color: #8b5cf6;
        color: #8b5cf6;
    }

    div[data-testid="stTabs"] button[role="tab"] p {
        font-size: 18px !important;
        font-weight: 900 !important;
    }


    .matching-box {
        background: linear-gradient(135deg,#eef2ff 0%,#f0f9ff 50%,#fdf2f8 100%);
        padding: 22px 24px;
        border-radius: 20px;
        border: 1px solid #c7d2fe;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 5px 16px rgba(99,102,241,0.08);
    }

    .matching-title {
        font-size: 28px;
        font-weight: 1000;
        color: #4338ca;
        margin-bottom: 8px;
    }

    .matching-guide {
        font-size: 16px;
        font-weight: 800;
        color: #475569;
        line-height: 1.7;
    }

    .selected-card-notice {
        background-color: #fef3c7;
        padding: 13px 15px;
        border-radius: 14px;
        border: 1px solid #facc15;
        color: #92400e;
        font-size: 15px;
        font-weight: 900;
        margin-bottom: 14px;
        line-height: 1.5;
    }

    .match-progress-box {
        background: linear-gradient(135deg,#dcfce7,#dbeafe);
        border: 1px solid #bbf7d0;
        border-radius: 16px;
        padding: 13px 15px;
        margin: 12px 0 16px 0;
        font-size: 17px;
        font-weight: 900;
        color: #14532d;
        text-align: center;
    }

    @media (max-width: 520px) {
        .main-title {
            font-size: 33px;
        }
        .dialogue-title {
            font-size: 27px;
        }
        .en-line {
            font-size: 19px;
        }
        .ko-line {
            font-size: 15px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# TTS 함수
# =========================
def remove_speaker_label(sentence):
    """
    음성에서는 A:, B:를 빼고 자연스럽게 읽게 합니다.
    """
    return re.sub(r"^[A-Z]:\s*", "", sentence).strip()


def make_dialogue_tts_text(lines):
    """
    대화 전체를 하나의 음성 텍스트로 만듭니다.
    Google TTS URL 방식이 아니라 gTTS를 사용하므로 긴 대화에서도 더 안정적입니다.
    """
    clean_lines = []

    for line in lines:
        text = remove_speaker_label(line["en"])
        clean_lines.append(text)

    return " ".join(clean_lines)


@st.cache_data(show_spinner=False)
def make_gtts_audio(text):
    """
    대화 전체 mp3 생성
    """
    fp = io.BytesIO()
    tts = gTTS(text=text, lang="en", tld="com", slow=False)
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def play_dialogue_audio(lines, key):
    """
    대화 전체 듣기:
    - 대화 전체를 하나의 mp3처럼 재생
    - 한국어 해석 보기 버튼을 눌러 화면이 다시 실행되어도 오디오가 사라지지 않도록
      st.session_state에 생성된 음성 파일을 저장합니다.
    """
    audio_state_key = f"{key}_audio_bytes"
    audio_text_key = f"{key}_audio_text"

    if st.button("🔊 대화 전체 듣기", key=key, use_container_width=True):
        try:
            dialogue_text = make_dialogue_tts_text(lines)
            audio_bytes = make_gtts_audio(dialogue_text)

            st.session_state[audio_state_key] = audio_bytes
            st.session_state[audio_text_key] = dialogue_text

        except Exception as e:
            st.error("음성 파일을 만들지 못했습니다. requirements.txt에 gTTS가 있는지 확인해 주세요.")
            st.caption(f"오류 내용: {e}")

    # 버튼을 누른 뒤 생성된 오디오는 session_state에 남아 있으므로,
    # 한국어 해석 보기/숨기기 때문에 rerun되어도 계속 표시됩니다.
    if audio_state_key in st.session_state:
        st.markdown(
            """
            <div class="audio-box">
                대화 전체 음성입니다. 한국어 해석을 켜고 꺼도 이 오디오는 유지됩니다.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.audio(st.session_state[audio_state_key], format="audio/mp3")

        if st.button("🧹 듣기 파일 숨기기", key=f"{key}_clear_audio", use_container_width=True):
            if audio_state_key in st.session_state:
                del st.session_state[audio_state_key]
            if audio_text_key in st.session_state:
                del st.session_state[audio_text_key]
            st.rerun()



# =========================
# 문장 매칭 활동 함수
# =========================
def clean_text_for_display(text):
    return html.escape(str(text).strip())


def safe_key(text):
    return re.sub(r"[^a-zA-Z0-9가-힣_]+", "_", str(text))


def shuffle_options(options, seed):
    import random
    rng = random.Random(seed)
    options = list(options)
    rng.shuffle(options)
    return options


def show_sentence_matching_activity(dialogue_data, key_prefix):
    """
    팝송 파일의 '문장 매칭 게임'과 같은 방식입니다.
    왼쪽 영어 전체 문장과 오른쪽 한국어 해석을 차례로 눌러 짝을 맞춥니다.
    """
    st.markdown(
        """
        <div class="matching-box">
            <div class="matching-title">🧩 문장 매칭하기</div>
            <div class="matching-guide">
                왼쪽의 영어 문장 전체와 오른쪽의 한국어 해석을 차례로 눌러 짝을 맞추세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    match_key = safe_key(key_prefix)

    pairs = []
    for i, line in enumerate(dialogue_data["lines"], start=1):
        pairs.append({
            "id": f"{match_key}_{i}",
            "en": line["en"],
            "ko": line["ko"],
        })

    st.session_state.setdefault(f"match_done_{match_key}", [])
    st.session_state.setdefault(f"match_selected_{match_key}", None)
    st.session_state.setdefault(f"match_message_{match_key}", "")
    st.session_state.setdefault(f"match_show_answer_{match_key}", False)

    done = st.session_state[f"match_done_{match_key}"]
    selected = st.session_state[f"match_selected_{match_key}"]

    total = len(pairs)
    current_score = len(done)

    st.markdown(
        f'<div class="match-progress-box">현재 맞춘 문장: {current_score} / {total}</div>',
        unsafe_allow_html=True
    )

    if selected:
        st.markdown(
            f'<div class="selected-card-notice">선택됨: {clean_text_for_display(selected["text"])}</div>',
            unsafe_allow_html=True
        )

    if st.session_state[f"match_message_{match_key}"]:
        msg = st.session_state[f"match_message_{match_key}"]
        if "정답" in msg:
            st.success(msg)
        elif "오답" in msg:
            st.error(msg)
        else:
            st.info(msg)

    en_cards = [
        {"id": p["id"], "text": p["en"], "kind": "en"}
        for p in pairs
        if p["id"] not in done
    ]

    ko_cards = [
        {"id": p["id"], "text": p["ko"], "kind": "ko"}
        for p in pairs
        if p["id"] not in done
    ]

    en_cards = shuffle_options(en_cards, seed=f"{match_key}_en")
    ko_cards = shuffle_options(ko_cards, seed=f"{match_key}_ko")

    col_en, col_ko = st.columns(2)

    with col_en:
        st.markdown("### English")
        for card in en_cards:
            if st.button(card["text"], key=f"match_en_{match_key}_{card['id']}", use_container_width=True):
                current_selected = st.session_state[f"match_selected_{match_key}"]

                if current_selected is None:
                    st.session_state[f"match_selected_{match_key}"] = card
                    st.session_state[f"match_message_{match_key}"] = "오른쪽에서 알맞은 한국어 해석을 고르세요."
                else:
                    if current_selected["id"] == card["id"] and current_selected["kind"] != card["kind"]:
                        if card["id"] not in done:
                            done.append(card["id"])
                        st.session_state[f"match_selected_{match_key}"] = None
                        st.session_state[f"match_message_{match_key}"] = "정답입니다! ✅"
                    else:
                        st.session_state[f"match_selected_{match_key}"] = card
                        st.session_state[f"match_message_{match_key}"] = "영어 문장을 다시 선택했습니다. 오른쪽 해석을 고르세요."

                st.rerun()

    with col_ko:
        st.markdown("### Korean")
        for card in ko_cards:
            if st.button(card["text"], key=f"match_ko_{match_key}_{card['id']}", use_container_width=True):
                current_selected = st.session_state[f"match_selected_{match_key}"]

                if current_selected is None:
                    st.session_state[f"match_selected_{match_key}"] = card
                    st.session_state[f"match_message_{match_key}"] = "왼쪽에서 알맞은 영어 문장을 고르세요."
                else:
                    if current_selected["id"] == card["id"] and current_selected["kind"] != card["kind"]:
                        if card["id"] not in done:
                            done.append(card["id"])
                        st.session_state[f"match_selected_{match_key}"] = None
                        st.session_state[f"match_message_{match_key}"] = "정답입니다! ✅"
                    else:
                        st.session_state[f"match_selected_{match_key}"] = card
                        st.session_state[f"match_message_{match_key}"] = "한국어 해석을 다시 선택했습니다. 왼쪽 영어 문장을 고르세요."

                st.rerun()

    if len(done) == total:
        st.success("🎉 모든 문장을 맞췄습니다! 대화문 전체를 잘 이해했습니다.")
        st.balloons()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("🔄 문장 매칭 다시 하기", key=f"match_reset_{match_key}", use_container_width=True):
            st.session_state[f"match_done_{match_key}"] = []
            st.session_state[f"match_selected_{match_key}"] = None
            st.session_state[f"match_message_{match_key}"] = ""
            st.session_state[f"match_show_answer_{match_key}"] = False
            st.rerun()

    with c2:
        if st.button("👀 정답 전체 보기", key=f"match_answer_{match_key}", use_container_width=True):
            st.session_state[f"match_show_answer_{match_key}"] = not st.session_state.get(f"match_show_answer_{match_key}", False)
            st.rerun()

    if st.session_state.get(f"match_show_answer_{match_key}", False):
        st.markdown("### ✅ 정답 전체")
        for i, p in enumerate(pairs, start=1):
            st.markdown(
                f"""
                <div class="line-card">
                    <div class="en-line">{i}. {clean_text_for_display(p["en"])}</div>
                    <div class="ko-line">{clean_text_for_display(p["ko"])}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================
# 생존 160 단어 활용 대화문 10개
# =========================
dialogues = [
    {
        "title": "1. First Day at School",
        "ko_title": "학교 첫날",
        "words": "I, you, he, she, we, they, friend, teacher, student, classmate, family, father, mother, brother, sister, name, person, man, woman, child",
        "lines": [
            {"en": "A: Hi, I'm new here. What's your name?", "ko": "A: 안녕, 나 여기 처음이야. 네 이름은 뭐야?"},
            {"en": "B: I'm Minho. You can sit with me.", "ko": "B: 나는 민호야. 나랑 같이 앉아도 돼."},
            {"en": "A: Are you a student in this class?", "ko": "A: 너 이 반 학생이야?"},
            {"en": "B: Yeah. He is my classmate, and she is my friend.", "ko": "B: 응. 그는 내 반 친구고, 그녀는 내 친구야."},
            {"en": "A: Nice. We can study together.", "ko": "A: 좋다. 우리 같이 공부할 수 있겠다."},
            {"en": "B: Sure. They are nice, and our teacher is kind.", "ko": "B: 물론이지. 그들도 착하고, 우리 선생님도 친절해."},
            {"en": "A: My family is excited. My father, mother, brother, and sister all said, good luck!", "ko": "A: 우리 가족도 기대하고 있어. 아버지, 어머니, 형, 누나가 모두 잘하라고 했어."},
            {"en": "B: That's sweet. You're a good person.", "ko": "B: 따뜻하다. 너 좋은 사람이구나."},
            {"en": "A: I was a shy child, so I'm a little nervous.", "ko": "A: 내가 어릴 때는 수줍은 아이였어서 조금 긴장돼."},
            {"en": "B: Don't worry. That man and that woman are new teachers, too.", "ko": "B: 걱정하지 마. 저 남자분과 저 여자분도 새로 오신 선생님들이야."},
        ],
    },
    {
        "title": "2. Classroom Moves",
        "ko_title": "교실 활동",
        "words": "go, come, walk, run, sit, stand, stop, start, open, close, eat, drink, sleep, study, read, write, listen, speak, help, wait",
        "lines": [
            {"en": "A: Should we go now or come later?", "ko": "A: 우리 지금 갈까, 아니면 나중에 올까?"},
            {"en": "B: Let's start now. Walk slowly. Don't run.", "ko": "B: 지금 시작하자. 천천히 걸어. 뛰지는 마."},
            {"en": "A: Okay. Should I sit down?", "ko": "A: 알겠어. 앉으면 돼?"},
            {"en": "B: Yeah, sit down first. Then stand up when the teacher says so.", "ko": "B: 응, 먼저 앉아. 그리고 선생님이 말하면 일어서."},
            {"en": "A: Got it. Should I open the window?", "ko": "A: 알겠어. 창문 열까?"},
            {"en": "B: Open the window, but close the door.", "ko": "B: 창문은 열고, 문은 닫아."},
            {"en": "A: Can I eat my bread and drink water?", "ko": "A: 빵 먹고 물 마셔도 돼?"},
            {"en": "B: Wait a minute. Stop eating during practice.", "ko": "B: 잠깐만. 연습 중에는 먹는 거 멈춰."},
            {"en": "A: I'm sleepy. I didn't sleep well.", "ko": "A: 나 졸려. 잠을 잘 못 잤어."},
            {"en": "B: Hang in there. Listen, speak, read, write, and I'll help you study.", "ko": "B: 조금만 버텨. 듣고, 말하고, 읽고, 써 봐. 내가 공부 도와줄게."},
        ],
    },
    {
        "title": "3. Feeling Sick",
        "ko_title": "몸 상태 말하기",
        "words": "happy, sad, angry, tired, hungry, thirsty, sick, okay, fine, cold, hot, pain, headache, stomachache, fever, hurt, good, bad, worried, scared",
        "lines": [
            {"en": "A: You don't look happy. Are you okay?", "ko": "A: 너 행복해 보이지 않아. 괜찮아?"},
            {"en": "B: I'm fine, but I'm really tired.", "ko": "B: 괜찮긴 한데 정말 피곤해."},
            {"en": "A: Are you hungry or thirsty?", "ko": "A: 배고프거나 목말라?"},
            {"en": "B: Yeah, I'm thirsty. And I feel sick.", "ko": "B: 응, 목말라. 그리고 몸이 좀 안 좋아."},
            {"en": "A: Do you have a headache?", "ko": "A: 두통 있어?"},
            {"en": "B: A little. My stomach hurts, too.", "ko": "B: 조금. 배도 아파."},
            {"en": "A: You might have a fever. Are you cold or hot?", "ko": "A: 열이 있을 수도 있어. 춥니, 덥니?"},
            {"en": "B: Both. I feel cold, then hot.", "ko": "B: 둘 다. 춥다가 덥다가 해."},
            {"en": "A: That's bad. Don't be scared. I'm worried, but you'll be good.", "ko": "A: 안 좋네. 무서워하지 마. 걱정되지만 괜찮아질 거야."},
            {"en": "B: Thanks. I was getting angry and sad, but now I feel better.", "ko": "B: 고마워. 화도 나고 슬펐는데 이제 좀 나아졌어."},
        ],
    },
    {
        "title": "4. Lunch Time",
        "ko_title": "점심시간",
        "words": "food, water, rice, bread, milk, juice, coffee, tea, apple, banana, egg, meat, chicken, fish, breakfast, lunch, dinner, snack, medicine, hospital",
        "lines": [
            {"en": "A: Did you eat breakfast?", "ko": "A: 아침 먹었어?"},
            {"en": "B: No, I just had milk and a banana.", "ko": "B: 아니, 우유랑 바나나만 먹었어."},
            {"en": "A: No wonder you're hungry. Let's get lunch.", "ko": "A: 그래서 배고팠구나. 점심 먹으러 가자."},
            {"en": "B: I want rice, chicken, and maybe fish.", "ko": "B: 나는 밥, 닭고기, 그리고 생선도 조금 먹고 싶어."},
            {"en": "A: I'll get bread, an egg, and some meat.", "ko": "A: 나는 빵, 달걀, 고기 좀 먹을래."},
            {"en": "B: Do you want water or juice?", "ko": "B: 물 마실래, 주스 마실래?"},
            {"en": "A: Water, please. I already had coffee and tea.", "ko": "A: 물 주세요. 이미 커피랑 차를 마셨어."},
            {"en": "B: I have an apple for a snack later.", "ko": "B: 나는 나중에 간식으로 먹을 사과가 있어."},
            {"en": "A: Nice. But if your stomach hurts again, take medicine.", "ko": "A: 좋네. 그런데 배가 또 아프면 약 먹어."},
            {"en": "B: Yeah. If it gets worse, I'll go to the hospital.", "ko": "B: 응. 더 심해지면 병원 갈게."},
        ],
    },
    {
        "title": "5. Finding the Way",
        "ko_title": "길 찾기",
        "words": "home, school, classroom, bathroom, hospital, store, station, bus, car, taxi, train, bike, road, street, here, there, near, far, left, right",
        "lines": [
            {"en": "A: Excuse me. Is the station near here?", "ko": "A: 실례합니다. 역이 여기 근처에 있나요?"},
            {"en": "B: Yeah, it's not far. Go down this street.", "ko": "B: 네, 멀지 않아요. 이 거리를 따라 내려가세요."},
            {"en": "A: Do I turn left or right?", "ko": "A: 왼쪽으로 도나요, 오른쪽으로 도나요?"},
            {"en": "B: Turn left at the store. The station is there.", "ko": "B: 가게에서 왼쪽으로 도세요. 역은 거기에 있어요."},
            {"en": "A: Thanks. Can I take a bus from there?", "ko": "A: 감사합니다. 거기서 버스를 탈 수 있나요?"},
            {"en": "B: Yes. You can also take a taxi or a train.", "ko": "B: 네. 택시나 기차도 탈 수 있어요."},
            {"en": "A: I came by bike, but the road is busy.", "ko": "A: 자전거로 왔는데 도로가 복잡하네요."},
            {"en": "B: Then don't ride your bike there. A car almost hit someone yesterday.", "ko": "B: 그러면 거기서는 자전거 타지 마세요. 어제 차가 사람을 칠 뻔했어요."},
            {"en": "A: Got it. Is the bathroom in the station?", "ko": "A: 알겠습니다. 화장실은 역 안에 있나요?"},
            {"en": "B: Yes. And the hospital is between the station and the school classroom building.", "ko": "B: 네. 그리고 병원은 역과 학교 교실 건물 사이에 있어요."},
        ],
    },
    {
        "title": "6. Time Check",
        "ko_title": "시간 확인",
        "words": "time, now, today, tomorrow, yesterday, morning, afternoon, evening, night, early, late, one, two, three, four, five, six, seven, eight, nine, ten",
        "lines": [
            {"en": "A: What time is it now?", "ko": "A: 지금 몇 시야?"},
            {"en": "B: It's seven in the morning.", "ko": "B: 아침 7시야."},
            {"en": "A: Seven? That's early.", "ko": "A: 7시? 빠르네."},
            {"en": "B: Yeah, but yesterday I woke up late.", "ko": "B: 응, 그런데 어제는 늦게 일어났어."},
            {"en": "A: What do we have today?", "ko": "A: 오늘 뭐 있어?"},
            {"en": "B: One test in the morning, two classes in the afternoon, and three meetings in the evening.", "ko": "B: 아침에 시험 하나, 오후에 수업 두 개, 저녁에 모임 세 개 있어."},
            {"en": "A: Wow. Four, five, six things already.", "ko": "A: 와. 벌써 네 개, 다섯 개, 여섯 개 일이네."},
            {"en": "B: And tomorrow we have eight or nine pages to read.", "ko": "B: 그리고 내일은 여덟 쪽이나 아홉 쪽을 읽어야 해."},
            {"en": "A: I need ten hours of sleep tonight.", "ko": "A: 오늘 밤에는 열 시간 자야겠다."},
            {"en": "B: Same here. Let's not stay up late.", "ko": "B: 나도. 늦게까지 깨어 있지 말자."},
        ],
    },
    {
        "title": "7. Looking for Things",
        "ko_title": "물건 찾기",
        "words": "bag, phone, book, notebook, pen, pencil, desk, chair, door, window, key, money, card, ticket, clothes, shoes, hat, watch, cup, bottle",
        "lines": [
            {"en": "A: Where's my bag?", "ko": "A: 내 가방 어디 있지?"},
            {"en": "B: It's on the chair, next to your desk.", "ko": "B: 네 책상 옆 의자 위에 있어."},
            {"en": "A: Thanks. I also need my phone and watch.", "ko": "A: 고마워. 휴대폰이랑 시계도 필요해."},
            {"en": "B: Your phone is by the window, and your watch is near the door.", "ko": "B: 휴대폰은 창문 옆에 있고, 시계는 문 근처에 있어."},
            {"en": "A: Do you see my book, notebook, pen, and pencil?", "ko": "A: 내 책, 공책, 펜, 연필 보여?"},
            {"en": "B: Yeah, they're in your bag.", "ko": "B: 응, 가방 안에 있어."},
            {"en": "A: Great. I have my card, but I don't have money.", "ko": "A: 좋아. 카드는 있는데 돈이 없어."},
            {"en": "B: You also need your ticket.", "ko": "B: 표도 필요해."},
            {"en": "A: Right. And I need clothes, shoes, and a hat for the trip.", "ko": "A: 맞다. 여행 가려면 옷, 신발, 모자도 필요해."},
            {"en": "B: Don't forget your cup, bottle, and key.", "ko": "B: 컵, 병, 열쇠도 잊지 마."},
        ],
    },
    {
        "title": "8. Asking for Help",
        "ko_title": "도움 요청",
        "words": "help, please, sorry, excuse me, again, slowly, understand, question, problem, need, want, know, say, tell, ask, answer, repeat, speak, look, listen",
        "lines": [
            {"en": "A: Excuse me. Can you help me, please?", "ko": "A: 실례합니다. 저 좀 도와주실 수 있나요?"},
            {"en": "B: Sure. What's the problem?", "ko": "B: 물론이죠. 무슨 문제예요?"},
            {"en": "A: I don't understand this question.", "ko": "A: 이 질문을 이해하지 못하겠어요."},
            {"en": "B: No problem. Look here and listen.", "ko": "B: 괜찮아요. 여기 보고 들어 보세요."},
            {"en": "A: Sorry, can you say that again?", "ko": "A: 죄송한데 다시 말해 주실 수 있나요?"},
            {"en": "B: Of course. I'll speak slowly.", "ko": "B: 물론이죠. 천천히 말할게요."},
            {"en": "A: Thanks. I want to know the answer.", "ko": "A: 감사합니다. 답을 알고 싶어요."},
            {"en": "B: First, ask yourself what you need.", "ko": "B: 먼저, 네가 무엇이 필요한지 스스로 물어봐요."},
            {"en": "A: Can you tell me one more time?", "ko": "A: 한 번 더 말해 주실 수 있나요?"},
            {"en": "B: Sure. Repeat after me.", "ko": "B: 물론이죠. 저를 따라 반복하세요."},
        ],
    },
    {
        "title": "9. Simple Opinions",
        "ko_title": "생각과 의견",
        "words": "think, believe, guess, remember, forget, mean, agree, disagree, opinion, idea, reason, example, fact, choice, decision, advice, suggestion, possible, impossible, confusing",
        "lines": [
            {"en": "A: What do you think about this idea?", "ko": "A: 이 생각에 대해 어떻게 생각해?"},
            {"en": "B: I believe it's possible.", "ko": "B: 가능하다고 믿어."},
            {"en": "A: Really? I guess it sounds hard.", "ko": "A: 정말? 나는 어려워 보인다고 생각했어."},
            {"en": "B: I agree it's hard, but it's not impossible.", "ko": "B: 어렵다는 건 동의하지만 불가능하진 않아."},
            {"en": "A: What's your reason?", "ko": "A: 이유가 뭐야?"},
            {"en": "B: Here's one example. We remember more when we practice every day.", "ko": "B: 예를 하나 들게. 우리는 매일 연습할 때 더 많이 기억해."},
            {"en": "A: That's a fact, but I forget words quickly.", "ko": "A: 그건 사실이야. 그런데 나는 단어를 빨리 잊어."},
            {"en": "B: My advice is simple. Make a choice and keep going.", "ko": "B: 내 조언은 간단해. 선택하고 계속해."},
            {"en": "A: Good suggestion. Your opinion makes sense.", "ko": "A: 좋은 제안이야. 네 의견이 말이 돼."},
            {"en": "B: If it's confusing, ask again before you make a decision.", "ko": "B: 헷갈리면 결정하기 전에 다시 물어봐."},
        ],
    },
    {
        "title": "10. Plans and Future",
        "ko_title": "계획과 미래",
        "words": "plan, appointment, promise, meeting, date, event, party, festival, deadline, calendar, next week, message, join, prepare, decide, change, cancel, on time, available, reminder, smartphone, screen, app, website, internet, Wi-Fi, password, text, video call, gallery, news, channel, post, comment, upload, download, search, click, battery, notification, job, work, company, office, factory, engineer, mechanic, chef, firefighter, farmer, designer, singer, actor, athlete, dream, future, goal, skill, interview, experience",
        "lines": [
            {"en": "A: Do you have a plan for next week?", "ko": "A: 다음 주 계획 있어?"},
            {"en": "B: Yeah, I have an appointment, a meeting, and a job interview.", "ko": "B: 응, 약속 하나, 회의 하나, 그리고 취업 면접이 있어."},
            {"en": "A: That's a lot. Did you put it on your calendar?", "ko": "A: 많네. 달력에 넣어 뒀어?"},
            {"en": "B: Yep. I also set a reminder on my smartphone.", "ko": "B: 응. 스마트폰에 알림도 설정했어."},
            {"en": "A: Is your battery okay? You'll need Wi-Fi, the internet, and maybe a video call.", "ko": "A: 배터리는 괜찮아? 와이파이, 인터넷, 영상 통화도 필요할 수 있잖아."},
            {"en": "B: True. I saved the password, the website, and the app.", "ko": "B: 맞아. 비밀번호, 웹사이트, 앱을 저장해 뒀어."},
            {"en": "A: What kind of work do you want?", "ko": "A: 어떤 일을 하고 싶어?"},
            {"en": "B: My dream is to be an engineer at a good company, maybe in an office or a factory.", "ko": "B: 내 꿈은 좋은 회사에서 엔지니어가 되는 거야. 사무실이나 공장에서 일할 수도 있고."},
            {"en": "A: Nice. I once wanted to be a mechanic, a chef, a firefighter, a farmer, a designer, a singer, an actor, and even an athlete.", "ko": "A: 멋지다. 나는 한때 정비사, 요리사, 소방관, 농부, 디자이너, 가수, 배우, 심지어 운동선수도 되고 싶었어."},
            {"en": "B: That's great experience. Just prepare your skills and don't be late.", "ko": "B: 좋은 경험이네. 기술을 준비하고 늦지 않으면 돼."},
            {"en": "A: I'll text you if I need to change or cancel the date.", "ko": "A: 날짜를 바꾸거나 취소해야 하면 문자할게."},
            {"en": "B: Promise me you'll be on time and available for the event, party, or festival.", "ko": "B: 행사, 파티, 축제에 시간 맞춰 오고 가능하다고 약속해 줘."},
            {"en": "A: I promise. My future goal is clear now.", "ko": "A: 약속할게. 이제 내 미래 목표가 분명해졌어."},
        ],
    },
]

# =========================
# 화면 구성
# =========================
st.markdown("<div class='main-title'>💬 Survival English Dialogues</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>생존 영어 160개 단어를 활용한 일상 대화체 연습입니다. 영어만 먼저 보고, 필요하면 한국어 해석을 확인하세요.</div>",
    unsafe_allow_html=True
)

tab_names = [f"{i + 1}. {d['ko_title']}" for i, d in enumerate(dialogues)]
tabs = st.tabs(tab_names)

for i, tab in enumerate(tabs):
    with tab:
        d = dialogues[i]

        st.markdown(
            f"""
            <div class="dialogue-header">
                <div class="dialogue-title">{d['title']}</div>
                <div class="dialogue-desc">{d['ko_title']} · 일상 대화체 표현 연습</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2 = st.columns([1, 1])

        with c1:
            play_dialogue_audio(d["lines"], key=f"dialogue_audio_{i}")

        with c2:
            show_korean = st.toggle(
                "🇰🇷 한국어 해석 보기",
                value=False,
                key=f"show_korean_{i}"
            )

        st.divider()

        for line in d["lines"]:
            st.markdown('<div class="line-card">', unsafe_allow_html=True)

            st.markdown(
                f"<div class='en-line'>{line['en']}</div>",
                unsafe_allow_html=True
            )

            if show_korean:
                st.markdown(
                    f"<div class='ko-line'>{line['ko']}</div>",
                    unsafe_allow_html=True
                )

            st.markdown('</div>', unsafe_allow_html=True)

        with st.expander("사용된 단어 보기"):
            st.markdown(
                f"""
                <div class="word-box">
                    {d['words']}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()
        show_sentence_matching_activity(d, key_prefix=f"dialogue_matching_{i}_{d['ko_title']}")
