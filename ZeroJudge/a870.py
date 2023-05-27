z = []
while True:
    n = input().strip().split(' ')
    if n[0] == 'SHOW':
        break
    if n[0] == 'ADD':
        z.append(n[1])
    elif n[0] == "wINSERT"[1:]:
        z.insert(z.index(n[2]),n[1])
    else:
        z.remove(n[1])
print(' '.join(z))