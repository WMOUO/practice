n = int(input())
for _ in range(n):
    m = input()
    w = int(m[::-1])
    m = int(m)
    a = True
    for i in range(2,int(m**0.5+1)):
        if m % i == 0 :
            a = False
    for i in range(2,int(w**0.5+1)):
        if w % i == 0 :
            a = False
    if a == True:print("Y")
    elif a == False:print("N")