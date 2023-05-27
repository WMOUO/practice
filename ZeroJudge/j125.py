from queue import PriorityQueue
z = []
a = int(input())
for _ in range(a):
    z.append([int(_) for _ in input().split(' ') if _])
w = [[0, 0]]
r = [[[0, 0] for _ in range(a)] for _ in range(a)]
r[0][0] = [-1, 1]
while len(w) != 0:
    h = []
    for i in w:
        if i[0] != 0:  # 上
            if r[i[0]-1][i[1]][1] == 0 or max(r[i[0]][i[1]][0], abs(z[i[0]-1][i[1]]-z[i[0]][i[1]])) < r[i[0]-1][i[1]][0]:
                r[i[0]-1][i[1]] = [max(r[i[0]][i[1]][0], abs(z[i[0]-1]
                                       [i[1]]-z[i[0]][i[1]])), r[i[0]][i[1]][1]+1]
                if [i[0]-1, i[1]] not in h:
                    h.append([i[0]-1, i[1]])
        if i[0] != a-1:  # 下
            if r[i[0]+1][i[1]][1] == 0 or max(r[i[0]][i[1]][0], abs(z[i[0]+1][i[1]]-z[i[0]][i[1]])) < r[i[0]+1][i[1]][0]:
                r[i[0]+1][i[1]] = [max(r[i[0]][i[1]][0], abs(z[i[0]+1]
                                       [i[1]]-z[i[0]][i[1]])), r[i[0]][i[1]][1]+1]
                if [i[0]+1, i[1]] not in h:
                    h.append([i[0]+1, i[1]])
        if i[1] != 0:  # 左
            if r[i[0]][i[1]-1][1] == 0 or max(r[i[0]][i[1]][0], abs(z[i[0]][i[1]-1]-z[i[0]][i[1]])) < r[i[0]][i[1]-1][0]:
                r[i[0]][i[1]-1] = [max(r[i[0]][i[1]][0], abs(z[i[0]]
                                       [i[1]-1]-z[i[0]][i[1]])), r[i[0]][i[1]][1]+1]
                if [i[0], i[1]-1] not in h:
                    h.append([i[0], i[1]-1])
        if i[1] != a-1:  # 右
            if r[i[0]][i[1]+1][1] == 0 or max(r[i[0]][i[1]][0], abs(z[i[0]][i[1]+1]-z[i[0]][i[1]])) < r[i[0]][i[1]+1][0]:
                r[i[0]][i[1]+1] = [max(r[i[0]][i[1]][0], abs(z[i[0]]
                                       [i[1]+1]-z[i[0]][i[1]])), r[i[0]][i[1]][1]+1]
                if [i[0], i[1]+1] not in h:
                    h.append([i[0], i[1]+1])
    w = h
print(r[-1][-1][0])
print(r[-1][-1][1]-1)