from collections import deque

def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1

    sources = deque()

    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

def main():
    print(str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print(str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print(str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()