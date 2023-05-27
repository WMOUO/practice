n = int(input())
a = 2*(n-1)+1
for i in range(n):print(str('_'*((a-(2*(i)))//2))+str('*'*(2*i+1))+str('_'*((a-(2*(i)))//2)))