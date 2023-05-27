while True:
    try:
        n = [int(_) for _ in input().split(" ") if _]
        n.sort()
        if sum(n) != (n[0]+n[-1])*len(n)//2:
            print("Not jolly")
        else:
            print("Jolly")
    except:
        break
#1 2 4 7 11 16
a = 1
b = 2
c = 1
#---
a = 2
b = 3

#1 7 2 -2 -5 -7 -8 