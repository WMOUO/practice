for o in range(1,int(input())+1):
    a = input()
    n = [_ for _ in ' '.join(input()).split(' ') if _]
    ans = 0
    i = 0
    while i < len(n):
        if n[i] == '.':
            i += 3
            ans += 1
        else:
            i += 1
    print(f'Case {o}: {ans}')