from json.encoder import INFINITY
m = int(input())
for _ in range(m):
    G = dict()#鄰接串列表
    V = {}#走訪
    W = dict()#權重
    ans = 0#記錄答案的陣列
    n = input().split(" ")
    for i in n:
        if i == "":continue
        #鄰接串列 
        i = str(i).split(",")
        if G.get(i[0],'None') != 'None' :
            G[i[0]].append(i[1]+" "+i[2])
        else:
            G[i[0]] = [i[1]+" "+i[2]]
        if G.get(i[1],'None') != 'None' :
            G[i[1]].append(i[0]+" "+i[2])
        else:
            G[i[1]] = [i[0]+" "+i[2]]
        #走訪
        if V.get(i[0],"None") == "None":
            V[i[0]] = False
        if V.get(i[1],"None") == "None":
            V[i[1]] = False
        #權重
        if W.get(i[0],"None") == "None":
            W[i[0]] = INFINITY
        if W.get(i[1],"None") == "None":
            W[i[1]] = INFINITY
    #過程
    w = n[0][0]
    W[w] = 0
    p = INFINITY
    while False in list(V.values()):
        V[w] = True
        if False not in list(V.values()):break
        p = INFINITY
        for i in G[w]:
            i = str(i).split(" ")
            if int(i[1])< W[i[0]]:
                W[i[0]] = int(i[1])
        #決定權重最小值
        for i in list(W.keys()):
            if W[i] < p and V[i] == False:
                p = int(W[i])
                w = i
        #變更走訪、權重
        ans += p
    print(ans)