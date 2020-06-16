class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def EntryNodeOfLoop(pHead):
    if pHead is None: return None
    fast, slow = pHead
    while True:
        if fast.next is None or fast.next.next is None:
            return None
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    fast = pHead
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast       


if __name__ == "__main__":
    list_nodes =[ListNode(i) for i in range(1, 8)]
    for index in range(len(list_nodes) - 1):
        list_nodes[index].next = list_nodes[index+1]
    
    print(EntryNodeOfLoop(list_nodes[0]).val)

