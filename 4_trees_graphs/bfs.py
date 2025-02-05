from collections import defaultdict

# breadth-first search algorithm
def bfs(graph, v, target, visited):
    queue.append(v)
    visited.append(v)
    # as long as queue has items
    while queue:
        print('queue',queue)
        s = queue.pop(0)
        for n in graph[s]:
            if n not in visited:
                print(s,'->',n)
                if n == target:
                    print('Found',target)
                    return # stop if found
                visited.append(n)
                queue.append(n)
            else:
                print(s,'->',n,'already visited')

# helper to create a maze
def add_edge(graph,u,v):
    graph[u].append(v) # directed
    graph[v].append(u) # undirected

# create maze
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

visited = []
queue = []
start = 0
target = 10
bfs(maze,start,target,visited)
