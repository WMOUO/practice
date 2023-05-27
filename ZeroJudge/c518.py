#python時間太久
a,b = map(int,input().split(' '))
n = input()
i = input()
u = input()
for t in range(len(i)):
    n = n.replace(i[t],u[t])
print(n)