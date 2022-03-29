from collections import deque

class PStr:
   def __init__(self, s, openC, closedC):
    self.s = s
    self.closedC = closedC
    self.openC = openC

def generateParenthesis(n):
    res = []
    queue = deque()
    queue.append(PStr("", 0, 0))

    while queue:
        ps = queue.popleft()

        if ps.openC == n and ps.closedC == n:
            res.append(ps.s)
        else:
            if ps.openC < n:
                queue.append(PStr(ps.s + "(", ps.openC + 1, ps.closedC))

            if ps.openC > ps.closedC:
                queue.append(PStr(ps.s + ")", ps.openC, ps.closedC + 1))

    return res

print(generateParenthesis(3))