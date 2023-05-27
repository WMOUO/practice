n = [int(_) for _ in input().split(' ')]
a = 1
b = 1
while True:
    if n[0] // a < n[2]:
        a -= 1
        break
    a += 1
while True:
    if n[1] // b < n[3]:
        b -= 1
        break
    b += 1
print(round(n[0]/a,3),round(n[1]/b,3))