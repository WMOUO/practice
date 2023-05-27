while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        if n[0] // 10 >= 1 and n[2] // 2 >= 1:
            n[1] += min(n[0] // 10,n[2] // 2)
        print(f'{n[0]} 個餅乾，{n[1]} 盒巧克力，{n[2]} 個蛋糕。')
    except:
        break