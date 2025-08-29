# 3D Surface Plot
def plot_3d():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    ax = plt.figure().add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title("3D Surface Plot")
    plt.show()

plot_3d()


# Best First Search
from queue import PriorityQueue

def best_first_search(graph, heuristic, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    came_from = {}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            print("Best First Search Path:", ' -> '.join(path))
            return

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))
                    came_from[neighbor] = current

graph = {
    'S': ['A', 'C'],
    'A': ['S', 'C', 'B'],
    'B': ['A', 'D'],
    'C': ['S', 'A', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'G'],
    'F': ['D', 'G'],
    'G': ['E', 'F']
}

heuristic = {
    'S': 50,
    'A': 100,
    'B': 200,
    'C': 100,
    'D': 60,
    'E': 70,
    'F': 20,
    'G': 0
}


best_first_search(graph, heuristic, 'A', 'G')
