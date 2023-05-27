z = [1,2,3,4,5]
w = 2
while len(z) < 1500 :
    z.append(min(z[w]*2,z[w]*3,z[w]*5))
    w += 1
print(f"The 1500'th ugly number is {z[-1]}.")
# z = [1]
# r = 0
# while len(z) <= 4500:
#     a = z[r]*2
#     b = z[r]*3
#     c = z[r]*5
#     if a not in z:
#         z.append(a)
#     if b not in z:
#         z.append(b)
#     if c not in z:
#         z.append(c)
#     r += 1
#     z.sort()
# print(z)
# print(f"The 1500'th ugly number is {z[1499]}.")