a,b = map(int,input().split(' '))
c = int(input())
z = [None]*26
r = [0]*26
for i in range(a):
    n = [_ for _ in input().upper().split(' ') if _]
    for u in range(len(n)):
        if n[u].isalpha():
            z[ord(n[u])-65] = (i,u)
            r[ord(n[u])-65] = 1
if sum(r) < c:
    print('Mission fail.')
else:
    b = 0
    for i in z:
        if i == None:
            continue
        print(i[0],i[1])
        b += 1
        if b == c:
            break

#5 5
#5
#0 0 a 0 0
#0 b 0 0 0
#c 0 0 0 0
#0 d 0 0 0
#0 0 e 0 0

#2 2
#4
#g e
#f d