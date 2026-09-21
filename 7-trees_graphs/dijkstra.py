from collections import defaultdict

def dijkstra(graph, start, target):
    visited = []
    previous = []

    # initialization, all distances infinite from start
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue = []
    queue.append((start,0))    
    print('Starting queue',queue)
    while queue:
        current = queue[0][0] # current vertex
        cur_dist = queue[0][1] # distance from start to current vertex
        print('-> Go to',current, 'since smallest distance from',start)
        # check if target reached
        if current == target:
            print('Target',target,'found, shortest distance from',start,'is',cur_dist)
            if not current in previous:
                previous.append(current)
            return cur_dist, previous
        # calculate new distances from start
        for neigh, neigh_dist in graph[current].items():
            if neigh in visited:
                print(current,'to',neigh,': already visited')
                continue
            # update distance to neighbor if smaller
            new_dist = cur_dist + neigh_dist
            print(current,'to',neigh,':',cur_dist,'+',neigh_dist,'=',new_dist,end='')
            if new_dist < distances[neigh]:
                print(', new dist from',start,'to',neigh,'is now',new_dist,'<',distances[neigh])
                distances[neigh] = new_dist
                if not current in previous:
                    previous.append(current)
                try:
                    idx = next(i for i, t in enumerate(queue) if t[0] == neigh)
                    queue[idx] = (neigh, new_dist)
                except StopIteration:
                    queue.append((neigh,new_dist))
            else:
                print(', dist from',start,'to',neigh,'not updated as',new_dist,'>=',distances[neigh])
        # remove current vertex from queue and
        # sort queue, so that minimum dist from start is first item
        visited.append((current))
        queue.pop(0)
        queue = sorted(queue, key=lambda x: x[1]) 
        print('Updated queue',queue)
    # path to target not found
    return float('inf'), previous

graph = {
    "A": {"B": 2 },
    "B": {"C": 3, "D": 2 },
    "C": {"B": 3, "D": 2, "E": 1, "G": 4 },
    "D": {"B": 2, "C": 2, "F": 7 },
    "E": {"C": 1, "G": 6},
    "F": {"D": 7, "G": 1},
    "G": {"C": 4, "E": 6, "F": 1}
}
distance, visited_vertices = dijkstra(graph, 'A', 'F')
print(distance, visited_vertices)

