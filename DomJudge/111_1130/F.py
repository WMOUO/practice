a = input()
b = ' '.join(input().strip()).split(' ')
z = ''
for i in a:
    if i not in b:
        z += i
print(z)