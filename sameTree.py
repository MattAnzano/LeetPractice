# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer1 = []
        answer2 = []
        self.helperFunction(p, q, answer1, answer2)
        
        for i in range(len(answer1)):
            if answer1[i] != answer2[i]:
                return False   
        return True
    
    
    def helperFunction(self, p, q, answer1, answer2):
        if p != None and q != None:
            self.helperFunction(p.left, q.left, answer1, answer2)
            answer1.append(p.val)
            answer2.append(q.val)
            self.helperFunction(p.right, q.right, answer1, answer2)
