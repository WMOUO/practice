a,b,c = map(int,input().split(' '))
if b**2-(4*a*c)<0:print('No real root')
else:
    r = int((b**2 - a*c*4)**0.5)
    ans = (b*(-1) + r) // (2*a)
    ans_2 = (b*(-1)-r) // (2*a)
    if ans == ans_2:print(f'Two same roots x={ans}')
    else:print(f'Two different roots x1={max(ans,ans_2)} , x2={min(ans,ans_2)}')