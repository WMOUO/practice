n = int(input())
if n <= 10:
    print(n*100)
elif n > 10 and n < 21:
    print((n-10)*200+10*100)
else:
    print((n-20)*300+10*200+10*100)