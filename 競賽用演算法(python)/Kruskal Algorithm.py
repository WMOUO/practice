from queue import PriorityQueue
pq = PriorityQueue()
n = int(input())
went = []
num = [float('inf')]*(n)
node = 0
i = 0
cost = 0
while True:
    p = [int(_) for _ in input().split(' ') if _]
    if len(p) == 1:
        break
    pq.put(tuple(p))
while n > 0:
    r = pq.get()
    if num[r[1]] == num[r[2]] != float('inf'):
        continue
    else:
        cost += r[0]
        if num[r[1]] == num[r[2]] == float('inf'):
            went.append({r[1],r[2]})
            num[r[1]],num[r[2]] = i,i
            i += 1
            if i == 1:
                node += 2
        elif num[r[1]] != num[r[2]]:
            if num[r[1]] < num[r[2]] :
                if num[r[2]] == float('inf'):
                    node += 1
                    went[num[r[1]]].add(r[2])
                    num[r[2]] = num[r[1]]
                else:
                    went[num[r[1]]] |= went[num[r[2]]]
                    if num[r[1]] == 0:
                        node += len(went[num[r[2]]])
                    for u in went[num[r[2]]]:
                        num[u] = num[r[1]]
            else:
                if num[r[1]] == float('inf'):
                    node += 1
                    went[num[r[2]]].add(r[1])
                    num[r[1]] = num[r[2]]
                else:
                    went[num[r[2]]] |= went[num[r[1]]]
                    if num[r[2]] == 0:
                        node += len(went[num[r[1]]])
                    for u in went[num[r[1]]]:
                        num[u] = num[r[2]]
    if node == n:
        break
print(cost)
#5
#1 0 1
#1 1 2
#1 2 3
#2 3 4
#1 2 4
#0

#5
#1 0 4
#1 0 1
#1 2 3
#1 2 4
#2 2 4
#0

#5
#1 0 4
#3 0 1
#4 1 4
#5 1 2
#6 2 4
#2 2 3
#7 3 4
#0