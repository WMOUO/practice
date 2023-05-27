for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    ans = 0
    for i in range(min(n[0],n[1]),max(n[0],n[1])+1):
        if str(n[2]) in str(i):ans += 1
    print(ans)