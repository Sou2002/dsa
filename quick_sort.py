def partition(my_list: list[int], start_index: int, end_index: int) -> int:
    pivot_index: int = start_index
    pivot: int = my_list[pivot_index]

    while start_index < end_index:
        while start_index < len(my_list) and pivot >= my_list[start_index]:
            start_index += 1

        while pivot < my_list[end_index]:
            end_index -= 1

        if start_index < end_index:
            my_list[start_index], my_list[end_index] = my_list[end_index], my_list[start_index]

    my_list[pivot_index], my_list[end_index] = my_list[end_index], my_list[pivot_index]

    return end_index

def quick_sort(my_list: list[int], start_index: int, end_index: int) -> None:
    if start_index < end_index:
        partition_index: int = partition(my_list, start_index, end_index)
        quick_sort(my_list, start_index, partition_index - 1)
        quick_sort(my_list, partition_index + 1, end_index)

if __name__ == '__main__':
    l = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(l, 0, len(l) - 1)
    print(l)