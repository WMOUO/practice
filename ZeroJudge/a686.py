for i in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    if n[0] > n[1] and n[1] <= n[2]:print("Poor Snail")
    else:
        n[0] -= n[1]
        a = 1
        if n[0] >= 1:
            a += (n[0] // (n[1]- n[2]))
            if n[0] % (n[1]- n[2]) != 0:a += 1
        print(a)