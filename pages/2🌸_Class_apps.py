import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components
from gtts import gTTS
import io
import base64
from streamlit_drawable_canvas import st_canvas
import random
import html

st.set_page_config(
    page_title="Classroom Tools",
    page_icon="🧰",
    layout="wide"
)

# Function to create word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud


st.title("🧰 수업 도구 모음")
# 학생 안내 문구
# =========================
st.markdown("""
<div style="
    background: linear-gradient(135deg, #eef7ff, #f7fbff);
    border: 1px solid #d6e9ff;
    border-radius: 18px;
    padding: 22px 24px;
    margin-bottom: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
">
    <p style="font-size:18px; line-height:1.7; margin-bottom:12px;">
        이 앱은 수업 시간에 바로 사용할 수 있는 간단한 도구 모음입니다.
        위의 탭을 눌러 필요한 기능을 선택하세요.
    </p>
    <ul style="font-size:16px; line-height:1.8; margin-bottom:0;">
        <li><b>Blackboard</b>: 칠판처럼 글을 크게 보여줍니다.</li>
        <li><b>Drawing</b>: 화면에 자유롭게 그림을 그릴 수 있습니다.</li>
        <li><b>QR code</b>: 인터넷 주소를 QR 코드로 바꿉니다.</li>
        <li><b>Timer</b>: 활동 시간을 정하고 타이머를 사용할 수 있습니다.</li>
        <li><b>WordCloud</b>: 입력한 글에서 중요한 단어를 구름 모양으로 보여줍니다.</li>
        <li><b>Emoji</b>: 수업 자료에 사용할 이모지를 쉽게 찾을 수 있습니다.</li>
        <li><b>Multi-TTS</b>: 여러 언어의 문장을 음성으로 들을 수 있습니다.</li>
        <li><b>Grouping</b>: 학생들을 무작위로 조 편성할 수 있습니다.</li>
        <li><b>Translation</b>: 영어↔한국어 번역을 하고, 영어 문장의 발음도 들을 수 있습니다.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
# Streamlit tabs
tabs = st.tabs([
    "✏️Blackboard",
    "🎨Drawing",
    "🔳QR code",
    "⏳Timer",
    "☁️WordCloud",
    "😀Emoji",
    "👥Grouping",
    "🌐Translation"
])

# --- Tab 0: Blackboard ---
with tabs[0]:
    st.subheader("📚 Blackboard")

    c1, c2 = st.columns([1, 1])
    with c1:
        font_size = st.slider("Text size", 12, 124, 32, 2)
    with c2:
        text_color = st.color_picker("Text color", "#ffffff")

    text = st.text_area("✍️ Write on the board", height=100, placeholder="Type your ideas here...")

    st.markdown(
        f"""
        <div style="
            background-color: #006666;
            padding: 1.5rem;
            border-radius: 10px;
            min-height: 350px;
            font-size: {font_size}px;
            color: {text_color};
            line-height: 1.6;
            white-space: pre-wrap;
        ">
        {text if text.strip() else " "}
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Tab 1: Drawing ---
with tabs[1]:
    st.caption("Use the canvas below to draw freely. You can change the stroke width and color.")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        stroke_width = st.slider("✏️ Stroke Width", 1, 10, 5)
    with col2:
        stroke_color = st.color_picker("🖌 Stroke Color", "#000000")
    with col3:
        bg_color = st.color_picker("🖼 Background Color", "#FFFFFF")

    if "clear_canvas" not in st.session_state:
        st.session_state["clear_canvas"] = False

    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=400,
        width=600,
        drawing_mode="freedraw",
        key="main_canvas" if not st.session_state["clear_canvas"] else "new_canvas"
    )

    if st.button("🗑️ Clear Canvas"):
        st.session_state["clear_canvas"] = not st.session_state["clear_canvas"]
        st.rerun()

# --- Tab 2: QR ---
with tabs[2]:
    st.caption("QR code generator")

    col1, col2, col3 = st.columns([3, 3, 2])
    with col1:
        qr_link = st.text_input("📌 Enter URL link:", key="qr_link")
    with col2:
        caption = st.text_input("Enter a caption (optional):", key="qr_caption")
    with col3:
        st.write("")
        generate_qr_button = st.button("🔆 Click to Generate QR", key="generate_qr")

    if generate_qr_button and qr_link:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_link)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white').convert('RGB').resize((600, 600))
        st.image(qr_img, caption=caption if caption else "Generate", use_container_width=False, width=400)

