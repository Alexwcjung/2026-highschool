import streamlit as st
import streamlit.components.v1 as components
import random
import html

st.set_page_config(
    page_title="모두의 단어 말판",
    page_icon="🗺️",
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

character_options = [
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼",
    "🐯", "🦁", "🐸", "🐵", "🐧", "🐢", "🦄", "🐳"
]

event_templates = [
    {"type": "event", "title": "🚀 앞으로 2칸", "action": "forward2", "desc": "바로 앞으로 2칸 이동!"},
    {"type": "event", "title": "🌀 뒤로 2칸", "action": "back2", "desc": "바로 뒤로 2칸 이동!"},
    {"type": "event", "title": "🎲 한 번 더", "action": "extra", "desc": "같은 학생이 한 번 더 굴리기!"},
    {"type": "event", "title": "😴 한 번 쉬기", "action": "skip", "desc": "다음 차례를 한 번 쉽니다."},
    {"type": "event", "title": "🔄 자리 바꾸기", "action": "swap", "desc": "가장 앞선 학생과 자리 바꾸기!"},
]

dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅",
    "-": "🎲"
}

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
        margin-bottom: 20px;
    ">
        <h1 style="font-size:42px; font-weight:900; color:#1f2937; margin-bottom:8px;">
            🗺️ 모두의 단어 말판
        </h1>
        <p style="font-size:18px; color:#4b5563; margin:0;">
            주사위를 굴려 이동하고, 단어의 한국어 뜻을 서로 확인하는 게임입니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("자기 차례에 주사위를 굴리면 바로 이동합니다. 도착한 단어의 뜻을 말하고, 다른 학생들이 맞았는지 확인합니다.")

# =========================
# 설정
# =========================
st.markdown("### ⚙️ 게임 설정")

col1, col2, col3 = st.columns(3)

with col1:
    player_count = st.slider("학생 / 모둠 수", 1, 4, 4)

with col2:
    board_side = st.slider("말판 크기", 5, 7, 6)

with col3:
    penalty = st.slider("틀리면 뒤로", 0, 3, 1)

st.markdown("### 🧸 캐릭터 선택")

char_cols = st.columns(player_count)

selected_chars = []

for i in range(player_count):
    with char_cols[i]:
        default_index = i
        selected = st.selectbox(
            f"{i + 1}번",
            character_options,
            index=default_index,
            key=f"char_select_{i}"
        )
        selected_chars.append(selected)

# =========================
# 보드 경로
# =========================
def make_path_positions(n):
    path = []

    for c in range(n):
        path.append((0, c))

    for r in range(1, n):
        path.append((r, n - 1))

    for c in range(n - 2, -1, -1):
        path.append((n - 1, c))

    for r in range(n - 2, 0, -1):
        path.append((r, 0))

    return path


path_positions = make_path_positions(board_side)
board_size = len(path_positions)

