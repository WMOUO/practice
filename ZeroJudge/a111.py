z = []
for _ in range(int(input())):
    a,b = map(int,input().split(' '))
    z.append([a,b])
a = z[-1][0]
z = z[:-1]
while True:
    if len(z) == 0:
            print(0)
            break
    b = z[0]
    if a > b[1]:
        a -= b[1]
        z = z[1:]
        
    else:
        print(len(z))
        break