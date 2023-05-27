a = int(input())
z = []
r = []
for _ in range(a):
    z.append([_ for _ in ' '.join(input().split(' ')) if _])
r.append([int(_) for _ in input().split(' ') if _])
while len(r) != 0:
    t = []
    for i in r:
        z[i[0]][i[1]] = '+'#上
        if i[0]-1 < 0:continue
        else:
            if z[i[0]-1][i[1]] == "-" and [i[0]-1,i[1]] not in t and [i[0]-1,i[1]] not in r:
                t.append([i[0]-1,i[1]])
        if i[0]+1 > a:continue#下
        else:
            if z[i[0]+1][i[1]] == "-" and [i[0]+1,i[1]] not in t and [i[0]+1,i[1]] not in r:
                t.append([i[0]+1,i[1]])
        if i[1]-1 < 0:continue#左
        else:
            if z[i[0]][i[1]-1] == "-" and [i[0],i[1]-1] not in t and [i[0],i[1]-1] not in r:
                t.append([i[0],i[1]-1])
        if i[1]+1 > a:continue#右
        else:
            if z[i[0]][i[1]+1] == "-" and [i[0],i[1]+1] not in t and [i[0],i[1]+1] not in r:
                t.append([i[0],i[1]+1])
        r = t
for i in z:
    print(''.join(i))