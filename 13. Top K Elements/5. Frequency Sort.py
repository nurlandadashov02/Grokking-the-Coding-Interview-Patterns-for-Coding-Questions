from heapq import *

# O(N + DlogD)
def frequencySort(s):
    char_freq = {}
    # O(N)
    for c in s:
        if c not in char_freq:
            char_freq[c] = 0
        char_freq[c] += 1

    # O(DlogD)
    maxHeap = [(-freq, char) for char, freq in list(char_freq.items())]
    heapify(maxHeap)

    res = ""

    # O(D)
    while maxHeap:
        freq, char = heappop(maxHeap)
        res += char * (-freq)

    return res

print(frequencySort("tree"))