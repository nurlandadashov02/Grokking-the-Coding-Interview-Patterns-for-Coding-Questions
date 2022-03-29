class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    count = 1
    temp = head
    while count < p - 1:
        temp = temp.next
        count += 1

    count2 = count

    prev, curr, temp_next = None, temp.next, None
    while count < q and curr is not None:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
        count += 1

    temp.next = prev

    temp2 = prev
    while count2 < q - 1:
        temp2 = temp2.next
        count2 += 1

    temp2.next = curr
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("original: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("reverse:  ", end='')
    result.print_list()


main()
