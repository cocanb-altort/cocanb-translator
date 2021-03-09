// very weird stuff happens

const quotesPlaceholderSymbol = "|";
const intPlaceholder = "`";
const newNoList = ["nô", "nó", "nò", "nö"];
const cocans = ["cocan", "Cocan", "cocán", "Cocán"];
const cocanPlaceholder = "&";
const minSpaceFrequency = 0.1;
const maxSpaceFrequency = 0.3;

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

function numToSuffixString(int) {
    var strList = [ , ];
    strList[0] = "å".repeat(Math.floor(int / 26));
    strList[1] = String.fromCharCode((int % 26) + 96);
    return strList.join("")
}

function cocanbiseSentence(sentence) {
    // splits into words
    var words = sentence.split(" ");

    // removes punctuation

    // converts numbers to ignore
    // var ints = [];

    // for (i = 0; i < words.length; i++) {
    //     if (words[i] - 0 != NaN) {
    //         ints.push(words[i]);
    //         words[i] = intPlaceholder;
    //     }
    // }

    // counts letters in each word
    var wordLengths = [];

    for (i = 0; i < words.length; i++) {
        if (words[i] != quotesPlaceholderSymbol) {
            wordLengths.push(words[i].length)
        }
    }

    // gets word lengths
    for (i = 0; i < wordLengths; i++) {
        wordLengths[i] = numToSuffixString(wordLengths[i])
    }

    console.log(wordLengths)

    // moves last letters
    var lastLetters = [];

    var rootArray = [];

    for (i = 0; i < words.length; i++) {
        if (words[i] != quotesPlaceholderSymbol) {
            lastLetters.push(words[i].slice(-1));
            rootArray.push(words[i].slice(0, -1));
        }
    }

    // combines root and suffix into strings
    root = rootArray.join("");

    var suffix = [];

    for (i = 0; i < words.length; i++) {
        suffix.push(lastLetters[i]);
        suffix.push(wordLengths[i]);
    }

    suffix = suffix.join("")

    console.log(root)
    console.log(suffix)

    // finds special substrings and deals with them
    for (i = 0; i < root.length; i++) {
        root.replace("no", newNoList[Math.floor(Math.random() * newNoList.length)]);

        for (i = 0; i < cocans.length; i++) {
            suffix.replace(cocans[i], cocanPlaceholder);
        }
    }

    for (i = 0; i < suffix.length; i++) {
        suffix.replace("no", newNoList[Math.floor(Math.random() * newNoList.length)]);
        
        for (i = 0; i < cocans.length; i++) {
            suffix.replace(cocans[i], cocanPlaceholder);
        }
    }

    // adds diacritics

    // combines everything
    var output = root + "non" + suffix;

    // adds spaces
    output = output.split("");

    for (i = 0; i < Math.floor(Math.random() * (maxSpaceFrequency - minSpaceFrequency) + minSpaceFrequency); i++) {
        var pos = Math.floor(Math.random * output.length)
        output = output.splice(pos, 0, " ");
    }

    output = output.join("");

    for (i = 0; i < output.length; i++) {
        output.replace("  ", " ")
    }

    // reinserts "Cocán"
    for (i = 0; i < output.length; i++) {
        output.replace(cocanPlaceholder, "Cocán");
    }

    // reinserts numbers
    // for (i = 0; i < ints.length; i++) {
    //     output.replace(intPlaceholder, ints[i]);
    // }

    return output
}

function englishToCocanb(input) {
    // separates string based on quotes
    var separatedQuotesList = input.split('"');

    // gets parts outside of quotes
    var outsideQuotes = [];
    var insideQuotes = [];

    for (i = 0; i < separatedQuotesList.length; i++) {
        if (i % 2 == 0) {
            outsideQuotes.push(separatedQuotesList[i]);
        } 
        else {
            insideQuotes.push(separatedQuotesList[i]);
        }
    }

    // joins outsideQuotes and separates it by sentences
    var stringWithPlaceholder = outsideQuotes.join(" " + quotesPlaceholderSymbol + " ");

    var stringWithPlaceholderAsList = stringWithPlaceholder.split("")
    var sentencesPunct = [];
    var sentences = [];

    for (i = 0; i < stringWithPlaceholder.length; i++) {
        if (stringWithPlaceholderAsList[i] == ".") {
            sentences.push(stringWithPlaceholderAsList.slice(0, i - 1).join(""))
            sentences = sentences.splice(0, i + 1)
            sentencesPunct.push(". ")
        }
        else if (stringWithPlaceholderAsList[i] == "?") {
            sentences.push(stringWithPlaceholderAsList.slice(0, i - 1).join(""))
            sentences = sentences.splice(0, i + 1)
            sentencesPunct.push("? ")
        }
        else if (stringWithPlaceholderAsList[i] == "!") {
            sentences.push(stringWithPlaceholderAsList.slice(0, i - 1).join(""))
            sentences = sentences.splice(0, i + 1)
            sentencesPunct.push("! ")
        }
    }

    // magic
    for (i = 0; i < sentences.length; i++) {
        sentences[i] = cocanbiseSentence(sentences[i]);
    }

    // recombines sentences
    var output = [];

    for (i = 0; i < sentences.length; i++) {
        output.push(sentences[i]);
        output.push(sentencesPunct[i]);
    }

    // cocanbises quotes
    for (i = 0; i < sentences.length; i++)

    // attaches period if it doesn't exist
    if (output.indexOf(".") == -1 && output.indexOf("?") == -1 && output.indexOf("!") == -1) {
        output = output.concat(".")
    }

    output = output.join("")

    return output;
}