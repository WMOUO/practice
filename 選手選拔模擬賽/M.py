while True:
    try:
        a = input().strip().split(' ')
        b = input().strip().split(' ')
        z = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
        for i in range(1,len(a)+1):
            for u in range(1,len(b)+1):
                if a[i-1] == b[u-1]:
                    z[i][u] = z[i-1][u-1] + 1
                else:
                    z[i][u] = max(z[i-1][u],z[i][u-1])
        print(z[-1][-1])
    except:
        break
#A B A D E
#B A E
#A A A
#B B
#12 5 3 4
#4 12 3 5