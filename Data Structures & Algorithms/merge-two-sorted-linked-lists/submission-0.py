# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = node = ListNode()

        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        curr1 = list1
        curr2 = list2

        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                node.next = curr1
                curr1 = curr1.next
                node = node.next
            else:
                node.next = curr2
                curr2 = curr2.next
                node = node.next
        if curr1 == None:
            node.next = curr2
        if curr2 == None: 
            node.next = curr1

        return temp.next    
