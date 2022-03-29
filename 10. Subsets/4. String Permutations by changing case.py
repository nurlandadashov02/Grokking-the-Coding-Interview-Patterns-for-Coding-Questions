s = "a1b2"

res = [""]

for c in s:
    if c.isalpha():
        length = len(res)
        for i in range(length):
            res.append(res[i] + c.upper())
            res[i] += c.lower()
    else:
        length = len(res)
        for i in range(length):
            res[i] += c

print(res)