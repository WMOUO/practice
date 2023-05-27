import time
n = 2000000000
start = time.perf_counter()
length = int(n**0.5)+1
s = [True]*length
primes = []
for i in range(2,length):
    if s[i]:
        primes.append(i)
        s[i*i:length:i] = [False]*len(range(i*i,length,i))
while True:
    flag = True
    for prime in primes:
        if n % prime == 0:
            flag = False
            break
    if flag == True:
        print(n)
        break
    n -= 1
print(time.perf_counter()-start)