1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        a=head
9        while a and a.next:
10            if a.val==a.next.val:
11                a.next=a.next.next
12            else:
13                a=a.next
14        return head