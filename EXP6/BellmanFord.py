weight = [
    [0, 4, 0, 0],
    [0, 0, -2, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
]

n = 4 
dist = [9999] * n
parent = [-1] * n

source = 0
dist[source] = 0

def relax(u, v):
    if dist[v] > dist[u] + weight[u][v]:
        dist[v] = dist[u] + weight[u][v]
        parent[v] = u

def BellmanFord():
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if weight[u][v] != 0:
                    relax(u, v)

    for u in range(n):
        for v in range(n):
            if weight[u][v] != 0 and dist[v] > dist[u] + weight[u][v]:
                return False  
    return True

if BellmanFord():
    print(f"Shortest distances from source {source}: {dist}")
    print(f"Parent nodes: {[p + 1 for p in parent]}") 
else:
    print("Graph contains a negative weight cycle. No solution.")
