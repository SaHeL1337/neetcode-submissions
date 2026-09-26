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
            reverseListHead = head
            nextElement = head.next
            reverseListHead.next = previousNode
            previousNode = reverseListHead
            head = nextElement

        return reverseListHead