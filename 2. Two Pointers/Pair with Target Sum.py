inp = [2, 5, 9, 11]
target = 11

a = 0
b = len(inp) - 1

while a < b:
    if inp[a] + inp[b] > target:
        b -= 1
    elif inp[a] + inp[b] < target:
        a += 1
    else:
        break

print([a, b])
