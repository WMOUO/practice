while True:
    try:
        a = input()
        n = [_ for _ in input().split(' ') if _]
        if n[1] in n[0]:
            print("Yes")
            print(f"pos: {n[0].index(n[1])}")
        else:
            print("No")
    except:
        break