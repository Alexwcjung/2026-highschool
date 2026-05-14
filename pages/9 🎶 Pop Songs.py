import streamlit as st
import random
import string

# =========================
# 1. 기본 설정 및 디자인
# =========================
st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #1e293b; }

    .main-title {
        background-color: #f8fafc;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #6366f1;
        text-align: center;
        color: #4338ca;
        margin-bottom: 25px;
    }

    .info-box {
        background-color: #f1f5f9;
        padding: 24px;
        border-radius: 15px;
        border: 1px solid #cbd5e1;
        line-height: 1.8;
        margin-bottom: 25px;
    }

    .info-box h3 {
        color: #4338ca;
        border-bottom: 3px solid #6366f1;
        padding-bottom: 12px;
        margin-top: 0;
    }

    .lyrics-container {
        padding: 12px 20px;
        border-left: 5px solid #6366f1;
        margin-bottom: 10px;
        background-color: #f8fafc;
        border-radius: 0 10px 10px 0;
    }

    .eng-line {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e3a8a;
    }

    .kor-sub {
        font-size: 0.9rem;
        color: #64748b;
        margin-top: 4px;
    }

    .quiz-box {
        background-color: #f0f9ff;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #bae6fd;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #86efac;
        margin-top: 18px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# 2. 세션 상태 관리
# =========================
if "selected_song" not in st.session_state:
    st.session_state.selected_song = "1. Let It Go - Frozen OST"

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False


# =========================
# 3. 상단 제목 및 컨트롤
# =========================
st.markdown(
    '<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>',
    unsafe_allow_html=True
)

song_options = [
    "1. Let It Go - Frozen OST",
    "2. Hello - Adele",
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones",
    "6. Fix you - Cold Play",
]

def sync_song():
    st.session_state.quiz_submitted = False

song_choice = st.selectbox(
    "👉 학습할 노래를 선택하세요",
    song_options,
    index=song_options.index(st.session_state.selected_song),
    on_change=sync_song,
    key="song_selector"
)

st.session_state.selected_song = song_choice

# 순서 배열 삭제함
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈"]

selected_tab = st.radio(
    "학습 단계",
    tabs_list,
    horizontal=True,
    key="current_tab"
)


# =========================
# 4. 곡별 데이터 설정
# =========================

if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=RgGRyssdJvw&list=RDRgGRyssdJvw&start_radio=1"

    bg_content = '''
    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#be185d;">
        ❄️ Let It Go: 숨겨 왔던 자신을 받아들이는 순간
    </h3>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        <b>Let It Go</b>는 영화 <i>Frozen</i>의 대표곡으로,
        엘사가 더 이상 자신의 능력과 감정을 숨기지 않고
        스스로를 받아들이는 장면에서 나오는 노래입니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        엘사는 어릴 때부터 자신의 얼음 마법이 다른 사람을 다치게 할 수 있다는
        두려움 속에서 살아왔습니다. 그래서 감정을 숨기고,
        능력을 감추며, 언제나 조심해야 했습니다.
        하지만 대관식 날 엘사의 능력이 사람들 앞에서 드러나고,
        사람들은 엘사를 두려워합니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        엘사는 모든 것을 피해 눈 덮인 산으로 도망치고,
        그곳에서 처음으로 자신의 진짜 모습을 마주합니다.
        이 노래는 단순히 “다 잊어버리자”는 의미가 아니라,
        그동안 억눌렀던 두려움, 책임감, 타인의 시선에서 벗어나
        자기 자신을 받아들이는 과정을 보여줍니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        수업에서는 <b>let it go</b>, <b>conceal</b>, <b>hold back</b>,
        <b>storm inside</b>, <b>I'm free</b>, <b>the past is in the past</b>
        같은 표현을 중심으로 배울 수 있습니다.
        특히 이 노래는 자유, 두려움, 자기표현, 자신감에 대해
        함께 생각해 볼 수 있는 좋은 자료입니다.
    </p>
    '''

    lyrics_full = [
        (
            "The snow glows white on the mountain tonight / Not a footprint to be seen",
            "오늘 밤 산 위에는 눈이 하얗게 빛나고 / 발자국 하나 보이지 않아요"
        ),
        (
            "A kingdom of isolation / And it looks like I'm the queen",
            "고립된 왕국 / 그리고 내가 그곳의 여왕인 것 같아요"
        ),
        (
            "The wind is howling like this swirling storm inside / Couldn't keep it in, heaven knows I tried",
            "바람은 내 안에서 휘몰아치는 폭풍처럼 울부짖고 / 더는 감출 수 없었어요, 하늘은 내가 얼마나 노력했는지 알 거예요"
        ),
        (
            "Don't let them in, don't let them see / Be the good girl you always have to be",
            "그들을 들이지 마, 보여주지 마 / 언제나 그래야만 했던 착한 소녀가 되어라"
        ),
        (
            "Conceal, don't feel, don't let them know / Well, now they know",
            "숨기고, 느끼지 말고, 그들이 알게 하지 마 / 하지만 이제 그들이 알아버렸어요"
        ),
        (
            "Let it go, let it go / Can't hold it back anymore",
            "놓아버려, 놓아버려 / 더 이상 붙잡아 둘 수 없어"
        ),
        (
            "Let it go, let it go / Turn away and slam the door",
            "놓아버려, 놓아버려 / 돌아서서 문을 세게 닫아버려"
        ),
        (
            "I don't care what they're going to say / Let the storm rage on",
            "사람들이 뭐라고 하든 상관없어 / 폭풍이 계속 몰아치게 둬"
        ),
        (
            "The cold never bothered me anyway",
            "어차피 추위는 나를 괴롭힌 적이 없으니까"
        ),
        (
            "It's funny how some distance makes everything seem small / And the fears that once controlled me can't get to me at all",
            "거리를 두고 보니 모든 것이 작아 보이는 게 참 이상해 / 한때 나를 지배했던 두려움도 이제는 나에게 닿지 못해"
        ),
        (
            "It's time to see what I can do / To test the limits and break through",
            "이제 내가 무엇을 할 수 있는지 볼 시간이야 / 한계를 시험하고 그것을 깨고 나아갈 시간이야"
        ),
        (
            "No right, no wrong, no rules for me / I'm free",
            "옳고 그름도, 나를 묶는 규칙도 없어 / 나는 자유로워"
        ),
        (
            "Let it go, let it go / I am one with the wind and sky",
            "놓아버려, 놓아버려 / 나는 바람과 하늘과 하나가 되었어"
        ),
        (
            "Let it go, let it go / You'll never see me cry",
            "놓아버려, 놓아버려 / 너희는 다시는 내가 우는 모습을 보지 못할 거야"
        ),
        (
            "Here I stand and here I stay / Let the storm rage on",
            "나는 여기 서 있고, 여기 머물 거야 / 폭풍이 계속 몰아치게 둬"
        ),
        (
            "My power flurries through the air into the ground / My soul is spiraling in frozen fractals all around",
            "내 힘은 공기를 지나 땅속으로 흩날려 퍼지고 / 내 영혼은 사방의 얼어붙은 결정 속에서 소용돌이쳐"
        ),
        (
            "And one thought crystallizes like an icy blast / I'm never going back, the past is in the past",
            "그리고 하나의 생각이 얼음바람처럼 선명하게 굳어져 / 나는 절대 돌아가지 않아, 과거는 과거일 뿐이야"
        ),
        (
            "Let it go, let it go / And I'll rise like the break of dawn",
            "놓아버려, 놓아버려 / 나는 새벽이 밝아오듯 다시 일어설 거야"
        ),
        (
            "Let it go, let it go / That perfect girl is gone",
            "놓아버려, 놓아버려 / 그 완벽한 소녀는 이제 없어"
        ),
        (
            "Here I stand in the light of day / Let the storm rage on",
            "나는 밝은 낮의 빛 속에 서 있어 / 폭풍이 계속 몰아치게 둬"
        ),
        (
            "The cold never bothered me anyway",
            "어차피 추위는 나를 괴롭힌 적이 없으니까"
        ),
    ]

    comprehension_questions = [
        {
            "q": "1. 이 노래를 부르는 인물은 누구인가요?",
            "options": [
                "Anna",
                "Olaf",
                "Kristoff",
                "Elsa",              
            ],
            "answer": "Elsa"
        },
        {
            "q": "2. 엘사는 어디에서 이 노래를 부르나요?",
            "options": [
                "교실",
                "바닷가",
                "눈 덮인 산",               
                "도시 거리"
            ],
            "answer": "눈 덮인 산"
        },
        {
            "q": "3. 엘사가 더 이상 하지 않으려는 것은 무엇인가요?",
            "options": [
                "음식을 먹는 것",
                "학교에 가는 것",
                "동물과 이야기하는 것",
                "자신을 숨기는 것",                
            ],
            "answer": "자신을 숨기는 것"
        },
        {
            "q": "4. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "배고픔",
                "지루함",
                "자유와 해방감",             
                "질투"
            ],
            "answer": "자유와 해방감"
        },
        {
            "q": "5. 'conceal'의 뜻으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "숨기다",
                "달리다",
                "노래하다",
                "웃다"
            ],
            "answer": "숨기다"
        },
        {
            "q": "6. 'Can't hold it back anymore'는 어떤 의미에 가깝나요?",
            "options": [
                "더 이상 문을 열 수 없다",
                "더 이상 노래할 수 없다",
                "더 이상 걸을 수 없다",
                "더 이상 억누를 수 없다",                
            ],
            "answer": "더 이상 억누를 수 없다"
        },
        {
            "q": "7. 'I'm free'에서 엘사가 느끼는 감정은 무엇인가요?",
            "options": [
                "두려움",
                "부끄러움",
                "자유로움",
                "배고픔"
            ],
            "answer": "자유로움"
        },
        {
            "q": "8. 'the past is in the past'는 어떤 의미인가요?",
            "options": [
                "과거로 돌아가고 싶다",
                "과거는 과거일 뿐이다",               
                "과거가 가장 중요하다",
                "과거를 다시 만들 수 있다"
            ],
            "answer": "과거는 과거일 뿐이다"
        },
    ]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=IND0m6m4H4Q&list=RDIND0m6m4H4Q&start_radio=1"

    bg_content = '''
    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#4338ca;">
        ☎️ Hello: 과거의 누군가에게 건네는 늦은 안부
    </h3>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        Adele의 <b>Hello</b>는 시간이 많이 흐른 뒤, 과거의 누군가에게 다시 연락하고 싶은 마음을 담은 노래입니다.
        노래 속 화자는 상대에게 전화를 걸며 오래전의 관계, 미안함, 후회,
        그리고 아직 완전히 치유되지 않은 감정을 떠올립니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        이 노래에서 화자는 단순히 “안녕”이라고 말하는 것이 아니라,
        과거에 하지 못했던 사과를 전하고 싶어 합니다.
        하지만 두 사람 사이에는 시간의 거리, 마음의 거리, 그리고 실제 거리까지 생겨 있습니다.
        그래서 반복되는 <b>Hello</b>라는 말은 인사이면서 동시에 조심스러운 사과의 시작처럼 들립니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        수업에서는 <b>I'm sorry</b>, <b>I tried</b>, <b>after all these years</b>,
        <b>used to be</b>, <b>the other side</b> 같은 표현을 중심으로 배울 수 있습니다.
        특히 이 노래는 속도가 비교적 느리고 감정이 분명하게 드러나기 때문에,
        학생들이 가사를 읽으며 화자의 감정과 영어 표현을 함께 이해하기에 좋습니다.
    </p>
    '''

    lyrics_full = [
        (
            "Hello, it's me / I was wondering if after all these years you'd like to meet, to go over everything",
            "안녕, 나야 / 이 모든 세월이 흐른 뒤에 네가 만나서 모든 일을 다시 이야기해 보고 싶어 할지 궁금했어"
        ),
        (
            "They say that time's supposed to heal ya / But I ain't done much healing",
            "사람들은 시간이 너를 치유해 줄 거라고 말하지만 / 나는 별로 치유되지 않은 것 같아"
        ),
        (
            "Hello, can you hear me? / I'm in California dreaming about who we used to be",
            "여보세요, 내 말 들리니? / 나는 캘리포니아에서 예전의 우리 모습을 떠올리고 있어"
        ),
        (
            "When we were younger and free / I've forgotten how it felt before the world fell at our feet",
            "우리가 더 어리고 자유로웠을 때 / 세상이 우리 발아래 있는 것 같았던 그 느낌을 나는 잊어버렸어"
        ),
        (
            "There's such a difference between us / And a million miles",
            "우리 사이에는 너무 큰 차이가 있어 / 그리고 백만 마일만큼의 거리도 있어"
        ),
        (
            "Hello from the other side / I must've called a thousand times to tell you",
            "저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야"
        ),
        (
            "I'm sorry, for everything that I've done / But when I call you never seem to be home",
            "내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아"
        ),
        (
            "Hello from the outside / At least I can say that I've tried to tell you",
            "바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어"
        ),
        (
            "I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
            "네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아"
        ),
        (
            "Hello, how are you? / It's so typical of me to talk about myself",
            "안녕, 어떻게 지내? / 내 이야기만 하는 건 정말 나다운 일이야"
        ),
        (
            "I'm sorry, I hope that you're well / Did you ever make it out of that town where nothing ever happened?",
            "미안해, 네가 잘 지내길 바라 / 아무 일도 일어나지 않던 그 마을에서 벗어났니?"
        ),
        (
            "It's no secret that the both of us are running out of time",
            "우리 둘 다 시간이 얼마 남지 않았다는 건 비밀도 아니야"
        ),
        (
            "Hello from the other side / I must've called a thousand times to tell you",
            "저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야"
        ),
        (
            "I'm sorry, for everything that I've done / But when I call you never seem to be home",
            "내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아"
        ),
        (
            "Hello from the outside / At least I can say that I've tried to tell you",
            "바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어"
        ),
        (
            "I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
            "네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아"
        ),
        (
            "Ooooohh, anymore / Ooooohh, anymore / Ooooohh, anymore / Anymore",
            "오, 더 이상 / 오, 더 이상 / 오, 더 이상 / 더 이상"
        ),
        (
            "Hello from the other side / I must've called a thousand times to tell you",
            "저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야"
        ),
        (
            "I'm sorry, for everything that I've done / But when I call you never seem to be home",
            "내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아"
        ),
        (
            "Hello from the outside / At least I can say that I've tried to tell you",
            "바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어"
        ),
        (
            "I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
            "네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아"
        ),
    ]

    comprehension_questions = [
        {
            "q": "1. 이 노래에서 화자는 누구에게 연락하려고 하나요?",
            "options": [
                "새로 만난 선생님",
                "유명한 가수",
                "캘리포니아의 낯선 사람"
                "과거에 알던 사람",                
            ],
            "answer": "과거에 알던 사람"
        },
        {
            "q": "2. 화자가 상대에게 가장 말하고 싶어 하는 것은 무엇인가요?",
            "options": [
                "고맙다는 말",
                "미안하다는 말",
                "생일 축하한다는 말",
                "여행을 가자는 말"
            ],
            "answer": "미안하다는 말"
        },
        {
            "q": "3. 노래에서 사람들은 시간이 무엇을 해 준다고 말하나요?",
            "options": [
                "사람을 부자로 만들어 준다",
                "과거를 완전히 바꿔 준다",
                "상처를 치유해 준다",
                "슬픔을 바로 없애 준다"
            ],
            "answer": "상처를 치유해 준다"
        },
        {
            "q": "4. 화자는 어디에서 예전의 자신들을 떠올리고 있나요?",
            "options": [
                "런던",
                "캘리포니아",
                "뉴욕",
                "파리"
            ],
            "answer": "캘리포니아"
        },
        {
            "q": "5. 'I must've called a thousand times'는 어떤 의미에 가깝나요?",
            "options": [
                "정확히 천 번만 전화했다",
                "한 번도 전화하지 않았다",
                "전화번호를 잊어버렸다"
                "정말 여러 번 연락하려고 했다",
            ],
            "answer": "정말 여러 번 연락하려고 했다"
        },
        {
            "q": "6. 'Hello from the other side'에서 'the other side'는 무엇을 상징한다고 볼 수 있나요?",
            "options": [
                "학교의 반대편 교실",
                "가수가 사는 집",
                "멀어진 시간과 마음의 거리",
                "무대의 왼쪽"
            ],
            "answer": "멀어진 시간과 마음의 거리"
        },
        {
            "q": "7. 화자가 'I tried'라고 말하는 이유는 무엇인가요?",
            "options": [
                "노래 대회에 나가려고 했기 때문에",
                "캘리포니아로 여행을 가고 싶었기 때문에",
                "새로운 친구를 만들고 싶었기 때문에"
                "상대에게 사과하려고 노력했기 때문에",
            ],
            "answer": "상대에게 사과하려고 노력했기 때문에"
        },
        {
            "q": "8. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "여행의 설렘",
                "후회와 사과",
                "복수심과 분노",
                "시험에 대한 걱정"
            ],
            "answer": "후회와 사과"
        },
    ]

