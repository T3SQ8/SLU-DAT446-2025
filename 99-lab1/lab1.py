
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
    for sentence in document:
        while i < len(sentence):
            pass



def list_top_words(words, exclude, nr_show):
    pass
    # HINT https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html
    # HINT https://docs.python.org/3/library/functions.html#sorted


print(tokenize(document))
print(list_top_words(repetitive_sentence, stopwords, 3))
