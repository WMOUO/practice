n = input().strip().split(' ')
a = n[1]
b = n[2]
c = int(n[0])
a = int(a)+int(b)
a = ' '.join(str(a)).split(' ')
for i in range(len(a)-1,-1,-1):
    if int(a[i]) >= c:
        a[i] = str(int(a[i])-c)
        if i == 0:
            a = ['0'] + a
            a[0] = str(0 + 1)
        else:
            a[i-1] = str(int(a[i-1]) + 1)
print(''.join(a))