graph=[
    [0,6,5,5,0,0,0],
    [0,0,0,0,-1,0,0],
    [0,-2,0,0,1,0,0],
    [0,0,-2,0,0,-1,0],
    [0,0,0,0,0,0,3],
    [0,0,0,0,0,0,3],
    [0,0,0,0,0,0,0],
]

n=len(graph)
dist=n*[9999]
parent=n*[-1]
source=0

dist[source]=0
c=0


def relax(u,v):
    if(dist[v]>dist[u]+graph[u][v]):
        dist[v]=dist[u]+graph[u][v]
        parent[v]=u


def BellmanFord():
    for _ in range(n-1):
        for u in range(0,n):
            for v in range(0,n):
                if(graph[u][v]!=0):
                    relax(u,v)

    
    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0 and dist[v] > dist[u] + graph[u][v]:
                return False 
    return True



if BellmanFord():
    print(f"Shortest distances from source {source}: {dist}")
    parent=[p+1 for p in parent]
    print(f"Parent nodes: {parent}")
else:
    print("Graph contains a negative weight cycle. No solution.")