inp = [2, 3, 3, 3, 6, 9, 9]

nextNonDuplicate = 1

for next in range(1, len(inp)):
    if inp[next] != inp[nextNonDuplicate - 1]:
        inp[nextNonDuplicate] = inp[next]
        nextNonDuplicate += 1

print(nextNonDuplicate)
