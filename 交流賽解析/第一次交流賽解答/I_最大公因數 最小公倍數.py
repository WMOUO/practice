# 1
from math import gcd, lcm
from math import gcd
for _ in range(int(input())):
    a, b = map(int, input().split())
    i = min(a, b)
    ans = [0, 0]
    while True:
        if a % i == 0 and b % i == 0:
            ans[0] = i
            break
        i -= 1
    i = max(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            ans[1] = i
            break
        i += 1
    print(ans[0], ans[1])
# 2
for _ in range(int(input())):
    n = [int(_) for _ in input().split() if _]
    print(gcd(n[0], n[1]), n[0]*n[1]//gcd(n[0], n[1]))

###
for _ in range(int(input().split())):
    a, b = map(int, input().split())
    print(gcd(a, b), lcm(a, b))
