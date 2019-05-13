# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        p, q = l1, l2
        carry = 0
        while p or q:
            value = carry
            if p:
                value += p.val
                p = p.next
            if q:
                value += q.val
                q = q.next
            carry = value // 10
            curr.next = ListNode(value%10)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(1)
        return dummy.next
            
                
            
        