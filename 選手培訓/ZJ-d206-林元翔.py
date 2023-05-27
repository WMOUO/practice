z = []
while True:
    try:        
        tmp = [int(_) for _ in input().split(" ") if _]
        z += tmp
    except:
        break
x = []
a = 0
b = 0
for i in z :
    if a == 0:a = i ** 2
    else:
        x.append(i)
        b += 1
        if b == a:
            a,b = 0,0
            x = list(map(str,x))
            print(' '.join(x))
            x = []
    