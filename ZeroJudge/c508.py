a = int(input())
n = sorted([int(_) for _ in input().split(' ') if _])
w = list(set(n))
n = map(str,n)
print(' '.join(n))
w.reverse()
w = map(str,w)
print(' '.join(w))
# a = int(input())
# n = sorted([int(_) for _ in input().split(' ') if _])
# print(' '.join(map(str,n)))
# print(' '.join(map(str,sorted(list(set(n)),key = lambda x:-x))))