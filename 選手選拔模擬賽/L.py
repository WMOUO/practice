while True:
    try:
        a = input()
        b = input()
        c = 0
        for i in range(len(a)):
            if  a[i] != b[i] :
                c += 1
        print(f'{c/len(a):.2%}')
    except:
        break
#AUACCGGCAUUU
#AUACGGCGAUUU