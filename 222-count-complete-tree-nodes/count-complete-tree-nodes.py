# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        count=1
        while q:
          for _ in range(len(q)):
             node=q.popleft()
             if node.left:
                q.append(node.left)
                count+=1
             if node.right:
                q.append(node.right)
                count+=1
        return count




        
        