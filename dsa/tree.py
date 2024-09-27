class TreeNode():
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        pass

class BinaryTree():
    def __init__(self, root) -> None:
        self.root = root
        
    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.value)

    def preOrder(self, root):

        print(root.value)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        self.inOrder(root.left)
        print(root.value)
        self.inOrder(root.right)
    def initTree(self, root):


        pass
    def invertTree(self, root):
        #switch the child nodes with each other
        #create temp node pointer
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)


        return root
    
    def insertNode(self, root):
        pass


    
def maxDepth(root) -> int:
    if root is None:
        return 0

    return  1 + max(maxDepth(root.left), maxDepth(root.right))


def isSameTree(p, q) -> bool:
    #dfs on every node check if the vals are the same
    #base case is if left and right are null
    if not p and not q:
        return True
    if not p or not q or p.val!=q.val:
        return False
    
    return (
    isSameTree(p.left, q.left)
    and
    isSameTree(p.right, q.right))


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #have pointer to the root node to check for lca
    cur = root 
    #check casses if the values are less than or greater than the root node 

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur
    pass


def isBalanced(root: TreeNode)->bool:
    def dfs(root):
        if root is None:
            return 0
        
        return 1 + dfs(root.right) + dfs(root.left)
    
    l1 = dfs(root.left)
    l2 = dfs(root.right)
    
    res = l1 - l2
    abs(res)

    pass

def searchBST(root, val):
    if not root:
        return None
    
    if root.val ==val:
        return root
    
    searchBST(root.right)
    searchBST(root.left)
    pass

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def dfs(root1, root2):
            
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val!=root2.val:
                return False
            
            return dfs(root1.right, root2.left) and dfs(root1.left, root2.right)
        
        return dfs(root.left, root.right)
        
