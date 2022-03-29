class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def middle(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(str(middle(head).value))

    head.next.next.next.next.next = Node(6)
    print(str(middle(head).value))

    head.next.next.next.next.next.next = Node(7)
    print(str(middle(head).value))


main()
