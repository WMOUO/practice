a = input().split(" ")
b = input().split(" ")
c = input().split(" ")
d = input().split(" ")
z = {1:"A",2:"B",3:"C",4:"D"}
t = True
n = 0
while t == True:
    z = [a[0],b[0],c[0],d[0]]
    r = 0
    for i in z:
        if i == 'A':n = 0
        elif i == "10":
            if n + 10 <= 99:n += 10
            else:n -= 10
        elif i == "Q":
            if n + 20 <= 99 :n += 20
            else:n -= 10
        elif i == "K":n = 99
        elif i == "5" or i == "J":
            if r == 0:a = a[1:]
            elif r == 1:b = b[1:]
            elif r == 2:c = c[1:]
            elif r == 3:d = d[1:]
            continue
        elif i == "4":z = z[::-1]
        else:n += int(i)