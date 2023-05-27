for _ in range(int(input())):
    n = input()
    ans = []
    for i in n:
        while True:
            try:
                ans.append(int(i))
                break
            except:
                break
    if len(ans) != 0:
        ans.sort()
        ans = map(str,list(set(ans)))
        print(''.join(ans))
    else:
        print('N')