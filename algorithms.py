import heapq, math, time

def heuristic(node, end_node, positions):
    # Euclidean distance as the heuristic
    node_pos = positions.get(node)
    end_node_pos = positions.get(end_node)
    if node_pos is not None and end_node_pos is not None:
        return math.sqrt((end_node_pos[0] - node_pos[0])**2 + (end_node_pos[1] - node_pos[1])**2)
    return float('inf') 

def a_star_algorithm(start_node, end_node, graph, positions):
    start_time = time.time()
    total_distance = 0
    nodes_visited = 0
    open_set = set([start_node])
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start_node] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start_node] = heuristic(start_node, end_node, positions)

    open_heap = []
    heapq.heappush(open_heap, (f_score[start_node], start_node))

    while open_set:
        current = heapq.heappop(open_heap)[1]
        if current == end_node:
            path = reconstruct_path(came_from, current)
            computation_time = time.time() - start_time * 1000
            return path, total_distance, nodes_visited, computation_time

        open_set.remove(current)
        for neighbor in graph[current]:
            nodes_visited += 1
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                total_distance += graph[current][neighbor]
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end_node, positions)
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heapq.heappush(open_heap, (f_score[neighbor], neighbor))

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def bidirectional_dijkstra(graph, start, goal):
    def dijkstra_partial(graph, start, other_visited):
        distances = {vertex: float('infinity') for vertex in graph}
        distances[start] = 0
        pq = [(0, start)]
        visited = {}
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_vertex in other_visited:
                return visited, current_vertex

            visited[current_vertex] = current_distance
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return visited, None

    visited_start, visited_goal = {}, {}
    while True:
        visited_start, middle = dijkstra_partial(graph, start, visited_goal)
        if middle:
            break
        visited_goal, middle = dijkstra_partial(graph, goal, visited_start)
        if middle:
            break

    path = [middle]
    while path[-1] != start:
        for neighbor in graph[path[-1]]:
            if neighbor in visited_start and visited_start[neighbor] + graph[path[-1]][neighbor] == visited_start[path[-1]]:
                path.append(neighbor)
                break
    path.reverse()

    next_node = middle
    while next_node != goal:
        for neighbor in graph[next_node]:
            if neighbor in visited_goal and visited_goal[neighbor] + graph[next_node][neighbor] == visited_goal[next_node]:
                next_node = neighbor
                path.append(next_node)
                break

    return path

def bellman_ford_algorithm(graph, start_node):
    distance = {node: float('inf') for node in graph}
    distance[start_node] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour, weight in graph[node].items():
                if distance[node] + weight < distance[neighbour]:
                    distance[neighbour] = distance[node] + weight

    # Check for negative weight cycles
    for node in graph:
        for neighbour, weight in graph[node].items():
            if distance[node] + weight < distance[neighbour]:
                return "Graph contains a negative weight cycle"

    return distance
