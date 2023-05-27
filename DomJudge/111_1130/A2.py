while True:
    n = int(input())
    if n == 0:
        break
    if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0):
        print('a leap year')
    else:
        print('a normal year')