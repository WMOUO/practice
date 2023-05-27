#二進位小數點要到16位元
for _ in range(int(input())):
    n = input().strip().split(' ')
    r = 0
    while len(n) > 0:
        a = n.pop(0)
        b = n.pop(0)
        r += int(a+b,16)
    r = f'{r:x}'
    if len(r) > 4:
        a = r[:len(r)-4]
        r = r[len(r)-4:]
    r = int(r,16)
    a = int(a,16)
    r += a
    r = f'{r:b}'
    w = ''
    r = '0'*(16-len(r))+r
    for i in range(len(r)):
        if r[i] == '1':
            w += '0'
        else:
            w += '1'
    r = int(w,2)
    r = f'{r:x}'
    if len(r) <= 3:
        r = '0'*((1+3)-len(r))+r
    print(r)
#101110100111011
#010001011000100
#1010001011000100