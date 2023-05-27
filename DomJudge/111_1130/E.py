from collections import Counter
a = int(input())
n = Counter([int(_) for _ in input().split(' ') if _])
n = sorted(list(n.items()))
for i in n:
    print(i[0],i[1])