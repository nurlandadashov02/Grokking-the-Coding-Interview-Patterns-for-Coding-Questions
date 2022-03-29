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


def cycle_start(head):
    p1, p2 = head, head
    k = cycle_length(head)

    for _ in range(k):
        p2 = p2.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print(str(cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print(str(cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print(str(cycle_start(head).value))


main()
