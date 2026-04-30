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

dice_faces = {
    "-": "🎲",
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅",
}

event_templates = [
    {"type": "event", "title": "🚀 앞으로 2칸", "action": "forward2", "desc": "앞으로 2칸 이동"},
    {"type": "event", "title": "🌀 뒤로 2칸", "action": "back2", "desc": "뒤로 2칸 이동"},
    {"type": "event", "title": "🎲 한 번 더", "action": "extra", "desc": "한 번 더 굴리기"},
    {"type": "event", "title": "😴 한 번 쉬기", "action": "skip", "desc": "다음 차례 쉬기"},
    {"type": "event", "title": "🔄 자리 바꾸기", "action": "swap", "desc": "1등과 자리 바꾸기"},
]

# =========================
# 제목
# =========================
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #fce7f3, #e0f2fe, #fef3c7);
        border-radius: 30px;
        padding: 26px 24px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        margin-bottom: 18px;
    ">
        <h1 style="font-size:42px; font-weight:900; color:#1f2937; margin-bottom:8px;">
            🗺️ 모두의 단어 말판
        </h1>
        <p style="font-size:18px; color:#4b5563; margin:0;">
            주사위 2개를 굴려 이동하고, 도착한 칸의 단어 뜻을 맞히는 게임
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.info("자기 차례에 주사위 2개를 굴리면 캐릭터가 이동합니다. 도착한 칸의 영어 단어를 보고 한국어 뜻을 말하세요.")

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
        selected = st.selectbox(
            f"{i + 1}번",
            character_options,
            index=i,
            key=f"char_select_{i}"
        )
        selected_chars.append(selected)

# =========================
# 보드 경로 만들기
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
# 보드 아이템 만들기
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

    return board


def reset_game():
    for key in list(st.session_state.keys()):
        if key.startswith("marble_"):
            del st.session_state[key]


# =========================
# 세션 상태 초기화
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
    st.session_state.marble_dice1 = "-"
    st.session_state.marble_dice2 = "-"
    st.session_state.marble_message = "🎲 주사위를 굴려 시작하세요!"
    st.session_state.marble_finished = False
    st.session_state.marble_needs_answer = False
    st.session_state.marble_show_answer = False
    st.session_state.marble_skip = [False for _ in range(player_count)]
    st.session_state.marble_roll_count = 0
    st.session_state.marble_last_moved_player = None

if (
    "marble_positions" not in st.session_state
    or st.session_state.marble_player_count_saved != player_count
):
    st.session_state.marble_positions = [0 for _ in range(player_count)]
    st.session_state.marble_player_count_saved = player_count
    st.session_state.marble_turn = 0
    st.session_state.marble_dice = "-"
    st.session_state.marble_dice1 = "-"
    st.session_state.marble_dice2 = "-"
    st.session_state.marble_message = "🎲 주사위를 굴려 시작하세요!"
    st.session_state.marble_finished = False
    st.session_state.marble_needs_answer = False
    st.session_state.marble_show_answer = False
    st.session_state.marble_skip = [False for _ in range(player_count)]
    st.session_state.marble_roll_count = 0
    st.session_state.marble_last_moved_player = None

