n = [int(_) for _ in input().split(" ") if _]
print(f'{(n[0]**n[1]) % (n[2]**n[3]):,}'.replace(',',' '))