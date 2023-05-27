n = [int(_) for _ in input().split(' ') if _]
r = 0
for i in range(1,n[1]) :
    if i == 2 :
        if n[0] % 400 == 0 or (n[0] % 100 != 0 and n[0] % 4 == 0):
            r += 29
        else:
            r += 28
    elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        r += 31
    else:
        r += 30
r += n[2]
print(r)


# from datetime import datetime
# n = input().split(' ')
# a = datetime.strptime(n[0]+'-01-01',"%Y-%m-%d").date()
# n = '-'.join(n)
# b = datetime.strptime(n,"%Y-%m-%d").date()
# print((b-a).days+1)
