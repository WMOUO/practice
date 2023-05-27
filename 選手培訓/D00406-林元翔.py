D={f"{i:04b}":f"{i:X}"for i in range(16)}
for i in range(8):
    t = f"{i:03b}"
    D[t] = i
#字典產生
n = int(input())
for i in range(n):
    z = ''
    u = input()
    y = u
    while len(u) % 4 != 0 :
        u = '0' + u
    for i in range(0,len(u)+1,4):
        r = u[i:i+4]
        if r =='': break
        c = str(D[r])
        z += c
    z += ','
    while len(y) % 3 != 0 :
        y = '0' + y
    for i in range(0,len(u)+1,3):
        r = y[i:i+3]
        if r =='': break
        c = str(D[r])
        z += c
    print(z)