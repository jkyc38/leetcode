# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initialize q
        if not root: #empty case
            return []
        q = deque()
        q.append(root)
        ret = []
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen): #loops through the current level cuz qlen keeps track of how many leaves are at the level

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ret.append(level)
        
        return ret

                
            
