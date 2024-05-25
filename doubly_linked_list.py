class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f"<{self.data}>"


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        ptr = self.head
        counter: int = 0

        while ptr:
            ptr = ptr.next
            counter += 1

        return counter

    def __str__(self) -> str:
        ptr = self.head
        list_str: str = ""

        while ptr:
            list_str += str(ptr.data) + \
                "<-->" if ptr.next else str(ptr.data)
            ptr = ptr.next

        return list_str

    def insert_at_beg(self, data) -> None:
        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, index: int, data) -> None:
        if index < 0 or index > len(self):
            raise IndexError

        elif index == 0:
            self.insert_at_beg(data)

        else:
            new_node = Node(data)
            ptr = self.head

            for _ in range(index - 1):
                ptr = ptr.next

            new_node.next = ptr.next
            ptr.next = new_node

            if new_node.next:
                ptr = new_node.next
                new_node.prev = ptr.prev
                ptr.prev = new_node

    def append(self, data) -> None:
        self.insert(len(self), data)

    def remove_beg(self) -> None:
        if self.head is None:
            print("Linked List is empty!")
            
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove(self, index: int) -> None:
        if index < 0 or index > len(self):
            raise IndexError

        elif index == 0:
            self.remove_beg()

        else:
            ptr = self.head

            for _ in range(index - 1):
                ptr = ptr.next

            if ptr.next.next is None:
                ptr.next.prev = None
                ptr.next = None

            else:
                ptr.next = ptr.next.next
                ptr.next.prev = ptr


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.insert_at_beg(10)
    l.insert_at_beg(20)
    print(l)

    l.insert(1, 30)
    print(l)

    l.append(40)
    print(l)

    l.remove(3)
    print(l)

    l.remove_beg()
    print(l)
