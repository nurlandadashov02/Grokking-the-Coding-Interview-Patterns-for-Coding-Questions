class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def cycle_length(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print(str(cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print(str(cycle_length(head)))


main()
