z = [0,5,8,8,2,3,5,2,9,4,1,1,7,6,4,7]
for _ in range(int(input())):
    n = int(input())
    a = n // 16
    b = n % 16
    print(str(z[b-1])+' '+str(72*a+sum(z[0:b])))