class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def levelOrder(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.info, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# ==========================
# EJEMPLO
# ==========================

tree = BinarySearchTree()

# Valores que se insertarán en el BST
values = [4, 2, 7, 1, 3, 6, 9]

for value in values:
    tree.create(value)

print("Recorrido Level Order:")
levelOrder(tree.root)