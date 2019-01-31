# Total number of characters in ASCII table
POSSIBLE_KEYS = [chr(i) for i in range(0, 256)]

# Most common letters (single)
LETTER_FREQUENCIES = {
    'A':  8.55,
    'B':  1.60,
    'C':  3.16,
    'D':  3.87,
    'E': 12.10,
    'F':  2.18,
    'G':  2.09,
    'H':  4.96,
    'I':  7.33,
    'J':  0.22,
    'K':  0.81,
    'L':  4.21,
    'M':  2.53,
    'N':  7.17,
    'O':  7.47,
    'P':  2.07,
    'Q':  0.10,
    'R':  6.33,
    'S':  6.73,
    'T':  8.94,
    'U':  2.68,
    'V': 1.06,
    'W':  1.83,
    'X':  0.19,
    'Y':  1.72,
    'Z':  0.11
}

# Most common double letters
COMMON_DOUBLES = ["ss", "ee", "tt", "ff", "ll", "mm", "oo", ]

# Most common single words
COMMON_SINGLES = ['a', 'I', ]

# Most common pairs of letters
COMMON_PAIRS = [
    'th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 'en',
    'es', 'of', 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 'le', 'is',
    'ou', 'ar', 'as', 'de', 'rt', 've',
]

# Most common two letter words
COMMON_PAIR_WORDS = [
    'of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by',
    'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am',
]

# Most common triples of letters
TRIGRAMS = [
    'the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce',
    'edt', 'tis', 'oft', 'sth', 'men',
]

# Most frequent initial letters in a word
COMMON_INITIALS = [
    'T', 'O', 'A', 'W', 'B', 'C', 'D', 'S', 'F', 'M', 'R', 'H', 'I', 'Y', 'E',
    'G', 'L', 'N', 'P', 'U', 'J', 'K',
]


def score(result):
    """Score each decrypted text."""
    score = 0
    # Some bytes are spaces, when joined we can delimit with those spaces
    words = result.split()

    for word in words:
        for letter in LETTER_FREQUENCIES:
            if letter.lower() in word.lower():
                score += LETTER_FREQUENCIES[letter]

    for word in words:
        for letter in LETTER_FREQUENCIES:
            if letter.lower() in word:
                score += LETTER_FREQUENCIES[letter]
        if word[:1] in COMMON_INITIALS:
            score += 1
        for double in COMMON_DOUBLES:
            if double in word:
                score += 1
        for pair in COMMON_PAIRS:
            if pair in word:
                score += 1
        for pair_word in COMMON_PAIR_WORDS:
            if pair_word in word:
                score += 1
        for trigram in TRIGRAMS:
            if trigram in word:
                score += 1
    return score


# examine the frequency of each xor result to find best scoring match
def find_match(results):
    """Get the text that scores highest."""
    highest_score = 0

    for i, result in enumerate(results):
        curr_score = score(result)

        if curr_score > highest_score:
            highest_score = curr_score
            key = i
            plaintext = result
    return (highest_score, key, plaintext)
