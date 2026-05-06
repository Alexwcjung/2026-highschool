import streamlit as st
import random

st.set_page_config(
    page_title="TBLT 그림 묘사하기",
    page_icon="🖼️",
    layout="wide"
)

# =====================================================
# 그림묘사 TBLT 활동 자료
# 이미지는 이모지/상황 카드로 대체했습니다.
# 실제 사진을 쓰려면 image_url에 이미지 주소를 넣으면 됩니다.
# =====================================================
TASKS = [
    {
        "title": "공원에서",
        "emoji": "🌳",
        "image_prompt": "공원에서 사람들이 산책하고, 아이들이 공을 차고, 한 사람이 벤치에서 책을 읽고 있습니다.",
        "keywords": ["park", "people", "walking", "children", "playing soccer", "bench", "reading"],
        "model": "This picture shows a park. Some people are walking, and children are playing soccer. A person is sitting on a bench and reading a book. The weather looks nice and peaceful.",
        "level1": "This is a park. People are walking. Children are playing soccer.",
        "questions": [
            "Where is this place?",
            "What are the people doing?",
            "How does the place look?"
        ]
    },
    {
        "title": "카페에서",
        "emoji": "☕",
        "image_prompt": "카페 안에서 사람들이 커피를 마시고, 한 학생은 노트북으로 공부하고, 직원은 음료를 만들고 있습니다.",
        "keywords": ["cafe", "coffee", "people", "drinking", "student", "laptop", "barista"],
        "model": "This picture shows a cafe. Some people are drinking coffee and talking. A student is studying with a laptop. A barista is making drinks behind the counter.",
        "level1": "This is a cafe. People are drinking coffee. A student is using a laptop.",
        "questions": [
            "Where are they?",
            "What is the student doing?",
            "What is the barista doing?"
        ]
    },
    {
        "title": "공항에서",
        "emoji": "✈️",
        "image_prompt": "공항에서 사람들이 여행 가방을 들고 줄을 서 있으며, 안내판을 보고 있는 사람도 있습니다.",
        "keywords": ["airport", "travelers", "suitcase", "waiting in line", "sign", "flight"],
        "model": "This picture shows an airport. Many travelers are standing in line with their suitcases. Some people are looking at the flight information board. They may be waiting for check-in.",
        "level1": "This is an airport. People have suitcases. They are waiting in line.",
        "questions": [
            "Where is this place?",
            "What do people have?",
            "What are they waiting for?"
        ]
    },
    {
        "title": "식당에서",
        "emoji": "🍽️",
        "image_prompt": "식당에서 가족이 함께 식사를 하고 있고, 직원이 음식을 가져오고 있습니다.",
        "keywords": ["restaurant", "family", "eating", "waiter", "food", "table"],
        "model": "This picture shows a restaurant. A family is eating together at a table. A waiter is bringing food. Everyone looks relaxed and happy.",
        "level1": "This is a restaurant. A family is eating. A waiter is bringing food.",
        "questions": [
            "Where are they?",
            "Who is eating together?",
            "What is the waiter doing?"
        ]
    },
    {
        "title": "도서관에서",
        "emoji": "📚",
        "image_prompt": "도서관에서 학생들이 조용히 책을 읽고 공부하고 있으며, 책장이 많이 보입니다.",
        "keywords": ["library", "students", "reading", "studying", "bookshelves", "quiet"],
        "model": "This picture shows a library. Several students are reading books and studying quietly. There are many bookshelves in the background. The atmosphere looks calm.",
        "level1": "This is a library. Students are reading and studying. It is quiet.",
        "questions": [
            "Where is this place?",
            "What are the students doing?",
            "How is the atmosphere?"
        ]
    },
    {
        "title": "병원에서",
        "emoji": "🏥",
        "image_prompt": "병원에서 의사가 환자와 이야기하고 있고, 간호사가 서류를 확인하고 있습니다.",
        "keywords": ["hospital", "doctor", "patient", "nurse", "talking", "checking documents"],
        "model": "This picture shows a hospital. A doctor is talking to a patient. A nurse is checking some documents. They seem to be helping the patient.",
        "level1": "This is a hospital. A doctor is talking to a patient. A nurse is checking papers.",
        "questions": [
            "Where are they?",
            "What is the doctor doing?",
            "What is the nurse doing?"
        ]
    }
]

USEFUL_EXPRESSIONS = [
    "This picture shows ...",
    "I can see ...",
    "There is ...",
    "There are ...",
    "A man is ...",
    "A woman is ...",
    "Some people are ...",
    "In the background, ...",
    "On the left, ...",
    "On the right, ...",
    "They look happy / busy / relaxed.",
    "The place looks peaceful / crowded / clean."
]

