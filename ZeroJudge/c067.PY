r = 1
while True:
    a = int(input())
    if a == 0:break
    n = [int(_) for _ in input().split(' ') if _]
    w = sum(n) // a
    ans = 0
    for i in n:
        if i < w:
            ans += w-i
    print(f"Set #{r}")
    print(f'The minimum number of moves is {ans}.')
    r += 1