from bisect import bisect_left,bisect_right
z = []
for i in range(1,1001):
    z.append(i*i)
while True:
    n = [int(_) for _ in input().split(' ') if _]
    if n[0] == n[1] == 0:
        break
    print(bisect_right(z,n[1])-bisect_left(z,n[0]))