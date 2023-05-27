z = {}
o = {}
t = [[0]*5 for _ in range(5)]
r = []
a = 0
for _ in range(5):
    b = 0
    n = [int(_) for _ in input().split(' ') if _]
    r += n
    for i in n:
        z[i] = a,b
        b += 1
    a += 1
while True:
    n = int(input())
    if n == -1:break
    t[z[n][0]][z[n][1]] = 1
for i in range(5):#橫
    if sum(t[i]) == 4:
        w = t[i].index(0)
        if o.get(o[t[i][w]],"None") == "None":o[t[i][w]] = 1
        else:o[t[i][w]] += 1
for i in range(5):#直
    if sum(t[0][i],t[1][i],t[2][i],t[3][i],t[4][i]) == 4:
        w = t[i].index(0)
        if o.get(o[t[i][w]],"None") == "None":o[t[i][w]] = 1
        else:o[t[i][w]] += 1
a,b = 0,0#左上到右下

a,b = 5,0#左下到右上