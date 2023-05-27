while True:
    ans = 0
    r = int(input())
    if r == 0:break
    for i in range(1,r+1):
        ans += i ** 2
    print(ans)