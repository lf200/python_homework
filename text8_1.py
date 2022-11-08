import numpy as np
# n,m=map(int,input("").split())
#
# array=np.zeros([1,n],dtype=np.float)
# array[0][m-1]=1
# print(array)
def main():
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # x = len(a)
    # n, m = map(int, input("").split(" "))
    # a = np.array(a)
    # if n * m == x:
    #     o = np.zeros([n, m],dtype=int)
    #     for i in range(n*m):
    #        o[i//m][i%m] = a[i]
    #     print(o)
    # else:
    #     print("NO")
    arr = input("")
    a = [float(x) for x in arr.split()]
    a = np.array(a)
    a = np.sort(a)
    # a = np.flipud(a)
    print(a)

if __name__ == '__main__':
    main()



