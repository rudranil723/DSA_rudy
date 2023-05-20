# DFS algorithm implementation in Python

# A graph is represented as a dictionary of lists where each key represents a vertex
# and the corresponding value is a list of vertices that the key vertex is connected to.

# function for DFS traversal
def dfs(graph, start):
    visited = set()  # set to keep track of visited vertices
    stack = [start]  # initialize the stack with the starting vertex

    while stack:
        vertex = stack.pop()  # pop the top element from the stack
        if vertex not in visited:
            visited.add(vertex)  # mark the vertex as visited
            print(vertex, end=' ')
            # add the neighbors of the current vertex to the stack
            stack.extend(graph[vertex] - visited)
    print()

# Example usage:
# Graph represented as dictionary of lists
graph = {0: {1, 2}, 1: {2}, 2: {0, 3}, 3: {3}}
dfs(graph, 2)  # starting vertex is 2
