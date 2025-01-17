#inorder predecessor

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

def rightmost(root):
    while root.right:
        root = root.right
    return root
    

def predecessor(root, x):
    if root is None:
        return None
    curr = root
    pred = None
    while curr is not None:
        if curr.val == x:
            if curr.left != None:
                pred = rightmost(curr.left)
                return pred
        elif curr.val > x:
            curr = curr.left
        elif curr.val < x:
            pred = curr
            curr = curr.right
        else:
            break
        return pred

def main():
    root = Node(70)
    insert(root, 100)
    insert(root, 3)
    insert(root, 150)
    insert(root, 90)
    insert(root, 98)
    insert(root, 1)
    insert(root, 69)
    insert(root, 50)
    inorder(root)
    print()
    pred = predecessor(root, 90)
    if pred:
        print("predecessor of 90 is ", pred.val)
    pred = predecessor(root, 70)
    if pred:
        print("predecessor of 70 is ", pred.val)
    pred = predecessor(root, 150)
    if pred:
        print("predecessor of 150 is ", pred.val)
    pred = predecessor(root, 1)
    if pred:
        print("predecessor of 1 is ", pred.val)
    else:
         print("predecessor not found, must be the smallest element of the tree")
    


if __name__ == "__main__":
    main()


                
                

    
