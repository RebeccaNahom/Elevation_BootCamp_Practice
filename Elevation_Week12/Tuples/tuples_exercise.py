from numpy import *

# nums_tuples = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(nums_tuples[::2])
# for i in nums_tuples:
#     if nums_tuples[i] % 2 == 0:
#         print(nums_tuples[i])

# exercise 1+2:
# my_tuple = (1, "Rebecca", 4.5, [5, 3, 2], True, {"first": "R", "last":"N"}, 7, "t")
# print(my_tuple[3], my_tuple[-4])

# exercise 3:
# days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
# days = days[:2] + days[3:]
# print(days)

# exercise 4:
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(numbers[::-1])

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for b in board:
    for a in b:
        print(" | " , a, end= " ")
    print(" |")

# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# for r in T:
#     for c in r:
#         print(c,end = " ")
#     print()