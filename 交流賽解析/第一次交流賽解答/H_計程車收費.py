n = float(input())*10-15
if n <= 0:
    print(85)
else:
    if n % 3 != 0:
        print(str(int(85+(n//3)*5+5)))
    else:
        r = int(85+(n//3)*5)
        print(str(r))