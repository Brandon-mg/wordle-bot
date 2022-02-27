import json
import string
fileobj=open("freq_map.json")
wordfrq=json.load(fileobj)

yellows=[]
word_vector = [set(string.ascii_lowercase) for _ in range(5)]
for attempts in range(5):
    guess=input("enter guess:")
    clues=input("enter clues:")
    if clues=="ggggg":
        break
    for i, ch in enumerate(clues):
        if ch == "g":
            word_vector[i]={guess[i]}
        elif ch == "y":
            try:
                word_vector[i].remove(guess[i])
            except KeyError:
                pass
        elif ch=="b":
            for vector in word_vector:
                try:
                    vector.remove(guess[i])
                except KeyError:
                    pass

    def match(g,wv):
        for ch, vch in zip(g, wv):
            if ch not in vch:
                return False
        return True
    words=[word for word in wordfrq.keys() if match(word,word_vector)]
    words.sort(key=lambda frq: wordfrq[frq], reverse =True)
    print(words[:5])
