# Contour Plot
import numpy as np
import matplotlib.pyplot as plt

def counter_plot():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X**2 + Y**2)

    contour = plt.contourf(X, Y, Z, cmap='coolwarm')
    plt.colorbar(contour)
    plt.title("Contour Plot")
    plt.show()

counter_plot()

# Aystar Algorithm
from queue import PriorityQueue

def aystar(graph, heuristics, start, goal):
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    came_from = {}

    while not pq.empty():
        _, current = pq.get()
        if current == goal:
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            print("A* algorithm: ", "->".join(path))
            break
        for neighbour, cost in graph[current]:
            new_cost = g_cost[current] + cost
            if new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                priority = new_cost + heuristics[neighbour]
                pq.put((priority, neighbour))
                came_from[neighbour] = current

graph = { 
  'a': [('b', 9), ('c', 4), ('d', 7)], 
  'b': [('a', 9), ('e', 11)], 
  'c': [('a', 4), ('d', 12), ('f', 12), ('e', 17)], 
  'd': [('a', 7), ('c', 12), ('f', 14)], 
  'e': [('b', 11), ('c', 17), ('z', 5)], 
  'f': [('c', 12), ('d', 14), ('z', 9)], 
  'z': [('e', 5), ('f', 9)] 
}

heuristics = { 'a': 21, 'b': 14, 'c': 18, 'd': 18, 'e': 5, 'f': 8, 'z': 0}

aystar(graph, heuristics, 'a', 'z')
