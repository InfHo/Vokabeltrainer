

words = {
        "have":"haben",
        "you":["Du", "du", "Sie"],
        "watch":"schauen",
        "go":"gehen"
    }

for word in words:
    print(word, words[word])

import random

words_list = list(words.values())



##z = random.randint(



##x = random.choice(list(words.values()))



def wortfunktion(words):
    y = random.choice(list(words.keys()))

    print(y, ">>>>", words[y])
    
