def find_paths(graphh, startt, endd, pathh):
    pathh = pathh + [startt]
    pathss = []

    if startt == endd:
        return [pathh]

    if not graphh.get(startt):
        return []

    for neighbor in graphh[startt]:
        new_paths = find_paths(graphh, neighbor, endd, pathh)
        pathss.extend(new_paths)

    return pathss


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_paths(graph, start, end, path)
print(*paths)
