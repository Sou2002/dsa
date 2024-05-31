class BinarySearchTree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: int) -> None:
        if self.data == data:
            print("Node already exist!")
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self) -> list[int]:
        elements: list[int] = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find(self, data: int) -> bool:
        if self.data == data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def find_min(self) -> int:
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val: int) -> None:
        if self.data > val:
            if self.left:
                self.left = self.left.delete(val)
        elif self.data < val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


if __name__ == '__main__':
    bst = BinarySearchTree(10)
    data_list = [15, 20, 5, 2, 8]
    for elements in data_list:
        bst.insert(elements)

    print(bst.in_order_traversal())
    print(bst.find(2))
    print(bst.find(12))
    print(bst.find_min())

    bst.delete(5)
    print(bst.in_order_traversal())
