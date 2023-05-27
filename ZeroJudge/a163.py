for _ in range(int(input())):
    n,m = input().split()
    c = int(m)
    a = [int(_) for _ in input().split(' ') if _]
    ans = []
    for i in a:
        b = a.pop(-1)
        ans.append(a)