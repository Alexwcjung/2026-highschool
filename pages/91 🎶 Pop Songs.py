import streamlit as st
import streamlit.components.v1 as components
import random
import html
import re
import json
import uuid

st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
.stApp { background-color:#ffffff; color:#1e293b; }
.main-title {
    background: linear-gradient(135deg,#eef2ff,#f0f9ff,#fdf2f8);
    padding: 25px;
    border-radius: 18px;
    border: 2px solid #6366f1;
    text-align: center;
    color: #3730a3;
    margin-bottom: 22px;
}
.info-box {
    background-color:#f8fafc;
    padding:34px 38px;
    border-radius:22px;
    border:2px solid #cbd5e1;
    line-height:2.1;
    margin-bottom:26px;
    font-size:1.35rem;
}
.info-box h3 {
    color:#4338ca;
    border-bottom:4px solid #6366f1;
    padding-bottom:14px;
    margin-bottom:22px;
    font-size:2.4rem;
    font-weight:900;
}
.info-box p {
    font-size:1.35rem;
    line-height:2.1;
    color:#1e293b;
    margin-bottom:20px;
}
.info-box p {
    font-size:1.35rem;
    line-height:2.1;
    color:#1e293b;
    margin-bottom:20px;
}
.lyrics-container {
    padding:14px 20px;
    border-left:5px solid #6366f1;
    margin-bottom:10px;
    background-color:#f8fafc;
    border-radius:0 12px 12px 0;
}
.eng-line { font-size:1.08rem; font-weight:800; color:#1e3a8a; }
.kor-sub { font-size:0.95rem; color:#64748b; margin-top:5px; line-height:1.6; }
.quiz-box { background-color:#f0f9ff; padding:20px; border-radius:18px; border:1px solid #bae6fd; margin-top:22px; margin-bottom:20px; }
.score-box { background:linear-gradient(135deg,#dcfce7,#bbf7d0); padding:18px; border-radius:18px; border:1px solid #86efac; margin-top:18px; text-align:center; font-size:1.15rem; font-weight:900; }
.wrong-box { background:#fff7ed; padding:15px; border-radius:14px; border:1px solid #fdba74; margin-top:10px; }
.game-card { background:linear-gradient(135deg,#eef2ff,#f8fafc); border:1px solid #c7d2fe; border-radius:18px; padding:20px; margin-bottom:18px; }
.big-guide { font-size:1.12rem; font-weight:800; color:#475569; line-height:1.7; }
.matching-box { background:linear-gradient(135deg,#eef2ff 0%,#f0f9ff 50%,#fdf2f8 100%); padding:24px; border-radius:20px; border:1px solid #c7d2fe; margin-top:18px; margin-bottom:22px; }
.matching-title { font-size:2rem; font-weight:900; color:#4338ca; margin-bottom:10px; }
.selected-card-notice { background-color:#fef3c7; padding:14px 16px; border-radius:14px; border:1px solid #facc15; color:#92400e; font-size:1.05rem; font-weight:900; margin-bottom:16px; }
.feedback-ko { background:#fefce8; border:1px solid #fde68a; padding:18px; border-radius:16px; line-height:1.8; margin-top:14px; }
.feedback-en { background:#eff6ff; border:1px solid #bfdbfe; padding:18px; border-radius:16px; line-height:1.8; margin-top:14px; }
.advice-box { background:#f0fdf4; border:1px solid #bbf7d0; padding:18px; border-radius:16px; line-height:1.8; margin-top:14px; }

/* 배경 학습 전용 큰 글씨 카드 */
.bg-card {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
    padding: 34px 38px;
    border-radius: 24px;
    border: 2px solid #c7d2fe;
    margin-bottom: 26px;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.08);
}
.bg-title {
    font-size: 2.35rem;
    font-weight: 900;
    color: #3730a3;
    margin-bottom: 22px;
    padding-bottom: 14px;
    border-bottom: 4px solid #6366f1;
}
.bg-p {
    font-size: 1.35rem;
    line-height: 2.05;
    color: #1e293b;
    margin-bottom: 18px;
    font-weight: 560;
}
.bg-key {
    color: #1e3a8a;
    font-weight: 900;
}

</style>
""", unsafe_allow_html=True)


def clean_text_for_display(text):
    return html.escape(str(text).strip())

def safe_key(text):
    return re.sub(r"[^a-zA-Z0-9가-힣_]+", "_", text)

def shuffle_options(options, seed):
    rng = random.Random(seed)
    options = list(options)
    rng.shuffle(options)
    return options

def try_translate_ko_to_en(korean_text):
    korean_text = str(korean_text).strip()
    if not korean_text:
        return ""
    try:
        from deep_translator import GoogleTranslator
        translated = GoogleTranslator(source="ko", target="en").translate(korean_text)
        translated = str(translated).strip()
        if re.search(r"[가-힣]", translated):
            raise ValueError("Korean remained")
        return translated
    except Exception:
        return (
            "While listening to this song, I looked back on my own memories and emotions. "
            "This reflection was not just about the past; it helped me think about my relationships, choices, and feelings more deeply. "
            "The song reminds me that difficult memories can become meaningful when we try to understand them honestly."
        )

def make_polished_feedback(song_title, question, student_answer):
    answer = str(student_answer).strip()
    question = str(question).strip()
    if len(answer) < 10:
        polished_ko = (
            "이 노래를 들으며 아직 생각을 길게 정리하지는 못했지만, 마음속에 떠오르는 감정이 있다는 점이 중요합니다. "
            "노래 속 화자의 마음처럼, 나에게도 쉽게 말하지 못한 기억이나 다시 생각해 보고 싶은 순간이 있을 수 있습니다. "
            "그 감정을 조금 더 자세히 들여다보면, 단순한 감상이 아니라 나 자신을 이해하는 글로 발전할 수 있습니다."
        )
    else:
        polished_ko = (
            f"이 노래를 들으며 나는 다음과 같은 생각을 하게 되었습니다. {answer} "
            "이 경험은 단순히 지나간 일을 떠올리는 데서 끝나지 않습니다. 그때의 감정과 지금의 마음을 함께 돌아보게 하며, "
            "사람과의 관계가 언제나 쉽지만은 않다는 사실도 생각하게 합니다. 노래 속 화자의 감정처럼, 나 역시 과거의 한 장면을 다시 바라보며 "
            "그때 미처 표현하지 못했던 마음을 생각해 볼 수 있었습니다. 이런 성찰은 나의 감정을 더 깊이 이해하고, 앞으로의 관계를 조금 더 성숙하게 바라보는 계기가 됩니다."
        )
    if ("Scientist" in song_title or "그리운" in question or "옛" in question or "처음" in question or "관계" in question) and len(answer) >= 10:
        polished_ko = (
            f"이 노래를 들으며 나는 과거의 관계와 그때의 감정을 다시 떠올리게 되었습니다. {answer} "
            "그 기억은 단순한 추억이라기보다, 마음을 쉽게 열지 못했던 순간과 서로를 충분히 이해하지 못했던 시간을 돌아보게 합니다. "
            "노래 속 화자가 ‘처음으로 돌아가고 싶다’고 말하는 것처럼, 나 역시 그때로 돌아간다면 조금 더 솔직하게 말하고, "
            "상대의 마음을 더 천천히 이해하려 했을 것 같습니다. 결국 이 노래는 사랑이나 관계가 생각처럼 쉽지 않지만, "
            "그 어려움 속에서도 우리는 자신의 감정과 선택을 배울 수 있다는 점을 느끼게 해 줍니다."
        )
    english_translation = try_translate_ko_to_en(polished_ko)
    if re.search(r"[가-힣]", english_translation):
        english_translation = (
            "While listening to this song, I looked back on a past relationship and the emotions I felt at that time. "
            "The memory was not just a simple memory; it helped me think about moments when it was difficult to open my heart and when two people could not fully understand each other. "
            "Like the speaker in the song who wants to go back to the start, I also wondered what I might say or do differently if I could return to that moment. "
            "In the end, this song reminds me that love and relationships are not always easy, but they can help us understand our feelings and grow as a person."
        )
    advice = (
        "쓰기 조언: 글을 더 좋게 만들고 싶다면 ① 떠오른 사람이나 장면, ② 그때의 감정, ③ 지금 돌아보며 깨달은 점을 차례로 써 보세요. "
        "영어로 쓸 때는 다음 구조를 활용하면 좋습니다: While listening to this song, I thought about ~. / At that time, I felt ~ because ~. / Looking back now, I realize that ~."
    )
    return polished_ko, english_translation, advice

SONGS = {'1. Let It Go - Frozen OST': {'video_url': 'https://www.youtube.com/watch?v=RgGRyssdJvw',
                               'bg': '\n'
                                     '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#be185d;">\n'
                                     '        ❄️ Let It Go: 숨겨 왔던 자신을 받아들이는 순간\n'
                                     '    </h3>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        <b>Let It Go</b>는 영화 <i>Frozen</i>의 대표곡으로,\n'
                                     '        엘사가 더 이상 자신의 능력과 감정을 숨기지 않고\n'
                                     '        스스로를 받아들이는 장면에서 나오는 노래입니다.\n'
                                     '    </p>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        엘사는 어릴 때부터 자신의 얼음 마법이 다른 사람을 다치게 할 수 있다는\n'
                                     '        두려움 속에서 살아왔습니다. 그래서 감정을 숨기고,\n'
                                     '        능력을 감추며, 언제나 조심해야 했습니다.\n'
                                     '        하지만 대관식 날 엘사의 능력이 사람들 앞에서 드러나고,\n'
                                     '        사람들은 엘사를 두려워합니다.\n'
                                     '    </p>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        엘사는 모든 것을 피해 눈 덮인 산으로 도망치고,\n'
                                     '        그곳에서 처음으로 자신의 진짜 모습을 마주합니다.\n'
                                     '        이 노래는 단순히 “다 잊어버리자”는 의미가 아니라,\n'
                                     '        그동안 억눌렀던 두려움, 책임감, 타인의 시선에서 벗어나\n'
                                     '        자기 자신을 받아들이는 과정을 보여줍니다.\n'
                                     '    </p>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        수업에서는 <b>let it go</b>, <b>conceal</b>, <b>hold back</b>,\n'
                                     "        <b>storm inside</b>, <b>I'm free</b>, <b>the past is in the past</b>\n"
                                     '        같은 표현을 중심으로 배울 수 있습니다.\n'
                                     '        특히 이 노래는 자유, 두려움, 자기표현, 자신감에 대해\n'
                                     '        함께 생각해 볼 수 있는 좋은 자료입니다.\n'
                                     '    </p>\n'
                                     '    ',
                               'lyrics': [('The snow glows white on the mountain tonight / Not a footprint to be seen',
                                           '오늘 밤 산 위에는 눈이 하얗게 빛나고 / 발자국 하나 보이지 않아요'),
                                          ("A kingdom of isolation / And it looks like I'm the queen", '고립된 왕국 / 그리고 내가 그곳의 여왕인 것 같아요'),
                                          ("The wind is howling like this swirling storm inside / Couldn't keep it in, heaven knows I tried",
                                           '바람은 내 안에서 휘몰아치는 폭풍처럼 울부짖고 / 더는 감출 수 없었어요, 하늘은 내가 얼마나 노력했는지 알 거예요'),
                                          ("Don't let them in, don't let them see / Be the good girl you always have to be",
                                           '그들을 들이지 마, 보여주지 마 / 언제나 그래야만 했던 착한 소녀가 되어라'),
                                          ("Conceal, don't feel, don't let them know / Well, now they know", '숨기고, 느끼지 말고, 그들이 알게 하지 마 / 하지만 이제 그들이 알아버렸어요'),
                                          ("Let it go, let it go / Can't hold it back anymore", '놓아버려, 놓아버려 / 더 이상 붙잡아 둘 수 없어'),
                                          ('Let it go, let it go / Turn away and slam the door', '놓아버려, 놓아버려 / 돌아서서 문을 세게 닫아버려'),
                                          ("I don't care what they're going to say / Let the storm rage on", '사람들이 뭐라고 하든 상관없어 / 폭풍이 계속 몰아치게 둬'),
                                          ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없으니까'),
                                          ("It's funny how some distance makes everything seem small / And the fears that once controlled me can't get to me "
                                           'at all',
                                           '거리를 두고 보니 모든 것이 작아 보이는 게 참 이상해 / 한때 나를 지배했던 두려움도 이제는 나에게 닿지 못해'),
                                          ("It's time to see what I can do / To test the limits and break through",
                                           '이제 내가 무엇을 할 수 있는지 볼 시간이야 / 한계를 시험하고 그것을 깨고 나아갈 시간이야'),
                                          ("No right, no wrong, no rules for me / I'm free", '옳고 그름도, 나를 묶는 규칙도 없어 / 나는 자유로워'),
                                          ('Let it go, let it go / I am one with the wind and sky', '놓아버려, 놓아버려 / 나는 바람과 하늘과 하나가 되었어'),
                                          ("Let it go, let it go / You'll never see me cry", '놓아버려, 놓아버려 / 너희는 다시는 내가 우는 모습을 보지 못할 거야'),
                                          ('Here I stand and here I stay / Let the storm rage on', '나는 여기 서 있고, 여기 머물 거야 / 폭풍이 계속 몰아치게 둬'),
                                          ('My power flurries through the air into the ground / My soul is spiraling in frozen fractals all around',
                                           '내 힘은 공기를 지나 땅속으로 흩날려 퍼지고 / 내 영혼은 사방의 얼어붙은 결정 속에서 소용돌이쳐'),
                                          ("And one thought crystallizes like an icy blast / I'm never going back, the past is in the past",
                                           '그리고 하나의 생각이 얼음바람처럼 선명하게 굳어져 / 나는 절대 돌아가지 않아, 과거는 과거일 뿐이야'),
                                          ("Let it go, let it go / And I'll rise like the break of dawn", '놓아버려, 놓아버려 / 나는 새벽이 밝아오듯 다시 일어설 거야'),
                                          ('Let it go, let it go / That perfect girl is gone', '놓아버려, 놓아버려 / 그 완벽한 소녀는 이제 없어'),
                                          ('Here I stand in the light of day / Let the storm rage on', '나는 밝은 낮의 빛 속에 서 있어 / 폭풍이 계속 몰아치게 둬'),
                                          ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없으니까')],
                               'quiz': [{'q': '1. 이 노래를 부르는 인물은 누구인가요?', 'options': ['Anna', 'Olaf', 'Kristoff', 'Elsa'], 'answer': 'Elsa'},
                                        {'q': '2. 엘사는 어디에서 이 노래를 부르나요?', 'options': ['교실', '바닷가', '눈 덮인 산', '도시 거리'], 'answer': '눈 덮인 산'},
                                        {'q': '3. 엘사가 더 이상 하지 않으려는 것은 무엇인가요?',
                                         'options': ['음식을 먹는 것', '학교에 가는 것', '동물과 이야기하는 것', '자신을 숨기는 것'],
                                         'answer': '자신을 숨기는 것'},
                                        {'q': '4. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?', 'options': ['배고픔', '지루함', '자유와 해방감', '질투'], 'answer': '자유와 해방감'},
                                        {'q': "5. 'conceal'의 뜻으로 가장 알맞은 것은 무엇인가요?", 'options': ['숨기다', '달리다', '노래하다', '웃다'], 'answer': '숨기다'},
                                        {'q': "6. 'Can't hold it back anymore'는 어떤 의미에 가깝나요?",
                                         'options': ['더 이상 문을 열 수 없다', '더 이상 노래할 수 없다', '더 이상 걸을 수 없다', '더 이상 억누를 수 없다'],
                                         'answer': '더 이상 억누를 수 없다'},
                                        {'q': "7. 'I'm free'에서 엘사가 느끼는 감정은 무엇인가요?", 'options': ['두려움', '부끄러움', '자유로움', '배고픔'], 'answer': '자유로움'},
                                        {'q': "8. 'the past is in the past'는 어떤 의미인가요?",
                                         'options': ['과거로 돌아가고 싶다', '과거는 과거일 뿐이다', '과거가 가장 중요하다', '과거를 다시 만들 수 있다'],
                                         'answer': '과거는 과거일 뿐이다'}],
                               'key_expressions': [('Let it go', '놓아버려'),
                                                   ("Can't hold it back anymore", '더 이상 억누를 수 없어'),
                                                   ("Conceal, don't feel", '숨기고, 느끼지 마'),
                                                   ('Let the storm rage on', '폭풍이 계속 몰아치게 둬'),
                                                   ("I'm free", '나는 자유로워'),
                                                   ('The past is in the past', '과거는 과거일 뿐이야'),
                                                   ('Here I stand', '나는 여기 서 있어'),
                                                   ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없어'),
                                                   ('Test the limits', '한계를 시험하다'),
                                                   ('Break through', '뚫고 나아가다')],
                               'matching': [('Let it go', '놓아버려'),
                                            ("Can't hold it back anymore", '더 이상 억누를 수 없어'),
                                            ("I'm free", '나는 자유로워'),
                                            ('The past is in the past', '과거는 과거일 뿐이야'),
                                            ('Here I stand', '나는 여기 서 있어'),
                                            ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없어')],
                               'reflect_questions': ['다른 사람의 시선 때문에 나 자신을 숨긴 적이 있나요?',
                                                     '내가 더 이상 붙잡고 싶지 않은 두려움이나 걱정은 무엇인가요?',
                                                     '이 노래처럼 “나는 자유로워”라고 말하고 싶은 순간은 언제인가요?']},
 '2. Hello - Adele': {'video_url': 'https://www.youtube.com/watch?v=h7NBamHcX58',
                      'bg': '\n'
                            '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#4338ca;">\n'
                            '        ☎️ Hello: 과거의 누군가에게 건네는 늦은 안부\n'
                            '    </h3>\n'
                            '\n'
                            '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                            '        Adele의 <b>Hello</b>는 시간이 많이 흐른 뒤, 과거의 누군가에게 다시 연락하고 싶은 마음을 담은 노래입니다.\n'
                            '        노래 속 화자는 상대에게 전화를 걸며 오래전의 관계, 미안함, 후회,\n'
                            '        그리고 아직 완전히 치유되지 않은 감정을 떠올립니다.\n'
                            '    </p>\n'
                            '\n'
                            '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                            '        이 노래에서 화자는 단순히 “안녕”이라고 말하는 것이 아니라,\n'
                            '        과거에 하지 못했던 사과를 전하고 싶어 합니다.\n'
                            '        하지만 두 사람 사이에는 시간의 거리, 마음의 거리, 그리고 실제 거리까지 생겨 있습니다.\n'
                            '        그래서 반복되는 <b>Hello</b>라는 말은 인사이면서 동시에 조심스러운 사과의 시작처럼 들립니다.\n'
                            '    </p>\n'
                            '\n'
                            '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                            "        수업에서는 <b>I'm sorry</b>, <b>I tried</b>, <b>after all these years</b>,\n"
                            '        <b>used to be</b>, <b>the other side</b> 같은 표현을 중심으로 배울 수 있습니다.\n'
                            '        특히 이 노래는 속도가 비교적 느리고 감정이 분명하게 드러나기 때문에,\n'
                            '        학생들이 가사를 읽으며 화자의 감정과 영어 표현을 함께 이해하기에 좋습니다.\n'
                            '    </p>\n'
                            '    ',
                      'lyrics': [("Hello, it's me / I was wondering if after all these years you'd like to meet, to go over everything",
                                  '안녕, 나야 / 이 모든 세월이 흐른 뒤에 네가 만나서 모든 일을 다시 이야기해 보고 싶어 할지 궁금했어'),
                                 ("They say that time's supposed to heal ya / But I ain't done much healing",
                                  '사람들은 시간이 너를 치유해 줄 거라고 말하지만 / 나는 별로 치유되지 않은 것 같아'),
                                 ("Hello, can you hear me? / I'm in California dreaming about who we used to be",
                                  '여보세요, 내 말 들리니? / 나는 캘리포니아에서 예전의 우리 모습을 떠올리고 있어'),
                                 ("When we were younger and free / I've forgotten how it felt before the world fell at our feet",
                                  '우리가 더 어리고 자유로웠을 때 / 세상이 우리 발아래 있는 것 같았던 그 느낌을 나는 잊어버렸어'),
                                 ("There's such a difference between us / And a million miles", '우리 사이에는 너무 큰 차이가 있어 / 그리고 백만 마일만큼의 거리도 있어'),
                                 ("Hello from the other side / I must've called a thousand times to tell you", '저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야'),
                                 ("I'm sorry, for everything that I've done / But when I call you never seem to be home",
                                  '내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아'),
                                 ("Hello from the outside / At least I can say that I've tried to tell you", '바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어'),
                                 ("I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
                                  '네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아'),
                                 ("Hello, how are you? / It's so typical of me to talk about myself", '안녕, 어떻게 지내? / 내 이야기만 하는 건 정말 나다운 일이야'),
                                 ("I'm sorry, I hope that you're well / Did you ever make it out of that town where nothing ever happened?",
                                  '미안해, 네가 잘 지내길 바라 / 아무 일도 일어나지 않던 그 마을에서 벗어났니?'),
                                 ("It's no secret that the both of us are running out of time", '우리 둘 다 시간이 얼마 남지 않았다는 건 비밀도 아니야'),
                                 ("Hello from the other side / I must've called a thousand times to tell you", '저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야'),
                                 ("I'm sorry, for everything that I've done / But when I call you never seem to be home",
                                  '내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아'),
                                 ("Hello from the outside / At least I can say that I've tried to tell you", '바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어'),
                                 ("I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
                                  '네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아'),
                                 ('Ooooohh, anymore / Ooooohh, anymore / Ooooohh, anymore / Anymore', '오, 더 이상 / 오, 더 이상 / 오, 더 이상 / 더 이상'),
                                 ("Hello from the other side / I must've called a thousand times to tell you", '저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야'),
                                 ("I'm sorry, for everything that I've done / But when I call you never seem to be home",
                                  '내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아'),
                                 ("Hello from the outside / At least I can say that I've tried to tell you", '바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어'),
                                 ("I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
                                  '네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아')],
                      'quiz': [{'q': '1. 이 노래에서 화자는 누구에게 연락하려고 하나요?', 'options': ['새로 만난 선생님', '유명한 가수', '캘리포니아의 낯선 사람', '과거에 알던 사람'], 'answer': '과거에 알던 사람'},
                               {'q': '2. 화자가 상대에게 가장 말하고 싶어 하는 것은 무엇인가요?', 'options': ['고맙다는 말', '미안하다는 말', '생일 축하한다는 말', '여행을 가자는 말'], 'answer': '미안하다는 말'},
                               {'q': '3. 노래에서 사람들은 시간이 무엇을 해 준다고 말하나요?',
                                'options': ['사람을 부자로 만들어 준다', '과거를 완전히 바꿔 준다', '상처를 치유해 준다', '슬픔을 바로 없애 준다'],
                                'answer': '상처를 치유해 준다'},
                               {'q': '4. 화자는 어디에서 예전의 자신들을 떠올리고 있나요?', 'options': ['런던', '캘리포니아', '뉴욕', '파리'], 'answer': '캘리포니아'},
                               {'q': "5. 'I must've called a thousand times'는 어떤 의미에 가깝나요?",
                                'options': ['정확히 천 번만 전화했다', '한 번도 전화하지 않았다', '전화번호를 잊어버렸다', '정말 여러 번 연락하려고 했다'],
                                'answer': '정말 여러 번 연락하려고 했다'},
                               {'q': "6. 'Hello from the other side'에서 'the other side'는 무엇을 상징한다고 볼 수 있나요?",
                                'options': ['학교의 반대편 교실', '가수가 사는 집', '멀어진 시간과 마음의 거리', '무대의 왼쪽'],
                                'answer': '멀어진 시간과 마음의 거리'},
                               {'q': "7. 화자가 'I tried'라고 말하는 이유는 무엇인가요?",
                                'options': ['노래 대회에 나가려고 했기 때문에', '캘리포니아로 여행을 가고 싶었기 때문에', '새로운 친구를 만들고 싶었기 때문에', '상대에게 사과하려고 노력했기 때문에'],
                                'answer': '상대에게 사과하려고 노력했기 때문에'},
                               {'q': '8. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?', 'options': ['여행의 설렘', '후회와 사과', '복수심과 분노', '시험에 대한 걱정'], 'answer': '후회와 사과'}],
                      'key_expressions': [("Hello, it's me", '안녕, 나야'),
                                          ('After all these years', '이 모든 세월이 흐른 뒤에'),
                                          ("Time's supposed to heal you", '시간이 너를 치유해 줄 거라고 여겨진다'),
                                          ('Can you hear me?', '내 말 들리니?'),
                                          ('Who we used to be', '예전의 우리 모습'),
                                          ('Hello from the other side', '저편에서 전하는 안녕'),
                                          ("I must've called a thousand times", '정말 여러 번 전화했을 거야'),
                                          ("I'm sorry", '미안해'),
                                          ("At least I can say that I've tried", '적어도 노력했다고 말할 수 있어'),
                                          ("I hope that you're well", '네가 잘 지내길 바라')],
                      'matching': [("Hello, it's me", '안녕, 나야'),
                                   ("I'm sorry", '미안해'),
                                   ('I tried', '나는 노력했어'),
                                   ('Hello from the other side', '저편에서 안녕이라고 말해'),
                                   ('Can you hear me?', '내 말 들리니?'),
                                   ("I hope that you're well", '네가 잘 지내길 바라')],
                      'reflect_questions': ['오랫동안 연락하지 못했지만 다시 이야기하고 싶은 사람이 있나요?', '누군가에게 미안하다고 말하지 못했던 경험이 있나요?', '시간이 지나면서 치유된 감정이나 아직 남아 있는 감정이 있나요?']},
 '3. A Whole New World - Aladdin OST': {'video_url': 'https://www.youtube.com/watch?v=9FJssSUxI88',
                                        'bg': '\n'
                                              '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#4338ca;">\n'
                                              '        🕌 A Whole New World: 새로운 세상을 바라보는 순간\n'
                                              '    </h3>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        <b>A Whole New World</b>는 영화 <i>Aladdin</i>의 대표곡으로,\n'
                                              '        알라딘과 자스민이 마법 양탄자를 타고 밤하늘을 날며\n'
                                              '        새로운 세상을 바라보는 장면에서 나오는 노래입니다.\n'
                                              '    </p>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        자스민은 궁전 안에서 공주로 살아가지만,\n'
                                              '        정해진 규칙과 역할 속에서 자유롭게 세상을 경험하지 못합니다.\n'
                                              '        알라딘은 그런 자스민에게 궁전 밖의 넓은 세상을 보여 주고,\n'
                                              '        자스민은 처음으로 자신이 알지 못했던 새로운 풍경과 가능성을 마주하게 됩니다.\n'
                                              '    </p>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        이 노래에서 <b>a whole new world</b>는 단순히 새로운 장소만을 뜻하지 않습니다.\n'
                                              '        새로운 시선, 새로운 경험, 그리고 스스로 선택할 수 있는 자유를 의미합니다.\n'
                                              '        두 사람은 마법 양탄자를 타고 하늘을 날며,\n'
                                              '        두려움보다 설렘이 더 큰 새로운 세계로 함께 나아갑니다.\n'
                                              '    </p>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        수업에서는 <b>I can show you the world</b>, <b>open your eyes</b>,\n'
                                              '        <b>point of view</b>, <b>crystal clear</b>, <b>new horizons</b>\n'
                                              '        같은 표현을 중심으로 배울 수 있습니다.\n'
                                              '        특히 이 노래는 속도가 비교적 부드럽고 장면이 분명해서,\n'
                                              '        학생들이 영어 표현과 함께 설렘, 자유, 새로운 경험의 감정을 이해하기에 좋습니다.\n'
                                              '    </p>\n'
                                              '    ',
                                        'lyrics': [('I can show you the world / Shining, shimmering, splendid', '내가 너에게 세상을 보여 줄 수 있어 / 빛나고, 반짝이고, 눈부신 세상을'),
                                                   ('Tell me, princess, now when did / You last let your heart decide?',
                                                    '말해 봐요, 공주님, 언제였나요 / 마지막으로 마음이 원하는 대로 선택했던 때가?'),
                                                   ('I can open your eyes / Take you wonder by wonder', '내가 너의 눈을 뜨게 해 줄 수 있어 / 놀라움에서 또 다른 놀라움으로 데려가며'),
                                                   ('Over, sideways and under / On a magic carpet ride', '위로, 옆으로, 아래로 날아가며 / 마법 양탄자를 타고'),
                                                   ('A whole new world / A new fantastic point of view', '완전히 새로운 세상 / 새롭고 환상적인 시선'),
                                                   ('No one to tell us no / Or where to go', '아무도 우리에게 안 된다고 말하지 않고 / 어디로 가라고 하지도 않아'),
                                                   ("Or say we're only dreaming", '우리가 그저 꿈꾸고 있을 뿐이라고 말하지도 않아'),
                                                   ('A whole new world / A dazzling place I never knew', '완전히 새로운 세상 / 내가 전에는 알지 못했던 눈부신 곳'),
                                                   ("But when I'm way up here, it's crystal clear / That now I'm in a whole new world with you",
                                                    '하지만 이렇게 높은 곳에 올라오니 모든 것이 분명해 / 지금 나는 너와 함께 완전히 새로운 세상에 있어'),
                                                   ("(Now I'm in a whole new world with you)", '이제 나는 너와 함께 완전히 새로운 세상에 있어'),
                                                   ('Unbelievable sights / Indescribable feeling', '믿기 어려운 풍경들 / 말로 표현할 수 없는 감정'),
                                                   ('Soaring, tumbling, freewheeling / Through an endless diamond sky',
                                                    '솟아오르고, 구르고, 자유롭게 날아가며 / 끝없이 펼쳐진 다이아몬드 같은 하늘을 지나'),
                                                   ("A whole new world / Don't you dare close your eyes", '완전히 새로운 세상 / 절대 눈 감지 마'),
                                                   ('A hundred thousand things to see / Hold your breath, it gets better',
                                                    '볼 것이 셀 수 없이 많아 / 숨을 참고 봐, 더 좋아질 거야'),
                                                   ("I'm like a shooting star, I've come so far / I can't go back to where I used to be",
                                                    '나는 별똥별 같아, 정말 멀리까지 왔어 / 예전의 내가 있던 곳으로 돌아갈 수 없어'),
                                                   ('A whole new world / Every turn a surprise', '완전히 새로운 세상 / 방향을 틀 때마다 놀라움이 있어'),
                                                   ('With new horizons to pursue / Every moment, red-letter', '따라갈 새로운 지평선들이 있고 / 모든 순간이 특별해'),
                                                   ("I'll chase them anywhere, there's time to spare / Let me share this whole new world with you",
                                                    '나는 어디든 그것들을 따라갈 거야, 시간은 충분해 / 이 완전히 새로운 세상을 너와 함께 나누게 해 줘'),
                                                   ('A whole new world / A whole new world', '완전히 새로운 세상 / 완전히 새로운 세상'),
                                                   ("That's where we'll be / That's where we'll be", '그곳이 우리가 있을 곳이야 / 그곳이 우리가 있을 곳이야'),
                                                   ('A thrilling chase / A wondrous place', '짜릿한 모험 / 놀라운 곳'),
                                                   ('For you and me', '너와 나를 위한')],
                                        'quiz': [{'q': '1. 이 노래에서 두 사람은 무엇을 타고 있나요?', 'options': ['기차', '자전거', '배', '마법 양탄자'], 'answer': '마법 양탄자'},
                                                 {'q': '2. 이 노래에서 알라딘은 자스민에게 무엇을 보여 주고 싶어 하나요?',
                                                  'options': ['학교 교실', '시험 문제', '새로운 세상', '휴대전화'],
                                                  'answer': '새로운 세상'},
                                                 {'q': "3. 'A whole new world'가 상징하는 것으로 가장 알맞은 것은 무엇인가요?",
                                                  'options': ['낡은 방', '어려운 시험', '혼자 있는 시간', '새로운 시선과 경험'],
                                                  'answer': '새로운 시선과 경험'},
                                                 {'q': "4. 'I can open your eyes'는 어떤 의미에 가깝나요?",
                                                  'options': ['잠에서 깨우다', '눈을 감게 하다', '새로운 것을 보게 해 주다', '멀리 보내다'],
                                                  'answer': '새로운 것을 보게 해 주다'},
                                                 {'q': "5. 'point of view'의 뜻으로 가장 알맞은 것은 무엇인가요?", 'options': ['문', '속도', '약속', '관점'], 'answer': '관점'},
                                                 {'q': '6. 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?',
                                                  'options': ['후회와 슬픔', '분노와 복수', '설렘과 자유로움', '지루함'],
                                                  'answer': '설렘과 자유로움'},
                                                 {'q': "7. 'I can't go back to where I used to be'는 어떤 의미인가요?",
                                                  'options': ['집에 갈 길을 잃었다', '예전의 모습으로 돌아갈 수 없다', '학교에 다시 가야 한다', '여행을 취소했다'],
                                                  'answer': '예전의 모습으로 돌아갈 수 없다'},
                                                 {'q': '8. 이 노래의 주요 배경으로 가장 알맞은 것은 무엇인가요?',
                                                  'options': ['교실에서 보는 시험', '바닷가에서 하는 운동', '시장 안의 장면', '밤하늘을 나는 마법 양탄자 여행'],
                                                  'answer': '밤하늘을 나는 마법 양탄자 여행'}],
                                        'key_expressions': [('I can show you the world', '내가 너에게 세상을 보여 줄 수 있어'),
                                                            ('Shining, shimmering, splendid', '빛나고 반짝이고 눈부신'),
                                                            ('Let your heart decide', '마음이 결정하게 하다'),
                                                            ('Open your eyes', '눈을 뜨게 하다'),
                                                            ('A whole new world', '완전히 새로운 세상'),
                                                            ('Point of view', '관점'),
                                                            ('No one to tell us no', '아무도 안 된다고 말하지 않음'),
                                                            ('Unbelievable sights', '믿기 어려운 풍경들'),
                                                            ('Indescribable feeling', '말로 표현할 수 없는 감정'),
                                                            ('New horizons to pursue', '따라갈 새로운 지평선들')],
                                        'matching': [('I can show you the world', '내가 너에게 세상을 보여 줄 수 있어'),
                                                     ('A whole new world', '완전히 새로운 세상'),
                                                     ('A new fantastic point of view', '새롭고 환상적인 시선'),
                                                     ("Don't you dare close your eyes", '절대 눈 감지 마'),
                                                     ('Open your eyes', '눈을 떠 봐'),
                                                     ('Every turn a surprise', '방향을 틀 때마다 놀라움이 있어')],
                                        'reflect_questions': ['내가 경험해 보고 싶은 “완전히 새로운 세상”은 무엇인가요?', '누군가가 나에게 새로운 관점을 보여 준 적이 있나요?', '두려움보다 설렘이 더 컸던 경험이 있나요?']},
 '4. Stand By Me - Ben E. King': {'video_url': 'https://www.youtube.com/watch?v=c5hDjpi_HM0',
                                  'bg': '\n'
                                        '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#15803d;">\n'
                                        '        🤝 Stand By Me: 곁에 있어 주는 힘\n'
                                        '    </h3>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        '        <b>Stand By Me</b>는 어둡고 불안한 순간에도\n'
                                        '        누군가가 내 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다.\n'
                                        '        제목의 <b>stand by me</b>는 단순히 “내 옆에 서 있어”라는 뜻을 넘어,\n'
                                        '        “내 곁에 있어 줘”, “나를 지켜 줘”, “함께해 줘”라는 의미로 이해할 수 있습니다.\n'
                                        '    </p>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        '        노래 속 화자는 밤이 찾아오고 세상이 어두워지는 장면을 떠올립니다.\n'
                                        '        하지만 그는 혼자가 아니라는 믿음 때문에 두려워하지 않습니다.\n'
                                        '        달빛만 보이는 어두운 상황, 하늘이 무너지고 산이 바다로 무너져 내리는 듯한\n'
                                        '        극단적인 상황에서도 사랑하는 사람이 곁에 있다면 괜찮다고 말합니다.\n'
                                        '    </p>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        '        이 노래는 어려운 단어가 많지 않고,\n'
                                        "        <b>I won't be afraid</b>, <b>I won't cry</b>, <b>stand by me</b>처럼\n"
                                        '        짧고 반복적인 표현이 많아 학생들이 듣고 따라 부르기에 좋습니다.\n'
                                        '        또한 친구, 가족, 사랑하는 사람의 존재가 주는 안정감과 용기를\n'
                                        '        자연스럽게 이야기해 볼 수 있는 노래입니다.\n'
                                        '    </p>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        "        수업에서는 <b>stand by me</b>, <b>I won't be afraid</b>,\n"
                                        "        <b>I won't cry</b>, <b>shed a tear</b>, <b>whenever you're in trouble</b>\n"
                                        '        같은 표현을 중심으로 배울 수 있습니다.\n'
                                        '        특히 이 노래는 느린 속도와 반복 구조 덕분에\n'
                                        '        기초 학습자도 영어 표현을 소리로 익히기에 적합합니다.\n'
                                        '    </p>\n'
                                        '    ',
                                  'lyrics': [('When the night has come / And the land is dark', '밤이 찾아오고 / 세상이 어두워질 때'),
                                             ("And the moon is the only light we'll see", '달빛만이 우리가 볼 수 있는 유일한 빛일 때'),
                                             ("No, I won't be afraid / Oh, I won't be afraid", '아니, 나는 두려워하지 않을 거야 / 오, 나는 두려워하지 않을 거야'),
                                             ('Just as long as you stand / Stand by me', '네가 곁에 있어 준다면 / 내 곁에 있어 준다면'),
                                             ("So darlin', darlin' / Stand by me, oh, stand by me", '그러니 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘'),
                                             ('Oh, stand, stand by me / Stand by me', '오, 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘'),
                                             ('If the sky that we look upon / Should tumble and fall', '우리가 바라보는 하늘이 / 무너져 내린다 해도'),
                                             ('Or the mountain should crumble to the sea', '산이 부서져 바다로 무너져 내린다 해도'),
                                             ("I won't cry, I won't cry / No, I won't shed a tear", '나는 울지 않을 거야, 울지 않을 거야 / 아니, 눈물 한 방울도 흘리지 않을 거야'),
                                             ('Just as long as you stand / Stand by me', '네가 곁에 있어 준다면 / 내 곁에 있어 준다면'),
                                             ("And darlin', darlin' / Stand by me, oh, stand by me", '그리고 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘'),
                                             ('Oh, stand now, stand by me / Stand by me', '오, 지금 곁에 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘'),
                                             ("Darlin', darlin' / Stand by me, oh, stand by me", '사랑하는 사람아, 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘'),
                                             ('Oh, stand now, stand by me / Stand by me', '오, 지금 곁에 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘'),
                                             ("Whenever you're in trouble / Won't you stand by me?", '네가 힘든 순간에 / 내 곁에 있어 주지 않을래?'),
                                             ("Oh, stand by me / Won't you stand now?", '오, 내 곁에 있어 줘 / 지금 내 곁에 있어 주지 않을래?'),
                                             ('Oh, stand, stand by me', '오, 있어 줘, 내 곁에 있어 줘')],
                                  'quiz': [{'q': '1. 이 노래는 어떤 시간적 배경으로 시작하나요?', 'options': ['아침', '밤', '점심시간', '학교 수업 시간'], 'answer': '밤'},
                                           {'q': '2. 노래에서 보이는 유일한 빛은 무엇인가요?', 'options': ['햇빛', '달빛', '휴대전화 불빛', '촛불'], 'answer': '달빛'},
                                           {'q': '3. 화자는 두려움에 대해 무엇이라고 말하나요?',
                                            'options': ['나는 두려워하지 않을 거야', '나는 항상 두려워', '나는 두려움을 좋아해', '나는 학교가 두려워'],
                                            'answer': '나는 두려워하지 않을 거야'},
                                           {'q': "4. 'Stand by me'의 의미로 가장 알맞은 것은 무엇인가요?",
                                            'options': ['멀리 도망가', '앉아 있어', '집에 가', '내 곁에 있어 줘'],
                                            'answer': '내 곁에 있어 줘'},
                                           {'q': '5. 이 노래의 중심 주제로 가장 알맞은 것은 무엇인가요?',
                                            'options': ['쇼핑', '경쟁', '요리', '함께 있어 주는 힘과 위로'],
                                            'answer': '함께 있어 주는 힘과 위로'},
                                           {'q': '6. 화자가 두려워하지 않는 이유는 무엇인가요?',
                                            'options': ['돈이 많기 때문에', '날씨가 맑기 때문에', '누군가가 곁에 있어 주기 때문에', '잠을 자고 있기 때문에'],
                                            'answer': '누군가가 곁에 있어 주기 때문에'},
                                           {'q': "7. 'I won't shed a tear'의 의미로 가장 알맞은 것은 무엇인가요?",
                                            'options': ['눈물 한 방울도 흘리지 않겠다', '많이 웃겠다', '잠을 자겠다', '멀리 떠나겠다'],
                                            'answer': '눈물 한 방울도 흘리지 않겠다'},
                                           {'q': "8. 'Whenever you're in trouble'은 어떤 뜻인가요?",
                                            'options': ['네가 여행을 갈 때마다', '네가 노래할 때마다', '네가 힘든 순간에는 언제든지', '네가 밥을 먹을 때마다'],
                                            'answer': '네가 힘든 순간에는 언제든지'}],
                                  'key_expressions': [('Stand by me', '내 곁에 있어 줘'),
                                                      ('The night has come', '밤이 찾아왔다'),
                                                      ('The land is dark', '세상이 어둡다'),
                                                      ('The only light', '유일한 빛'),
                                                      ("I won't be afraid", '나는 두려워하지 않을 거야'),
                                                      ('Just as long as', '~하는 한'),
                                                      ('Tumble and fall', '무너져 내리다'),
                                                      ('Crumble to the sea', '바다로 무너져 내리다'),
                                                      ("I won't shed a tear", '눈물 한 방울도 흘리지 않을 거야'),
                                                      ("Whenever you're in trouble", '네가 힘든 순간에는 언제든지')],
                                  'matching': [('Stand by me', '내 곁에 있어 줘'),
                                               ("I won't be afraid", '나는 두려워하지 않을 거야'),
                                               ("I won't cry", '나는 울지 않을 거야'),
                                               ("Whenever you're in trouble", '네가 힘든 순간에는 언제든지'),
                                               ('The land is dark', '세상이 어두워'),
                                               ('The moon is the only light', '달빛만이 유일한 빛이야')],
                                  'reflect_questions': ['내가 힘들 때 곁에 있어 주었던 사람은 누구인가요?', '누군가에게 “내 곁에 있어 줘”라고 말하고 싶었던 순간이 있나요?', '나도 누군가에게 힘이 되어 준 경험이 있나요?']},
 "5. Don't Know Why - Norah Jones": {'video_url': 'https://www.youtube.com/watch?v=nhLdJeLTM48',
                                     'bg': '\n'
                                           '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#7c3aed;">\n'
                                           "        🌙 Don't Know Why: 이유를 알 수 없는 마음\n"
                                           '    </h3>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           "        <b>Don't Know Why</b>는 Norah Jones의 대표곡으로,\n"
                                           '        조용하고 부드러운 멜로디 속에 설명하기 어려운 아쉬움과 후회를 담고 있는 노래입니다.\n'
                                           '        노래 속 화자는 누군가에게 가지 않았던 자신의 행동을 떠올리며,\n'
                                           '        왜 그렇게 했는지 스스로도 알 수 없다고 말합니다.\n'
                                           '    </p>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           '        이 노래는 큰 사건을 직접적으로 설명하기보다,\n'
                                           '        마음속에 남아 있는 감정의 흔적을 천천히 보여 줍니다.\n'
                                           '        해가 뜰 때까지 기다렸지만 결국 가지 못했고,\n'
                                           '        새벽이 밝아오는 순간에는 차라리 멀리 날아가 버리고 싶어 합니다.\n'
                                           '        그래서 이 노래에는 후회, 망설임, 외로움, 그리움이 조용하게 섞여 있습니다.\n'
                                           '    </p>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           "        특히 <b>I don't know why I didn't come</b>이라는 문장이 반복되면서,\n"
                                           '        화자가 자신의 마음을 명확히 설명하지 못하는 상태가 잘 드러납니다.\n'
                                           '        이 반복 표현은 학생들이 듣고 따라 말하기 좋고,\n'
                                           "        <b>I don't know why</b>, <b>I wished that I could</b>,\n"
                                           '        <b>on my mind</b>, <b>empty as a drum</b> 같은 표현을 배우기에도 좋습니다.\n'
                                           '    </p>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           '        수업에서는 이 노래를 통해 느린 영어 발음, 감정 표현,\n'
                                           '        후회와 그리움을 나타내는 문장을 함께 배울 수 있습니다.\n'
                                           '        속도가 빠르지 않고 분위기가 차분해서,\n'
                                           '        학생들이 영어 소리를 듣고 가사의 의미를 천천히 따라가기에 적합합니다.\n'
                                           '    </p>\n'
                                           '    ',
                                     'lyrics': [("I waited 'til I saw the sun / I don't know why I didn't come", '나는 해가 보일 때까지 기다렸어 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("I left you by the house of fun / Don't know why I didn't come", '나는 너를 즐거움의 집 곁에 남겨 두었어 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("Don't know why I didn't come", '왜 내가 가지 않았는지 모르겠어'),
                                                ('When I saw the break of day / I wished that I could fly away', '새벽이 밝아오는 것을 보았을 때 / 나는 날아가 버릴 수 있기를 바랐어'),
                                                ('Instead of kneeling in the sand / Catching tear-drops in my hand', '모래 위에 무릎 꿇고 있는 대신 / 손으로 눈물방울을 받으며'),
                                                ("My heart is drenched in wine / But you'll be on my mind forever",
                                                 '내 마음은 와인에 흠뻑 젖어 있지만 / 너는 영원히 내 마음속에 있을 거야'),
                                                ('Out across the endless sea / I would die in ecstasy', '끝없는 바다 저편으로 / 나는 황홀함 속에서 죽을 수도 있을 것 같아'),
                                                ("But I'll be a bag of bones / Driving down the road alone", '하지만 나는 뼈만 남은 사람처럼 / 혼자 길을 따라 운전하게 되겠지'),
                                                ("My heart is drenched in wine / But you'll be on my mind forever",
                                                 '내 마음은 와인에 흠뻑 젖어 있지만 / 너는 영원히 내 마음속에 있을 거야'),
                                                ("Something has to make you run / I don't know why I didn't come", '무언가가 너를 떠나게 만들었겠지 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("I feel as empty as a drum / I don't know why I didn't come", '나는 북처럼 텅 빈 기분이야 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("Don't know why I didn't come / I don't know why I didn't come", '왜 내가 가지 않았는지 모르겠어 / 왜 내가 가지 않았는지 모르겠어')],
                                     'quiz': [{'q': '1. 화자는 무엇을 볼 때까지 기다렸나요?', 'options': ['버스', '해', '선생님', '전화'], 'answer': '해'},
                                              {'q': '2. 화자가 계속 모르겠다고 말하는 것은 무엇인가요?',
                                               'options': ['무엇을 먹을지', '학교가 어디인지', '왜 자신이 가지 않았는지', '어떻게 읽는지'],
                                               'answer': '왜 자신이 가지 않았는지'},
                                              {'q': "3. 'break of day'의 뜻으로 가장 알맞은 것은 무엇인가요?", 'options': ['한밤중', '점심시간', '새벽', '겨울'], 'answer': '새벽'},
                                              {'q': '4. 화자는 새벽을 보았을 때 무엇을 바랐나요?',
                                               'options': ['일찍 자는 것', '차를 사는 것', '수학을 공부하는 것', '날아가 버리는 것'],
                                               'answer': '날아가 버리는 것'},
                                              {'q': '5. 이 노래의 분위기로 가장 알맞은 것은 무엇인가요?',
                                               'options': ['조용하고 후회스러운 분위기', '화나고 시끄러운 분위기', '빠르고 웃긴 분위기', '신나고 거친 분위기'],
                                               'answer': '조용하고 후회스러운 분위기'},
                                              {'q': "6. 'You'll be on my mind forever'는 어떤 의미인가요?",
                                               'options': ['너는 곧 잊혀질 거야', '너는 영원히 내 마음속에 있을 거야', '너는 나와 함께 여행할 거야', '너는 노래를 부를 거야'],
                                               'answer': '너는 영원히 내 마음속에 있을 거야'},
                                              {'q': "7. 'I feel as empty as a drum'은 어떤 감정에 가깝나요?", 'options': ['배부름', '자신감', '공허함', '분노'], 'answer': '공허함'},
                                              {'q': '8. 이 노래에서 반복되는 핵심 문장은 무엇인가요?',
                                               'options': ['Stand by me', 'Let it go', 'A whole new world', "I don't know why I didn't come"],
                                               'answer': "I don't know why I didn't come"}],
                                     'key_expressions': [("I don't know why", '나는 왜 그런지 모르겠어'),
                                                         ("I didn't come", '나는 가지 않았어'),
                                                         ('The break of day', '새벽'),
                                                         ('I wished that I could fly away', '나는 날아가 버릴 수 있기를 바랐어'),
                                                         ('Tear-drops', '눈물방울'),
                                                         ('On my mind', '마음속에 있는'),
                                                         ('Forever', '영원히'),
                                                         ('Endless sea', '끝없는 바다'),
                                                         ('Driving down the road alone', '혼자 길을 따라 운전하며'),
                                                         ('Empty as a drum', '북처럼 텅 빈')],
                                     'matching': [("I don't know why", '나는 왜 그런지 모르겠어'),
                                                  ('I wished that I could fly away', '나는 날아가 버릴 수 있기를 바랐어'),
                                                  ("You'll be on my mind forever", '너는 영원히 내 마음속에 있을 거야'),
                                                  ('I feel as empty as a drum', '나는 북처럼 텅 빈 기분이야'),
                                                  ('I waited till I saw the sun', '나는 해가 보일 때까지 기다렸어'),
                                                  ('Driving down the road alone', '혼자 길을 따라 운전하며')],
                                     'reflect_questions': ['왜 그랬는지 스스로도 잘 설명할 수 없는 선택을 한 적이 있나요?',
                                                           '마음속에 오래 남아 있는 사람이나 기억이 있나요?',
                                                           '후회가 남는 일을 지금 다시 바라본다면 어떤 생각이 드나요?']},
 '6. Fix You - Coldplay': {'video_url': 'https://www.youtube.com/watch?v=Z0IZ3MjGFEo',
                           'bg': '\n'
                                 '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#2563eb;">\n'
                                 '        💡 Fix You: 힘든 순간에 건네는 위로\n'
                                 '    </h3>\n'
                                 '\n'
                                 '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                 '        Coldplay의 <b>Fix You</b>는 실패, 상실, 지침, 슬픔을 겪는 사람에게\n'
                                 '        따뜻한 위로를 건네는 노래입니다. 노래 속 화자는 상대가 최선을 다했지만\n'
                                 '        원하는 결과를 얻지 못했을 때, 그리고 잃어버린 것을 되돌릴 수 없을 때의\n'
                                 '        아픔을 조용히 바라봅니다.\n'
                                 '    </p>\n'
                                 '\n'
                                 '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                 '        이 노래에서 반복되는 <b>Lights will guide you home</b>은\n'
                                 '        어두운 순간에도 길을 비춰 주는 희망을 상징합니다.\n'
                                 '        또한 <b>I will try to fix you</b>는 상대를 완벽하게 고쳐 주겠다는 뜻이라기보다,\n'
                                 '        힘든 시간을 혼자 견디지 않도록 곁에서 도와주고 싶다는 마음으로 이해할 수 있습니다.\n'
                                 '    </p>\n'
                                 '\n'
                                 '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                 "        수업에서는 <b>try your best</b>, <b>don't succeed</b>,\n"
                                 '        <b>what you want / what you need</b>, <b>stuck in reverse</b>,\n'
                                 '        <b>learn from my mistakes</b> 같은 표현을 중심으로 배울 수 있습니다.\n'
                                 '        특히 이 노래는 속도가 비교적 느리고 감정선이 분명해서,\n'
                                 '        학생들이 영어 표현과 함께 위로, 희망, 회복의 의미를 이해하기에 좋습니다.\n'
                                 '    </p>\n'
                                 '    ',
                           'lyrics': [("When you try your best, but you don't succeed / When you get what you want, but not what you need",
                                       '네가 최선을 다했지만 성공하지 못할 때 / 원하는 것을 얻었지만 정작 필요한 것은 얻지 못할 때'),
                                      ("When you feel so tired, but you can't sleep / Stuck in reverse", '너무 지쳤지만 잠들 수 없을 때 / 거꾸로 갇혀 있는 것처럼 느껴질 때'),
                                      ("And the tears come streaming down your face / When you lose something you can't replace",
                                       '눈물이 네 얼굴을 타고 흘러내릴 때 / 대신할 수 없는 무언가를 잃었을 때'),
                                      ('When you love someone, but it goes to waste / Could it be worse?', '누군가를 사랑했지만 그 마음이 헛되어 버렸을 때 / 이보다 더 나쁠 수 있을까?'),
                                      ('Lights will guide you home / And ignite your bones', '빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야'),
                                      ('And I will try to fix you', '그리고 나는 너를 다시 일으켜 주려고 노력할 거야'),
                                      ("And high up above or down below / When you're too in love to let it go", '저 높은 곳에 있든 아주 낮은 곳에 있든 / 너무 사랑해서 놓아주기 어려울 때'),
                                      ("But if you never try, you'll never know / Just what you're worth", '하지만 시도하지 않으면 절대 알 수 없어 / 네가 얼마나 소중한 사람인지'),
                                      ('Lights will guide you home / And ignite your bones', '빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야'),
                                      ('And I will try to fix you', '그리고 나는 너를 다시 일으켜 주려고 노력할 거야'),
                                      ('Tears stream down your face / When you lose something you cannot replace', '눈물이 네 얼굴을 타고 흘러내려 / 대신할 수 없는 무언가를 잃었을 때'),
                                      ('Tears stream down your face, and I / Tears stream down your face', '눈물이 네 얼굴을 타고 흘러내리고, 나는 / 눈물이 네 얼굴을 타고 흘러내려'),
                                      ('I promise you I will learn from my mistakes / Tears stream down your face, and I',
                                       '나는 내 실수에서 배우겠다고 약속할게 / 눈물이 네 얼굴을 타고 흘러내리고, 나는'),
                                      ('Lights will guide you home / And ignite your bones', '빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야'),
                                      ('And I will try to fix you', '그리고 나는 너를 다시 일으켜 주려고 노력할 거야')],
                           'quiz': [{'q': '1. 이 노래에서 화자는 어떤 사람을 위로하고 있나요?',
                                     'options': ['시험을 준비하는 사람', '여행을 떠나는 사람', '힘들고 지친 사람', '운동을 시작한 사람'],
                                     'answer': '힘들고 지친 사람'},
                                    {'q': "2. 'When you try your best, but you don't succeed'의 의미로 가장 알맞은 것은 무엇인가요?",
                                     'options': ['최선을 다했지만 성공하지 못할 때', '아무 노력도 하지 않았을 때', '원하는 것을 모두 얻었을 때', '잠을 충분히 잤을 때'],
                                     'answer': '최선을 다했지만 성공하지 못할 때'},
                                    {'q': "3. 'what you want'와 'what you need'의 차이로 알맞은 것은 무엇인가요?",
                                     'options': ['둘 다 항상 같은 뜻이다', 'want는 원하는 것, need는 정말 필요한 것이다', 'want는 먹는 것, need는 노래하는 것이다', 'need는 필요 없는 것이다'],
                                     'answer': 'want는 원하는 것, need는 정말 필요한 것이다'},
                                    {'q': "4. 'Lights will guide you home'은 무엇을 상징한다고 볼 수 있나요?",
                                     'options': ['휴대전화 불빛', '가게의 간판', '어두운 길에서의 희망과 방향', '자동차 헤드라이트만'],
                                     'answer': '어두운 길에서의 희망과 방향'},
                                    {'q': "5. 'If you never try, you'll never know'의 의미로 가장 알맞은 것은 무엇인가요?",
                                     'options': ['절대 시도하면 안 된다', '시도하지 않으면 알 수 없다', '모든 것을 이미 알고 있다', '실패하면 끝이다'],
                                     'answer': '시도하지 않으면 알 수 없다'},
                                    {'q': "6. 'I will learn from my mistakes'는 어떤 태도를 보여 주나요?",
                                     'options': ['실수를 숨기려는 태도', '남을 탓하려는 태도', '포기하려는 태도', '실수에서 배우려는 태도'],
                                     'answer': '실수에서 배우려는 태도'},
                                    {'q': '7. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?', 'options': ['위로와 희망', '웃음과 장난', '분노와 복수', '경쟁과 승리'], 'answer': '위로와 희망'},
                                    {'q': "8. 'I will try to fix you'는 어떤 의미에 가깝나요?",
                                     'options': ['너를 혼내겠다', '너를 완전히 바꾸겠다', '너를 떠나겠다', '너를 도와 다시 일어서게 하고 싶다'],
                                     'answer': '너를 도와 다시 일어서게 하고 싶다'}],
                           'key_expressions': [('Try your best', '최선을 다하다'),
                                               ("Don't succeed", '성공하지 못하다'),
                                               ('What you want', '네가 원하는 것'),
                                               ('What you need', '네게 필요한 것'),
                                               ('Stuck in reverse', '거꾸로 갇힌 듯한'),
                                               ('Tears stream down your face', '눈물이 얼굴을 타고 흐르다'),
                                               ("You can't replace", '대신할 수 없다'),
                                               ('Lights will guide you home', '빛이 너를 집으로 인도할 거야'),
                                               ('Ignite your bones', '네 안의 힘을 다시 밝혀 주다'),
                                               ('Learn from my mistakes', '내 실수에서 배우다')],
                           'matching': [('When you try your best', '네가 최선을 다할 때'),
                                        ('Lights will guide you home', '빛이 너를 집으로 인도할 거야'),
                                        ('I will try to fix you', '나는 너를 다시 일으켜 주려고 노력할 거야'),
                                        ("If you never try, you'll never know", '시도하지 않으면 절대 알 수 없어'),
                                        ('Tears stream down your face', '눈물이 네 얼굴을 타고 흘러내려'),
                                        ('I will learn from my mistakes', '나는 내 실수에서 배울 거야')],
                           'reflect_questions': ['최선을 다했지만 원하는 결과를 얻지 못했던 경험이 있나요?', '힘들 때 나를 다시 일으켜 준 사람이나 말이 있었나요?', '나도 누군가를 위로하거나 도와주고 싶었던 적이 있나요?']},
 '7. The Scientist - Coldplay': {'video_url': 'https://www.youtube.com/watch?v=kV82ahVRPFg&list=RDkV82ahVRPFg&start_radio=1',
                                 'bg': '<h3 style="font-size:2.2rem; margin-bottom:20px; color:#2563eb;">🔬 The Scientist: 처음으로 돌아가고 싶은 마음</h3>\n'
                                       '<p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">Coldplay의 <b>The Scientist</b>는 지나간 관계와 후회를 돌아보며, 처음으로 '
                                       '돌아가 다시 말하고 싶은 마음을 담은 노래입니다.</p>\n'
                                       '<p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">노래 속 화자는 사랑과 이별을 과학처럼 분석하려 하지만, 마음은 숫자와 공식처럼 쉽게 설명되지 '
                                       '않는다는 것을 깨닫습니다.</p>',
                                 'lyrics': [
    ("Come up to meet you, tell you I′m sorry", "너를 만나러 와서 미안하다고 말하려 해"),
    ("You don't know how lovely you are", "너는 네가 얼마나 사랑스러운지 몰라"),
    ("I had to find you, tell you I need you", "나는 너를 찾아야 했고, 네가 필요하다고 말해야 했어"),
    ("Tell you I set you apart", "네가 나에게 특별하다고 말해야 했어"),
    ("Tell me your secrets and ask me your questions", "네 비밀을 말해 주고, 내게 질문을 해 줘"),
    ("Oh, let′s go back to the start", "오, 처음으로 돌아가자"),
    ("Runnin' in circles, comin' up tails", "빙빙 돌며, 계속 좋지 않은 결과가 나오고 있어"),
    ("Heads on a science apart", "머리는 과학처럼 따로 떨어져 있어"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("It′s such a shame for us to part", "우리가 헤어진다는 건 정말 안타까운 일이야"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("No one ever said it would be this hard", "아무도 이렇게 힘들 거라고 말하지 않았어"),
    ("Oh, take me back to the start", "오, 나를 처음으로 데려가 줘"),
    ("I was just guessing at numbers and figures", "나는 그저 숫자와 수치를 추측하고 있었어"),
    ("Pulling the puzzles apart", "퍼즐을 하나하나 떼어 내며"),
    ("Questions of science, science and progress", "과학의 질문들, 과학과 진보는"),
    ("Do not speak as loud as my heart", "내 마음만큼 크게 말하지 못해"),
    ("But tell me you love me, come back and haunt me", "하지만 나를 사랑한다고 말해 줘, 돌아와 나를 계속 맴돌아 줘"),
    ("Oh, and I rush to the start", "오, 나는 서둘러 처음으로 돌아가"),
    ("Runnin′ in circles, chasin' our tails", "빙빙 돌며, 우리의 꼬리를 쫓듯 같은 자리를 맴돌아"),
    ("Coming back as we are", "있는 그대로의 우리로 돌아오며"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("Oh, it′s such a shame for us to part", "오, 우리가 헤어진다는 건 정말 안타까운 일이야"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("No one ever said it would be so hard", "아무도 이렇게 힘들 거라고 말하지 않았어"),
    ("I'm going back to the start", "나는 처음으로 돌아가고 있어"),
],
                                 'quiz': [{'q': '1. 화자가 상대에게 가장 먼저 말하고 싶은 것은 무엇인가요?',
                                           'options': ['미안하다는 말', '축하한다는 말', '화났다는 말', '떠나자는 말'],
                                           'answer': '미안하다는 말'},
                                          {'q': "2. “You don't know how lovely you are”의 의미는 무엇인가요?",
                                           'options': ['너는 네가 얼마나 사랑스러운지 모른다', '너는 나를 전혀 모른다', '너는 과학을 좋아한다', '너는 돌아오지 않는다'],
                                           'answer': '너는 네가 얼마나 사랑스러운지 모른다'},
                                          {'q': "3. “Let's go back to the start”의 의미는 무엇인가요?",
                                           'options': ['처음으로 돌아가자', '학교로 가자', '과학을 공부하자', '집에 가자'],
                                           'answer': '처음으로 돌아가자'},
                                          {'q': '4. “Running in circles”는 어떤 상태를 나타내나요?',
                                           'options': ['같은 자리를 맴도는 상태', '빠르게 성공하는 상태', '잠을 자는 상태', '완전히 잊은 상태'],
                                           'answer': '같은 자리를 맴도는 상태'},
                                          {'q': '5. “Nobody said it was easy”의 의미는 무엇인가요?',
                                           'options': ['아무도 쉽다고 말하지 않았다', '모두 쉽다고 말했다', '과학은 쉽다', '사랑은 항상 쉽다'],
                                           'answer': '아무도 쉽다고 말하지 않았다'},
                                          {'q': '6. “Do not speak as loud as my heart”는 어떤 뜻에 가깝나요?',
                                           'options': ['이성과 과학보다 마음의 소리가 더 크다', '심장이 실제로 소리를 낸다', '과학이 가장 중요하다', '말을 하지 말라는 뜻이다'],
                                           'answer': '이성과 과학보다 마음의 소리가 더 크다'},
                                          {'q': '7. 화자가 반복해서 돌아가고 싶어 하는 곳은 어디인가요?', 'options': ['처음', '학교', '바다', '무대'], 'answer': '처음'},
                                          {'q': '8. 이 노래의 중심 감정은 무엇인가요?', 'options': ['후회와 그리움', '분노와 복수', '승리와 환호', '웃음과 장난'], 'answer': '후회와 그리움'}],
                                 'key_expressions': [("Tell you I'm sorry", '미안하다고 말하다'),
                                                     ('How lovely you are', '네가 얼마나 사랑스러운지'),
                                                     ('I had to find you', '나는 너를 찾아야 했어'),
                                                     ('I need you', '네가 필요해'),
                                                     ('I set you apart', '나는 너를 특별하게 여겨'),
                                                     ('Tell me your secrets', '네 비밀을 말해 줘'),
                                                     ("Let's go back to the start", '처음으로 돌아가자'),
                                                     ('Running in circles', '빙빙 돌다'),
                                                     ('Nobody said it was easy', '아무도 그것이 쉽다고 말하지 않았어'),
                                                     ('Take me back to the start', '나를 처음으로 데려가 줘')],
                                 'matching': [("Tell you I'm sorry", '미안하다고 말하다'),
                                              ("You don't know how lovely you are", '너는 네가 얼마나 사랑스러운지 몰라'),
                                              ('Tell you I need you', '네가 필요하다고 말하다'),
                                              ("Let's go back to the start", '처음으로 돌아가자'),
                                              ('Nobody said it was easy', '아무도 그것이 쉽다고 말하지 않았어'),
                                              ("I'm going back to the start", '나는 처음으로 돌아가고 있어')],
                                 'reflect_questions': ['당신도 가수처럼 그리운 옛 연인이나 다시 이야기하고 싶은 사람이 있나요?',
                                                       '처음으로 돌아갈 수 있다면 다시 말하고 싶은 말은 무엇인가요?',
                                                       '사랑이나 관계가 생각보다 쉽지 않았다고 느낀 경험이 있나요?']}}


BACKGROUND_CONTENT = {
    "1. Let It Go - Frozen OST": {
        "title": "❄️ Let It Go: 숨겨 왔던 자신을 받아들이는 순간",
        "paragraphs": [
            "Let It Go는 영화 Frozen의 대표곡으로, 엘사가 더 이상 자신의 능력과 감정을 숨기지 않고 스스로를 받아들이는 장면에서 나오는 노래입니다. 엘사는 왕국의 공주이지만, 자신의 얼음 마법이 다른 사람을 다치게 할 수 있다는 두려움 때문에 늘 조심하며 살아왔습니다.",
            "어릴 때부터 엘사는 감정을 숨기고, 능력을 감추고, ‘착한 아이’처럼 행동해야 한다는 압박을 받았습니다. 하지만 대관식 날 능력이 사람들 앞에서 드러나자, 사람들은 엘사를 이해하기보다 두려워합니다. 결국 엘사는 모든 시선과 책임을 피해 눈 덮인 산으로 도망칩니다.",
            "산 위에서 엘사는 처음으로 자신의 진짜 모습을 마주합니다. 이 노래는 단순히 ‘다 잊어버리자’는 의미가 아니라, 그동안 억눌렀던 두려움, 책임감, 타인의 시선에서 벗어나 자기 자신을 받아들이는 과정을 보여 줍니다.",
            "수업에서는 let it go, conceal, hold back, storm inside, I'm free, the past is in the past 같은 표현을 중심으로 배울 수 있습니다. 특히 이 노래는 자유, 두려움, 자기표현, 자신감에 대해 학생들과 이야기하기 좋은 자료입니다."
        ],
    },
    "2. Hello - Adele": {
        "title": "☎️ Hello: 과거의 누군가에게 건네는 늦은 안부",
        "paragraphs": [
            "Adele의 Hello는 시간이 많이 흐른 뒤, 과거의 누군가에게 다시 연락하고 싶은 마음을 담은 노래입니다. 노래 속 화자는 상대에게 전화를 걸며 오래전의 관계, 미안함, 후회, 그리고 아직 완전히 치유되지 않은 감정을 떠올립니다.",
            "이 노래에서 화자는 단순히 ‘안녕’이라고 말하는 것이 아닙니다. 과거에 하지 못했던 사과를 조심스럽게 꺼내고 싶어 합니다. 하지만 두 사람 사이에는 시간의 거리, 마음의 거리, 그리고 실제 거리까지 생겨 있습니다.",
            "반복되는 Hello라는 말은 인사이면서 동시에 사과의 시작처럼 들립니다. 화자는 내가 너무 늦은 것은 아닐까, 상대는 이미 괜찮아진 것은 아닐까 생각하면서도, 적어도 자신은 말하려고 노력했다고 고백합니다.",
            "수업에서는 I'm sorry, I tried, after all these years, used to be, the other side 같은 표현을 중심으로 배울 수 있습니다. 학생들은 이 노래를 통해 사과, 후회, 시간의 흐름, 그리고 관계의 거리감을 영어 표현과 함께 이해할 수 있습니다."
        ],
    },
    "3. A Whole New World - Aladdin OST": {
        "title": "🕌 A Whole New World: 새로운 세상을 바라보는 순간",
        "paragraphs": [
            "A Whole New World는 영화 Aladdin의 대표곡으로, 알라딘과 자스민이 마법 양탄자를 타고 밤하늘을 날며 새로운 세상을 바라보는 장면에서 나오는 노래입니다. 이 장면은 단순한 낭만적인 비행이 아니라, 자스민이 처음으로 궁전 밖의 세상을 직접 경험하는 순간입니다.",
            "자스민은 공주로서 화려한 삶을 살지만, 정해진 규칙과 역할 속에서 자유롭게 세상을 경험하지 못했습니다. 알라딘은 그런 자스민에게 궁전 밖의 넓은 세상과 새로운 가능성을 보여 줍니다.",
            "이 노래에서 a whole new world는 새로운 장소만을 뜻하지 않습니다. 새로운 시선, 새로운 경험, 그리고 스스로 선택할 수 있는 자유를 의미합니다. 두 사람은 두려움보다 설렘이 더 큰 세계로 함께 나아갑니다.",
            "수업에서는 I can show you the world, open your eyes, point of view, crystal clear, new horizons 같은 표현을 중심으로 배울 수 있습니다. 학생들에게 ‘내가 경험해 보고 싶은 새로운 세상’이나 ‘나에게 새로운 관점을 보여 준 사람’을 생각하게 할 수 있습니다."
        ],
    },
    "4. Stand By Me - Ben E. King": {
        "title": "🤝 Stand By Me: 곁에 있어 주는 힘",
        "paragraphs": [
            "Stand By Me는 어둡고 불안한 순간에도 누군가가 내 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다. 제목의 stand by me는 단순히 ‘내 옆에 서 있어’가 아니라, ‘내 곁에 있어 줘’, ‘나를 지켜 줘’, ‘함께해 줘’라는 의미로 이해할 수 있습니다.",
            "노래는 밤이 찾아오고 세상이 어두워지는 장면으로 시작합니다. 달빛만 보이는 상황은 불안과 두려움을 상징하지만, 화자는 혼자가 아니라는 믿음 때문에 두려워하지 않겠다고 말합니다.",
            "하늘이 무너지고 산이 바다로 무너져 내리는 듯한 극단적인 표현은 삶에서 마주할 수 있는 큰 어려움을 나타냅니다. 하지만 사랑하는 사람이 곁에 있다면 그 모든 상황도 견딜 수 있다고 노래합니다.",
            "수업에서는 I won't be afraid, I won't cry, shed a tear, whenever you're in trouble 같은 표현을 중심으로 배울 수 있습니다. 친구, 가족, 사랑하는 사람이 주는 안정감과 용기를 이야기하기에 좋은 노래입니다."
        ],
    },
    "5. Don't Know Why - Norah Jones": {
        "title": "🌙 Don't Know Why: 이유를 알 수 없는 마음",
        "paragraphs": [
            "Don't Know Why는 Norah Jones의 대표곡으로, 조용하고 부드러운 멜로디 속에 설명하기 어려운 아쉬움과 후회를 담고 있는 노래입니다. 노래 속 화자는 누군가에게 가지 않았던 자신의 행동을 떠올리며, 왜 그렇게 했는지 스스로도 알 수 없다고 말합니다.",
            "이 노래는 큰 사건을 직접적으로 설명하지 않습니다. 대신 마음속에 남아 있는 감정의 흔적을 천천히 보여 줍니다. 해가 뜰 때까지 기다렸지만 결국 가지 못했고, 새벽이 밝아오는 순간에는 차라리 멀리 날아가 버리고 싶어 합니다.",
            "I don't know why I didn't come이라는 문장이 반복되면서, 화자가 자신의 마음을 명확히 설명하지 못하는 상태가 잘 드러납니다. 이 반복 속에는 후회, 망설임, 외로움, 그리움이 조용하게 섞여 있습니다.",
            "수업에서는 I don't know why, I wished that I could, on my mind, empty as a drum 같은 표현을 중심으로 배울 수 있습니다. 학생들이 이유를 설명하기 어려운 감정과 후회를 영어로 표현해 보는 활동으로 연결하기 좋습니다."
        ],
    },
    "6. Fix You - Coldplay": {
        "title": "💡 Fix You: 힘든 순간에 건네는 위로",
        "paragraphs": [
            "Coldplay의 Fix You는 실패, 상실, 지침, 슬픔을 겪는 사람에게 따뜻한 위로를 건네는 노래입니다. 노래 속 화자는 상대가 최선을 다했지만 원하는 결과를 얻지 못했을 때, 그리고 잃어버린 것을 되돌릴 수 없을 때의 아픔을 조용히 바라봅니다.",
            "반복되는 Lights will guide you home은 어두운 순간에도 길을 비춰 주는 희망을 상징합니다. 또한 I will try to fix you는 상대를 완벽하게 고쳐 주겠다는 뜻이라기보다, 힘든 시간을 혼자 견디지 않도록 곁에서 도와주고 싶다는 마음으로 이해할 수 있습니다.",
            "이 노래는 실패를 부끄러운 것으로만 보지 않습니다. 오히려 실수에서 배우고, 무너진 자리에서 다시 일어설 수 있다는 가능성을 보여 줍니다. 그래서 이 노래는 위로와 회복의 메시지를 전달합니다.",
            "수업에서는 try your best, don't succeed, what you want / what you need, stuck in reverse, learn from my mistakes 같은 표현을 중심으로 배울 수 있습니다. 학생들에게 ‘나를 다시 일으켜 준 사람’이나 ‘내가 누군가에게 해 줄 수 있는 위로’를 생각하게 할 수 있습니다."
        ],
    },
    "7. The Scientist - Coldplay": {
        "title": "🔬 The Scientist: 처음으로 돌아가고 싶은 마음",
        "paragraphs": [
            "Coldplay의 The Scientist는 지나간 관계와 후회를 돌아보며, 처음으로 돌아가 다시 말하고 싶은 마음을 담은 노래입니다. 노래 속 화자는 사랑과 이별을 과학처럼 분석하려 하지만, 마음은 숫자와 공식처럼 쉽게 설명되지 않는다는 것을 깨닫습니다.",
            "Come up to meet you, tell you I'm sorry는 상대를 다시 만나 사과하고 싶은 마음을 보여 줍니다. Tell you I need you, Tell you I set you apart는 상대가 자신에게 얼마나 특별한 존재였는지를 뒤늦게 깨닫는 표현입니다.",
            "반복되는 Let's go back to the start와 Take me back to the start는 단순히 과거로 돌아가고 싶다는 뜻을 넘어, 관계가 어긋나기 전의 순수한 순간으로 돌아가고 싶은 마음을 나타냅니다. 이 노래의 핵심 감정은 후회, 그리움, 미안함, 그리고 다시 시작하고 싶은 마음입니다.",
            "수업에서는 tell you I'm sorry, I need you, set you apart, go back to the start, nobody said it was easy 같은 표현을 중심으로 배울 수 있습니다. 또한 ‘다시 돌아가고 싶은 순간’, ‘그때 하지 못한 말’, ‘관계가 왜 생각보다 어려운가’를 주제로 reflective writing을 하기에 좋습니다."
        ],
    },
}


def show_background(song_choice, data):
    """배경 학습 탭만 HTML/컴포넌트 없이 안정적으로 크게 출력합니다."""
    bg = BACKGROUND_CONTENT.get(song_choice)
    if bg is None:
        bg = {
            "title": "🎵 배경 학습",
            "paragraphs": [str(data.get("bg", "")).replace("<br>", " ").replace("<p>", "").replace("</p>", "")]
        }

    st.markdown('<div class="bg-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="bg-title">{bg["title"]}</div>', unsafe_allow_html=True)
    for p in bg["paragraphs"]:
        st.markdown(f'<div class="bg-p">{p}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


if "selected_song" not in st.session_state:
    st.session_state.selected_song = list(SONGS.keys())[0]
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"

def sync_song():
    for k in list(st.session_state.keys()):
        if k.startswith(("quiz_", "keygame_", "match_", "reflect_")):
            del st.session_state[k]

st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
song_options = list(SONGS.keys())
song_choice = st.selectbox("👉 학습할 노래를 선택하세요", song_options, index=song_options.index(st.session_state.selected_song) if st.session_state.selected_song in song_options else 0, on_change=sync_song, key="song_selector")
st.session_state.selected_song = song_choice
data = SONGS[song_choice]

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "📝 Key Expression 뜻 맞추기", "🧩 문장 매칭 게임", "✍️ 생각 적기"]
selected_tab = st.radio("학습 단계", tabs_list, horizontal=True, key="current_tab")

if selected_tab == "🎬 배경 학습":
    show_background(song_choice, data)
    st.video(data["video_url"])
    st.markdown(
        """
        <div class="game-card">
            <div class="big-guide">
            노래를 듣기 전에 배경을 먼저 읽고, 화자의 감정과 상황을 생각해 보세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


elif selected_tab == "📖 가사 & 퀴즈":
    st.subheader("🎬 노래 영상")
    st.video(data["video_url"])
    st.markdown("---")
    st.subheader("📖 전체 가사와 한국어 해석")
    for en, ko in data["lyrics"]:
        st.markdown(f"""
        <div class="lyrics-container">
            <div class="eng-line">{clean_text_for_display(en)}</div>
            <div class="kor-sub">{clean_text_for_display(ko)}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("✅ 내용 이해 문제 8문항")
    st.markdown('<div class="quiz-box"><b>전체 가사를 읽은 뒤 문제를 풀어 봅시다.</b><br>화자의 상황, 감정, 반복되는 표현을 중심으로 생각하면 됩니다.</div>', unsafe_allow_html=True)
    quiz_key = safe_key(song_choice)
    user_answers = []
    for i, item in enumerate(data["quiz"], start=1):
        q = item["q"]
        q_text = q if str(q).strip().startswith(str(i)) else f"{i}. {q}"
        options = shuffle_options(item["options"], seed=f"{quiz_key}_quiz_{i}")
        picked = st.radio(q_text, options, key=f"quiz_{quiz_key}_{i}", index=None)
        user_answers.append((q_text, picked, item["answer"]))
    c1, c2 = st.columns(2)
    with c1:
        submit_quiz = st.button("정답 확인", key=f"quiz_submit_{quiz_key}", use_container_width=True)
    with c2:
        if st.button("다시 풀기", key=f"quiz_reset_{quiz_key}", use_container_width=True):
            for k in list(st.session_state.keys()):
                if k.startswith(f"quiz_{quiz_key}_"):
                    del st.session_state[k]
            st.rerun()
    if submit_quiz:
        score = sum(1 for _, picked, answer in user_answers if picked == answer)
        st.markdown(f'<div class="score-box">점수: {score} / {len(user_answers)}</div>', unsafe_allow_html=True)
        for idx, (_, picked, answer) in enumerate(user_answers, start=1):
            if picked == answer:
                st.success(f"{idx}번 정답입니다. ✅")
            else:
                st.markdown(f'<div class="wrong-box"><b>{idx}번</b> 다시 확인해 보세요.<br>내가 고른 답: {clean_text_for_display(picked) if picked else "선택 안 함"}<br>정답: <b>{clean_text_for_display(answer)}</b></div>', unsafe_allow_html=True)

elif selected_tab == "📝 Key Expression 뜻 맞추기":
    st.subheader("📝 Key Expression 뜻 맞추기")
    st.markdown(
        '<div class="game-card"><div class="big-guide">'
        '영어 표현을 보고 한국어 뜻을 고르는 문제와, 한국어 뜻을 보고 영어 표현을 고르는 문제가 섞여 나옵니다.<br>'
        '각 노래마다 중요한 표현 10개를 양방향으로 연습합니다.'
        '</div></div>',
        unsafe_allow_html=True
    )

    key_key = safe_key(song_choice)
    expressions = data["key_expressions"]

    all_english_options = [en for en, _ in expressions]
    all_korean_options = [ko for _, ko in expressions]

    user_answers = []

    for i, (en, ko) in enumerate(expressions, start=1):
        # 곡명과 번호를 seed로 사용해 문제 방향을 섞습니다.
        # 새로고침해도 같은 곡에서는 문제 방향이 안정적으로 유지됩니다.
        direction_rng = random.Random(f"{key_key}_direction_{i}")
        direction = direction_rng.choice(["en_to_ko", "ko_to_en"])

        rng = random.Random(f"{key_key}_keygame_{i}")

        if direction == "en_to_ko":
            # 영어 표현 → 한국어 뜻 고르기
            distractors = [x for x in all_korean_options if x != ko]
            wrongs = rng.sample(distractors, k=min(3, len(distractors)))
            options = shuffle_options(wrongs + [ko], seed=f"{key_key}_keygame_options_{i}")

            st.markdown(f"### {i}. {en}")
            picked = st.radio(
                "알맞은 한국어 뜻을 고르세요.",
                options,
                key=f"keygame_{key_key}_{i}",
                index=None
            )

            user_answers.append({
                "direction": "en_to_ko",
                "question": en,
                "picked": picked,
                "answer": ko,
                "en": en,
                "ko": ko,
            })

        else:
            # 한국어 뜻 → 영어 표현 고르기
            distractors = [x for x in all_english_options if x != en]
            wrongs = rng.sample(distractors, k=min(3, len(distractors)))
            options = shuffle_options(wrongs + [en], seed=f"{key_key}_keygame_options_{i}")

            st.markdown(f"### {i}. {ko}")
            picked = st.radio(
                "알맞은 영어 표현을 고르세요.",
                options,
                key=f"keygame_{key_key}_{i}",
                index=None
            )

            user_answers.append({
                "direction": "ko_to_en",
                "question": ko,
                "picked": picked,
                "answer": en,
                "en": en,
                "ko": ko,
            })

    c1, c2 = st.columns(2)

    with c1:
        submit_key = st.button(
            "Key Expression 정답 확인",
            key=f"keygame_submit_{key_key}",
            use_container_width=True
        )

    with c2:
        if st.button(
            "Key Expression 다시 풀기",
            key=f"keygame_reset_{key_key}",
            use_container_width=True
        ):
            for k in list(st.session_state.keys()):
                if k.startswith(f"keygame_{key_key}_"):
                    del st.session_state[k]
            st.rerun()

    if submit_key:
        score = sum(1 for item in user_answers if item["picked"] == item["answer"])
        st.markdown(
            f'<div class="score-box">점수: {score} / {len(user_answers)}</div>',
            unsafe_allow_html=True
        )

        for idx, item in enumerate(user_answers, start=1):
            en = item["en"]
            ko = item["ko"]
            picked = item["picked"]
            answer = item["answer"]

            if picked == answer:
                st.success(f"{idx}번 정답 ✅  {en} = {ko}")
            else:
                st.error(
                    f"{idx}번 오답 ❌  정답: {answer}\n\n"
                    f"전체 표현: {en} = {ko}"
                )


elif selected_tab == "🧩 문장 매칭 게임":
    match_key = safe_key(song_choice)

    pairs = [
        {
            "id": f"pair_{i}",
            "en": en,
            "ko": ko
        }
        for i, (en, ko) in enumerate(data["matching"], start=1)
    ]

    en_cards = [{"id": p["id"], "text": p["en"]} for p in pairs]
    ko_cards = [{"id": p["id"], "text": p["ko"]} for p in pairs]

    en_cards = shuffle_options(en_cards, seed=f"{match_key}_en")
    ko_cards = shuffle_options(ko_cards, seed=f"{match_key}_ko")

    payload = {
        "en": en_cards,
        "ko": ko_cards,
        "total": len(pairs),
    }

    data_json = json.dumps(payload, ensure_ascii=False)
    component_id = "match_" + uuid.uuid4().hex

    components.html(
        f"""
        <div id="{component_id}" class="match-app">
            <div class="match-head">
                <div class="match-title">🧩 문장 매칭 게임</div>
                <div class="match-guide">
                    왼쪽 영어 표현과 오른쪽 한국어 뜻을 차례로 눌러 짝을 맞추세요.<br>
                    선택한 박스는 색칠되고, 정답이면 두 박스가 반짝이며 함께 사라집니다.
                </div>
            </div>

            <div class="match-status">
                <div id="status_{component_id}">먼저 영어 또는 한국어 박스를 하나 선택하세요.</div>
                <div id="score_{component_id}">맞춘 개수: 0 / {len(pairs)}</div>
            </div>

            <div class="match-board">
                <div class="match-col">
                    <div class="col-title">English</div>
                    <div id="en_{component_id}" class="card-wrap"></div>
                </div>
                <div class="match-col">
                    <div class="col-title">Korean</div>
                    <div id="ko_{component_id}" class="card-wrap"></div>
                </div>
            </div>

            <div class="progress-outer">
                <div id="bar_{component_id}" class="progress-inner"></div>
            </div>

            <button id="reset_{component_id}" class="reset-btn">매칭 게임 다시 시작</button>
        </div>

        <style>
            #{component_id}.match-app {{
                font-family: Arial, sans-serif;
                width: 100%;
                box-sizing: border-box;
                background: linear-gradient(135deg,#eef2ff 0%,#f0f9ff 50%,#fdf2f8 100%);
                border: 1px solid #c7d2fe;
                border-radius: 22px;
                padding: 22px;
                margin: 8px 0 22px 0;
                color: #1e293b;
            }}

            #{component_id} .match-head {{
                background: rgba(255,255,255,0.72);
                border: 1px solid #dbeafe;
                border-radius: 18px;
                padding: 18px 20px;
                margin-bottom: 16px;
            }}

            #{component_id} .match-title {{
                font-size: 30px;
                font-weight: 1000;
                color: #4338ca;
                margin-bottom: 8px;
            }}

            #{component_id} .match-guide {{
                font-size: 16px;
                font-weight: 800;
                color: #475569;
                line-height: 1.7;
            }}

            #{component_id} .match-status {{
                display: grid;
                grid-template-columns: 1.5fr 0.8fr;
                gap: 10px;
                margin-bottom: 14px;
                align-items: center;
            }}

            #{component_id} .match-status > div {{
                background: #ffffff;
                border: 1px solid #dbeafe;
                border-radius: 14px;
                padding: 12px 14px;
                font-size: 15px;
                font-weight: 900;
                color: #1d4ed8;
                min-height: 24px;
            }}

            #{component_id} .match-board {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 14px;
            }}

            #{component_id} .match-col {{
                background: rgba(255,255,255,0.72);
                border: 1px solid #e5e7eb;
                border-radius: 18px;
                padding: 14px;
            }}

            #{component_id} .col-title {{
                font-size: 22px;
                font-weight: 1000;
                color: #111827;
                margin-bottom: 12px;
            }}

            #{component_id} .card-wrap {{
                display: flex;
                flex-direction: column;
                gap: 10px;
            }}

            #{component_id} .match-card {{
                width: 100%;
                text-align: left;
                border: 2px solid #c7d2fe;
                background: #ffffff;
                color: #1e293b;
                border-radius: 16px;
                padding: 14px 15px;
                font-size: 17px;
                font-weight: 900;
                line-height: 1.55;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(15,23,42,0.06);
                transition: transform .16s ease, background .16s ease, border-color .16s ease, box-shadow .16s ease;
                position: relative;
                overflow: hidden;
            }}

            #{component_id} .match-card:hover {{
                transform: translateY(-2px);
                border-color: #818cf8;
                box-shadow: 0 8px 18px rgba(99,102,241,0.16);
            }}

            #{component_id} .match-card.selected {{
                background: linear-gradient(135deg,#fef3c7 0%,#fde68a 100%);
                border-color: #f59e0b;
                color: #78350f;
                box-shadow: 0 0 0 4px rgba(245,158,11,0.18), 0 8px 20px rgba(245,158,11,0.22);
                transform: scale(1.015);
            }}

            #{component_id} .match-card.wrong {{
                animation: shake_{component_id} .28s ease-in-out;
                background: #fee2e2;
                border-color: #ef4444;
                color: #7f1d1d;
            }}

            #{component_id} .match-card.correct {{
                background: linear-gradient(135deg,#dcfce7,#bbf7d0);
                border-color: #22c55e;
                color: #14532d;
                animation: sparkleDisappear_{component_id} .68s ease forwards;
            }}

            #{component_id} .match-card.correct::after {{
                content: "✨";
                position: absolute;
                inset: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 34px;
                background: radial-gradient(circle, rgba(255,255,255,0.95), rgba(255,255,255,0.20), rgba(255,255,255,0));
                animation: sparkleFlash_{component_id} .68s ease forwards;
                pointer-events: none;
            }}

            @keyframes sparkleDisappear_{component_id} {{
                0% {{ opacity: 1; transform: scale(1); max-height: 220px; margin-bottom: 0; }}
                35% {{ opacity: 1; transform: scale(1.04); }}
                70% {{ opacity: .55; transform: scale(.96); max-height: 220px; }}
                100% {{ opacity: 0; transform: scale(.86); max-height: 0; padding-top: 0; padding-bottom: 0; border-width: 0; margin: 0; }}
            }}

            @keyframes sparkleFlash_{component_id} {{
                0% {{ opacity: 0; transform: scale(.6) rotate(0deg); }}
                35% {{ opacity: 1; transform: scale(1.25) rotate(8deg); }}
                100% {{ opacity: 0; transform: scale(1.7) rotate(-10deg); }}
            }}

            @keyframes shake_{component_id} {{
                0%, 100% {{ transform: translateX(0); }}
                25% {{ transform: translateX(-5px); }}
                50% {{ transform: translateX(5px); }}
                75% {{ transform: translateX(-3px); }}
            }}

            #{component_id} .progress-outer {{
                width: 100%;
                height: 14px;
                background: #e5e7eb;
                border-radius: 999px;
                overflow: hidden;
                margin: 16px 0 12px 0;
            }}

            #{component_id} .progress-inner {{
                height: 100%;
                width: 0%;
                background: linear-gradient(90deg,#60a5fa,#a78bfa,#f472b6);
                border-radius: 999px;
                transition: width .28s ease;
            }}

            #{component_id} .reset-btn {{
                width: 100%;
                border: 1px solid #c7d2fe;
                background: #ffffff;
                color: #4338ca;
                border-radius: 999px;
                min-height: 46px;
                font-size: 16px;
                font-weight: 1000;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(15,23,42,0.05);
            }}

            #{component_id} .reset-btn:hover {{
                background: #eef2ff;
            }}

            #{component_id} .done-message {{
                background: linear-gradient(135deg,#dcfce7,#bbf7d0);
                border: 1px solid #86efac;
                color: #14532d;
                border-radius: 16px;
                padding: 16px;
                margin-top: 14px;
                font-size: 20px;
                font-weight: 1000;
                text-align: center;
                animation: pop_{component_id} .45s ease;
            }}

            @keyframes pop_{component_id} {{
                0% {{ transform: scale(.92); opacity: 0; }}
                100% {{ transform: scale(1); opacity: 1; }}
            }}

            @media (max-width: 720px) {{
                #{component_id} .match-board {{
                    grid-template-columns: 1fr;
                }}
                #{component_id} .match-status {{
                    grid-template-columns: 1fr;
                }}
                #{component_id} .match-card {{
                    font-size: 15px;
                }}
            }}
        </style>

        <script>
            const data_{component_id} = {data_json};
            const root_{component_id} = document.getElementById("{component_id}");
            const enBox_{component_id} = document.getElementById("en_{component_id}");
            const koBox_{component_id} = document.getElementById("ko_{component_id}");
            const status_{component_id} = document.getElementById("status_{component_id}");
            const score_{component_id} = document.getElementById("score_{component_id}");
            const bar_{component_id} = document.getElementById("bar_{component_id}");
            const reset_{component_id} = document.getElementById("reset_{component_id}");

            let selected_{component_id} = null;
            let done_{component_id} = new Set();
            let locked_{component_id} = false;

            function escapeHtml_{component_id}(str) {{
                return String(str)
                    .replaceAll("&", "&amp;")
                    .replaceAll("<", "&lt;")
                    .replaceAll(">", "&gt;")
                    .replaceAll('"', "&quot;")
                    .replaceAll("'", "&#039;");
            }}

            function makeCard_{component_id}(card, kind) {{
                const btn = document.createElement("button");
                btn.className = "match-card";
                btn.dataset.id = card.id;
                btn.dataset.kind = kind;
                btn.innerHTML = escapeHtml_{component_id}(card.text);
                btn.addEventListener("click", () => handleClick_{component_id}(btn, card, kind));
                return btn;
            }}

            function render_{component_id}() {{
                enBox_{component_id}.innerHTML = "";
                koBox_{component_id}.innerHTML = "";

                data_{component_id}.en.forEach(card => {{
                    if (!done_{component_id}.has(card.id)) {{
                        enBox_{component_id}.appendChild(makeCard_{component_id}(card, "en"));
                    }}
                }});

                data_{component_id}.ko.forEach(card => {{
                    if (!done_{component_id}.has(card.id)) {{
                        koBox_{component_id}.appendChild(makeCard_{component_id}(card, "ko"));
                    }}
                }});

                updateScore_{component_id}();
            }}

            function updateScore_{component_id}() {{
                const count = done_{component_id}.size;
                const total = data_{component_id}.total;
                score_{component_id}.textContent = "맞춘 개수: " + count + " / " + total;
                bar_{component_id}.style.width = ((count / total) * 100) + "%";

                if (count === total) {{
                    status_{component_id}.textContent = "모든 문장을 맞췄습니다! 훌륭합니다. 🎉";
                    if (!root_{component_id}.querySelector(".done-message")) {{
                        const msg = document.createElement("div");
                        msg.className = "done-message";
                        msg.textContent = "🎉 모든 문장을 맞췄습니다!";
                        root_{component_id}.appendChild(msg);
                    }}
                }}
            }}

            function clearSelection_{component_id}() {{
                root_{component_id}.querySelectorAll(".match-card.selected").forEach(el => el.classList.remove("selected"));
                selected_{component_id} = null;
            }}

            function handleClick_{component_id}(el, card, kind) {{
                if (locked_{component_id}) return;
                if (done_{component_id}.has(card.id)) return;

                if (!selected_{component_id}) {{
                    selected_{component_id} = {{ el, card, kind }};
                    el.classList.add("selected");
                    status_{component_id}.textContent = kind === "en"
                        ? "오른쪽에서 알맞은 한국어 뜻을 고르세요."
                        : "왼쪽에서 알맞은 영어 표현을 고르세요.";
                    return;
                }}

                if (selected_{component_id}.el === el) {{
                    clearSelection_{component_id}();
                    status_{component_id}.textContent = "선택을 취소했습니다. 다시 하나를 고르세요.";
                    return;
                }}

                if (selected_{component_id}.card.id === card.id && selected_{component_id}.kind !== kind) {{
                    locked_{component_id} = true;
                    selected_{component_id}.el.classList.remove("selected");
                    el.classList.remove("selected");

                    selected_{component_id}.el.classList.add("correct");
                    el.classList.add("correct");
                    status_{component_id}.textContent = "정답입니다! 두 박스가 함께 사라집니다. ✅";

                    const matchedId = card.id;

                    setTimeout(() => {{
                        done_{component_id}.add(matchedId);
                        selected_{component_id} = null;
                        locked_{component_id} = false;
                        render_{component_id}();

                        if (done_{component_id}.size < data_{component_id}.total) {{
                            status_{component_id}.textContent = "좋아요. 다음 문장을 맞춰 보세요.";
                        }}
                    }}, 680);
                }} else {{
                    locked_{component_id} = true;
                    selected_{component_id}.el.classList.add("wrong");
                    el.classList.add("wrong");
                    status_{component_id}.textContent = "아쉬워요. 다시 짝을 맞춰 보세요. ❌";

                    setTimeout(() => {{
                        selected_{component_id}.el.classList.remove("selected", "wrong");
                        el.classList.remove("wrong");
                        selected_{component_id} = null;
                        locked_{component_id} = false;
                    }}, 360);
                }}
            }}

            reset_{component_id}.addEventListener("click", () => {{
                selected_{component_id} = null;
                done_{component_id} = new Set();
                locked_{component_id} = false;

                const doneMsg = root_{component_id}.querySelector(".done-message");
                if (doneMsg) doneMsg.remove();

                status_{component_id}.textContent = "먼저 영어 또는 한국어 박스를 하나 선택하세요.";
                render_{component_id}();
            }});

            render_{component_id}();
        </script>
        """,
        height=760,
        scrolling=True
    )
    
elif selected_tab == "✍️ 생각 적기":
    st.subheader("✍️ 생각 적기: Reflective Writing")
    st.markdown('<div class="game-card"><div class="big-guide">질문을 하나 고르고, 노래를 들으며 떠오른 생각을 자유롭게 적어 보세요.<br>학생이 쓴 내용을 바탕으로 한국어 글을 조금 더 풍부하게 다듬고, 그 글을 자연스러운 영어로 번역해 줍니다.<br>맨 밑에는 글을 더 발전시키기 위한 쓰기 조언만 제시합니다.</div></div>', unsafe_allow_html=True)
    reflect_key = safe_key(song_choice)
    questions = data["reflect_questions"][:3]
    selected_question = st.radio("질문을 선택하세요.", questions, key=f"reflect_question_{reflect_key}", index=0)
    answer = st.text_area("내 생각을 적어 보세요.", placeholder="예: 이 노래를 들으며 예전에 좋아했던 사람이 떠올랐다. 그때는 내 마음을 잘 표현하지 못했고, 지금 생각하면 조금 아쉽다...", height=180, key=f"reflect_answer_{reflect_key}")
    if st.button("피드백 받기", key=f"reflect_submit_{reflect_key}", use_container_width=True):
        if not answer.strip():
            st.warning("먼저 자신의 생각을 한두 문장이라도 적어 보세요.")
        else:
            ko_feedback, en_feedback, advice = make_polished_feedback(song_choice, selected_question, answer)
            st.markdown("### 🇰🇷 다듬은 한국어 글")
            st.markdown(f'<div class="feedback-ko">{clean_text_for_display(ko_feedback)}</div>', unsafe_allow_html=True)
            st.markdown("### 🇺🇸 English Translation")
            st.markdown(f'<div class="feedback-en">{clean_text_for_display(en_feedback)}</div>', unsafe_allow_html=True)
            st.markdown("### ✨ 쓰기 조언")
            st.markdown(f'<div class="advice-box">{clean_text_for_display(advice)}</div>', unsafe_allow_html=True)


여기 다른 모든것을 모두 그대로 유지하고. 하나도 바꾸지 말고. 같은 형태로 my heart will go on 도 추가해줘. 똑같은 형태로. 가사를 줄게. 

Every night in my dreams
I see you, I feel you
That is how I know you go on
Far across the distance
And spaces between us
You have come to show you go on
Near, far, wherever you are
I believe that the heart does go on
Once more, you open the door
And you're here in my heart
And my heart will go on and on
Love can touch us one time
And last for a lifetime
And never let go 'til we're gone
Love was when I loved you
One true time I'd hold to
In my life, we'll always go on
Near, far, wherever you are
I believe that the heart does go on (why does the heart go on?)
Once more, you open the door
And you're here in my heart
And my heart will go on and on
You're here, there's nothing I fear
And I know that my heart will go on
We'll stay forever this way
You are safe in my heart and
My heart will go on and on
import streamlit as st
import streamlit.components.v1 as components
import random
import html
import re
import json
import uuid

st.set_page_config(page_title="Pop Song Master Class", page_icon="🎵", layout="wide")

st.markdown("""
<style>
.stApp { background-color:#ffffff; color:#1e293b; }
.main-title {
    background: linear-gradient(135deg,#eef2ff,#f0f9ff,#fdf2f8);
    padding: 25px;
    border-radius: 18px;
    border: 2px solid #6366f1;
    text-align: center;
    color: #3730a3;
    margin-bottom: 22px;
}
.info-box {
    background-color:#f8fafc;
    padding:34px 38px;
    border-radius:22px;
    border:2px solid #cbd5e1;
    line-height:2.1;
    margin-bottom:26px;
    font-size:1.35rem;
}
.info-box h3 {
    color:#4338ca;
    border-bottom:4px solid #6366f1;
    padding-bottom:14px;
    margin-bottom:22px;
    font-size:2.4rem;
    font-weight:900;
}
.info-box p {
    font-size:1.35rem;
    line-height:2.1;
    color:#1e293b;
    margin-bottom:20px;
}
.info-box p {
    font-size:1.35rem;
    line-height:2.1;
    color:#1e293b;
    margin-bottom:20px;
}
.lyrics-container {
    padding:14px 20px;
    border-left:5px solid #6366f1;
    margin-bottom:10px;
    background-color:#f8fafc;
    border-radius:0 12px 12px 0;
}
.eng-line { font-size:1.08rem; font-weight:800; color:#1e3a8a; }
.kor-sub { font-size:0.95rem; color:#64748b; margin-top:5px; line-height:1.6; }
.quiz-box { background-color:#f0f9ff; padding:20px; border-radius:18px; border:1px solid #bae6fd; margin-top:22px; margin-bottom:20px; }
.score-box { background:linear-gradient(135deg,#dcfce7,#bbf7d0); padding:18px; border-radius:18px; border:1px solid #86efac; margin-top:18px; text-align:center; font-size:1.15rem; font-weight:900; }
.wrong-box { background:#fff7ed; padding:15px; border-radius:14px; border:1px solid #fdba74; margin-top:10px; }
.game-card { background:linear-gradient(135deg,#eef2ff,#f8fafc); border:1px solid #c7d2fe; border-radius:18px; padding:20px; margin-bottom:18px; }
.big-guide { font-size:1.12rem; font-weight:800; color:#475569; line-height:1.7; }
.matching-box { background:linear-gradient(135deg,#eef2ff 0%,#f0f9ff 50%,#fdf2f8 100%); padding:24px; border-radius:20px; border:1px solid #c7d2fe; margin-top:18px; margin-bottom:22px; }
.matching-title { font-size:2rem; font-weight:900; color:#4338ca; margin-bottom:10px; }
.selected-card-notice { background-color:#fef3c7; padding:14px 16px; border-radius:14px; border:1px solid #facc15; color:#92400e; font-size:1.05rem; font-weight:900; margin-bottom:16px; }
.feedback-ko { background:#fefce8; border:1px solid #fde68a; padding:18px; border-radius:16px; line-height:1.8; margin-top:14px; }
.feedback-en { background:#eff6ff; border:1px solid #bfdbfe; padding:18px; border-radius:16px; line-height:1.8; margin-top:14px; }
.advice-box { background:#f0fdf4; border:1px solid #bbf7d0; padding:18px; border-radius:16px; line-height:1.8; margin-top:14px; }

/* 배경 학습 전용 큰 글씨 카드 */
.bg-card {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
    padding: 34px 38px;
    border-radius: 24px;
    border: 2px solid #c7d2fe;
    margin-bottom: 26px;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.08);
}
.bg-title {
    font-size: 2.35rem;
    font-weight: 900;
    color: #3730a3;
    margin-bottom: 22px;
    padding-bottom: 14px;
    border-bottom: 4px solid #6366f1;
}
.bg-p {
    font-size: 1.35rem;
    line-height: 2.05;
    color: #1e293b;
    margin-bottom: 18px;
    font-weight: 560;
}
.bg-key {
    color: #1e3a8a;
    font-weight: 900;
}

</style>
""", unsafe_allow_html=True)


def clean_text_for_display(text):
    return html.escape(str(text).strip())

def safe_key(text):
    return re.sub(r"[^a-zA-Z0-9가-힣_]+", "_", text)

def shuffle_options(options, seed):
    rng = random.Random(seed)
    options = list(options)
    rng.shuffle(options)
    return options

def try_translate_ko_to_en(korean_text):
    korean_text = str(korean_text).strip()
    if not korean_text:
        return ""
    try:
        from deep_translator import GoogleTranslator
        translated = GoogleTranslator(source="ko", target="en").translate(korean_text)
        translated = str(translated).strip()
        if re.search(r"[가-힣]", translated):
            raise ValueError("Korean remained")
        return translated
    except Exception:
        return (
            "While listening to this song, I looked back on my own memories and emotions. "
            "This reflection was not just about the past; it helped me think about my relationships, choices, and feelings more deeply. "
            "The song reminds me that difficult memories can become meaningful when we try to understand them honestly."
        )

def make_polished_feedback(song_title, question, student_answer):
    answer = str(student_answer).strip()
    question = str(question).strip()
    if len(answer) < 10:
        polished_ko = (
            "이 노래를 들으며 아직 생각을 길게 정리하지는 못했지만, 마음속에 떠오르는 감정이 있다는 점이 중요합니다. "
            "노래 속 화자의 마음처럼, 나에게도 쉽게 말하지 못한 기억이나 다시 생각해 보고 싶은 순간이 있을 수 있습니다. "
            "그 감정을 조금 더 자세히 들여다보면, 단순한 감상이 아니라 나 자신을 이해하는 글로 발전할 수 있습니다."
        )
    else:
        polished_ko = (
            f"이 노래를 들으며 나는 다음과 같은 생각을 하게 되었습니다. {answer} "
            "이 경험은 단순히 지나간 일을 떠올리는 데서 끝나지 않습니다. 그때의 감정과 지금의 마음을 함께 돌아보게 하며, "
            "사람과의 관계가 언제나 쉽지만은 않다는 사실도 생각하게 합니다. 노래 속 화자의 감정처럼, 나 역시 과거의 한 장면을 다시 바라보며 "
            "그때 미처 표현하지 못했던 마음을 생각해 볼 수 있었습니다. 이런 성찰은 나의 감정을 더 깊이 이해하고, 앞으로의 관계를 조금 더 성숙하게 바라보는 계기가 됩니다."
        )
    if ("Scientist" in song_title or "그리운" in question or "옛" in question or "처음" in question or "관계" in question) and len(answer) >= 10:
        polished_ko = (
            f"이 노래를 들으며 나는 과거의 관계와 그때의 감정을 다시 떠올리게 되었습니다. {answer} "
            "그 기억은 단순한 추억이라기보다, 마음을 쉽게 열지 못했던 순간과 서로를 충분히 이해하지 못했던 시간을 돌아보게 합니다. "
            "노래 속 화자가 ‘처음으로 돌아가고 싶다’고 말하는 것처럼, 나 역시 그때로 돌아간다면 조금 더 솔직하게 말하고, "
            "상대의 마음을 더 천천히 이해하려 했을 것 같습니다. 결국 이 노래는 사랑이나 관계가 생각처럼 쉽지 않지만, "
            "그 어려움 속에서도 우리는 자신의 감정과 선택을 배울 수 있다는 점을 느끼게 해 줍니다."
        )
    english_translation = try_translate_ko_to_en(polished_ko)
    if re.search(r"[가-힣]", english_translation):
        english_translation = (
            "While listening to this song, I looked back on a past relationship and the emotions I felt at that time. "
            "The memory was not just a simple memory; it helped me think about moments when it was difficult to open my heart and when two people could not fully understand each other. "
            "Like the speaker in the song who wants to go back to the start, I also wondered what I might say or do differently if I could return to that moment. "
            "In the end, this song reminds me that love and relationships are not always easy, but they can help us understand our feelings and grow as a person."
        )
    advice = (
        "쓰기 조언: 글을 더 좋게 만들고 싶다면 ① 떠오른 사람이나 장면, ② 그때의 감정, ③ 지금 돌아보며 깨달은 점을 차례로 써 보세요. "
        "영어로 쓸 때는 다음 구조를 활용하면 좋습니다: While listening to this song, I thought about ~. / At that time, I felt ~ because ~. / Looking back now, I realize that ~."
    )
    return polished_ko, english_translation, advice

SONGS = {'1. Let It Go - Frozen OST': {'video_url': 'https://www.youtube.com/watch?v=RgGRyssdJvw',
                               'bg': '\n'
                                     '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#be185d;">\n'
                                     '        ❄️ Let It Go: 숨겨 왔던 자신을 받아들이는 순간\n'
                                     '    </h3>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        <b>Let It Go</b>는 영화 <i>Frozen</i>의 대표곡으로,\n'
                                     '        엘사가 더 이상 자신의 능력과 감정을 숨기지 않고\n'
                                     '        스스로를 받아들이는 장면에서 나오는 노래입니다.\n'
                                     '    </p>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        엘사는 어릴 때부터 자신의 얼음 마법이 다른 사람을 다치게 할 수 있다는\n'
                                     '        두려움 속에서 살아왔습니다. 그래서 감정을 숨기고,\n'
                                     '        능력을 감추며, 언제나 조심해야 했습니다.\n'
                                     '        하지만 대관식 날 엘사의 능력이 사람들 앞에서 드러나고,\n'
                                     '        사람들은 엘사를 두려워합니다.\n'
                                     '    </p>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        엘사는 모든 것을 피해 눈 덮인 산으로 도망치고,\n'
                                     '        그곳에서 처음으로 자신의 진짜 모습을 마주합니다.\n'
                                     '        이 노래는 단순히 “다 잊어버리자”는 의미가 아니라,\n'
                                     '        그동안 억눌렀던 두려움, 책임감, 타인의 시선에서 벗어나\n'
                                     '        자기 자신을 받아들이는 과정을 보여줍니다.\n'
                                     '    </p>\n'
                                     '\n'
                                     '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                     '        수업에서는 <b>let it go</b>, <b>conceal</b>, <b>hold back</b>,\n'
                                     "        <b>storm inside</b>, <b>I'm free</b>, <b>the past is in the past</b>\n"
                                     '        같은 표현을 중심으로 배울 수 있습니다.\n'
                                     '        특히 이 노래는 자유, 두려움, 자기표현, 자신감에 대해\n'
                                     '        함께 생각해 볼 수 있는 좋은 자료입니다.\n'
                                     '    </p>\n'
                                     '    ',
                               'lyrics': [('The snow glows white on the mountain tonight / Not a footprint to be seen',
                                           '오늘 밤 산 위에는 눈이 하얗게 빛나고 / 발자국 하나 보이지 않아요'),
                                          ("A kingdom of isolation / And it looks like I'm the queen", '고립된 왕국 / 그리고 내가 그곳의 여왕인 것 같아요'),
                                          ("The wind is howling like this swirling storm inside / Couldn't keep it in, heaven knows I tried",
                                           '바람은 내 안에서 휘몰아치는 폭풍처럼 울부짖고 / 더는 감출 수 없었어요, 하늘은 내가 얼마나 노력했는지 알 거예요'),
                                          ("Don't let them in, don't let them see / Be the good girl you always have to be",
                                           '그들을 들이지 마, 보여주지 마 / 언제나 그래야만 했던 착한 소녀가 되어라'),
                                          ("Conceal, don't feel, don't let them know / Well, now they know", '숨기고, 느끼지 말고, 그들이 알게 하지 마 / 하지만 이제 그들이 알아버렸어요'),
                                          ("Let it go, let it go / Can't hold it back anymore", '놓아버려, 놓아버려 / 더 이상 붙잡아 둘 수 없어'),
                                          ('Let it go, let it go / Turn away and slam the door', '놓아버려, 놓아버려 / 돌아서서 문을 세게 닫아버려'),
                                          ("I don't care what they're going to say / Let the storm rage on", '사람들이 뭐라고 하든 상관없어 / 폭풍이 계속 몰아치게 둬'),
                                          ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없으니까'),
                                          ("It's funny how some distance makes everything seem small / And the fears that once controlled me can't get to me "
                                           'at all',
                                           '거리를 두고 보니 모든 것이 작아 보이는 게 참 이상해 / 한때 나를 지배했던 두려움도 이제는 나에게 닿지 못해'),
                                          ("It's time to see what I can do / To test the limits and break through",
                                           '이제 내가 무엇을 할 수 있는지 볼 시간이야 / 한계를 시험하고 그것을 깨고 나아갈 시간이야'),
                                          ("No right, no wrong, no rules for me / I'm free", '옳고 그름도, 나를 묶는 규칙도 없어 / 나는 자유로워'),
                                          ('Let it go, let it go / I am one with the wind and sky', '놓아버려, 놓아버려 / 나는 바람과 하늘과 하나가 되었어'),
                                          ("Let it go, let it go / You'll never see me cry", '놓아버려, 놓아버려 / 너희는 다시는 내가 우는 모습을 보지 못할 거야'),
                                          ('Here I stand and here I stay / Let the storm rage on', '나는 여기 서 있고, 여기 머물 거야 / 폭풍이 계속 몰아치게 둬'),
                                          ('My power flurries through the air into the ground / My soul is spiraling in frozen fractals all around',
                                           '내 힘은 공기를 지나 땅속으로 흩날려 퍼지고 / 내 영혼은 사방의 얼어붙은 결정 속에서 소용돌이쳐'),
                                          ("And one thought crystallizes like an icy blast / I'm never going back, the past is in the past",
                                           '그리고 하나의 생각이 얼음바람처럼 선명하게 굳어져 / 나는 절대 돌아가지 않아, 과거는 과거일 뿐이야'),
                                          ("Let it go, let it go / And I'll rise like the break of dawn", '놓아버려, 놓아버려 / 나는 새벽이 밝아오듯 다시 일어설 거야'),
                                          ('Let it go, let it go / That perfect girl is gone', '놓아버려, 놓아버려 / 그 완벽한 소녀는 이제 없어'),
                                          ('Here I stand in the light of day / Let the storm rage on', '나는 밝은 낮의 빛 속에 서 있어 / 폭풍이 계속 몰아치게 둬'),
                                          ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없으니까')],
                               'quiz': [{'q': '1. 이 노래를 부르는 인물은 누구인가요?', 'options': ['Anna', 'Olaf', 'Kristoff', 'Elsa'], 'answer': 'Elsa'},
                                        {'q': '2. 엘사는 어디에서 이 노래를 부르나요?', 'options': ['교실', '바닷가', '눈 덮인 산', '도시 거리'], 'answer': '눈 덮인 산'},
                                        {'q': '3. 엘사가 더 이상 하지 않으려는 것은 무엇인가요?',
                                         'options': ['음식을 먹는 것', '학교에 가는 것', '동물과 이야기하는 것', '자신을 숨기는 것'],
                                         'answer': '자신을 숨기는 것'},
                                        {'q': '4. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?', 'options': ['배고픔', '지루함', '자유와 해방감', '질투'], 'answer': '자유와 해방감'},
                                        {'q': "5. 'conceal'의 뜻으로 가장 알맞은 것은 무엇인가요?", 'options': ['숨기다', '달리다', '노래하다', '웃다'], 'answer': '숨기다'},
                                        {'q': "6. 'Can't hold it back anymore'는 어떤 의미에 가깝나요?",
                                         'options': ['더 이상 문을 열 수 없다', '더 이상 노래할 수 없다', '더 이상 걸을 수 없다', '더 이상 억누를 수 없다'],
                                         'answer': '더 이상 억누를 수 없다'},
                                        {'q': "7. 'I'm free'에서 엘사가 느끼는 감정은 무엇인가요?", 'options': ['두려움', '부끄러움', '자유로움', '배고픔'], 'answer': '자유로움'},
                                        {'q': "8. 'the past is in the past'는 어떤 의미인가요?",
                                         'options': ['과거로 돌아가고 싶다', '과거는 과거일 뿐이다', '과거가 가장 중요하다', '과거를 다시 만들 수 있다'],
                                         'answer': '과거는 과거일 뿐이다'}],
                               'key_expressions': [('Let it go', '놓아버려'),
                                                   ("Can't hold it back anymore", '더 이상 억누를 수 없어'),
                                                   ("Conceal, don't feel", '숨기고, 느끼지 마'),
                                                   ('Let the storm rage on', '폭풍이 계속 몰아치게 둬'),
                                                   ("I'm free", '나는 자유로워'),
                                                   ('The past is in the past', '과거는 과거일 뿐이야'),
                                                   ('Here I stand', '나는 여기 서 있어'),
                                                   ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없어'),
                                                   ('Test the limits', '한계를 시험하다'),
                                                   ('Break through', '뚫고 나아가다')],
                               'matching': [('Let it go', '놓아버려'),
                                            ("Can't hold it back anymore", '더 이상 억누를 수 없어'),
                                            ("I'm free", '나는 자유로워'),
                                            ('The past is in the past', '과거는 과거일 뿐이야'),
                                            ('Here I stand', '나는 여기 서 있어'),
                                            ('The cold never bothered me anyway', '어차피 추위는 나를 괴롭힌 적이 없어')],
                               'reflect_questions': ['다른 사람의 시선 때문에 나 자신을 숨긴 적이 있나요?',
                                                     '내가 더 이상 붙잡고 싶지 않은 두려움이나 걱정은 무엇인가요?',
                                                     '이 노래처럼 “나는 자유로워”라고 말하고 싶은 순간은 언제인가요?']},
 '2. Hello - Adele': {'video_url': 'https://www.youtube.com/watch?v=h7NBamHcX58',
                      'bg': '\n'
                            '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#4338ca;">\n'
                            '        ☎️ Hello: 과거의 누군가에게 건네는 늦은 안부\n'
                            '    </h3>\n'
                            '\n'
                            '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                            '        Adele의 <b>Hello</b>는 시간이 많이 흐른 뒤, 과거의 누군가에게 다시 연락하고 싶은 마음을 담은 노래입니다.\n'
                            '        노래 속 화자는 상대에게 전화를 걸며 오래전의 관계, 미안함, 후회,\n'
                            '        그리고 아직 완전히 치유되지 않은 감정을 떠올립니다.\n'
                            '    </p>\n'
                            '\n'
                            '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                            '        이 노래에서 화자는 단순히 “안녕”이라고 말하는 것이 아니라,\n'
                            '        과거에 하지 못했던 사과를 전하고 싶어 합니다.\n'
                            '        하지만 두 사람 사이에는 시간의 거리, 마음의 거리, 그리고 실제 거리까지 생겨 있습니다.\n'
                            '        그래서 반복되는 <b>Hello</b>라는 말은 인사이면서 동시에 조심스러운 사과의 시작처럼 들립니다.\n'
                            '    </p>\n'
                            '\n'
                            '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                            "        수업에서는 <b>I'm sorry</b>, <b>I tried</b>, <b>after all these years</b>,\n"
                            '        <b>used to be</b>, <b>the other side</b> 같은 표현을 중심으로 배울 수 있습니다.\n'
                            '        특히 이 노래는 속도가 비교적 느리고 감정이 분명하게 드러나기 때문에,\n'
                            '        학생들이 가사를 읽으며 화자의 감정과 영어 표현을 함께 이해하기에 좋습니다.\n'
                            '    </p>\n'
                            '    ',
                      'lyrics': [("Hello, it's me / I was wondering if after all these years you'd like to meet, to go over everything",
                                  '안녕, 나야 / 이 모든 세월이 흐른 뒤에 네가 만나서 모든 일을 다시 이야기해 보고 싶어 할지 궁금했어'),
                                 ("They say that time's supposed to heal ya / But I ain't done much healing",
                                  '사람들은 시간이 너를 치유해 줄 거라고 말하지만 / 나는 별로 치유되지 않은 것 같아'),
                                 ("Hello, can you hear me? / I'm in California dreaming about who we used to be",
                                  '여보세요, 내 말 들리니? / 나는 캘리포니아에서 예전의 우리 모습을 떠올리고 있어'),
                                 ("When we were younger and free / I've forgotten how it felt before the world fell at our feet",
                                  '우리가 더 어리고 자유로웠을 때 / 세상이 우리 발아래 있는 것 같았던 그 느낌을 나는 잊어버렸어'),
                                 ("There's such a difference between us / And a million miles", '우리 사이에는 너무 큰 차이가 있어 / 그리고 백만 마일만큼의 거리도 있어'),
                                 ("Hello from the other side / I must've called a thousand times to tell you", '저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야'),
                                 ("I'm sorry, for everything that I've done / But when I call you never seem to be home",
                                  '내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아'),
                                 ("Hello from the outside / At least I can say that I've tried to tell you", '바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어'),
                                 ("I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
                                  '네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아'),
                                 ("Hello, how are you? / It's so typical of me to talk about myself", '안녕, 어떻게 지내? / 내 이야기만 하는 건 정말 나다운 일이야'),
                                 ("I'm sorry, I hope that you're well / Did you ever make it out of that town where nothing ever happened?",
                                  '미안해, 네가 잘 지내길 바라 / 아무 일도 일어나지 않던 그 마을에서 벗어났니?'),
                                 ("It's no secret that the both of us are running out of time", '우리 둘 다 시간이 얼마 남지 않았다는 건 비밀도 아니야'),
                                 ("Hello from the other side / I must've called a thousand times to tell you", '저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야'),
                                 ("I'm sorry, for everything that I've done / But when I call you never seem to be home",
                                  '내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아'),
                                 ("Hello from the outside / At least I can say that I've tried to tell you", '바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어'),
                                 ("I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
                                  '네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아'),
                                 ('Ooooohh, anymore / Ooooohh, anymore / Ooooohh, anymore / Anymore', '오, 더 이상 / 오, 더 이상 / 오, 더 이상 / 더 이상'),
                                 ("Hello from the other side / I must've called a thousand times to tell you", '저편에서 안녕이라고 말해 / 너에게 말하려고 나는 아마 천 번은 전화했을 거야'),
                                 ("I'm sorry, for everything that I've done / But when I call you never seem to be home",
                                  '내가 했던 모든 일에 대해 미안해 / 하지만 내가 전화할 때 너는 늘 집에 없는 것 같아'),
                                 ("Hello from the outside / At least I can say that I've tried to tell you", '바깥쪽에서 안녕이라고 말해 / 적어도 나는 너에게 말하려고 노력했다고는 말할 수 있어'),
                                 ("I'm sorry, for breaking your heart / But it don't matter, it clearly doesn't tear you apart anymore",
                                  '네 마음을 아프게 해서 미안해 / 하지만 이제는 상관없는 것 같아, 더 이상 너를 아프게 하지 않는 것 같아')],
                      'quiz': [{'q': '1. 이 노래에서 화자는 누구에게 연락하려고 하나요?', 'options': ['새로 만난 선생님', '유명한 가수', '캘리포니아의 낯선 사람', '과거에 알던 사람'], 'answer': '과거에 알던 사람'},
                               {'q': '2. 화자가 상대에게 가장 말하고 싶어 하는 것은 무엇인가요?', 'options': ['고맙다는 말', '미안하다는 말', '생일 축하한다는 말', '여행을 가자는 말'], 'answer': '미안하다는 말'},
                               {'q': '3. 노래에서 사람들은 시간이 무엇을 해 준다고 말하나요?',
                                'options': ['사람을 부자로 만들어 준다', '과거를 완전히 바꿔 준다', '상처를 치유해 준다', '슬픔을 바로 없애 준다'],
                                'answer': '상처를 치유해 준다'},
                               {'q': '4. 화자는 어디에서 예전의 자신들을 떠올리고 있나요?', 'options': ['런던', '캘리포니아', '뉴욕', '파리'], 'answer': '캘리포니아'},
                               {'q': "5. 'I must've called a thousand times'는 어떤 의미에 가깝나요?",
                                'options': ['정확히 천 번만 전화했다', '한 번도 전화하지 않았다', '전화번호를 잊어버렸다', '정말 여러 번 연락하려고 했다'],
                                'answer': '정말 여러 번 연락하려고 했다'},
                               {'q': "6. 'Hello from the other side'에서 'the other side'는 무엇을 상징한다고 볼 수 있나요?",
                                'options': ['학교의 반대편 교실', '가수가 사는 집', '멀어진 시간과 마음의 거리', '무대의 왼쪽'],
                                'answer': '멀어진 시간과 마음의 거리'},
                               {'q': "7. 화자가 'I tried'라고 말하는 이유는 무엇인가요?",
                                'options': ['노래 대회에 나가려고 했기 때문에', '캘리포니아로 여행을 가고 싶었기 때문에', '새로운 친구를 만들고 싶었기 때문에', '상대에게 사과하려고 노력했기 때문에'],
                                'answer': '상대에게 사과하려고 노력했기 때문에'},
                               {'q': '8. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?', 'options': ['여행의 설렘', '후회와 사과', '복수심과 분노', '시험에 대한 걱정'], 'answer': '후회와 사과'}],
                      'key_expressions': [("Hello, it's me", '안녕, 나야'),
                                          ('After all these years', '이 모든 세월이 흐른 뒤에'),
                                          ("Time's supposed to heal you", '시간이 너를 치유해 줄 거라고 여겨진다'),
                                          ('Can you hear me?', '내 말 들리니?'),
                                          ('Who we used to be', '예전의 우리 모습'),
                                          ('Hello from the other side', '저편에서 전하는 안녕'),
                                          ("I must've called a thousand times", '정말 여러 번 전화했을 거야'),
                                          ("I'm sorry", '미안해'),
                                          ("At least I can say that I've tried", '적어도 노력했다고 말할 수 있어'),
                                          ("I hope that you're well", '네가 잘 지내길 바라')],
                      'matching': [("Hello, it's me", '안녕, 나야'),
                                   ("I'm sorry", '미안해'),
                                   ('I tried', '나는 노력했어'),
                                   ('Hello from the other side', '저편에서 안녕이라고 말해'),
                                   ('Can you hear me?', '내 말 들리니?'),
                                   ("I hope that you're well", '네가 잘 지내길 바라')],
                      'reflect_questions': ['오랫동안 연락하지 못했지만 다시 이야기하고 싶은 사람이 있나요?', '누군가에게 미안하다고 말하지 못했던 경험이 있나요?', '시간이 지나면서 치유된 감정이나 아직 남아 있는 감정이 있나요?']},
 '3. A Whole New World - Aladdin OST': {'video_url': 'https://www.youtube.com/watch?v=9FJssSUxI88',
                                        'bg': '\n'
                                              '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#4338ca;">\n'
                                              '        🕌 A Whole New World: 새로운 세상을 바라보는 순간\n'
                                              '    </h3>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        <b>A Whole New World</b>는 영화 <i>Aladdin</i>의 대표곡으로,\n'
                                              '        알라딘과 자스민이 마법 양탄자를 타고 밤하늘을 날며\n'
                                              '        새로운 세상을 바라보는 장면에서 나오는 노래입니다.\n'
                                              '    </p>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        자스민은 궁전 안에서 공주로 살아가지만,\n'
                                              '        정해진 규칙과 역할 속에서 자유롭게 세상을 경험하지 못합니다.\n'
                                              '        알라딘은 그런 자스민에게 궁전 밖의 넓은 세상을 보여 주고,\n'
                                              '        자스민은 처음으로 자신이 알지 못했던 새로운 풍경과 가능성을 마주하게 됩니다.\n'
                                              '    </p>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        이 노래에서 <b>a whole new world</b>는 단순히 새로운 장소만을 뜻하지 않습니다.\n'
                                              '        새로운 시선, 새로운 경험, 그리고 스스로 선택할 수 있는 자유를 의미합니다.\n'
                                              '        두 사람은 마법 양탄자를 타고 하늘을 날며,\n'
                                              '        두려움보다 설렘이 더 큰 새로운 세계로 함께 나아갑니다.\n'
                                              '    </p>\n'
                                              '\n'
                                              '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                              '        수업에서는 <b>I can show you the world</b>, <b>open your eyes</b>,\n'
                                              '        <b>point of view</b>, <b>crystal clear</b>, <b>new horizons</b>\n'
                                              '        같은 표현을 중심으로 배울 수 있습니다.\n'
                                              '        특히 이 노래는 속도가 비교적 부드럽고 장면이 분명해서,\n'
                                              '        학생들이 영어 표현과 함께 설렘, 자유, 새로운 경험의 감정을 이해하기에 좋습니다.\n'
                                              '    </p>\n'
                                              '    ',
                                        'lyrics': [('I can show you the world / Shining, shimmering, splendid', '내가 너에게 세상을 보여 줄 수 있어 / 빛나고, 반짝이고, 눈부신 세상을'),
                                                   ('Tell me, princess, now when did / You last let your heart decide?',
                                                    '말해 봐요, 공주님, 언제였나요 / 마지막으로 마음이 원하는 대로 선택했던 때가?'),
                                                   ('I can open your eyes / Take you wonder by wonder', '내가 너의 눈을 뜨게 해 줄 수 있어 / 놀라움에서 또 다른 놀라움으로 데려가며'),
                                                   ('Over, sideways and under / On a magic carpet ride', '위로, 옆으로, 아래로 날아가며 / 마법 양탄자를 타고'),
                                                   ('A whole new world / A new fantastic point of view', '완전히 새로운 세상 / 새롭고 환상적인 시선'),
                                                   ('No one to tell us no / Or where to go', '아무도 우리에게 안 된다고 말하지 않고 / 어디로 가라고 하지도 않아'),
                                                   ("Or say we're only dreaming", '우리가 그저 꿈꾸고 있을 뿐이라고 말하지도 않아'),
                                                   ('A whole new world / A dazzling place I never knew', '완전히 새로운 세상 / 내가 전에는 알지 못했던 눈부신 곳'),
                                                   ("But when I'm way up here, it's crystal clear / That now I'm in a whole new world with you",
                                                    '하지만 이렇게 높은 곳에 올라오니 모든 것이 분명해 / 지금 나는 너와 함께 완전히 새로운 세상에 있어'),
                                                   ("(Now I'm in a whole new world with you)", '이제 나는 너와 함께 완전히 새로운 세상에 있어'),
                                                   ('Unbelievable sights / Indescribable feeling', '믿기 어려운 풍경들 / 말로 표현할 수 없는 감정'),
                                                   ('Soaring, tumbling, freewheeling / Through an endless diamond sky',
                                                    '솟아오르고, 구르고, 자유롭게 날아가며 / 끝없이 펼쳐진 다이아몬드 같은 하늘을 지나'),
                                                   ("A whole new world / Don't you dare close your eyes", '완전히 새로운 세상 / 절대 눈 감지 마'),
                                                   ('A hundred thousand things to see / Hold your breath, it gets better',
                                                    '볼 것이 셀 수 없이 많아 / 숨을 참고 봐, 더 좋아질 거야'),
                                                   ("I'm like a shooting star, I've come so far / I can't go back to where I used to be",
                                                    '나는 별똥별 같아, 정말 멀리까지 왔어 / 예전의 내가 있던 곳으로 돌아갈 수 없어'),
                                                   ('A whole new world / Every turn a surprise', '완전히 새로운 세상 / 방향을 틀 때마다 놀라움이 있어'),
                                                   ('With new horizons to pursue / Every moment, red-letter', '따라갈 새로운 지평선들이 있고 / 모든 순간이 특별해'),
                                                   ("I'll chase them anywhere, there's time to spare / Let me share this whole new world with you",
                                                    '나는 어디든 그것들을 따라갈 거야, 시간은 충분해 / 이 완전히 새로운 세상을 너와 함께 나누게 해 줘'),
                                                   ('A whole new world / A whole new world', '완전히 새로운 세상 / 완전히 새로운 세상'),
                                                   ("That's where we'll be / That's where we'll be", '그곳이 우리가 있을 곳이야 / 그곳이 우리가 있을 곳이야'),
                                                   ('A thrilling chase / A wondrous place', '짜릿한 모험 / 놀라운 곳'),
                                                   ('For you and me', '너와 나를 위한')],
                                        'quiz': [{'q': '1. 이 노래에서 두 사람은 무엇을 타고 있나요?', 'options': ['기차', '자전거', '배', '마법 양탄자'], 'answer': '마법 양탄자'},
                                                 {'q': '2. 이 노래에서 알라딘은 자스민에게 무엇을 보여 주고 싶어 하나요?',
                                                  'options': ['학교 교실', '시험 문제', '새로운 세상', '휴대전화'],
                                                  'answer': '새로운 세상'},
                                                 {'q': "3. 'A whole new world'가 상징하는 것으로 가장 알맞은 것은 무엇인가요?",
                                                  'options': ['낡은 방', '어려운 시험', '혼자 있는 시간', '새로운 시선과 경험'],
                                                  'answer': '새로운 시선과 경험'},
                                                 {'q': "4. 'I can open your eyes'는 어떤 의미에 가깝나요?",
                                                  'options': ['잠에서 깨우다', '눈을 감게 하다', '새로운 것을 보게 해 주다', '멀리 보내다'],
                                                  'answer': '새로운 것을 보게 해 주다'},
                                                 {'q': "5. 'point of view'의 뜻으로 가장 알맞은 것은 무엇인가요?", 'options': ['문', '속도', '약속', '관점'], 'answer': '관점'},
                                                 {'q': '6. 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?',
                                                  'options': ['후회와 슬픔', '분노와 복수', '설렘과 자유로움', '지루함'],
                                                  'answer': '설렘과 자유로움'},
                                                 {'q': "7. 'I can't go back to where I used to be'는 어떤 의미인가요?",
                                                  'options': ['집에 갈 길을 잃었다', '예전의 모습으로 돌아갈 수 없다', '학교에 다시 가야 한다', '여행을 취소했다'],
                                                  'answer': '예전의 모습으로 돌아갈 수 없다'},
                                                 {'q': '8. 이 노래의 주요 배경으로 가장 알맞은 것은 무엇인가요?',
                                                  'options': ['교실에서 보는 시험', '바닷가에서 하는 운동', '시장 안의 장면', '밤하늘을 나는 마법 양탄자 여행'],
                                                  'answer': '밤하늘을 나는 마법 양탄자 여행'}],
                                        'key_expressions': [('I can show you the world', '내가 너에게 세상을 보여 줄 수 있어'),
                                                            ('Shining, shimmering, splendid', '빛나고 반짝이고 눈부신'),
                                                            ('Let your heart decide', '마음이 결정하게 하다'),
                                                            ('Open your eyes', '눈을 뜨게 하다'),
                                                            ('A whole new world', '완전히 새로운 세상'),
                                                            ('Point of view', '관점'),
                                                            ('No one to tell us no', '아무도 안 된다고 말하지 않음'),
                                                            ('Unbelievable sights', '믿기 어려운 풍경들'),
                                                            ('Indescribable feeling', '말로 표현할 수 없는 감정'),
                                                            ('New horizons to pursue', '따라갈 새로운 지평선들')],
                                        'matching': [('I can show you the world', '내가 너에게 세상을 보여 줄 수 있어'),
                                                     ('A whole new world', '완전히 새로운 세상'),
                                                     ('A new fantastic point of view', '새롭고 환상적인 시선'),
                                                     ("Don't you dare close your eyes", '절대 눈 감지 마'),
                                                     ('Open your eyes', '눈을 떠 봐'),
                                                     ('Every turn a surprise', '방향을 틀 때마다 놀라움이 있어')],
                                        'reflect_questions': ['내가 경험해 보고 싶은 “완전히 새로운 세상”은 무엇인가요?', '누군가가 나에게 새로운 관점을 보여 준 적이 있나요?', '두려움보다 설렘이 더 컸던 경험이 있나요?']},
 '4. Stand By Me - Ben E. King': {'video_url': 'https://www.youtube.com/watch?v=c5hDjpi_HM0',
                                  'bg': '\n'
                                        '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#15803d;">\n'
                                        '        🤝 Stand By Me: 곁에 있어 주는 힘\n'
                                        '    </h3>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        '        <b>Stand By Me</b>는 어둡고 불안한 순간에도\n'
                                        '        누군가가 내 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다.\n'
                                        '        제목의 <b>stand by me</b>는 단순히 “내 옆에 서 있어”라는 뜻을 넘어,\n'
                                        '        “내 곁에 있어 줘”, “나를 지켜 줘”, “함께해 줘”라는 의미로 이해할 수 있습니다.\n'
                                        '    </p>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        '        노래 속 화자는 밤이 찾아오고 세상이 어두워지는 장면을 떠올립니다.\n'
                                        '        하지만 그는 혼자가 아니라는 믿음 때문에 두려워하지 않습니다.\n'
                                        '        달빛만 보이는 어두운 상황, 하늘이 무너지고 산이 바다로 무너져 내리는 듯한\n'
                                        '        극단적인 상황에서도 사랑하는 사람이 곁에 있다면 괜찮다고 말합니다.\n'
                                        '    </p>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        '        이 노래는 어려운 단어가 많지 않고,\n'
                                        "        <b>I won't be afraid</b>, <b>I won't cry</b>, <b>stand by me</b>처럼\n"
                                        '        짧고 반복적인 표현이 많아 학생들이 듣고 따라 부르기에 좋습니다.\n'
                                        '        또한 친구, 가족, 사랑하는 사람의 존재가 주는 안정감과 용기를\n'
                                        '        자연스럽게 이야기해 볼 수 있는 노래입니다.\n'
                                        '    </p>\n'
                                        '\n'
                                        '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                        "        수업에서는 <b>stand by me</b>, <b>I won't be afraid</b>,\n"
                                        "        <b>I won't cry</b>, <b>shed a tear</b>, <b>whenever you're in trouble</b>\n"
                                        '        같은 표현을 중심으로 배울 수 있습니다.\n'
                                        '        특히 이 노래는 느린 속도와 반복 구조 덕분에\n'
                                        '        기초 학습자도 영어 표현을 소리로 익히기에 적합합니다.\n'
                                        '    </p>\n'
                                        '    ',
                                  'lyrics': [('When the night has come / And the land is dark', '밤이 찾아오고 / 세상이 어두워질 때'),
                                             ("And the moon is the only light we'll see", '달빛만이 우리가 볼 수 있는 유일한 빛일 때'),
                                             ("No, I won't be afraid / Oh, I won't be afraid", '아니, 나는 두려워하지 않을 거야 / 오, 나는 두려워하지 않을 거야'),
                                             ('Just as long as you stand / Stand by me', '네가 곁에 있어 준다면 / 내 곁에 있어 준다면'),
                                             ("So darlin', darlin' / Stand by me, oh, stand by me", '그러니 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘'),
                                             ('Oh, stand, stand by me / Stand by me', '오, 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘'),
                                             ('If the sky that we look upon / Should tumble and fall', '우리가 바라보는 하늘이 / 무너져 내린다 해도'),
                                             ('Or the mountain should crumble to the sea', '산이 부서져 바다로 무너져 내린다 해도'),
                                             ("I won't cry, I won't cry / No, I won't shed a tear", '나는 울지 않을 거야, 울지 않을 거야 / 아니, 눈물 한 방울도 흘리지 않을 거야'),
                                             ('Just as long as you stand / Stand by me', '네가 곁에 있어 준다면 / 내 곁에 있어 준다면'),
                                             ("And darlin', darlin' / Stand by me, oh, stand by me", '그리고 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘'),
                                             ('Oh, stand now, stand by me / Stand by me', '오, 지금 곁에 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘'),
                                             ("Darlin', darlin' / Stand by me, oh, stand by me", '사랑하는 사람아, 사랑하는 사람아 / 내 곁에 있어 줘, 오, 내 곁에 있어 줘'),
                                             ('Oh, stand now, stand by me / Stand by me', '오, 지금 곁에 있어 줘, 내 곁에 있어 줘 / 내 곁에 있어 줘'),
                                             ("Whenever you're in trouble / Won't you stand by me?", '네가 힘든 순간에 / 내 곁에 있어 주지 않을래?'),
                                             ("Oh, stand by me / Won't you stand now?", '오, 내 곁에 있어 줘 / 지금 내 곁에 있어 주지 않을래?'),
                                             ('Oh, stand, stand by me', '오, 있어 줘, 내 곁에 있어 줘')],
                                  'quiz': [{'q': '1. 이 노래는 어떤 시간적 배경으로 시작하나요?', 'options': ['아침', '밤', '점심시간', '학교 수업 시간'], 'answer': '밤'},
                                           {'q': '2. 노래에서 보이는 유일한 빛은 무엇인가요?', 'options': ['햇빛', '달빛', '휴대전화 불빛', '촛불'], 'answer': '달빛'},
                                           {'q': '3. 화자는 두려움에 대해 무엇이라고 말하나요?',
                                            'options': ['나는 두려워하지 않을 거야', '나는 항상 두려워', '나는 두려움을 좋아해', '나는 학교가 두려워'],
                                            'answer': '나는 두려워하지 않을 거야'},
                                           {'q': "4. 'Stand by me'의 의미로 가장 알맞은 것은 무엇인가요?",
                                            'options': ['멀리 도망가', '앉아 있어', '집에 가', '내 곁에 있어 줘'],
                                            'answer': '내 곁에 있어 줘'},
                                           {'q': '5. 이 노래의 중심 주제로 가장 알맞은 것은 무엇인가요?',
                                            'options': ['쇼핑', '경쟁', '요리', '함께 있어 주는 힘과 위로'],
                                            'answer': '함께 있어 주는 힘과 위로'},
                                           {'q': '6. 화자가 두려워하지 않는 이유는 무엇인가요?',
                                            'options': ['돈이 많기 때문에', '날씨가 맑기 때문에', '누군가가 곁에 있어 주기 때문에', '잠을 자고 있기 때문에'],
                                            'answer': '누군가가 곁에 있어 주기 때문에'},
                                           {'q': "7. 'I won't shed a tear'의 의미로 가장 알맞은 것은 무엇인가요?",
                                            'options': ['눈물 한 방울도 흘리지 않겠다', '많이 웃겠다', '잠을 자겠다', '멀리 떠나겠다'],
                                            'answer': '눈물 한 방울도 흘리지 않겠다'},
                                           {'q': "8. 'Whenever you're in trouble'은 어떤 뜻인가요?",
                                            'options': ['네가 여행을 갈 때마다', '네가 노래할 때마다', '네가 힘든 순간에는 언제든지', '네가 밥을 먹을 때마다'],
                                            'answer': '네가 힘든 순간에는 언제든지'}],
                                  'key_expressions': [('Stand by me', '내 곁에 있어 줘'),
                                                      ('The night has come', '밤이 찾아왔다'),
                                                      ('The land is dark', '세상이 어둡다'),
                                                      ('The only light', '유일한 빛'),
                                                      ("I won't be afraid", '나는 두려워하지 않을 거야'),
                                                      ('Just as long as', '~하는 한'),
                                                      ('Tumble and fall', '무너져 내리다'),
                                                      ('Crumble to the sea', '바다로 무너져 내리다'),
                                                      ("I won't shed a tear", '눈물 한 방울도 흘리지 않을 거야'),
                                                      ("Whenever you're in trouble", '네가 힘든 순간에는 언제든지')],
                                  'matching': [('Stand by me', '내 곁에 있어 줘'),
                                               ("I won't be afraid", '나는 두려워하지 않을 거야'),
                                               ("I won't cry", '나는 울지 않을 거야'),
                                               ("Whenever you're in trouble", '네가 힘든 순간에는 언제든지'),
                                               ('The land is dark', '세상이 어두워'),
                                               ('The moon is the only light', '달빛만이 유일한 빛이야')],
                                  'reflect_questions': ['내가 힘들 때 곁에 있어 주었던 사람은 누구인가요?', '누군가에게 “내 곁에 있어 줘”라고 말하고 싶었던 순간이 있나요?', '나도 누군가에게 힘이 되어 준 경험이 있나요?']},
 "5. Don't Know Why - Norah Jones": {'video_url': 'https://www.youtube.com/watch?v=nhLdJeLTM48',
                                     'bg': '\n'
                                           '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#7c3aed;">\n'
                                           "        🌙 Don't Know Why: 이유를 알 수 없는 마음\n"
                                           '    </h3>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           "        <b>Don't Know Why</b>는 Norah Jones의 대표곡으로,\n"
                                           '        조용하고 부드러운 멜로디 속에 설명하기 어려운 아쉬움과 후회를 담고 있는 노래입니다.\n'
                                           '        노래 속 화자는 누군가에게 가지 않았던 자신의 행동을 떠올리며,\n'
                                           '        왜 그렇게 했는지 스스로도 알 수 없다고 말합니다.\n'
                                           '    </p>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           '        이 노래는 큰 사건을 직접적으로 설명하기보다,\n'
                                           '        마음속에 남아 있는 감정의 흔적을 천천히 보여 줍니다.\n'
                                           '        해가 뜰 때까지 기다렸지만 결국 가지 못했고,\n'
                                           '        새벽이 밝아오는 순간에는 차라리 멀리 날아가 버리고 싶어 합니다.\n'
                                           '        그래서 이 노래에는 후회, 망설임, 외로움, 그리움이 조용하게 섞여 있습니다.\n'
                                           '    </p>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           "        특히 <b>I don't know why I didn't come</b>이라는 문장이 반복되면서,\n"
                                           '        화자가 자신의 마음을 명확히 설명하지 못하는 상태가 잘 드러납니다.\n'
                                           '        이 반복 표현은 학생들이 듣고 따라 말하기 좋고,\n'
                                           "        <b>I don't know why</b>, <b>I wished that I could</b>,\n"
                                           '        <b>on my mind</b>, <b>empty as a drum</b> 같은 표현을 배우기에도 좋습니다.\n'
                                           '    </p>\n'
                                           '\n'
                                           '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                           '        수업에서는 이 노래를 통해 느린 영어 발음, 감정 표현,\n'
                                           '        후회와 그리움을 나타내는 문장을 함께 배울 수 있습니다.\n'
                                           '        속도가 빠르지 않고 분위기가 차분해서,\n'
                                           '        학생들이 영어 소리를 듣고 가사의 의미를 천천히 따라가기에 적합합니다.\n'
                                           '    </p>\n'
                                           '    ',
                                     'lyrics': [("I waited 'til I saw the sun / I don't know why I didn't come", '나는 해가 보일 때까지 기다렸어 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("I left you by the house of fun / Don't know why I didn't come", '나는 너를 즐거움의 집 곁에 남겨 두었어 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("Don't know why I didn't come", '왜 내가 가지 않았는지 모르겠어'),
                                                ('When I saw the break of day / I wished that I could fly away', '새벽이 밝아오는 것을 보았을 때 / 나는 날아가 버릴 수 있기를 바랐어'),
                                                ('Instead of kneeling in the sand / Catching tear-drops in my hand', '모래 위에 무릎 꿇고 있는 대신 / 손으로 눈물방울을 받으며'),
                                                ("My heart is drenched in wine / But you'll be on my mind forever",
                                                 '내 마음은 와인에 흠뻑 젖어 있지만 / 너는 영원히 내 마음속에 있을 거야'),
                                                ('Out across the endless sea / I would die in ecstasy', '끝없는 바다 저편으로 / 나는 황홀함 속에서 죽을 수도 있을 것 같아'),
                                                ("But I'll be a bag of bones / Driving down the road alone", '하지만 나는 뼈만 남은 사람처럼 / 혼자 길을 따라 운전하게 되겠지'),
                                                ("My heart is drenched in wine / But you'll be on my mind forever",
                                                 '내 마음은 와인에 흠뻑 젖어 있지만 / 너는 영원히 내 마음속에 있을 거야'),
                                                ("Something has to make you run / I don't know why I didn't come", '무언가가 너를 떠나게 만들었겠지 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("I feel as empty as a drum / I don't know why I didn't come", '나는 북처럼 텅 빈 기분이야 / 왜 내가 가지 않았는지 모르겠어'),
                                                ("Don't know why I didn't come / I don't know why I didn't come", '왜 내가 가지 않았는지 모르겠어 / 왜 내가 가지 않았는지 모르겠어')],
                                     'quiz': [{'q': '1. 화자는 무엇을 볼 때까지 기다렸나요?', 'options': ['버스', '해', '선생님', '전화'], 'answer': '해'},
                                              {'q': '2. 화자가 계속 모르겠다고 말하는 것은 무엇인가요?',
                                               'options': ['무엇을 먹을지', '학교가 어디인지', '왜 자신이 가지 않았는지', '어떻게 읽는지'],
                                               'answer': '왜 자신이 가지 않았는지'},
                                              {'q': "3. 'break of day'의 뜻으로 가장 알맞은 것은 무엇인가요?", 'options': ['한밤중', '점심시간', '새벽', '겨울'], 'answer': '새벽'},
                                              {'q': '4. 화자는 새벽을 보았을 때 무엇을 바랐나요?',
                                               'options': ['일찍 자는 것', '차를 사는 것', '수학을 공부하는 것', '날아가 버리는 것'],
                                               'answer': '날아가 버리는 것'},
                                              {'q': '5. 이 노래의 분위기로 가장 알맞은 것은 무엇인가요?',
                                               'options': ['조용하고 후회스러운 분위기', '화나고 시끄러운 분위기', '빠르고 웃긴 분위기', '신나고 거친 분위기'],
                                               'answer': '조용하고 후회스러운 분위기'},
                                              {'q': "6. 'You'll be on my mind forever'는 어떤 의미인가요?",
                                               'options': ['너는 곧 잊혀질 거야', '너는 영원히 내 마음속에 있을 거야', '너는 나와 함께 여행할 거야', '너는 노래를 부를 거야'],
                                               'answer': '너는 영원히 내 마음속에 있을 거야'},
                                              {'q': "7. 'I feel as empty as a drum'은 어떤 감정에 가깝나요?", 'options': ['배부름', '자신감', '공허함', '분노'], 'answer': '공허함'},
                                              {'q': '8. 이 노래에서 반복되는 핵심 문장은 무엇인가요?',
                                               'options': ['Stand by me', 'Let it go', 'A whole new world', "I don't know why I didn't come"],
                                               'answer': "I don't know why I didn't come"}],
                                     'key_expressions': [("I don't know why", '나는 왜 그런지 모르겠어'),
                                                         ("I didn't come", '나는 가지 않았어'),
                                                         ('The break of day', '새벽'),
                                                         ('I wished that I could fly away', '나는 날아가 버릴 수 있기를 바랐어'),
                                                         ('Tear-drops', '눈물방울'),
                                                         ('On my mind', '마음속에 있는'),
                                                         ('Forever', '영원히'),
                                                         ('Endless sea', '끝없는 바다'),
                                                         ('Driving down the road alone', '혼자 길을 따라 운전하며'),
                                                         ('Empty as a drum', '북처럼 텅 빈')],
                                     'matching': [("I don't know why", '나는 왜 그런지 모르겠어'),
                                                  ('I wished that I could fly away', '나는 날아가 버릴 수 있기를 바랐어'),
                                                  ("You'll be on my mind forever", '너는 영원히 내 마음속에 있을 거야'),
                                                  ('I feel as empty as a drum', '나는 북처럼 텅 빈 기분이야'),
                                                  ('I waited till I saw the sun', '나는 해가 보일 때까지 기다렸어'),
                                                  ('Driving down the road alone', '혼자 길을 따라 운전하며')],
                                     'reflect_questions': ['왜 그랬는지 스스로도 잘 설명할 수 없는 선택을 한 적이 있나요?',
                                                           '마음속에 오래 남아 있는 사람이나 기억이 있나요?',
                                                           '후회가 남는 일을 지금 다시 바라본다면 어떤 생각이 드나요?']},
 '6. Fix You - Coldplay': {'video_url': 'https://www.youtube.com/watch?v=Z0IZ3MjGFEo',
                           'bg': '\n'
                                 '    <h3 style="font-size:2.2rem; margin-bottom:20px; color:#2563eb;">\n'
                                 '        💡 Fix You: 힘든 순간에 건네는 위로\n'
                                 '    </h3>\n'
                                 '\n'
                                 '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                 '        Coldplay의 <b>Fix You</b>는 실패, 상실, 지침, 슬픔을 겪는 사람에게\n'
                                 '        따뜻한 위로를 건네는 노래입니다. 노래 속 화자는 상대가 최선을 다했지만\n'
                                 '        원하는 결과를 얻지 못했을 때, 그리고 잃어버린 것을 되돌릴 수 없을 때의\n'
                                 '        아픔을 조용히 바라봅니다.\n'
                                 '    </p>\n'
                                 '\n'
                                 '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                 '        이 노래에서 반복되는 <b>Lights will guide you home</b>은\n'
                                 '        어두운 순간에도 길을 비춰 주는 희망을 상징합니다.\n'
                                 '        또한 <b>I will try to fix you</b>는 상대를 완벽하게 고쳐 주겠다는 뜻이라기보다,\n'
                                 '        힘든 시간을 혼자 견디지 않도록 곁에서 도와주고 싶다는 마음으로 이해할 수 있습니다.\n'
                                 '    </p>\n'
                                 '\n'
                                 '    <p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">\n'
                                 "        수업에서는 <b>try your best</b>, <b>don't succeed</b>,\n"
                                 '        <b>what you want / what you need</b>, <b>stuck in reverse</b>,\n'
                                 '        <b>learn from my mistakes</b> 같은 표현을 중심으로 배울 수 있습니다.\n'
                                 '        특히 이 노래는 속도가 비교적 느리고 감정선이 분명해서,\n'
                                 '        학생들이 영어 표현과 함께 위로, 희망, 회복의 의미를 이해하기에 좋습니다.\n'
                                 '    </p>\n'
                                 '    ',
                           'lyrics': [("When you try your best, but you don't succeed / When you get what you want, but not what you need",
                                       '네가 최선을 다했지만 성공하지 못할 때 / 원하는 것을 얻었지만 정작 필요한 것은 얻지 못할 때'),
                                      ("When you feel so tired, but you can't sleep / Stuck in reverse", '너무 지쳤지만 잠들 수 없을 때 / 거꾸로 갇혀 있는 것처럼 느껴질 때'),
                                      ("And the tears come streaming down your face / When you lose something you can't replace",
                                       '눈물이 네 얼굴을 타고 흘러내릴 때 / 대신할 수 없는 무언가를 잃었을 때'),
                                      ('When you love someone, but it goes to waste / Could it be worse?', '누군가를 사랑했지만 그 마음이 헛되어 버렸을 때 / 이보다 더 나쁠 수 있을까?'),
                                      ('Lights will guide you home / And ignite your bones', '빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야'),
                                      ('And I will try to fix you', '그리고 나는 너를 다시 일으켜 주려고 노력할 거야'),
                                      ("And high up above or down below / When you're too in love to let it go", '저 높은 곳에 있든 아주 낮은 곳에 있든 / 너무 사랑해서 놓아주기 어려울 때'),
                                      ("But if you never try, you'll never know / Just what you're worth", '하지만 시도하지 않으면 절대 알 수 없어 / 네가 얼마나 소중한 사람인지'),
                                      ('Lights will guide you home / And ignite your bones', '빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야'),
                                      ('And I will try to fix you', '그리고 나는 너를 다시 일으켜 주려고 노력할 거야'),
                                      ('Tears stream down your face / When you lose something you cannot replace', '눈물이 네 얼굴을 타고 흘러내려 / 대신할 수 없는 무언가를 잃었을 때'),
                                      ('Tears stream down your face, and I / Tears stream down your face', '눈물이 네 얼굴을 타고 흘러내리고, 나는 / 눈물이 네 얼굴을 타고 흘러내려'),
                                      ('I promise you I will learn from my mistakes / Tears stream down your face, and I',
                                       '나는 내 실수에서 배우겠다고 약속할게 / 눈물이 네 얼굴을 타고 흘러내리고, 나는'),
                                      ('Lights will guide you home / And ignite your bones', '빛이 너를 집으로 인도할 거야 / 그리고 네 안의 힘을 다시 밝혀 줄 거야'),
                                      ('And I will try to fix you', '그리고 나는 너를 다시 일으켜 주려고 노력할 거야')],
                           'quiz': [{'q': '1. 이 노래에서 화자는 어떤 사람을 위로하고 있나요?',
                                     'options': ['시험을 준비하는 사람', '여행을 떠나는 사람', '힘들고 지친 사람', '운동을 시작한 사람'],
                                     'answer': '힘들고 지친 사람'},
                                    {'q': "2. 'When you try your best, but you don't succeed'의 의미로 가장 알맞은 것은 무엇인가요?",
                                     'options': ['최선을 다했지만 성공하지 못할 때', '아무 노력도 하지 않았을 때', '원하는 것을 모두 얻었을 때', '잠을 충분히 잤을 때'],
                                     'answer': '최선을 다했지만 성공하지 못할 때'},
                                    {'q': "3. 'what you want'와 'what you need'의 차이로 알맞은 것은 무엇인가요?",
                                     'options': ['둘 다 항상 같은 뜻이다', 'want는 원하는 것, need는 정말 필요한 것이다', 'want는 먹는 것, need는 노래하는 것이다', 'need는 필요 없는 것이다'],
                                     'answer': 'want는 원하는 것, need는 정말 필요한 것이다'},
                                    {'q': "4. 'Lights will guide you home'은 무엇을 상징한다고 볼 수 있나요?",
                                     'options': ['휴대전화 불빛', '가게의 간판', '어두운 길에서의 희망과 방향', '자동차 헤드라이트만'],
                                     'answer': '어두운 길에서의 희망과 방향'},
                                    {'q': "5. 'If you never try, you'll never know'의 의미로 가장 알맞은 것은 무엇인가요?",
                                     'options': ['절대 시도하면 안 된다', '시도하지 않으면 알 수 없다', '모든 것을 이미 알고 있다', '실패하면 끝이다'],
                                     'answer': '시도하지 않으면 알 수 없다'},
                                    {'q': "6. 'I will learn from my mistakes'는 어떤 태도를 보여 주나요?",
                                     'options': ['실수를 숨기려는 태도', '남을 탓하려는 태도', '포기하려는 태도', '실수에서 배우려는 태도'],
                                     'answer': '실수에서 배우려는 태도'},
                                    {'q': '7. 이 노래의 중심 감정으로 가장 알맞은 것은 무엇인가요?', 'options': ['위로와 희망', '웃음과 장난', '분노와 복수', '경쟁과 승리'], 'answer': '위로와 희망'},
                                    {'q': "8. 'I will try to fix you'는 어떤 의미에 가깝나요?",
                                     'options': ['너를 혼내겠다', '너를 완전히 바꾸겠다', '너를 떠나겠다', '너를 도와 다시 일어서게 하고 싶다'],
                                     'answer': '너를 도와 다시 일어서게 하고 싶다'}],
                           'key_expressions': [('Try your best', '최선을 다하다'),
                                               ("Don't succeed", '성공하지 못하다'),
                                               ('What you want', '네가 원하는 것'),
                                               ('What you need', '네게 필요한 것'),
                                               ('Stuck in reverse', '거꾸로 갇힌 듯한'),
                                               ('Tears stream down your face', '눈물이 얼굴을 타고 흐르다'),
                                               ("You can't replace", '대신할 수 없다'),
                                               ('Lights will guide you home', '빛이 너를 집으로 인도할 거야'),
                                               ('Ignite your bones', '네 안의 힘을 다시 밝혀 주다'),
                                               ('Learn from my mistakes', '내 실수에서 배우다')],
                           'matching': [('When you try your best', '네가 최선을 다할 때'),
                                        ('Lights will guide you home', '빛이 너를 집으로 인도할 거야'),
                                        ('I will try to fix you', '나는 너를 다시 일으켜 주려고 노력할 거야'),
                                        ("If you never try, you'll never know", '시도하지 않으면 절대 알 수 없어'),
                                        ('Tears stream down your face', '눈물이 네 얼굴을 타고 흘러내려'),
                                        ('I will learn from my mistakes', '나는 내 실수에서 배울 거야')],
                           'reflect_questions': ['최선을 다했지만 원하는 결과를 얻지 못했던 경험이 있나요?', '힘들 때 나를 다시 일으켜 준 사람이나 말이 있었나요?', '나도 누군가를 위로하거나 도와주고 싶었던 적이 있나요?']},
 '7. The Scientist - Coldplay': {'video_url': 'https://www.youtube.com/watch?v=kV82ahVRPFg&list=RDkV82ahVRPFg&start_radio=1',
                                 'bg': '<h3 style="font-size:2.2rem; margin-bottom:20px; color:#2563eb;">🔬 The Scientist: 처음으로 돌아가고 싶은 마음</h3>\n'
                                       '<p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">Coldplay의 <b>The Scientist</b>는 지나간 관계와 후회를 돌아보며, 처음으로 '
                                       '돌아가 다시 말하고 싶은 마음을 담은 노래입니다.</p>\n'
                                       '<p style="font-size:1.35rem; line-height:2.0; color:#1e293b;">노래 속 화자는 사랑과 이별을 과학처럼 분석하려 하지만, 마음은 숫자와 공식처럼 쉽게 설명되지 '
                                       '않는다는 것을 깨닫습니다.</p>',
                                 'lyrics': [
    ("Come up to meet you, tell you I′m sorry", "너를 만나러 와서 미안하다고 말하려 해"),
    ("You don't know how lovely you are", "너는 네가 얼마나 사랑스러운지 몰라"),
    ("I had to find you, tell you I need you", "나는 너를 찾아야 했고, 네가 필요하다고 말해야 했어"),
    ("Tell you I set you apart", "네가 나에게 특별하다고 말해야 했어"),
    ("Tell me your secrets and ask me your questions", "네 비밀을 말해 주고, 내게 질문을 해 줘"),
    ("Oh, let′s go back to the start", "오, 처음으로 돌아가자"),
    ("Runnin' in circles, comin' up tails", "빙빙 돌며, 계속 좋지 않은 결과가 나오고 있어"),
    ("Heads on a science apart", "머리는 과학처럼 따로 떨어져 있어"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("It′s such a shame for us to part", "우리가 헤어진다는 건 정말 안타까운 일이야"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("No one ever said it would be this hard", "아무도 이렇게 힘들 거라고 말하지 않았어"),
    ("Oh, take me back to the start", "오, 나를 처음으로 데려가 줘"),
    ("I was just guessing at numbers and figures", "나는 그저 숫자와 수치를 추측하고 있었어"),
    ("Pulling the puzzles apart", "퍼즐을 하나하나 떼어 내며"),
    ("Questions of science, science and progress", "과학의 질문들, 과학과 진보는"),
    ("Do not speak as loud as my heart", "내 마음만큼 크게 말하지 못해"),
    ("But tell me you love me, come back and haunt me", "하지만 나를 사랑한다고 말해 줘, 돌아와 나를 계속 맴돌아 줘"),
    ("Oh, and I rush to the start", "오, 나는 서둘러 처음으로 돌아가"),
    ("Runnin′ in circles, chasin' our tails", "빙빙 돌며, 우리의 꼬리를 쫓듯 같은 자리를 맴돌아"),
    ("Coming back as we are", "있는 그대로의 우리로 돌아오며"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("Oh, it′s such a shame for us to part", "오, 우리가 헤어진다는 건 정말 안타까운 일이야"),
    ("Nobody said it was easy", "아무도 그것이 쉽다고 말하지 않았어"),
    ("No one ever said it would be so hard", "아무도 이렇게 힘들 거라고 말하지 않았어"),
    ("I'm going back to the start", "나는 처음으로 돌아가고 있어"),
],
                                 'quiz': [{'q': '1. 화자가 상대에게 가장 먼저 말하고 싶은 것은 무엇인가요?',
                                           'options': ['미안하다는 말', '축하한다는 말', '화났다는 말', '떠나자는 말'],
                                           'answer': '미안하다는 말'},
                                          {'q': "2. “You don't know how lovely you are”의 의미는 무엇인가요?",
                                           'options': ['너는 네가 얼마나 사랑스러운지 모른다', '너는 나를 전혀 모른다', '너는 과학을 좋아한다', '너는 돌아오지 않는다'],
                                           'answer': '너는 네가 얼마나 사랑스러운지 모른다'},
                                          {'q': "3. “Let's go back to the start”의 의미는 무엇인가요?",
                                           'options': ['처음으로 돌아가자', '학교로 가자', '과학을 공부하자', '집에 가자'],
                                           'answer': '처음으로 돌아가자'},
                                          {'q': '4. “Running in circles”는 어떤 상태를 나타내나요?',
                                           'options': ['같은 자리를 맴도는 상태', '빠르게 성공하는 상태', '잠을 자는 상태', '완전히 잊은 상태'],
                                           'answer': '같은 자리를 맴도는 상태'},
                                          {'q': '5. “Nobody said it was easy”의 의미는 무엇인가요?',
                                           'options': ['아무도 쉽다고 말하지 않았다', '모두 쉽다고 말했다', '과학은 쉽다', '사랑은 항상 쉽다'],
                                           'answer': '아무도 쉽다고 말하지 않았다'},
                                          {'q': '6. “Do not speak as loud as my heart”는 어떤 뜻에 가깝나요?',
                                           'options': ['이성과 과학보다 마음의 소리가 더 크다', '심장이 실제로 소리를 낸다', '과학이 가장 중요하다', '말을 하지 말라는 뜻이다'],
                                           'answer': '이성과 과학보다 마음의 소리가 더 크다'},
                                          {'q': '7. 화자가 반복해서 돌아가고 싶어 하는 곳은 어디인가요?', 'options': ['처음', '학교', '바다', '무대'], 'answer': '처음'},
                                          {'q': '8. 이 노래의 중심 감정은 무엇인가요?', 'options': ['후회와 그리움', '분노와 복수', '승리와 환호', '웃음과 장난'], 'answer': '후회와 그리움'}],
                                 'key_expressions': [("Tell you I'm sorry", '미안하다고 말하다'),
                                                     ('How lovely you are', '네가 얼마나 사랑스러운지'),
                                                     ('I had to find you', '나는 너를 찾아야 했어'),
                                                     ('I need you', '네가 필요해'),
                                                     ('I set you apart', '나는 너를 특별하게 여겨'),
                                                     ('Tell me your secrets', '네 비밀을 말해 줘'),
                                                     ("Let's go back to the start", '처음으로 돌아가자'),
                                                     ('Running in circles', '빙빙 돌다'),
                                                     ('Nobody said it was easy', '아무도 그것이 쉽다고 말하지 않았어'),
                                                     ('Take me back to the start', '나를 처음으로 데려가 줘')],
                                 'matching': [("Tell you I'm sorry", '미안하다고 말하다'),
                                              ("You don't know how lovely you are", '너는 네가 얼마나 사랑스러운지 몰라'),
                                              ('Tell you I need you', '네가 필요하다고 말하다'),
                                              ("Let's go back to the start", '처음으로 돌아가자'),
                                              ('Nobody said it was easy', '아무도 그것이 쉽다고 말하지 않았어'),
                                              ("I'm going back to the start", '나는 처음으로 돌아가고 있어')],
                                 'reflect_questions': ['당신도 가수처럼 그리운 옛 연인이나 다시 이야기하고 싶은 사람이 있나요?',
                                                       '처음으로 돌아갈 수 있다면 다시 말하고 싶은 말은 무엇인가요?',
                                                       '사랑이나 관계가 생각보다 쉽지 않았다고 느낀 경험이 있나요?']}}


BACKGROUND_CONTENT = {
    "1. Let It Go - Frozen OST": {
        "title": "❄️ Let It Go: 숨겨 왔던 자신을 받아들이는 순간",
        "paragraphs": [
            "Let It Go는 영화 Frozen의 대표곡으로, 엘사가 더 이상 자신의 능력과 감정을 숨기지 않고 스스로를 받아들이는 장면에서 나오는 노래입니다. 엘사는 왕국의 공주이지만, 자신의 얼음 마법이 다른 사람을 다치게 할 수 있다는 두려움 때문에 늘 조심하며 살아왔습니다.",
            "어릴 때부터 엘사는 감정을 숨기고, 능력을 감추고, ‘착한 아이’처럼 행동해야 한다는 압박을 받았습니다. 하지만 대관식 날 능력이 사람들 앞에서 드러나자, 사람들은 엘사를 이해하기보다 두려워합니다. 결국 엘사는 모든 시선과 책임을 피해 눈 덮인 산으로 도망칩니다.",
            "산 위에서 엘사는 처음으로 자신의 진짜 모습을 마주합니다. 이 노래는 단순히 ‘다 잊어버리자’는 의미가 아니라, 그동안 억눌렀던 두려움, 책임감, 타인의 시선에서 벗어나 자기 자신을 받아들이는 과정을 보여 줍니다.",
            "수업에서는 let it go, conceal, hold back, storm inside, I'm free, the past is in the past 같은 표현을 중심으로 배울 수 있습니다. 특히 이 노래는 자유, 두려움, 자기표현, 자신감에 대해 학생들과 이야기하기 좋은 자료입니다."
        ],
    },
    "2. Hello - Adele": {
        "title": "☎️ Hello: 과거의 누군가에게 건네는 늦은 안부",
        "paragraphs": [
            "Adele의 Hello는 시간이 많이 흐른 뒤, 과거의 누군가에게 다시 연락하고 싶은 마음을 담은 노래입니다. 노래 속 화자는 상대에게 전화를 걸며 오래전의 관계, 미안함, 후회, 그리고 아직 완전히 치유되지 않은 감정을 떠올립니다.",
            "이 노래에서 화자는 단순히 ‘안녕’이라고 말하는 것이 아닙니다. 과거에 하지 못했던 사과를 조심스럽게 꺼내고 싶어 합니다. 하지만 두 사람 사이에는 시간의 거리, 마음의 거리, 그리고 실제 거리까지 생겨 있습니다.",
            "반복되는 Hello라는 말은 인사이면서 동시에 사과의 시작처럼 들립니다. 화자는 내가 너무 늦은 것은 아닐까, 상대는 이미 괜찮아진 것은 아닐까 생각하면서도, 적어도 자신은 말하려고 노력했다고 고백합니다.",
            "수업에서는 I'm sorry, I tried, after all these years, used to be, the other side 같은 표현을 중심으로 배울 수 있습니다. 학생들은 이 노래를 통해 사과, 후회, 시간의 흐름, 그리고 관계의 거리감을 영어 표현과 함께 이해할 수 있습니다."
        ],
    },
    "3. A Whole New World - Aladdin OST": {
        "title": "🕌 A Whole New World: 새로운 세상을 바라보는 순간",
        "paragraphs": [
            "A Whole New World는 영화 Aladdin의 대표곡으로, 알라딘과 자스민이 마법 양탄자를 타고 밤하늘을 날며 새로운 세상을 바라보는 장면에서 나오는 노래입니다. 이 장면은 단순한 낭만적인 비행이 아니라, 자스민이 처음으로 궁전 밖의 세상을 직접 경험하는 순간입니다.",
            "자스민은 공주로서 화려한 삶을 살지만, 정해진 규칙과 역할 속에서 자유롭게 세상을 경험하지 못했습니다. 알라딘은 그런 자스민에게 궁전 밖의 넓은 세상과 새로운 가능성을 보여 줍니다.",
            "이 노래에서 a whole new world는 새로운 장소만을 뜻하지 않습니다. 새로운 시선, 새로운 경험, 그리고 스스로 선택할 수 있는 자유를 의미합니다. 두 사람은 두려움보다 설렘이 더 큰 세계로 함께 나아갑니다.",
            "수업에서는 I can show you the world, open your eyes, point of view, crystal clear, new horizons 같은 표현을 중심으로 배울 수 있습니다. 학생들에게 ‘내가 경험해 보고 싶은 새로운 세상’이나 ‘나에게 새로운 관점을 보여 준 사람’을 생각하게 할 수 있습니다."
        ],
    },
    "4. Stand By Me - Ben E. King": {
        "title": "🤝 Stand By Me: 곁에 있어 주는 힘",
        "paragraphs": [
            "Stand By Me는 어둡고 불안한 순간에도 누군가가 내 곁에 있어 준다면 두렵지 않다는 메시지를 담은 노래입니다. 제목의 stand by me는 단순히 ‘내 옆에 서 있어’가 아니라, ‘내 곁에 있어 줘’, ‘나를 지켜 줘’, ‘함께해 줘’라는 의미로 이해할 수 있습니다.",
            "노래는 밤이 찾아오고 세상이 어두워지는 장면으로 시작합니다. 달빛만 보이는 상황은 불안과 두려움을 상징하지만, 화자는 혼자가 아니라는 믿음 때문에 두려워하지 않겠다고 말합니다.",
            "하늘이 무너지고 산이 바다로 무너져 내리는 듯한 극단적인 표현은 삶에서 마주할 수 있는 큰 어려움을 나타냅니다. 하지만 사랑하는 사람이 곁에 있다면 그 모든 상황도 견딜 수 있다고 노래합니다.",
            "수업에서는 I won't be afraid, I won't cry, shed a tear, whenever you're in trouble 같은 표현을 중심으로 배울 수 있습니다. 친구, 가족, 사랑하는 사람이 주는 안정감과 용기를 이야기하기에 좋은 노래입니다."
        ],
    },
    "5. Don't Know Why - Norah Jones": {
        "title": "🌙 Don't Know Why: 이유를 알 수 없는 마음",
        "paragraphs": [
            "Don't Know Why는 Norah Jones의 대표곡으로, 조용하고 부드러운 멜로디 속에 설명하기 어려운 아쉬움과 후회를 담고 있는 노래입니다. 노래 속 화자는 누군가에게 가지 않았던 자신의 행동을 떠올리며, 왜 그렇게 했는지 스스로도 알 수 없다고 말합니다.",
            "이 노래는 큰 사건을 직접적으로 설명하지 않습니다. 대신 마음속에 남아 있는 감정의 흔적을 천천히 보여 줍니다. 해가 뜰 때까지 기다렸지만 결국 가지 못했고, 새벽이 밝아오는 순간에는 차라리 멀리 날아가 버리고 싶어 합니다.",
            "I don't know why I didn't come이라는 문장이 반복되면서, 화자가 자신의 마음을 명확히 설명하지 못하는 상태가 잘 드러납니다. 이 반복 속에는 후회, 망설임, 외로움, 그리움이 조용하게 섞여 있습니다.",
            "수업에서는 I don't know why, I wished that I could, on my mind, empty as a drum 같은 표현을 중심으로 배울 수 있습니다. 학생들이 이유를 설명하기 어려운 감정과 후회를 영어로 표현해 보는 활동으로 연결하기 좋습니다."
        ],
    },
    "6. Fix You - Coldplay": {
        "title": "💡 Fix You: 힘든 순간에 건네는 위로",
        "paragraphs": [
            "Coldplay의 Fix You는 실패, 상실, 지침, 슬픔을 겪는 사람에게 따뜻한 위로를 건네는 노래입니다. 노래 속 화자는 상대가 최선을 다했지만 원하는 결과를 얻지 못했을 때, 그리고 잃어버린 것을 되돌릴 수 없을 때의 아픔을 조용히 바라봅니다.",
            "반복되는 Lights will guide you home은 어두운 순간에도 길을 비춰 주는 희망을 상징합니다. 또한 I will try to fix you는 상대를 완벽하게 고쳐 주겠다는 뜻이라기보다, 힘든 시간을 혼자 견디지 않도록 곁에서 도와주고 싶다는 마음으로 이해할 수 있습니다.",
            "이 노래는 실패를 부끄러운 것으로만 보지 않습니다. 오히려 실수에서 배우고, 무너진 자리에서 다시 일어설 수 있다는 가능성을 보여 줍니다. 그래서 이 노래는 위로와 회복의 메시지를 전달합니다.",
            "수업에서는 try your best, don't succeed, what you want / what you need, stuck in reverse, learn from my mistakes 같은 표현을 중심으로 배울 수 있습니다. 학생들에게 ‘나를 다시 일으켜 준 사람’이나 ‘내가 누군가에게 해 줄 수 있는 위로’를 생각하게 할 수 있습니다."
        ],
    },
    "7. The Scientist - Coldplay": {
        "title": "🔬 The Scientist: 처음으로 돌아가고 싶은 마음",
        "paragraphs": [
            "Coldplay의 The Scientist는 지나간 관계와 후회를 돌아보며, 처음으로 돌아가 다시 말하고 싶은 마음을 담은 노래입니다. 노래 속 화자는 사랑과 이별을 과학처럼 분석하려 하지만, 마음은 숫자와 공식처럼 쉽게 설명되지 않는다는 것을 깨닫습니다.",
            "Come up to meet you, tell you I'm sorry는 상대를 다시 만나 사과하고 싶은 마음을 보여 줍니다. Tell you I need you, Tell you I set you apart는 상대가 자신에게 얼마나 특별한 존재였는지를 뒤늦게 깨닫는 표현입니다.",
            "반복되는 Let's go back to the start와 Take me back to the start는 단순히 과거로 돌아가고 싶다는 뜻을 넘어, 관계가 어긋나기 전의 순수한 순간으로 돌아가고 싶은 마음을 나타냅니다. 이 노래의 핵심 감정은 후회, 그리움, 미안함, 그리고 다시 시작하고 싶은 마음입니다.",
            "수업에서는 tell you I'm sorry, I need you, set you apart, go back to the start, nobody said it was easy 같은 표현을 중심으로 배울 수 있습니다. 또한 ‘다시 돌아가고 싶은 순간’, ‘그때 하지 못한 말’, ‘관계가 왜 생각보다 어려운가’를 주제로 reflective writing을 하기에 좋습니다."
        ],
    },
}


def show_background(song_choice, data):
    """배경 학습 탭만 HTML/컴포넌트 없이 안정적으로 크게 출력합니다."""
    bg = BACKGROUND_CONTENT.get(song_choice)
    if bg is None:
        bg = {
            "title": "🎵 배경 학습",
            "paragraphs": [str(data.get("bg", "")).replace("<br>", " ").replace("<p>", "").replace("</p>", "")]
        }

    st.markdown('<div class="bg-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="bg-title">{bg["title"]}</div>', unsafe_allow_html=True)
    for p in bg["paragraphs"]:
        st.markdown(f'<div class="bg-p">{p}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


if "selected_song" not in st.session_state:
    st.session_state.selected_song = list(SONGS.keys())[0]
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🎬 배경 학습"

def sync_song():
    for k in list(st.session_state.keys()):
        if k.startswith(("quiz_", "keygame_", "match_", "reflect_")):
            del st.session_state[k]

st.markdown('<div class="main-title"><h1>🎵 Pop Song English Learning</h1></div>', unsafe_allow_html=True)
song_options = list(SONGS.keys())
song_choice = st.selectbox("👉 학습할 노래를 선택하세요", song_options, index=song_options.index(st.session_state.selected_song) if st.session_state.selected_song in song_options else 0, on_change=sync_song, key="song_selector")
st.session_state.selected_song = song_choice
data = SONGS[song_choice]

tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "📝 Key Expression 뜻 맞추기", "🧩 문장 매칭 게임", "✍️ 생각 적기"]
selected_tab = st.radio("학습 단계", tabs_list, horizontal=True, key="current_tab")

if selected_tab == "🎬 배경 학습":
    show_background(song_choice, data)
    st.video(data["video_url"])
    st.markdown(
        """
        <div class="game-card">
            <div class="big-guide">
            노래를 듣기 전에 배경을 먼저 읽고, 화자의 감정과 상황을 생각해 보세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


elif selected_tab == "📖 가사 & 퀴즈":
    st.subheader("🎬 노래 영상")
    st.video(data["video_url"])
    st.markdown("---")
    st.subheader("📖 전체 가사와 한국어 해석")
    for en, ko in data["lyrics"]:
        st.markdown(f"""
        <div class="lyrics-container">
            <div class="eng-line">{clean_text_for_display(en)}</div>
            <div class="kor-sub">{clean_text_for_display(ko)}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("✅ 내용 이해 문제 8문항")
    st.markdown('<div class="quiz-box"><b>전체 가사를 읽은 뒤 문제를 풀어 봅시다.</b><br>화자의 상황, 감정, 반복되는 표현을 중심으로 생각하면 됩니다.</div>', unsafe_allow_html=True)
    quiz_key = safe_key(song_choice)
    user_answers = []
    for i, item in enumerate(data["quiz"], start=1):
        q = item["q"]
        q_text = q if str(q).strip().startswith(str(i)) else f"{i}. {q}"
        options = shuffle_options(item["options"], seed=f"{quiz_key}_quiz_{i}")
        picked = st.radio(q_text, options, key=f"quiz_{quiz_key}_{i}", index=None)
        user_answers.append((q_text, picked, item["answer"]))
    c1, c2 = st.columns(2)
    with c1:
        submit_quiz = st.button("정답 확인", key=f"quiz_submit_{quiz_key}", use_container_width=True)
    with c2:
        if st.button("다시 풀기", key=f"quiz_reset_{quiz_key}", use_container_width=True):
            for k in list(st.session_state.keys()):
                if k.startswith(f"quiz_{quiz_key}_"):
                    del st.session_state[k]
            st.rerun()
    if submit_quiz:
        score = sum(1 for _, picked, answer in user_answers if picked == answer)
        st.markdown(f'<div class="score-box">점수: {score} / {len(user_answers)}</div>', unsafe_allow_html=True)
        for idx, (_, picked, answer) in enumerate(user_answers, start=1):
            if picked == answer:
                st.success(f"{idx}번 정답입니다. ✅")
            else:
                st.markdown(f'<div class="wrong-box"><b>{idx}번</b> 다시 확인해 보세요.<br>내가 고른 답: {clean_text_for_display(picked) if picked else "선택 안 함"}<br>정답: <b>{clean_text_for_display(answer)}</b></div>', unsafe_allow_html=True)

elif selected_tab == "📝 Key Expression 뜻 맞추기":
    st.subheader("📝 Key Expression 뜻 맞추기")
    st.markdown(
        '<div class="game-card"><div class="big-guide">'
        '영어 표현을 보고 한국어 뜻을 고르는 문제와, 한국어 뜻을 보고 영어 표현을 고르는 문제가 섞여 나옵니다.<br>'
        '각 노래마다 중요한 표현 10개를 양방향으로 연습합니다.'
        '</div></div>',
        unsafe_allow_html=True
    )

    key_key = safe_key(song_choice)
    expressions = data["key_expressions"]

    all_english_options = [en for en, _ in expressions]
    all_korean_options = [ko for _, ko in expressions]

    user_answers = []

    for i, (en, ko) in enumerate(expressions, start=1):
        # 곡명과 번호를 seed로 사용해 문제 방향을 섞습니다.
        # 새로고침해도 같은 곡에서는 문제 방향이 안정적으로 유지됩니다.
        direction_rng = random.Random(f"{key_key}_direction_{i}")
        direction = direction_rng.choice(["en_to_ko", "ko_to_en"])

        rng = random.Random(f"{key_key}_keygame_{i}")

        if direction == "en_to_ko":
            # 영어 표현 → 한국어 뜻 고르기
            distractors = [x for x in all_korean_options if x != ko]
            wrongs = rng.sample(distractors, k=min(3, len(distractors)))
            options = shuffle_options(wrongs + [ko], seed=f"{key_key}_keygame_options_{i}")

            st.markdown(f"### {i}. {en}")
            picked = st.radio(
                "알맞은 한국어 뜻을 고르세요.",
                options,
                key=f"keygame_{key_key}_{i}",
                index=None
            )

            user_answers.append({
                "direction": "en_to_ko",
                "question": en,
                "picked": picked,
                "answer": ko,
                "en": en,
                "ko": ko,
            })

        else:
            # 한국어 뜻 → 영어 표현 고르기
            distractors = [x for x in all_english_options if x != en]
            wrongs = rng.sample(distractors, k=min(3, len(distractors)))
            options = shuffle_options(wrongs + [en], seed=f"{key_key}_keygame_options_{i}")

            st.markdown(f"### {i}. {ko}")
            picked = st.radio(
                "알맞은 영어 표현을 고르세요.",
                options,
                key=f"keygame_{key_key}_{i}",
                index=None
            )

            user_answers.append({
                "direction": "ko_to_en",
                "question": ko,
                "picked": picked,
                "answer": en,
                "en": en,
                "ko": ko,
            })

    c1, c2 = st.columns(2)

    with c1:
        submit_key = st.button(
            "Key Expression 정답 확인",
            key=f"keygame_submit_{key_key}",
            use_container_width=True
        )

    with c2:
        if st.button(
            "Key Expression 다시 풀기",
            key=f"keygame_reset_{key_key}",
            use_container_width=True
        ):
            for k in list(st.session_state.keys()):
                if k.startswith(f"keygame_{key_key}_"):
                    del st.session_state[k]
            st.rerun()

    if submit_key:
        score = sum(1 for item in user_answers if item["picked"] == item["answer"])
        st.markdown(
            f'<div class="score-box">점수: {score} / {len(user_answers)}</div>',
            unsafe_allow_html=True
        )

        for idx, item in enumerate(user_answers, start=1):
            en = item["en"]
            ko = item["ko"]
            picked = item["picked"]
            answer = item["answer"]

            if picked == answer:
                st.success(f"{idx}번 정답 ✅  {en} = {ko}")
            else:
                st.error(
                    f"{idx}번 오답 ❌  정답: {answer}\n\n"
                    f"전체 표현: {en} = {ko}"
                )


elif selected_tab == "🧩 문장 매칭 게임":
    match_key = safe_key(song_choice)

    pairs = [
        {
            "id": f"pair_{i}",
            "en": en,
            "ko": ko
        }
        for i, (en, ko) in enumerate(data["matching"], start=1)
    ]

    en_cards = [{"id": p["id"], "text": p["en"]} for p in pairs]
    ko_cards = [{"id": p["id"], "text": p["ko"]} for p in pairs]

    en_cards = shuffle_options(en_cards, seed=f"{match_key}_en")
    ko_cards = shuffle_options(ko_cards, seed=f"{match_key}_ko")

    payload = {
        "en": en_cards,
        "ko": ko_cards,
        "total": len(pairs),
    }

    data_json = json.dumps(payload, ensure_ascii=False)
    component_id = "match_" + uuid.uuid4().hex

    components.html(
        f"""
        <div id="{component_id}" class="match-app">
            <div class="match-head">
                <div class="match-title">🧩 문장 매칭 게임</div>
                <div class="match-guide">
                    왼쪽 영어 표현과 오른쪽 한국어 뜻을 차례로 눌러 짝을 맞추세요.<br>
                    선택한 박스는 색칠되고, 정답이면 두 박스가 반짝이며 함께 사라집니다.
                </div>
            </div>

            <div class="match-status">
                <div id="status_{component_id}">먼저 영어 또는 한국어 박스를 하나 선택하세요.</div>
                <div id="score_{component_id}">맞춘 개수: 0 / {len(pairs)}</div>
            </div>

            <div class="match-board">
                <div class="match-col">
                    <div class="col-title">English</div>
                    <div id="en_{component_id}" class="card-wrap"></div>
                </div>
                <div class="match-col">
                    <div class="col-title">Korean</div>
                    <div id="ko_{component_id}" class="card-wrap"></div>
                </div>
            </div>

            <div class="progress-outer">
                <div id="bar_{component_id}" class="progress-inner"></div>
            </div>

            <button id="reset_{component_id}" class="reset-btn">매칭 게임 다시 시작</button>
        </div>

        <style>
            #{component_id}.match-app {{
                font-family: Arial, sans-serif;
                width: 100%;
                box-sizing: border-box;
                background: linear-gradient(135deg,#eef2ff 0%,#f0f9ff 50%,#fdf2f8 100%);
                border: 1px solid #c7d2fe;
                border-radius: 22px;
                padding: 22px;
                margin: 8px 0 22px 0;
                color: #1e293b;
            }}

            #{component_id} .match-head {{
                background: rgba(255,255,255,0.72);
                border: 1px solid #dbeafe;
                border-radius: 18px;
                padding: 18px 20px;
                margin-bottom: 16px;
            }}

            #{component_id} .match-title {{
                font-size: 30px;
                font-weight: 1000;
                color: #4338ca;
                margin-bottom: 8px;
            }}

            #{component_id} .match-guide {{
                font-size: 16px;
                font-weight: 800;
                color: #475569;
                line-height: 1.7;
            }}

            #{component_id} .match-status {{
                display: grid;
                grid-template-columns: 1.5fr 0.8fr;
                gap: 10px;
                margin-bottom: 14px;
                align-items: center;
            }}

            #{component_id} .match-status > div {{
                background: #ffffff;
                border: 1px solid #dbeafe;
                border-radius: 14px;
                padding: 12px 14px;
                font-size: 15px;
                font-weight: 900;
                color: #1d4ed8;
                min-height: 24px;
            }}

            #{component_id} .match-board {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 14px;
            }}

            #{component_id} .match-col {{
                background: rgba(255,255,255,0.72);
                border: 1px solid #e5e7eb;
                border-radius: 18px;
                padding: 14px;
            }}

            #{component_id} .col-title {{
                font-size: 22px;
                font-weight: 1000;
                color: #111827;
                margin-bottom: 12px;
            }}

            #{component_id} .card-wrap {{
                display: flex;
                flex-direction: column;
                gap: 10px;
            }}

            #{component_id} .match-card {{
                width: 100%;
                text-align: left;
                border: 2px solid #c7d2fe;
                background: #ffffff;
                color: #1e293b;
                border-radius: 16px;
                padding: 14px 15px;
                font-size: 17px;
                font-weight: 900;
                line-height: 1.55;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(15,23,42,0.06);
                transition: transform .16s ease, background .16s ease, border-color .16s ease, box-shadow .16s ease;
                position: relative;
                overflow: hidden;
            }}

            #{component_id} .match-card:hover {{
                transform: translateY(-2px);
                border-color: #818cf8;
                box-shadow: 0 8px 18px rgba(99,102,241,0.16);
            }}

            #{component_id} .match-card.selected {{
                background: linear-gradient(135deg,#fef3c7 0%,#fde68a 100%);
                border-color: #f59e0b;
                color: #78350f;
                box-shadow: 0 0 0 4px rgba(245,158,11,0.18), 0 8px 20px rgba(245,158,11,0.22);
                transform: scale(1.015);
            }}

            #{component_id} .match-card.wrong {{
                animation: shake_{component_id} .28s ease-in-out;
                background: #fee2e2;
                border-color: #ef4444;
                color: #7f1d1d;
            }}

            #{component_id} .match-card.correct {{
                background: linear-gradient(135deg,#dcfce7,#bbf7d0);
                border-color: #22c55e;
                color: #14532d;
                animation: sparkleDisappear_{component_id} .68s ease forwards;
            }}

            #{component_id} .match-card.correct::after {{
                content: "✨";
                position: absolute;
                inset: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 34px;
                background: radial-gradient(circle, rgba(255,255,255,0.95), rgba(255,255,255,0.20), rgba(255,255,255,0));
                animation: sparkleFlash_{component_id} .68s ease forwards;
                pointer-events: none;
            }}

            @keyframes sparkleDisappear_{component_id} {{
                0% {{ opacity: 1; transform: scale(1); max-height: 220px; margin-bottom: 0; }}
                35% {{ opacity: 1; transform: scale(1.04); }}
                70% {{ opacity: .55; transform: scale(.96); max-height: 220px; }}
                100% {{ opacity: 0; transform: scale(.86); max-height: 0; padding-top: 0; padding-bottom: 0; border-width: 0; margin: 0; }}
            }}

            @keyframes sparkleFlash_{component_id} {{
                0% {{ opacity: 0; transform: scale(.6) rotate(0deg); }}
                35% {{ opacity: 1; transform: scale(1.25) rotate(8deg); }}
                100% {{ opacity: 0; transform: scale(1.7) rotate(-10deg); }}
            }}

            @keyframes shake_{component_id} {{
                0%, 100% {{ transform: translateX(0); }}
                25% {{ transform: translateX(-5px); }}
                50% {{ transform: translateX(5px); }}
                75% {{ transform: translateX(-3px); }}
            }}

            #{component_id} .progress-outer {{
                width: 100%;
                height: 14px;
                background: #e5e7eb;
                border-radius: 999px;
                overflow: hidden;
                margin: 16px 0 12px 0;
            }}

            #{component_id} .progress-inner {{
                height: 100%;
                width: 0%;
                background: linear-gradient(90deg,#60a5fa,#a78bfa,#f472b6);
                border-radius: 999px;
                transition: width .28s ease;
            }}

            #{component_id} .reset-btn {{
                width: 100%;
                border: 1px solid #c7d2fe;
                background: #ffffff;
                color: #4338ca;
                border-radius: 999px;
                min-height: 46px;
                font-size: 16px;
                font-weight: 1000;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(15,23,42,0.05);
            }}

            #{component_id} .reset-btn:hover {{
                background: #eef2ff;
            }}

            #{component_id} .done-message {{
                background: linear-gradient(135deg,#dcfce7,#bbf7d0);
                border: 1px solid #86efac;
                color: #14532d;
                border-radius: 16px;
                padding: 16px;
                margin-top: 14px;
                font-size: 20px;
                font-weight: 1000;
                text-align: center;
                animation: pop_{component_id} .45s ease;
            }}

            @keyframes pop_{component_id} {{
                0% {{ transform: scale(.92); opacity: 0; }}
                100% {{ transform: scale(1); opacity: 1; }}
            }}

            @media (max-width: 720px) {{
                #{component_id} .match-board {{
                    grid-template-columns: 1fr;
                }}
                #{component_id} .match-status {{
                    grid-template-columns: 1fr;
                }}
                #{component_id} .match-card {{
                    font-size: 15px;
                }}
            }}
        </style>

        <script>
            const data_{component_id} = {data_json};
            const root_{component_id} = document.getElementById("{component_id}");
            const enBox_{component_id} = document.getElementById("en_{component_id}");
            const koBox_{component_id} = document.getElementById("ko_{component_id}");
            const status_{component_id} = document.getElementById("status_{component_id}");
            const score_{component_id} = document.getElementById("score_{component_id}");
            const bar_{component_id} = document.getElementById("bar_{component_id}");
            const reset_{component_id} = document.getElementById("reset_{component_id}");

            let selected_{component_id} = null;
            let done_{component_id} = new Set();
            let locked_{component_id} = false;

            function escapeHtml_{component_id}(str) {{
                return String(str)
                    .replaceAll("&", "&amp;")
                    .replaceAll("<", "&lt;")
                    .replaceAll(">", "&gt;")
                    .replaceAll('"', "&quot;")
                    .replaceAll("'", "&#039;");
            }}

            function makeCard_{component_id}(card, kind) {{
                const btn = document.createElement("button");
                btn.className = "match-card";
                btn.dataset.id = card.id;
                btn.dataset.kind = kind;
                btn.innerHTML = escapeHtml_{component_id}(card.text);
                btn.addEventListener("click", () => handleClick_{component_id}(btn, card, kind));
                return btn;
            }}

            function render_{component_id}() {{
                enBox_{component_id}.innerHTML = "";
                koBox_{component_id}.innerHTML = "";

                data_{component_id}.en.forEach(card => {{
                    if (!done_{component_id}.has(card.id)) {{
                        enBox_{component_id}.appendChild(makeCard_{component_id}(card, "en"));
                    }}
                }});

                data_{component_id}.ko.forEach(card => {{
                    if (!done_{component_id}.has(card.id)) {{
                        koBox_{component_id}.appendChild(makeCard_{component_id}(card, "ko"));
                    }}
                }});

                updateScore_{component_id}();
            }}

            function updateScore_{component_id}() {{
                const count = done_{component_id}.size;
                const total = data_{component_id}.total;
                score_{component_id}.textContent = "맞춘 개수: " + count + " / " + total;
                bar_{component_id}.style.width = ((count / total) * 100) + "%";

                if (count === total) {{
                    status_{component_id}.textContent = "모든 문장을 맞췄습니다! 훌륭합니다. 🎉";
                    if (!root_{component_id}.querySelector(".done-message")) {{
                        const msg = document.createElement("div");
                        msg.className = "done-message";
                        msg.textContent = "🎉 모든 문장을 맞췄습니다!";
                        root_{component_id}.appendChild(msg);
                    }}
                }}
            }}

            function clearSelection_{component_id}() {{
                root_{component_id}.querySelectorAll(".match-card.selected").forEach(el => el.classList.remove("selected"));
                selected_{component_id} = null;
            }}

            function handleClick_{component_id}(el, card, kind) {{
                if (locked_{component_id}) return;
                if (done_{component_id}.has(card.id)) return;

                if (!selected_{component_id}) {{
                    selected_{component_id} = {{ el, card, kind }};
                    el.classList.add("selected");
                    status_{component_id}.textContent = kind === "en"
                        ? "오른쪽에서 알맞은 한국어 뜻을 고르세요."
                        : "왼쪽에서 알맞은 영어 표현을 고르세요.";
                    return;
                }}

                if (selected_{component_id}.el === el) {{
                    clearSelection_{component_id}();
                    status_{component_id}.textContent = "선택을 취소했습니다. 다시 하나를 고르세요.";
                    return;
                }}

                if (selected_{component_id}.card.id === card.id && selected_{component_id}.kind !== kind) {{
                    locked_{component_id} = true;
                    selected_{component_id}.el.classList.remove("selected");
                    el.classList.remove("selected");

                    selected_{component_id}.el.classList.add("correct");
                    el.classList.add("correct");
                    status_{component_id}.textContent = "정답입니다! 두 박스가 함께 사라집니다. ✅";

                    const matchedId = card.id;

                    setTimeout(() => {{
                        done_{component_id}.add(matchedId);
                        selected_{component_id} = null;
                        locked_{component_id} = false;
                        render_{component_id}();

                        if (done_{component_id}.size < data_{component_id}.total) {{
                            status_{component_id}.textContent = "좋아요. 다음 문장을 맞춰 보세요.";
                        }}
                    }}, 680);
                }} else {{
                    locked_{component_id} = true;
                    selected_{component_id}.el.classList.add("wrong");
                    el.classList.add("wrong");
                    status_{component_id}.textContent = "아쉬워요. 다시 짝을 맞춰 보세요. ❌";

                    setTimeout(() => {{
                        selected_{component_id}.el.classList.remove("selected", "wrong");
                        el.classList.remove("wrong");
                        selected_{component_id} = null;
                        locked_{component_id} = false;
                    }}, 360);
                }}
            }}

            reset_{component_id}.addEventListener("click", () => {{
                selected_{component_id} = null;
                done_{component_id} = new Set();
                locked_{component_id} = false;

                const doneMsg = root_{component_id}.querySelector(".done-message");
                if (doneMsg) doneMsg.remove();

                status_{component_id}.textContent = "먼저 영어 또는 한국어 박스를 하나 선택하세요.";
                render_{component_id}();
            }});

            render_{component_id}();
        </script>
        """,
        height=760,
        scrolling=True
    )
    
elif selected_tab == "✍️ 생각 적기":
    st.subheader("✍️ 생각 적기: Reflective Writing")
    st.markdown('<div class="game-card"><div class="big-guide">질문을 하나 고르고, 노래를 들으며 떠오른 생각을 자유롭게 적어 보세요.<br>학생이 쓴 내용을 바탕으로 한국어 글을 조금 더 풍부하게 다듬고, 그 글을 자연스러운 영어로 번역해 줍니다.<br>맨 밑에는 글을 더 발전시키기 위한 쓰기 조언만 제시합니다.</div></div>', unsafe_allow_html=True)
    reflect_key = safe_key(song_choice)
    questions = data["reflect_questions"][:3]
    selected_question = st.radio("질문을 선택하세요.", questions, key=f"reflect_question_{reflect_key}", index=0)
    answer = st.text_area("내 생각을 적어 보세요.", placeholder="예: 이 노래를 들으며 예전에 좋아했던 사람이 떠올랐다. 그때는 내 마음을 잘 표현하지 못했고, 지금 생각하면 조금 아쉽다...", height=180, key=f"reflect_answer_{reflect_key}")
    if st.button("피드백 받기", key=f"reflect_submit_{reflect_key}", use_container_width=True):
        if not answer.strip():
            st.warning("먼저 자신의 생각을 한두 문장이라도 적어 보세요.")
        else:
            ko_feedback, en_feedback, advice = make_polished_feedback(song_choice, selected_question, answer)
            st.markdown("### 🇰🇷 다듬은 한국어 글")
            st.markdown(f'<div class="feedback-ko">{clean_text_for_display(ko_feedback)}</div>', unsafe_allow_html=True)
            st.markdown("### 🇺🇸 English Translation")
            st.markdown(f'<div class="feedback-en">{clean_text_for_display(en_feedback)}</div>', unsafe_allow_html=True)
            st.markdown("### ✨ 쓰기 조언")
            st.markdown(f'<div class="advice-box">{clean_text_for_display(advice)}</div>', unsafe_allow_html=True)


