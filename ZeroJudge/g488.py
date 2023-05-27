n = int(input())
z = [0,1]
for i in range(2,n+1):
    z.append(z[i-1]+i**2-i+1)
print(z[-1])