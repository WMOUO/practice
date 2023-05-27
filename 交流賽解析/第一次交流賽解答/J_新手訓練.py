for _ in range(int(input())):
    n = [int(_) for _ in input().split() if _]
    if n[0] == 1:
        print(n[1]+n[2])
    elif n[0] == 2:
        print(n[1]-n[2])
    elif n[0] == 3:
        print(n[1]*n[2])
    else:
        print(n[1]//n[2])

###
for _ in range(int(input())):
    a, b, c = input().split()
    op = ['+', '-', '*', '//']
    print(eval(b+op[int(a)-1]+c))