elif "3. A Whole New World" in song_choice:
    video_url = "https://www.youtube.com/watch?v=9FJssSUxI88&list=RD9FJssSUxI88&start_radio=1"

    bg_content = '''
    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#4338ca;">
        🕌 A Whole New World: 새로운 세상을 바라보는 순간
    </h3>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        <b>A Whole New World</b>는 영화 <i>Aladdin</i>의 대표곡으로,
        알라딘과 자스민이 마법 양탄자를 타고 밤하늘을 날며
        새로운 세상을 바라보는 장면에서 나오는 노래입니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        자스민은 궁전 안에서 공주로 살아가지만,
        정해진 규칙과 역할 속에서 자유롭게 세상을 경험하지 못합니다.
        알라딘은 그런 자스민에게 궁전 밖의 넓은 세상을 보여 주고,
        자스민은 처음으로 자신이 알지 못했던 새로운 풍경과 가능성을 마주하게 됩니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        이 노래에서 <b>a whole new world</b>는 단순히 새로운 장소만을 뜻하지 않습니다.
        새로운 시선, 새로운 경험, 그리고 스스로 선택할 수 있는 자유를 의미합니다.
        두 사람은 마법 양탄자를 타고 하늘을 날며,
        두려움보다 설렘이 더 큰 새로운 세계로 함께 나아갑니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        수업에서는 <b>I can show you the world</b>, <b>open your eyes</b>,
        <b>point of view</b>, <b>crystal clear</b>, <b>new horizons</b>
        같은 표현을 중심으로 배울 수 있습니다.
        특히 이 노래는 속도가 비교적 부드럽고 장면이 분명해서,
        학생들이 영어 표현과 함께 설렘, 자유, 새로운 경험의 감정을 이해하기에 좋습니다.
    </p>
    '''

    lyrics_full = [
        (
            "I can show you the world / Shining, shimmering, splendid",
            "내가 너에게 세상을 보여 줄 수 있어 / 빛나고, 반짝이고, 눈부신 세상을"
        ),
        (
            "Tell me, princess, now when did / You last let your heart decide?",
            "말해 봐요, 공주님, 언제였나요 / 마지막으로 마음이 원하는 대로 선택했던 때가?"
        ),
        (
            "I can open your eyes / Take you wonder by wonder",
            "내가 너의 눈을 뜨게 해 줄 수 있어 / 놀라움에서 또 다른 놀라움으로 데려가며"
        ),
        (
            "Over, sideways and under / On a magic carpet ride",
            "위로, 옆으로, 아래로 날아가며 / 마법 양탄자를 타고"
        ),
        (
            "A whole new world / A new fantastic point of view",
            "완전히 새로운 세상 / 새롭고 환상적인 시선"
        ),
        (
            "No one to tell us no / Or where to go",
            "아무도 우리에게 안 된다고 말하지 않고 / 어디로 가라고 하지도 않아"
        ),
        (
            "Or say we're only dreaming",
            "우리가 그저 꿈꾸고 있을 뿐이라고 말하지도 않아"
        ),
        (
            "A whole new world / A dazzling place I never knew",
            "완전히 새로운 세상 / 내가 전에는 알지 못했던 눈부신 곳"
        ),
        (
            "But when I'm way up here, it's crystal clear / That now I'm in a whole new world with you",
            "하지만 이렇게 높은 곳에 올라오니 모든 것이 분명해 / 지금 나는 너와 함께 완전히 새로운 세상에 있어"
        ),
        (
            "(Now I'm in a whole new world with you)",
            "이제 나는 너와 함께 완전히 새로운 세상에 있어"
        ),
        (
            "Unbelievable sights / Indescribable feeling",
            "믿기 어려운 풍경들 / 말로 표현할 수 없는 감정"
        ),
        (
            "Soaring, tumbling, freewheeling / Through an endless diamond sky",
            "솟아오르고, 구르고, 자유롭게 날아가며 / 끝없이 펼쳐진 다이아몬드 같은 하늘을 지나"
        ),
        (
            "A whole new world / Don't you dare close your eyes",
            "완전히 새로운 세상 / 절대 눈 감지 마"
        ),
        (
            "A hundred thousand things to see / Hold your breath, it gets better",
            "볼 것이 셀 수 없이 많아 / 숨을 참고 봐, 더 좋아질 거야"
        ),
        (
            "I'm like a shooting star, I've come so far / I can't go back to where I used to be",
            "나는 별똥별 같아, 정말 멀리까지 왔어 / 예전의 내가 있던 곳으로 돌아갈 수 없어"
        ),
        (
            "A whole new world / Every turn a surprise",
            "완전히 새로운 세상 / 방향을 틀 때마다 놀라움이 있어"
        ),
        (
            "With new horizons to pursue / Every moment, red-letter",
            "따라갈 새로운 지평선들이 있고 / 모든 순간이 특별해"
        ),
        (
            "I'll chase them anywhere, there's time to spare / Let me share this whole new world with you",
            "나는 어디든 그것들을 따라갈 거야, 시간은 충분해 / 이 완전히 새로운 세상을 너와 함께 나누게 해 줘"
        ),
        (
            "A whole new world / A whole new world",
            "완전히 새로운 세상 / 완전히 새로운 세상"
        ),
        (
            "That's where we'll be / That's where we'll be",
            "그곳이 우리가 있을 곳이야 / 그곳이 우리가 있을 곳이야"
        ),
        (
            "A thrilling chase / A wondrous place",
            "짜릿한 모험 / 놀라운 곳"
        ),
        (
            "For you and me",
            "너와 나를 위한"
        ),
    ]

    comprehension_questions = [
        {
            "q": "1. 이 노래에서 두 사람은 무엇을 타고 있나요?",
            "options": [
                "기차",
                "자전거",
                "배"
                "마법 양탄자",
            ],
            "answer": "마법 양탄자"
        },
        {
            "q": "2. 이 노래에서 알라딘은 자스민에게 무엇을 보여 주고 싶어 하나요?",
            "options": [
                "학교 교실",
                "시험 문제",
                "새로운 세상",
                "휴대전화"
            ],
            "answer": "새로운 세상"
        },
        {
            "q": "3. 'A whole new world'가 상징하는 것으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "낡은 방",
                "어려운 시험",
                "혼자 있는 시간"
                "새로운 시선과 경험",
            ],
            "answer": "새로운 시선과 경험"
        },
        {
            "q": "4. 'I can open your eyes'는 어떤 의미에 가깝나요?",
            "options": [
                "잠에서 깨우다",
                "눈을 감게 하다",
                "새로운 것을 보게 해 주다",
                "멀리 보내다"
            ],
            "answer": "새로운 것을 보게 해 주다"
        },
        {
            "q": "5. 'point of view'의 뜻으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "문",
                "속도",
                "약속"
                "관점",
            ],
            "answer": "관점"
        },
        {
            "q": "6. 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "후회와 슬픔",
                "분노와 복수",
                "설렘과 자유로움",
                "지루함"
            ],
            "answer": "설렘과 자유로움"
        },
        {
            "q": "7. 'I can't go back to where I used to be'는 어떤 의미인가요?",
            "options": [
                "집에 갈 길을 잃었다",
                "예전의 모습으로 돌아갈 수 없다",
                "학교에 다시 가야 한다",
                "여행을 취소했다"
            ],
            "answer": "예전의 모습으로 돌아갈 수 없다"
        },
        {
            "q": "8. 이 노래의 주요 배경으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "교실에서 보는 시험",
                "바닷가에서 하는 운동",
                "시장 안의 장면"
                "밤하늘을 나는 마법 양탄자 여행",
            ],
            "answer": "밤하늘을 나는 마법 양탄자 여행"
        },
    ]

