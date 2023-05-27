a,b = map(int,input().split(' '))
if a % 2 == 0 or b % 2 == 0 : print((b-a)//2+1)
else:print((b-a)//2)