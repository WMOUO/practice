n = input().split()
a = 0
h = 0
while True:
    h += 2 **a
    if h >= len(n):
        print(a+1)
        break    
    a += 1