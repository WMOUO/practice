ans = 0
z = []
r = True
for i in input():
    if i == "(":z.append('(')
    else:
        if len(z) == 0 or z[-1] != "(":
            r = False
            break
        a = z.pop(-1)
        ans += 1
if r == True and len(z) == 0:
    print(ans)
else:
    print(0)