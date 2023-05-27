def P(A):
    length = 10
    queue = [None]*length
    front = -1
    rear = -1
    i = 0
    while i < len(A):
        if A[i].upper() == "EN": #ENQUEUE
            if rear<(length-1):
                rear += 1
                queue[rear] = A[i+1]
            else : print("queue overflow")
            i += 2
        elif A[i].upper() == "DE": #DEQUEUE
            if front<rear :
                front += 1
                data = queue[front]
                print(data)
            else : print("queue empty")
            i += 1
while True:
    L = [a for a in input().split(" ") if a]
    if len(L)==0:break
    S = P(L)