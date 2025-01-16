class Node:
    def __init__(self, key):
        self.val= key
        self.left= None
        self.right= None

def find_ceil(root, x):
    if root is None:
        return -1
    if root.val==x:
        return x
    if root.val > x:
        ceil_val= find_ceil(root.left, x)
    elif root.val < x :
        ceil_val= find_ceil(root.right, x)

    return ceil_val if ceil_val >= x and ceil_val != -1 else root.val

def find_floor(root, x):
    if root is None:
        return -1
    if root.val == x:
        return root.val
    elif root.val > x:
        floor_val = find_floor(root.left, x)
    elif root.val < x:
        floor_val = find_floor(root.right, x)
    return floor_val if floor_val <= x and floor_val != -1 else root.val 

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



            
def main():
    root= Node(50)
    insert(root, 60)
    insert(root, 70)
    insert(root, 100)
    insert(root, 80)
    insert(root, 120)
    insert(root, 110)
    insert(root, 150)
    inorder(root)
    print()
    ceil_is = find_ceil(root, 150)
    print("ceil of 150 is ", ceil_is)
    ceil_is = find_ceil(root, 105)
    print("ceil of 105 is ", ceil_is)

    floor_is = find_floor(root, 90)
    print("floor of 90 is ", floor_is)
    floor_is = find_floor(root, 80)
    print("floor of 80 is ", floor_is)
    

if __name__=="__main__":
    main()
