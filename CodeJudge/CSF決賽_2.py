n = [int(_) for _ in input().split(' ') if _]
n.sort(reverse = True)
r = 0
while len(n) > 0:
    n.pop(0)
    r += n.pop(0)
    n.pop()
print(r)

n = [int(_) for _ in input().split(' ') if _]
n.sort(reverse = True)
r = 0
n = n[:-1*(len(n)//3)]
for i in range(len(n)) :
    if i % 2 == 1:
        r += n[i]
print(r)