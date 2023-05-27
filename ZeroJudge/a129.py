z,ans,ans_2=[],[],0
for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ')]
    z.append([(n[0]**2+n[1]**2),n[2]])
z.sort()
for i in range(len(z)):
    ans.append(z[i][1])
r = ans[::-1]
t = [0]*len(r)
e = 100001
for i in range(len(r)):
    if r[i] < e:
        e = r[i]
    t[i] = e
for i in range(len(ans)):
    if ans[i] - t[len(r)-i-1] > ans_2:
        ans_2 = ans[i] - t[len(r)-i-1]
print(ans_2)