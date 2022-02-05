class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = list1
        spointer = list2
        head = ListNode()
        npointer = head
        
        while(pointer or spointer):
            if not pointer:
                npointer.next = spointer
                return self.deletefront(head)
                
            elif not spointer:
                npointer.next = pointer
                return self.deletefront(head)
            
            if pointer.val <= spointer.val:
                npointer.next = pointer
                npointer = npointer.next
                pointer = pointer.next
                
            else:
                npointer.next = spointer
                npointer = npointer.next
                spointer = spointer.next
                
        return self.deletefront(head)
    
    def deletefront(self, head):
        if head != None:
            temp = head
            head = head.next
            temp = None
        return head