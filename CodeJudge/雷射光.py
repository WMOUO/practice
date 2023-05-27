a = int(input())
w,e = 64+a,49+a-1
b = int(input())
c = [ord(_) for _ in ' '.join(input()).split(' ') if _]
r = ''
for _ in range(b):
    n = [ord(_) for _ in ' '.join(input()).split(' ') if _]
    if c[0] not in n and c[1] not in n:
        r += "S"
    else:
        if c[0] in n:
            if c[0]-1 not in n and c[0]-1 >= 65:
                c[0] -= 1
                r += 'L'
            else:
                c[0] += 1
                r += 'R'
        if c[1] in n:#上下
            if c[1]-1 not in n and c[1]-1 >= 49:#上
                c[1] -= 1
                r += "U"
            else:
                c[1] += 1
                r += "D"
print(r)