def binary_search(my_list: list[int], val: int, left_index: int, right_index: int) -> int:
    my_list.sort()

    if left_index > right_index:
        return -1

    mid_index: int = (left_index + right_index) // 2

    if my_list[mid_index] == val:
        return mid_index
    
    elif my_list[mid_index] > val:
        right_index = mid_index - 1
    
    elif my_list[mid_index] < val:
        left_index = mid_index + 1

    return binary_search(my_list, val, left_index, right_index)
    

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(l, 12, 0, len(l) - 1))