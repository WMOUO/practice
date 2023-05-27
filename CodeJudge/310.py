n = int(input())
w = 0
for i in range(1,n):
    w += 1/(i**0.5+(i+1)**0.5)
print(f'{w:.4f}')