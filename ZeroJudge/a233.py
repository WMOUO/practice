a = int(input())
print(' '.join(list(map(str,sorted([int(_) for _ in input().split(' ') if _])))))