class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"<{self.data}>"


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        ptr = self.head
        counter: int = 0

        while ptr != None:
            ptr = ptr.next
            counter += 1

        return counter

    def __str__(self) -> str:
        ptr = self.head
        list_str: str = ""

        while ptr != None:
            list_str += str(ptr.data) + \
                "-->" if ptr.next != None else str(ptr.data)
            ptr = ptr.next

        return list_str

    def insert_at_beg(self, data) -> None:
        if self.head is None:
            self.head = Node(data)

        else:
            start_node = Node(data)
            start_node.next = self.head
            self.head = start_node

    def insert(self, index: int, data) -> None:
        if index < 0 or index > len(self):
            raise IndexError

        elif index == 0:
            self.insert_at_beg(data)

        else:
            node = Node(data)
            ptr = self.head

            for _ in range(index - 1):
                ptr = ptr.next

            node.next = ptr.next
            ptr.next = node

    def append(self, data) -> None:
        self.insert(len(self), data)

    def remove_beg(self) -> None:
        if self.head is None:
            print("Linked List is empty!")
            
        else:
            self.head = self.head.next

    def remove(self, index: int) -> None:
        if index < 0 or index > len(self):
            raise IndexError

        elif index == 0:
            self.remove_beg()

        else:
            ptr = self.head

            for _ in range(index - 1):
                ptr = ptr.next

            ptr.next = ptr.next.next


if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_beg(10)
    l.insert_at_beg(20)
    print(l)

    l.insert(1, 30)
    print(l)

    l.append(40)
    print(l)

    l.remove(2)
    print(l)

    l.remove_beg()
    print(l)
