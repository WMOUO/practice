arr =[]
up = 0
ans = 0
for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    arr.append(n)
arr = sorted(arr,key=lambda x:(x[0],-x[1]))
for i in arr:
    if i[0] < up and i[1] <= up:continue
    elif i[0] < up and i[1] > up:
        ans += i[1]-up
        up = i[1]
    else:
        ans += i[1]-i[0]
        up = i[1]
print(ans)
#下面那個會TLE
# a = 10
# z = [0]*11
# for _ in range(int(input())):
#     n = [int(_) for _ in input().split(' ') if _]
#     b = max(n)
#     if b > a:
#         t = [0]*(b-a)
#         z += t
#         a += b-a
#     for _ in range(min(n[0],n[1])-1,max(n[0],n[1])):
#         z[_] = 1
# print(sum(z))