def big(m):
    a = 0
    b = 1#每次都+1，到2時a+1
    while b != len(m):
        z = "True"
        if int(m[b]) < int(m[a]) :
            z = "F"
            break
        else:
            if b % 2 == 0:a += 1
            b += 1
    if z == "F":return "F"
    else:return "H"
def lit(m):
    a = 0
    b = 1
    while b != len(m):
        z = "True"
        if int(m[b]) > int(m[a]) :
            z="F"
            break
        else:
            if b % 2 == 0:a += 1
            b += 1
    if z == "F":return "F"
    else:return "H"
def bst(m):
    a = 0
    b = 1
    while b != len(m):
        z = "True"
        if b % 2 != 0 :#奇數區小於
            if int(m[a]) < int(m[b]):
                z = "F"
                break
        elif b % 2 == 0:#偶數區大於
            if int(m[a]) > int(m[b]):
                z = "F"
                break
        if b % 2 == 0:a += 1
        b += 1
    if z == "F":return "F"
    else:return "B"
u = int(input())
for _ in range(u):
    n = input().split(',')
    if len(n) == 0:break
    if n[0] < n[1]:p = big(n)
    elif n[0] > n[1]:p = lit(n)
    if p == "F":
        p = bst(n)
    print(p)