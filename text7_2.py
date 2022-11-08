n = int(input())
a = []
b = [0]*n
for j in range(n):
    a.append(b[:])
s = n*n#魔方阵最大的数值
c = 1#放入数组的值
x , y = 0 , 0
while c <= s:
    for i in range(n):#向右
        a[y][x] = c
        c += 1
        x += 1
    x -= 1
    n -= 1#经过第一个for循环之后少掉了一行
    y += 1
    for r in range(n):#向下
        a[y][x] = c
        c += 1
        y += 1
    y -= 1
    x -= 1#经过第二个循环少掉了一列
    for l in range(n):#向左
        a[y][x] = c
        x -= 1
        c += 1
    x += 1
    n -= 1#经过第三个循环减少了一行
    y -= 1
    for k in range(n):#向上
        a[y][x] = c
        y -= 1
        c += 1
    y += 1
    x += 1
with open("file.out", "w") as file:
    for p in a:
        for f in p:
            file.write("%5d"%f)
        file.write("\n")
