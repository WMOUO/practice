for _ in range(int(input())):
    n = int(input())
    ans = []
    i = 9
    while i >= 2:
        if n % i == 0:
            n //= i
            ans.append(i)
        else:i -= 1
    if ans == [] or len(str(n)) >= 2:print(-1)
    else:
        ans.sort()
        ans = list(map(str,ans))
        print(''.join(ans))