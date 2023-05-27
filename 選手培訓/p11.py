a,b = map(int,input().split(' '))
if a % 2 != 0:a += 1
if b % 2 != 0:b -= 1
n = (b-a)//2+1
print(n*(a+b)//2)