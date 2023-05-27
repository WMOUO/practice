while True:
    try:
        a,b = map(int,input().split(' '))
        z = []
        for _ in range(a):
            z.append([0]+[int(_) for _ in input().split(" ") if _])
        z = [[0]*len(z[0])] + z
        for i in range(1,len(z)):
            for u in range(1,len(z[i])):
                z[i][u] = z[i][u] + z[i-1][u] + z[i][u-1] - z[i-1][u-1]
        for _ in range(b):
            n = [int(_) for _ in input().split(" ") if _]
            print(z[n[2]][n[3]] - z[n[0]-1][n[3]] - z[n[2]][n[1]-1] + z[n[0]-1][n[1]-1])
    except:
        break
#1 2 3 4 5
#6 7 8 9 10
#11 12 13 14 15
#16 17 18 19 20
#21 22 23 24 25