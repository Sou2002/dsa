def bubble_sort(my_list: list[int]) -> None:
    flag: bool = True
    for _ in range(len(my_list) - 1):
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                flag: bool = False

        if flag:
            print("The list is already sorted!")
            break



if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    bubble_sort(l)
    print(l)