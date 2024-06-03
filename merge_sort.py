def sorted_merge(arr1: list[int], arr2: list[int]) -> list[int]:
    sorted_array: list[int] = []
    i: int = 0
    j: int = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_array.append(arr1[i])
            i += 1

        else:
            sorted_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1

    return sorted_array


def merge_sort(my_list: list[int]) -> list[int]:
    if len(my_list) <= 1:
        return my_list

    mid_index: int = len(my_list) // 2
    left: list[int] = my_list[:mid_index]
    right: list[int] = my_list[mid_index:]

    sorted_left: list[int] = merge_sort(left)
    sorted_right: list[int] = merge_sort(right)

    return sorted_merge(sorted_left, sorted_right)


if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]

    a1 = [14, 19, 21]
    a2 = [17, 18]

    print(sorted_merge(a1, a2))
