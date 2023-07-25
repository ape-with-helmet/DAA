#Develop an optimal route for a scenario where a person wants to buy a ticket to a baseball game. Along the way from house to reaching the destination, the person has to visit some toll gates. while visiting the toll gates, find the minimum cost path from a given source to the destination.
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def find_optimal_route(graph, start, destination):
    distances = dijkstra(graph, start)
    if distances[destination] == float('inf'):
        return None
    route = []
    node = destination

    while node != start:
        route.append(node)
        neighbors = graph[node]
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in neighbors.items():
            if distances[neighbor] + weight == distances[node] and distances[neighbor] < min_distance:
                min_distance = distances[neighbor]
                next_node = neighbor
        if next_node is None or next_node in route:
            return None
        node = next_node

    route.append(start)
    route.reverse()
    return route
graph={}
n=int(input("Enter the no of toll stations:"))
for i in range(0,n):
    name=input("Enter station name:")
    station={}
    for i in range(0,n-1):
        name1=input("")
        dist=int(input(""))
        station[name1]=dist
    graph[name]=station
g=1
while g!=0:
    start_location=input("Enter the starting station: ")
    destination_location=input("Enter the destination station: ")
    optimal_route=find_optimal_route(graph,start_location,destination_location)
    if optimal_route is None:
        print("No valid route")
    else:
        print("Optimal route: ",'->'.join(optimal_route))
    g=int(input("If you wish to not check other routes, press 0.\nPress any other number to repeat...\nEnter your choice"))

# Enter the no of toll stations:5
# Enter station name:a
# b
# 3
# c
# 99
# d
# 7
# e
# 99
# Enter station name:b
# a
# 3
# c
# 4
# d
# 2
# e
# 99
# Enter station name:c
# a
# 99
# b
# 4
# d
# 5
# e
# 6
# Enter station name:d
# a
# 7
# b
# 2
# c
# 5
# e
# 4
# Enter station name:e
# a
# 99
# b
# 99
# c
# 6
# d
# 4
# Enter starting location:a
# Enter destination:c
# Optimal Route: a -> b -> c
# Enter starting location:e
# Enter destination:b
# Optimal Route: e -> d -> b