# --- Tab 3: Timer ---
with tabs[3]:
    st.subheader("⏳ Classroom Timer")
    st.caption("Set the time and click Start.")

    col1, col2, col3 = st.columns(3)

    with col1:
        timer_min = st.number_input("Minutes", min_value=0, max_value=180, value=5, step=1)

    with col2:
        timer_sec = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=5)

    with col3:
        st.write("")
        st.write("")
        st.info(f"Set time: {timer_min:02d}:{timer_sec:02d}")

    total_seconds = timer_min * 60 + timer_sec

    timer_html = f"""
    <div style="
        width: 100%;
        max-width: 700px;
        margin: 20px auto;
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #f8fbff, #eef5ff);
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
        text-align: center;
        font-family: Arial, sans-serif;
    ">
        <div id="timerDisplay" style="
            font-size: 90px;
            font-weight: 800;
            color: #1f4e79;
            margin-bottom: 25px;
        ">
            {timer_min:02d}:{timer_sec:02d}
        </div>

        <button onclick="startTimer()" style="
            font-size: 24px;
            padding: 12px 28px;
            margin: 8px;
            border: none;
            border-radius: 12px;
            background-color: #2e86de;
            color: white;
            cursor: pointer;
        ">Start</button>

        <button onclick="pauseTimer()" style="
            font-size: 24px;
            padding: 12px 28px;
            margin: 8px;
            border: none;
            border-radius: 12px;
            background-color: #f39c12;
            color: white;
            cursor: pointer;
        ">Pause</button>

        <button onclick="resetTimer()" style="
            font-size: 24px;
            padding: 12px 28px;
            margin: 8px;
            border: none;
            border-radius: 12px;
            background-color: #e74c3c;
            color: white;
            cursor: pointer;
        ">Reset</button>

        <p id="message" style="
            margin-top: 25px;
            font-size: 28px;
            font-weight: bold;
            color: #d63031;
        "></p>
    </div>

    <script>
        let initialTime = {total_seconds};
        let remainingTime = initialTime;
        let timerInterval = null;

        function updateDisplay() {{
            let minutes = Math.floor(remainingTime / 60);
            let seconds = remainingTime % 60;

            document.getElementById("timerDisplay").innerHTML =
                String(minutes).padStart(2, '0') + ":" + String(seconds).padStart(2, '0');
        }}

        function startTimer() {{
            if (timerInterval !== null) {{
                return;
            }}

            document.getElementById("message").innerHTML = "";

            timerInterval = setInterval(function() {{
                if (remainingTime > 0) {{
                    remainingTime--;
                    updateDisplay();
                }} else {{
                    clearInterval(timerInterval);
                    timerInterval = null;
                    document.getElementById("message").innerHTML = "Time's up!";

                    let audio = new Audio("https://actions.google.com/sounds/v1/alarms/beep_short.ogg");
                    audio.play();
                }}
            }}, 1000);
        }}

        function pauseTimer() {{
            clearInterval(timerInterval);
            timerInterval = null;
        }}

        function resetTimer() {{
            clearInterval(timerInterval);
            timerInterval = null;
            remainingTime = initialTime;
            document.getElementById("message").innerHTML = "";
            updateDisplay();
        }}

        updateDisplay();
    </script>
    """

    components.html(timer_html, height=450)

# --- Tab 4: WordCloud ---
with tabs[4]:
    st.subheader("☁️ WordCloud Generator")
    st.caption("Paste text below and generate a word cloud.")

    wc_text = st.text_area(
        "📋 Paste text here",
        height=220,
        placeholder="Paste your text here...",
        key="wc_text"
    )

    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        max_words = st.slider("Max words", 30, 300, 120, 10)
    with c2:
        bg = st.selectbox("Background", ["white", "black"], index=0)
    with c3:
        colormap = st.selectbox("Color style", ["viridis", "plasma", "inferno", "magma", "cividis"], index=0)

    if st.button("✨ Generate WordCloud", key="btn_wc"):
        if not wc_text.strip():
            st.warning("Please paste some text first.")
        else:
            wc = WordCloud(
                width=1000,
                height=500,
                background_color=bg,
                max_words=max_words,
                colormap=colormap
            ).generate(wc_text)

            fig, ax = plt.subplots(figsize=(12, 6))
            ax.imshow(wc, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)

