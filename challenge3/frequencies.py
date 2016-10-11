import string

#most common letters (single)
common_letters = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U']

# most common double letters
common_doubles = ["ss", "ee", "tt", "ff", "ll", "mm", "oo"]

# most common single most_common_words
common_singles = ['a', 'I']

# most common pairs of letters that aren't necessarily words and that are not both the same
common_pairs = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 'en', 'es', 'of', 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've']

# most common two letter words
common_pair_words = ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am']

# most common triples of letters that aren't words
trigrams = ['the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men']

# most frequent initial letters in a word
common_initials = ['T', 'O', 'A', 'W', 'B', 'C', 'D', 'S', 'F', 'M', 'R', 'H', 'I', 'Y', 'E', 'G', 'L', 'N', 'P', 'U', 'J', 'K']

def score(string):
    score = 0
    words = string.split()
    
    for word in words:
        if word[0] in common_initials:
            score += 2
        for double in common_doubles:
            if double in word:
                score +=2
        for pair in common_pairs:
            if pair in word:
                score +=2
        for pair_word in common_pair_words:
            if pair_word in word:
                score +=2
        for trigram in trigrams:
            if trigram in word:
                score +=2
    return score
