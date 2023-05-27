z = []
while True:
    n = int(input())
    if n == -9999:
        break
    z.append(n)
print(tuple(z))
print(f'Length: {len(z)}')
print(f'Max: {max(z)}')
print(f'Min: {min(z)}')
print(f'Sum: {sum(z)}')