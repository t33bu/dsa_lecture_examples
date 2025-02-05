from collections import defaultdict

def add_edge(graph,u,v):
    graph[u].append(v) # directed
    graph[v].append(u) # undirected

# DFS algorithm
def dfs(graph, v, target,visited):
    visited.append(v)
    if v == target:
        print('Found', target)
    # follow edges to child vertices
    for n in graph[v]:
        if n not in visited:
            print('visited:',visited,':',v,'->',n)
            dfs(graph, n, target, visited)

# create maze from example
maze = defaultdict(list)
add_edge(maze,0,1)
add_edge(maze,0,6)
add_edge(maze,0,8)
add_edge(maze,1,2)
add_edge(maze,1,3)
add_edge(maze,2,10)
add_edge(maze,2,11)
add_edge(maze,3,4)
add_edge(maze,3,12)
add_edge(maze,4,5)
add_edge(maze,4,13)
add_edge(maze,5,6)
add_edge(maze,5,9)
add_edge(maze,6,7)
add_edge(maze,7,8)
add_edge(maze,7,9)
add_edge(maze,8,14)
add_edge(maze,9,15)

# list of visited vertices needed to handle cycles
visited = []
start = 0
target = 18
dfs(maze,start,target,visited)
