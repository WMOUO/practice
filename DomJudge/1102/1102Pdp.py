a = int(input())
n = [int(_) for _ in input().split(' ') if _]
n.sort(key = lambda x:-x)
a = sum(n)
z = [[1,n] for _ in range(int(1))]+[[0,0] for _ in range(a)]
ans = set()
for i in range(1,a+1):
    for u in n:
        if z[i-u][0] == 1 and u in z[i-u][1]:
            z[i][0] = 1
            w = list(z[i-u][1])
            w.remove(u)
            z[i][1] = w
            ans.add(i)
print(len(ans))
for i in ans:
    print(i,end = ' ')