elif "4. Stand By Me" in song_choice:
    video_url = "https://www.youtube.com/watch?v=c5hDjpi_HM0&list=RDc5hDjpi_HM0&start_radio=1"

    bg_content = '''
    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#15803d;">
        🤝 Stand By Me: 곁에 있어 주는 힘
    </h3>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        <b>Stand By Me</b>는 어둡고 불안한 순간에도
        누군가가 내 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다.
        제목의 <b>stand by me</b>는 단순히 “내 옆에 서 있어”라는 뜻을 넘어,
        “내 곁에 있어 줘”, “나를 지켜 줘”, “함께해 줘”라는 의미로 이해할 수 있습니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        노래 속 화자는 밤이 찾아오고 세상이 어두워지는 장면을 떠올립니다.
        하지만 그는 혼자가 아니라는 믿음 때문에 두려워하지 않습니다.
        달빛만 보이는 어두운 상황, 하늘이 무너지고 산이 바다로 무너져 내리는 듯한
        극단적인 상황에서도 사랑하는 사람이 곁에 있다면 괜찮다고 말합니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        이 노래는 어려운 단어가 많지 않고,
        <b>I won't be afraid</b>, <b>I won't cry</b>, <b>stand by me</b>처럼
        짧고 반복적인 표현이 많아 학생들이 듣고 따라 부르기에 좋습니다.
        또한 친구, 가족, 사랑하는 사람의 존재가 주는 안정감과 용기를
        자연스럽게 이야기해 볼 수 있는 노래입니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        수업에서는 <b>stand by me</b>, <b>I won't be afraid</b>,
        <b>I won't cry</b>, <b>shed a tear</b>, <b>whenever you're in trouble</b>
        같은 표현을 중심으로 배울 수 있습니다.
        특히 이 노래는 느린 속도와 반복 구조 덕분에
        기초 학습자도 영어 표현을 소리로 익히기에 적합합니다.
    </p>
    '''

    lyrics_full = [
        (
            "When the night has come / And the land is dark",
            "밤이 찾아오고 / 세상이 어두워질 때"
        ),
        (
            "And the moon is the only light we'll see",
            "달빛만이 우리가 볼 수 있는 유일한 빛일 때"
        ),
        (
            "No, I won't be afraid / Oh, I won't be afraid",
            "아니, 나는 두려워하지 않을 거야 / 오, 나는 두려워하지 않을 거야"
        ),
        (
            "Just as long as you stand / Stand by me",
            "네가 곁에 있어 준다면 / 내 곁에 있어 준다면"
        ),
        (
            "So darlin', darlin' / Stand by me, oh, stand by me",
            "그러니 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘"
        ),
        (
            "Oh, stand, stand by me / Stand by me",
            "오, 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘"
        ),
        (
            "If the sky that we look upon / Should tumble and fall",
            "우리가 바라보는 하늘이 / 무너져 내린다 해도"
        ),
        (
            "Or the mountain should crumble to the sea",
            "산이 부서져 바다로 무너져 내린다 해도"
        ),
        (
            "I won't cry, I won't cry / No, I won't shed a tear",
            "나는 울지 않을 거야, 울지 않을 거야 / 아니, 눈물 한 방울도 흘리지 않을 거야"
        ),
        (
            "Just as long as you stand / Stand by me",
            "네가 곁에 있어 준다면 / 내 곁에 있어 준다면"
        ),
        (
            "And darlin', darlin' / Stand by me, oh, stand by me",
            "그리고 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘"
        ),
        (
            "Oh, stand now, stand by me / Stand by me",
            "오, 지금 곁에 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘"
        ),
        (
            "Darlin', darlin' / Stand by me, oh, stand by me",
            "사랑하는 사람아, 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘"
        ),
        (
            "Oh, stand now, stand by me / Stand by me",
            "오, 지금 곁에 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘"
        ),
        (
            "Whenever you're in trouble / Won't you stand by me?",
            "네가 힘든 순간에 / 내 곁에 있어 주지 않을래?"
        ),
        (
            "Oh, stand by me / Won't you stand now?",
            "오, 내 곁에 있어 줘 / 지금 내 곁에 있어 주지 않을래?"
        ),
        (
            "Oh, stand, stand by me",
            "오, 있어 줘, 내 곁에 있어 줘"
        ),
    ]

    comprehension_questions = [
        {
            "q": "1. 이 노래는 어떤 시간적 배경으로 시작하나요?",
            "options": [
                "아침",
                "밤",
                "점심시간",
                "학교 수업 시간"
            ],
            "answer": "밤"
        },
        {
            "q": "2. 노래에서 보이는 유일한 빛은 무엇인가요?",
            "options": [
                "햇빛",
                "달빛",
                "휴대전화 불빛",
                "촛불"
            ],
            "answer": "달빛"
        },
        {
            "q": "3. 화자는 두려움에 대해 무엇이라고 말하나요?",
            "options": [
                "나는 두려워하지 않을 거야",
                "나는 항상 두려워",
                "나는 두려움을 좋아해",
                "나는 학교가 두려워"
            ],
            "answer": "나는 두려워하지 않을 거야"
        },
        {
            "q": "4. 'Stand by me'의 의미로 가장 알맞은 것은 무엇인가요?",
            "options": [ 
                "멀리 도망가",
                "앉아 있어",
                "집에 가"
                "내 곁에 있어 줘",
            ],
            "answer": "내 곁에 있어 줘"
        },
        {
            "q": "5. 이 노래의 중심 주제로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "쇼핑",
                "경쟁",
                "요리",
                "함께 있어 주는 힘과 위로",

            ],
            "answer": "함께 있어 주는 힘과 위로"
        },
        {
            "q": "6. 화자가 두려워하지 않는 이유는 무엇인가요?",
            "options": [
                "돈이 많기 때문에",
                "날씨가 맑기 때문에",
                "누군가가 곁에 있어 주기 때문에",
                "잠을 자고 있기 때문에"
            ],
            "answer": "누군가가 곁에 있어 주기 때문에"
        },
        {
            "q": "7. 'I won't shed a tear'의 의미로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "눈물 한 방울도 흘리지 않겠다",
                "많이 웃겠다",
                "잠을 자겠다",
                "멀리 떠나겠다"
            ],
            "answer": "눈물 한 방울도 흘리지 않겠다"
        },
        {
            "q": "8. 'Whenever you're in trouble'은 어떤 뜻인가요?",
            "options": [
                "네가 여행을 갈 때마다",
                "네가 노래할 때마다",
                "네가 힘든 순간에는 언제든지",                
                "네가 밥을 먹을 때마다"
            ],
            "answer": "네가 힘든 순간에는 언제든지"
        },
    ]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=nhLdJeLTM48&list=RDnhLdJeLTM48&start_radio=1"

    bg_content = '''
    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#7c3aed;">
        🌙 Don't Know Why: 이유를 알 수 없는 마음
    </h3>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        <b>Don't Know Why</b>는 Norah Jones의 대표곡으로,
        조용하고 부드러운 멜로디 속에 설명하기 어려운 아쉬움과 후회를 담고 있는 노래입니다.
        노래 속 화자는 누군가에게 가지 않았던 자신의 행동을 떠올리며,
        왜 그렇게 했는지 스스로도 알 수 없다고 말합니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        이 노래는 큰 사건을 직접적으로 설명하기보다,
        마음속에 남아 있는 감정의 흔적을 천천히 보여 줍니다.
        해가 뜰 때까지 기다렸지만 결국 가지 못했고,
        새벽이 밝아오는 순간에는 차라리 멀리 날아가 버리고 싶어 합니다.
        그래서 이 노래에는 후회, 망설임, 외로움, 그리움이 조용하게 섞여 있습니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        특히 <b>I don't know why I didn't come</b>이라는 문장이 반복되면서,
        화자가 자신의 마음을 명확히 설명하지 못하는 상태가 잘 드러납니다.
        이 반복 표현은 학생들이 듣고 따라 말하기 좋고,
        <b>I don't know why</b>, <b>I wished that I could</b>,
        <b>on my mind</b>, <b>empty as a drum</b> 같은 표현을 배우기에도 좋습니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        수업에서는 이 노래를 통해 느린 영어 발음, 감정 표현,
        후회와 그리움을 나타내는 문장을 함께 배울 수 있습니다.
        속도가 빠르지 않고 분위기가 차분해서,
        학생들이 영어 소리를 듣고 가사의 의미를 천천히 따라가기에 적합합니다.
    </p>
    '''

    lyrics_full = [
        (
            "I waited 'til I saw the sun / I don't know why I didn't come",
            "나는 해가 보일 때까지 기다렸어 / 왜 내가 가지 않았는지 모르겠어"
        ),
        (
            "I left you by the house of fun / Don't know why I didn't come",
            "나는 너를 즐거움의 집 곁에 남겨 두었어 / 왜 내가 가지 않았는지 모르겠어"
        ),
        (
            "Don't know why I didn't come",
            "왜 내가 가지 않았는지 모르겠어"
        ),
        (
            "When I saw the break of day / I wished that I could fly away",
            "새벽이 밝아오는 것을 보았을 때 / 나는 날아가 버릴 수 있기를 바랐어"
        ),
        (
            "Instead of kneeling in the sand / Catching tear-drops in my hand",
            "모래 위에 무릎 꿇고 있는 대신 / 손으로 눈물방울을 받으며"
        ),
        (
            "My heart is drenched in wine / But you'll be on my mind forever",
            "내 마음은 와인에 흠뻑 젖어 있지만 / 너는 영원히 내 마음속에 있을 거야"
        ),
        (
            "Out across the endless sea / I would die in ecstasy",
            "끝없는 바다 저편으로 / 나는 황홀함 속에서 죽을 수도 있을 것 같아"
        ),
        (
            "But I'll be a bag of bones / Driving down the road alone",
            "하지만 나는 뼈만 남은 사람처럼 / 혼자 길을 따라 운전하게 되겠지"
        ),
        (
            "My heart is drenched in wine / But you'll be on my mind forever",
            "내 마음은 와인에 흠뻑 젖어 있지만 / 너는 영원히 내 마음속에 있을 거야"
        ),
        (
            "Something has to make you run / I don't know why I didn't come",
            "무언가가 너를 떠나게 만들었겠지 / 왜 내가 가지 않았는지 모르겠어"
        ),
        (
            "I feel as empty as a drum / I don't know why I didn't come",
            "나는 북처럼 텅 빈 기분이야 / 왜 내가 가지 않았는지 모르겠어"
        ),
        (
            "Don't know why I didn't come / I don't know why I didn't come",
            "왜 내가 가지 않았는지 모르겠어 / 왜 내가 가지 않았는지 모르겠어"
        ),
    ]

    comprehension_questions = [
        {
            "q": "1. 화자는 무엇을 볼 때까지 기다렸나요?",
            "options": [
                "버스",
                "해",
                "선생님",
                "전화"
            ],
            "answer": "해"
        },
        {
            "q": "2. 화자가 계속 모르겠다고 말하는 것은 무엇인가요?",
            "options": [
                "무엇을 먹을지",
                "학교가 어디인지",
                "왜 자신이 가지 않았는지",
                "어떻게 읽는지"
            ],
            "answer": "왜 자신이 가지 않았는지"
        },
        {
            "q": "3. 'break of day'의 뜻으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "한밤중",
                "점심시간",
                "새벽",
                "겨울"
            ],
            "answer": "새벽"
        },
        {
            "q": "4. 화자는 새벽을 보았을 때 무엇을 바랐나요?",
            "options": [
                "일찍 자는 것",
                "차를 사는 것",
                "수학을 공부하는 것",
                "날아가 버리는 것"
            ],
            "answer": "날아가 버리는 것"
        },
        {
            "q": "5. 이 노래의 분위기로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "조용하고 후회스러운 분위기",
                "화나고 시끄러운 분위기",
                "빠르고 웃긴 분위기",
                "신나고 거친 분위기"
            ],
            "answer": "조용하고 후회스러운 분위기"
        },
        {
            "q": "6. 'You'll be on my mind forever'는 어떤 의미인가요?",
            "options": [
                "너는 곧 잊혀질 거야",
                "너는 영원히 내 마음속에 있을 거야",
                "너는 나와 함께 여행할 거야",
                "너는 노래를 부를 거야"
            ],
            "answer": "너는 영원히 내 마음속에 있을 거야"
        },
        {
            "q": "7. 'I feel as empty as a drum'은 어떤 감정에 가깝나요?",
            "options": [
                "배부름",
                "자신감",
                "공허함",
                "분노"
            ],
            "answer": "공허함"
        },
        {
            "q": "8. 이 노래에서 반복되는 핵심 문장은 무엇인가요?",
            "options": [
                "Stand by me",
                "Let it go",
                "A whole new world",
                "I don't know why I didn't come"
            ],
            "answer": "I don't know why I didn't come"
        },
    ]

