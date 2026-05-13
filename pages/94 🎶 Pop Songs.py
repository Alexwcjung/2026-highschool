import streamlit as st
import random
import string

# =========================
# 1. 스타일 최적화 (단순화 및 모바일 대응)
# =========================
st.set_page_config(page_title="Music English", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    /* 모바일에서 여백 줄이기 */
    .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
    
    .info-box {
        background-color: #f8fafc; padding: 15px; border-radius: 10px;
        border: 1px solid #e2e8f0; line-height: 1.6; font-size: 0.95rem; margin-bottom: 15px;
    }
    .info-box h3 { font-size: 1.2rem; color: #1e3a8a; margin-bottom: 8px; border-bottom: 2px solid #6366f1; }
    
    .lyrics-container {
        padding: 10px; border-left: 4px solid #6366f1;
        margin-bottom: 8px; background-color: #f1f5f9; border-radius: 0 8px 8px 0;
    }
    .eng-line { font-size: 1rem; font-weight: 700; color: #1e3a8a; }
    .kor-sub { font-size: 0.85rem; color: #64748b; }
    
    /* 라디오 버튼(탭) 디자인 간소화 */
    div[data-testid="stMarkdownContainer"] > p { font-size: 1rem !important; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# 세션 관리
# -------------------------
if 'selected_song' not in st.session_state: st.session_state.selected_song = "1. Let It Go - Frozen OST"
if 'submitted_step2' not in st.session_state: st.session_state.submitted_step2 = False
if 'q3_cards' not in st.session_state: st.session_state.q3_cards = []
if 'current_tab' not in st.session_state: st.session_state.current_tab = "🎬 배경 학습"

def reset_data():
    st.session_state.submitted_step2 = False
    st.session_state.q3_cards = []
    st.session_state.show_q3_result = False
    st.session_state.current_tab = "🎬 배경 학습"
    if 'scrambled' in st.session_state: del st.session_state.scrambled

# -------------------------
# 곡 선택 (번호 유지)
# -------------------------
song_options = [
    "1. Let It Go - Frozen OST", 
    "2. Hello - Adele", 
    "3. A Whole New World - Aladdin OST",
    "4. Stand By Me - Ben E. King",
    "5. Don't Know Why - Norah Jones"
]
song_choice = st.selectbox("곡을 선택하세요", song_options)

if st.session_state.selected_song != song_choice:
    st.session_state.selected_song = song_choice
    reset_data()
    st.rerun()

# 탭 제어
tabs_list = ["🎬 배경 학습", "📖 가사 & 퀴즈", "🧩 순서 배열"]
selected_tab = st.radio("", tabs_list, index=tabs_list.index(st.session_state.current_tab), horizontal=True, label_visibility="collapsed")
st.session_state.current_tab = selected_tab

# -------------------------
# 곡별 데이터
# -------------------------
if "1. Let It Go" in song_choice:
    video_url = "https://www.youtube.com/watch?v=L0MK7qz13bU"
    bg_content = "<h3>❄️ Let It Go</h3><p>엘사가 타인의 시선을 벗어나 <b>심리적 해방감</b>을 느끼는 과정을 담고 있습니다. '착한 소녀'라는 억압을 깨고 자아를 찾는 노래입니다.</p>"
    lyrics_raw = [
        ("The snow glows white on the mountain tonight", "오늘 밤 산엔 눈이 하얗게 빛나네요"),
        ("A kingdom of isolation, and it looks like I'm the queen", "고립된 이 왕국에서 내가 여왕인 것 같아요"),
        ("The wind is howling like this swirling storm inside", "내 안의 폭풍처럼 바람이 울부짖고 있어요"),
        ("Couldn't keep it in, heaven knows I tried", "더는 숨길 수 없었죠, 하늘은 내 노력을 알 거예요"),
        ("Don't let them in, don't let them see", "그들을 들여보내지 마요, 보여주지 마요"),
        ("Conceal, don't feel, don't let them know", "숨기고, 느끼지 마요, 모르게 하세요")
    ]
    questions = [("1. 엘사의 현재 기분은?", ["해방감", "공포"], "해방감"), ("2. 'Conceal'의 뜻은?", ["숨기다", "드러내다"], "숨기다")]

elif "2. Hello" in song_choice:
    video_url = "https://www.youtube.com/watch?v=YQHsXMglC9A"
    bg_content = "<h3>☎️ Hello</h3><p>과거의 연인에게 건네는 뒤늦은 사과입니다. 돌아갈 수 없는 <b>과거와 현재 사이의 단절</b>을 노래합니다.</p>"
    lyrics_raw = [
        ("Hello, it's me", "안녕, 나야"),
        ("I was wondering if after all these years you'd like to meet", "시간이 흐른 뒤에 네가 만나고 싶어 할지 궁금했어"),
        ("Hello from the other side", "반대편에서 인사해"),
        ("I must've called a thousand times", "수천 번은 전화했을 거야")
    ]
    questions = [("1. 노래의 목적은?", ["사과", "부탁"], "사과")]

elif "5. Don't Know Why" in song_choice:
    video_url = "https://www.youtube.com/watch?v=tO4dxvguQDk"
    bg_content = "<h3>🍂 Don't Know Why</h3><p>망설임 때문에 놓쳐버린 인연에 대한 <b>쓸쓸한 후회</b>를 담고 있습니다. 왜 그때 다가지 못했는지 자책하는 독백입니다.</p>"
    lyrics_raw = [
        ("I waited 'til I saw the sun", "해가 뜰 때까지 기다렸어요"),
        ("I don't know why I didn't come", "왜 가지 않았는지 모르겠어요"),
        ("I left you by the house of fun", "당신을 그곳에 남겨둔 채로요"),
        ("When I saw the break of day, I wished that I could fly away", "새벽이 올 때 멀리 날아가고 싶었죠"),
        ("My heart is drenched in wine", "내 마음은 슬픔(술)에 젖어버렸어요"),
        ("I feel as empty as a drum", "텅 빈 드럼처럼 공허해요")
    ]
    questions = [
        ("1. 주요 분위기는?", ["후회", "환희"], "후회"),
        ("2. 'Drenched in wine'은?", ["슬픈 마음", "취한 상태"], "슬픈 마음"),
        ("3. 'Bag of bones'는?", ["야윈 상태", "튼튼함"], "야윈 상태"),
        ("4. 가지 않은 이유는?", ["망설임", "거절"], "망설임"),
        ("5. 'Empty as a drum'은?", ["공허함", "소음"], "공허함"),
        ("6. 반복의 효과는?", ["자책 강조", "단어 공부"], "자책 강조")
    ]
else:
    video_url = "https://www.youtube.com/watch?v=Us-TVg40ExM"
    bg_content = "<h3>🌟 명곡 학습</h3><p>준비 중입니다.</p>"
    lyrics_raw = [("Lyric Eng", "가사 한글")]
    questions = [("Q1", ["A", "B"], "A")]

# -------------------------
# 가사/순서 가공 (a, b, c...)
# -------------------------
alphabet = list(string.ascii_lowercase)
full_lyrics = []
for i, (eng, kor) in enumerate(lyrics_raw):
    label = alphabet[i] if i < len(alphabet) else str(i)
    full_lyrics.append((f"({label}) {eng}", kor))

correct_order = [line[0] for line in full_lyrics]
if 'scrambled' not in st.session_state or st.session_state.get('last_song') != song_choice:
    st.session_state.scrambled = random.sample(correct_order, len(correct_order))
    st.session_state.last_song = song_choice

# -------------------------
# 탭별 출력
# -------------------------
if selected_tab == "🎬 배경 학습":
    st.markdown(f'<div class="info-box">{bg_content}</div>', unsafe_allow_html=True)
    st.video(video_url)

elif selected_tab == "📖 가사 & 퀴즈":
    st.video(video_url)
    st.markdown("---")
    st.markdown("### 🎼 Lyrics")
    for eng, kor in full_lyrics:
        st.markdown(f'<div class="lyrics-container"><div class="eng-line">{eng}</div><div class="kor-sub">{kor}</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💡 Quiz")
    with st.form(f"q_{song_choice}"):
        for i, (q, opts, ans) in enumerate(questions):
            q_text = q
            if st.session_state.submitted_step2:
                user_val = st.session_state.get(f"qs_{i}")
                q_text += " ✅" if user_val == ans else f" 🔍 ({ans})"
            st.radio(q_text, opts, index=None, key=f"qs_{i}")
        if st.form_submit_button("채점"):
            st.session_state.submitted_step2 = True
            st.rerun()

elif selected_tab == "🧩 순서 배열":
    st.info("가사 순서(a, b, c...)대로 클릭!")
    for i, text in enumerate(st.session_state.scrambled):
        is_sel = text in st.session_state.q3_cards
        if st.button(text, key=f"b3_{i}", use_container_width=True, disabled=is_sel):
            st.session_state.q3_cards.append(text)
            st.rerun()
    st.divider()
    for idx, card in enumerate(st.session_state.q3_cards):
        c1, c2 = st.columns([0.85, 0.15])
        c1.write(f"{idx+1}: {card}")
        if c2.button("X", key=f"d3_{idx}"):
            st.session_state.q3_cards.pop(idx)
            st.rerun()
    
    if len(st.session_state.q3_cards) == len(correct_order):
        if st.button("결과 확인", type="primary", use_container_width=True):
            st.session_state.show_q3_result = True
            st.rerun()
            
    if st.session_state.get('show_q3_result'):
        all_correct = True
        for i, user_s in enumerate(st.session_state.q3_cards):
            if user_s == correct_order[i]: st.success(f"{i+1}: OK")
            else:
                st.error(f"{i+1}: NO (정답: {correct_order[i]})")
                all_correct = False
        if all_correct: st.balloons()
