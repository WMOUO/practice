z = []
a = 0
r = 0
for i in range(12):
    n = int(input())
    if i % 2 == 0:
        r += n
    if a == 3:
        print(f'{n:>3d}')
        a = 0
    else:
        print(f'{n:>3d}',end = '')
    a += 1
print(r)