class StackElement:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"<{self.data}>"


class Stack:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        ptr = self.head
        list_str: str = ""

        while ptr:
            list_str += str(ptr.data) + \
                "-->" if ptr.next else str(ptr.data)
            ptr = ptr.next

        return list_str

    def peek(self):
        return self.head.data

    def push(self, data) -> None:
        if self.head is None:
            self.head = StackElement(data)

        else:
            start_node = StackElement(data)
            start_node.next = self.head
            self.head = start_node

    def pop(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            popped_element = self.head.data
            self.head = self.head.next
            return popped_element


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())
    print(s)
    print(s.pop())
    print(s)
