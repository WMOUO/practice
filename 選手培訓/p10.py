z = []
n = [int(_) for _ in input().split(' ') if _]
for _ in range(3):
    a = n.pop(0)
    b = n.pop(0)
    z.append([a,b])
z.sort()
a = (z[1][1]-z[0][1])
b = (z[1][0]-z[0][0])
c = (z[2][1]-z[1][1])
d = (z[2][0]-z[1][0])
if a / b == c / d :print("LINE")
else:print('TRIANGLE')