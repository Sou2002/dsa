class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.children: list[Tree] = []
        self.parent = None

    def get_level(self) -> int:
        level: int = 0
        while self.parent != None:
            self = self.parent
            level += 1
        return level

    def dfs(self) -> None:
        spaces: str = " " * self.get_level() * 3
        prefix_str: str = spaces + "|__" if self.get_level() else ""
        print(prefix_str + self.data)
        for trees in self.children:
            trees.dfs()

    def add_child(self, trees) -> None:
        trees.parent = self
        self.children.append(trees)


if __name__ == '__main__':
    root = Tree("A")

    b = Tree("B")
    b.add_child(Tree("E"))
    f = Tree("F")
    b.add_child(f)
    f.add_child(Tree("G"))

    c = Tree("C")
    d = Tree("D")

    root.add_child(b)
    root.add_child(c)
    root.add_child(d)

    root.dfs()