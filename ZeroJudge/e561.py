for _ in range(int(input())):
    a = int(input())
    n = [int(_) for _ in input().split(' ') if _]
    ans = 0
    for i in range(a):
        for u in range(a-i-1):
            if n[u] > n[u+1]:
                n[u],n[u+1] = n[u+1],n[u]
                ans += 1
    print(f'Optimal train swapping takes {ans} swaps.')