elif "6. Fix You" in song_choice:
    video_url = "https://www.youtube.com/watch?v=k4V3Mo61fJM"

    bg_content = '''
    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#2563eb;">
        💡 Fix You: 힘든 순간에 건네는 위로
    </h3>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        Coldplay의 <b>Fix You</b>는 실패, 상실, 지침, 슬픔을 겪는 사람에게
        따뜻한 위로를 건네는 노래입니다. 노래 속 화자는 상대가 최선을 다했지만
        원하는 결과를 얻지 못했을 때, 그리고 잃어버린 것을 되돌릴 수 없을 때의
        아픔을 조용히 바라봅니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        이 노래에서 반복되는 <b>Lights will guide you home</b>은
        어두운 순간에도 길을 비춰 주는 희망을 상징합니다.
        또한 <b>I will try to fix you</b>는 상대를 완벽하게 고쳐 주겠다는 뜻이라기보다,
        힘든 시간을 혼자 견디지 않도록 곁에서 도와주고 싶다는 마음으로 이해할 수 있습니다.
    </p>

    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">
        수업에서는 <b>try your best</b>, <b>don't succeed</b>,
        <b>what you want / what you need</b>, <b>stuck in reverse</b>,
        <b>learn from my mistakes</b> 같은 표현을 중심으로 배울 수 있습니다.
        특히 이 노래는 속도가 비교적 느리고 감정선이 분명해서,
        학생들이 영어 표현과 함께 위로, 희망, 회복의 의미를 이해하기에 좋습니다.
    </p>
    '''

    lyrics_full = [
        (
            "When you try your best, but you don't succeed / When you get what you want, but not what you need",
            "네가 최선을 다했지만 성공하지 못할 때 / 원하는 것을 얻었지만 정작 필요한 것은 얻지 못할 때"
        ),
        (
            "When you feel so tired, but you can't sleep / Stuck in reverse",
            "너무 지쳤지만 잠들 수 없을 때 / 거꾸로 갇혀 있는 것처럼 느껴질 때"
        ),
        (
            "And the tears come streaming down your face / When you lose something you can't replace",
            "눈물이 네 얼굴을 타고 흘러내릴 때 / 대신할 수 없는 무언가를 잃었을 때"
        ),
        (
            "When you love someone, but it goes to waste / Could it be worse?",
            "누군가를 사랑했지만 그 마음이 헛되어 버렸을 때 / 이보다 더 나쁠 수 있을까?"
        ),
        (
            "Lights will guide you home / And ignite your bones",
            "빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야"
        ),
        (
            "And I will try to fix you",
            "그리고 나는 너를 다시 일으켜 주려고 노력할 거야"
        ),
        (
            "And high up above or down below / When you're too in love to let it go",
            "저 높은 곳에 있든 아주 낮은 곳에 있든 / 너무 사랑해서 놓아주기 어려울 때"
        ),
        (
            "But if you never try, you'll never know / Just what you're worth",
            "하지만 시도하지 않으면 절대 알 수 없어 / 네가 얼마나 소중한 사람인지"
        ),
        (
            "Lights will guide you home / And ignite your bones",
            "빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야"
        ),
        (
            "And I will try to fix you",
            "그리고 나는 너를 다시 일으켜 주려고 노력할 거야"
        ),
        (
            "Tears stream down your face / When you lose something you cannot replace",
            "눈물이 네 얼굴을 타고 흘러내려 / 대신할 수 없는 무언가를 잃었을 때"
        ),
        (
            "Tears stream down your face, and I / Tears stream down your face",
            "눈물이 네 얼굴을 타고 흘러내리고, 나는 / 눈물이 네 얼굴을 타고 흘러내려"
        ),
        (
            "I promise you I will learn from my mistakes / Tears stream down your face, and I",
            "나는 내 실수에서 배우겠다고 약속할게 / 눈물이 네 얼굴을 타고 흘러내리고, 나는"
        ),
        (
            "Lights will guide you home / And ignite your bones",
            "빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야"
        ),
        (
            "And I will try to fix you",
            "그리고 나는 너를 다시 일으켜 주려고 노력할 거야"
        ),
    ]

    comprehension_questions = [
        {
            "q": "1. 이 노래에서 화자는 어떤 사람을 위로하고 있나요?",
            "options": [
                "시험을 준비하는 사람",
                "여행을 떠나는 사람",
                "힘들고 지친 사람",
                "운동을 시작한 사람"
            ],
            "answer": "힘들고 지친 사람"
        },
        {
            "q": "2. 'When you try your best, but you don't succeed'의 의미로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "최선을 다했지만 성공하지 못할 때",
                "아무 노력도 하지 않았을 때",
                "원하는 것을 모두 얻었을 때",
                "잠을 충분히 잤을 때"
            ],
            "answer": "최선을 다했지만 성공하지 못할 때"
        },
        {
            "q": "3. 'what you want'와 'what you need'의 차이로 알맞은 것은 무엇인가요?",
            "options": [
                "둘 다 항상 같은 뜻이다",
                "want는 원하는 것, need는 정말 필요한 것이다",
                "want는 먹는 것, need는 노래하는 것이다",
                "need는 필요 없는 것이다"
            ],
            "answer": "want는 원하는 것, need는 정말 필요한 것이다"
        },
        {
            "q": "4. 'Lights will guide you home'은 무엇을 상징한다고 볼 수 있나요?",
            "options": [
                "휴대전화 불빛",
                "가게의 간판",
                "어두운 길에서의 희망과 방향",
                "자동차 헤드라이트만"
            ],
            "answer": "어두운 길에서의 희망과 방향"
        },
        {
            "q": "5. 'If you never try, you'll never know'의 의미로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "절대 시도하면 안 된다",
                "시도하지 않으면 알 수 없다",
                "모든 것을 이미 알고 있다",
                "실패하면 끝이다"
            ],
            "answer": "시도하지 않으면 알 수 없다"
        },
        {
            "q": "6. 'I will learn from my mistakes'는 어떤 태도를 보여 주나요?",
            "options": [
                "실수를 숨기려는 태도",
                "남을 탓하려는 태도",
                "포기하려는 태도",
                "실수에서 배우려는 태도"
            ],
            "answer": "실수에서 배우려는 태도"
        },
        {
            "q": "7. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?",
            "options": [
                "위로와 희망",
                "웃음과 장난",
                "분노와 복수",
                "경쟁과 승리"
            ],
            "answer": "위로와 희망"
        },
        {
            "q": "8. 'I will try to fix you'는 어떤 의미에 가깝나요?",
            "options": [
                "너를 혼내겠다",
                "너를 완전히 바꾸겠다",
                "너를 떠나겠다",
                "너를 도와 다시 일어서게 하고 싶다"
            ],
            "answer": "너를 도와 다시 일어서게 하고 싶다"
        },
    ]

