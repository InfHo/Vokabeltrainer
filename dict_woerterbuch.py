

words = {
        "have":"haben",
        "you":["Du", "du", "Sie"],
        "watch":"schauen"
    }

for word in words:
    print(word, words[word])


def vokabeltrainer():
    print("Was ist")
    print(words["you"])
    print("auf deutsch?")



vokabeltrainer()
