nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for sub_list in nested_list:
    for element in sub_list:
        print(element, end=' ')
    print()