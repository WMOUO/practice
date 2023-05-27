from math import gcd
z = [1,1,2,6,24,120]
for _ in range(int(input())):
    a =''
    b = ''
    n = input().replace(',',' ')
    n = [_ for _ in n.split(' ') if _]
    for i in range(1,3):
        n[i] = int(n[i])
        w = ' '.join(n[0]).split(' ')
        for u in range(len(w),0,-1):
            r = 1
            while True:
                if z[u-1]*r >= n[i]:
                    r -= 1
                    if i == 1:
                        a += w.pop(r)
                    else:
                        b += w.pop(r)
                    n[i] -= z[u-1]*r
                    break
                else:
                    r += 1
    print(gcd(int(a),int(b)))