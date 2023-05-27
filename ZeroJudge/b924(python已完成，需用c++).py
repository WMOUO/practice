#用c++
while True:
    try:
        a,b = map(int,input().split(' '))
        z = [0]*(a+1)
        for _ in range(b):
            n = [int(_) for _ in input().split(' ') if _]
            z[n[0]],z[n[1]] = z[n[0]]+1,z[n[1]]+1
        ans = 0
        for i in z:
            if i % 2 != 0:
                ans += 1
                if ans > 2:
                    break
        if ans == 2 or ans == 0:
            print("YES")
        else:
            print("NO")
        print()
        h = input()
    except:
        break