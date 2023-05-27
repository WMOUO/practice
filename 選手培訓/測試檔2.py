a = eval(input())
n = [int(_) for _ in input().split(' ') if _]
if a == 1:ans = n[0]
else:
    ans = 0
    while len(n) >= 2:
        ans += sum(n)
        n = n[:-1]
print(ans)