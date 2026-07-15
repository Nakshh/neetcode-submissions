# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        end = head
        for i in range(n):
            end = end.next
        
        prev = None
        while end:
            prev = node
            node = node.next
            end = end.next
        if prev:
            prev.next = node.next
        else:
            head = node.next
        


        return head