fruit = ['A', 'B', 'C', 'B', 'B', 'C']

window_start = 0
max_num = 0
tree = {}

for window_end in range(len(fruit)):
    if fruit[window_end] not in tree:
        tree[fruit[window_end]] = 1
    else:
        tree[fruit[window_end]] += 1

    while len(tree) > 2:
        tree[fruit[window_start]] -= 1
        if tree[fruit[window_start]] == 0:
            del tree[fruit[window_start]]
        window_start += 1

    max_num = max(max_num, window_end - window_start + 1)

print(max_num)
