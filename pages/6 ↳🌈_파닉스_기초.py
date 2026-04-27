import streamlit as st
import io
from gtts import gTTS

st.set_page_config(page_title="Phonics Guide", layout="centered")


# =========================================================
# 영어 발음 오디오 생성 함수
# =========================================================
@st.cache_data
def make_tts_audio(text):
    fp = io.BytesIO()
    tts = gTTS(text=text, lang="en")
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


def play_audio(text):
    st.audio(make_tts_audio(text), format="audio/mp3")


def render_sound_table(data, headers=("글자", "알파벳 이름", "실제 소리", "예시 단어")):
    h1, h2, h3, h4 = st.columns([1, 1.5, 1.5, 2.5])
    h1.markdown(f"**{headers[0]}**")
    h2.markdown(f"**{headers[1]}**")
    h3.markdown(f"**{headers[2]}**")
    h4.markdown(f"**{headers[3]}**")
    st.markdown("---")

    for item in data:
        symbol = item["symbol"]
        name_label = item["name_label"]
        name_audio = item["name_audio"]
        sound_label = item["sound_label"]
        sound_audio = item["sound_audio"]
        word_label = item["word_label"]
        word_audio = item["word_audio"]

        c1, c2, c3, c4 = st.columns([1, 1.5, 1.5, 2.5])

        with c1:
            st.markdown(f"### {symbol}")

        with c2:
            st.write(name_label)
            play_audio(name_audio)

        with c3:
            st.write(sound_label)
            play_audio(sound_audio)

        with c4:
            st.write(word_label)
            play_audio(word_audio)

        st.markdown("---")


def render_simple_audio_list(data, title="🔊 발음 듣기"):
    st.markdown(f"### {title}")

    for label, audio_text in data:
        with st.expander(f"🔊 {label} 듣기"):
            st.write(f"**{audio_text}**")
            play_audio(audio_text)


# =========================================================
# CSS 디자인
# =========================================================
st.markdown(
    """
    <style>
    .title-box {
        background: linear-gradient(135deg, #e8f3ff, #fff4e6);
        padding: 28px;
        border-radius: 24px;
        margin-bottom: 24px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        text-align: center;
    }

    .title-box h1 {
        color: #1f3b57;
        margin-bottom: 8px;
        font-size: 34px;
    }

    .title-box p {
        color: #555;
        font-size: 18px;
        margin: 0;
    }

    .phonics-card {
        background: #ffffff;
        border-radius: 22px;
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 5px 16px rgba(0,0,0,0.07);
        border: 1px solid #eeeeee;
    }

    .phonics-card h3 {
        margin-top: 0;
        color: #1f4e79;
    }

    .phonics-card p {
        font-size: 20px;
        line-height: 1.8;
    }

    .rule-box {
        background: #fff9e8;
        border: 1.5px solid #ffe2a8;
        border-radius: 18px;
        padding: 18px;
        margin: 16px 0;
        font-size: 20px;
        line-height: 1.8;
    }

    table {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 제목
# =========================================================
st.markdown(
    """
    <div class="title-box">
        <h1>🌈 Phonics Adventure</h1>
        <p>알파벳 이름, 실제 소리, 단어 발음을 함께 들어 보며 파닉스를 배워 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)


tabs = st.tabs([
    "🌈 파닉스란?",
    "🧩 자음 소리",
    "🍎 단모음",
    "🌟 장모음",
    "🪄 Magic E",
    "🤝 Blends",
    "👯 Digraphs",
    "🌊 Vowel Teams",
    "🚗 R-Controlled",
    "🏠 Word Families"
])


