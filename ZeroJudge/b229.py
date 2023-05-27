n = int(input())
a = 1
b = 3
for i in range(2,n+1):
    a,b = b,b*2+a
print(b)