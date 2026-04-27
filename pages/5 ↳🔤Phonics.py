import streamlit as st

st.set_page_config(page_title="Phonics Guide", layout="centered")

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

    .sound-box {
        background: linear-gradient(135deg, #f3f8ff, #ffffff);
        border-left: 7px solid #8bbcff;
        padding: 18px 20px;
        border-radius: 16px;
        margin: 14px 0;
        font-size: 20px;
        line-height: 1.8;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }

    .word-chip {
        display: inline-block;
        background-color: #eef5ff;
        border: 1px solid #cfe2ff;
        border-radius: 999px;
        padding: 8px 14px;
        margin: 5px;
        font-size: 18px;
        font-weight: 700;
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
        <h1>🔤 Phonics Guide</h1>
        <p>영어 단어를 읽기 위한 소리 규칙을 기초부터 배워 봅시다.</p>
    </div>
    """,
    unsafe_allow_html=True
)

tabs = st.tabs([
    "🔤 파닉스란?",
    "🔊 자음 소리",
    "🍎 단모음",
    "🌟 장모음",
    "✨ Magic E",
    "🤝 Consonant Blends",
    "👯 Digraphs",
    "🌈 Vowel Teams",
    "🚗 R-Controlled",
    "🏠 Word Families"
])


# =========================================================
# Tab 1: 파닉스란?
# =========================================================
with tabs[0]:
    st.subheader("🔤 파닉스란?")

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
        ### ✅ 파닉스 학습 순서

        1. 알파벳 글자와 기본 소리 알기  
        2. 자음과 모음 소리 구분하기  
        3. 짧은 단어 읽기  
        4. Magic E, blends, digraphs 같은 규칙 익히기  
        5. 긴 단어와 문장 읽기로 확장하기
        """
    )

    st.markdown(
        """
        <div class="rule-box">
            <b>중요!</b><br>
            영어는 글자 이름과 실제 소리가 다를 수 있습니다.<br><br>
            예: <b>B</b>의 이름은 “비”이지만, 단어 안에서는 보통 <b>/b/</b> 소리가 납니다.<br>
            <b>bat</b> = /b/ + /a/ + /t/
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Tab 2: 자음 소리
# =========================================================
with tabs[1]:
    st.subheader("🔊 자음 소리")

    st.markdown(
        """
        <div class="phonics-card">
            <h3>📌 Consonants</h3>
            <p>
                <b>자음</b>은 모음 a, e, i, o, u를 제외한 대부분의 글자입니다.
            </p>
            <p>
                단어의 처음과 끝에서 많이 쓰이며, 단어의 뼈대를 만들어 줍니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ✅ 자주 나오는 자음 소리")

    st.markdown(
        """
        | 글자 | 소리 느낌 | 예시 |
        |---|---|---|
        | b | /b/ | bat, bag, boy |
        | c | /k/ | cat, cup, car |
        | d | /d/ | dog, desk, dad |
        | f | /f/ | fish, fan, fox |
        | g | /g/ | gum, goat, game |
        | h | /h/ | hat, hen, hot |
        | j | /j/ | jam, jet, job |
        | k | /k/ | kid, kite, king |
        | l | /l/ | leg, lion, log |
        | m | /m/ | man, milk, mom |
        | n | /n/ | net, nose, nine |
        | p | /p/ | pig, pen, pop |
        | r | /r/ | red, run, rain |
        | s | /s/ | sun, sit, sad |
        | t | /t/ | top, ten, tiger |
        | v | /v/ | van, vet, vest |
        | w | /w/ | web, win, water |
        | y | /y/ | yes, yellow, yogurt |
        | z | /z/ | zoo, zebra, zip |
        """
    )

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

    st.markdown(
        """
        | 모음 | 소리 느낌 | 예시 |
        |---|---|---|
        | a | 애 | cat, bag, man |
        | e | 에 | bed, pen, ten |
        | i | 이와 에 사이 짧은 소리 | sit, big, fish |
        | o | 아/오 사이 짧은 소리 | hot, dog, box |
        | u | 어 | cup, sun, bus |
        """
    )

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

    st.markdown(
        """
        | 모음 | 장모음 소리 | 예시 |
        |---|---|---|
        | a | 에이 | cake, name, rain |
        | e | 이 | he, we, tree |
        | i | 아이 | bike, time, five |
        | o | 오우 | home, note, boat |
        | u | 유 / 우 | cute, use, blue |
        """
    )

    st.info("장모음은 Magic E나 vowel team에서 자주 나옵니다.")


# =========================================================
# Tab 5: Magic E
# =========================================================
with tabs[4]:
    st.subheader("✨ Magic E")

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

    st.markdown(
        """
        <div class="rule-box">
            <b>규칙</b><br>
            자음 + 모음 + 자음 + e<br><br>
            앞의 모음은 길게 읽고, 마지막 e는 조용합니다.
        </div>
        """,
        unsafe_allow_html=True
    )

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

    st.success("예: cap은 ‘캡’처럼 짧게, cape는 ‘케이프’처럼 길게 읽습니다.")


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

    st.markdown("### ✅ Beginning Blends")

    st.markdown(
        """
        | Blend | 예시 |
        |---|---|
        | bl | black, blue, block |
        | br | brown, bread, brush |
        | cl | clap, clock, class |
        | cr | crab, cry, cross |
        | dr | drum, dress, drive |
        | fl | flag, flower, fly |
        | fr | frog, friend, fruit |
        | gl | glass, glad, glue |
        | gr | green, grass, grape |
        | pl | plane, play, plant |
        | pr | print, pray, price |
        | sk | sky, skate, skip |
        | sl | sleep, slide, slow |
        | sm | smile, small, smell |
        | sn | snake, snow, snack |
        | sp | spoon, speak, sport |
        | st | star, stop, student |
        | sw | swim, sweet, swing |
        | tr | tree, train, truck |
        """
    )

    st.markdown("### ✅ Ending Blends")

    st.markdown(
        """
        | Blend | 예시 |
        |---|---|
        | -nd | hand, sand, wind |
        | -nt | tent, went, plant |
        | -mp | lamp, jump, camp |
        | -st | fast, best, last |
        | -sk | desk, mask, task |
        | -ft | left, gift, soft |
        | -lk | milk, walk, talk |
        """
    )

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

    st.markdown(
        """
        | Digraph | 소리 | 예시 |
        |---|---|---|
        | sh | 쉬 | ship, fish, shop |
        | ch | 치 | chair, lunch, cheese |
        | th | ㅆ/ㄷ 사이 소리 | thin, this, bath |
        | wh | 우/ㅎw | what, when, white |
        | ph | f 소리 | phone, photo, graph |
        | ck | k 소리 | duck, sock, black |
        """
    )

    st.warning("th는 한국어에 정확히 같은 소리가 없어 학생들이 특히 어려워합니다.")


# =========================================================
# Tab 8: Vowel Teams
# =========================================================
with tabs[7]:
    st.subheader("🌈 Vowel Teams")

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

    st.markdown(
        """
        | Vowel Team | 소리 느낌 | 예시 |
        |---|---|---|
        | ai | 에이 | rain, train, paint |
        | ay | 에이 | day, play, say |
        | ee | 이 | see, tree, green |
        | ea | 이 / 에 | eat, meat, bread |
        | oa | 오우 | boat, coat, road |
        | ow | 오우 / 아우 | snow, window / cow, now |
        | oi | 오이 | coin, oil, point |
        | oy | 오이 | boy, toy, enjoy |
        | ou | 아우 / 어 | out, house / touch |
        | oo | 우 / 으 | moon, food / book, look |
        """
    )

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

    st.markdown(
        """
        | 철자 | 소리 느낌 | 예시 |
        |---|---|---|
        | ar | 아r | car, star, park |
        | er | 어r | her, teacher, sister |
        | ir | 어r | bird, girl, shirt |
        | or | 오r | corn, horse, sport |
        | ur | 어r | turn, nurse, purple |
        """
    )

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

    st.markdown("### ✅ 자주 나오는 Word Families")

    st.markdown(
        """
        | 패턴 | 단어 |
        |---|---|
        | -at | cat, bat, hat, mat, sat |
        | -an | can, man, fan, pan, ran |
        | -ap | cap, map, tap, nap, gap |
        | -en | pen, hen, ten, men |
        | -et | net, wet, pet, set |
        | -ig | big, pig, dig, wig |
        | -it | sit, hit, fit, bit |
        | -og | dog, log, fog, hog |
        | -op | hop, top, pop, mop |
        | -ug | bug, rug, mug, hug |
        """
    )

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
