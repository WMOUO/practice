z = []
while True:
    try:        
        n = input()
        if n not in z:
            z.append(n)
            print('NO')
        else:
            print('YES')
    except:
        break