# --- Tab 5: Emoji ---
with tabs[5]:
    st.subheader("😀 Emoji Board")
    st.caption("큰 이모지 박스에서 필요한 부분을 드래그해서 복사한 뒤 수업 자료, 칠판, 활동지에 붙여 넣으세요.")

    EMOJI_CATEGORIES = {
        "😀 감정/표정": """
😀 😃 😄 😁 😆 😅 😂 🤣 🙂 🙃 😉 😊 😇
😍 🥰 😘 😗 😙 😚 😋 😛 😜 🤪 😝 🤑
🤗 🤭 🤫 🤔 🤨 😐 😑 😶 🙄 😏 😒 😬
😮 😯 😲 😳 🥺 😦 😧 😨 😰 😥 😢 😭
😱 😖 😣 😞 😓 😩 😫 🥱 😴 😌 😎 🤓 🧐
😕 😟 🙁 ☹️ 😮‍💨 😤 😡 😠 🤯 🫢 🫣
👍 👎 👏 🙌 👐 🤲 🙏 👌 ✌️ 🤞 🤟 🤘 💪
👀 👂 👃 👄 👅 🧠 🗣️ 👤 👥
🧑 👨 👩 👦 👧 👶 👴 👵
👨‍🏫 👩‍🏫 🧑‍🏫 👨‍🎓 👩‍🎓 🧑‍🎓
        """,

        "📚 수업/학습": """
📚 📖 📕 📗 📘 📙 📔 📒 📓 📝 ✏️
🖊️ 🖋️ 🖍️ 📐 📏 📌 📍 📎 🖇️ ✂️
🗂️ 📁 📂 🗒️ 📋 📊 📈 📉 🧾 📰
🎓 🏫 🧑‍🏫 👩‍🏫 👨‍🏫 🧑‍🎓 👩‍🎓 👨‍🎓
💡 🔍 🔎 🧪 🔬 🔭 🧲
💻 🖥️ ⌨️ 🖱️ 🖨️ 📱 📲
🎤 🎧 🎼 🎹 🎸 🥁
        """,

        "🎯 활동/평가": """
🎯 ✅ ☑️ ✔️ ❌ ❎ ⭕ ⭐ 🌟 💯 🏆
🥇 🥈 🥉 🎲 🎮 🧩 🃏 🔔 ⏰ ⏳
🚀 🔥 🎉 🎊 👏 💬 🗯️ ❓ ❗ 📢 📣
📝 📋 📌 📍 🔖 🎁 🎈
        """,

        "🌍 장소/세계": """
🌍 🌎 🌏 🗺️ 🧭
🏠 🏡 🏫 🏢 🏥 🏦 🏪 🏬 🏭 🏛️
🏰 🏯 🗼 🗽 ⛪ 🕌 🛕 🕍 ⛩️
🌉 🌁 🌃 🌆 🌇 🏞️ 🏝️ 🏖️ 🏜️ ⛰️
🇰🇷 🇺🇸 🇬🇧 🇯🇵 🇨🇳 🇫🇷 🇩🇪 🇪🇸 🇮🇹 🇨🇦
        """,

        "🚗 교통/여행": """
🚗 🚕 🚙 🚌 🚎 🏎️ 🚓 🚑 🚒 🚐 🚚 🚛
🚜 🛵 🏍️ 🚲 🛴
🚂 🚆 🚇 🚊 🚉 🚝 🚄
✈️ 🛫 🛬 🚁 🚀 🛸
⛵ 🚤 🛳️ 🚢 ⚓
🧳 🎒 🛣️ 🛤️ ⛽ 🚦 🚧 🛑 🅿️ 🎫
        """,

        "🍎 음식/생활": """
🍎 🍏 🍊 🍋 🍌 🍉 🍇 🍓 🍒 🍑 🍍 🥭
🍕 🍔 🍟 🌭 🥪 🍞 🥐 🥚 🍗 🍖
🍜 🍝 🍚 🍱 🍣 🍰 🍪 🍫 🍬 🍭
☕ 🥤 🧃 🍽️ 🥢 🥄
        """,

        "🌱 자연/날씨": """
☀️ 🌤️ ⛅ 🌥️ ☁️ 🌧️ ⛈️ 🌩️ 🌨️ ❄️
🌈 💧 💦 🌊 🔥 ⭐ 🌟 ✨ ⚡ 🌙
🌳 🌲 🌴 🌵 🌾 🌱 🌿 🍀 🍁 🍂 🍃
🌹 🌷 🌻 🌼 🌸 🌺 🍄
🐶 🐱 🐭 🐰 🐻 🐼 🐯 🦁 🐵 🐦
🐔 🐧 🐸 🐴 🐮 🐷 🐝 🦋 🐢 🐍
🐙 🦑 🦐 🦀 🐠 🐟 🐬 🐳 🐋
        """,

        "🏺 역사/사회": """
🏺 🪨 ⚔️ 🛡️ 👑 🏛️ 📜 🕯️ 🪖 🗳️
🇰🇷 🐻 🌅 🦅 🚢 🏭 🌐 🤝 ⚖️ 🕊️
📚 📖 📝 🔍 🗺️ 🧭 ⏳
        """,

        "🔢 숫자/기호": """
0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟
⬅️ ➡️ ⬆️ ⬇️ ↗️ ↘️ ↙️ ↖️ ↔️ ↕️
🔁 🔄 🔃 ▶️ ⏸️ ⏹️ ⏭️ ⏮️ ⏪ ⏩
➕ ➖ ✖️ ➗
🔴 🟠 🟡 🟢 🔵 🟣 ⚫ ⚪
🟥 🟧 🟨 🟩 🟦 🟪 ⬛ ⬜
🅰️ 🅱️ 🆎 🅾️ 🆕 🆗 🆙 🆒 🆓 🆘
        """,
    }

    emoji_tabs = st.tabs(list(EMOJI_CATEGORIES.keys()))

    def show_big_emoji_box(emojis, height=360):
        safe_emojis = html.escape(emojis.strip())
        emoji_html = f"""
        <html>
        <head>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background: transparent;
                font-family: Arial, sans-serif;
            }}
            .emoji-box {{
                background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
                border: 2px solid #e2e8f0;
                border-radius: 22px;
                padding: 22px 24px;
                font-size: 34px;
                line-height: 1.75;
                word-spacing: 9px;
                box-shadow: 0 5px 14px rgba(0,0,0,0.06);
                user-select: text;
                white-space: pre-wrap;
                overflow-y: auto;
                height: {height - 40}px;
                box-sizing: border-box;
            }}
            @media (max-width: 768px) {{
                .emoji-box {{
                    font-size: 28px;
                    line-height: 1.7;
                    padding: 18px;
                }}
            }}
        </style>
        </head>
        <body>
            <div class="emoji-box">{safe_emojis}</div>
        </body>
        </html>
        """
        components.html(emoji_html, height=height, scrolling=False)

    for tab, (category, emojis) in zip(emoji_tabs, EMOJI_CATEGORIES.items()):
        with tab:
            st.markdown(f"### {category}")
            show_big_emoji_box(emojis, height=390)

