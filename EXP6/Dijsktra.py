graph=[
    [0,7,9,0,0,4],
    [7,0,10,15,0,0],
    [9,10,0,11,0,2],
    [0,15,11,0,6,0],
    [0,0,0,6,0,9],
    [4,0,2,0,9,0]
]

n=len(graph)
dist=n*[9999]
parent=n*[-1]
visited=n*[0]
source=0

dist[source]=0

def extract_min():
    return min((dist[i], i) for i in range(n) if not visited[i])[1]

def relax(u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        parent[v] = u

def Dikstra():
    for i in range(0,n):
        u=extract_min()

        for j in range(0,n):
            if(graph[u][j]!=0 and visited[j]!=1):
                relax(u,j)
        visited[u]=1

Dikstra()

print(dist)
print(parent)