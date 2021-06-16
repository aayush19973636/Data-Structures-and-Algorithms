def length(head):
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count

def deleteNode(head, pos):
    if pos < 0 or pos > length(head):
        return head
    
    if head is None: 
        return head
    if pos == 0:
        return head.next
    
    current = head
    prev = None
    count = 0

    while count < pos:
        prev = current
        current = current.next
        count += 1

    if prev.next == None:
        return head
    if prev is not None:
        nextNode = current.next
        prev.next = nextNode
    else:
        head = head.next
        return head
    
    return head

