a = 0
z = [0,0,0]
for _ in range(int(input())):
    n = input().strip()
    if n == 'Get_Kill':
        a += 1
        if a <= 2:
            print('You have slain an enemie.')
        elif a == 3:
            print('KILLING SPREE!')
        elif a == 4:
            print('RAMPAGE~')
        elif a == 5:
            print('UNSTOPPABLE!')
        elif a == 6:
            print('DOMINATING!')
        elif a == 7:
            print('GUALIKE!')
        else:
            print('LEGENDARY!')
        z[0] += 1
    elif n == 'Die':
        if a >= 3:
            print('SHUTDOWN.')
        else:
            print('You have been slained.')
        a = 0
        z[1] += 1
    else:
        z[2] += 1
print(f"{z[0]}/{z[1]}/{z[2]}")