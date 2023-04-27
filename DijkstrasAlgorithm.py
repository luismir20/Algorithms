import heapq

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        (distance, current_node) = heapq.heappop(heap)

        if distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            distance_to_neighbour = distance + weight

            if distance_to_neighbour < distances[neighbour]:
                distances[neighbour] = distance_to_neighbour
                heapq.heappush(heap, (distance_to_neighbour, neighbour))

    return distances


print(dijkstra(graph, 'A'))


# {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}

# Explanation

# Dijkstra's Algorithm helps you find the shortest path between two intersections on the map. 
# Let's say you want to find the shortest path between intersection A and intersection F, 
# and the map looks like this:

#    2     1
# A --- B --- C --- D
#  \         |     |
#   \        |     |
#    4       3     1
#     \      |   /
#      \     |  /
#       \    | /
#        E -- F
#         2   1

# In this map, each node represents an intersection, 
# and each edge has a weight that represents the distance between two intersections.

# Here's how Dijkstra's Algorithm works step-by-step to find 
# the shortest path between intersection A and intersection F:

# First, we start at intersection A, and we set the distance from A to A as 0, 
# and the distance from A to all other intersections as infinity 
# (since we haven't visited them yet).

# Distances:
# A: 0
# B: inf
# C: inf
# D: inf
# E: inf
# F: inf

# Next, we visit all the neighbours of A (which are B and E), 
# and we update their distances to reflect the distance from A to B and from A to E.
# We then visit the neighbours of B and E (which are C and D for B, and F for E), 
# and we update their distances to reflect the shortest path that we have found so far.

# Distances:
# A: 0
# B: 2
# C: 3
# D: 5
# E: 4
# F: 6

# Finally, we have found the shortest path from A to F,
# which is A -> B -> C -> D -> F, with a distance of 6.



# import heapq: 
# We start by importing the heapq module, 
# which provides an implementation of the heap queue algorithm.

# def dijkstra(graph, start): 
# We define a function called dijkstra that takes in a graph and a start node as input.

# distances = {node: float('inf') for node in graph}: 
# We create a dictionary called distances that stores the distances 
# from the starting node to each other node in the graph. 
# We initialize all the distances to infinity except for the starting node, 
# which we set to 0.

# heap = [(0, start)]: 
# We create a heap called heap that stores the nodes to visit, 
# along with their distances from the starting node. 
# We start with the starting node and its distance, which is 0.

# while heap:: 
# We start a while loop that runs as long as there are nodes to visit in the heap.

# (distance, current_node) = heapq.heappop(heap): 
# We remove the node with the smallest distance from the heap, 
# and we store its distance and node in the variables distance and current_node, 
# respectively.

# if distance > distances[current_node]: continue: 
# We check if the distance from the starting node to the current node is greater 
# than the distance we have already recorded in distances for that node. 
# If it is, we skip this node and move on to the next one.

# for neighbour, weight in graph[current_node].items():: 
# We loop over all the neighbours of the current node, along with their edge weights.

# distance_to_neighbour = distance + weight: 
# We calculate the distance from the starting node to the neighbour node by adding 
# the distance from the starting node to the current node (which we already know) 
# to the weight of the edge between the current node and the neighbour node.

# if distance_to_neighbour < distances[neighbour]:: 
# We check if the distance we just calculated is less than the distance 
# we have already recorded in distances for the neighbour node. 
# If it is, we update the distance in distances to the new, smaller distance, 
# and we add the neighbour node and its distance to the heap.

# return distances: Once we have visited all the nodes in the graph, 
# we return the distances dictionary, which contains the shortest distances 
# from the starting node to all other nodes in the graph.





