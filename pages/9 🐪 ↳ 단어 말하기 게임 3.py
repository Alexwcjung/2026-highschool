import streamlit as st
import random
import html

st.set_page_config(
    page_title="모두의 단어 말판 게임",
    page_icon="🎲",
    layout="wide"
)

# =========================
# 단어 데이터
# =========================
word_data = [
    {"word": "cat", "meaning": "고양이"},
    {"word": "dog", "meaning": "개"},
    {"word": "sun", "meaning": "태양, 해"},
    {"word": "run", "meaning": "달리다, 뛰다"},
    {"word": "sit", "meaning": "앉다"},
    {"word": "big", "meaning": "큰"},
    {"word": "red", "meaning": "빨간색"},
    {"word": "pen", "meaning": "펜"},
    {"word": "box", "meaning": "상자"},
    {"word": "cup", "meaning": "컵"},
    {"word": "fish", "meaning": "물고기, 생선"},
    {"word": "book", "meaning": "책"},
    {"word": "milk", "meaning": "우유"},
    {"word": "jump", "meaning": "뛰다, 점프하다"},
    {"word": "bed", "meaning": "침대"},
    {"word": "apple", "meaning": "사과"},
    {"word": "banana", "meaning": "바나나"},
    {"word": "happy", "meaning": "행복한, 기쁜"},
    {"word": "sad", "meaning": "슬픈"},
    {"word": "school", "meaning": "학교"},
    {"word": "teacher", "meaning": "선생님, 교사"},
    {"word": "student", "meaning": "학생"},
    {"word": "water", "meaning": "물"},
    {"word": "chair", "meaning": "의자"},
    {"word": "desk", "meaning": "책상"},
    {"word": "phone", "meaning": "전화기, 휴대폰"},
    {"word": "music", "meaning": "음악"},
    {"word": "pizza", "meaning": "피자"},
    {"word": "green", "meaning": "초록색"},
    {"word": "blue", "meaning": "파란색"},
]

# =========================
# 제목
# =========================
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #fce7f3, #e0f2fe, #fef3c7);
        border-radius: 30px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        margin-bottom: 24px;
    ">
        <h1 style="font-size:42px; font-weight:900; color:#1f2937; margin-bottom:8px;">
            🎲 모두의 단어 말판 게임
        </h1>
        <p style="font-size:18px; color:#4b5563; margin:0;">
            모두의 마블처럼 바깥쪽 말판을 돌며 단어의 뜻을 맞히는 모둠 게임입니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("게임 방법: 주사위 굴리기 → 도착한 칸의 단어 읽기 → 한국어 뜻 말하기 → 맞았어요/틀렸어요 클릭")

# =========================
# 설정
# =========================
st.markdown("### ⚙️ 게임 설정")

col1, col2, col3, col4 = st.columns(4)

with col1:
    team_count = st.slider("모둠 수", 2, 6, 4)

with col2:
    board_side = st.slider(
        "말판 크기",
        min_value=5,
        max_value=7,
        value=6,
        help="6이면 6x6 말판이 만들어집니다."
    )

with col3:
    penalty = st.slider("틀리면 뒤로", 0, 3, 1)

with col4:
    show_meaning = st.checkbox("말판에 뜻 보이기", value=False)

team_icons = ["🔴", "🔵", "🟢", "🟡", "🟣", "🟠"]

# =========================
# 보드 경로 만들기
# =========================
def make_path_positions(n):
    path = []

    # 위쪽: 왼쪽 -> 오른쪽
    for c in range(n):
        path.append((0, c))

    # 오른쪽: 위 -> 아래
    for r in range(1, n):
        path.append((r, n - 1))

    # 아래쪽: 오른쪽 -> 왼쪽
    for c in range(n - 2, -1, -1):
        path.append((n - 1, c))

    # 왼쪽: 아래 -> 위
    for r in range(n - 2, 0, -1):
        path.append((r, 0))

    return path


path_positions = make_path_positions(board_side)
board_size = len(path_positions)

# =========================
# 보드 단어 만들기
# =========================
def make_board_words(size):
    random.seed(size)
    if size <= len(word_data):
        return random.sample(word_data, size)

    board = []
    while len(board) < size:
        board.extend(word_data)
    return board[:size]


# =========================
# 세션 초기화
# =========================
if "marble_board_size_saved" not in st.session_state:
    st.session_state.marble_board_size_saved = board_size

