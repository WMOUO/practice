while True:
    try:
        n = int(input())
        if n % 3 == 0:
            print(n//3)
        else:
            print(n//3+1)
    except:
        break
#
while True:
    try:
        print((int(input())+2)//3)
    except:
        break