# =========================================================
# Tab 1: 파닉스란?
# =========================================================
with tabs[0]:
    st.subheader("🌈 파닉스란?")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Phonics</h3>
            <p>
                <b>Phonics</b>는 영어 글자와 소리의 관계를 배우는 방법입니다.
            </p>
            <p>
                즉, 영어 단어를 볼 때 <b>글자를 소리로 바꾸어 읽는 힘</b>을 기르는 공부입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("파닉스를 배우면 처음 보는 단어도 어느 정도 읽을 수 있게 됩니다.")

    st.markdown(
        """
        ### ✅ 중요한 차이

        영어에서는 **알파벳 이름**과 **단어 안에서 나는 실제 소리**가 다릅니다.

        예를 들어,

        - 글자 **B**의 이름은 “비”처럼 들립니다.
        - 하지만 단어 안에서는 보통 **/b/**, 즉 “브”에 가까운 소리가 납니다.
        - 그래서 **bat**은 “비-에이-티”가 아니라 **/b/ + /a/ + /t/**로 읽습니다.
        """
    )

    st.markdown(
        """
        <div class="rule-box">
            <b>예시</b><br><br>
            <b>B</b> 이름: B<br>
            <b>B</b> 실제 소리: /b/<br>
            <b>bat</b>: /b/ + /a/ + /t/
        </div>
        """,
        unsafe_allow_html=True
    )

    intro_data = [
        {
            "symbol": "B",
            "name_label": "이름: B",
            "name_audio": "letter B",
            "sound_label": "소리: /b/",
            "sound_audio": "buh, buh, buh",
            "word_label": "bat, bag, boy",
            "word_audio": "bat, bag, boy",
        },
        {
            "symbol": "C",
            "name_label": "이름: C",
            "name_audio": "letter C",
            "sound_label": "소리: /k/",
            "sound_audio": "kuh, kuh, kuh",
            "word_label": "cat, cup, car",
            "word_audio": "cat, cup, car",
        },
        {
            "symbol": "M",
            "name_label": "이름: M",
            "name_audio": "letter M",
            "sound_label": "소리: /m/",
            "sound_audio": "mmm, mmm, mmm",
            "word_label": "man, milk, mom",
            "word_audio": "man, milk, mom",
        },
    ]

    st.markdown("### 🔊 알파벳 이름 / 실제 소리 / 단어 비교")
    render_sound_table(intro_data)


