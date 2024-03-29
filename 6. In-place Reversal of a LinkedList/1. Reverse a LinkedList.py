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


def reverse(head):
    prev, curr, temp_next = None, head, None
    while curr is not None:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("original: ", end='')
    head.print_list()
    result = reverse(head)
    print("reverse:  ", end='')
    result.print_list()


main()
