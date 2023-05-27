def P(A):
    queue = []
    i = 0
    while i < len(A):
        if A[i].upper() == "EN": 
            queue.append(A[i+1])
            i += 2
        elif A[i].upper() == "DE": 
            if len(queue) > 0 :
                data = queue[0]
                queue = queue[1:]
                print(data)
            else : print("queue empty")
            i += 1
while True:
    L = [a for a in input().split(" ") if a]
    if len(L)==0:break
    S = P(L)