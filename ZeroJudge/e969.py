n = [int(_) for _ in input().split(' ') if _]
r = 0
if (n[2] == 0 and n[0] < 32) or (n[2] == 1 and n[0] < 55):
    print("Wayne can't eat and drink.")
else:
    while True:
        if n[2] == 0:
            n[0] -= 32
            if n[0] < 0:
                break
            elif n[0] == 0:
                print(f"{r}: Wayne eats an Apple pie, and now he doesn't have money.")
            elif n[0] == 1:
                print(f"{r}: Wayne eats an Apple pie, and now he has {n[0]} dollar.")
            else:
                print(f"{r}: Wayne eats an Apple pie, and now he has {n[0]} dollars.")
        else:
            n[0] -= 55
            if n[0] < 0:
                break
            elif n[0] == 0:
                print(f"{r}: Wayne drinks a Corn soup, and now he doesn't have money.")
            elif n[0] == 1:
                print(f'{r}: Wayne drinks a Corn soup, and now he has {n[0]} dollar.')
            else:
                print(f'{r}: Wayne drinks a Corn soup, and now he has {n[0]} dollars.')
        r += n[1]
        n[2] = (n[2]+1) % 2