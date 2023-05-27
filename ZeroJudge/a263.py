import datetime
while True:
    try:
        a = [int(_) for _ in input().split(' ') if _]
        b = [int(_) for _ in input().split(' ') if _]
        a = datetime.date(a[0],a[1],a[2])
        b = datetime.date(b[0],b[1],b[2])
        print(abs(b-a).days)
    except:
        break