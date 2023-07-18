#Develop an optimal route for a scenario where a person wants to buy a ticket to a baseball game. Along the way from house to reaching the destination, the person has to visit some toll gates. while visiting the toll gates, find the minimum cost path from a given source to the destination.
import heapq

def dijkstra(graph,start):
    distances={node: float('inf') for node in graph}
    distances[start]=0
    heap=[(0,start)]
    while heap:
        current_dist,current_node=heapq.heappop(heap)
        if current_dist>distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance=current_dist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))
    return distances

def find_optimal_route(graph,start,destination):
    distances=dijkstra(graph,start)
    if distances[destination]==float('inf'):
        return None
    route=[]
    node=destination
    while node!=start:
        route.append(node)
        neighbors=graph[node]
        min_distance=float('inf')
        next_node=None
        for neighbor, weight in neighbors.items():
            if distances[neighbor]+weight==distances[node]and distances[neighbor]<min_distance:
                min_distance=distances[neighbor]
                next_node=neighbor
        if next_node is None or next_node in route:
            print(next_node,distances)
            return None
        node=next_node
    route.append(start)
    route.reverse()
    return route
#graph[]
graph={
    'A':{'B':3,'C':99,'D':7,'E':99},
    'B':{'A':3,'C':99,'D':7,'E':99},
    'C':{'A':99,'C':99,'D':7,'E':99},
    'D':{'A':7,'C':99,'D':7,'E':99},
    'E':{'A':3,'C':99,'D':7,'E':99},
}
start_location='C'
destination_location='A'
optimal_route=find_optimal_route(graph,start_location,destination_location)
if optimal_route is None:
    print("No valid route")
else:
    print("Optimal route: ",'->'.join(optimal_route))