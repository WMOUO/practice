import math
while True:
    try:
        n = [int(n) for n in input().split(" ") if n]
        if len(n) == 0:break
        a=((n[0]-1)*(-1)*n[0])-(2*n[1])
        a = int((-1) + math.ceil((1-4*1*a)**0.5)/2)
        print(a+1)
    except:
        break