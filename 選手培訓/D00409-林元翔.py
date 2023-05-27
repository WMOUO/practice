n = int(input())
H = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for _ in range(n):
    L = input()
    z = []
    y = 0
    a = 0
    c = 0
    c = H[L[0]]
    for i in L :
        if  H[i] > c :
            y = y - c
            a = H[i] - c
            c = H[i]
            y += a
        else:
            c = H[i]
            y += c
    print(y)