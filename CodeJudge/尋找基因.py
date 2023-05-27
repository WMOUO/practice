n = input().strip()
a = 0
i = 0
t = False
r = ''
z = []
while i < len(n)-2:
    if t == True:
        if n[i:i+3] == 'TGA' or n[i:i+3] == 'TAG' or n[i:i+3] == 'TAA':
            t = False
            if len(r) != 0 and len(r) % 3 == 0:
                w = True
                for u in range(len(r)-2):
                    if r[u:u+3] == 'TGA' or r[u:u+3] == 'TAG' or r[u:u+3] == 'TAA' or r[u:u+3] == 'ATG':
                        w = False
                        break
                if w == True:
                    z.append(r)
            if len(r) % 3 != 0 or w == False:
                i = a
            r = ''
            continue
        r += n[i]
    else:
        if n[i:i+3] == 'ATG':
            a = i+1
            i += 2
            t = True
    i += 1
if len(z) != 0:
    for i in z:
        print(i)
else:
    print('沒有基因')