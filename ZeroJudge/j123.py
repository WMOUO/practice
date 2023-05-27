a = [int(_) for _ in input().split(' ') if _]
z = [[0 for _ in range(a[1])] for _ in range(a[0])]
ans = a[0]*a[1]
a[0] -= 1
a[1] -= 1
w = 0
for _ in range(a[2]) :
    n = [_ for _ in input().split(' ') if _]
    n[1] = int(n[1])
    t = False
    if n[0] == 'A':
        r = a[1]
        while True:
            if r == -1:
                break
            if z[n[1]][r] == z[n[1]+1][r] == z[n[1]+2][r] == z[n[1]+3][r] == 0:
                r -= 1
                t = True
            else:
                break
        if t == True:
            r += 1
            z[n[1]][r],z[n[1]+1][r],z[n[1]+2][r],z[n[1]+3][r] = 1,1,1,1
            ans -= 4
        else:
            w += 1
    elif n[0] == 'B':
        r = a[1]-2
        while True:
            if r == -1:
                break
            if z[n[1]][r] == z[n[1]][r+1] == z[n[1]][r+2] == 0:
                r -= 1
                t = True
            else:
                break
        if t == True:
            r += 1
            z[n[1]][r],z[n[1]][r+1],z[n[1]][r+2] = 1,1,1
            ans -= 3
        else:
            w += 1
    elif n[0] == 'C':
        r = a[1]-1
        while True:
            if r == -1:
                break
            if z[n[1]][r] == z[n[1]][r+1] == z[n[1]+1][r] == z[n[1]+1][r+1] == 0:
                r -= 1
                t = True
            else:
                break
        if t == True:
            r += 1
            z[n[1]][r],z[n[1]][r+1],z[n[1]+1][r],z[n[1]+1][r+1] = 1,1,1,1
            ans -= 4
        else:
            w += 1
    elif n[0] == 'D':
        r = a[1]-2
        while True:
            if r == -1:
                break
            if z[n[1]+1][r] == z[n[1]+1][r+1] == z[n[1]+1][r+2] == z[n[1]][r+2] == 0:
                r -= 1
                t = True
            else:
                break
        if t == True:
            r += 1
            z[n[1]+1][r],z[n[1]+1][r+1],z[n[1]+1][r+2],z[n[1]][r+2] = 1,1,1,1
            ans -= 4
        else:
            w += 1
    else:
        r = a[1]-1
        while True:
            if r == -1:
                break
            if z[n[1]][r+1] == z[n[1]+1][r] == z[n[1]+1][r+1] == z[n[1]+2][r] == z[n[1]+2][r+1] == 0:
                r -= 1
                t = True
            else:
                break
        if t == True:
            r += 1
            z[n[1]][r+1],z[n[1]+1][r],z[n[1]+1][r+1],z[n[1]+2][r],z[n[1]+2][r+1] = 1,1,1,1,1
            ans -= 5
        else:
            w += 1
print(ans,w)