n = sorted([int(_) for _ in input().split(' ') if _])
print(' '.join(map(str,n)))
if n[0]+n[1] <= n[2]:
    print('No')
else:
    if n[0]**2+n[1]**2 < n[2]**2:
        print('Obtuse')
    elif n[0]**2+n[1]**2 == n[2]**2:
        print('Right')
    else:
        print('Acute')