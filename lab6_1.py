count = 0


def hnt(begin, wend, oth, upn):
    global count
    if upn == 1:
        count = 1 + count
        print("[STEP%4d] " % count, end='')
        print("%c->" % begin, end='')
        print(wend)

    else:
        hnt(begin, oth, wend, upn - 1)
        hnt(begin, wend, oth, 1)
        hnt(oth, wend, begin, upn - 1)


n = int(input())
hnt('A', 'C', 'B', n)

