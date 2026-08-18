# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        freq ={}
        curr = head
        while curr:
            address = id(curr)
            if address in freq:
                return True
            freq[address] = 1
            curr = curr.next
        return False

        