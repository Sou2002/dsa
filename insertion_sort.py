def insertion_sort(my_list: list[int]) -> None:
    for i in range(1, len(my_list)):
        anchor: int = my_list[i]
        for j in range(i - 1, -1, -1):
            if anchor < my_list[j]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    insertion_sort(l)
    print(l)