if "marble_team_count_saved" not in st.session_state:
    st.session_state.marble_team_count_saved = team_count

if (
    "marble_board_words" not in st.session_state
    or st.session_state.marble_board_size_saved != board_size
):
    st.session_state.marble_board_words = make_board_words(board_size)
    st.session_state.marble_board_size_saved = board_size
    st.session_state.marble_positions = [0 for _ in range(team_count)]
    st.session_state.marble_turn = 0
    st.session_state.marble_dice = "-"
    st.session_state.marble_message = "🎲 주사위를 굴려 게임을 시작하세요!"
    st.session_state.marble_finished = False
    st.session_state.marble_rolled = False

if (
    "marble_positions" not in st.session_state
    or st.session_state.marble_team_count_saved != team_count
):
    st.session_state.marble_positions = [0 for _ in range(team_count)]
    st.session_state.marble_team_count_saved = team_count
    st.session_state.marble_turn = 0
    st.session_state.marble_dice = "-"
    st.session_state.marble_message = "🎲 주사위를 굴려 게임을 시작하세요!"
    st.session_state.marble_finished = False
    st.session_state.marble_rolled = False

if "marble_turn" not in st.session_state:
    st.session_state.marble_turn = 0

if "marble_dice" not in st.session_state:
    st.session_state.marble_dice = "-"

if "marble_message" not in st.session_state:
    st.session_state.marble_message = "🎲 주사위를 굴려 게임을 시작하세요!"

if "marble_finished" not in st.session_state:
    st.session_state.marble_finished = False

if "marble_rolled" not in st.session_state:
    st.session_state.marble_rolled = False

board_words = st.session_state.marble_board_words
positions = st.session_state.marble_positions
current_turn = st.session_state.marble_turn

if current_turn >= team_count:
    current_turn = 0
    st.session_state.marble_turn = 0

current_position = positions[current_turn]
current_item = board_words[current_position]

