import time
#2000000000
print(2000000000**0.5)
st = time.perf_counter()
z = [0]+[1]*50000
r = []
for i in range(2,len(z)):
    if z[i] == 1:
        r.append(i)
        for u in range(i*2,len(z),i):
            z[u] = 0

i = 2000000000
while True:
    t = True
    for u in r:
        if i % u == 0:
            t = False
            break
    if t == True:
        print(i)
        break
    i -= 1
en = time.perf_counter()
print(en-st)