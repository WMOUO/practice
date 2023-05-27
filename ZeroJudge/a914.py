z = []
for _ in range(int(input())):
    z.append([int(_) for _ in input().split(' ') if _])
for i in sorted(z):
    i = map(str,i)
    print(' '.join(i))