# =========================
# 상태판
# =========================
st.markdown(
    f"""
    <div style="
        background: linear-gradient(135deg, #dcfce7, #dbeafe, #fce7f3);
        border-radius: 24px;
        padding: 22px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border: 2px solid #bbf7d0;
    ">
        <div style="font-size:32px; font-weight:900; color:#14532d;">
            현재 차례: {team_icons[current_turn]} {current_turn + 1}모둠
        </div>
        <div style="font-size:22px; font-weight:800; color:#334155; margin-top:8px;">
            🎲 마지막 주사위: {st.session_state.marble_dice}
        </div>
        <div style="font-size:18px; font-weight:700; color:#475569; margin-top:8px;">
            {st.session_state.marble_message}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 모두의 마블식 보드
# =========================
st.markdown("### 🗺️ 모두의 마블식 단어 말판")

cell_map = {}
for idx, pos in enumerate(path_positions):
    cell_map[pos] = idx

board_html = f"""
<div style="
    background: linear-gradient(135deg, #eff6ff, #fff7ed, #f0fdf4);
    border: 6px solid #93c5fd;
    border-radius: 34px;
    padding: 24px;
    margin-top: 22px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.14);
">
<div style="
    display: grid;
    grid-template-columns: repeat({board_side}, 1fr);
    gap: 12px;
">
"""

for r in range(board_side):
    for c in range(board_side):
        if (r, c) in cell_map:
            i = cell_map[(r, c)]
            item = board_words[i]
            word = html.escape(item["word"])
            meaning = html.escape(item["meaning"])

            teams_here = []
            for team_idx, pos in enumerate(positions):
                if pos == i:
                    teams_here.append(f"{team_icons[team_idx]}{team_idx + 1}")

            markers = " ".join(teams_here)

            is_start = i == 0
            is_finish = i == board_size - 1
            is_current = i == current_position

            if is_finish:
                bg = "linear-gradient(135deg, #fef3c7, #fecaca)"
                border = "#f97316"
                label = "🏁 FINISH"
            elif is_start:
                bg = "linear-gradient(135deg, #dcfce7, #dbeafe)"
                border = "#22c55e"
                label = "START"
            elif is_current:
                bg = "linear-gradient(135deg, #fce7f3, #dbeafe)"
                border = "#ec4899"
                label = f"현재 {i + 1}"
            else:
                bg = "white"
                border = "#e5e7eb"
                label = f"{i + 1}"

            meaning_html = ""
            if show_meaning:
                meaning_html = f"""
                <div style="font-size:14px; font-weight:700; color:#475569; margin-top:4px;">
                    {meaning}
                </div>
                """

            board_html += f"""
            <div style="
                min-height: 125px;
                background: {bg};
                border: 4px solid {border};
                border-radius: 22px;
                padding: 10px;
                text-align: center;
                box-shadow: 0 5px 14px rgba(0,0,0,0.10);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div style="font-size:13px; font-weight:900; color:#64748b;">
                    {label}
                </div>
                <div style="font-size:24px; font-weight:900; color:#111827; line-height:1.2;">
                    {word}
                </div>
                {meaning_html}
                <div style="font-size:22px; font-weight:900; min-height:28px;">
                    {markers}
                </div>
            </div>
            """
        else:
            board_html += f"""
            <div style="
                min-height: 125px;
                background: rgba(255,255,255,0.35);
                border: 3px dashed rgba(147,197,253,0.55);
                border-radius: 22px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #94a3b8;
                font-size: 20px;
                font-weight: 900;
            ">
                🎲
            </div>
            """

board_html += """
</div>
</div>
"""

st.markdown(board_html, unsafe_allow_html=True)

# =========================
# 현재 미션
# =========================
st.markdown(
    f"""
    <div style="
        background: white;
        border-radius: 26px;
        padding: 22px;
        margin: 20px 0;
        text-align: center;
        border: 3px solid #fed7aa;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    ">
        <div style="font-size:18px; font-weight:900; color:#9a3412;">
            현재 미션
        </div>
        <div style="font-size:44px; font-weight:900; color:#111827; margin-top:8px;">
            {html.escape(current_item["word"])}
        </div>
        <div style="font-size:20px; font-weight:800; color:#475569; margin-top:8px;">
            {current_turn + 1}모둠은 이 단어를 읽고 한국어 뜻을 말하세요.
        </div>
        <div style="font-size:20px; font-weight:900; color:#2563eb; margin-top:8px;">
            교사용 정답: {html.escape(current_item["meaning"])}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 게임 진행 버튼
# =========================
st.markdown("### 🎮 게임 진행")

col_roll, col_correct, col_wrong, col_reset = st.columns(4)

with col_roll:
    if st.button("🎲 주사위 굴리기", use_container_width=True):
        if not st.session_state.marble_finished:
            dice = random.randint(1, 6)
            st.session_state.marble_dice = dice

            new_pos = positions[current_turn] + dice
            if new_pos >= board_size - 1:
                new_pos = board_size - 1

            positions[current_turn] = new_pos
            moved_word = board_words[new_pos]["word"]

            st.session_state.marble_message = (
                f"🚀 {current_turn + 1}모둠이 {dice}칸 이동했습니다. "
                f"'{moved_word}' 단어의 뜻을 말하세요!"
            )
            st.session_state.marble_rolled = True
            st.rerun()

with col_correct:
    if st.button("✅ 맞았어요", use_container_width=True):
        if not st.session_state.marble_finished:
            if not st.session_state.marble_rolled:
                st.session_state.marble_message = "먼저 주사위를 굴려 주세요!"
            else:
                if positions[current_turn] >= board_size - 1:
                    st.session_state.marble_finished = True
                    st.session_state.marble_message = f"🏆 {current_turn + 1}모둠 승리!"
                    st.balloons()
                else:
                    st.session_state.marble_message = f"✅ {current_turn + 1}모둠 정답! 다음 모둠 차례입니다."
                    st.session_state.marble_turn = (current_turn + 1) % team_count
                    st.session_state.marble_rolled = False
            st.rerun()

with col_wrong:
    if st.button("❌ 틀렸어요", use_container_width=True):
        if not st.session_state.marble_finished:
            if not st.session_state.marble_rolled:
                st.session_state.marble_message = "먼저 주사위를 굴려 주세요!"
            else:
                new_pos = max(0, positions[current_turn] - penalty)
                positions[current_turn] = new_pos

                st.session_state.marble_message = (
                    f"😢 {current_turn + 1}모둠 오답! "
                    f"{penalty}칸 뒤로 이동합니다."
                )
                st.session_state.marble_turn = (current_turn + 1) % team_count
                st.session_state.marble_rolled = False
            st.rerun()

with col_reset:
    if st.button("🔄 게임 리셋", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key.startswith("marble_"):
                del st.session_state[key]
        st.rerun()
