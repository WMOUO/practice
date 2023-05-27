while True:
    try:
        a = []
        b = []
        ans = []
        max = 0
        n = int(input())
        if n == 0:
            break
        m = [int(_) for _ in input().split(" ") if _]
        for i in range(n):
            a = b
            b = []
            for j in range(1,n):#-i+1
                if i == 0:
                    if j == 1:b = [m[i]]
                    f = m[j]+b[j-1]
                    b.append(f)
                elif i != 0:
                    # if j == 0:
                    #     f = m[i]
                    #     b.append(f)
                    # else:
                    f = a[j]-a[0]
                    b.append(f)
                if f > max:
                    max = f
        # for i in range(n):
        #     for j in range(i, n):
        #         if i != 0:
        #             z[i][j] = z[i-1][j] - z[i-1][i-1]
        #         else:
        #             if j != 0:
        #                 z[i][j] = z[i][j-1]+m[j]
        #             else:
        #                 z[i][j] = m[j]
        #         ans.append(z[i][j])
        # w = max(ans)
        if max > 0:
            print(f'The maximum winning streak is {max}.')
        else:
            print('Losing streak.')
    except:
        break