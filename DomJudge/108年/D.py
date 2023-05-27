for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    print(n[0]**n[1]%n[2])