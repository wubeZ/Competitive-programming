def has_cycle(head):
    seen = set()
    
    if head == None:
        return 0
    
    while(head.next):
        if head in seen:
            return 1
        seen.add(head)
        head = head.next
        
    return 0