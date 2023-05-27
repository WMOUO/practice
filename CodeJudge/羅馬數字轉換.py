z = {"M":1000 ,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
n = input().strip()
r = 0
w = 0
while w < len(n):
    if w < len(n)-1 and n[w:w+2] in z:
        r += z[n[w:w+2]]
        w += 2
    else:
        r += z[n[w]]
        w += 1
print(r)