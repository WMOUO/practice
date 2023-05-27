from bisect import bisect_left
n = [int(_) for _ in input().split(' ') if _]
z = []
for i in n:
    a = bisect_left(z,i)
    if a == len(z):
        z.append(i)
    else:
        z[a] = i
print(len(z))