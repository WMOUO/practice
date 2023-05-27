for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    ans = 0
    for i in n[1:]:
        if n[0] < i:
            ans += 1
    print(ans)