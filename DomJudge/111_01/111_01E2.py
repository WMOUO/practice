for _ in range(int(input())):
    a = int(input())
    b = int(input())
    z = []
    for _ in range(a):
        z.append([int(_) for _ in input().split(' ') if _])
    r = [[None for _ in range(b)] for _ in range(a)]
    r[0][0] = z[0][0]
    w = [[0,0]]
    while True:
        h = []
        for i in w:
            if i[1] > 0 :
                if  r[i[0]][i[1]-1] == None or r[i[0]][i[1]] + z[i[0]][i[1]-1] < r[i[0]][i[1]-1]:
                    r[i[0]][i[1]-1] = r[i[0]][i[1]] + z[i[0]][i[1]-1]
                    if [i[0],i[1]-1] not in h:
                        h.append([i[0],i[1]-1])
            if i[1] < b-1 :
                if r[i[0]][i[1]+1] == None or r[i[0]][i[1]] + z[i[0]][i[1]+1] < r[i[0]][i[1]+1]:
                    r[i[0]][i[1]+1] = r[i[0]][i[1]] + z[i[0]][i[1]+1]
                    if [i[0],i[1]+1] not in h:
                        h.append([i[0],i[1]+1])
            if i[0] < a-1 :
                if r[i[0]+1][i[1]] == None or r[i[0]][i[1]] + z[i[0]+1][i[1]] < r[i[0]+1][i[1]]:
                    r[i[0]+1][i[1]] = r[i[0]][i[1]] + z[i[0]+1][i[1]]
                    if [i[0]+1,i[1]] not in h:
                        h.append([i[0]+1,i[1]])
            if i[0] > 0 :
                if r[i[0]-1][i[1]] == None or r[i[0]][i[1]] + z[i[0]-1][i[1]] < r[i[0]-1][i[1]]:
                    r[i[0]-1][i[1]] = r[i[0]][i[1]] + z[i[0]-1][i[1]]
                    if [i[0]-1,i[1]] not in h:
                        h.append([i[0]-1,i[1]])
        if len(h) == 0:
            break
        else:
            w = h
    print(r[-1][-1])
'''
2
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5

3
1
1
9
2
2
0 0
0 0
5
6
0 9 9 0 0 0
0 9 0 0 9 0
0 9 0 9 9 0
0 0 0 9 9 0
9 9 9 9 9 0

'''