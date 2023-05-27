n = input().lower()
ans = input().lower()
real_ans = ''
a = None
for i in range(len(n)):
    if n[i] == ans:
        if a != None:
            real_ans += str(i-a)+' '
        a = i
print(real_ans[:-1])