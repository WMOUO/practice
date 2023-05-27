n = int(input())
if n > 40:
    print(100)
elif n > 20:
    print(80+n-20)
elif n > 10:
    print(60+(n-10)*2)
else:
    print(n*6)