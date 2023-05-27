import datetime
a = int(input())
n = [int(_) for _ in input().split(" ") if _]
m = [int(_) for _ in input().split("/") if _]
b = max(n)
u = 1
t = False
while t == False:
    t = True
    for i in n:
        if b*u % i != 0:
            u += 1
            t = False
            break
day = b*u
k = str(datetime.date(m[0],m[1],m[2])+datetime.timedelta(days = day))
k = list(k.split('-'))
print('/'.join(k))