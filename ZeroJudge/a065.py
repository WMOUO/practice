n = input()
ans = ''
for i in range(1,len(n)):
    a = max(ord(n[i]),ord(n[i-1]))-min(ord(n[i]),ord(n[i-1]))
    ans += str(a)
print(ans)