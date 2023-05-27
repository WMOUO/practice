def f():
    global w,r,n,z,k
    z = set(n)-{-1}
    a = w - z - k
    k = k | a
    z = w & z
    for i in a:
        n[i] = -1
    if len(a) == 0:
        return len(z)
    return f()
k = set()
n = [int(_) for _ in input().split(',') if _]
r = len(n)
w = set(list(range(r)))
print(f())