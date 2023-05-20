from collections import deque

def bfs(graph, start):
    # Keep track of visited nodes
    visited = set()

    # Initialize queue for BFS
    queue = deque([start])

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()

        # If the vertex has not been visited yet
        if vertex not in visited:
            # Mark the vertex as visited
            visited.add(vertex)

            # Add all adjacent vertices to the queue
            queue.extend(graph[vertex] - visited)

    return visited

# Example graph
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

print(bfs(graph, 'A'))
