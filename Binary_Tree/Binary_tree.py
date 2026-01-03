class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(root.data,end=" --> ")
            self.inorder(root.right)
    def preorder(self,root): 
        if(root):
            print(root.data,end=" --> ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" --> ")
    def max_depth(self, root):
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return 1 + max(left_depth, right_depth)

root=Node(12)
root.left=Node(14)
root.right=Node(20)
root.left.right=Node(25)
root.left.left=Node(30)
root.right.right=Node(21)
root.right.left=Node(32)
root.inorder(root)
print()
root.postorder(root)
print()
root.preorder(root)
print()
print("maximum depth of the binary tree is " , root.max_depth(root))