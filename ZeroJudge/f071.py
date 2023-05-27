#幸運號碼可能會重複
a = [int(_) for _ in input().split(' ') if _]
b = [int(_) for _ in input().split(' ') if _]
c = [int(_) for _ in input().split(' ') if _]
ans = 0
t = True
for i in range(5):
    if b[i] == a[0]:
        ans += c[i]
    if b[i] == a[1]:
        ans += c[i]
    if b[i] == a[2]:
        ans -= c[i]
        t = False
if t == False:
    print(max(0,ans))
else:
    print(ans*2)