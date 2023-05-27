while True:
    try:
        n = input()
        z = []
        for i in n:
            if i == '+' or i == '-' or i =='*' or i =='/' or i == '%':
                a = z.pop()
                b = z.pop()
            if i =='+':
                z.append(a+b)
            elif i == '-':
                z.append(b-a)
            elif i == '*':
                z.append(a*b)
            elif i == '/':
                z.append(b/a)
            elif i == '%':z.append(b%a)
            else:
                z.append(int(i))
        print(int(z[-1]))
    except:
        break