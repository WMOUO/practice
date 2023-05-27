z = [0]*1000001
for i in range(2,len(z)):
    for u in range(i,len(z),i):
        z[u]+= 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f'{n} : {len(z[n])-1}')