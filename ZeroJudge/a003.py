n = [int(_) for _ in input().split(' ') if _]
r = (n[0]*2+n[1])%3
if r == 0:
    print('普通')
elif r == 1:
    print('吉')
else:
    print('大吉')