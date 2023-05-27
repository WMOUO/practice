z = [0]*5001
z[1] = 1
for i in range(2,5001):
    z[i] = z[i-1]+z[i-2]
while True:
    try:
        n = int(input())
        print(f'The Fibonacci number for {n} is {z[n]}')
    except:
        break