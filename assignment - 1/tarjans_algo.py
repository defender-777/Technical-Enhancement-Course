from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_bridges(self):
        visited = [False]*self.n
        disc = [0]*self.n
        low = [0]*self.n
        parent = [-1]*self.n
        bridges = []

        self.time = 0

        def dfs(u):
            visited[u] = True
            disc[u] = low[u] = self.time
            self.time += 1

            for v in self.graph[u]:

                if not visited[v]:
                    parent[v] = u
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        bridges.append((u,v))

                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        for i in range(self.n):
            if not visited[i]:
                dfs(i)

        return bridges


if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(1,0)
    g.add_edge(0,2)
    g.add_edge(2,1)
    g.add_edge(0,3)
    g.add_edge(3,4)

    print("Critical Links:", g.find_bridges())