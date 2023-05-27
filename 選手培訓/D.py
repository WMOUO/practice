ans = 0
for _ in range(int(input())):
    n = [int(_) for _ in input().split(" ") if _]
    ans += n[0] * n[1]
print(ans)