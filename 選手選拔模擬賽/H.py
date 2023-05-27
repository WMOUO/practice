n = [int(_) for _ in input().split(' ')]
z = [str(n[0])]
t = True
while True:
    if n[0] == 1 or n[0] == 0:
        break
    if n[0] % n[1] != 0:
        t = False
    n[0] //= n[1]
    z.append(str(n[0]))
if t == True:
    print('Perfect!')
else:
    print(' '.join(z))