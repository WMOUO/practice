n = int(input())
for i in range(n):
    m = eval(input())
    a = True
    for i in range(2,int(m**0.5+1)):
        if m % i == 0 :
            a = False
    if a == True:print("Y")
    elif a == False:print("N")