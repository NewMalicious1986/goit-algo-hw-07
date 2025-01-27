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

def tree_sum(root):
    if not root:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

# Test
root = Node(5)
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)

total_sum = tree_sum(root)
print(f"Сума всіх значень у дереві: {total_sum}")
