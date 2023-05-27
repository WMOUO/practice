z = []
for _ in range(int(input())):
    x = [float(_) for _ in input().split(" ") if _]
    z.append(x)
ans = 0
ans2 = 0
b = 0
c = 1
while True:
    ans += z[b][0] * z[c][1]
    ans2 += z[c][0] * z[b][1]
    b += 1
    c += 1
    if c == len(z):
        c = 0
        ans += z[b][0] * z[c][1]
        b = 0
        c = len(z)-1
        ans2 += z[b][0] * z[c][1]
        break
ans = str(abs(ans-ans2)/2).split(".")
if len(ans[1]) < 2:
    ans[1] += '0'
elif len(ans[1]) > 2:
    ans[1] = ans[1][:2]
print('.'.join(ans))