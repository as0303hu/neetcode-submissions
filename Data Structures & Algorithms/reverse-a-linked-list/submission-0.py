# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        rev = None
        while last:
            new_nod =ListNode(last.val)
            new_nod.next = rev
            rev = new_nod
            last = last.next
        return rev
            



        