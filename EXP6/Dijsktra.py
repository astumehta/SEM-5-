graph = [
    [0, 7, 9, 0, 0, 4],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [4, 0, 2, 0, 9, 0]
]

n = 6

dist = [9999] * n
parent = [-1] * n
visited = [0] * n

source = 0
dist[source] = 0

def extract_min():
    return min((dist[i], i) for i in range(n) if not visited[i])[1]

def relax(u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        parent[v] = u

for _ in range(n):
    u = extract_min()
    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            relax(u, v)
    visited[u] = 1

print(f"Shortest distances from source {source}: {dist}")
parent = [p + 1 if p != -1 else -1 for p in parent]
print(f"Parent nodes: {parent}")
