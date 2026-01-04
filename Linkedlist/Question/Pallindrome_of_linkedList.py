'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

'''

# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next 
            fast = fast.next.next
        second = self.reverseList(slow.next)

        first = head
        new_head = second

        while(new_head != None):
            if (first.val != new_head.val):
                self.reverseList(second)
                return False
            first = first.next
            new_head = new_head.next

        self.reverseList(second)
        return True