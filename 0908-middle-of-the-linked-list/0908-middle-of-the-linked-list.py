# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None 
        temp=head
        count=1 
        while temp.next !=None:
            temp=temp.next
            count+=1
        print(count)
        slow=head
        fast=head
        

        while fast.next !=None and fast.next.next!=None:
            # print(fast.next)
            
            slow=slow.next
            fast=fast.next.next
        if count%2==0:
            return slow.next
        return slow