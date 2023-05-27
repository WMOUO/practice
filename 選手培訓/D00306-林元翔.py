while True :
    try:
        L = [a for a in input().split(" ") if a]
        if len(L) == 0 :break
        ans = True
        z = []
        for i in L :
            if i == "+" or i == "-" or i == "*" or i == "//" or i == "**":
                if len(z) <= 1:
                    ans = False
                    break
                n1 = eval(z[-1])
                n2 = eval(z[-2])
                z = z[:-2]
                if i == '+':
                    z.append(str(n2 + n1))
                elif i == '-':
                    z.append(str(n2 - n1))
                elif i == '*':
                    z.append(str(n2 * n1))
                elif i == '//':
                    z.append(str(n2 // n1))   
                elif i == "**":
                    z.append(str(n2 ** n1))
            else :z.append(i)
        if ans == False or len(z) > 1 :print('Error')
        else:
            print(int(z[0]))
    except:
        break