z = [0,0]
for i in range(2):
    n = sum([int(_) for _ in input().split(' ') if _])
    r = sum([int(_) for _ in input().split(' ') if _])
    if n > r:
        z[i] = '主'
    else:z[i] = '客'
    print(str(n)+':'+str(r))
if z[0] == z[1]:
    if z[0] == "主":
        print("Win")
    else:print("Lose")
else:
    print("Tie")