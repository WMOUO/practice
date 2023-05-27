n = 1
while True:
    a = int(input())
    if a < 0:break
    r = [int(_) for _ in input().split(' ') if _]
    z = [int(_) for _ in input().split(' ') if _]
    r = [a]+r
    print(f'Case {n}:')
    for i in range(12):
        if r[i] >= z[i]:
            print('No problem! :D')
            r[i] -= z[i]
        else:print('No problem. :(')
        r[i+1] += r[i]
    n += 1