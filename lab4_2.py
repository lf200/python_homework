fn = 1
fm = 1
fmn = 1
# 求每个数
def C(m, n):
    fn = 1
    fm = 1
    fmn = 1
    for i in range(1, n):
        fn *= i
    for i in range(1, m):
        fm *= i
    for i in range(1, n - m + 1):
        fmn *= i
    c = int(fn / (fm * fmn))
    return c
# 循环输出
n = int(input(""))
list1 = C(int(n / 2), n)
x = (len(str(list1)))
for i in range(1, n + 1):
    for o in range(1, n + 1 - i):
        print(" " * x, end="")
    s = ""
    for j in range(1, i + 1):
        s += " " * (x - len(str(C(j, i)))) + str(C(j, i)) + " " * x
    print(s)

