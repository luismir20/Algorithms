graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, 'A')


#A -> B -> D -> E -> F -> C


# #
# We start at node 'A' and visit it.
# We then visit the neighbours of 'A', which are 'B' and 'C'. We choose 'B' as the next node to visit.
# We visit 'B' and its neighbours, which are 'D' and 'E'. We choose 'D' as the next node to visit.
# We visit 'D' and its neighbours, but there are none, so we backtrack to 'B'.
# We then visit the next neighbour of 'B', which is 'E'. We visit 'E' and its neighbour 'F'.
# We backtrack to 'B' again and visit its next neighbour, which is 'C'. We visit 'C' and backtrack to 'A'.
# Finally, we visit the last neighbour of 'A', which is 'C'.

# A -- B -- D
#   \    \ 
#    C    E -- F
