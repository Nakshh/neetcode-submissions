# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        ## Merging
        if list1.val <= list2.val:
            A, B = list1, list2
        else:
            A, B = list2, list1

        while A:
            if A.next and B:
                if A.next.val <= B.val:
                    A = A.next
                else:
                    temp = A.next
                    A.next = B
                    B = B.next
                    A.next.next = temp
            elif B:
                A.next = B
                break
            else:
                break


        return min(list1, list2, key=lambda node: node.val)
