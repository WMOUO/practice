for _ in range(int(input())):
    ans = []
    n = input().split('}, {')
    a = n[0][1:].replace(',',' ')
    a = [int(_) for _ in a.split(' ') if _]
    a = set(a)
    b = n[1][:-1].replace(',',' ')
    b = [int(_) for _ in b.split(' ') if _]
    b = set(b)
    if len(a|b) != 0:
        ans.append(a|b)
    else:
        ans.append('N')
    if len(a&b) != 0:
        ans.append(a&b)
    else:
        ans.append('N')
    if len(a-b) != 0:
        ans.append(a-b)
    else:
        ans.append('N')
    if len(a^b) != 0:
        ans.append(a^b)
    else:
        ans.append('N')
    r = ''
    for i in ans:
        r += str(i)+', '
    print(r[:-2])