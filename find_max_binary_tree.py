class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.val

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 500)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 100500)

max_value = find_max(root)
if max_value is not None:
    print(f"Найбільше значення в дереві: {max_value}")
else:
    print("Дерево порожнє")
