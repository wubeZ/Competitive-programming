def removeDuplicates(llist):
    pointer = llist
    while(pointer.next):
        if pointer.data == pointer.next.data:
            temp = pointer.next
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next
    return llist
    