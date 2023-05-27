# a = int(input())
# maze = []
# arr = [[1,1]]
# for _ in range(a):
#     n = input()
#     t = []
#     for _ in n:
#         if _ == "#":t.append(-1)
#         else:t.append(0)
#     maze.append(t)
# i = 1
# maze[1][1] = i
# temhile True:
#     i += 1
#     tem = []
#     for u in arr :
#         if maze[u[0]+1][u[1]] == 0 or maze[u[0]+1][u[1]] > maze[u[0]][u[1]]+1 and maze[u[0]+1][u[1]] != -1:
#             maze[u[0]+1][u[1]] = i
#             tem.append([u[0]+1,u[1]])
#         if maze[u[0]][u[1]+1] == 0 or maze[u[0]][u[1]+1] > maze[u[0]][u[1]]+1 and maze[u[0]][u[1]+1] != -1:
#             maze[u[0]][u[1]+1] = i
#             tem.append([u[0],u[1]+1])
#         if maze[u[0]][u[1]-1] == 0 or maze[u[0]][u[1]-1] > maze[u[0]][u[1]]+1 and maze[u[0]][u[1]-1] != -1:
#             maze[u[0]][u[1]-1] = i
#             tem.append([u[0],u[1]-1])
#         if maze[u[0]-1][u[1]] == 0 or maze[u[0]-1][u[1]] > maze[u[0]][u[1]]+1 and maze[u[0]-1][u[1]] != -1:
#             maze[u[0]-1][u[1]] = i
#             tem.append([u[0]-1,u[1]])
#     arr = tem
#     for r in maze:
#         print(r)
#     print()
#     if arr == []:
#         break
# if maze[a-2][a-2] == 0:print('No solution!')
# else:print(maze[a-2][a-2])
# 9
# #########
# #.......#
# #.#####.#
# #.......#
# ##.#.####
# #..#.#..#
# #.##.##.#
# #.......#
# #########
a = int(input())
n = [int(_)-1 for _ in input().split()]#x0 = n[0],y0 = n[1],x1 = n[2],y1 = n[3]
maze = []
arr = [[n[0],n[1]]]
for _ in range(a):
    p = input()
    t = []
    for _ in p:
        if _ == "#":t.append(-1)
        else:t.append(0)
    maze.append(t)
i = 0
maze[n[0]][n[1]] = i
while True:
    i += 1
    tem = []
    for u in arr :
        if maze[u[0]+1][u[1]] == 0 or maze[u[0]+1][u[1]] > maze[u[0]][u[1]]+1 and maze[u[0]+1][u[1]] != -1:
            maze[u[0]+1][u[1]] = i
            tem.append([u[0]+1,u[1]])
        if maze[u[0]][u[1]+1] == 0 or maze[u[0]][u[1]+1] > maze[u[0]][u[1]]+1 and maze[u[0]][u[1]+1] != -1:
            maze[u[0]][u[1]+1] = i
            tem.append([u[0],u[1]+1])
        if maze[u[0]][u[1]-1] == 0 or maze[u[0]][u[1]-1] > maze[u[0]][u[1]]+1 and maze[u[0]][u[1]-1] != -1:
            maze[u[0]][u[1]-1] = i
            tem.append([u[0],u[1]-1])
        if maze[u[0]-1][u[1]] == 0 or maze[u[0]-1][u[1]] > maze[u[0]][u[1]]+1 and maze[u[0]-1][u[1]] != -1:
            maze[u[0]-1][u[1]] = i
            tem.append([u[0]-1,u[1]])
    arr = tem
    if arr == []:
        break
if n[0] != n[2] and n[1] != n[3] and maze[n[2]][n[3]] == 0:print('No solution!')
else:print(maze[n[2]][n[3]])
