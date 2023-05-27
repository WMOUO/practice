while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        n = [(n[0],n[1]),(n[2],n[3]),(n[4],n[5])]
        n.sort()
        if n[1][0]-n[0][0] != n[2][0]-n[1][0] or n[1][1]-n[0][1] != n[2][1]-n[1][1]:
            print('TRIANGLE')
        else:
            print("LINE")
    except:
        break