n = [_ for _ in input().split(' ')]
if len(n[0]) > 2:
    a = n.pop(0)
    n.append(a[0:2])
    n.append(a[2:])
while True:
    sum = 1
    for i in n:
        sum *= int(i)
    n =[]
    sum = str(sum)
    if len(sum) > 2:
        while len(sum) > 1:
            if sum[0:2] != '00':n.append(sum[0:2])
            sum = sum[2:]
        if len(sum) == 1:
            if sum == '0':continue
            n.append(sum)
    else:n.append(sum)
    if len(n) == 1:break
a = n.pop()
n.append(a[0])
if len(a) == 2:n.append(a[1])
while True:
    sum = 1
    for i in n:
        if i == '0':continue
        sum *= int(i)
    n = []
    if len(str(sum)) == 2:
        for i in str(sum):
            n.append(i)
    else:
        print(sum)
        break