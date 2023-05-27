for _ in range(int(input())):
    a,b = map(int,input().split(' '))
    print(f"Case {_+1} :")
    for i in range(b):
        if a % b != 0 and i+1 == b:print(f'第{i+1}位 : 拿{a//b+a%b}元並說DD! BAD!')
        else:print(f'第{i+1}位 : 拿{a//b}元並說DD! BAD!')