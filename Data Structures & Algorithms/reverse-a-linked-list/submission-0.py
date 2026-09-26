# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        reverseListHead = head
        previousNode = None
        while head != None:
            reverseListHead = ListNode(head.val, previousNode)
            previousNode = reverseListHead
            head = head.next

        return reverseListHead