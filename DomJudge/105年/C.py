for _ in range(int(input())):
    n = [_ for _ in input().split('/')]
    ans = ''
    n[0] = n[0].split('.')
    n[1] = n[1].split('.')
    for i in range(4):
        ans += str(int(n[0][i]) & int(n[1][i]))+'.'
    print(ans[:-1])