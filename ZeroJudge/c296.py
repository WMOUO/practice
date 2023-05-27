#AC
n, m, k = map(int, input().split())
ans = 0
for i in range(n-k+1, n+1):
    ans = (ans + m) % i
print(ans + 1)
# #TLE
# n,m,k = map(int,input().split(' '))
# z = [False]+[True]*n
# u = 0
# for i in range(k):
#     r = 0
#     while True:
#         if z[u] == True:
#             r += 1
#             if r == m:
#                 z[u] = False
#                 break
#         u += 1
#         if u > n:
#             u = 1
# while True:
#     u += 1
#     if u > n:
#         u = 1
#     if z[u] == True:
#         print(u)
#         break
