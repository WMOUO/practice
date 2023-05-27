n = [int(_) for _ in input().split(' ') if _]
for _ in range(int(input())):
    r = [int(_) for _ in input().split(' ') if _]
    if r[0] > n[0]+n[1] or r[0] < n[0]-n[1]:continue#範圍外
    if r[1] <= n[2]:#接球
        n[0] = r[0]
    else:#躲避
        if n[0] > r[0]:
            n[0] += 15
        else:
            n[0] -= 15
print(n[0])