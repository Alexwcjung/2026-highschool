# =========================
# 4. 활동 탭
# =========================
with tab_activity:
    st.markdown(f"## 🎮 {data['title']} Activities")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 1. Reading Check</div>
    <p style="font-size:20px;">Reading 내용을 잘 이해했는지 확인해 봅시다.</p>
</div>
""", unsafe_allow_html=True)

    # 인물별 이해 문제
    # 나중에 다른 인물도 추가할 수 있도록 data 안에 없으면 기본 문제를 사용
    if "comprehension_questions" in data:
        comprehension_questions = data["comprehension_questions"]
    else:
        comprehension_questions = [
            {
                "question": "1. What sport does the student like?",
                "options": ["Baseball", "Soccer", "Basketball", "Tennis"],
                "answer": "Soccer"
            },
            {
                "question": "2. What position does the student usually play?",
                "options": ["Goalkeeper", "Defender", "Forward", "Coach"],
                "answer": "Forward"
            },
            {
                "question": "3. What does Ronaldo tell the student to do?",
                "options": [
                    "Stop practicing",
                    "Give up when tired",
                    "Believe in yourself and never give up",
                    "Play computer games"
                ],
                "answer": "Believe in yourself and never give up"
            }
        ]

    user_choices = []

    for i, q in enumerate(comprehension_questions, start=1):
        choice = st.radio(
            q["question"],
            q["options"],
            key=f"{person_name}_comprehension_{i}"
        )
        user_choices.append((choice, q["answer"]))

    if st.button("✅ 이해 문제 정답 확인", key=f"{person_name}_comprehension_check"):
        score = 0

        for i, (choice, answer) in enumerate(user_choices, start=1):
            if choice == answer:
                score += 1
                st.success(f"{i}번 정답입니다!")
            else:
                st.error(f"{i}번 정답은 **{answer}** 입니다.")

        st.markdown(f"## 점수: {score} / {len(comprehension_questions)}")

        if score == 3:
            st.balloons()
            st.success("완벽합니다! Reading 내용을 아주 잘 이해했습니다. 🏆")
        elif score == 2:
            st.info("좋습니다! 거의 다 이해했습니다. Reading을 한 번 더 읽으면 더 좋아집니다.")
        else:
            st.warning("괜찮습니다. Reading을 다시 읽고 핵심 표현을 확인해 봅시다.")

    st.markdown("---")

    st.markdown("""
<div class="activity-box">
    <div class="big-word">Mission 2. Reflection Writing</div>
    <p style="font-size:20px;">
    Ronaldo와의 대화를 읽고, 본인이 배울 점을 적어 봅시다.<br>
    영어로 써도 되고, 한국어로 써도 됩니다.
    </p>
</div>
""", unsafe_allow_html=True)

    reflection = st.text_area(
        "✍️ Ronaldo를 통해 내가 배울 점은 무엇인가요?",
        placeholder="예: I learned that I should believe in myself and never give up.\n또는: 로날도를 보며 지쳐도 포기하지 않고 계속 연습하는 태도를 배워야겠다고 생각했다.",
        height=180,
        key=f"{person_name}_reflection"
    )

    if st.button("💬 피드백 받기", key=f"{person_name}_reflection_feedback"):
        text = reflection.strip()

        if not text:
            st.warning("먼저 자신의 생각을 한 문장 이상 적어 주세요.")
        else:
            word_count = len(text.split())
            char_count = len(text)

            st.markdown("### 💬 Feedback")

            # 영어로 쓴 경우 간단 판정
            english_letters = sum(1 for ch in text if ch.isalpha() and ch.lower() in "abcdefghijklmnopqrstuvwxyz")
            korean_letters = sum(1 for ch in text if "가" <= ch <= "힣")

            if english_letters > korean_letters:
                st.success("영어로 자신의 생각을 표현하려고 한 점이 좋습니다.")

                if word_count >= 12:
                    st.info("문장의 길이도 충분합니다. 자신의 생각을 비교적 구체적으로 표현했습니다.")
                else:
                    st.info("좋은 시작입니다. 이유를 한 문장 더 추가하면 더 좋은 답이 됩니다.")

                if "because" in text.lower():
                    st.success("because를 사용해서 이유를 설명한 점이 좋습니다.")
                else:
                    st.warning("다음에는 because를 사용해서 이유를 덧붙여 보세요.")

                if "never give up" in text.lower() or "believe" in text.lower() or "practice" in text.lower():
                    st.success("오늘 배운 핵심 표현을 잘 활용했습니다.")
                else:
                    st.info("오늘 배운 표현인 believe in yourself, never give up, keep practicing 중 하나를 넣어 보면 더 좋습니다.")

                st.markdown("""
#### ✨ 더 좋은 예시
I learned that I should believe in myself and never give up because practice is very important.
""")

            else:
                st.success("자신의 생각을 한국어로 잘 표현했습니다.")

                if char_count >= 40:
                    st.info("내용이 충분히 구체적입니다. 단순한 감상이 아니라 배울 점을 잘 적었습니다.")
                else:
                    st.info("좋은 시작입니다. 왜 그렇게 생각했는지 이유를 조금 더 쓰면 더 좋습니다.")

                if "포기" in text or "연습" in text or "노력" in text or "믿" in text:
                    st.success("오늘 지문의 핵심 메시지와 잘 연결했습니다.")
                else:
                    st.info("로날도의 메시지인 연습, 자신감, 포기하지 않는 태도와 연결하면 더 좋습니다.")

                st.markdown("""
#### ✨ 영어로 바꾸면 이렇게 쓸 수 있어요
I learned that I should believe in myself and never give up.
""")

            st.markdown("---")
            st.markdown("### 🌟 Teacher Comment")
            st.success("좋습니다. 이 활동의 핵심은 정답을 맞히는 것이 아니라, 지문 속 인물의 태도를 내 삶과 연결해 보는 것입니다.")
