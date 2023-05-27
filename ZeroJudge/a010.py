n = int(input())
a = 2
b = 0
z = ''
while True:
    
    if n % a == 0:
        b += 1
        n //= a
    else:
        if b > 1:
            z += str(a)+'^'+str(b)+' * '
        elif b == 1:
            z += str(a)+' * '
        b = 0
        a += 1
        if a == n:
            z += str(a)+' * '
            n = 1
        if n == 1:
            break
print(z[:-3])