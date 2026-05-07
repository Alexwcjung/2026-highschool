import streamlit as st
import random
import json
import html
import uuid
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Survival English 160",
    page_icon="🛟",
    layout="wide"
)

st.markdown("""
<style>
.main-title {{font-size:44px;font-weight:900;color:#1f2937;margin-bottom:4px;}}
.sub-title {{font-size:17px;color:#6b7280;margin-bottom:24px;}}
.hero-box {{background:linear-gradient(135deg,#ecfeff 0%,#fef3c7 50%,#fce7f3 100%);border-radius:22px;padding:18px 22px;margin-bottom:24px;box-shadow:0 6px 18px rgba(0,0,0,.06);border:1px solid rgba(255,255,255,.8);}}
.theme-header {{background:linear-gradient(135deg,#0ea5e9 0%,#8b5cf6 50%,#ec4899 100%);color:white;padding:30px 32px;border-radius:28px;margin-bottom:26px;box-shadow:0 10px 24px rgba(14,165,233,.28);}}
.theme-title {{font-size:40px;font-weight:1000;margin-bottom:10px;letter-spacing:-.5px;line-height:1.15;}}
.theme-desc {{font-size:19px;font-weight:800;opacity:.98;line-height:1.55;}}
.word-card {{background:white;border-radius:18px;padding:10px 14px;margin-bottom:8px;border:1px solid #e0f2fe;box-shadow:0 3px 10px rgba(0,0,0,.04);}}
.word-row {{display:flex;align-items:center;gap:10px;}}
.word-number {{min-width:38px;font-size:13px;font-weight:900;color:#0369a1;background:#e0f2fe;border-radius:999px;padding:5px 9px;text-align:center;}}
.word-text {{min-width:170px;font-size:25px;font-weight:900;color:#111827;white-space:nowrap;}}
.meaning-text {{font-size:19px;font-weight:800;color:#374151;margin-left:8px;white-space:nowrap;line-height:42px;}}
.emoji-text {{font-size:25px;line-height:1;text-align:center;padding-top:2px;}}
.quiz-card {{background:#fff;border-radius:24px;padding:22px 24px;margin-bottom:18px;border:1px solid #e9d5ff;box-shadow:0 5px 18px rgba(0,0,0,.06);}}
.quiz-number {{display:inline-block;background:#dcfce7;color:#166534;padding:6px 12px;border-radius:999px;font-weight:900;font-size:13px;margin-bottom:10px;}}
.quiz-word {{font-size:34px;font-weight:900;color:#111827;margin-bottom:8px;}}
.score-box {{background:linear-gradient(135deg,#dcfce7 0%,#dbeafe 50%,#fce7f3 100%);border-radius:24px;padding:24px 26px;margin:20px 0;border:1px solid #bbf7d0;box-shadow:0 6px 18px rgba(0,0,0,.06);}}
.score-title {{font-size:27px;font-weight:900;color:#14532d;}}
.wrong-box {{background:#fff7ed;border-left:6px solid #fb923c;border-radius:18px;padding:16px 18px;margin:18px 0;color:#7c2d12;font-weight:700;}}
.answer-box {{background:#f8fafc;border-radius:20px;padding:18px 20px;border:1px solid #e2e8f0;margin-bottom:16px;}}
.stButton > button {{border-radius:999px;font-weight:800;border:1px solid #d1d5db;padding:.45rem 1rem;}}
.stButton > button:hover {{border-color:#0ea5e9;color:#0ea5e9;}}
div[data-baseweb="tab-list"] {{gap:10px;flex-wrap:wrap;}}
button[data-baseweb="tab"] {{min-height:58px;padding:12px 18px;border-radius:18px 18px 0 0;background:#f8fafc;border:1px solid #e5e7eb;margin-right:4px;}}
button[data-baseweb="tab"] p {{font-size:21px!important;font-weight:1000!important;color:#111827!important;line-height:1.25!important;white-space:nowrap;}}
button[data-baseweb="tab"][aria-selected="true"] {{background:linear-gradient(135deg,#dbeafe,#fce7f3);border-bottom:4px solid #8b5cf6;}}
div[role="radiogroup"] label p {{font-size:18px!important;font-weight:900!important;}}
@media(max-width:600px){{.main-title{{font-size:34px;}}.theme-header{{padding:24px 22px;border-radius:24px;}}.theme-title{{font-size:33px;}}.theme-desc{{font-size:16px;}}button[data-baseweb="tab"]{{min-height:52px;padding:10px 14px;}}button[data-baseweb="tab"] p{{font-size:18px!important;}}}}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🛟 Survival English 160</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>생존 회화에 꼭 필요한 문장과 단어를 듣고, 따라 하고, 퀴즈로 익혀 봅시다.</div>", unsafe_allow_html=True)
st.markdown("""
<div class="hero-box"><div style="font-size:18px;font-weight:900;color:#374151;">이 단어 160개만 외우면 미국에서 생존이 가능합니다.</div></div>
""", unsafe_allow_html=True)

word_themes = {'🧍 나와 사람': [{'word': 'I', 'meaning': '나'},
             {'word': 'you', 'meaning': '너, 당신'},
             {'word': 'he', 'meaning': '그'},
             {'word': 'she', 'meaning': '그녀'},
             {'word': 'we', 'meaning': '우리'},
             {'word': 'they', 'meaning': '그들'},
             {'word': 'friend', 'meaning': '친구'},
             {'word': 'teacher', 'meaning': '선생님'},
             {'word': 'student', 'meaning': '학생'},
             {'word': 'classmate', 'meaning': '반 친구'},
             {'word': 'family', 'meaning': '가족'},
             {'word': 'father', 'meaning': '아버지'},
             {'word': 'mother', 'meaning': '어머니'},
             {'word': 'brother', 'meaning': '형제, 남자 형제'},
             {'word': 'sister', 'meaning': '자매, 여자 형제'},
             {'word': 'name', 'meaning': '이름'},
             {'word': 'person', 'meaning': '사람'},
             {'word': 'man', 'meaning': '남자'},
             {'word': 'woman', 'meaning': '여자'},
             {'word': 'child', 'meaning': '아이'}],
 '🏃 기본 동작': [{'word': 'go', 'meaning': '가다'},
             {'word': 'come', 'meaning': '오다'},
             {'word': 'walk', 'meaning': '걷다'},
             {'word': 'run', 'meaning': '달리다'},
             {'word': 'sit', 'meaning': '앉다'},
             {'word': 'stand', 'meaning': '서다'},
             {'word': 'stop', 'meaning': '멈추다'},
             {'word': 'start', 'meaning': '시작하다'},
             {'word': 'open', 'meaning': '열다'},
             {'word': 'close', 'meaning': '닫다'},
             {'word': 'eat', 'meaning': '먹다'},
             {'word': 'drink', 'meaning': '마시다'},
             {'word': 'sleep', 'meaning': '자다'},
             {'word': 'study', 'meaning': '공부하다'},
             {'word': 'read', 'meaning': '읽다'},
             {'word': 'write', 'meaning': '쓰다'},
             {'word': 'listen', 'meaning': '듣다'},
             {'word': 'speak', 'meaning': '말하다'},
             {'word': 'help', 'meaning': '돕다'},
             {'word': 'wait', 'meaning': '기다리다'}],
 '💖 감정·몸 상태': [{'word': 'happy', 'meaning': '행복한'},
               {'word': 'sad', 'meaning': '슬픈'},
               {'word': 'angry', 'meaning': '화난'},
               {'word': 'tired', 'meaning': '피곤한'},
               {'word': 'hungry', 'meaning': '배고픈'},
               {'word': 'thirsty', 'meaning': '목마른'},
               {'word': 'sick', 'meaning': '아픈'},
               {'word': 'okay', 'meaning': '괜찮은'},
               {'word': 'fine', 'meaning': '괜찮은'},
               {'word': 'cold', 'meaning': '추운, 차가운'},
               {'word': 'hot', 'meaning': '더운, 뜨거운'},
               {'word': 'pain', 'meaning': '통증'},
               {'word': 'headache', 'meaning': '두통'},
               {'word': 'stomachache', 'meaning': '복통'},
               {'word': 'fever', 'meaning': '열'},
               {'word': 'hurt', 'meaning': '아프다, 다치다'},
               {'word': 'good', 'meaning': '좋은'},
               {'word': 'bad', 'meaning': '나쁜'},
               {'word': 'worried', 'meaning': '걱정하는'},
               {'word': 'scared', 'meaning': '무서워하는'}],
 '🍎 음식·물': [{'word': 'food', 'meaning': '음식'},
            {'word': 'water', 'meaning': '물'},
            {'word': 'rice', 'meaning': '밥, 쌀'},
            {'word': 'bread', 'meaning': '빵'},
            {'word': 'milk', 'meaning': '우유'},
            {'word': 'juice', 'meaning': '주스'},
            {'word': 'coffee', 'meaning': '커피'},
            {'word': 'tea', 'meaning': '차'},
            {'word': 'apple', 'meaning': '사과'},
            {'word': 'banana', 'meaning': '바나나'},
            {'word': 'egg', 'meaning': '달걀'},
            {'word': 'meat', 'meaning': '고기'},
            {'word': 'chicken', 'meaning': '닭고기, 닭'},
            {'word': 'fish', 'meaning': '생선, 물고기'},
            {'word': 'breakfast', 'meaning': '아침 식사'},
            {'word': 'lunch', 'meaning': '점심 식사'},
            {'word': 'dinner', 'meaning': '저녁 식사'},
            {'word': 'snack', 'meaning': '간식'},
            {'word': 'medicine', 'meaning': '약'},
            {'word': 'hospital', 'meaning': '병원'}],
 '🚗 장소·이동': [{'word': 'home', 'meaning': '집'},
             {'word': 'school', 'meaning': '학교'},
             {'word': 'classroom', 'meaning': '교실'},
             {'word': 'bathroom', 'meaning': '화장실'},
             {'word': 'hospital', 'meaning': '병원'},
             {'word': 'store', 'meaning': '가게'},
             {'word': 'station', 'meaning': '역'},
             {'word': 'bus', 'meaning': '버스'},
             {'word': 'car', 'meaning': '자동차'},
             {'word': 'taxi', 'meaning': '택시'},
             {'word': 'train', 'meaning': '기차'},
             {'word': 'bike', 'meaning': '자전거'},
             {'word': 'road', 'meaning': '도로'},
             {'word': 'street', 'meaning': '거리'},
             {'word': 'here', 'meaning': '여기'},
             {'word': 'there', 'meaning': '거기'},
             {'word': 'near', 'meaning': '가까운'},
             {'word': 'far', 'meaning': '먼'},
             {'word': 'left', 'meaning': '왼쪽'},
             {'word': 'right', 'meaning': '오른쪽, 맞는'}],
 '⏰ 시간·숫자': [{'word': 'time', 'meaning': '시간'},
             {'word': 'now', 'meaning': '지금'},
             {'word': 'today', 'meaning': '오늘'},
             {'word': 'tomorrow', 'meaning': '내일'},
             {'word': 'yesterday', 'meaning': '어제'},
             {'word': 'morning', 'meaning': '아침'},
             {'word': 'afternoon', 'meaning': '오후'},
             {'word': 'evening', 'meaning': '저녁'},
             {'word': 'night', 'meaning': '밤'},
             {'word': 'nine', 'meaning': '아홉'},
             {'word': 'late', 'meaning': '늦은'},
             {'word': 'one', 'meaning': '하나'},
             {'word': 'two', 'meaning': '둘'},
             {'word': 'three', 'meaning': '셋'},
             {'word': 'four', 'meaning': '넷'},
             {'word': 'five', 'meaning': '다섯'},
             {'word': 'six', 'meaning': '여섯'},
             {'word': 'seven', 'meaning': '일곱'},
             {'word': 'eight', 'meaning': '여덟'},
             {'word': 'ten', 'meaning': '열'}],
 '🎒 물건·돈': [{'word': 'bag', 'meaning': '가방'},
            {'word': 'phone', 'meaning': '전화기'},
            {'word': 'book', 'meaning': '책'},
            {'word': 'notebook', 'meaning': '공책'},
            {'word': 'pen', 'meaning': '펜'},
            {'word': 'pencil', 'meaning': '연필'},
            {'word': 'desk', 'meaning': '책상'},
            {'word': 'chair', 'meaning': '의자'},
            {'word': 'door', 'meaning': '문'},
            {'word': 'window', 'meaning': '창문'},
            {'word': 'key', 'meaning': '열쇠'},
            {'word': 'money', 'meaning': '돈'},
            {'word': 'card', 'meaning': '카드'},
            {'word': 'ticket', 'meaning': '표, 티켓'},
            {'word': 'clothes', 'meaning': '옷'},
            {'word': 'shoes', 'meaning': '신발'},
            {'word': 'hat', 'meaning': '모자'},
            {'word': 'watch', 'meaning': '시계'},
            {'word': 'cup', 'meaning': '컵'},
            {'word': 'bottle', 'meaning': '병'}],
 '🆘 도움 요청': [{'word': 'help', 'meaning': '도움, 돕다'},
             {'word': 'please', 'meaning': '부디, 제발'},
             {'word': 'sorry', 'meaning': '미안합니다'},
             {'word': 'excuse me', 'meaning': '실례합니다'},
             {'word': 'again', 'meaning': '다시'},
             {'word': 'slowly', 'meaning': '천천히'},
             {'word': 'understand', 'meaning': '이해하다'},
             {'word': 'question', 'meaning': '질문'},
             {'word': 'problem', 'meaning': '문제'},
             {'word': 'need', 'meaning': '필요하다'},
             {'word': 'want', 'meaning': '원하다'},
             {'word': 'know', 'meaning': '알다'},
             {'word': 'say', 'meaning': '말하다'},
             {'word': 'tell', 'meaning': '말하다, 알려주다'},
             {'word': 'ask', 'meaning': '묻다'},
             {'word': 'answer', 'meaning': '대답, 답'},
             {'word': 'repeat', 'meaning': '반복하다'},
             {'word': 'speak', 'meaning': '말하다'},
             {'word': 'look', 'meaning': '보다'},
             {'word': 'listen', 'meaning': '듣다'}]}
WORD_EMOJIS = {'I': '🙋',
 'you': '👉',
 'he': '👦',
 'she': '👧',
 'we': '👥',
 'they': '👥',
 'friend': '🤝',
 'teacher': '👩\u200d🏫',
 'student': '🧑\u200d🎓',
 'classmate': '👫',
 'family': '👨\u200d👩\u200d👧',
 'father': '👨',
 'mother': '👩',
 'brother': '👦',
 'sister': '👧',
 'name': '🏷️',
 'person': '🧍',
 'man': '👨',
 'woman': '👩',
 'child': '🧒',
 'go': '➡️',
 'come': '⬅️',
 'walk': '🚶',
 'run': '🏃',
 'sit': '🪑',
 'stand': '🧍',
 'stop': '🛑',
 'start': '▶️',
 'open': '📂',
 'close': '📕',
 'eat': '🍽️',
 'drink': '🥤',
 'sleep': '😴',
 'study': '📚',
 'read': '📖',
 'write': '✏️',
 'listen': '👂',
 'speak': '🗣️',
 'help': '🆘',
 'wait': '⏳',
 'happy': '😊',
 'sad': '😢',
 'angry': '😠',
 'tired': '🥱',
 'hungry': '😋',
 'thirsty': '🥤',
 'sick': '🤒',
 'okay': '👌',
 'fine': '🙂',
 'cold': '🥶',
 'hot': '🥵',
 'pain': '🤕',
 'headache': '🤯',
 'stomachache': '🤢',
 'fever': '🌡️',
 'hurt': '🩹',
 'good': '👍',
 'bad': '👎',
 'worried': '😟',
 'scared': '😨',
 'food': '🍽️',
 'water': '💧',
 'rice': '🍚',
 'bread': '🍞',
 'milk': '🥛',
 'juice': '🧃',
 'coffee': '☕',
 'tea': '🍵',
 'apple': '🍎',
 'banana': '🍌',
 'egg': '🥚',
 'meat': '🥩',
 'chicken': '🍗',
 'fish': '🐟',
 'breakfast': '🍳',
 'lunch': '🍱',
 'dinner': '🍽️',
 'snack': '🍪',
 'medicine': '💊',
 'hospital': '🏥',
 'home': '🏠',
 'school': '🏫',
 'classroom': '🧑\u200d🏫',
 'bathroom': '🚻',
 'store': '🏪',
 'station': '🚉',
 'bus': '🚌',
 'car': '🚗',
 'taxi': '🚕',
 'train': '🚆',
 'bike': '🚲',
 'road': '🛣️',
 'street': '🏙️',
 'here': '📍',
 'there': '📌',
 'near': '↔️',
 'far': '🌁',
 'left': '⬅️',
 'right': '➡️',
 'time': '⏰',
 'now': '🕒',
 'today': '📅',
 'tomorrow': '➡️📅',
 'yesterday': '⬅️📅',
 'morning': '🌅',
 'afternoon': '☀️',
 'evening': '🌆',
 'night': '🌙',
 'early': '🐓',
 'late': '🌃',
 'one': '1️⃣',
 'two': '2️⃣',
 'three': '3️⃣',
 'four': '4️⃣',
 'five': '5️⃣',
 'six': '6️⃣',
 'seven': '7️⃣',
 'eight': '8️⃣',
 'nine': '9️⃣',
 'ten': '🔟',
 'bag': '🎒',
 'phone': '📱',
 'book': '📘',
 'notebook': '📓',
 'pen': '🖊️',
 'pencil': '✏️',
 'desk': '🪑',
 'chair': '🪑',
 'door': '🚪',
 'window': '🪟',
 'key': '🔑',
 'money': '💵',
 'card': '💳',
 'ticket': '🎫',
 'clothes': '👕',
 'shoes': '👟',
 'hat': '🧢',
 'watch': '⌚',
 'cup': '☕',
 'bottle': '🍼',
 'please': '🙏',
 'sorry': '🙇',
 'excuse me': '🙋',
 'again': '🔁',
 'slowly': '🐢',
 'understand': '💡',
 'question': '❓',
 'problem': '⚠️',
 'need': '📌',
 'want': '✨',
 'know': '🧠',
 'say': '💬',
 'tell': '📣',
 'ask': '❔',
 'answer': '✅',
 'repeat': '🔁',
 'look': '👀'}

AUDIO_CHANNEL_NAME = "survival_english_audio_channel"


def inject_global_audio_manager():
    components.html(r"""
    <script>
    (function() {
        const root = window.parent || window;
        if (root.__survivalAudioManagerReady) return;
        root.__survivalAudioManagerReady = true;

        const script = root.document.createElement("script");
        script.id = "survival-audio-manager-script";
        script.textContent = `
        (function() {
            if (window.__survivalAudioManager) return;
            window.__survivalAudioManager = {
                token: 0,
                timer: null,
                state: { type: "idle", index: 0, round: 1, repeat: 1, word: "" },
                channelName: "survival_english_audio_channel",
                clearTimer: function() {
                    if (this.timer) { clearTimeout(this.timer); this.timer = null; }
                },
                getVoice: function() {
                    const voices = window.speechSynthesis.getVoices ? window.speechSynthesis.getVoices() : [];
                    const preferred = ["Samantha", "Google US English", "Microsoft Jenny", "Microsoft Aria", "Microsoft Zira", "Karen", "Victoria"];
                    for (const name of preferred) {
                        const v = voices.find(x => x.name && x.name.toLowerCase().includes(name.toLowerCase()) && x.lang && x.lang.toLowerCase().startsWith("en"));
                        if (v) return v;
                    }
                    return voices.find(x => x.lang && x.lang.toLowerCase().startsWith("en")) || null;
                },
                broadcast: function(data) {
                    try { new BroadcastChannel(this.channelName).postMessage(data); } catch(e) {}
                },
                stop: function() {
                    this.token += 1;
                    this.clearTimer();
                    try { window.speechSynthesis.cancel(); } catch(e) {}
                    this.state.type = "idle";
                    this.broadcast({ type: "GLOBAL_AUDIO_STOPPED" });
                },
                speakOnce: function(text, rate, token, done) {
                    if (token !== this.token) return;
                    let u = new SpeechSynthesisUtterance(text || "");
                    u.lang = "en-US";
                    u.rate = rate || 0.75;
                    u.pitch = 1.05;
                    const voice = this.getVoice();
                    if (voice) u.voice = voice;
                    let finished = false;
                    const finish = () => {
                        if (finished) return;
                        finished = true;
                        if (token !== this.token) return;
                        done && done();
                    };
                    u.onend = finish;
                    u.onerror = finish;
                    try { window.speechSynthesis.speak(u); } catch(e) { finish(); }
                    const safeMs = Math.max(900, String(text || "").length * 145 / Math.max(rate || 0.75, 0.45));
                    this.clearTimer();
                    this.timer = setTimeout(finish, safeMs + 900);
                },
                speakSingle: function(text, opt) {
                    opt = opt || {};
                    this.stop();
                    this.token += 1;
                    const token = this.token;
                    const repeat = opt.repeat || 1;
                    const rate = opt.rate || 0.75;
                    const pause = opt.pause || 450;
                    let n = 0;
                    this.state = { type: "single", index: 0, round: 1, repeat: repeat, word: text };
                    const loop = () => {
                        if (token !== this.token) return;
                        if (n >= repeat) { this.broadcast({ type: "GLOBAL_AUDIO_DONE" }); return; }
                        n += 1;
                        this.broadcast({ type: "GLOBAL_AUDIO_WORD", word: text, repeatNow: n, repeatTotal: repeat, mode: "single" });
                        this.speakOnce(text, rate, token, () => { this.timer = setTimeout(loop, pause); });
                    };
                    loop();
                },
                playCassette: function(items, opt) {
                    opt = opt || {};
                    this.stop();
                    this.token += 1;
                    const token = this.token;
                    const rate = opt.rate || 0.75;
                    const repeatMax = opt.repeatMax || 1;
                    const eachRepeat = opt.eachRepeat || 2;
                    const pause = opt.pause || 500;
                    let index = Math.max(0, Math.min(items.length - 1, opt.startIndex || 0));
                    let round = 1;
                    let each = 0;
                    this.state = { type: "cassette", index: index, round: round, repeat: repeatMax, word: "" };
                    const loop = () => {
                        if (token !== this.token) return;
                        if (!items || !items.length) return;
                        if (index >= items.length) {
                            if (round < repeatMax) { round += 1; index = 0; each = 0; }
                            else {
                                this.state = { type: "idle", index: items.length - 1, round: round, repeat: repeatMax, word: items[items.length - 1].word };
                                this.broadcast({ type: "GLOBAL_AUDIO_DONE" });
                                return;
                            }
                        }
                        const item = items[index];
                        each += 1;
                        this.state = { type: "cassette", index: index, round: round, repeat: repeatMax, word: item.word };
                        this.broadcast({ type: "GLOBAL_AUDIO_WORD", word: item.word, meaning: item.meaning, index: index, total: items.length, round: round, repeatTotal: repeatMax, each: each, eachTotal: eachRepeat, theme: item.theme, mode: "cassette" });
                        this.speakOnce(item.word, rate, token, () => {
                            if (token !== this.token) return;
                            if (each < eachRepeat) {
                                this.timer = setTimeout(loop, pause);
                            } else {
                                each = 0;
                                index += 1;
                                this.timer = setTimeout(loop, pause);
                            }
                        });
                    };
                    loop();
                },
                pause: function() { try { window.speechSynthesis.pause(); } catch(e) {} },
                resume: function() { try { window.speechSynthesis.resume(); } catch(e) {} }
            };
        })();`;
        root.document.head.appendChild(script);
    })();
    </script>
    """, height=0)

inject_global_audio_manager()


def get_word_emoji(word):
    return WORD_EMOJIS.get(word, "🌱")


def html_word_audio_player(label, text, repeat_count=20, pause_ms=1500, height=42):
    player_id = f"word_player_{{uuid.uuid4().hex}}"
    safe_label = json.dumps(label, ensure_ascii=False)
    safe_text = json.dumps(text, ensure_ascii=False)
    safe_player_id = json.dumps(player_id)
    components.html(f"""
    <div style="font-family:Arial,sans-serif;display:flex;align-items:center;gap:6px;height:36px;">
        <button id="play_{{player_id}}" style="background:linear-gradient(135deg,#fce7f3,#dbeafe);border:1px solid #e9d5ff;border-radius:999px;padding:5px 8px;font-weight:800;font-size:12px;color:#374151;cursor:pointer;white-space:nowrap;">{{label}}</button>
        <button id="stop_{{player_id}}" style="background:#fff7ed;border:1px solid #fed7aa;border-radius:999px;padding:5px 8px;font-weight:800;font-size:12px;color:#9a3412;cursor:pointer;white-space:nowrap;">⏹ 중지</button>
        <span id="status_{{player_id}}" style="font-size:12px;color:#075985;font-weight:700;white-space:nowrap;"></span>
        <script>
        (function() {{
            const root = window.parent || window;
            const playBtn = document.getElementById("play_{{player_id}}");
            const stopBtn = document.getElementById("stop_{{player_id}}");
            const status = document.getElementById("status_{{player_id}}");
            const wordText = {{safe_text}};
            const labelText = {{safe_label}};
            const playerId = {{safe_player_id}};
            let channel = null;
            try {{ channel = new BroadcastChannel("survival_english_audio_channel"); }} catch(e) {{}}
            if (channel) {{
                channel.onmessage = function(event) {{
                    if (!event.data) return;
                    if (event.data.type === "GLOBAL_AUDIO_WORD" && event.data.mode === "single" && event.data.word === wordText) {{
                        status.innerText = event.data.repeatNow + "/" + event.data.repeatTotal;
                        playBtn.innerText = "재생중";
                    }}
                    if (event.data.type === "GLOBAL_AUDIO_DONE" || event.data.type === "GLOBAL_AUDIO_STOPPED") {{
                        playBtn.innerText = labelText;
                    }}
                }};
            }}
            playBtn.addEventListener("click", function() {{
                if (root.__survivalAudioManager) {{
                    root.__survivalAudioManager.speakSingle(wordText, {{ repeat: {repeat_count}, rate: 0.75, pause: {pause_ms} }});
                    status.innerText = "시작";
                    playBtn.innerText = "재생중";
                }} else {{ status.innerText = "다시 클릭"; }}
            }});
            stopBtn.addEventListener("click", function() {{
                if (root.__survivalAudioManager) root.__survivalAudioManager.stop();
                status.innerText = "중지됨";
                playBtn.innerText = labelText;
            }});
        }})();
        </script>
    </div>
    """, height=height)


def audio_button(label, text, key=None):
    html_word_audio_player(label, text, repeat_count=20, pause_ms=1500, height=42)


def flatten_survival_words():
    all_items = []
    number = 1
    for theme_name, theme_words in word_themes.items():
        for item in theme_words:
            all_items.append({"number": number, "theme": theme_name, "word": item["word"], "meaning": item["meaning"]})
            number += 1
    return all_items


def make_theme_cassette_items(theme_words, theme_name):
    return [{"number": idx, "theme": theme_name, "word": item["word"], "meaning": item["meaning"]} for idx, item in enumerate(theme_words, start=1)]


def browser_easy_cassette_player(all_items, title="📼 단어 카세트", intro="재생 버튼을 누르면 단어가 차례대로 재생됩니다.", height=600):
    player_id = f"cassette_{{uuid.uuid4().hex}}"
    cassette_json = json.dumps(all_items, ensure_ascii=False)
    safe_title = html.escape(title)
    safe_intro = html.escape(intro)
    max_index = max(len(all_items) - 1, 0)
    components.html(f"""
    <style>
    .easy-cassette-wrap{{font-family:Arial,sans-serif;width:100%;max-width:100%;box-sizing:border-box;overflow:hidden;border-radius:28px;padding:20px;background:linear-gradient(135deg,#eff6ff 0%,#fff7ed 48%,#fdf2f8 100%);border:1px solid #bae6fd;box-shadow:0 8px 22px rgba(15,23,42,.10);}}
    .easy-cassette-top{{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:12px;}}
    .easy-cassette-title{{font-size:24px;font-weight:900;color:#0f172a;line-height:1.25;}}
    .easy-cassette-small{{font-size:13px;font-weight:900;color:#475569;background:rgba(255,255,255,.75);border:1px solid #dbeafe;border-radius:999px;padding:7px 12px;}}
    .easy-now-card{{background:rgba(255,255,255,.86);border:1px solid #dbeafe;border-radius:24px;padding:18px;margin:12px 0;}}
    .easy-theme{{display:inline-block;font-size:13px;font-weight:900;color:#7c3aed;background:#f3e8ff;border-radius:999px;padding:6px 11px;margin-bottom:9px;}}
    .easy-word{{font-size:clamp(42px,9vw,72px);font-weight:900;color:#111827;line-height:1.05;word-break:break-word;letter-spacing:-1px;}}
    .easy-meaning{{margin-top:8px;font-size:clamp(20px,5vw,31px);font-weight:900;color:#334155;line-height:1.25;word-break:keep-all;}}
    .easy-progress-box{{background:rgba(255,255,255,.76);border:1px solid #dbeafe;border-radius:20px;padding:13px 14px;margin:12px 0;}}
    .easy-bar-bg{{width:100%;height:14px;background:#e2e8f0;border-radius:999px;overflow:hidden;margin:8px 0 9px 0;}}
    .easy-bar-fill{{height:100%;width:0%;background:linear-gradient(90deg,#38bdf8,#8b5cf6,#ec4899);border-radius:999px;}}
    .easy-range{{width:100%;height:34px;accent-color:#8b5cf6;cursor:pointer;}}
    .easy-control-grid{{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:9px;margin-top:12px;}}
    .easy-sub-grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:8px;}}
    .easy-btn{{width:100%;min-height:48px;border-radius:18px;border:1px solid #cbd5e1;font-size:16px;font-weight:900;cursor:pointer;box-sizing:border-box;white-space:nowrap;box-shadow:0 3px 9px rgba(15,23,42,.07);}}
    .easy-btn-main{{min-height:58px;font-size:20px;background:linear-gradient(135deg,#dbeafe,#fce7f3);border-color:#c4b5fd;color:#111827;}}
    .easy-select-row{{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:10px;}}
    .easy-select-box{{background:rgba(255,255,255,.84);border:1px solid #dbeafe;border-radius:18px;padding:10px 12px;box-sizing:border-box;}}
    .easy-label{{font-size:12px;font-weight:900;color:#64748b;margin-bottom:5px;}}
    .easy-select{{width:100%;border:0;background:transparent;font-size:16px;font-weight:900;color:#0f172a;outline:none;}}
    .easy-status{{margin-top:10px;font-size:14px;font-weight:900;color:#075985;min-height:20px;line-height:1.35;}}
    @media(max-width:520px){{.easy-cassette-wrap{{padding:14px 11px;border-radius:22px;}}.easy-cassette-title{{font-size:19px;}}.easy-control-grid{{grid-template-columns:1fr;gap:7px;}}.easy-btn{{min-height:43px;font-size:13px;border-radius:15px;padding:7px 4px;}}.easy-btn-main{{min-height:52px;font-size:18px;}}}}
    </style>
    <div class="easy-cassette-wrap">
        <div class="easy-cassette-top"><div class="easy-cassette-title">{safe_title}</div><div id="count_{player_id}" class="easy-cassette-small">1 / {len(all_items)}</div></div>
        <div style="font-size:14px;font-weight:800;color:#475569;line-height:1.5;margin-bottom:8px;">{safe_intro}</div>
        <div class="easy-now-card"><div id="theme_{player_id}" class="easy-theme">Theme</div><div id="word_{player_id}" class="easy-word">Ready</div><div id="meaning_{player_id}" class="easy-meaning">재생 버튼을 눌러 주세요.</div></div>
        <div class="easy-progress-box"><div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:4px;"><span style="font-size:13px;font-weight:900;color:#075985;">🎚️ 단어 위치</span><span id="percent_{player_id}" style="font-size:13px;font-weight:900;color:#7c3aed;">0%</span></div><div class="easy-bar-bg"><div id="bar_{player_id}" class="easy-bar-fill"></div></div><input id="progress_{player_id}" class="easy-range" type="range" min="0" max="{max_index}" value="0" step="1"></div>
        <div class="easy-control-grid"><button id="play_{player_id}" class="easy-btn easy-btn-main">▶️ 듣기</button><button id="pause_{player_id}" class="easy-btn" style="background:#ecfeff;border-color:#67e8f9;color:#155e75;">⏸ 잠깐 멈춤</button><button id="replay_{player_id}" class="easy-btn" style="background:#fef3c7;border-color:#fde68a;color:#92400e;">🔁 현재 단어</button></div>
        <div class="easy-sub-grid"><button id="prev_{player_id}" class="easy-btn" style="background:#f8fafc;color:#334155;">⏮ 이전</button><button id="stop_{player_id}" class="easy-btn" style="background:#fff7ed;border-color:#fed7aa;color:#9a3412;">⏹ 처음</button><button id="next_{player_id}" class="easy-btn" style="background:#f8fafc;color:#334155;">다음 ⏭</button></div>
        <div class="easy-select-row"><div class="easy-select-box"><div class="easy-label">속도</div><select id="speed_{player_id}" class="easy-select"><option value="0.55">천천히</option><option value="0.75" selected>보통</option><option value="0.95">조금 빠르게</option><option value="1.15">빠르게</option></select></div><div class="easy-select-box"><div class="easy-label">전체 반복</div><select id="repeat_{player_id}" class="easy-select"><option value="1">1번</option><option value="2">2번</option><option value="3" selected>3번</option></select></div></div>
        <div id="status_{player_id}" class="easy-status"></div>
    </div>
    <script>
    (function() {{
        const root = window.parent || window;
        const cassetteItems = {cassette_json};
        const playBtn = document.getElementById("play_{player_id}");
        const pauseBtn = document.getElementById("pause_{player_id}");
        const replayBtn = document.getElementById("replay_{player_id}");
        const prevBtn = document.getElementById("prev_{player_id}");
        const nextBtn = document.getElementById("next_{player_id}");
        const stopBtn = document.getElementById("stop_{player_id}");
        const progress = document.getElementById("progress_{player_id}");
        const visualBar = document.getElementById("bar_{player_id}");
        const percentBox = document.getElementById("percent_{player_id}");
        const status = document.getElementById("status_{player_id}");
        const wordBox = document.getElementById("word_{player_id}");
        const meaningBox = document.getElementById("meaning_{player_id}");
        const countBox = document.getElementById("count_{player_id}");
        const themeBox = document.getElementById("theme_{player_id}");
        const speedSelect = document.getElementById("speed_{player_id}");
        const repeatSelect = document.getElementById("repeat_{player_id}");
        let index = 0;
        let channel = null;
        try {{ channel = new BroadcastChannel("survival_english_audio_channel"); }} catch(e) {{}}
        function getEmoji(word) {{ const m = {"I": "🙋", "you": "👉", "he": "👦", "she": "👧", "we": "👥", "they": "👥", "friend": "🤝", "teacher": "👩‍🏫", "student": "🧑‍🎓", "classmate": "👫", "family": "👨‍👩‍👧", "father": "👨", "mother": "👩", "brother": "👦", "sister": "👧", "name": "🏷️", "person": "🧍", "man": "👨", "woman": "👩", "child": "🧒", "go": "➡️", "come": "⬅️", "walk": "🚶", "run": "🏃", "sit": "🪑", "stand": "🧍", "stop": "🛑", "start": "▶️", "open": "📂", "close": "📕", "eat": "🍽️", "drink": "🥤", "sleep": "😴", "study": "📚", "read": "📖", "write": "✏️", "listen": "👂", "speak": "🗣️", "help": "🆘", "wait": "⏳", "happy": "😊", "sad": "😢", "angry": "😠", "tired": "🥱", "hungry": "😋", "thirsty": "🥤", "sick": "🤒", "okay": "👌", "fine": "🙂", "cold": "🥶", "hot": "🥵", "pain": "🤕", "headache": "🤯", "stomachache": "🤢", "fever": "🌡️", "hurt": "🩹", "good": "👍", "bad": "👎", "worried": "😟", "scared": "😨", "food": "🍽️", "water": "💧", "rice": "🍚", "bread": "🍞", "milk": "🥛", "juice": "🧃", "coffee": "☕", "tea": "🍵", "apple": "🍎", "banana": "🍌", "egg": "🥚", "meat": "🥩", "chicken": "🍗", "fish": "🐟", "breakfast": "🍳", "lunch": "🍱", "dinner": "🍽️", "snack": "🍪", "medicine": "💊", "hospital": "🏥", "home": "🏠", "school": "🏫", "classroom": "🧑‍🏫", "bathroom": "🚻", "store": "🏪", "station": "🚉", "bus": "🚌", "car": "🚗", "taxi": "🚕", "train": "🚆", "bike": "🚲", "road": "🛣️", "street": "🏙️", "here": "📍", "there": "📌", "near": "↔️", "far": "🌁", "left": "⬅️", "right": "➡️", "time": "⏰", "now": "🕒", "today": "📅", "tomorrow": "➡️📅", "yesterday": "⬅️📅", "morning": "🌅", "afternoon": "☀️", "evening": "🌆", "night": "🌙", "early": "🐓", "late": "🌃", "one": "1️⃣", "two": "2️⃣", "three": "3️⃣", "four": "4️⃣", "five": "5️⃣", "six": "6️⃣", "seven": "7️⃣", "eight": "8️⃣", "nine": "9️⃣", "ten": "🔟", "bag": "🎒", "phone": "📱", "book": "📘", "notebook": "📓", "pen": "🖊️", "pencil": "✏️", "desk": "🪑", "chair": "🪑", "door": "🚪", "window": "🪟", "key": "🔑", "money": "💵", "card": "💳", "ticket": "🎫", "clothes": "👕", "shoes": "👟", "hat": "🧢", "watch": "⌚", "cup": "☕", "bottle": "🍼", "please": "🙏", "sorry": "🙇", "excuse me": "🙋", "again": "🔁", "slowly": "🐢", "understand": "💡", "question": "❓", "problem": "⚠️", "need": "📌", "want": "✨", "know": "🧠", "say": "💬", "tell": "📣", "ask": "❔", "answer": "✅", "repeat": "🔁", "look": "👀"}; return m[word] || "🌱"; }}
        function updateDisplay(i) {{
            if (typeof i === "number") index = Math.max(0, Math.min(cassetteItems.length - 1, i));
            const item = cassetteItems[index]; if (!item) return;
            const max = Math.max(cassetteItems.length - 1, 1); const pct = Math.round((index / max) * 100);
            progress.value = index; visualBar.style.width = pct + "%"; percentBox.innerText = pct + "%"; countBox.innerText = (index + 1) + " / " + cassetteItems.length;
            themeBox.innerText = item.theme || "Theme"; wordBox.innerText = item.word + " " + getEmoji(item.word); meaningBox.innerText = item.meaning || "";
        }}
        if (channel) {{
            channel.onmessage = function(event) {{
                if (!event.data) return;
                if (event.data.type === "GLOBAL_AUDIO_WORD" && event.data.mode === "cassette") {{
                    const idx = event.data.index;
                    if (typeof idx === "number") updateDisplay(idx);
                    status.innerText = "재생 중: " + (event.data.index + 1) + " / " + event.data.total + " · 단어 " + event.data.each + "/" + event.data.eachTotal + " · 전체 반복 " + event.data.round + "/" + event.data.repeatTotal;
                    playBtn.innerText = "재생 중...";
                }}
                if (event.data.type === "GLOBAL_AUDIO_DONE") {{ status.innerText = "카세트 듣기 완료!"; playBtn.innerText = "▶️ 듣기"; }}
                if (event.data.type === "GLOBAL_AUDIO_STOPPED") {{ playBtn.innerText = "▶️ 듣기"; }}
            }};
        }}
        playBtn.addEventListener("click", function() {{
            if (!root.__survivalAudioManager) {{ status.innerText = "다시 클릭해 주세요."; return; }}
            root.__survivalAudioManager.playCassette(cassetteItems, {{ startIndex: index, rate: parseFloat(speedSelect.value || "0.75"), repeatMax: parseInt(repeatSelect.value || "1"), eachRepeat: 2, pause: 500 }});
            playBtn.innerText = "재생 중..."; status.innerText = "카세트 듣기 시작";
        }});
        pauseBtn.addEventListener("click", function() {{ if(root.__survivalAudioManager) root.__survivalAudioManager.pause(); status.innerText="잠깐 멈춤"; }});
        replayBtn.addEventListener("click", function() {{ if(root.__survivalAudioManager) root.__survivalAudioManager.speakSingle(cassetteItems[index].word, {{repeat:2, rate:parseFloat(speedSelect.value || "0.75"), pause:500}}); status.innerText="현재 단어 2번 듣기"; }});
        prevBtn.addEventListener("click", function() {{ updateDisplay(index - 1); }});
        nextBtn.addEventListener("click", function() {{ updateDisplay(index + 1); }});
        stopBtn.addEventListener("click", function() {{ if(root.__survivalAudioManager) root.__survivalAudioManager.stop(); updateDisplay(0); status.innerText="처음으로 돌아갔습니다."; }});
        progress.addEventListener("input", function() {{ updateDisplay(parseInt(progress.value)); }});
        updateDisplay(0);
    }})();
    </script>
    """, height=height)


def browser_survival_cassette_player(all_items, height=620):
    browser_easy_cassette_player(all_items, title="📼 전체 단어 카세트 듣기", intro="전체 단어를 단어만 차례대로 들을 수 있습니다. 각 단어는 2번씩 발음됩니다.", height=height)


def browser_theme_cassette_player(theme_items, theme_name, height=580):
    browser_easy_cassette_player(theme_items, title=f"📼 {{theme_name}} 단어 카세트 듣기", intro="이 테마 단어만 차례대로 들을 수 있습니다. 각 단어는 2번씩 발음됩니다.", height=height)


def show_all_cassette_tab():
    st.markdown("## 🎧 전체 단어만 카세트 듣기")
    all_items = flatten_survival_words()
    browser_survival_cassette_player(all_items, height=760)
    with st.expander("📜 전체 카세트 단어 목록 보기"):
        for item in all_items:
            st.markdown(f"""
            <div style="background:white;border:1px solid #dbeafe;border-radius:16px;padding:12px 14px;margin-bottom:8px;box-shadow:0 2px 8px rgba(0,0,0,.035);">
                <div style="font-size:18px;font-weight:900;color:#111827;">{{item['number']}}. {{item['word']}}</div>
                <div style="font-size:15px;font-weight:800;color:#374151;margin-top:4px;">단어 뜻: {{item['meaning']}}</div>
                <div style="font-size:12px;color:#94a3b8;margin-top:4px;">{{item['theme']}}</div>
            </div>
            """, unsafe_allow_html=True)


def show_cassette_player(theme_words, theme_name):
    st.markdown("### 🎧 이 테마 단어만 카세트 듣기")
    theme_items = make_theme_cassette_items(theme_words, theme_name)
    browser_theme_cassette_player(theme_items, theme_name, height=680)


all_words = []
for theme_words in word_themes.values():
    all_words.extend(theme_words)
all_meanings = [item["meaning"] for item in all_words]


def get_shuffled_options(theme_name, index, options):
    key = f"{{theme_name}}_options_{{index}}"
    if key not in st.session_state:
        shuffled = options[:]
        random.seed(f"{{theme_name}}_{{index}}")
        random.shuffle(shuffled)
        st.session_state[key] = shuffled
    return st.session_state[key]


def make_quiz_items(theme_words, theme_name):
    quiz_items = []
    for idx, item in enumerate(theme_words):
        correct = item["meaning"]
        distractors = [m for m in all_meanings if m != correct]
        random.seed(f"{{theme_name}}_{{item['word']}}_{{idx}}")
        wrong_options = random.sample(distractors, 3)
        quiz_items.append({{"word": item["word"], "answer": correct, "options": [correct] + wrong_options}})
    return quiz_items


def init_state(theme_name):
    st.session_state.setdefault(f"{{theme_name}}_submitted1", False)
    st.session_state.setdefault(f"{{theme_name}}_submitted2", False)
    st.session_state.setdefault(f"{{theme_name}}_wrong", [])


def reset_theme(theme_name):
    for key in list(st.session_state.keys()):
        if key.startswith(theme_name):
            del st.session_state[key]


def show_word_cards(theme_words, theme_name):
    st.markdown("### 🌱 핵심 단어 익히기")
    st.write("생존 회화에 꼭 필요한 단어를 듣고 익혀 보세요.")
    for idx, item in enumerate(theme_words):
        st.markdown('<div class="word-card">', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1.25, 1.05, 0.35, 1.65])
        with col1:
            st.markdown(f"""<div class="word-row"><div class="word-number">{{idx + 1}}</div><div class="word-text">{{item['word']}}</div></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='meaning-text'>{{item['meaning']}}</div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div class='emoji-text'>{{get_word_emoji(item['word'])}}</div>", unsafe_allow_html=True)
        with col4:
            audio_button("🔊 듣기", item["word"], key=f"{{theme_name}}_learn_audio_{{idx}}")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('---')
    show_cassette_player(theme_words, theme_name)


def show_quiz(theme_words, theme_name):
    init_state(theme_name)
    quiz_items = make_quiz_items(theme_words, theme_name)
    submitted1_key = f"{{theme_name}}_submitted1"
    submitted2_key = f"{{theme_name}}_submitted2"
    wrong_key = f"{{theme_name}}_wrong"
    if not st.session_state[submitted1_key]:
        st.markdown("### 🧸 1차 퀴즈")
        st.write("영어 단어를 보고 알맞은 뜻을 고르세요.")
        for i, q in enumerate(quiz_items):
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
            st.markdown(f"<div class='quiz-number'>🌟 Question {{i + 1}}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='quiz-word'>{{q['word']}}</div>", unsafe_allow_html=True)
            audio_button("🔊 발음 듣기", q["word"], key=f"{{theme_name}}_quiz_audio1_{{i}}")
            options = get_shuffled_options(theme_name, i, q["options"])
            st.radio("뜻을 고르세요.", options, key=f"{{theme_name}}_q1_{{i}}")
            st.markdown('</div>', unsafe_allow_html=True)
        if st.button("✅ 1차 제출하기", key=f"{{theme_name}}_submit1"):
            wrong = []
            for i, q in enumerate(quiz_items):
                if st.session_state.get(f"{{theme_name}}_q1_{{i}}") != q["answer"]:
                    wrong.append(i)
            st.session_state[wrong_key] = wrong
            st.session_state[submitted1_key] = True
            st.rerun()
    elif st.session_state[submitted1_key] and not st.session_state[submitted2_key]:
        wrong = st.session_state[wrong_key]
        score = len(quiz_items) - len(wrong)
        st.markdown(f"""<div class="score-box"><div class="score-title">🎉 1차 결과: {{score}} / {{len(quiz_items)}}점</div></div>""", unsafe_allow_html=True)
        if len(wrong) == 0:
            st.balloons(); st.success("🌈 완벽합니다! 이 테마의 생존 단어를 모두 잘 기억하고 있습니다.")
            if st.button("🔄 다시 풀기", key=f"{{theme_name}}_reset_all_correct"):
                reset_theme(theme_name); st.rerun()
        else:
            st.markdown(f"""<div class="wrong-box">🍊 틀린 단어 {{len(wrong)}}개를 다시 풀어 봅시다.</div>""", unsafe_allow_html=True)
            st.markdown("### 🔁 2차 퀴즈: 틀린 단어만 다시 풀기")
            for i in wrong:
                q = quiz_items[i]
                st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
                st.markdown(f"<div class='quiz-number'>🌟 Retry {{i + 1}}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='quiz-word'>{{q['word']}}</div>", unsafe_allow_html=True)
                audio_button("🔊 발음 다시 듣기", q["word"], key=f"{{theme_name}}_quiz_audio2_{{i}}")
                options = get_shuffled_options(theme_name, i, q["options"])
                st.radio("뜻을 다시 고르세요.", options, key=f"{{theme_name}}_q2_{{i}}")
                st.markdown('</div>', unsafe_allow_html=True)
            if st.button("✅ 2차 제출하기", key=f"{{theme_name}}_submit2"):
                st.session_state[submitted2_key] = True
                st.rerun()
    else:
        wrong = st.session_state[wrong_key]
        second_wrong = []
        for i in wrong:
            q = quiz_items[i]
            if st.session_state.get(f"{{theme_name}}_q2_{{i}}") != q["answer"]:
                second_wrong.append(i)
        final_score = len(quiz_items) - len(second_wrong)
        st.markdown(f"""<div class="score-box"><div class="score-title">🏆 최종 결과: {{final_score}} / {{len(quiz_items)}}점</div></div>""", unsafe_allow_html=True)
        if len(second_wrong) == 0: st.balloons(); st.success("💖 좋습니다! 틀렸던 단어까지 모두 다시 확인했습니다.")
        else: st.warning("🍊 아래 단어들은 다시 복습하면 좋습니다.")
        st.markdown("### ✅ 정답 확인")
        if len(wrong) == 0:
            st.info("틀린 문제가 없습니다.")
        else:
            for i in wrong:
                q = quiz_items[i]
                user1 = st.session_state.get(f"{{theme_name}}_q1_{{i}}")
                user2 = st.session_state.get(f"{{theme_name}}_q2_{{i}}")
                st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                st.markdown(f"### 🌱 {{q['word']}}")
                audio_button("🔊 발음 다시 듣기", q["word"], key=f"{{theme_name}}_answer_audio_{{i}}")
                st.write(f"1차 선택: {{user1}}")
                st.write(f"2차 선택: {{user2}}")
                st.success(f"정답: {{q['answer']}}")
                st.markdown('</div>', unsafe_allow_html=True)
        if st.button("🔄 다시 풀기", key=f"{{theme_name}}_reset"):
            reset_theme(theme_name); st.rerun()


tab_names = list(word_themes.keys()) + ["🎧 전체 카세트 듣기"]
tabs = st.tabs(tab_names)
for tab, theme_name in zip(tabs[:-1], word_themes.keys()):
    with tab:
        theme_words = word_themes[theme_name]
        st.markdown(f"""
        <div class="theme-header"><div class="theme-title">{{theme_name}}</div><div class="theme-desc">이 테마에는 {{len(theme_words)}}개의 생존 단어가 있습니다. 핵심 단어를 듣고 익혀 봅시다.</div></div>
        """, unsafe_allow_html=True)
        mode = st.radio("학습 모드를 선택하세요.", ["🌱 핵심 단어 익히기", "🧸 퀴즈 풀기"], key=f"{{theme_name}}_mode", horizontal=True)
        if mode == "🌱 핵심 단어 익히기": show_word_cards(theme_words, theme_name)
        else: show_quiz(theme_words, theme_name)
with tabs[-1]:
    show_all_cassette_tab()
