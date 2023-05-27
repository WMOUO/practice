n = int(input())
while True:
    try:
        print(n//abs(n))
        break
    except:
        print(0)
        break