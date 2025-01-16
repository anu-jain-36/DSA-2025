# minimum/max element in a BST
# print BST in ascending/descending order

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def min(root):
    while root:
        min = root.val
        root = root.left
    return min

def max(root):
    while root:
        max= root.val
        root = root.right
    return max

def ascend(root):
    if root:
        ascend(root.left)
        print(root.val, end = " ")
        ascend(root.right)

def descend(root):
    if root:
        descend(root.right)
        print(root.val, end = " ")
        descend(root.left)

def insert(root, x):
    if root is None:
        return Node(x)
    elif root.val == x:
        return root
    elif root.val > x:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root
    

def main():
    root = Node(150)
    insert(root, 60)
    insert(root, 200)
    insert(root, 80)
    insert(root, 90)
    insert(root, 200)
    insert(root, 70)
    ascend(root)
    print()
    descend(root)
    print()
    mini = min(root)
    print("Minimum value is", mini)
    maxi = max(root)
    print("Maximum value is", maxi)

if __name__ == "__main__":
    main()
        