# --- Tab 6: Grouping ---
with tabs[6]:
    st.subheader("👥 Grouping Tool")
    st.caption("CSV를 올리지 않아도 기본 명단으로 조 편성을 할 수 있습니다.")
    st.caption("CSV를 올릴 경우, 반드시 `Course`, `Names` 열이 있어야 합니다.")

    default_data = pd.DataFrame({
        "Course": [
            "Class 1", "Class 1", "Class 1", "Class 1", "Class 1",
            "Class 1", "Class 1", "Class 1", "Class 1", "Class 1",
            "Class 2", "Class 2", "Class 2", "Class 2", "Class 2",
            "Class 2", "Class 2", "Class 2", "Class 2", "Class 2"
        ],
        "Names": [
            "Student 1", "Student 2", "Student 3", "Student 4", "Student 5",
            "Student 6", "Student 7", "Student 8", "Student 9", "Student 10",
            "Student 11", "Student 12", "Student 13", "Student 14", "Student 15",
            "Student 16", "Student 17", "Student 18", "Student 19", "Student 20"
        ]
    })

    uploaded_file = st.file_uploader("🌱 Step 1: Upload your CSV file (optional)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        source_label = "✅ Uploaded CSV data"
    else:
        df = default_data
        source_label = "📂 Using default sample data"

    if all(col in df.columns for col in ["Course", "Names"]):
        st.markdown("### 📋 Current Student List")
        st.dataframe(df, use_container_width=True)

        course_list = df["Course"].dropna().unique().tolist()
        selected_course = st.selectbox("🌱 Step 2: Select Course for Grouping", course_list)

        course_df = df[df["Course"] == selected_course]
        names = course_df["Names"].dropna().tolist()
        total_students = len(names)

        st.info(
            f"{source_label} | 🎓 **{selected_course}**: "
            f"Total **{total_students}** students available for grouping."
        )

        st.markdown("##### 🌱 Step 3: Group Settings")

        col_in1, col_in2 = st.columns(2)

        with col_in1:
            num_group3 = st.number_input(
                "Number of 3-member groups",
                min_value=0,
                value=0,
                step=1
            )

        with col_in2:
            num_group4 = st.number_input(
                "Number of 4-member groups",
                min_value=0,
                value=0,
                step=1
            )

        needed_students = num_group3 * 3 + num_group4 * 4

        st.write(f"Selected students needed: **{needed_students}**")
        st.write(f"Available students: **{total_students}**")

        if needed_students > total_students:
            st.warning("설정한 조 인원 수가 현재 학생 수보다 많습니다. 조 개수를 줄여 주세요.")

        if st.button("🌱 Step 4: Generate Groups"):
            if total_students == 0:
                st.warning("No students available for grouping.")

            elif num_group3 == 0 and num_group4 == 0:
                st.warning("Please enter at least one group.")

            else:
                names_for_grouping = names.copy()
                random.shuffle(names_for_grouping)

                grouped_data = []
                group_num = 1
                assigned_count = 0

                for _ in range(num_group3):
                    if len(names_for_grouping) >= 3:
                        members = names_for_grouping[:3]
                        names_for_grouping = names_for_grouping[3:]

                        group_row = {"Group": f"Group {group_num}"}
                        for i, member in enumerate(members):
                            group_row[f"Member{i+1}"] = member

                        grouped_data.append(group_row)
                        group_num += 1
                        assigned_count += 3

                for _ in range(num_group4):
                    if len(names_for_grouping) >= 4:
                        members = names_for_grouping[:4]
                        names_for_grouping = names_for_grouping[4:]

                        group_row = {"Group": f"Group {group_num}"}
                        for i, member in enumerate(members):
                            group_row[f"Member{i+1}"] = member

                        grouped_data.append(group_row)
                        group_num += 1
                        assigned_count += 4

                remaining_count = len(names_for_grouping)

                if remaining_count > 0:
                    group_row = {"Group": f"Group {group_num} (Remainder)"}
                    for i, member in enumerate(names_for_grouping):
                        group_row[f"Member{i+1}"] = member

                    grouped_data.append(group_row)
                    assigned_count += remaining_count

                if not grouped_data:
                    st.warning("No groups were created. Please check your settings.")

                else:
                    grouped_df = pd.DataFrame(grouped_data)

                    cols = ["Group"] + [
                        c for c in grouped_df.columns if c.startswith("Member")
                    ]

                    grouped_df = grouped_df[cols].fillna("")

                    st.success(
                        f"✅ Grouping Complete! "
                        f"Total {assigned_count} students assigned to {len(grouped_data)} groups."
                    )

                    st.dataframe(grouped_df, use_container_width=True)

                    csv_text = grouped_df.to_csv(index=False)
                    csv_bytes = csv_text.encode("utf-8-sig")

                    st.download_button(
                        label="📥 Download Grouped CSV",
                        data=csv_bytes,
                        file_name=f"grouped_{selected_course.replace(' ', '_')}.csv",
                        mime="text/csv"
                    )

    else:
        st.error("The file must contain both `Course`, `Names` columns.")

# --- Tab 7: Translation ---
with tabs[7]:
    st.subheader("🌐 Translation Tool")
    lang_options = {
        "한국어 Korean": "ko",
        "영어 English": "en",
        "일본어 Japanese": "ja",
        "중국어 Chinese Simplified": "zh-CN",
        "스페인어 Spanish": "es",
        "프랑스어 French": "fr",
        "독일어 German": "de",
        "러시아어 Russian": "ru",
        "베트남어 Vietnamese": "vi",
        "태국어 Thai": "th",
        "인도네시아어 Indonesian": "id",
        "아랍어 Arabic": "ar",
        "힌디어 Hindi": "hi",
        "이탈리아어 Italian": "it",
        "포르투갈어 Portuguese": "pt",
    }

    if "translated_text" not in st.session_state:
        st.session_state["translated_text"] = ""
    if "translation_target_code" not in st.session_state:
        st.session_state["translation_target_code"] = ""

    c1, c2 = st.columns(2)
    with c1:
        source_lang_label = st.selectbox(
            "원문 언어",
            ["자동 감지 Auto"] + list(lang_options.keys()),
            index=0
        )
    with c2:
        target_lang_label = st.selectbox(
            "번역할 언어",
            list(lang_options.keys()),
            index=0
        )

    source_text = st.text_area(
        "번역할 문장을 입력하세요",
        height=200,
        placeholder="예: I like soccer. / 나는 축구를 좋아합니다.",
        key="translation_source_input"
    )

    if st.button("🌐 번역하기", use_container_width=True):
        if not source_text.strip():
            st.warning("번역할 문장을 먼저 입력하세요.")
        else:
            try:
                from deep_translator import GoogleTranslator

                source_code = "auto" if source_lang_label == "자동 감지 Auto" else lang_options[source_lang_label]
                target_code = lang_options[target_lang_label]

                translated = GoogleTranslator(
                    source=source_code,
                    target=target_code
                ).translate(source_text)

                st.session_state["translated_text"] = translated
                st.session_state["translation_target_code"] = target_code

            except ModuleNotFoundError:
                st.error("번역 기능을 사용하려면 deep-translator 패키지를 설치해야 합니다.")
                st.code("pip install deep-translator", language="bash")
                st.info("Streamlit Cloud에서는 requirements.txt에 deep-translator를 추가하세요.")

            except Exception as e:
                st.error("번역 중 오류가 발생했습니다.")
                st.write(e)

    if st.session_state["translated_text"]:
        st.markdown("#### 번역 결과")

        translated_result = st.text_area(
            "",
            value=st.session_state["translated_text"],
            height=200,
            key="translation_result",
            label_visibility="collapsed"
        )

    if st.session_state["translation_target_code"] == "en":
        speed_label = st.radio(
            "",
            ["0.25", "0.5", "1", "1.25", "1.5"],
            index=2,
            horizontal=True,
            label_visibility="collapsed"
        )

            playback_rate = float(speed_label)

            if st.button("🔊 발음 듣기", use_container_width=True):
                if not translated_result.strip():
                    st.warning("읽을 영어 문장이 없습니다.")
                else:
                    try:
                        tts = gTTS(text=translated_result, lang="en", tld="com", slow=False)
                        speech = io.BytesIO()
                        tts.write_to_fp(speech)
                        speech.seek(0)

                        audio_base64 = base64.b64encode(speech.getvalue()).decode("utf-8")

                        audio_html = f"""
                        <div style="
                            background: #f8fafc;
                            border: 1px solid #e2e8f0;
                            border-radius: 16px;
                            padding: 16px;
                            margin-top: 8px;
                        ">
                            <audio id="english_audio" controls autoplay style="width: 100%;">
                                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                            </audio>
                            <script>
                                const audio = document.getElementById("english_audio");
                                audio.playbackRate = {playback_rate};
                            </script>
                            <p style="margin-top:10px; color:#475569; font-size:14px;">
                                현재 속도: <b>{speed_label}x</b>
                            </p>
                        </div>
                        """
                        components.html(audio_html, height=130)

                    except Exception as e:
                        st.error("영어 발음 생성 중 오류가 발생했습니다.")
                        st.write(e)
        else:
            st.info("번역할 언어를 영어 English로 선택하면 영어 발음을 들을 수 있습니다.")

