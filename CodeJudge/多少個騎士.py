n = [int(_) for _ in input().split(' ')]
a = max(n)
b = min(n)
if b == 1:
    print(a)
elif b == 2:
    if a % 4 > 2 :
        print(4 * (a // 4) + 4)
    else:
        print(4 * (a // 4) + 2 * (a % 4))
else:
    print((a*b+1)//2)