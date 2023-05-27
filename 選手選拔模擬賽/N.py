while True:
    r = [26,9]
    n = int(input())
    if n == 0:
        break
    r[0] += n
    r[1] += n
    r[0] %= 26
    if r[0] % 26 == 0:
        r[0] = 26
    r[1] %= 10
    r[1] += 1
    if r[1] % 10 == 0:
        r[1] = 1
    print(chr(r[0]+64)+str(r[1]))