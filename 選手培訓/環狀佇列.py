def P(A) :
    MaxQueue = 9
    queue = [None]*MaxQueue
    front = -1 
    rear = -1
    counter = 0 
    i = 0
    x = -1
    while i < len(A):
        if A[i].upper() == "EN":
            if counter < MaxQueue:
                rear = (rear + 1) % MaxQueue
                queue[rear] = A[i+1]
                counter += 1
            else:print("queue overflow")
            i += 2 
        elif A[i].upper() == "DE":
            if counter > 0 :
                front = (front + 1) % MaxQueue
                data = queue[front]
                counter -= 1 
                print(data)
            else:print("queue empty")
            i += 1
    for _ in range(len(A)):
        if queue[x] != None:
           x += 1
           if x == 6:
               x = -1
               queue[x] == None
        elif queue[x] == None:
            continue
    for c in range(len(A)):
        if A[c] != None :
            return A[c]
while True :
    L = [a for a in input().split()]
    if len(L) == 0:break
    V = P(L)
    print(V)