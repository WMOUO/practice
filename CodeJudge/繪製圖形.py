a = int(input())
b = int(input())
if a == 0:
    for i in range(b):
        print('  *')
        print(' * *')
        for _ in range(4):
            print('*   *')
        print(' * *')
        print('  *')
else:
    for i in range(b):
        for _ in range(2):
            print('*   *')
        print(' * *')
        print('  *')
        print('  *')
        print(' * *')
        for _ in range(2):
            print('*   *')