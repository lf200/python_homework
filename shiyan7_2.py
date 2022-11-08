w1 = open('src.txt', 'r')
w2 = open('dest.txt', 'w')
for line in w1:
    w2.write(line.lower())

w1.close()
w2.close()