# =========================
# 보드 아이템
# =========================
def make_board_items(size):
    random.seed(size)

    if size <= len(word_data):
        selected_words = random.sample(word_data, size)
    else:
        selected_words = []
        while len(selected_words) < size:
            selected_words.extend(word_data)
        selected_words = selected_words[:size]

    board = []

    for item in selected_words:
        board.append({
            "type": "word",
            "word": item["word"],
            "meaning": item["meaning"]
        })

    possible_event_positions = list(range(3, size - 2))
    event_count = max(3, size // 5)

    random.seed(f"events_{size}")
    event_positions = random.sample(
        possible_event_positions,
        min(event_count, len(possible_event_positions))
    )

    for idx, pos in enumerate(event_positions):
        board[pos] = event_templates[idx % len(event_templates)]

    # START와 FINISH는 단어 칸으로 둠
    return board


def reset_game():
    for key in list(st.session_state.keys()):
        if key.startswith("marble_"):
            del st.session_state[key]


# =========================
# 세션 초기화
# =========================
if "marble_board_side_saved" not in st.session_state:
    st.session_state.marble_board_side_saved = board_side

if "marble_player_count_saved" not in st.session_state:
    st.session_state.marble_player_count_saved = player_count

if (
    "marble_board_items" not in st.session_state
    or st.session_state.marble_board_side_saved != board_side
):
    st.session_state.marble_board_items = make_board_items(board_size)
    st.session_state.marble_board_side_saved = board_side
    st.session_state.marble_positions = [0 for _ in range(player_count)]
    st.session_state.marble_turn = 0
    st.session_state.marble_dice = "-"
    st.session_state.marble_message = "🎲 자기 차례가 되면 주사위를 굴리세요!"
    st.session_state.marble_finished = False
    st.session_state.marble_needs_answer = False
    st.session_state.marble_show_answer = False
    st.session_state.marble_skip = [False for _ in range(player_count)]
    st.session_state.marble_roll_count = 0

if (
    "marble_positions" not in st.session_state
    or st.session_state.marble_player_count_saved != player_count
):
    st.session_state.marble_positions = [0 for _ in range(player_count)]
    st.session_state.marble_player_count_saved = player_count
    st.session_state.marble_turn = 0
    st.session_state.marble_dice = "-"
    st.session_state.marble_message = "🎲 자기 차례가 되면 주사위를 굴리세요!"
    st.session_state.marble_finished = False
    st.session_state.marble_needs_answer = False
    st.session_state.marble_show_answer = False
    st.session_state.marble_skip = [False for _ in range(player_count)]
    st.session_state.marble_roll_count = 0

for key, default in {
    "marble_turn": 0,
    "marble_dice": "-",
    "marble_message": "🎲 자기 차례가 되면 주사위를 굴리세요!",
    "marble_finished": False,
    "marble_needs_answer": False,
    "marble_show_answer": False,
    "marble_roll_count": 0,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

if "marble_skip" not in st.session_state:
    st.session_state.marble_skip = [False for _ in range(player_count)]

if len(st.session_state.marble_skip) != player_count:
    st.session_state.marble_skip = [False for _ in range(player_count)]

board_items = st.session_state.marble_board_items
positions = st.session_state.marble_positions
current_turn = st.session_state.marble_turn

if current_turn >= player_count:
    current_turn = 0
    st.session_state.marble_turn = 0

current_position = positions[current_turn]
current_item = board_items[current_position]

# =========================
# 차례 넘기기
# =========================
def advance_turn():
    if player_count == 1:
        st.session_state.marble_turn = 0
        return

    next_turn = (st.session_state.marble_turn + 1) % player_count

    checked = 0
    while st.session_state.marble_skip[next_turn] and checked < player_count:
        st.session_state.marble_skip[next_turn] = False
        st.session_state.marble_message += f" / {next_turn + 1}번은 한 번 쉬기!"
        next_turn = (next_turn + 1) % player_count
        checked += 1

    st.session_state.marble_turn = next_turn


# =========================
# 이벤트 처리
# =========================
def apply_event(event):
    turn = st.session_state.marble_turn
    positions = st.session_state.marble_positions
    action = event["action"]

    if action == "forward2":
        positions[turn] = min(board_size - 1, positions[turn] + 2)
        landed = board_items[positions[turn]]

        if landed["type"] == "word":
            st.session_state.marble_message = f"🚀 앞으로 2칸! '{landed['word']}' 뜻을 말하세요."
            st.session_state.marble_needs_answer = True
        else:
            st.session_state.marble_message = "🚀 앞으로 2칸 이동!"
            advance_turn()

    elif action == "back2":
        positions[turn] = max(0, positions[turn] - 2)
        landed = board_items[positions[turn]]

        if landed["type"] == "word":
            st.session_state.marble_message = f"🌀 뒤로 2칸! '{landed['word']}' 뜻을 말하세요."
            st.session_state.marble_needs_answer = True
        else:
            st.session_state.marble_message = "🌀 뒤로 2칸 이동!"
            advance_turn()

    elif action == "extra":
        st.session_state.marble_message = "🎲 한 번 더! 같은 학생이 다시 주사위를 굴리세요."
        st.session_state.marble_needs_answer = False

    elif action == "skip":
        st.session_state.marble_skip[turn] = True
        st.session_state.marble_message = "😴 다음 차례를 한 번 쉽니다."
        st.session_state.marble_needs_answer = False
        advance_turn()

    elif action == "swap":
        first_player = max(range(player_count), key=lambda i: positions[i])

        if first_player != turn:
            positions[turn], positions[first_player] = positions[first_player], positions[turn]
            st.session_state.marble_message = f"🔄 {turn + 1}번과 {first_player + 1}번이 자리를 바꿨습니다!"
        else:
            st.session_state.marble_message = "🔄 이미 가장 앞에 있습니다!"

        st.session_state.marble_needs_answer = False
        advance_turn()


# =========================
# 미션 카드
# =========================
st.markdown("### 🎯 현재 미션")

if st.session_state.marble_finished:
    mission_word = "🏆 게임 종료"
    mission_text = st.session_state.marble_message
    answer_text = "수고했습니다!"

elif st.session_state.marble_needs_answer and current_item["type"] == "word":
    mission_word = current_item["word"]
    mission_text = f"{selected_chars[current_turn]} {current_turn + 1}번은 이 단어의 한국어 뜻을 말하세요. 다른 학생들은 맞았는지 확인해 주세요."
    answer_text = current_item["meaning"]

elif current_item["type"] == "event":
    mission_word = current_item["title"]
    mission_text = current_item["desc"]
    answer_text = "이벤트 칸입니다."

else:
    mission_word = "🎲 주사위 굴리기"
    mission_text = f"{selected_chars[current_turn]} {current_turn + 1}번 차례입니다. 주사위를 굴리면 바로 이동합니다."
    answer_text = "주사위를 굴려 주세요."

flip_class = "flipped" if st.session_state.marble_show_answer else ""

mission_html = f"""
<style>
.flip-card {{
    background-color: transparent;
    width: 100%;
    height: 260px;
    perspective: 1000px;
    margin-bottom: 18px;
}}

.flip-card-inner {{
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.7s;
    transform-style: preserve-3d;
}}

.flip-card-inner.flipped {{
    transform: rotateY(180deg);
}}

.flip-card-front, .flip-card-back {{
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 30px;
    padding: 26px 24px;
    box-sizing: border-box;
    box-shadow: 0 8px 24px rgba(0,0,0,0.10);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}}

.flip-card-front {{
    background: linear-gradient(135deg, #fff7ed, #e0f2fe);
    border: 4px solid #fb923c;
}}

.flip-card-back {{
    background: linear-gradient(135deg, #dcfce7, #dbeafe);
    border: 4px solid #22c55e;
    transform: rotateY(180deg);
}}

.mission-small {{
    font-size: 21px;
    font-weight: 900;
    color: #9a3412;
    margin-bottom: 10px;
}}

.mission-word {{
    font-size: 54px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 12px;
}}

.mission-text {{
    font-size: 21px;
    font-weight: 800;
    color: #374151;
    line-height: 1.5;
}}

.answer-title {{
    font-size: 24px;
    font-weight: 900;
    color: #166534;
    margin-bottom: 12px;
}}

.answer-text {{
    font-size: 50px;
    font-weight: 900;
    color: #14532d;
}}

@media (max-width: 700px) {{
    .flip-card {{
        height: 240px;
    }}

    .mission-word {{
        font-size: 38px;
    }}

    .mission-text {{
        font-size: 17px;
    }}

    .answer-text {{
        font-size: 34px;
    }}
}}
</style>

<div class="flip-card">
    <div class="flip-card-inner {flip_class}">
        <div class="flip-card-front">
            <div class="mission-small">현재 차례: {selected_chars[current_turn]} {current_turn + 1}번</div>
            <div class="mission-word">{html.escape(mission_word)}</div>
            <div class="mission-text">{html.escape(mission_text)}</div>
        </div>
        <div class="flip-card-back">
            <div class="answer-title">한국어 뜻</div>
            <div class="answer-text">{html.escape(answer_text)}</div>
        </div>
    </div>
</div>
"""

st.markdown(mission_html, unsafe_allow_html=True)

if st.button("🔁 정답 뒤집기 / 다시 가리기", use_container_width=True):
    st.session_state.marble_show_answer = not st.session_state.marble_show_answer
    st.rerun()

# =========================
# 주사위 시각화
# =========================
dice_value = st.session_state.marble_dice
dice_face = dice_faces.get(dice_value, "🎲")

dice_html = f"""
<style>
.dice-wrap {{
    background: linear-gradient(135deg, #fef3c7, #dbeafe);
    border: 4px solid #93c5fd;
    border-radius: 28px;
    padding: 18px;
    text-align: center;
    margin: 16px 0;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}}

.dice-face {{
    font-size: 74px;
    font-weight: 900;
    animation: diceRoll 0.8s ease-in-out;
}}

@keyframes diceRoll {{
    0% {{ transform: rotate(0deg) scale(0.7); }}
    25% {{ transform: rotate(90deg) scale(1.2); }}
    50% {{ transform: rotate(180deg) scale(0.9); }}
    75% {{ transform: rotate(270deg) scale(1.2); }}
    100% {{ transform: rotate(360deg) scale(1); }}
}}

.dice-text {{
    font-size: 20px;
    font-weight: 900;
    color: #334155;
}}
</style>

<div class="dice-wrap">
    <div class="dice-face">{dice_face}</div>
    <div class="dice-text">마지막 주사위: {dice_value}</div>
    <div class="dice-text">{html.escape(st.session_state.marble_message)}</div>
</div>
"""

components.html(dice_html, height=185)

# =========================
# 버튼
# =========================
st.markdown("### 🎮 게임 진행")

col_roll, col_correct, col_wrong, col_reset = st.columns(4)

with col_roll:
    if st.button("🎲 주사위 굴리기", use_container_width=True):
        if st.session_state.marble_finished:
            st.session_state.marble_message = "이미 게임이 끝났습니다."

        elif st.session_state.marble_needs_answer:
            st.session_state.marble_message = "먼저 현재 단어의 답을 확인해 주세요."

        else:
            dice = random.randint(1, 6)
            st.session_state.marble_dice = dice
            st.session_state.marble_show_answer = False
            st.session_state.marble_roll_count += 1

            new_pos = positions[current_turn] + dice
            if new_pos >= board_size - 1:
                new_pos = board_size - 1

            positions[current_turn] = new_pos
            landed = board_items[new_pos]

            if landed["type"] == "word":
                st.session_state.marble_message = (
                    f"{selected_chars[current_turn]} {current_turn + 1}번이 {dice}칸 이동! "
                    f"'{landed['word']}' 뜻을 말하세요."
                )
                st.session_state.marble_needs_answer = True

            else:
                st.session_state.marble_message = (
                    f"{selected_chars[current_turn]} {current_turn + 1}번이 {dice}칸 이동! "
                    f"이벤트: {landed['title']}"
                )
                apply_event(landed)

        st.rerun()

with col_correct:
    if st.button("✅ 맞았어요", use_container_width=True):
        st.session_state.marble_show_answer = False

        if st.session_state.marble_finished:
            st.session_state.marble_message = "이미 게임이 끝났습니다."

        elif not st.session_state.marble_needs_answer:
            st.session_state.marble_message = "현재 확인할 단어 미션이 없습니다."

        else:
            if positions[current_turn] >= board_size - 1:
                st.session_state.marble_finished = True
                st.session_state.marble_message = f"🏆 {selected_chars[current_turn]} {current_turn + 1}번 승리!"
                st.balloons()
            else:
                st.session_state.marble_message = f"✅ {current_turn + 1}번 정답! 다음 차례입니다."
                st.session_state.marble_needs_answer = False
                advance_turn()

        st.rerun()

with col_wrong:
    if st.button("❌ 틀렸어요", use_container_width=True):
        st.session_state.marble_show_answer = False

        if st.session_state.marble_finished:
            st.session_state.marble_message = "이미 게임이 끝났습니다."

        elif not st.session_state.marble_needs_answer:
            st.session_state.marble_message = "현재 확인할 단어 미션이 없습니다."

        else:
            positions[current_turn] = max(0, positions[current_turn] - penalty)
            st.session_state.marble_message = (
                f"😢 {current_turn + 1}번 오답! {penalty}칸 뒤로 이동합니다."
            )
            st.session_state.marble_needs_answer = False
            advance_turn()

        st.rerun()

with col_reset:
    if st.button("🔄 게임 리셋", use_container_width=True):
        reset_game()
        st.rerun()

# =========================
# 말판
# =========================
st.markdown("### 🗺️ 모두의 마블식 단어 말판")

cell_map = {}
for idx, pos in enumerate(path_positions):
    cell_map[pos] = idx

board_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: transparent;
}}

