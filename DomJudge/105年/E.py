for _ in range(int(input())):
    n = [0]+[int(_) for _ in input().split(',')]
    Heap = True
    Binary = True
    for i in range(1,len(n)+1):
        if Binary == True:
            if i * 2 <= len(n)-1 and n[i] < n[i*2]:
                Binary = False
            if i * 2 + 1 <= len(n)-1 and n[i] > n[i*2+1]:
                Binary = False
        if Heap == True :
            if i * 2 <= len(n)-1 and (n[i] > n[i*2]) != (n[1] > n[2]):
                Heap = False
            if i * 2 + 1 <= len(n)-1 and (n[i] > n[i*2]) != (n[i] > n[i*2+1]):
                Heap = False
    if Binary == True :
        print("B")
    elif Heap == True:
        print("H")
    else:
        print("F")