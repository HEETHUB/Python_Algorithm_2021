from linked_list_helper import ListNode

def P4(num1: ListNode, num2: ListNode) -> ListNode: 
    ##### Write your Code Here #####
    rev_num1, rev_num2 = None, None
    # Linked List 뒤집기
    while num1:
        rev_num1, rev_num1.next, num1 = num1, rev_num1, num1.next
    while num2:
        rev_num2, rev_num2.next, num2 = num2, rev_num2, num2.next
    # 뒤집은 Linked List들끼리 덧셈
    start = rev_num1
    while rev_num1 or rev_num2:
        if rev_num1 and rev_num2:
            rev_num1.val += rev_num2.val
            if rev_num1.next:
                rev_num1, rev_num2 = rev_num1.next, rev_num2.next
            elif rev_num2.next:
                rev_num1.next = ListNode(0)
                rev_num1, rev_num2 = rev_num1.next, rev_num2.next
            else:
                rev_num1, rev_num2 = rev_num1.next, rev_num2.next
        elif rev_num1:
            rev_num1 = rev_num1.next
    rev_num1 = start
    # 자릿수 맞춰주기
    while rev_num1:
        if rev_num1.val >= 10:
            rev_num1.val -= 10
            if rev_num1.next:
                rev_num1.next.val += 1
                rev_num1 = rev_num1.next
            else:
                newNode = ListNode(1)
                rev_num1.next = newNode
                rev_num1 = rev_num1.next
        else:
            rev_num1 = rev_num1.next
    rev_num1 = start
    # 덧셈 완료된 Linked List를 다시 뒤집기
    fin_num = None
    while rev_num1:
        fin_num, fin_num.next, rev_num1 = rev_num1, fin_num, rev_num1.next
    return fin_num
    ##### End of your code #####

