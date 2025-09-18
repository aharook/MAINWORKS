
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.val, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val, end=" ")


def treeHeight(root):
    if root is None:
        return 0
    return max(treeHeight(root.left), treeHeight(root.right)) + 1


def isBalanced(root):
    if root is None:
        return True
    
    left_h = treeHeight(root.left)
    right_h = treeHeight(root.right)
    
    if abs(left_h - right_h) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

# Підрахунок кількості листків
def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)


root = None
keys = [50, 30, 20, 40, 70, 60, 80]


for key in keys:
    root = insert(root, key)
print("In-order після вставки:")
inOrder(root)
print("\n")


print("Пошук 40:", "знайдено" if search(root, 40) else "не знайдено")
print("Пошук 90:", "знайдено" if search(root, 90) else "не знайдено", "\n")


for key in [20, 70]:
    root = deleteNode(root, key)
    print(f"Після видалення {key}:")
    inOrder(root)
    print("\n")


print("In-order:"); inOrder(root); print()
print("Pre-order:"); preOrder(root); print()
print("Post-order:"); postOrder(root); print("\n")


print("Висота дерева:", treeHeight(root))
print("Збалансоване дерево:", isBalanced(root))
print("Кількість листових вузлів:", countLeaves(root))
