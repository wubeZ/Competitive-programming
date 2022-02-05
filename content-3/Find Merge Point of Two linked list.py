def findMergeNode(head1, head2):
    seen = set()
    while(head1):
        seen.add(head1)
        head1 = head1.next
        
    while(head2):
        if head2 in seen:
            return head2.data
        head2 = head2.next