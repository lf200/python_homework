f = open("in162.txt", 'r')
x = open("out162.txt", 'w')
sum = 0
for i in list(map(float, f.readline().split(" "))):
    sum +=i
x.write("%.2f" %(sum * 0.454))


