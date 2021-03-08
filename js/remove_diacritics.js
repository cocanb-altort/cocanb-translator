const diacritics = {
    "a": ["a", "à", "á", "â", "ä"],
    "e": ["e", "è", "é", "ê"],
    "i": ["i", "ì", "í", "î"],
    "o": ["o", "ò", "ó", "ô", "ö"],
    "u": ["u", "ù", "ú", "û", "ü"],
    "y": ["y", "ý"],
    "g": ["g", "ğ"],
    "c": ["c", "č", "ć"],
    "s": ["s", "š", "ś"],
    "z": ["z", "ž", "ź"],
    "n": ["n", "ň"],
    "r": ["r", "ř"],
    "l": ["l", "ł"],
    "d": ["d", "đ"]
}

function removeDiacritics(input) {
    var array = input.split("");
    for (i = 0; i < array.length; i++) {
        for (char in diacritics) {
            if (array[i] in diacritics[char]) {
                array[i] = char;
            }
        }
    }

    var output = array.join("");
    return output;
}

console.log(removeDiacritics("á"))