def lol(r):
    if r == 1:
        return 1
    if r % 2 == 0:
        return lol(r//2)
    else:
        return lol(r-1)+lol(r+1)

n = int(input())
print(lol(n))