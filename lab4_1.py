def F2C(f1, f2):
    if(f1 > f2 or f1 < 32 or f2 < 32):
        print("error")
    else:
        for i in range(f1, f2+1, 2):
            c = (i-32) / 9 * 5
            print(f"{i} : %.2f"%c)
f1, f2 = map(int,input("").split(","))
F2C(f1, f2)