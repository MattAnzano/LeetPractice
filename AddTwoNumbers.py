# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        resultNode = ListNode()
        digitSum = 0
        carry = False
        while(node1.next != None and node2.next != None):
            if node1 != None:
                value1 = node1.val
            else:
                value1 = 0
            if node2 != None:
                value2 = node2.val
            else:
                value2 = 0
            digitSum = value1 + value2
            if digitSum > 9:
                carry = True
                digit = (digitSum % 10) + 1
            else:
                carry = False
                digit = digitSum % 10
                
            resultNode.val = digit
            resultNode.next = ListNode()
            
            node1 = node1.next
            node2 = node2.next
            
        return resultNode
