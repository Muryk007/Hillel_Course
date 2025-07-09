my_lst =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10, 11, 12, 13, 14, 15]
duplicates = []

# for item in my_lst:
#         if my_lst.count(item) > 1:
#                 duplicates.append(item)

for item in my_lst:
        if item % 2 == 0:
            duplicates.append(item)

print("Сума усіх парних чисел =", sum(duplicates))
