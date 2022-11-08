n = int(input())
f = open("hamlet.txt", "r")
txt = f.read()
txt = txt.lower()
for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(i, " ")
words = txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0)+1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(n):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))
f.close()

