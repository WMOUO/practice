b = [0]
n = int(input())
m = [int(_) for _ in input().split(" ") if _]
for i in range(n):
    b.append(b[i]+m[i])
for _ in range(int(input())):
    w = [int(_) for _ in input().split(" ")]
    print(b[w[1]]-b[w[0]-1])