inp = 12


def sum_square_of_digits(n):
    return sum([int(d) ** 2 for d in str(n)])


def has_cycle(n):
    fast, slow = n, n
    while fast != 1 and sum_square_of_digits(fast) != 1:
        slow = sum_square_of_digits(slow)
        fast = sum_square_of_digits(sum_square_of_digits(fast))

        if fast == slow:
            return True
    return False

print(str(has_cycle(inp)))