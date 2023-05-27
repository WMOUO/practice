t = int(input())
a = [int(_) for _ in input().split(' ') if _]
a.sort()

b,c = -1,-1
for i in a:
    if i < 60 and i > b:b = i
    elif i >= 60:
        c = i
        break
a = map(str,a)
print(' '.join(a))
if b == -1:print("best case")
else:print(b)
if c == -1:print("worst case")
else:print(c)