# =========================
# 5. 화면 출력
# =========================

if selected_tab == "🎬 배경 학습":
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown(bg_content, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🎬 Music Video")
    st.video(video_url)


elif selected_tab == "📖 가사 & 퀴즈":
    st.markdown("## 🎵 Full Lyrics & Quiz")

    st.markdown(
        """
        <div class="quiz-box">
            <h3 style="margin-top:0;">🎬 영상을 보며 전체 가사를 읽어 봅시다</h3>
            <p style="font-size:16px; margin-bottom:0;">
            먼저 영상을 보면서 노래의 분위기를 느껴 봅시다.
            그다음 영어 가사와 한국어 뜻을 함께 읽고, 아래 이해도 문제를 풀어 봅시다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ✅ 두 번째 탭에도 같은 영상 넣기
    st.video(video_url)

    st.markdown("---")
    st.markdown("## 📖 Lyrics")

    for eng, kor in lyrics_full:
        st.markdown(
            f"""
            <div class="lyrics-container">
                <div class="eng-line">{eng}</div>
                <div class="kor-sub">{kor}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("## 📝 이해도 문제")

    st.markdown(
        """
        <div class="quiz-box">
            <b>전체 가사를 읽은 뒤 문제를 풀어 봅시다.</b><br>
            화자의 상황, 감정, 반복되는 표현을 중심으로 생각하면 됩니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    score = 0
    user_answers = []

    safe_song_key = (
        song_choice
        .replace(" ", "_")
        .replace(".", "")
        .replace("-", "_")
        .replace("'", "")
        .replace("&", "and")
    )

    with st.form(f"comprehension_quiz_form_{safe_song_key}"):
        for i, item in enumerate(comprehension_questions):
            st.markdown(f"### {item['q']}")

            answer = st.radio(
                "정답을 고르세요.",
                item["options"],
                key=f"comp_quiz_{safe_song_key}_{i}",
                label_visibility="collapsed"
            )

            user_answers.append(answer)

        submitted = st.form_submit_button("✅ 정답 확인하기")

    if submitted:
        st.markdown("## 📌 결과 확인")

        for i, item in enumerate(comprehension_questions):
            correct = item["answer"]
            user_answer = user_answers[i]

            if user_answer == correct:
                score += 1
                st.success(f"{i+1}. 정답입니다! ✅")
            else:
                st.error(f"{i+1}. 틀렸습니다 ❌")
                st.markdown(f"정답: **{correct}**")

        st.markdown(
            f"""
            <div class="score-box">
                <h2 style="margin:0;">점수: {score} / {len(comprehension_questions)}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
