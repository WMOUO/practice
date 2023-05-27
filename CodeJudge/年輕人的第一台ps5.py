a,b = map(int,input().split(' '))
z = [int(_) for _ in input().split(' ') if _]
r = [0.0]*b
for _ in range(a):
    n = [int(_) for _ in input().split(' ') if _]
    for i in n:
        r[i-1] += 1/len(n)
w = [0,0]
for i in range(b):
    p = min(1.0,(z[i]/(r[i]+1)))
    if p > w[0] :
        w[0] = p
        w[1] = i+1
print(w[1])
        
# a,b = map(int,input().split(' '))
# n = [int(_) for _ in input().split(' ') if _]
# z = [1]*b
# for _ in range(a) :
#     for i in [int(_) for _ in input().split(' ') if _]:
#         z[i-1] += 1
# w = [n[0] / z[0],0]
# for i in range(1,len(z)):
#     if n[i] / z[i] > w[0] :
#         w[0] = n[i] / z[i]
#         w[1] = i
# print(w[1]+1)