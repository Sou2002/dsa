def selection_sort(my_list: list[int]) -> None:
    for i in range(len(my_list) - 1):
        min_ele: int = my_list[i]
        for j in range(i + 1, len(my_list)):
            if my_list[j] < min_ele:
                min_ele = my_list[j]
                my_list[i], my_list[j] = my_list[j], my_list[i]


if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    selection_sort(l)
    print(l)
