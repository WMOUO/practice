z = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
for _ in range(int(input())):
    n = int(input())
    ans = ''
    for i in z.keys():
        if n//i >= 1:
            ans += z[i]*(n//i)
            n %= i
    print(ans)
