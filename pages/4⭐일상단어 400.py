import streamlit as st
import streamlit.components.v1 as components
import json
import html
import random
import re
import uuid

st.set_page_config(page_title="Daily English 400", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.stApp { background:#ffffff; color:#111827; }
.main-title { font-size:44px; font-weight:1000; color:#111827; margin-bottom:4px; }
.sub-title { font-size:17px; color:#6b7280; margin-bottom:24px; }
.hero-box {
    background: linear-gradient(135deg,#dcfce7 0%,#e0f2fe 55%,#fef3c7 100%);
    border:1px solid #bbf7d0; border-radius:28px; padding:26px 30px; margin-bottom:24px;
    box-shadow:0 8px 24px rgba(34,197,94,0.10);
}
.hero-title { font-size:28px; font-weight:1000; color:#0f172a; margin-bottom:8px; }
.hero-text { font-size:15px; color:#374151; line-height:1.8; font-weight:700; }
.theme-header {
    background:linear-gradient(135deg,#22c55e,#0ea5e9,#8b5cf6);
    color:white; padding:30px 34px; border-radius:30px; margin-bottom:22px;
    box-shadow:0 8px 20px rgba(34,197,94,0.24);
}
.theme-title { font-size:38px; font-weight:1000; margin-bottom:6px; line-height:1.2; }
.theme-desc { font-size:18px; font-weight:850; opacity:.95; }
.word-card {
    background:white; border-radius:18px; padding:10px 14px; margin-bottom:8px;
    border:1px solid #dcfce7; box-shadow:0 3px 10px rgba(0,0,0,0.04);
}
.word-row { display:flex; align-items:center; gap:10px; }
.word-number { min-width:38px; font-size:13px; font-weight:1000; color:#166534; background:#dcfce7; border-radius:999px; padding:5px 9px; text-align:center; }
.word-text { min-width:170px; font-size:25px; font-weight:1000; color:#111827; }
.meaning-text { font-size:19px; font-weight:850; color:#374151; margin-left:8px; }
.emoji-text { font-size:25px; line-height:1; text-align:center; padding-top:2px; }
.dialogue-box { background:#fefce8; border:1px solid #fde68a; border-radius:24px; padding:20px 22px; margin-bottom:24px; }
.dialogue-title { font-size:18px; font-weight:1000; color:#854d0e; margin-bottom:14px; }
.dialogue-line { font-size:19px; font-weight:1000; color:#111827; margin-top:10px; }
.dialogue-meaning { font-size:15px; color:#6b7280; margin-bottom:5px; font-weight:700; }
.quiz-card { background:#ffffff; border-radius:24px; padding:22px 24px; margin-bottom:18px; border:1px solid #dbeafe; box-shadow:0 5px 18px rgba(0,0,0,0.06); }
.quiz-number { display:inline-block; background:#dbeafe; color:#1d4ed8; padding:6px 12px; border-radius:999px; font-weight:1000; font-size:13px; margin-bottom:10px; }
.quiz-word { font-size:34px; font-weight:1000; color:#111827; margin-bottom:8px; }
.score-box { background:linear-gradient(135deg,#dcfce7,#dbeafe,#fce7f3); border-radius:24px; padding:24px 26px; margin:20px 0; border:1px solid #bbf7d0; }
.score-title { font-size:27px; font-weight:1000; color:#14532d; }
.wrong-box { background:#fff7ed; border-left:6px solid #fb923c; border-radius:18px; padding:16px 18px; margin:18px 0; color:#7c2d12; font-weight:800; }
.stButton > button {
    border-radius:999px; font-weight:1000; border:1px solid #bbf7d0; padding:1.0rem 1.2rem;
    min-height:58px; font-size:20px; box-shadow:0 6px 16px rgba(34,197,94,0.12);
}
.stButton > button:hover { border-color:#22c55e; color:#22c55e; }
div[data-testid="stTabs"] button[role="tab"] { min-height:58px !important; padding:10px 16px !important; border-radius:18px 18px 0 0 !important; }
div[data-testid="stTabs"] button[role="tab"] p { font-size:21px !important; font-weight:1000 !important; line-height:1.3 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { background:linear-gradient(135deg,#dcfce7,#dbeafe,#fef3c7) !important; border-radius:18px 18px 0 0 !important; }
@media (max-width:520px) {
    .main-title { font-size:34px; }
    .theme-title { font-size:30px !important; }
    .word-text { font-size:23px; min-width:125px; }
    .meaning-text { font-size:17px; }
    div[data-testid="stTabs"] button[role="tab"] p { font-size:17px !important; }
}
</style>
""", unsafe_allow_html=True)


def clean_text(text):
    return html.escape(str(text))


def safe_key(text):
    return re.sub(r"[^a-zA-Z0-9가-힣_]+", "_", str(text))


def browser_tts_button(text, label="🔊 듣기", height=70):
    text = str(text).strip()
    if not text:
        return
    safe_text = json.dumps(text, ensure_ascii=False)
    safe_label = clean_text(label)
    btn_id = "tts_" + uuid.uuid4().hex
    components.html(f"""
    <div style="width:100%; margin:4px 0 8px 0;">
      <button id="{btn_id}"
        style="width:100%; min-height:48px; border-radius:999px; border:1px solid #bbf7d0; background:white;
               font-size:22px; font-weight:900; cursor:pointer; box-shadow:0 4px 12px rgba(34,197,94,0.12);"
        onclick='window.speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance({safe_text}); u.lang="en-US"; u.rate=0.82; u.pitch=1.0; u.volume=1.0; window.speechSynthesis.speak(u);'>
        {safe_label}
      </button>
    </div>
    """, height=height)


def js_cassette_visual_player(items, title="🎧 단어 듣기", height=520):
    player_id = "cassette_" + uuid.uuid4().hex
    safe_items = json.dumps(items, ensure_ascii=False)
    safe_title = clean_text(title)
    components.html(f"""
    <div id="wrap_{player_id}" style="background:linear-gradient(135deg,#f0fdf4 0%,#eff6ff 55%,#fff7ed 100%); border:1px solid #bbf7d0; border-radius:28px; padding:22px 18px; box-shadow:0 8px 22px rgba(34,197,94,0.12);">
      <div style="display:flex; justify-content:center; align-items:center; margin-bottom:14px; font-size:18px; font-weight:900; color:#14532d;">{safe_title}</div>
      <div style="background:white; border:1px solid #dcfce7; border-radius:24px; padding:26px 18px; text-align:center;">
        <div id="count_{player_id}" style="float:right; background:white; border:1px solid #dcfce7; border-radius:999px; padding:8px 16px; font-size:16px; font-weight:900; color:#1e3a8a;">1 / 1</div>
        <div id="theme_{player_id}" style="display:inline-block; background:#dcfce7; color:#166534; padding:8px 18px; border-radius:999px; font-size:18px; font-weight:900; margin-bottom:16px;">theme</div>
        <div id="emoji_{player_id}" style="font-size:54px; margin:8px 0;">🌱</div>
        <div id="word_{player_id}" style="font-size:74px; font-weight:1000; line-height:1.08; color:#0f172a; letter-spacing:-2px;">word</div>
        <div id="meaning_{player_id}" style="font-size:38px; font-weight:900; color:#1f2937; margin-top:14px;">뜻</div>
        <div style="height:18px; background:#e2e8f0; border-radius:999px; margin:24px 0 0 0; overflow:hidden;">
          <div id="bar_{player_id}" style="height:100%; width:0%; background:linear-gradient(90deg,#22c55e,#0ea5e9); border-radius:999px;"></div>
        </div>
      </div>
      <button id="play_{player_id}" style="width:100%; min-height:48px; margin-top:14px; border-radius:14px; border:1px solid #86efac; background:#dcfce7; font-size:18px; font-weight:1000; cursor:pointer;">▶️ 재생</button>
      <div style="display:flex; gap:10px; margin-top:12px;">
        <button id="prev_{player_id}" style="flex:1; min-height:44px; border-radius:14px; border:1px solid #cbd5e1; background:white; font-size:17px; font-weight:900; cursor:pointer;">⏮ 이전</button>
        <button id="next_{player_id}" style="flex:1; min-height:44px; border-radius:14px; border:1px solid #cbd5e1; background:white; font-size:17px; font-weight:900; cursor:pointer;">다음 ⏭</button>
      </div>
      <div id="status_{player_id}" style="margin-top:12px; color:#0369a1; font-size:15px; font-weight:900;">준비 완료</div>
    </div>
    <script>
      const items_{player_id} = {safe_items};
      let currentIndex_{player_id} = 0;
      let isPlaying_{player_id} = false;
      const synth_{player_id} = window.speechSynthesis;
      const wordEl_{player_id} = document.getElementById("word_{player_id}");
      const meaningEl_{player_id} = document.getElementById("meaning_{player_id}");
      const emojiEl_{player_id} = document.getElementById("emoji_{player_id}");
      const themeEl_{player_id} = document.getElementById("theme_{player_id}");
      const countEl_{player_id} = document.getElementById("count_{player_id}");
      const barEl_{player_id} = document.getElementById("bar_{player_id}");
      const playBtn_{player_id} = document.getElementById("play_{player_id}");
      const prevBtn_{player_id} = document.getElementById("prev_{player_id}");
      const nextBtn_{player_id} = document.getElementById("next_{player_id}");
      const statusEl_{player_id} = document.getElementById("status_{player_id}");

      function loadCurrent_{player_id}() {{
        if (!items_{player_id}.length) return;
        const item = items_{player_id}[currentIndex_{player_id}];
        wordEl_{player_id}.textContent = item.word || "";
        meaningEl_{player_id}.textContent = item.meaning || "";
        emojiEl_{player_id}.textContent = item.emoji || "🌱";
        themeEl_{player_id}.textContent = item.theme || "단어";
        countEl_{player_id}.textContent = (currentIndex_{player_id}+1) + " / " + items_{player_id}.length;
        const pct = items_{player_id}.length <= 1 ? 100 : (currentIndex_{player_id} / (items_{player_id}.length-1)) * 100;
        barEl_{player_id}.style.width = pct + "%";
      }}

      function speakCurrent_{player_id}() {{
        if (!items_{player_id}.length) return;
        synth_{player_id}.cancel();
        const item = items_{player_id}[currentIndex_{player_id}];
        const u = new SpeechSynthesisUtterance(item.word || "");
        u.lang = "en-US"; u.rate = 0.78; u.pitch = 1.0; u.volume = 1.0;
        u.onstart = function() {{ statusEl_{player_id}.textContent = "🔊 재생 중: " + (currentIndex_{player_id}+1) + " / " + items_{player_id}.length; }};
        u.onend = function() {{
          if (!isPlaying_{player_id}) return;
          if (currentIndex_{player_id} < items_{player_id}.length - 1) {{
            currentIndex_{player_id} += 1;
            loadCurrent_{player_id}();
            setTimeout(speakCurrent_{player_id}, 650);
          }} else {{
            isPlaying_{player_id} = false;
            playBtn_{player_id}.textContent = "▶️ 처음부터 다시";
            statusEl_{player_id}.textContent = "✅ 카세트 재생 완료";
            barEl_{player_id}.style.width = "100%";
          }}
        }};
        synth_{player_id}.speak(u);
      }}

      playBtn_{player_id}.addEventListener("click", function() {{
        if (isPlaying_{player_id}) {{
          isPlaying_{player_id} = false;
          synth_{player_id}.cancel();
          playBtn_{player_id}.textContent = "▶️ 재생";
          statusEl_{player_id}.textContent = "⏸ 일시 정지";
        }} else {{
          if (currentIndex_{player_id} >= items_{player_id}.length - 1 && barEl_{player_id}.style.width === "100%") currentIndex_{player_id} = 0;
          isPlaying_{player_id} = true;
          playBtn_{player_id}.textContent = "⏸ 멈춤";
          loadCurrent_{player_id}();
          speakCurrent_{player_id}();
        }}
      }});
      prevBtn_{player_id}.addEventListener("click", function() {{
        isPlaying_{player_id} = false; synth_{player_id}.cancel(); playBtn_{player_id}.textContent = "▶️ 재생";
        currentIndex_{player_id} = Math.max(0, currentIndex_{player_id} - 1); loadCurrent_{player_id}();
      }});
      nextBtn_{player_id}.addEventListener("click", function() {{
        isPlaying_{player_id} = false; synth_{player_id}.cancel(); playBtn_{player_id}.textContent = "▶️ 재생";
        currentIndex_{player_id} = Math.min(items_{player_id}.length - 1, currentIndex_{player_id} + 1); loadCurrent_{player_id}();
      }});
      loadCurrent_{player_id}();
    </script>
    """, height=height, scrolling=False)


WORD_THEMES = {
    "🏫 학교생활": [
        {"word":"subject","meaning":"과목"},{"word":"math","meaning":"수학"},{"word":"science","meaning":"과학"},{"word":"history","meaning":"역사"},{"word":"music","meaning":"음악"},
        {"word":"art","meaning":"미술"},{"word":"P.E.","meaning":"체육"},{"word":"club","meaning":"동아리"},{"word":"schedule","meaning":"일정표"},{"word":"semester","meaning":"학기"},
        {"word":"assignment","meaning":"과제"},{"word":"project","meaning":"프로젝트"},{"word":"presentation","meaning":"발표"},{"word":"report","meaning":"보고서"},{"word":"textbook","meaning":"교과서"},
        {"word":"workbook","meaning":"문제집"},{"word":"library","meaning":"도서관"},{"word":"cafeteria","meaning":"급식소, 식당"},{"word":"hallway","meaning":"복도"},{"word":"attendance","meaning":"출석"}],
    "✏️ 교실 활동": [
        {"word":"copy","meaning":"베껴 쓰다"},{"word":"repeat","meaning":"반복하다"},{"word":"underline","meaning":"밑줄 치다"},{"word":"circle","meaning":"동그라미 치다"},{"word":"choose","meaning":"고르다"},
        {"word":"check","meaning":"확인하다"},{"word":"match","meaning":"연결하다, 맞추다"},{"word":"complete","meaning":"완성하다"},{"word":"fill","meaning":"채우다"},{"word":"spell","meaning":"철자를 말하다"},
        {"word":"pronounce","meaning":"발음하다"},{"word":"review","meaning":"복습하다"},{"word":"explain","meaning":"설명하다"},{"word":"describe","meaning":"묘사하다"},{"word":"compare","meaning":"비교하다"},
        {"word":"discuss","meaning":"토론하다"},{"word":"present","meaning":"발표하다"},{"word":"take notes","meaning":"필기하다"},{"word":"turn in","meaning":"제출하다"},{"word":"hand out","meaning":"나누어 주다"}],
    "🏠 집과 생활": [
        {"word":"living room","meaning":"거실"},{"word":"bedroom","meaning":"침실"},{"word":"kitchen","meaning":"부엌"},{"word":"balcony","meaning":"발코니"},{"word":"floor","meaning":"바닥, 층"},
        {"word":"wall","meaning":"벽"},{"word":"roof","meaning":"지붕"},{"word":"garden","meaning":"정원"},{"word":"yard","meaning":"마당"},{"word":"sofa","meaning":"소파"},
        {"word":"television","meaning":"텔레비전"},{"word":"refrigerator","meaning":"냉장고"},{"word":"microwave","meaning":"전자레인지"},{"word":"blanket","meaning":"담요"},{"word":"pillow","meaning":"베개"},
        {"word":"towel","meaning":"수건"},{"word":"soap","meaning":"비누"},{"word":"mirror","meaning":"거울"},{"word":"closet","meaning":"옷장"},{"word":"trash","meaning":"쓰레기"}],
    "🌅 하루 일과": [
        {"word":"routine","meaning":"일과"},{"word":"wake up","meaning":"잠에서 깨다"},{"word":"get up","meaning":"일어나다"},{"word":"brush","meaning":"닦다"},{"word":"shower","meaning":"샤워하다"},
        {"word":"dress","meaning":"옷을 입다"},{"word":"leave","meaning":"떠나다"},{"word":"arrive","meaning":"도착하다"},{"word":"return","meaning":"돌아오다"},{"word":"finish","meaning":"끝내다"},
        {"word":"relax","meaning":"쉬다"},{"word":"weekday","meaning":"평일"},{"word":"weekend","meaning":"주말"},{"word":"usually","meaning":"보통"},{"word":"often","meaning":"자주"},
        {"word":"sometimes","meaning":"가끔"},{"word":"always","meaning":"항상"},{"word":"never","meaning":"절대 ~하지 않다"},{"word":"habit","meaning":"습관"},{"word":"lifestyle","meaning":"생활 방식"}],
    "🎨 취미와 여가": [
        {"word":"hobby","meaning":"취미"},{"word":"movie","meaning":"영화"},{"word":"drama","meaning":"드라마"},{"word":"song","meaning":"노래"},{"word":"concert","meaning":"콘서트"},
        {"word":"dance","meaning":"춤"},{"word":"drawing","meaning":"그림 그리기"},{"word":"painting","meaning":"그림, 회화"},{"word":"comic","meaning":"만화"},{"word":"novel","meaning":"소설"},
        {"word":"photography","meaning":"사진 촬영"},{"word":"cooking","meaning":"요리"},{"word":"baking","meaning":"빵 굽기"},{"word":"camping","meaning":"캠핑"},{"word":"hiking","meaning":"하이킹"},
        {"word":"fishing","meaning":"낚시"},{"word":"free time","meaning":"자유 시간"},{"word":"favorite","meaning":"가장 좋아하는"},{"word":"popular","meaning":"인기 있는"},{"word":"relaxing","meaning":"편안한"}],
    "⚽ 운동과 활동": [
        {"word":"soccer","meaning":"축구"},{"word":"baseball","meaning":"야구"},{"word":"basketball","meaning":"농구"},{"word":"volleyball","meaning":"배구"},{"word":"tennis","meaning":"테니스"},
        {"word":"badminton","meaning":"배드민턴"},{"word":"swimming","meaning":"수영"},{"word":"cycling","meaning":"자전거 타기"},{"word":"skating","meaning":"스케이트 타기"},{"word":"boxing","meaning":"복싱"},
        {"word":"taekwondo","meaning":"태권도"},{"word":"yoga","meaning":"요가"},{"word":"fitness","meaning":"운동, 체력"},{"word":"field","meaning":"운동장"},{"word":"court","meaning":"코트"},
        {"word":"stadium","meaning":"경기장"},{"word":"coach","meaning":"코치"},{"word":"match","meaning":"경기"},{"word":"competition","meaning":"대회"},{"word":"medal","meaning":"메달"}],
    "☀️ 날씨와 계절": [
        {"word":"season","meaning":"계절"},{"word":"spring","meaning":"봄"},{"word":"summer","meaning":"여름"},{"word":"fall","meaning":"가을"},{"word":"winter","meaning":"겨울"},
        {"word":"cloudy","meaning":"흐린"},{"word":"rainy","meaning":"비 오는"},{"word":"snowy","meaning":"눈 오는"},{"word":"windy","meaning":"바람 부는"},{"word":"stormy","meaning":"폭풍우 치는"},
        {"word":"foggy","meaning":"안개 낀"},{"word":"dry","meaning":"건조한"},{"word":"wet","meaning":"젖은"},{"word":"humid","meaning":"습한"},{"word":"temperature","meaning":"온도"},
        {"word":"degree","meaning":"도"},{"word":"forecast","meaning":"일기예보"},{"word":"umbrella","meaning":"우산"},{"word":"raincoat","meaning":"비옷"},{"word":"rainbow","meaning":"무지개"}],
    "🌳 자연과 환경": [
        {"word":"nature","meaning":"자연"},{"word":"environment","meaning":"환경"},{"word":"plant","meaning":"식물"},{"word":"forest","meaning":"숲"},{"word":"lake","meaning":"호수"},
        {"word":"ocean","meaning":"바다"},{"word":"island","meaning":"섬"},{"word":"desert","meaning":"사막"},{"word":"farm","meaning":"농장"},{"word":"village","meaning":"마을"},
        {"word":"leaf","meaning":"잎"},{"word":"root","meaning":"뿌리"},{"word":"stone","meaning":"돌"},{"word":"sand","meaning":"모래"},{"word":"soil","meaning":"흙"},
        {"word":"plastic","meaning":"플라스틱"},{"word":"recycle","meaning":"재활용하다"},{"word":"save","meaning":"아끼다, 구하다"},{"word":"protect","meaning":"보호하다"},{"word":"pollution","meaning":"오염"}],
    "🍽️ 식당과 주문": [
        {"word":"restaurant","meaning":"식당"},{"word":"menu","meaning":"메뉴"},{"word":"seat","meaning":"자리"},{"word":"waiter","meaning":"남자 종업원"},{"word":"waitress","meaning":"여자 종업원"},
        {"word":"order","meaning":"주문하다"},{"word":"dish","meaning":"요리"},{"word":"meal","meaning":"식사"},{"word":"soup","meaning":"수프"},{"word":"salad","meaning":"샐러드"},
        {"word":"steak","meaning":"스테이크"},{"word":"pizza","meaning":"피자"},{"word":"pasta","meaning":"파스타"},{"word":"burger","meaning":"햄버거"},{"word":"sandwich","meaning":"샌드위치"},
        {"word":"dessert","meaning":"디저트"},{"word":"spicy","meaning":"매운"},{"word":"sweet","meaning":"달콤한"},{"word":"bill","meaning":"계산서"},{"word":"receipt","meaning":"영수증"}],
    "🛒 쇼핑과 가격": [
        {"word":"shop","meaning":"가게"},{"word":"market","meaning":"시장"},{"word":"mall","meaning":"쇼핑몰"},{"word":"supermarket","meaning":"슈퍼마켓"},{"word":"cashier","meaning":"계산원"},
        {"word":"customer","meaning":"손님"},{"word":"price","meaning":"가격"},{"word":"sale","meaning":"할인 판매"},{"word":"discount","meaning":"할인"},{"word":"coupon","meaning":"쿠폰"},
        {"word":"change","meaning":"거스름돈"},{"word":"coin","meaning":"동전"},{"word":"expensive","meaning":"비싼"},{"word":"cheap","meaning":"싼"},{"word":"size","meaning":"크기, 사이즈"},
        {"word":"color","meaning":"색깔"},{"word":"brand","meaning":"상표"},{"word":"exchange","meaning":"교환하다"},{"word":"refund","meaning":"환불"},{"word":"cash","meaning":"현금"}],
    "👕 옷과 외모": [
        {"word":"T-shirt","meaning":"티셔츠"},{"word":"pants","meaning":"바지"},{"word":"jeans","meaning":"청바지"},{"word":"shorts","meaning":"반바지"},{"word":"skirt","meaning":"치마"},
        {"word":"dress","meaning":"원피스, 옷을 입다"},{"word":"jacket","meaning":"재킷"},{"word":"coat","meaning":"코트"},{"word":"sweater","meaning":"스웨터"},{"word":"hoodie","meaning":"후드티"},
        {"word":"uniform","meaning":"교복, 제복"},{"word":"socks","meaning":"양말"},{"word":"sneakers","meaning":"운동화"},{"word":"boots","meaning":"부츠"},{"word":"sandals","meaning":"샌들"},
        {"word":"scarf","meaning":"목도리"},{"word":"gloves","meaning":"장갑"},{"word":"belt","meaning":"벨트"},{"word":"glasses","meaning":"안경"},{"word":"comfortable","meaning":"편안한"}],
    "🚌 교통과 길 찾기": [
        {"word":"bus stop","meaning":"버스 정류장"},{"word":"subway","meaning":"지하철"},{"word":"airport","meaning":"공항"},{"word":"terminal","meaning":"터미널"},{"word":"platform","meaning":"승강장"},
        {"word":"route","meaning":"경로"},{"word":"direction","meaning":"방향"},{"word":"straight","meaning":"곧장"},{"word":"corner","meaning":"모퉁이"},{"word":"block","meaning":"블록, 구역"},
        {"word":"traffic","meaning":"교통"},{"word":"crosswalk","meaning":"횡단보도"},{"word":"sidewalk","meaning":"인도"},{"word":"bridge","meaning":"다리"},{"word":"tunnel","meaning":"터널"},
        {"word":"entrance","meaning":"입구"},{"word":"exit","meaning":"출구"},{"word":"transfer","meaning":"갈아타다"},{"word":"lost","meaning":"길을 잃은"},{"word":"guide","meaning":"안내하다"}],
    "✈️ 여행과 숙박": [
        {"word":"travel","meaning":"여행하다"},{"word":"trip","meaning":"여행"},{"word":"vacation","meaning":"방학, 휴가"},{"word":"tourist","meaning":"관광객"},{"word":"passport","meaning":"여권"},
        {"word":"flight","meaning":"비행"},{"word":"hotel","meaning":"호텔"},{"word":"motel","meaning":"모텔"},{"word":"hostel","meaning":"호스텔"},{"word":"reservation","meaning":"예약"},
        {"word":"check in","meaning":"체크인하다"},{"word":"check out","meaning":"체크아웃하다"},{"word":"luggage","meaning":"짐"},{"word":"suitcase","meaning":"여행 가방"},{"word":"backpack","meaning":"배낭"},
        {"word":"souvenir","meaning":"기념품"},{"word":"museum","meaning":"박물관"},{"word":"famous","meaning":"유명한"},{"word":"local","meaning":"지역의"},{"word":"map","meaning":"지도"}],
    "👥 친구 관계": [
        {"word":"friendship","meaning":"우정"},{"word":"best friend","meaning":"가장 친한 친구"},{"word":"teammate","meaning":"팀 동료"},{"word":"partner","meaning":"짝, 동료"},{"word":"message","meaning":"메시지"},
        {"word":"call","meaning":"전화하다"},{"word":"chat","meaning":"채팅하다"},{"word":"invite","meaning":"초대하다"},{"word":"visit","meaning":"방문하다"},{"word":"meet","meaning":"만나다"},
        {"word":"hang out","meaning":"어울려 놀다"},{"word":"laugh","meaning":"웃다"},{"word":"share","meaning":"나누다"},{"word":"trust","meaning":"믿다"},{"word":"promise","meaning":"약속하다"},
        {"word":"secret","meaning":"비밀"},{"word":"joke","meaning":"농담"},{"word":"together","meaning":"함께"},{"word":"alone","meaning":"혼자"},{"word":"forgive","meaning":"용서하다"}],
    "😊 감정 표현": [
        {"word":"excited","meaning":"신난"},{"word":"nervous","meaning":"긴장한"},{"word":"bored","meaning":"지루한"},{"word":"surprised","meaning":"놀란"},{"word":"confused","meaning":"혼란스러운"},
        {"word":"embarrassed","meaning":"당황한"},{"word":"proud","meaning":"자랑스러운"},{"word":"disappointed","meaning":"실망한"},{"word":"lonely","meaning":"외로운"},{"word":"relaxed","meaning":"편안한"},
        {"word":"calm","meaning":"차분한"},{"word":"upset","meaning":"속상한"},{"word":"interested","meaning":"관심 있는"},{"word":"satisfied","meaning":"만족한"},{"word":"thankful","meaning":"감사하는"},
        {"word":"hopeful","meaning":"희망적인"},{"word":"mood","meaning":"기분"},{"word":"stress","meaning":"스트레스"},{"word":"confidence","meaning":"자신감"},{"word":"courage","meaning":"용기"}],
    "💭 생각과 의견": [
        {"word":"think","meaning":"생각하다"},{"word":"believe","meaning":"믿다"},{"word":"guess","meaning":"추측하다"},{"word":"remember","meaning":"기억하다"},{"word":"forget","meaning":"잊다"},
        {"word":"mean","meaning":"의미하다"},{"word":"agree","meaning":"동의하다"},{"word":"disagree","meaning":"동의하지 않다"},{"word":"opinion","meaning":"의견"},{"word":"idea","meaning":"생각"},
        {"word":"reason","meaning":"이유"},{"word":"example","meaning":"예시"},{"word":"fact","meaning":"사실"},{"word":"choice","meaning":"선택"},{"word":"decision","meaning":"결정"},
        {"word":"advice","meaning":"조언"},{"word":"suggestion","meaning":"제안"},{"word":"possible","meaning":"가능한"},{"word":"impossible","meaning":"불가능한"},{"word":"confusing","meaning":"헷갈리는"}],
    "📅 계획과 약속": [
        {"word":"plan","meaning":"계획"},{"word":"appointment","meaning":"약속, 예약"},{"word":"meeting","meaning":"회의"},{"word":"date","meaning":"날짜, 데이트"},{"word":"event","meaning":"행사"},
        {"word":"party","meaning":"파티"},{"word":"festival","meaning":"축제"},{"word":"deadline","meaning":"마감일"},{"word":"calendar","meaning":"달력"},{"word":"next week","meaning":"다음 주"},
        {"word":"this weekend","meaning":"이번 주말"},{"word":"tomorrow","meaning":"내일"},{"word":"tonight","meaning":"오늘 밤"},{"word":"join","meaning":"참여하다"},{"word":"prepare","meaning":"준비하다"},
        {"word":"decide","meaning":"결정하다"},{"word":"cancel","meaning":"취소하다"},{"word":"on time","meaning":"제시간에"},{"word":"available","meaning":"시간이 되는"},{"word":"reminder","meaning":"알림"}],
    "🩺 건강한 생활": [
        {"word":"health","meaning":"건강"},{"word":"body","meaning":"몸"},{"word":"eye","meaning":"눈"},{"word":"ear","meaning":"귀"},{"word":"nose","meaning":"코"},
        {"word":"mouth","meaning":"입"},{"word":"tooth","meaning":"이"},{"word":"hand","meaning":"손"},{"word":"arm","meaning":"팔"},{"word":"leg","meaning":"다리"},
        {"word":"foot","meaning":"발"},{"word":"stomach","meaning":"배, 위"},{"word":"back","meaning":"등, 뒤"},{"word":"heart","meaning":"심장, 마음"},{"word":"clinic","meaning":"병원, 진료소"},
        {"word":"medicine","meaning":"약"},{"word":"vitamin","meaning":"비타민"},{"word":"diet","meaning":"식단"},{"word":"cough","meaning":"기침"},{"word":"flu","meaning":"독감"}],
    "📱 미디어와 스마트폰": [
        {"word":"smartphone","meaning":"스마트폰"},{"word":"screen","meaning":"화면"},{"word":"app","meaning":"앱"},{"word":"website","meaning":"웹사이트"},{"word":"internet","meaning":"인터넷"},
        {"word":"Wi-Fi","meaning":"와이파이"},{"word":"password","meaning":"비밀번호"},{"word":"text","meaning":"문자를 보내다"},{"word":"video call","meaning":"영상 통화"},{"word":"gallery","meaning":"사진첩"},
        {"word":"news","meaning":"뉴스"},{"word":"channel","meaning":"채널"},{"word":"post","meaning":"게시물"},{"word":"comment","meaning":"댓글"},{"word":"upload","meaning":"업로드하다"},
        {"word":"download","meaning":"다운로드하다"},{"word":"search","meaning":"검색하다"},{"word":"click","meaning":"클릭하다"},{"word":"battery","meaning":"배터리"},{"word":"notification","meaning":"알림"}],
    "💼 직업과 미래": [
        {"word":"job","meaning":"직업"},{"word":"work","meaning":"일하다"},{"word":"company","meaning":"회사"},{"word":"office","meaning":"사무실"},{"word":"factory","meaning":"공장"},
        {"word":"engineer","meaning":"기술자, 엔지니어"},{"word":"mechanic","meaning":"정비사"},{"word":"chef","meaning":"요리사"},{"word":"firefighter","meaning":"소방관"},{"word":"farmer","meaning":"농부"},
        {"word":"designer","meaning":"디자이너"},{"word":"singer","meaning":"가수"},{"word":"actor","meaning":"배우"},{"word":"athlete","meaning":"운동선수"},{"word":"dream","meaning":"꿈"},
        {"word":"future","meaning":"미래"},{"word":"goal","meaning":"목표"},{"word":"skill","meaning":"기술"},{"word":"interview","meaning":"면접"},{"word":"experience","meaning":"경험"}],
    "🛠️ 기술과 자동차": [
        {"word":"car","meaning":"자동차"},{"word":"engine","meaning":"엔진"},{"word":"wheel","meaning":"바퀴"},{"word":"tire","meaning":"타이어"},{"word":"brake","meaning":"브레이크"},
        {"word":"repair","meaning":"수리하다"},{"word":"tool","meaning":"도구"},{"word":"machine","meaning":"기계"},{"word":"oil","meaning":"기름"},{"word":"battery","meaning":"배터리"},
        {"word":"electric","meaning":"전기의"},{"word":"driver","meaning":"운전자"},{"word":"license","meaning":"면허"},{"word":"safety","meaning":"안전"},{"word":"helmet","meaning":"헬멧"},
        {"word":"manual","meaning":"설명서"},{"word":"button","meaning":"버튼"},{"word":"signal","meaning":"신호"},{"word":"speed","meaning":"속도"},{"word":"test drive","meaning":"시운전"}],
    "🌍 세계와 문화": [
        {"word":"country","meaning":"나라"},{"word":"city","meaning":"도시"},{"word":"capital","meaning":"수도"},{"word":"language","meaning":"언어"},{"word":"culture","meaning":"문화"},
        {"word":"flag","meaning":"국기"},{"word":"people","meaning":"사람들"},{"word":"food","meaning":"음식"},{"word":"music","meaning":"음악"},{"word":"holiday","meaning":"휴일"},
        {"word":"festival","meaning":"축제"},{"word":"traditional","meaning":"전통적인"},{"word":"modern","meaning":"현대적인"},{"word":"history","meaning":"역사"},{"word":"world","meaning":"세계"},
        {"word":"map","meaning":"지도"},{"word":"continent","meaning":"대륙"},{"word":"Asia","meaning":"아시아"},{"word":"America","meaning":"미국, 아메리카"},{"word":"Europe","meaning":"유럽"}],
    "🆘 도움 요청": [
        {"word":"help","meaning":"도움"},{"word":"please","meaning":"제발, 부탁합니다"},{"word":"sorry","meaning":"미안한"},{"word":"problem","meaning":"문제"},{"word":"question","meaning":"질문"},
        {"word":"answer","meaning":"대답"},{"word":"again","meaning":"다시"},{"word":"slowly","meaning":"천천히"},{"word":"loudly","meaning":"크게"},{"word":"understand","meaning":"이해하다"},
        {"word":"repeat","meaning":"반복하다"},{"word":"explain","meaning":"설명하다"},{"word":"show","meaning":"보여 주다"},{"word":"tell","meaning":"말하다"},{"word":"need","meaning":"필요하다"},
        {"word":"borrow","meaning":"빌리다"},{"word":"lend","meaning":"빌려주다"},{"word":"find","meaning":"찾다"},{"word":"wait","meaning":"기다리다"},{"word":"emergency","meaning":"비상 상황"}]
}

EMOJI_MAP = {
    "subject":"📚","math":"➗","science":"🔬","history":"🏛️","music":"🎵","art":"🎨","P.E.":"🏃","club":"👥","schedule":"🗓️","semester":"🏫",
    "assignment":"📝","project":"📁","presentation":"🗣️","report":"📄","textbook":"📘","workbook":"📗","library":"📚","cafeteria":"🍽️","hallway":"🚶","attendance":"✅",
    "copy":"✍️","repeat":"🔁","underline":"〽️","circle":"⭕","choose":"☝️","check":"✅","match":"🏆","complete":"🏁","fill":"🖊️","spell":"🔤",
    "pronounce":"🗣️","review":"🔎","explain":"💬","describe":"🖼️","compare":"⚖️","discuss":"🗨️","present":"📢","take notes":"📝","turn in":"📥","hand out":"📤",
    "living room":"🛋️","bedroom":"🛏️","kitchen":"🍳","balcony":"🌇","floor":"🧱","wall":"🧱","roof":"🏠","garden":"🌷","yard":"🌳","sofa":"🛋️",
    "television":"📺","refrigerator":"🧊","microwave":"♨️","blanket":"🛌","pillow":"🛏️","towel":"🧺","soap":"🧼","mirror":"🪞","closet":"🚪","trash":"🗑️",
    "routine":"🔄","wake up":"⏰","get up":"🌅","brush":"🪥","shower":"🚿","dress":"👕","leave":"🚪","arrive":"📍","return":"↩️","finish":"🏁",
    "relax":"😌","weekday":"📅","weekend":"🎉","usually":"🔁","often":"🔂","sometimes":"🤔","always":"♾️","never":"🚫","habit":"🔁","lifestyle":"🌿",
    "hobby":"🎯","movie":"🎬","drama":"📺","song":"🎵","concert":"🎤","dance":"💃","drawing":"✏️","painting":"🖌️","comic":"💬","novel":"📖",
    "photography":"📷","cooking":"🍳","baking":"🍞","camping":"⛺","hiking":"🥾","fishing":"🎣","free time":"🕒","favorite":"⭐","popular":"🔥","relaxing":"😌",
    "soccer":"⚽","baseball":"⚾","basketball":"🏀","volleyball":"🏐","tennis":"🎾","badminton":"🏸","swimming":"🏊","cycling":"🚴","skating":"⛸️","boxing":"🥊",
    "taekwondo":"🥋","yoga":"🧘","fitness":"💪","field":"🏟️","court":"🎾","stadium":"🏟️","coach":"📣","competition":"🏁","medal":"🏅",
    "season":"🍂","spring":"🌸","summer":"☀️","fall":"🍁","winter":"❄️","cloudy":"☁️","rainy":"🌧️","snowy":"🌨️","windy":"🌬️","stormy":"⛈️",
    "foggy":"🌫️","dry":"🏜️","wet":"💦","humid":"💧","temperature":"🌡️","degree":"🌡️","forecast":"📡","umbrella":"☂️","raincoat":"🧥","rainbow":"🌈",
    "nature":"🌿","environment":"🌎","plant":"🌱","forest":"🌲","lake":"🏞️","ocean":"🌊","island":"🏝️","desert":"🏜️","farm":"🚜","village":"🏘️",
    "leaf":"🍃","root":"🌱","stone":"🪨","sand":"🏖️","soil":"🌱","plastic":"🥤","recycle":"♻️","save":"💾","protect":"🛡️","pollution":"🏭",
    "restaurant":"🍽️","menu":"📋","seat":"💺","waiter":"🤵","waitress":"🤵‍♀️","order":"🛎️","dish":"🍛","meal":"🍽️","soup":"🍲","salad":"🥗",
    "steak":"🥩","pizza":"🍕","pasta":"🍝","burger":"🍔","sandwich":"🥪","dessert":"🍰","spicy":"🌶️","sweet":"🍬","bill":"🧾","receipt":"🧾",
    "shop":"🏪","market":"🛒","mall":"🏬","supermarket":"🛒","cashier":"💁","customer":"🧑","price":"💰","sale":"🏷️","discount":"🔻","coupon":"🎟️",
    "change":"💵","coin":"🪙","expensive":"💸","cheap":"👍","size":"📏","color":"🎨","brand":"🏷️","exchange":"🔄","refund":"↩️","cash":"💵",
    "T-shirt":"👕","pants":"👖","jeans":"👖","shorts":"🩳","skirt":"👗","jacket":"🧥","coat":"🧥","sweater":"🧶","hoodie":"🧥","uniform":"🎽",
    "socks":"🧦","sneakers":"👟","boots":"🥾","sandals":"🩴","scarf":"🧣","gloves":"🧤","belt":"👖","glasses":"👓","comfortable":"😌",
    "bus stop":"🚏","subway":"🚇","airport":"✈️","terminal":"🚌","platform":"🚉","route":"🗺️","direction":"➡️","straight":"⬆️","corner":"↪️","block":"🏙️",
    "traffic":"🚦","crosswalk":"🚸","sidewalk":"🚶","bridge":"🌉","tunnel":"🚇","entrance":"🚪","exit":"🚪","transfer":"🔁","lost":"😵","guide":"🧭",
    "travel":"✈️","trip":"🧳","vacation":"🏖️","tourist":"📸","passport":"🛂","flight":"🛫","hotel":"🏨","motel":"🏩","hostel":"🛏️","reservation":"📅",
    "check in":"🔑","check out":"👋","luggage":"🧳","suitcase":"🧳","backpack":"🎒","souvenir":"🎁","museum":"🏛️","famous":"⭐","local":"📍","map":"🗺️",
    "friendship":"🤝","best friend":"👯","teammate":"👥","partner":"🤝","message":"💬","call":"📞","chat":"💬","invite":"✉️","visit":"🏠","meet":"🤝",
    "hang out":"🎉","laugh":"😂","share":"🤲","trust":"🤝","promise":"🤞","secret":"🤫","joke":"😄","together":"👥","alone":"🚶","forgive":"🫶",
    "excited":"🤩","nervous":"😬","bored":"🥱","surprised":"😲","confused":"😕","embarrassed":"😳","proud":"😊","disappointed":"😞","lonely":"🥲","calm":"🧘",
    "upset":"😟","interested":"🧐","satisfied":"😌","thankful":"🙏","hopeful":"🌟","mood":"🙂","stress":"😣","confidence":"💪","courage":"🦁",
    "think":"💭","believe":"🙏","guess":"🤔","remember":"🧠","forget":"💨","mean":"💡","agree":"👍","disagree":"👎","opinion":"💬","idea":"💡",
    "reason":"❓","example":"🔎","fact":"✅","choice":"☝️","decision":"✅","advice":"💡","suggestion":"💬","possible":"✅","impossible":"🚫","confusing":"😵",
    "plan":"📝","appointment":"📅","meeting":"👥","date":"📆","event":"🎪","party":"🎉","festival":"🎊","deadline":"⏳","calendar":"📅","next week":"➡️",
    "this weekend":"🎉","tomorrow":"➡️","tonight":"🌙","join":"🙋","prepare":"🎒","decide":"✅","cancel":"❌","on time":"⏰","available":"🟢","reminder":"🔔",
    "health":"🩺","body":"🧍","eye":"👁️","ear":"👂","nose":"👃","mouth":"👄","tooth":"🦷","hand":"✋","arm":"💪","leg":"🦵",
    "foot":"🦶","stomach":"🤰","back":"🔙","heart":"❤️","clinic":"🏥","medicine":"💊","vitamin":"💊","diet":"🥗","cough":"😷","flu":"🤒",
    "smartphone":"📱","screen":"🖥️","app":"📲","website":"🌐","internet":"🌐","Wi-Fi":"📶","password":"🔐","text":"💬","video call":"📹","gallery":"🖼️",
    "news":"📰","channel":"📺","post":"📝","comment":"💬","upload":"⬆️","download":"⬇️","search":"🔎","click":"🖱️","battery":"🔋","notification":"🔔",
    "job":"💼","work":"💼","company":"🏢","office":"🏢","factory":"🏭","engineer":"🛠️","mechanic":"🔧","chef":"👨‍🍳","firefighter":"🚒","farmer":"🚜",
    "designer":"🎨","singer":"🎤","actor":"🎭","athlete":"🏃","dream":"🌈","future":"🔮","goal":"🎯","skill":"🛠️","interview":"🎙️","experience":"🌱",
    "car":"🚗","engine":"⚙️","wheel":"🛞","tire":"🛞","brake":"🛑","repair":"🔧","tool":"🛠️","machine":"⚙️","oil":"🛢️","electric":"⚡",
    "driver":"🚗","license":"🪪","safety":"🦺","helmet":"⛑️","manual":"📖","button":"🔘","signal":"🚦","speed":"💨","test drive":"🚗",
    "country":"🌍","city":"🏙️","capital":"🏛️","language":"🗣️","culture":"🎎","flag":"🏳️","people":"👥","food":"🍽️","holiday":"🎉","traditional":"🏮",
    "modern":"🏙️","world":"🌍","continent":"🗺️","Asia":"🌏","America":"🗽","Europe":"🏰",
    "help":"🆘","please":"🙏","sorry":"🙇","problem":"⚠️","question":"❓","answer":"✅","again":"🔁","slowly":"🐢","loudly":"📢","understand":"💡",
    "show":"👀","tell":"🗣️","need":"🙋","borrow":"🤲","lend":"🤝","find":"🔎","wait":"⏳","emergency":"🚨"
}

THEME_DIALOGUES = {
    "🏫 학교생활": [{"en":"A: What subject do you like?","ko":"A: 너는 어떤 과목을 좋아하니?"},{"en":"B: I like science.","ko":"B: 나는 과학을 좋아해."},{"en":"A: Do you have an assignment?","ko":"A: 과제가 있니?"},{"en":"B: Yes, I have a report.","ko":"B: 응, 보고서가 있어."}],
    "✏️ 교실 활동": [{"en":"A: Please repeat after me.","ko":"A: 나를 따라 반복해 주세요."},{"en":"B: Okay, I will repeat.","ko":"B: 네, 반복할게요."},{"en":"A: Circle the answer.","ko":"A: 정답에 동그라미 치세요."},{"en":"B: I can do it.","ko":"B: 할 수 있어요."}],
    "🍽️ 식당과 주문": [{"en":"A: May I take your order?","ko":"A: 주문하시겠어요?"},{"en":"B: I want a burger, please.","ko":"B: 햄버거 주세요."},{"en":"A: Anything else?","ko":"A: 더 필요한 것이 있나요?"},{"en":"B: No, thank you.","ko":"B: 아니요, 감사합니다."}],
    "🆘 도움 요청": [{"en":"A: Can you help me, please?","ko":"A: 저를 도와주실 수 있나요?"},{"en":"B: Sure. What is the problem?","ko":"B: 물론이죠. 문제가 무엇인가요?"},{"en":"A: Please speak slowly.","ko":"A: 천천히 말해 주세요."},{"en":"B: Okay. I will explain again.","ko":"B: 좋아요. 다시 설명할게요."}]
}

if "unknown_words" not in st.session_state:
    st.session_state.unknown_words = []
if "unknown_word_info" not in st.session_state:
    st.session_state.unknown_word_info = {}


def review_id(theme_name, word):
    return f"{theme_name}||{word}"


def add_unknown_word(word, meaning, theme_name):
    rid = review_id(theme_name, word)
    if rid not in st.session_state.unknown_words:
        st.session_state.unknown_words.append(rid)
    st.session_state.unknown_word_info[rid] = {"word": word, "meaning": meaning, "theme": theme_name}


def remove_unknown_word(rid):
    if rid in st.session_state.unknown_words:
        st.session_state.unknown_words.remove(rid)
    st.session_state.unknown_word_info.pop(rid, None)


def get_word_emoji(word):
    return EMOJI_MAP.get(word, "🌱")


def make_cassette_items(words, theme_name):
    return [{"word":w["word"], "meaning":w["meaning"], "emoji":get_word_emoji(w["word"]), "theme":theme_name} for w in words]


def flatten_all_words():
    all_items = []
    for theme_name, words in WORD_THEMES.items():
        all_items.extend(make_cassette_items(words, theme_name))
    return all_items


def show_cassette_audio(items, title):
    """
    핵심 수정 부분:
    예전에는 st.button('테마별 전체 단어 듣기')을 눌러야 카세트가 생성되었습니다.
    지금은 버튼 없이 처음부터 카세트 플레이어가 화면에 떠 있습니다.
    학생은 안에 있는 ▶️ 재생 버튼만 누르면 됩니다.
    """
    if title == "전체 단어":
        display_title = "🎧 전체 단어 듣기"
    elif title == "복습 희망":
        display_title = "🎧 복습 희망 단어 듣기"
    else:
        display_title = "🎧 테마별 전체 단어 듣기"
    js_cassette_visual_player(items, title=display_title, height=520)


def show_dialogue(theme_name):
    dialogue = THEME_DIALOGUES.get(theme_name, [])
    if not dialogue:
        return
    st.markdown('<div class="dialogue-box">', unsafe_allow_html=True)
    st.markdown('<div class="dialogue-title">💬 오늘의 일상 대화</div>', unsafe_allow_html=True)
    for line in dialogue:
        st.markdown(f"<div class='dialogue-line'>{clean_text(line['en'])}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dialogue-meaning'>{clean_text(line['ko'])}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    dialogue_text = " ".join(re.sub(r"^[A-Z]:\s*", "", x["en"]) for x in dialogue)
    browser_tts_button(dialogue_text, label="🔊 대화 듣기", height=72)


def show_word_list(theme_name, words):
    st.markdown("### 📚 단어 목록")
    for i, item in enumerate(words, start=1):
        word = item["word"]
        meaning = item["meaning"]
        rid = review_id(theme_name, word)
        c1, c2, c3, c4, c5 = st.columns([0.7, 2.2, 2.0, 0.7, 2.2])
        with c1:
            st.markdown(f"<div class='word-number'>{i}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='word-text'>{clean_text(word)}</div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='meaning-text'>{clean_text(meaning)}</div>", unsafe_allow_html=True)
        with c4:
            st.markdown(f"<div class='emoji-text'>{get_word_emoji(word)}</div>", unsafe_allow_html=True)
        with c5:
            browser_tts_button(word, label="🔊 듣기", height=58)
        checked = rid in st.session_state.unknown_words
        new_checked = st.checkbox("정확히 모르겠어요", value=checked, key=f"unknown_{safe_key(rid)}")
        if new_checked and not checked:
            add_unknown_word(word, meaning, theme_name)
        elif checked and not new_checked:
            remove_unknown_word(rid)
        st.markdown("<hr style='border:none; border-top:1px solid #dcfce7; margin:7px 0 12px 0;'>", unsafe_allow_html=True)


def make_quiz_items(theme_name, words, n):
    rng = random.Random(f"quiz_{theme_name}_{n}")
    selected = words[:]
    rng.shuffle(selected)
    selected = selected[:min(n, len(selected))]
    all_meanings = [w["meaning"] for theme_words in WORD_THEMES.values() for w in theme_words]
    quiz_items = []
    for item in selected:
        wrongs = [m for m in all_meanings if m != item["meaning"]]
        options = rng.sample(wrongs, k=3) + [item["meaning"]]
        rng.shuffle(options)
        quiz_items.append({"word":item["word"], "answer":item["meaning"], "options":options})
    return quiz_items


def show_quiz(theme_name, words):
    st.markdown("### ✅ 뜻 확인 퀴즈")
    quiz_count = st.selectbox("문제 개수", [2, 5, 10, 15, 20], index=1, key=f"quiz_count_{safe_key(theme_name)}")
    quiz_items = make_quiz_items(theme_name, words, quiz_count)
    answers = []
    for i, q in enumerate(quiz_items, start=1):
        st.markdown(f"""
        <div class='quiz-card'>
            <div class='quiz-number'>{i}</div>
            <div class='quiz-word'>{clean_text(q['word'])}</div>
        </div>
        """, unsafe_allow_html=True)
        picked = st.radio("뜻을 고르세요.", q["options"], key=f"quiz_{safe_key(theme_name)}_{i}_{q['word']}", index=None)
        answers.append((q, picked))
    if st.button("정답 확인", key=f"submit_quiz_{safe_key(theme_name)}", use_container_width=True):
        score = sum(1 for q, picked in answers if picked == q["answer"])
        st.markdown(f"<div class='score-box'><div class='score-title'>점수: {score} / {len(quiz_items)}</div></div>", unsafe_allow_html=True)
        for i, (q, picked) in enumerate(answers, start=1):
            if picked != q["answer"]:
                st.markdown(f"<div class='wrong-box'>{i}번 다시 확인: {clean_text(q['word'])}<br>내 답: {clean_text(picked) if picked else '선택 안 함'}<br>정답: <b>{clean_text(q['answer'])}</b></div>", unsafe_allow_html=True)


def show_theme_page(theme_name):
    words = WORD_THEMES[theme_name]
    st.markdown(f"""
    <div class='theme-header'>
        <div class='theme-title'>{clean_text(theme_name)}</div>
        <div class='theme-desc'>이 테마의 단어를 듣고, 뜻을 확인하고, 필요한 단어는 복습 희망에 저장해 보세요.</div>
    </div>
    """, unsafe_allow_html=True)

    # 테마별 전체 단어 듣기: 클릭 전에도 처음부터 화면에 표시됨
    show_cassette_audio(make_cassette_items(words, theme_name), theme_name)
    show_dialogue(theme_name)
    show_word_list(theme_name, words)
    show_quiz(theme_name, words)


def show_all_cassette_tab():
    show_cassette_audio(flatten_all_words(), "전체 단어")


def show_review_tab():
    st.markdown("### ⭐ 복습 희망 단어")
    if not st.session_state.unknown_words:
        st.info("아직 복습 희망 단어가 없습니다. 단어 목록에서 '정확히 모르겠어요'를 체크해 주세요.")
        return
    items = []
    for rid in st.session_state.unknown_words:
        info = st.session_state.unknown_word_info.get(rid)
        if info:
            items.append({"word":info["word"], "meaning":info["meaning"], "emoji":get_word_emoji(info["word"]), "theme":info["theme"]})
    show_cassette_audio(items, "복습 희망")
    for i, item in enumerate(items, start=1):
        st.markdown(f"{i}. **{item['word']}** — {item['meaning']} ({item['theme']})")


st.markdown("<div class='main-title'>🌱 Daily English 400</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>기초 일상대화에 필요한 단어와 문장을 듣고 읽어 봅시다.</div>", unsafe_allow_html=True)
st.markdown("""
<div class='hero-box'>
    <div class='hero-title'>🎧 듣기 버튼을 따로 누르지 않아도 카세트가 처음부터 보입니다.</div>
    <div class='hero-text'>테마를 선택하면 바로 큰 단어 카드형 플레이어가 나타납니다. 학생은 플레이어 안의 ▶️ 재생 버튼만 누르면 됩니다.</div>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["🎧 전체 단어", "📚 테마별 학습", "⭐ 복습 희망"])

with tabs[0]:
    show_all_cassette_tab()

with tabs[1]:
    theme_names = list(WORD_THEMES.keys())
    selected_theme = st.selectbox("테마 선택", theme_names, index=0)
    show_theme_page(selected_theme)

with tabs[2]:
    show_review_tab()
