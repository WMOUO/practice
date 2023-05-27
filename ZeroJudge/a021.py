n = [_ for _ in input().split(' ')]
if n[1] == '+':
    print(eval(n[0])+eval(n[2]))
elif n[1] == '-':
    print(eval(n[0])-eval(n[2]))
elif n[1] == '*':
    print(eval(n[0])*eval(n[2]))
else:
    print(eval(n[0])//eval(n[2]))