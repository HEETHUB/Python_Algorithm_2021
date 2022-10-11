"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import *

def P3(head: ListNode) -> ListNode: 
    ##### Write your Code Here #####
    rev_head = None
    while head:
        rev_head, rev_head.next, head = head, rev_head, head.next
    return rev_head
    ##### End of your code #####
