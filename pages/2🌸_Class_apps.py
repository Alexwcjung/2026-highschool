import streamlit as st

# 이 코드는 기존 classroom tools 코드의 tabs 목록에 "😀Emoji" 탭을 추가한 뒤,
# 맨 아래에 붙여 넣어 사용할 수 있는 간단한 이모지 보드입니다.
#
# 예:
# tabs = st.tabs([
#     "✏️Blackboard", "🎨Drawing", "🔳QR code", "⏳Timer",
#     "☁️WordCloud", "🔊Multi-TTS", "👥Grouping", "😀Emoji"
# ])
#
# 그리고 아래 코드를 맨 아래에 추가하세요.

with tabs[7]:
    st.subheader("😀 Emoji Board")
    st.caption("필요한 이모지를 드래그해서 복사한 뒤, 수업 자료나 코드에 붙여넣으세요.")

    emoji_tabs = st.tabs([
        "😊 사람·감정",
        "🌿 자연·동물",
        "📚 수업·물건",
        "🏫 장소·교통",
        "✅ 기호·숫자",
        "🇰🇷 국기"
    ])

    emoji_style = """
    <style>
    .emoji-preview {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1.5px solid #e2e8f0;
        border-radius: 22px;
        padding: 20px 22px;
        margin: 12px 0 22px 0;
        font-size: 34px;
        line-height: 1.9;
        word-spacing: 10px;
        box-shadow: 0 5px 14px rgba(0,0,0,0.05);
        user-select: text;
    }
    .emoji-title {
        background: #eff6ff;
        border: 1.5px solid #bfdbfe;
        color: #1e3a8a;
        border-radius: 18px;
        padding: 12px 16px;
        margin-top: 10px;
        font-size: 18px;
        font-weight: 900;
    }
    @media (max-width: 768px) {
        .emoji-preview {
            font-size: 28px;
            line-height: 1.8;
            padding: 16px;
        }
    }
    </style>
    """
    st.markdown(emoji_style, unsafe_allow_html=True)

    def emoji_box(title, emojis):
        st.markdown(f"<div class='emoji-title'>{title}</div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="emoji-preview">
                {emojis}
            </div>
            """,
            unsafe_allow_html=True
        )

    with emoji_tabs[0]:
        emoji_box(
            "😊 사람·감정",
            """
            😀 😃 😄 😁 😆 😅 😂 🤣 🙂 🙃 😉 😊 😇
            😍 🥰 😘 😗 😙 😚 😋 😛 😜 🤪 😝 🤑
            🤗 🤭 🤫 🤔 🤨 😐 😑 😶 🙄 😏 😒 😬
            😮 😯 😲 😳 🥺 😦 😧 😨 😰 😥 😢 😭
            😱 😖 😣 😞 😓 😩 😫 🥱 😴 😌 😎 🤓 🧐
            😕 😟 🙁 ☹️ 😮‍💨 😤 😡 😠 🤯 😳 🫢 🫣
            👏 🙌 👐 🤲 🙏 👍 👎 👌 ✌️ 🤞 🤟 🤘 💪
            👀 👂 👃 👄 👅 🧠 🫀 🫁 🦷 🦴
            🗣️ 👤 👥 🧑 👨 👩 👦 👧 👶 👴 👵
            👨‍🏫 👩‍🏫 🧑‍🏫 👨‍🎓 👩‍🎓 🧑‍🎓 👨‍💻 👩‍💻 🧑‍💻
            """
        )

    with emoji_tabs[1]:
        emoji_box(
            "🌿 자연·동물",
            """
            ☀️ 🌤️ ⛅ 🌥️ ☁️ 🌧️ ⛈️ 🌩️ 🌨️ ❄️
            🌈 💧 💦 🌊 🔥 ⭐ 🌟 ✨ ⚡ 🌙 🌎 🌍 🌏
            🌳 🌲 🌴 🌵 🌾 🌱 🌿 🍀 🍁 🍂 🍃
            🌹 🌷 🌻 🌼 🌸 🌺 🪷 🍄 🪨
            🐶 🐱 🐭 🐹 🐰 🦊 🐻 🐼 🐨 🐯 🦁
            🐮 🐷 🐸 🐵 🐔 🐧 🐦 🐤 🦆 🦅 🦉
            🐺 🐗 🐴 🦄 🐝 🐛 🦋 🐌 🐞 🐜 🦗
            🕷️ 🦂 🐢 🐍 🦎 🐙 🦑 🦐 🦀 🐡 🐠
            🐟 🐬 🐳 🐋 🦈 🐊 🐅 🐆 🦓 🦍 🐘
            🦒 🦘 🐪 🐫 🦙 🐄 🐖 🐏 🐑 🐎
            """
        )

    with emoji_tabs[2]:
        emoji_box(
            "📚 수업·물건",
            """
            📚 📖 📕 📗 📘 📙 📔 📒 📓 📝 ✏️
            🖊️ 🖋️ 🖍️ 📐 📏 📌 📍 📎 🖇️ ✂️
            🗂️ 📁 📂 🗒️ 📋 📊 📈 📉 🧾 📰
            💻 🖥️ ⌨️ 🖱️ 🖨️ 📱 📲 ☎️ 📞 📟 📠
            📷 📸 🎥 📹 🎬 🎤 🎧 🎼 🎹 🎸 🥁
            🔍 🔎 💡 🔦 🕯️ 🧪 🔬 🔭 🧲 🧰 🪛 🔧
            🎲 🎮 🧩 🏆 🥇 🥈 🥉 🎯 🎁 🎈 🎉 🎊
            ⏰ ⏱️ ⏲️ 🕰️ ⌛ ⏳ 🔔 📢 📣
            🍎 🍏 🍊 🍋 🍌 🍉 🍇 🍓 🍒 🍑 🍍 🥭
            🍕 🍔 🍟 🌭 🥪 🌮 🍜 🍚 🍱 🍣 🍰 🍪 ☕
            """
        )

    with emoji_tabs[3]:
        emoji_box(
            "🏫 장소·교통",
            """
            🏠 🏡 🏫 🏢 🏥 🏦 🏪 🏬 🏭 🏰 🏯
            🗼 🗽 ⛪ 🕌 🛕 🕍 ⛩️ 🏟️ 🎡 🎢 🎠
            ⛲ ⛺ 🌁 🌉 🌃 🌆 🌇 🏞️ 🏝️ 🏖️ 🏜️
            🚗 🚕 🚙 🚌 🚎 🏎️ 🚓 🚑 🚒 🚐 🚚 🚛
            🚜 🛵 🏍️ 🚲 🛴 🚂 🚆 🚇 🚊 🚉 🚝 🚄
            ✈️ 🛫 🛬 🚁 🚀 🛸 ⛵ 🚤 🛳️ 🚢 ⚓
            🚧 🚦 🚥 🗺️ 🧭 🧳 🛂 🛃 🛄 🛅
            """
        )

    with emoji_tabs[4]:
        emoji_box(
            "✅ 기호·숫자",
            """
            ✅ ☑️ ✔️ ❌ ❎ ⭕ 🔴 🟠 🟡 🟢 🔵 🟣
            ⚫ ⚪ 🟥 🟧 🟨 🟩 🟦 🟪 ⬛ ⬜
            ⭐ 🌟 ✨ 💯 🔥 🎯 📌 📍 🚩 🏁
            ❗ ❕ ❓ ❔ ⁉️ ‼️
            ➡️ ⬅️ ⬆️ ⬇️ ↗️ ↘️ ↙️ ↖️ ↔️ ↕️
            🔁 🔄 🔃 ▶️ ⏸️ ⏹️ ⏭️ ⏮️ ⏪ ⏩
            0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟
            🅰️ 🅱️ 🆎 🅾️ 🆕 🆗 🆙 🆒 🆓 🆘
            🔤 🔡 🔠 🔢 #️⃣ *️⃣
            """
        )

    with emoji_tabs[5]:
        emoji_box(
            "🇰🇷 국기",
            """
            🇰🇷 🇺🇸 🇬🇧 🇨🇦 🇦🇺 🇳🇿
            🇯🇵 🇨🇳 🇹🇼 🇭🇰 🇸🇬 🇻🇳 🇹🇭 🇵🇭 🇮🇩 🇲🇾
            🇫🇷 🇩🇪 🇮🇹 🇪🇸 🇵🇹 🇬🇷 🇹🇷 🇷🇺 🇺🇦
            🇮🇳 🇸🇦 🇦🇪 🇮🇷 🇮🇶 🇮🇱
            🇪🇬 🇿🇦 🇰🇪 🇳🇬 🇲🇦
            🇧🇷 🇦🇷 🇨🇱 🇵🇪 🇨🇴 🇲🇽
            """
        )
