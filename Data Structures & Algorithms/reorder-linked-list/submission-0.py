# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of list
        slow_ptr = head
        fast_ptr = head.next

        # when fast ptr reaches end, slow reaches midpoint 
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # reverse second half of list
        second_half = slow_ptr.next
        prev = slow_ptr.next = None
        
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        
        # merge two halves of list
        first_half = head
        second_half = prev

        while second_half:
            temp1 = first_half.next 
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2

        