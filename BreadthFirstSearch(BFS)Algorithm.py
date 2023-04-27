graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  
queue = []  

def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


bfs(visited, graph, 'A')


#A -> B -> C -> D -> E -> F


# A -- B -- D
#   \    \ 
#    C    E -- F


# We start at node 'A' and add it to the queue.
# We then remove 'A' from the queue and visit its neighbours 'B' and 'C'. We add 'B' and 'C' to the queue.
# We remove 'B' from the queue and visit its neighbours 'D' and 'E'. We add 'D' and 'E' to the queue.
# We remove 'C' from the queue and visit its neighbour 'F'. We add 'F' to the queue.
# We remove 'D' from the queue, but it has no neighbours to visit.
# We remove 'E' from the queue, but it has only one neighbour 'F', which we have already visited.
# We remove 'F' from the queue, but it has no neighbours to visit.

