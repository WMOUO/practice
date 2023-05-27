# 1
a, b = input().split()
print(int(a)+int(b))
# 2
a, b = map(int, input().split())
print(a+b)
# 3
n = [int(_) for _ in input().split() if _]
print(sum(n))
# 4
print(sum([int(_) for _ in input().split() if _]))

###
print(sum(map(int, input().split())))
