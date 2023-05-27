a = int(input())
for i in [int(_) for _ in input().split(' ')]:
    r = 2
    while True:
        if i % r == 0:
            i = i // r
            if i == 1:
                print("True")
                break
        else:
            r += 1
            if r > 5:
                print("False")
                break