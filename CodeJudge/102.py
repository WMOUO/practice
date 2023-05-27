z = []
for _ in range(3+1):
    n = eval(input())
    n = f'{n:.2f}'
    z.append(n)
print(f'|{z[0]:>7} {z[1]:>7}|')
print(f'|{z[2]:>7} {z[3]:>7}|')
print(f'|{z[0]:<7} {z[1]:<7}|')
print(f'|{z[2]:<7} {z[3]:<7}|')