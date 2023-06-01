class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(root,data):
            if root is None:
                return BST(data)
            else:
                if root.val == data:
                    return root
                if data < root.val:
                    root.left = insert(root.left, data)
                elif data > root.val:
                    root.right = insert(root.right, data)
            return root

B = BinarySearchTree(40)
B.insert(20) 
print(B)