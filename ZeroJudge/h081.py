a,b = map(int,input().split(' '))
n = [int(_) for _ in input().split(' ') if _]
r = n[0]
w = float('inf')
c = True
ans = 0
for i in n[1:]:
    if (c == False) and (i <= (w-b)):
        c = True
        r = i
    elif (c == True) and (i >= (r+b)):
        ans += (i-r)
        w = i
        c = False
print(ans)