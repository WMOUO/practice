m = int(input())
for _ in range(m):
    n = [a for a in input().split(" ") if a]
    n = list(map(int,n))
    z = [[1 for i in range(n[1]+1)] for u in range(n[0]+1)]
    for x in range(2,n[0]+1):
        for y in range(2,n[1]+1):
            z[x][y] = z[x-1][y]+z[x][y-1]
    print(z[n[0]][n[1]])