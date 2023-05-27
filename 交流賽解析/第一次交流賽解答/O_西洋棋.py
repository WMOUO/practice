while True:
    n = [int(_) for _ in input().split(' ') if _]
    if n[0] == n[1] == n[2] == n[3] :
        break
    if n[0] == n[2] and n[1] == n[3] :
        print(0)
    elif n[0] == n[2] or n[1] == n[3] or abs(n[0]-n[2]) == abs(n[1]-n[3]):
        print(1)
    else:
        print(2)