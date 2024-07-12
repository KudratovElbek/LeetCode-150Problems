class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None:
        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        total = carry + x + y
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

# Misol ro'yxatlarini yaratamiz
def create_linked_list(nums):
    dummy_head = ListNode(0)
    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next

def print_linked_list(node):
    while node is not None:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

result = add_two_numbers(l1, l2)
print_linked_list(result)