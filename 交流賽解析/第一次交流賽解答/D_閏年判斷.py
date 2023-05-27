from calendar import isleap
while True:
    try:
        n = int(input())
        if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0):
            print('閏年')
        else:
            print('平年')
    except:
        break


while True:
    try:
        n = int(input())
        if isleap(n):
            print('閏年')
        else:
            print('平年')
    except:
        break

###
while True:
    try:
        print('閏年' if isleap(int(input())) else '平年')
    except:
        break
