def teny_last_words():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().splitlines()
    for i in range(-10,0):
        print(words[i])

def pything_words():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().splitlines()
    for word in words:
        if (len(word) >= 3 and word[0:3] == "pyt"):
            print(word)

teny_last_words()
print()
pything_words()
