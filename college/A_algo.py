import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.__create_graph()

    def __create_graph(self):
        for start, end, cost in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = {}
            if end not in self.graph_dict:
                self.graph_dict[end] = {}
            self.graph_dict[start][end] = cost
            self.graph_dict[end][start] = cost

    def heuristic(self, node, goal):
        # Define your heuristic function here
        pass

    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next_node in self.graph_dict[current]:
                new_cost = cost_so_far[current] + self.graph_dict[current][next_node]
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(next_node, goal)
                    frontier.put(next_node, priority)
                    came_from[next_node] = current

        return came_from, cost_so_far
