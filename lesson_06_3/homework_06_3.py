lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', "", set]

for element in lst1:
    lst2 = []
    if type(element) == str:
        lst2.append(element)
        print(lst2)