# =====================================================
# 세션 상태
# =====================================================
if "task_index" not in st.session_state:
    st.session_state.task_index = 0

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "student_answer" not in st.session_state:
    st.session_state.student_answer = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0


def next_task():
    st.session_state.task_index = (st.session_state.task_index + 1) % len(TASKS)
    st.session_state.submitted = False
    st.session_state.student_answer = ""


def random_task():
    st.session_state.task_index = random.randrange(len(TASKS))
    st.session_state.submitted = False
    st.session_state.student_answer = ""


def check_answer(answer, keywords):
    answer_lower = answer.lower()
    hit = 0
    for kw in keywords:
        if kw.lower() in answer_lower:
            hit += 1
    return hit


# =====================================================
# CSS
# =====================================================
st.markdown(
    """
    <style>
    .title-box {
        background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 50%, #fff7ed 100%);
        border: 1.5px solid #bfdbfe;
        border-radius: 28px;
        padding: 26px 30px;
        margin-bottom: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.07);
    }
    .title-box h1 {
        margin: 0;
        font-size: 40px;
        font-weight: 900;
        color: #0f172a;
    }
    .title-box p {
        margin-top: 10px;
        font-size: 18px;
        color: #334155;
        font-weight: 700;
        line-height: 1.6;
    }
    .picture-card {
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 28px;
        padding: 28px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.07);
        min-height: 330px;
    }
    .big-emoji {
        font-size: 110px;
        margin-bottom: 10px;
    }
    .situation {
        font-size: 22px;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 12px;
    }
    .desc {
        font-size: 17px;
        color: #334155;
        line-height: 1.7;
        font-weight: 700;
    }
    .mission-box {
        background: #fff7ed;
        border: 1.5px solid #fed7aa;
        border-radius: 22px;
        padding: 18px 20px;
        margin-bottom: 14px;
        color: #9a3412;
        font-size: 18px;
        font-weight: 850;
        line-height: 1.6;
    }
    .help-box {
        background: #f8fafc;
        border: 1.5px solid #e2e8f0;
        border-radius: 20px;
        padding: 16px 18px;
        margin-bottom: 12px;
        color: #334155;
        font-weight: 700;
        line-height: 1.6;
    }
    .tag {
        display: inline-block;
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1e40af;
        border-radius: 999px;
        padding: 6px 11px;
        margin: 4px;
        font-size: 14px;
        font-weight: 850;
    }
    .result-box {
        background: #ecfdf5;
        border: 1.5px solid #bbf7d0;
        border-radius: 22px;
        padding: 18px 20px;
        color: #166534;
        font-weight: 800;
        line-height: 1.7;
        margin-top: 14px;
    }
    @media (max-width: 768px) {
        .title-box {
            padding: 20px 18px;
            border-radius: 22px;
        }
        .title-box h1 {
            font-size: 28px;
        }
        .title-box p {
            font-size: 15px;
        }
        .big-emoji {
            font-size: 80px;
        }
        .situation {
            font-size: 19px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 제목
# =====================================================
st.markdown(
    """
    <div class="title-box">
        <h1>🖼️ TBLT 그림 묘사하기</h1>
        <p>
            토익 스피킹 Part 2처럼 그림을 보고 영어로 묘사하는 활동입니다.<br>
            먼저 상황을 파악하고, 키워드를 활용해 4~5문장으로 말해 봅시다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# 탭
# =====================================================
tab1, tab2, tab3 = st.tabs(["🖼️ 그림 묘사 활동", "🧩 표현 연습", "👩‍🏫 수업 운영안"])

# =====================================================
# 탭 1 활동
# =====================================================
with tab1:
    task = TASKS[st.session_state.task_index]

    top1, top2, top3 = st.columns(3)
    with top1:
        st.metric("현재 문제", f"{st.session_state.task_index + 1} / {len(TASKS)}")
    with top2:
        st.metric("점수", f"{st.session_state.score} / {st.session_state.total}")
    with top3:
        if st.button("🎲 랜덤 그림", use_container_width=True):
            random_task()
            st.rerun()

    left, right = st.columns([1.1, 1])

    with left:
        st.markdown(
            f"""
            <div class="picture-card">
                <div class="big-emoji">{task['emoji']}</div>
                <div class="situation">{task['title']}</div>
                <div class="desc">{task['image_prompt']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("➡️ 다음 그림", use_container_width=True):
            next_task()
            st.rerun()

    with right:
        st.markdown(
            """
            <div class="mission-box">
            🎯 미션<br>
            그림을 보고 영어로 4~5문장 말하기 / 쓰기
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("#### 🔑 사용하면 좋은 단어")
        tags = "".join([f"<span class='tag'>{kw}</span>" for kw in task["keywords"]])
        st.markdown(tags, unsafe_allow_html=True)

        with st.expander("💬 질문 힌트 보기"):
            for q in task["questions"]:
                st.markdown(f"- {q}")

        answer = st.text_area(
            "학생 답안",
            value=st.session_state.student_answer,
            height=160,
            placeholder="예: This picture shows a park. Some people are walking..."
        )

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("✅ 제출하기", use_container_width=True):
                st.session_state.student_answer = answer
                hit = check_answer(answer, task["keywords"])
                st.session_state.total += 1
                if hit >= 3:
                    st.session_state.score += 1
                st.session_state.submitted = True
                st.session_state.keyword_hit = hit
                st.rerun()

        with col_b:
            if st.button("🔄 다시 쓰기", use_container_width=True):
                st.session_state.student_answer = ""
                st.session_state.submitted = False
                st.rerun()

        if st.session_state.submitted:
            hit = st.session_state.get("keyword_hit", 0)

            if hit >= 5:
                comment = "아주 좋아요. 그림의 핵심 내용을 충분히 말했습니다."
            elif hit >= 3:
                comment = "좋아요. 핵심 단어를 어느 정도 사용했습니다."
            else:
                comment = "조금 더 구체적으로 말해 봅시다. 장소, 사람, 행동을 넣으면 좋습니다."

            st.markdown(
                f"""
                <div class="result-box">
                <b>피드백</b><br>
                사용한 핵심 단어 수: {hit}개<br>
                {comment}
                </div>
                """,
                unsafe_allow_html=True
            )

            with st.expander("👀 모범 답안 보기"):
                st.markdown("**쉬운 답안**")
                st.info(task["level1"])
                st.markdown("**토익 스피킹식 답안**")
                st.success(task["model"])

# =====================================================
# 탭 2 표현 연습
# =====================================================
with tab2:
    st.markdown("### 🧩 그림 묘사 기본 표현")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="help-box">
            <b>1단계: 장소 말하기</b><br>
            - This picture shows a park.<br>
            - This picture was taken in a cafe.<br>
            - It looks like a library.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="help-box">
            <b>2단계: 사람 말하기</b><br>
            - I can see many people.<br>
            - There is a man.<br>
            - There are some students.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="help-box">
            <b>3단계: 행동 말하기</b><br>
            - A man is reading a book.<br>
            - Some people are walking.<br>
            - A woman is talking on the phone.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="help-box">
            <b>4단계: 위치 말하기</b><br>
            - On the left, ...<br>
            - On the right, ...<br>
            - In the background, ...<br>
            - In the center, ...
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="help-box">
            <b>5단계: 분위기 말하기</b><br>
            - They look happy.<br>
            - The place looks busy.<br>
            - The atmosphere looks peaceful.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="help-box">
            <b>기본 틀</b><br>
            1. This picture shows ...<br>
            2. I can see ...<br>
            3. A person is ...<br>
            4. In the background, ...<br>
            5. The place looks ...
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### 📌 표현 목록")
    for exp in USEFUL_EXPRESSIONS:
        st.markdown(f"- `{exp}`")

# =====================================================
# 탭 3 수업 운영안
# =====================================================
with tab3:
    st.markdown("### 👩‍🏫 TBLT 수업 흐름")

    st.markdown(
        """
        #### 1. Pre-task
        - 그림 속 장소와 사람을 먼저 한국어로 확인
        - 핵심 단어 5~7개 제시
        - 기본 표현 연습: `This picture shows ...`, `I can see ...`

        #### 2. Task
        - 학생이 그림을 보고 영어로 4~5문장 묘사
        - 짝과 서로 답안 비교
        - 더 좋은 표현 1개씩 추가

        #### 3. Language Focus
        - 현재진행형 정리: `be + V-ing`
        - 위치 표현 정리: `on the left`, `in the background`
        - 분위기 표현 정리: `busy`, `peaceful`, `crowded`, `relaxed`

        #### 4. Re-task
        - 같은 그림을 다시 묘사
        - 또는 새 그림으로 30초 말하기
        - 처음 답안보다 문장 수와 표현을 늘리기
        """
    )

    st.markdown("### 📝 간단 평가 기준")
    st.dataframe(
        [
            {"기준": "내용", "설명": "장소, 사람, 행동을 말했는가?", "점수": "0~2점"},
            {"기준": "어휘", "설명": "그림과 관련된 단어를 사용했는가?", "점수": "0~2점"},
            {"기준": "문법", "설명": "현재진행형 be + V-ing를 사용했는가?", "점수": "0~2점"},
            {"기준": "유창성", "설명": "멈춤이 적고 자연스럽게 말했는가?", "점수": "0~2점"},
            {"기준": "완성도", "설명": "4~5문장으로 묘사를 완성했는가?", "점수": "0~2점"},
        ],
        use_container_width=True,
        hide_index=True
    )

st.caption("필요 패키지: streamlit")
