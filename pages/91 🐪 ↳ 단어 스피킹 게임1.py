# =========================
# 미션 박스
# =========================
st.markdown("### 🎯 현재 미션")

if st.session_state.marble_finished:
    mission_word = "🏆 게임 종료"
    mission_text = st.session_state.marble_message
    answer_text = "수고했습니다!"

elif st.session_state.marble_needs_answer and current_item["type"] == "word":
    mission_word = current_item["word"]
    mission_text = f"{team_icons[current_turn]} {current_turn + 1}모둠은 이 단어의 한국어 뜻을 말하세요. 다른 학생들은 맞았는지 확인해 주세요."
    answer_text = current_item["meaning"]

elif current_item["type"] == "event":
    mission_word = current_item["title"]
    mission_text = current_item["desc"]
    answer_text = "이벤트 칸입니다."

else:
    mission_word = "🎲 주사위 굴리기"
    mission_text = f"{team_icons[current_turn]} {current_turn + 1}모둠 차례입니다. 주사위를 굴리면 바로 이동합니다."
    answer_text = "주사위를 굴려 주세요."

show_answer_class = "flipped" if st.session_state.marble_show_answer else ""

mission_html = f"""
<style>
.flip-card {{
    background-color: transparent;
    width: 100%;
    height: 250px;
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
    font-size: 20px;
    font-weight: 900;
    color: #9a3412;
    margin-bottom: 10px;
}}

.mission-word {{
    font-size: 52px;
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

.answer-word {{
    font-size: 24px;
    font-weight: 900;
    color: #166534;
    margin-bottom: 10px;
}}

.answer-text {{
    font-size: 48px;
    font-weight: 900;
    color: #14532d;
}}

@media (max-width: 700px) {{
    .flip-card {{
        height: 230px;
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
    <div class="flip-card-inner {show_answer_class}">
        <div class="flip-card-front">
            <div class="mission-small">현재 차례: {team_icons[current_turn]} {current_turn + 1}모둠</div>
            <div class="mission-word">{html.escape(mission_word)}</div>
            <div class="mission-text">{html.escape(mission_text)}</div>
        </div>

        <div class="flip-card-back">
            <div class="answer-word">한국어 뜻</div>
            <div class="answer-text">{html.escape(answer_text)}</div>
        </div>
    </div>
</div>
"""

st.markdown(mission_html, unsafe_allow_html=True)

if st.button("🔁 정답 뒤집기 / 다시 가리기", use_container_width=True):
    st.session_state.marble_show_answer = not st.session_state.marble_show_answer
    st.rerun()
