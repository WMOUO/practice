while True:
    try:
        n = int(input())-1
        print(int((n*(n+1)*(2*n+1)/6)+((n+1)*n/2)+(n*2))//2+2)
    except:
        break