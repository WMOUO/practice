#質數表
z = [0]+[0,1]*500000
for i in range(3,int(1000000**0.5)+1,2):
    if z[i] == 0:
        for u in range(i*i,1000001,2*i):
            z[u] = 1
print('質數表 : ',end = '')
for i in range(len(z)):
    if z[i] == 0:
        print(i,end =' ')