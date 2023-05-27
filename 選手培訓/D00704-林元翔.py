import bisect 
for _ in range(int(input())):
    n = [n for n in input().split(",") if n]
    z = [n[0]]
    n = n[1:]
    for i in n:
        a = bisect.bisect(z,i)
        if a == len(z):
            if i == z[-1]:continue
            z.append(i)
        else:z[a] = i
    print(len(z))