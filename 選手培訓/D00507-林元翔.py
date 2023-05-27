m = int(input())
for _ in range(m):
    d = dict()#記錄邊的字典
    z = []#佇列
    ans = []#記錄答案的陣列
    n = input().split(" ")
    if n == []:break
    for i in n:
        if i == "":continue 
        i = str(i).split(",")
        if d.get(i[0],'None') != 'None' :
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
        if d.get(i[1],'None') != 'None' :
            d[i[1]].append(i[0])
        else:
            d[i[1]] = [i[0]]    #建立字典的建及值

    z.append(n[0][0])
    ans.append(n[0][0])
    while len(z) != 0:
        i = z[0]
        q = d[i]#將d字典裡的key為i的value全部取出來
        for u in q:
            if u not in ans:#判斷是否在ans陣列裡
                z.append(u)
                ans.append(u)
        z = z[1:]#佇列更新
    print(" ".join(ans))