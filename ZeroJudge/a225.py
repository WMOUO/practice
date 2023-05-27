while True:
    try:
        a = input()
        n = [int(_) for _ in input().split(' ') if _]
        n.sort(key = lambda x:(x%10,-(x//10)))
        print(' '.join(map(str,n)))
    except:
        break