string = "odicf"
pattern = "dc"

dict_pattern = {}

for c in pattern:
    if c not in dict_pattern:
        dict_pattern[c] = 0
    dict_pattern[c] += 1

window_start = 0
dict_str = dict_pattern
found = False
for window_end in range(len(string)):
    if string[window_end] in dict_pattern:
        dict_str[string[window_end]] -= 1
        if sum(dict_str.values()) == 0:
            found = True
            break
    else:
        while window_start != window_end:
            if string[window_start] in dict_pattern:
                dict_str[string[window_start]] += 1
            window_start += 1

print(found)