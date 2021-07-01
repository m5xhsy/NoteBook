class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, li):
        self.root = None
        if li:
            for val in li:
                self.insert(val)

    def insert(self, key):
        if not self.root:
            self.root = BiTreeNode(key)
        else:
            p = self.root
            while p:
                if key < p.data:
                    if p.lchild:
                        p = p.lchild
                    else:
                        p.lchild = BiTreeNode(key)
                        break
                elif key > p.data:
                    if p.rchild:
                        p = p.rchild
                    else:
                        p.rchild = BiTreeNode(key)
                        break
                else:
                    print(f"已经存在{p.data}")
                    break

    def traverse(self):
        li = []

        def pre_order(root):
            if root:
                pre_order(root.lchild)
                li.append(root.data)
                pre_order(root.rchild)

        pre_order(self.root)
        return li

    def query(self, key):
        p = self.root
        while p:
            if key > p.data:
                p = p.rchild
            elif key < p.data:
                p = p.lchild
            else:
                return p


e = BST([5, 4, 6, 8, 7, 16, 9, 2, 3, 10])

print(e.traverse())
print(e.query(5), e.query(5).data)


