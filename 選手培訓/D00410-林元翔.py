c = int(input())
for _ in range(c):
    z = 0
    n = input()
    if len(n) == 0 :break
    for i in range(15,0,-2):
        m = int(n[i])
        z += m
    for i in range(14,-1,-2):
        m = int(n[i]) * 2
        if m > 9 :m = m - 9
        z += m
    if z % 10 == 0 :
        print("T")
    else :
        print("F")