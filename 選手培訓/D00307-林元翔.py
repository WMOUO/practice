def P(A) :
    z = []#運算元 123
    x = []#運算子 +-*/
    y = []
    b = 0
    for i in A :
        if i =="(" :b = 1
        elif i == ")" :
            y = y[::-1]
            for u in y:
                z.append(u)
            b = 0
        elif i == "+" or i == "-" or i == "*" or i == "//" or i == "**":
            if i == "*" or i == "//" or i =="**" :
                if b == 1 :y.append(i)
                else:x.append(i)
            elif  i == '+' or i == '-':
                if b == 1 :
                    if len(y) < 1 or y[-2] == '+' or y[-2] == "-":
                        y.append(i)
                    else:
                        z.append(y[0])
                        y = y[1:]
                        y.append(i)
                else:
                    if len(x) < 1 or x[-2] == '+' or x[-2] == "-":
                        x.append(i)
                    else:
                        z.append(x[0])
                        x = x[1:]
                        x.append(i)
        else:
            if b == 1 :
                z.append(i)
            else:z.append(i)
    x = x[::-1]
    for i in x:
        z.append(i)
    return z
while True :
    try:
        L = [a for a in input().split(" ") if a]
        if len(L) == 0 :break
        V = P(L)
        print(' '.join(V))
    except:
        break
#12 + ( 2 + 3 * 6 )
#1 + 2 * 3 // 5 - 6 + 7 = 1 2 3 * 5 //  6 - 7 + +