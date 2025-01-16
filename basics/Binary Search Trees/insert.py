class Node:
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.val = key

def insert(root,key):
    if root == None:
        return Node(key)
    elif root.val == key:
        return root 
    elif root.val<key:
        root.right= insert(root.right, key)
    else:
        root.left= insert(root.left, key) 
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
    
def main():
    root = Node(50)
    insert(root, 35)
    insert(root,97) 
    insert(root,10)
    insert(root,20)
    insert(root,65)
    inorder(root)


if __name__=="__main__":
    main()