for key, default in {
    "marble_turn": 0,
    "marble_dice": "-",
    "marble_dice1": "-",
    "marble_dice2": "-",
    "marble_message": "🎲 주사위를 굴려 시작하세요!",
    "marble_finished": False,
    "marble_needs_answer": False,
    "marble_show_answer": False,
    "marble_roll_count": 0,
    "marble_last_moved_player": None,
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
            st.session_state.marble_message = "🚀 앞으로 2칸! 도착 단어의 뜻을 말하세요."
            st.session_state.marble_needs_answer = True
        else:
            st.session_state.marble_message = "🚀 앞으로 2칸 이동했습니다!"
            advance_turn()

    elif action == "back2":
        positions[turn] = max(0, positions[turn] - 2)
        landed = board_items[positions[turn]]

        if landed["type"] == "word":
            st.session_state.marble_message = "🌀 뒤로 2칸! 도착 단어의 뜻을 말하세요."
            st.session_state.marble_needs_answer = True
        else:
            st.session_state.marble_message = "🌀 뒤로 2칸 이동했습니다!"
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
# 현재 상태 안내
# =========================
st.markdown(
    f"""
    <div style="
        background: linear-gradient(135deg, #dcfce7, #dbeafe, #fce7f3);
        border-radius: 24px;
        padding: 18px;
        margin: 16px 0;
        text-align: center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border: 2px solid #bbf7d0;
    ">
        <div style="font-size:28px; font-weight:900; color:#14532d;">
            현재 차례: {selected_chars[current_turn]} {current_turn + 1}번
        </div>
        <div style="font-size:20px; font-weight:800; color:#334155; margin-top:8px;">
            마지막 주사위: {st.session_state.marble_dice1} + {st.session_state.marble_dice2} = {st.session_state.marble_dice}
        </div>
        <div style="font-size:18px; font-weight:700; color:#475569; margin-top:8px;">
            {html.escape(st.session_state.marble_message)}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 버튼
# =========================
st.markdown("### 🎮 게임 진행")

col_roll, col_flip, col_correct, col_wrong, col_reset = st.columns(5)

with col_roll:
    if st.button("🎲 주사위 굴리기", use_container_width=True):
        if st.session_state.marble_finished:
            st.session_state.marble_message = "이미 게임이 끝났습니다."

        elif st.session_state.marble_needs_answer:
            st.session_state.marble_message = "먼저 맞았어요 / 틀렸어요를 눌러 주세요."

        else:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice = dice1 + dice2

            st.session_state.marble_dice1 = dice1
            st.session_state.marble_dice2 = dice2
            st.session_state.marble_dice = dice
            st.session_state.marble_show_answer = False
            st.session_state.marble_roll_count += 1
            st.session_state.marble_last_moved_player = current_turn

            new_pos = positions[current_turn] + dice
            if new_pos >= board_size - 1:
                new_pos = board_size - 1

            positions[current_turn] = new_pos
            landed = board_items[new_pos]

            if landed["type"] == "word":
                st.session_state.marble_message = (
                    f"{selected_chars[current_turn]} {current_turn + 1}번이 "
                    f"{dice1}+{dice2}={dice}칸 이동했습니다. 도착한 칸의 단어 뜻을 말하세요."
                )
                st.session_state.marble_needs_answer = True
            else:
                st.session_state.marble_message = (
                    f"{selected_chars[current_turn]} {current_turn + 1}번이 "
                    f"{dice1}+{dice2}={dice}칸 이동했습니다. 이벤트: {landed['title']}"
                )
                apply_event(landed)

        st.rerun()

with col_flip:
    if st.button("🔁 정답 뒤집기", use_container_width=True):
        if st.session_state.marble_needs_answer:
            st.session_state.marble_show_answer = not st.session_state.marble_show_answer
        else:
            st.session_state.marble_message = "현재 뒤집을 단어가 없습니다."
        st.rerun()

with col_correct:
    if st.button("✅ 맞았어요", use_container_width=True):
        st.session_state.marble_show_answer = False

        if st.session_state.marble_finished:
            st.session_state.marble_message = "이미 게임이 끝났습니다."

        elif not st.session_state.marble_needs_answer:
            st.session_state.marble_message = "현재 확인할 단어가 없습니다."

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
            st.session_state.marble_message = "현재 확인할 단어가 없습니다."

        else:
            positions[current_turn] = max(0, positions[current_turn] - penalty)
            st.session_state.marble_message = (
                f"😢 {current_turn + 1}번 오답! {penalty}칸 뒤로 이동합니다."
            )
            st.session_state.marble_needs_answer = False
            advance_turn()

        st.rerun()

with col_reset:
    if st.button("🔄 리셋", use_container_width=True):
        reset_game()
        st.rerun()

# =========================
# 말판
# =========================
st.markdown("### 🗺️ 모두의 마블식 단어 말판")

cell_map = {}
for idx, pos in enumerate(path_positions):
    cell_map[pos] = idx

dice_value = st.session_state.marble_dice
dice1_value = st.session_state.marble_dice1
dice2_value = st.session_state.marble_dice2

dice1_face = dice_faces.get(dice1_value, "🎲")
dice2_face = dice_faces.get(dice2_value, "🎲")

roll_count = st.session_state.marble_roll_count

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
    font-size: 24px;
    font-weight: 900;
    min-height: 30px;
}}

.bounce {{
    animation: bounceMove 0.9s ease-in-out;
    display: inline-block;
}}

@keyframes bounceMove {{
    0% {{ transform: translateY(0) scale(1); }}
    20% {{ transform: translateY(-18px) scale(1.15); }}
    40% {{ transform: translateY(0) scale(1); }}
    60% {{ transform: translateY(-12px) scale(1.12); }}
    80% {{ transform: translateY(0) scale(1); }}
    100% {{ transform: translateY(0) scale(1); }}
}}

.center-cell {{
    min-height: 125px;
    background: rgba(255,255,255,0.55);
    border: 3px dashed rgba(147,197,253,0.75);
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #64748b;
    box-sizing: border-box;
}}

.dice-box {{
    width: 100%;
}}

.dice-row {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 14px;
}}

.dice-face {{
    font-size: 66px;
    font-weight: 900;
    display: inline-block;
    animation: diceJumpRoll 0.9s ease-in-out;
}}

.dice-face.second {{
    animation-delay: 0.08s;
}}

@keyframes diceJumpRoll {{
    0% {{ transform: translateY(0) rotate(0deg) scale(0.6); }}
    15% {{ transform: translateY(-28px) rotate(100deg) scale(1.15); }}
    30% {{ transform: translateY(0) rotate(180deg) scale(0.9); }}
    45% {{ transform: translateY(-22px) rotate(280deg) scale(1.2); }}
    60% {{ transform: translateY(0) rotate(380deg) scale(0.95); }}
    78% {{ transform: translateY(-14px) rotate(540deg) scale(1.1); }}
    100% {{ transform: translateY(0) rotate(720deg) scale(1); }}
}}

.dice-text {{
    font-size: 18px;
    font-weight: 900;
    color: #334155;
    margin-top: 8px;
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
        font-size: 16px;
        min-height: 18px;
    }}

    .dice-face {{
        font-size: 34px;
    }}

    .dice-row {{
        gap: 4px;
    }}

    .dice-text {{
        font-size: 11px;
    }}
}}
</style>
</head>
<body>
<div class="board-wrap">
<div class="board-grid">
"""

center_cells = []
for r in range(1, board_side - 1):
    for c in range(1, board_side - 1):
        center_cells.append((r, c))

center_index = len(center_cells) // 2
dice_center_pos = center_cells[center_index] if center_cells else (1, 1)

for r in range(board_side):
    for c in range(board_side):
        if (r, c) in cell_map:
            i = cell_map[(r, c)]
            item = board_items[i]

            markers = []
            for player_idx, pos in enumerate(positions):
                if pos == i:
                    marker_class = ""
                    if st.session_state.marble_last_moved_player == player_idx:
                        marker_class = "bounce"
                    markers.append(
                        f"<span class='{marker_class}'>{html.escape(selected_chars[player_idx])}{player_idx + 1}</span>"
                    )

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

            show_answer_here = (
                st.session_state.marble_show_answer
                and st.session_state.marble_needs_answer
                and i == positions[current_turn]
                and item["type"] == "word"
            )

            if item["type"] == "event":
                cell_word = html.escape(item["title"])
                cell_desc = html.escape(item["desc"])
            else:
                if show_answer_here:
                    cell_word = html.escape(item["meaning"])
                    cell_desc = "한국어 뜻"
                    bg = "linear-gradient(135deg, #dcfce7, #dbeafe)"
                    border = "#22c55e"
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
            if (r, c) == dice_center_pos:
                board_html += f"""
                <div class="center-cell">
                    <div class="dice-box" key="{roll_count}">
                        <div class="dice-row">
                            <div class="dice-face">{dice1_face}</div>
                            <div class="dice-face second">{dice2_face}</div>
                        </div>
                        <div class="dice-text">주사위: {dice1_value} + {dice2_value} = {dice_value}</div>
                    </div>
                </div>
                """
            else:
                board_html += """
                <div class="center-cell">
                    <div style="font-size:18px; font-weight:900; color:#94a3b8;">
                        모두의<br>단어 말판
                    </div>
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
