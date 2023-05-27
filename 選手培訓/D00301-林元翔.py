def P(A):
    z = []
    for i in A :
        if i == "(" :z.append(1)
        elif i == ")" :
            if len(z) == 0 or z[-1] == 2 or z[-1] == 3:return False
            elif z[-1] == 1:z=z[:-1]
        elif i == "[" :z.append(2)
        elif i == "]" :
            if len(z) == 0 or z[-1] == 1 or z[-1] == 3:return False
            elif z[-1] == 2:z=z[:-1]
        elif i == "{" :z.append(3)
        elif i == "}" :
            if len(z) == 0 or z[-1] == 1 or z[-1] == 2:return False
            elif z[-1] == 3:z=z[:-1]
    if z == [] :return True
    else :return False
n = int(input())
for i in range(n):
    L = [a for a in input()]
    V = P(L)
    if V == True :print("Yes")
    elif V == False :print("No")
#print("Yes" if P(input()) else "No")