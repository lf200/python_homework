def findFalseCoin(coins, start, n):
    min = coins[start]
    flag = 0
    for i in range(start, n + 1):
        if coins[i] < min:
            flag = 1
            min = i
            break
        elif coins[i] > min:
            flag = 1
            min = start
            break
    if flag == 1:
        print("Fake coin:{}".format(min))
    else:
        print("Fake coin is not found")

coins = list(input().split(','))
coins = [int(i) for i in coins]
findFalseCoin(coins, 0, len(coins)-1)

