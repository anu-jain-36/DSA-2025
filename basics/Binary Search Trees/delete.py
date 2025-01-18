#delete a node

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
        
def leftmost(root):
    while root.left:
        root = root.left
    return root.val

def delete(root, x):
    if root is None:
        return root
    if root.val > x:
        root.left = delete(root.left, x)
    elif root.val < x:
        root.right = delete(root.right, x)
    else:
        if root.left == None and root.right == None:
            return None
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = leftmost(root.right)
            root.val = succ
            root.right = delete(root.right, succ)
    return root
        

def main():
    root = Node(70)
    insert(root, 100)
    insert(root, 150)
    insert(root, 90)
    insert(root, 80)
    insert(root, 98)
    insert(root, 3)
    insert(root, 1)
    insert(root, 69)
    insert(root, 50)
    inorder(root)
    print()
    delete(root, 70)
    inorder(root)
    print()
    delete(root, 69)
    inorder(root)
    print()
    delete(root, 80)
    inorder(root)
    print()
    delete(root, 98)
    inorder(root)
    print()
    delete(root, 100)
    inorder(root)
    print()



if __name__=="__main__":
     main()
