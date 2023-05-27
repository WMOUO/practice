d = {"1": "I", "4":"IV", "5": "V", "9":"IX", "10": "X", "40":"XL", "50": "L", "90":"XC" , "100": "C", "400":"CD" , "500": "D", "900":"DM" ,"1000": "M"}
m = int(input())
for i in range(m):
    n = input()
    a = list(d.keys())
    a = a[::-1]
    z = []
    ans = ""
    e = 0
    while n != '0':
        b = a[e]
        if int(n) // int(b) != 0:
            n = str(int(n) - int(b))
            z.append(b)
        else:e += 1
    for i in z :
        ans += d[i]
    print(ans)