# =========================================================
# Tab 2: 자음 소리
# =========================================================
with tabs[1]:
    st.subheader("🧩 자음 소리")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Consonants</h3>
            <p>
                <b>자음</b>은 모음 a, e, i, o, u를 제외한 대부분의 글자입니다.
            </p>
            <p>
                자음은 단어의 처음과 끝에서 많이 쓰이며, 단어의 뼈대를 만들어 줍니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    consonant_data = [
        {"symbol": "b", "name_label": "B / 비", "name_audio": "letter B", "sound_label": "/b/ 브", "sound_audio": "buh, buh, buh", "word_label": "bat, bag, boy", "word_audio": "bat, bag, boy"},
        {"symbol": "c", "name_label": "C / 씨", "name_audio": "letter C", "sound_label": "/k/ 크", "sound_audio": "kuh, kuh, kuh", "word_label": "cat, cup, car", "word_audio": "cat, cup, car"},
        {"symbol": "d", "name_label": "D / 디", "name_audio": "letter D", "sound_label": "/d/ 드", "sound_audio": "duh, duh, duh", "word_label": "dog, desk, dad", "word_audio": "dog, desk, dad"},
        {"symbol": "f", "name_label": "F / 에프", "name_audio": "letter F", "sound_label": "/f/ 프", "sound_audio": "fff, fff, fff", "word_label": "fish, fan, fox", "word_audio": "fish, fan, fox"},
        {"symbol": "g", "name_label": "G / 지", "name_audio": "letter G", "sound_label": "/g/ 그", "sound_audio": "guh, guh, guh", "word_label": "gum, goat, game", "word_audio": "gum, goat, game"},
        {"symbol": "h", "name_label": "H / 에이치", "name_audio": "letter H", "sound_label": "/h/ 흐", "sound_audio": "huh, huh, huh", "word_label": "hat, hen, hot", "word_audio": "hat, hen, hot"},
        {"symbol": "j", "name_label": "J / 제이", "name_audio": "letter J", "sound_label": "/j/ 즈", "sound_audio": "juh, juh, juh", "word_label": "jam, jet, job", "word_audio": "jam, jet, job"},
        {"symbol": "k", "name_label": "K / 케이", "name_audio": "letter K", "sound_label": "/k/ 크", "sound_audio": "kuh, kuh, kuh", "word_label": "kid, kite, king", "word_audio": "kid, kite, king"},
        {"symbol": "l", "name_label": "L / 엘", "name_audio": "letter L", "sound_label": "/l/ 을", "sound_audio": "lll, lll, lll", "word_label": "leg, lion, log", "word_audio": "leg, lion, log"},
        {"symbol": "m", "name_label": "M / 엠", "name_audio": "letter M", "sound_label": "/m/ 음", "sound_audio": "mmm, mmm, mmm", "word_label": "man, milk, mom", "word_audio": "man, milk, mom"},
        {"symbol": "n", "name_label": "N / 엔", "name_audio": "letter N", "sound_label": "/n/ 은", "sound_audio": "nnn, nnn, nnn", "word_label": "net, nose, nine", "word_audio": "net, nose, nine"},
        {"symbol": "p", "name_label": "P / 피", "name_audio": "letter P", "sound_label": "/p/ 프", "sound_audio": "puh, puh, puh", "word_label": "pig, pen, pop", "word_audio": "pig, pen, pop"},
        {"symbol": "r", "name_label": "R / 알", "name_audio": "letter R", "sound_label": "/r/ 르", "sound_audio": "ruh, ruh, ruh", "word_label": "red, run, rain", "word_audio": "red, run, rain"},
        {"symbol": "s", "name_label": "S / 에스", "name_audio": "letter S", "sound_label": "/s/ 스", "sound_audio": "sss, sss, sss", "word_label": "sun, sit, sad", "word_audio": "sun, sit, sad"},
        {"symbol": "t", "name_label": "T / 티", "name_audio": "letter T", "sound_label": "/t/ 트", "sound_audio": "tuh, tuh, tuh", "word_label": "top, ten, tiger", "word_audio": "top, ten, tiger"},
        {"symbol": "v", "name_label": "V / 브이", "name_audio": "letter V", "sound_label": "/v/ 브", "sound_audio": "vvv, vvv, vvv", "word_label": "van, vet, vest", "word_audio": "van, vet, vest"},
        {"symbol": "w", "name_label": "W / 더블유", "name_audio": "letter W", "sound_label": "/w/ 우", "sound_audio": "wuh, wuh, wuh", "word_label": "web, win, water", "word_audio": "web, win, water"},
        {"symbol": "y", "name_label": "Y / 와이", "name_audio": "letter Y", "sound_label": "/y/ 여", "sound_audio": "yuh, yuh, yuh", "word_label": "yes, yellow, yogurt", "word_audio": "yes, yellow, yogurt"},
        {"symbol": "z", "name_label": "Z / 지", "name_audio": "letter Z", "sound_label": "/z/ 즈", "sound_audio": "zzz, zzz, zzz", "word_label": "zoo, zebra, zip", "word_audio": "zoo, zebra, zip"},
    ]

    st.markdown("### ✅ 자주 나오는 자음 소리")
    render_sound_table(consonant_data)

    st.warning("c와 g는 단어에 따라 소리가 달라질 수 있습니다. 예: cat / city, goat / giant")


