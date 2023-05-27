def P(A):
    z = []
    for i in A :
        if i == "a" :
            z.append('a')
        elif i == "b" :
            z.append('b')
        elif i == "c" :
            if len(z) <= 1:z.append("c")
            elif z[-1] == "b" and z[-2] == "a" :z = z[:-2]
            else:z.append("c")
    if len(z) == 0 :return True
    else :return False
while True:
    L = input()
    if len(L) == 0:break
    V = P(L)
    if V == True :print("True")
    elif V == False :print("False")