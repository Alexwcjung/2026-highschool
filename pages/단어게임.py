# =========================
# 여기부터 말판 게임 코드
# word_themes = {...} 아래에 붙여 넣으세요
# =========================

import random
import html

# =========================
# 말판 게임용 CSS
# =========================
st.markdown(
    """
    <style>
    .game-title {
        font-size: 42px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 6px;
    }

    .game-subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 24px;
    }

    .rule-box {
        background: linear-gradient(135deg, #fce7f3 0%, #e0f2fe 50%, #fef3c7 100%);
        border-radius: 26px;
        padding: 22px 26px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        line-height: 1.8;
        font-size: 17px;
    }

    .status-box {
        background: linear-gradient(135deg, #dcfce7 0%, #dbeafe 50%, #fce7f3 100%);
        border-radius: 24px;
        padding: 22px 24px;
        margin: 18px 0;
        text-align: center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border: 2px solid #bbf7d0;
    }

    .big-board {
        background: linear-gradient(135deg, #fff7ed, #eff6ff, #f0fdf4);
        border: 5px solid #93c5fd;
        border-radius: 34px;
        padding: 24px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.14);
        margin-top: 20px;
    }

    .board-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 14px;
    }

    .board-cell {
        min-height: 128px;
        border-radius: 22px;
        padding: 10px;
        text-align: center;
        box-shadow: 0 5px 14px rgba(0,0,0,0.10);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .cell-num {
        font-size: 14px;
        font-weight: 900;
        color: #64748b;
    }

    .cell-word {
        font-size: 25px;
        font-weight: 900;
        color: #111827;
        line-height: 1.2;
        word-break: keep-all;
    }

    .cell-meaning {
        font-size: 15px;
        font-weight: 700;
        color: #475569;
        line-height: 1.25;
    }

    .team-marker {
        font-size: 21px;
        font-weight: 900;
        min-height: 26px;
    }

    .mission-box {
        background: white;
        border-radius: 26px;
        padding: 22px;
        margin: 20px 0;
        text-align: center;
        border: 3px solid #fed7aa;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }

    .stButton > button {
        border-radius: 999px;
        font-weight: 900;
        padding: 0.55rem 1rem;
    }

    @media (max-width: 900px) {
        .board-grid {
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }

        .board-cell {
            min-height: 110px;
            padding: 8px;
        }

        .cell-word {
            font-size: 20px;
        }
    }

    @media (max-width: 600px) {
        .board-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .game-title {
            font-size: 32px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 제목
# =========================
st.markdown("<div class='game-title'>🎲 단어 말판 단체전</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='game-subtitle'>큰 말판 위의 단어를 읽고 뜻을 말하며 모둠별로 이동하는 보드게임입니다.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="rule-box">
        <b>📌 게임 방법</b><br>
        1. 단어 테마를 고릅니다.<br>
        2. 모둠이 차례대로 <b>주사위 굴리기</b>를 누릅니다.<br>
        3. 말이 도착한 칸의 <b>영어 단어를 읽고 뜻을 말합니다.</b><br>
        4. 맞으면 그 칸에 머물고, 틀리면 뒤로 이동합니다.<br>
        5. 먼저 마지막 칸에 도착해서 단어를 맞히는 모둠이 승리합니다.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 세션 키 함수
# =========================
def make_safe_key(text):
    return (
        text.replace(" ", "_")
        .replace("/", "_")
        .replace("·", "_")
        .replace("️", "")
    )


def game_key(theme, name):
    return f"word_board_{make_safe_key(theme)}_{name}"


def reset_board_game(theme):
    prefix = f"word_board_{make_safe_key(theme)}_"
    delete_keys = [k for k in st.session_state.keys() if k.startswith(prefix)]

    for k in delete_keys:
        del st.session_state[k]


def make_board_words(theme, words, board_size):
    key = game_key(theme, "board_words")

    if key not in st.session_state:
        if len(words) >= board_size:
            random.seed(f"{theme}_{board_size}")
            board_words = random.sample(words, board_size)
        else:
            board_words = []
            while len(board_words) < board_size:
                board_words.extend(words)
            board_words = board_words[:board_size]

        st.session_state[key] = board_words

    return st.session_state[key]


# =========================
# 게임 설정
# =========================
st.markdown("### ⚙️ 게임 설정")

theme = st.selectbox(
    "단어 테마를 선택하세요.",
    list(word_themes.keys())
)

theme_words = word_themes[theme]

col1, col2, col3, col4 = st.columns(4)

with col1:
    team_count = st.slider(
        "모둠 수",
        min_value=2,
        max_value=6,
        value=4,
        step=1
    )

with col2:
    board_size = st.slider(
        "말판 칸 수",
        min_value=12,
        max_value=36,
        value=24,
        step=6
    )

with col3:
    penalty = st.slider(
        "틀리면 뒤로",
        min_value=0,
        max_value=3,
        value=1,
        step=1
    )

with col4:
    show_meaning = st.checkbox(
        "말판에 뜻 보이기",
        value=False
    )

# =========================
# 상태 초기화
# =========================
board_words = make_board_words(theme, theme_words, board_size)

pos_key = game_key(theme, "positions")
turn_key = game_key(theme, "turn")
dice_key = game_key(theme, "dice")
msg_key = game_key(theme, "message")
finish_key = game_key(theme, "finished")
rolled_key = game_key(theme, "rolled")

if pos_key not in st.session_state:
    st.session_state[pos_key] = [0 for _ in range(team_count)]

if len(st.session_state[pos_key]) != team_count:
    st.session_state[pos_key] = [0 for _ in range(team_count)]

if turn_key not in st.session_state:
    st.session_state[turn_key] = 0

if dice_key not in st.session_state:
    st.session_state[dice_key] = "-"

if msg_key not in st.session_state:
    st.session_state[msg_key] = "🎲 주사위를 굴려 게임을 시작하세요!"

if finish_key not in st.session_state:
    st.session_state[finish_key] = False

if rolled_key not in st.session_state:
    st.session_state[rolled_key] = False

positions = st.session_state[pos_key]
current_turn = st.session_state[turn_key]

if current_turn >= team_count:
    current_turn = 0
    st.session_state[turn_key] = 0

current_position = positions[current_turn]
current_item = board_words[current_position]

team_icons = ["🔴", "🔵", "🟢", "🟡", "🟣", "🟠"]

# =========================
# 상태판
# =========================
st.markdown(
    f"""
    <div class="status-box">
        <div style="font-size:32px; font-weight:900; color:#14532d;">
            현재 차례: {current_turn + 1}모둠 {team_icons[current_turn]}
        </div>
        <div style="font-size:22px; font-weight:800; color:#334155; margin-top:8px;">
            🎲 마지막 주사위: {st.session_state[dice_key]}
        </div>
        <div style="font-size:18px; font-weight:700; color:#475569; margin-top:8px;">
            {st.session_state[msg_key]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# 큰 말판
# =========================
st.markdown("### 🗺️ 큰 단어 말판")

board_html = """
<div class="big-board">
<div class="board-grid">
"""

for i, item in enumerate(board_words):
    word = html.escape(item["word"])
    meaning = html.escape(item["meaning"])

    teams_here = []
    for team_idx, pos in enumerate(positions):
        if pos == i:
            teams_here.append(f"{team_icons[team_idx]}{team_idx + 1}")

    markers = " ".join(teams_here)

    is_current = i == current_position
    is_start = i == 0
    is_finish = i == board_size - 1

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

    if show_meaning:
        meaning_html = f"<div class='cell-meaning'>{meaning}</div>"
    else:
        meaning_html = "<div class='cell-meaning'>&nbsp;</div>"

    board_html += f"""
    <div class="board-cell" style="background:{bg}; border:4px solid {border};">
        <div class="cell-num">{label}</div>
        <div class="cell-word">{word}</div>
        {meaning_html}
        <div class="team-marker">{markers}</div>
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
    <div class="mission-box">
        <div style="font-size:18px; font-weight:900; color:#9a3412;">
            현재 미션
        </div>
        <div style="font-size:44px; font-weight:900; color:#111827; margin-top:8px;">
            {html.escape(current_item["word"])}
        </div>
        <div style="font-size:20px; font-weight:800; color:#475569; margin-top:8px;">
            {current_turn + 1}모둠은 이 단어를 읽고 뜻을 말하세요.
        </div>
        <div style="font-size:20px; font-weight:900; color:#2563eb; margin-top:8px;">
            정답: {html.escape(current_item["meaning"])}
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
        if not st.session_state[finish_key]:
            dice = random.randint(1, 6)
            st.session_state[dice_key] = dice

            new_pos = positions[current_turn] + dice
            if new_pos >= board_size - 1:
                new_pos = board_size - 1

            positions[current_turn] = new_pos

            moved_word = board_words[new_pos]["word"]
            st.session_state[msg_key] = (
                f"🚀 {current_turn + 1}모둠이 {dice}칸 이동했습니다. "
                f"말판의 '{moved_word}' 단어를 읽고 뜻을 말하세요!"
            )

            st.session_state[rolled_key] = True
            st.rerun()

with col_correct:
    if st.button("✅ 맞았어요", use_container_width=True):
        if not st.session_state[finish_key]:
            if not st.session_state[rolled_key]:
                st.session_state[msg_key] = "먼저 주사위를 굴려 주세요!"
            else:
                if positions[current_turn] >= board_size - 1:
                    st.session_state[finish_key] = True
                    st.session_state[msg_key] = f"🏆 {current_turn + 1}모둠 승리!"
                    st.balloons()
                else:
                    st.session_state[msg_key] = f"✅ {current_turn + 1}모둠 정답! 다음 모둠 차례입니다."
                    st.session_state[turn_key] = (current_turn + 1) % team_count
                    st.session_state[rolled_key] = False

            st.rerun()

with col_wrong:
    if st.button("❌ 틀렸어요", use_container_width=True):
        if not st.session_state[finish_key]:
            if not st.session_state[rolled_key]:
                st.session_state[msg_key] = "먼저 주사위를 굴려 주세요!"
            else:
                old_pos = positions[current_turn]
                new_pos = max(0, old_pos - penalty)
                positions[current_turn] = new_pos

                st.session_state[msg_key] = (
                    f"😢 {current_turn + 1}모둠 오답! "
                    f"{penalty}칸 뒤로 이동합니다."
                )
                st.session_state[turn_key] = (current_turn + 1) % team_count
                st.session_state[rolled_key] = False

            st.rerun()

with col_reset:
    if st.button("🔄 게임 리셋", use_container_width=True):
        reset_board_game(theme)
        st.rerun()

# =========================
# 모둠 위치표
# =========================
st.markdown("---")
st.markdown("### 📍 모둠 위치")

team_cols = st.columns(team_count)

for i in range(team_count):
    with team_cols[i]:
        pos = positions[i]
        word = board_words[pos]["word"]

        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border-radius:20px;
                padding:16px;
                text-align:center;
                border:3px solid #dbeafe;
                box-shadow:0 4px 10px rgba(0,0,0,0.05);
            ">
                <div style="font-size:25px; font-weight:900;">
                    {team_icons[i]} {i + 1}모둠
                </div>
                <div style="font-size:18px; font-weight:800; color:#475569; margin-top:6px;">
                    {pos + 1}번 칸
                </div>
                <div style="font-size:22px; font-weight:900; color:#111827; margin-top:6px;">
                    {html.escape(word)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
