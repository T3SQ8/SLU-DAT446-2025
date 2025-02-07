

document = [  
            '"Authorities found 23 cans of spray cheese, 4 inflatable pools,',  
            '75 rubber chickens painted gold, and nearly 600 pounds of expired',  
            'marshmallow fluff stacked in the basement,"',  
            'reported the detective in a press conference Tuesday.'  
]

repetitive_sentence = [
    "clean", "water", "is", "essential", "for", "health", "because",
    "it", "provides", "drinkable", "water", "that", "is", "essential",
    "for", "life", "and", "maintains", "environmental", "balance", "and",
    "clean", "water", "is", "essential", "for", "life"
]



stopwords = ["of", "from", "the", "is", "this", "and", "in", "a", "for"]


def tokenize(document):
    words = []
    for sentence in document:
        i = 0
        start = None
        while i < len(sentence):
            char = sentence[i]
            is_valid = char.isalpha() or char.isdigit()
            if is_valid and start is None:
                    start = i
            elif not is_valid and start is not None:
                words.append(sentence[start:i])
                start = None
            i += 1
        if start:
                words.append(sentence[start:i])

    return words


def list_top_words(words, exclude, nr_show):
    occurrences = {}
    for word in words:
        if word not in exclude:
            count = occurrences.get(word, 0)
            count += 1
            occurrences[word] = count
    s = sorted(occurrences.items(), key=lambda item: -item[1])
    s = s[0:nr_show]
    return s


# print(tokenize(document))

print(list_top_words(repetitive_sentence, stopwords, 3))
