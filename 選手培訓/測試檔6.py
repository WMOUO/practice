n = [int(n) for n in input().split(' ') if n]
if n[0] == n[1] == n[2] == 1:print('No real root')
else:
    ans = []
    ans.append(int(((n[1]*(-1)) + ((n[1]**2)-4*n[0]*n[2])**0.5 ) / (2*n[0])))
    ans.append(int(((n[1]*(-1)) - ((n[1]**2)-4*n[0]*n[2])**0.5 ) / (2*n[0])))
    ans.sort()
    ans = ans[::-1]
    if ans[0] == ans[1]:
        print(f'Two same roots x={ans[0]}')
    else:
        print(f'Two different roots x1={ans[0]} , x2={ans[1]}')