.board-wrap {{
    background: linear-gradient(135deg, #eff6ff, #fff7ed, #f0fdf4);
    border: 6px solid #93c5fd;
    border-radius: 34px;
    padding: 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.14);
    box-sizing: border-box;
    width: 100%;
}}

.board-grid {{
    display: grid;
    grid-template-columns: repeat({board_side}, 1fr);
    gap: 12px;
}}

.cell {{
    min-height: 125px;
    border-radius: 22px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 5px 14px rgba(0,0,0,0.10);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
}}

.cell-label {{
    font-size: 13px;
    font-weight: 900;
    color: #64748b;
}}

.cell-word {{
    font-size: 22px;
    font-weight: 900;
    color: #111827;
    line-height: 1.2;
    word-break: keep-all;
}}

.cell-desc {{
    font-size: 13px;
    font-weight: 700;
    color: #475569;
    line-height: 1.25;
}}

.markers {{
    font-size: 22px;
    font-weight: 900;
    min-height: 28px;
}}

.center-cell {{
    min-height: 125px;
    background: rgba(255,255,255,0.45);
    border: 3px dashed rgba(147,197,253,0.65);
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #64748b;
    font-size: 20px;
    font-weight: 900;
    line-height: 1.4;
    box-sizing: border-box;
}}

