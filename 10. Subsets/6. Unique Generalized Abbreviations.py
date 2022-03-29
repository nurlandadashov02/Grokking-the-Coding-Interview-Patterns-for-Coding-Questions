def substrings(s):
    res = ["", s[0]]
    start = 1
    for c in s[1:]:
        n = len(res)
        res.append(c)
        for i in range(start, n):
            res.append(res[i] + c)

        start += n - start

    return res

def generalized_abbreviations(word):
    result = [" ", word]
    subs = substrings(word)
    for s1 in range(1, len(subs)):
        sub1 = subs[s1]
        result.append(word.replace(sub1, str(len(sub1))))
        for s2 in range(s1 + 1, len(subs)):
            sub2 = subs[s2]
            if not sub2.find(sub1):
                result.append(word.replace(sub1, str(len(sub1))).replace(sub2, str(len(sub2))))

    return result

print(generalized_abbreviations("word"))