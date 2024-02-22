from flask import Flask, jsonify, request, render_template
import algorithms
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route', methods=['POST'])
def find_route():
    data = request.get_json()
    start_node = data.get('start')
    end_node = data.get('end')
    algorithm = data.get('algorithm')

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    positions = {
        'A': (0, 0),
        'B': (1, 0),
        'C': (1, 1),
        'D': (2, 2)
    }

    if algorithm == 'a_star':
        route, distance, nodes_visited, computation_time = algorithms.a_star_algorithm(start_node, end_node, graph, positions)
        computation_time *= 1000
    elif algorithm == 'bidirectional_dijkstra':
        start_time = time.time()
        route = algorithms.bidirectional_dijkstra(graph, start_node, end_node)
        computation_time = time.time() - start_time * 1000
        distance = sum(graph[route[i]][route[i+1]] for i in range(len(route) - 1)) if len(route) > 1 else 0
        nodes_visited = len(route)
    elif algorithm == 'bellman_ford':
        start_time = time.time()
        distances = algorithms.bellman_ford_algorithm(graph, start_node)
        computation_time = time.time() - start_time * 1000

        if distances == "Graph contains a negative weight cycle":
            return jsonify({"error": distances}), 400

        if end_node not in distances:
            return jsonify({"error": "End node not reachable"}), 400

        route = "Path not provided by Bellman-Ford"
        distance = distances[end_node]
        nodes_visited = "Not applicable for Bellman-Ford"
    else:
        return jsonify({"error": "Invalid algorithm specified"}), 400

    return jsonify({
        "Route": route, 
        "TotalDistance": distance, 
        "NodesVisited": nodes_visited, 
        "ComputationTime": computation_time
    })

if __name__ == '__main__':
    app.run(debug=True)
