class QueueElement:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"<{self.data}>"


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head

    def __str__(self) -> str:
        ptr = self.head
        list_str: str = ""

        while ptr:
            list_str += str(ptr.data) + \
                "-->" if ptr.next else str(ptr.data)
            ptr = ptr.next

        return list_str

    def enqueue(self, data) -> None:
        if self.head is None:
            self.head = QueueElement(data)
            self.tail = self.head

        else:
            new_node = QueueElement(data)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> None:
        if self.head is None:
            print("Queue is empty!")

        else:
            self.head = self.head.next


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
