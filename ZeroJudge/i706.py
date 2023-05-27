a = int(input())
n = [int(_) for _ in input().split(' ') if _]
ans = ['0']*a
r = n[0]
for i in range(1, a):
    if n[i] <= r:
        r = n[i]
    elif n[i] > n[i-1]:
        ans[i] = str(i)
    else:
        w = i-1
        while n[i] <= n[w]:
            w = int(ans[w])-1
            if ans[w] == '0':
                break
        if n[i] > n[w]:
            ans[i] = str(w+1)
print(' '.join(ans))