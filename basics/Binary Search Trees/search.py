class Node:
    def __init__(self, key):
        self.left= None
        self.right= None
        self.val= key

def insert(root, key):
        if root == None:
           return Node(key)
        elif root.val == key:
            return root
        elif root.val > key:
            root.left= insert(root.left, key)
        else: 
            root.right= insert(root.right, key)
        return root

def inorder(root):
         if root:
             inorder(root.left)
             print(root.val, end=" ")
             inorder(root.right)

def search(root, target):
         if root: 
             if root.val==target:
                 return True
             if root.val > target:
                 return search(root.left, target)
             if root.val < target:
                 return search(root.right, target)
              
         return False

def main():
    root = Node(50)
    insert(root,10)
    insert(root,30)
    insert (root, 75)
    insert(root, 80)
    insert(root, 15)
    bool = search(root, 75)
    print("75 found ?", bool)
    bool = search (root, 60)
    print("60 found ?", bool)
    inorder(root)
    
if(__name__=="__main__"):
    main()
    
             
