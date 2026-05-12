# 아래 내용은 전체 코드가 아닙니다.
# 기존 코드에서 딱 2곳만 바꾸세요.
#
# 1) recognition.maxAlternatives = 3; 을 아래처럼 변경
# recognition.maxAlternatives = 10;
#
# 2) 기존 isSmallRecognitionMistake 함수 전체를 아래 함수로 교체


function isSmallRecognitionMistake(spokenWord, answerWord) {
    if (!spokenWord || !answerWord) return false;

    const sw = normalizeText(spokenWord).replace(/\s+/g, "");
    const aw = normalizeText(answerWord).replace(/\s+/g, "");

    if (!sw || !aw) return false;
    if (sw === aw) return true;

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

    const pronouns = ["i", "you", "he", "she", "we", "they"];
    if (pronouns.includes(aw) && pronouns.includes(sw) && aw !== sw) {
        return false;
    }

    const dist = editDistance(sw, aw);
    const sim = wordSimilarity(sw, aw);

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

    let overlap = 0;
    if (soundSw && soundAw) {
        for (let i = 0; i < soundSw.length; i++) {
            if (soundAw.indexOf(soundSw[i]) !== -1) overlap += 1;
        }

        const base = Math.max(1, Math.min(soundSw.length, soundAw.length));
        if ((overlap / base) >= 0.35) return true;
    }

    if (aw.length <= 2) return dist <= 1 || sim >= 0.30;
    if (aw.length === 3) return dist <= 2 || sim >= 0.35;
    if (aw.length === 4) return dist <= 2 || sim >= 0.32;
    if (aw.length <= 6) return dist <= 3 || sim >= 0.30;
    return dist <= 4 || sim >= 0.28;
}
