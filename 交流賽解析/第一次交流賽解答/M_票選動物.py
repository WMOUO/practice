# #1
# z = [0,0]
# for _ in range(9):
#     n = input()
#     if n == 'Tiger':
#         z[0] += 1
#     elif n == 'Lion':
#         z[1] += 1
# if z[0] > z[1]:
#     print('Tiger')
# else:
#     print('Lion')
# 要不要做Counter代思考 待啦幹

###
from collections import Counter
print(max(Counter([input() for i in range(9)]).items(), key=lambda x: x[1])[0])
