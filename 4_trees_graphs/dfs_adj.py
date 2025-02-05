# maze as an adjacency list (=dictionary)
maze = {
    0: [1, 6, 8],
    1: [0, 2, 3],
    2: [1, 10, 11],
    3: [1, 4, 12],
    4: [3, 5, 13],
    5: [4, 6, 9,],
    6: [0, 5, 7],
    7: [6, 8, 9,],
    8: [0, 7, 14],
    9: [5, 7, 15],
    10: [2],
    11: [2],
    12: [3],
    13: [4],
    14: [8],
    15: [9]
}

# DFS with adjacency list
def dfs_adj(v,target):
    if v is None:
        return
    if v == target:
        print(target,'**Found**')
    visited.append(v)
    # find non-visited adjacent vertices
    # add them to a list
    adj_nodes = []
    for n in maze[v]:
        if n not in visited:
            adj_nodes.append(n)
    # follow edges to each adjacent vertex
    print(v,adj_nodes)
    for n in adj_nodes:
        dfs_adj(n,target)

visited = []
start = 0
target = 12
dfs_adj(start,target)
