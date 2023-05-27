for _ in range(1,int(input())+1):
    a = int(input())
    n = input()
    r,ans = 0,0
    while r < a:
        if n[r]=='.':
            ans += 1
            r += 3
        else:r += 1
    print(f'Case {_}: {ans}')