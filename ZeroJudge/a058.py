z = [0,0,0]
for _ in range(int(input())):
    z[(int(input())) % 3 ] += 1
print(z[0],z[1],z[2])