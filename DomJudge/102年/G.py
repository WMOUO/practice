for _ in range(int(input())):
    n = input().strip().replace('-','')
    ans = 0
    if len(n) == 10:
        a = 10
        for i in n[:-1]:
            ans += int(i)*a
            a -= 1
        ans = 11-(ans%11)
        if n[-1] == 'X':
            if ans == 10:
                print("T")
            else:
                print('F')
        else:
            if ans == int(n[-1]):
                print("T")
            else:
                print("F")
    else:
        a = 0
        for i in n[:-1]:
            if a == 0:
                ans += int(i)*1
            else:
                ans += int(i)*3
            a ^= 1
        ans = 10-ans%10
        if ans == int(n[-1]):
            print('T')
        else:
            print('F')