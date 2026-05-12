
아래처럼 "작동하는 코드"에서 딱 두 군데만 바꾸세요.
전체 구조, 테마 선택, 버튼 구조는 절대 건드리지 않습니다.

============================================================
1) recognition.maxAlternatives 수정
============================================================

아래 줄을 찾으세요.

recognition.maxAlternatives = 3;

아래처럼 바꾸세요.

recognition.maxAlternatives = 10;


============================================================
2) isSmallRecognitionMistake 함수만 통째로 교체
============================================================

아래 함수 전체를 찾으세요.

function isSmallRecognitionMistake(spokenWord, answerWord) {
    ...
}

그 함수 전체를 아래 코드로 교체하세요.


function isSmallRecognitionMistake(spokenWord, answerWord) {
    if (!spokenWord || !answerWord) return false;

    const sw = normalizeText(spokenWord).replace(/\s+/g, "");
    const aw = normalizeText(answerWord).replace(/\s+/g, "");

    if (!sw || !aw) return false;
    if (sw === aw) return true;

    // 브라우저 음성 인식이 자주 다르게 받아쓰는 단어들
    const aliases = {
        "i": ["i", "eye", "hi", "ai", "a"],
        "you": ["you", "u", "yew", "yo", "ya", "your"],
        "he": ["he", "hi", "hey"],
        "she": ["she", "see", "sea", "shi", "seat"],
        "we": ["we", "wee", "wi", "me", "be"],
        "they": ["they", "day", "dey", "the", "there", "their", "that"],
        "one": ["one", "won"],
        "two": ["two", "to", "too"],
        "three": ["three", "tree", "free"],
        "four": ["four", "for"],
        "five": ["five", "fife"],
        "six": ["six", "sex", "sick"],
        "eight": ["eight", "ate"],
        "here": ["here", "hear"],
        "there": ["there", "their"],
        "right": ["right", "write", "light"],
        "wait": ["wait", "weight"],
        "know": ["know", "no"],
        "okay": ["okay", "ok", "kay"],
        "pe": ["pe", "pee", "p", "physicaleducation"],
        "wifi": ["wifi", "wi", "wifei"],
        "tshirt": ["tshirt", "teeshirt", "t shirt", "tee shirt"]
    };

    if (aliases[aw] && aliases[aw].includes(sw)) return true;

    // 완전히 다른 대명사류만 막음
    // 예: 정답이 we인데 they라고 말하면 오답
    const pronouns = ["i", "you", "he", "she", "we", "they"];
    if (pronouns.includes(aw) && pronouns.includes(sw) && aw !== sw) {
        return false;
    }

    const dist = editDistance(sw, aw);
    const sim = wordSimilarity(sw, aw);

    // 모음 길이, 강세, 인토네이션 차이를 많이 무시하기 위한 자음 중심 비교
    function soundKey(x) {
        return String(x || "")
            .replace(/tion/g, "shun")
            .replace(/sion/g, "shun")
            .replace(/th/g, "d")
            .replace(/ph/g, "f")
            .replace(/gh/g, "g")
            .replace(/ck/g, "k")
            .replace(/qu/g, "kw")
            .replace(/x/g, "ks")
            .replace(/c/g, "k")
            .replace(/q/g, "k")
            .replace(/z/g, "s")
            .replace(/v/g, "b")
            .replace(/f/g, "p")
            .replace(/r/g, "l")
            .replace(/j/g, "g")
            .replace(/w/g, "u")
            .replace(/ee/g, "i")
            .replace(/ea/g, "i")
            .replace(/ie/g, "i")
            .replace(/ei/g, "i")
            .replace(/oo/g, "u")
            .replace(/ou/g, "u")
            .replace(/ow/g, "o")
            .replace(/oa/g, "o")
            .replace(/ai/g, "e")
            .replace(/ay/g, "e")
            .replace(/[aeiouy]/g, "");
    }

    const soundSw = soundKey(sw);
    const soundAw = soundKey(aw);

    if (soundSw && soundAw && soundSw === soundAw) return true;

    // 자음 일부가 겹치면 허용
    let overlap = 0;
    if (soundSw && soundAw) {
        for (let i = 0; i < soundSw.length; i++) {
            if (soundAw.indexOf(soundSw[i]) !== -1) overlap += 1;
        }

        const base = Math.max(1, Math.min(soundSw.length, soundAw.length));
        if ((overlap / base) >= 0.35) return true;
    }

    // 작동 안정성을 위해 기준은 단순하게 유지하되, 기존보다 많이 관대하게
    if (aw.length <= 2) return dist <= 1 || sim >= 0.30;
    if (aw.length === 3) return dist <= 2 || sim >= 0.35;
    if (aw.length === 4) return dist <= 2 || sim >= 0.32;
    if (aw.length <= 6) return dist <= 3 || sim >= 0.30;
    return dist <= 4 || sim >= 0.28;
}


============================================================
중요
============================================================

normalizeText(), isCorrectSpeech(), 테마 선택 코드, 버튼 코드, checkSpeech(), startRecognition()는 건드리지 마세요.

이번 수정은 작동하는 코드에서 아래 두 부분만 바꾸는 방식입니다.

1. recognition.maxAlternatives = 3; → recognition.maxAlternatives = 10;
2. isSmallRecognitionMistake 함수만 교체

이렇게 해야 테마 선택과 마이크 버튼이 깨지지 않습니다.