@media (max-width: 700px) {{
    .board-wrap {{
        padding: 10px;
        border-radius: 22px;
        border-width: 4px;
    }}

    .board-grid {{
        gap: 6px;
    }}

    .cell {{
        min-height: 92px;
        border-radius: 15px;
        padding: 6px;
    }}

    .center-cell {{
        min-height: 92px;
        border-radius: 15px;
        font-size: 13px;
    }}

    .cell-label {{
        font-size: 10px;
    }}

    .cell-word {{
        font-size: 15px;
    }}

    .cell-desc {{
        font-size: 10px;
    }}

    .markers {{
        font-size: 14px;
        min-height: 18px;
    }}
}}
</style>
</head>
<body>
<div class="board-wrap">
<div class="board-grid">
"""

for r in range(board_side):
    for c in range(board_side):
        if (r, c) in cell_map:
            i = cell_map[(r, c)]
            item = board_items[i]

            markers = []
            for player_idx, pos in enumerate(positions):
                if pos == i:
                    markers.append(f"{selected_chars[player_idx]}{player_idx + 1}")

            markers_text = " ".join(markers)

            is_start = i == 0
            is_finish = i == board_size - 1
            is_current = i == positions[current_turn]

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

            if item["type"] == "event":
                cell_word = html.escape(item["title"])
                cell_desc = html.escape(item["desc"])
            else:
                cell_word = html.escape(item["word"])
                cell_desc = "뜻 말하기"

            board_html += f"""
            <div class="cell" style="background:{bg}; border:4px solid {border};">
                <div class="cell-label">{label}</div>
                <div class="cell-word">{cell_word}</div>
                <div class="cell-desc">{cell_desc}</div>
                <div class="markers">{markers_text}</div>
            </div>
            """
        else:
            board_html += """
            <div class="center-cell">
                모두의<br>단어 말판
            </div>
            """

board_html += """
</div>
</div>
</body>
</html>
"""

board_height = 930 if board_side == 7 else 780 if board_side == 6 else 650
components.html(board_html, height=board_height, scrolling=True)