# =========================================================
# Tab 3: 단모음
# =========================================================
with tabs[2]:
    st.subheader("🍎 단모음 Short Vowels")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Short Vowels</h3>
            <p>
                <b>단모음</b>은 짧게 나는 모음 소리입니다.
            </p>
            <p>
                보통 <b>자음 + 모음 + 자음</b> 구조의 짧은 단어에서 많이 나옵니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    short_vowel_data = [
        {"symbol": "a", "name_label": "A / 에이", "name_audio": "letter A", "sound_label": "short a / 애", "sound_audio": "short a, a, cat", "word_label": "cat, bag, man", "word_audio": "cat, bag, man"},
        {"symbol": "e", "name_label": "E / 이", "name_audio": "letter E", "sound_label": "short e / 에", "sound_audio": "short e, e, bed", "word_label": "bed, pen, ten", "word_audio": "bed, pen, ten"},
        {"symbol": "i", "name_label": "I / 아이", "name_audio": "letter I", "sound_label": "short i / 짧은 이", "sound_audio": "short i, i, sit", "word_label": "sit, big, fish", "word_audio": "sit, big, fish"},
        {"symbol": "o", "name_label": "O / 오우", "name_audio": "letter O", "sound_label": "short o / 아·오", "sound_audio": "short o, o, hot", "word_label": "hot, dog, box", "word_audio": "hot, dog, box"},
        {"symbol": "u", "name_label": "U / 유", "name_audio": "letter U", "sound_label": "short u / 어", "sound_audio": "short u, u, cup", "word_label": "cup, sun, bus", "word_audio": "cup, sun, bus"},
    ]

    st.markdown("### ✅ 단모음: 이름 / 실제 소리 / 예시 단어")
    render_sound_table(short_vowel_data, headers=("모음", "알파벳 이름", "단모음 소리", "예시 단어"))

    st.markdown(
        """
        <div class="rule-box">
            <b>CVC 단어</b><br>
            C = consonant 자음<br>
            V = vowel 모음<br><br>
            <b>cat</b> = c + a + t<br>
            <b>bed</b> = b + e + d<br>
            <b>sit</b> = s + i + t
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Tab 4: 장모음
# =========================================================
with tabs[3]:
    st.subheader("🌟 장모음 Long Vowels")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Long Vowels</h3>
            <p>
                <b>장모음</b>은 모음 글자의 이름과 비슷하게 나는 소리입니다.
            </p>
            <p>
                a, e, i, o, u가 자기 이름처럼 소리나는 경우입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    long_vowel_data = [
        {"symbol": "a", "name_label": "A / 에이", "name_audio": "letter A", "sound_label": "long a / 에이", "sound_audio": "long a, cake", "word_label": "cake, name, rain", "word_audio": "cake, name, rain"},
        {"symbol": "e", "name_label": "E / 이", "name_audio": "letter E", "sound_label": "long e / 이", "sound_audio": "long e, tree", "word_label": "he, we, tree", "word_audio": "he, we, tree"},
        {"symbol": "i", "name_label": "I / 아이", "name_audio": "letter I", "sound_label": "long i / 아이", "sound_audio": "long i, bike", "word_label": "bike, time, five", "word_audio": "bike, time, five"},
        {"symbol": "o", "name_label": "O / 오우", "name_audio": "letter O", "sound_label": "long o / 오우", "sound_audio": "long o, home", "word_label": "home, note, boat", "word_audio": "home, note, boat"},
        {"symbol": "u", "name_label": "U / 유", "name_audio": "letter U", "sound_label": "long u / 유·우", "sound_audio": "long u, cute", "word_label": "cute, use, blue", "word_audio": "cute, use, blue"},
    ]

    st.markdown("### ✅ 장모음: 이름 / 실제 소리 / 예시 단어")
    render_sound_table(long_vowel_data, headers=("모음", "알파벳 이름", "장모음 소리", "예시 단어"))

    st.info("장모음은 Magic E나 vowel team에서 자주 나옵니다.")


# =========================================================
# Tab 5: Magic E
# =========================================================
with tabs[4]:
    st.subheader("🪄 Magic E")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Magic E란?</h3>
            <p>
                단어 끝에 <b>e</b>가 붙으면, 앞의 모음이 <b>장모음</b>으로 바뀌는 경우가 많습니다.
            </p>
            <p>
                이때 끝의 <b>e</b>는 보통 소리내어 읽지 않습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    magic_e_data = [
        ("cap → cape", "cap, cape"),
        ("tap → tape", "tap, tape"),
        ("kit → kite", "kit, kite"),
        ("bit → bite", "bit, bite"),
        ("hop → hope", "hop, hope"),
        ("cut → cute", "cut, cute"),
    ]

    st.markdown(
        """
        | 짧은 소리 | Magic E | 변화 |
        |---|---|---|
        | cap | cape | a: 애 → 에이 |
        | tap | tape | a: 애 → 에이 |
        | kit | kite | i: 짧은 이 → 아이 |
        | bit | bite | i: 짧은 이 → 아이 |
        | hop | hope | o: 짧은 오 → 오우 |
        | cut | cute | u: 어 → 유 |
        """
    )

    st.success("예: cap은 짧게, cape는 길게 읽습니다.")

    render_simple_audio_list(magic_e_data, "🔊 Magic E 비교 듣기")


# =========================================================
# Tab 6: Consonant Blends
# =========================================================
with tabs[5]:
    st.subheader("🤝 Consonant Blends")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Consonant Blends란?</h3>
            <p>
                <b>Consonant blends</b>는 자음 두 개 또는 세 개가 함께 나오지만,
                각각의 소리가 어느 정도 살아 있는 경우입니다.
            </p>
            <p>
                예: <b>bl</b>은 /b/와 /l/ 소리가 함께 납니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    blend_data = [
        {"symbol": "bl", "name_label": "b + l", "name_audio": "b l", "sound_label": "/bl/", "sound_audio": "bl, bl, black", "word_label": "black, blue, block", "word_audio": "black, blue, block"},
        {"symbol": "br", "name_label": "b + r", "name_audio": "b r", "sound_label": "/br/", "sound_audio": "br, br, brown", "word_label": "brown, bread, brush", "word_audio": "brown, bread, brush"},
        {"symbol": "cl", "name_label": "c + l", "name_audio": "c l", "sound_label": "/cl/", "sound_audio": "cl, cl, clap", "word_label": "clap, clock, class", "word_audio": "clap, clock, class"},
        {"symbol": "cr", "name_label": "c + r", "name_audio": "c r", "sound_label": "/cr/", "sound_audio": "cr, cr, crab", "word_label": "crab, cry, cross", "word_audio": "crab, cry, cross"},
        {"symbol": "dr", "name_label": "d + r", "name_audio": "d r", "sound_label": "/dr/", "sound_audio": "dr, dr, drum", "word_label": "drum, dress, drive", "word_audio": "drum, dress, drive"},
        {"symbol": "fl", "name_label": "f + l", "name_audio": "f l", "sound_label": "/fl/", "sound_audio": "fl, fl, flag", "word_label": "flag, flower, fly", "word_audio": "flag, flower, fly"},
        {"symbol": "fr", "name_label": "f + r", "name_audio": "f r", "sound_label": "/fr/", "sound_audio": "fr, fr, frog", "word_label": "frog, friend, fruit", "word_audio": "frog, friend, fruit"},
        {"symbol": "gl", "name_label": "g + l", "name_audio": "g l", "sound_label": "/gl/", "sound_audio": "gl, gl, glass", "word_label": "glass, glad, glue", "word_audio": "glass, glad, glue"},
        {"symbol": "gr", "name_label": "g + r", "name_audio": "g r", "sound_label": "/gr/", "sound_audio": "gr, gr, green", "word_label": "green, grass, grape", "word_audio": "green, grass, grape"},
        {"symbol": "pl", "name_label": "p + l", "name_audio": "p l", "sound_label": "/pl/", "sound_audio": "pl, pl, play", "word_label": "plane, play, plant", "word_audio": "plane, play, plant"},
        {"symbol": "pr", "name_label": "p + r", "name_audio": "p r", "sound_label": "/pr/", "sound_audio": "pr, pr, print", "word_label": "print, pray, price", "word_audio": "print, pray, price"},
        {"symbol": "sk", "name_label": "s + k", "name_audio": "s k", "sound_label": "/sk/", "sound_audio": "sk, sk, sky", "word_label": "sky, skate, skip", "word_audio": "sky, skate, skip"},
        {"symbol": "sl", "name_label": "s + l", "name_audio": "s l", "sound_label": "/sl/", "sound_audio": "sl, sl, sleep", "word_label": "sleep, slide, slow", "word_audio": "sleep, slide, slow"},
        {"symbol": "sm", "name_label": "s + m", "name_audio": "s m", "sound_label": "/sm/", "sound_audio": "sm, sm, smile", "word_label": "smile, small, smell", "word_audio": "smile, small, smell"},
        {"symbol": "sn", "name_label": "s + n", "name_audio": "s n", "sound_label": "/sn/", "sound_audio": "sn, sn, snake", "word_label": "snake, snow, snack", "word_audio": "snake, snow, snack"},
        {"symbol": "sp", "name_label": "s + p", "name_audio": "s p", "sound_label": "/sp/", "sound_audio": "sp, sp, spoon", "word_label": "spoon, speak, sport", "word_audio": "spoon, speak, sport"},
        {"symbol": "st", "name_label": "s + t", "name_audio": "s t", "sound_label": "/st/", "sound_audio": "st, st, star", "word_label": "star, stop, student", "word_audio": "star, stop, student"},
        {"symbol": "sw", "name_label": "s + w", "name_audio": "s w", "sound_label": "/sw/", "sound_audio": "sw, sw, swim", "word_label": "swim, sweet, swing", "word_audio": "swim, sweet, swing"},
        {"symbol": "tr", "name_label": "t + r", "name_audio": "t r", "sound_label": "/tr/", "sound_audio": "tr, tr, tree", "word_label": "tree, train, truck", "word_audio": "tree, train, truck"},
    ]

    st.markdown("### ✅ Blend 소리 / 예시 단어")
    render_sound_table(blend_data, headers=("Blend", "글자 조합", "실제 소리", "예시 단어"))

    st.info("blend는 두 소리가 합쳐지지만 완전히 새로운 소리가 되는 것은 아닙니다.")


# =========================================================
# Tab 7: Digraphs
# =========================================================
with tabs[6]:
    st.subheader("👯 Digraphs")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Digraph란?</h3>
            <p>
                <b>Digraph</b>는 두 글자가 만나 하나의 새로운 소리를 내는 경우입니다.
            </p>
            <p>
                blend와 다르게, 각각의 소리보다 <b>새로운 하나의 소리</b>로 읽습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    digraph_data = [
        {"symbol": "sh", "name_label": "s + h", "name_audio": "s h", "sound_label": "/sh/ 쉬", "sound_audio": "sh, sh, ship", "word_label": "ship, fish, shop", "word_audio": "ship, fish, shop"},
        {"symbol": "ch", "name_label": "c + h", "name_audio": "c h", "sound_label": "/ch/ 치", "sound_audio": "ch, ch, chair", "word_label": "chair, lunch, cheese", "word_audio": "chair, lunch, cheese"},
        {"symbol": "th", "name_label": "t + h", "name_audio": "t h", "sound_label": "/th/", "sound_audio": "th, th, thin, this", "word_label": "thin, this, bath", "word_audio": "thin, this, bath"},
        {"symbol": "wh", "name_label": "w + h", "name_audio": "w h", "sound_label": "/wh/", "sound_audio": "wh, wh, what", "word_label": "what, when, white", "word_audio": "what, when, white"},
        {"symbol": "ph", "name_label": "p + h", "name_audio": "p h", "sound_label": "/f/ 프", "sound_audio": "f, f, phone", "word_label": "phone, photo, graph", "word_audio": "phone, photo, graph"},
        {"symbol": "ck", "name_label": "c + k", "name_audio": "c k", "sound_label": "/k/ 크", "sound_audio": "k, k, duck", "word_label": "duck, sock, black", "word_audio": "duck, sock, black"},
    ]

    st.markdown("### ✅ Digraph 소리 / 예시 단어")
    render_sound_table(digraph_data, headers=("Digraph", "글자 조합", "실제 소리", "예시 단어"))

    st.warning("th는 한국어에 정확히 같은 소리가 없어 학생들이 특히 어려워합니다.")


# =========================================================
# Tab 8: Vowel Teams
# =========================================================
with tabs[7]:
    st.subheader("🌊 Vowel Teams")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Vowel Teams란?</h3>
            <p>
                <b>Vowel teams</b>는 모음 두 개가 함께 나와 하나의 모음 소리를 만드는 경우입니다.
            </p>
            <p>
                영어에는 같은 소리를 여러 철자로 쓰는 경우가 많기 때문에 자주 보는 것이 중요합니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    vowel_team_data = [
        {"symbol": "ai", "name_label": "a + i", "name_audio": "a i", "sound_label": "long a / 에이", "sound_audio": "long a, rain", "word_label": "rain, train, paint", "word_audio": "rain, train, paint"},
        {"symbol": "ay", "name_label": "a + y", "name_audio": "a y", "sound_label": "long a / 에이", "sound_audio": "long a, day", "word_label": "day, play, say", "word_audio": "day, play, say"},
        {"symbol": "ee", "name_label": "e + e", "name_audio": "e e", "sound_label": "long e / 이", "sound_audio": "long e, see", "word_label": "see, tree, green", "word_audio": "see, tree, green"},
        {"symbol": "ea", "name_label": "e + a", "name_audio": "e a", "sound_label": "long e / 이", "sound_audio": "long e, eat", "word_label": "eat, meat, bread", "word_audio": "eat, meat, bread"},
        {"symbol": "oa", "name_label": "o + a", "name_audio": "o a", "sound_label": "long o / 오우", "sound_audio": "long o, boat", "word_label": "boat, coat, road", "word_audio": "boat, coat, road"},
        {"symbol": "ow", "name_label": "o + w", "name_audio": "o w", "sound_label": "오우 / 아우", "sound_audio": "ow, snow, cow", "word_label": "snow, window, cow, now", "word_audio": "snow, window, cow, now"},
        {"symbol": "oi", "name_label": "o + i", "name_audio": "o i", "sound_label": "오이", "sound_audio": "oi, coin", "word_label": "coin, oil, point", "word_audio": "coin, oil, point"},
        {"symbol": "oy", "name_label": "o + y", "name_audio": "o y", "sound_label": "오이", "sound_audio": "oy, boy", "word_label": "boy, toy, enjoy", "word_audio": "boy, toy, enjoy"},
        {"symbol": "ou", "name_label": "o + u", "name_audio": "o u", "sound_label": "아우 / 어", "sound_audio": "ou, out, touch", "word_label": "out, house, touch", "word_audio": "out, house, touch"},
        {"symbol": "oo", "name_label": "o + o", "name_audio": "o o", "sound_label": "우 / 으", "sound_audio": "oo, moon, book", "word_label": "moon, food, book, look", "word_audio": "moon, food, book, look"},
    ]

    st.markdown("### ✅ Vowel Team 소리 / 예시 단어")
    render_sound_table(vowel_team_data, headers=("Vowel Team", "글자 조합", "실제 소리", "예시 단어"))

    st.info("vowel team은 예외가 많아서 ‘규칙 + 자주 보기’가 함께 필요합니다.")


# =========================================================
# Tab 9: R-Controlled Vowels
# =========================================================
with tabs[8]:
    st.subheader("🚗 R-Controlled Vowels")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 R-Controlled Vowels란?</h3>
            <p>
                모음 뒤에 <b>r</b>이 오면, 모음 소리가 r의 영향을 받아 달라집니다.
            </p>
            <p>
                그래서 <b>ar, er, ir, or, ur</b>은 따로 연습하는 것이 좋습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    r_controlled_data = [
        {"symbol": "ar", "name_label": "a + r", "name_audio": "a r", "sound_label": "아r", "sound_audio": "ar, car", "word_label": "car, star, park", "word_audio": "car, star, park"},
        {"symbol": "er", "name_label": "e + r", "name_audio": "e r", "sound_label": "어r", "sound_audio": "er, her", "word_label": "her, teacher, sister", "word_audio": "her, teacher, sister"},
        {"symbol": "ir", "name_label": "i + r", "name_audio": "i r", "sound_label": "어r", "sound_audio": "ir, bird", "word_label": "bird, girl, shirt", "word_audio": "bird, girl, shirt"},
        {"symbol": "or", "name_label": "o + r", "name_audio": "o r", "sound_label": "오r", "sound_audio": "or, corn", "word_label": "corn, horse, sport", "word_audio": "corn, horse, sport"},
        {"symbol": "ur", "name_label": "u + r", "name_audio": "u r", "sound_label": "어r", "sound_audio": "ur, turn", "word_label": "turn, nurse, purple", "word_audio": "turn, nurse, purple"},
    ]

    st.markdown("### ✅ R-Controlled 소리 / 예시 단어")
    render_sound_table(r_controlled_data, headers=("철자", "글자 조합", "실제 소리", "예시 단어"))

    st.success("er, ir, ur은 비슷하게 나는 경우가 많습니다. her, bird, turn을 비교해 보세요.")


# =========================================================
# Tab 10: Word Families
# =========================================================
with tabs[9]:
    st.subheader("🏠 Word Families")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Word Family란?</h3>
            <p>
                <b>Word family</b>는 끝소리나 철자 패턴이 같은 단어 묶음입니다.
            </p>
            <p>
                하나의 패턴을 익히면 여러 단어를 쉽게 읽을 수 있습니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    word_family_data = [
        {"symbol": "-at", "name_label": "a + t", "name_audio": "a t", "sound_label": "at", "sound_audio": "at, at, cat", "word_label": "cat, bat, hat, mat, sat", "word_audio": "cat, bat, hat, mat, sat"},
        {"symbol": "-an", "name_label": "a + n", "name_audio": "a n", "sound_label": "an", "sound_audio": "an, an, can", "word_label": "can, man, fan, pan, ran", "word_audio": "can, man, fan, pan, ran"},
        {"symbol": "-ap", "name_label": "a + p", "name_audio": "a p", "sound_label": "ap", "sound_audio": "ap, ap, cap", "word_label": "cap, map, tap, nap, gap", "word_audio": "cap, map, tap, nap, gap"},
        {"symbol": "-en", "name_label": "e + n", "name_audio": "e n", "sound_label": "en", "sound_audio": "en, en, pen", "word_label": "pen, hen, ten, men", "word_audio": "pen, hen, ten, men"},
        {"symbol": "-et", "name_label": "e + t", "name_audio": "e t", "sound_label": "et", "sound_audio": "et, et, pet", "word_label": "net, wet, pet, set", "word_audio": "net, wet, pet, set"},
        {"symbol": "-ig", "name_label": "i + g", "name_audio": "i g", "sound_label": "ig", "sound_audio": "ig, ig, pig", "word_label": "big, pig, dig, wig", "word_audio": "big, pig, dig, wig"},
        {"symbol": "-it", "name_label": "i + t", "name_audio": "i t", "sound_label": "it", "sound_audio": "it, it, sit", "word_label": "sit, hit, fit, bit", "word_audio": "sit, hit, fit, bit"},
        {"symbol": "-og", "name_label": "o + g", "name_audio": "o g", "sound_label": "og", "sound_audio": "og, og, dog", "word_label": "dog, log, fog, hog", "word_audio": "dog, log, fog, hog"},
        {"symbol": "-op", "name_label": "o + p", "name_audio": "o p", "sound_label": "op", "sound_audio": "op, op, hop", "word_label": "hop, top, pop, mop", "word_audio": "hop, top, pop, mop"},
        {"symbol": "-ug", "name_label": "u + g", "name_audio": "u g", "sound_label": "ug", "sound_audio": "ug, ug, bug", "word_label": "bug, rug, mug, hug", "word_audio": "bug, rug, mug, hug"},
    ]

    st.markdown("### ✅ Word Family 소리 / 예시 단어")
    render_sound_table(word_family_data, headers=("패턴", "글자 조합", "패턴 소리", "예시 단어"))

    st.markdown(
        """
        <div class="rule-box">
            <b>연습 방법</b><br><br>
            1. 먼저 공통 패턴을 읽습니다. 예: <b>-at</b><br>
            2. 앞에 자음을 붙여 읽습니다. c + at = <b>cat</b><br>
            3. 같은 패턴의 단어를 여러 개 읽습니다. cat, bat, hat, mat
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("word family는 읽기 부진 학생들에게 특히 효과적인 기초 읽기 연습이 될 수 있습니다.")
