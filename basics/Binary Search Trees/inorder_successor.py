#inorder successor

class Node:
    def __init__(self, key):
        self.val= key
        self.left= None
        self.right= None
        
def insert(root, x):
    if root is None:
        return Node(x)
    elif root.val == x:
        return root
    elif root.val > x:
       root.left = insert(root.left, x)
    elif root.val < x:
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
    return root

def successor(root, x):
    if root is None:
        return None
    
    suc = None
    curr= root
    while curr is not None:
        if curr.val == x:
            if curr.right:
                suc = leftmost(curr.right)
                return suc
            
        if curr.val > x:
            suc = curr
            curr = curr.left
            
        elif curr.val < x:
            curr = curr.right

        else:
            break
        

    return suc     
            

def main():
    root = Node(80)
    insert(root, 500)
    insert(root, 400)
    insert(root, 600)
    insert(root, 650)
    insert(root, 300)
    insert(root, 200)
    insert(root, 350)
    insert(root, 450)
    insert(root, 625)
    insert(root, 700)
    inorder(root)
    print()
    s = successor(root, 400)
    print("successor of 400 is ",s.val)
    s = successor(root, 350)
    print("successor of 350 is ",s.val)
    s = successor(root, 625)
    print("successor of 625 is ",s.val)
    s = successor(root, 80)
    print("successor of 80 is ",s.val)
    s = successor(root, 600)
    print("successor of 600 is ",s.val)

if __name__=="__main__":
    main()
