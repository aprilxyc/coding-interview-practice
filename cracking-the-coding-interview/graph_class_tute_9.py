class Edge:

    def __init__(self,u, v, w):
        self.u = u
        self.v = v
        self.w = w

class Graph:
    self.adj_list =[[] for i in range(n)]
    self.num_verticies

    def add_directed_graph(self, u, v, w):
        self.adj_list[u].append(Edge(u, v, w))

    # def dfs(self):
    #     for e in self.adj_list[start]:
    #         if e, v in visited:

    def has_cycle(self):
        self.visited = [False] * self.num_vertices
        if self.has_cycle_aux(0, None): # add previous to the vertex call
            return True
        else:
            return False

    # this is the recursive part
    # this uses DFS
    def has_cycle_aux(self, current, prev):
        print(current)
        self.visited[current] = True
        for e in self.adj_list[current]:
            if self.visited[e.v] and e.v != prev: # if you find a cycle return true, but you return true up to your previous call
                if e.v != prev: # if it has already been visited
                    return True
            else:
                return self.has_cycle_aux(e.v) # ^ that is why we have to return our previous call



# edge list is a list of edges in no particular order
# adjacency matrix very yfast in determining which vertices are adjancet (O(1))
# adjacency list is quick for getting all the neighbours of the vertex, which is why most graph algorithms use thi
G = Graph(S)
G.add_directed_edge(0, 1, 1)
G.add_directed_edge(0, 2, 1)
G.add_directed_edge(2, 0, 1)
# G.add_directed_edge(3, 2, 1)
# G.add_directed_edge(3, 4, 1)
G.has_cycle()

# This question has a bug! It does not say simple graph it just says undirected graph so it does not account fr loops?

# edge classes in assignment 4