# 1
while True:
    try:
        n = input()
        ans = 0
        for i in n:
            ans += int(i)
        print(ans)
    except:
        break
# 3
while True:
    try:
        print(sum([int(_) for _ in ' '.join(input()).split(' ') if _]))
    except:
        break

###
while True:
    try:
        print(sum(map(int, input())))
    except:
        break
