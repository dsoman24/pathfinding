# Simple grid graph generator algorithm (given a width and a height), my own design. Creates adjacency matrix representation.

from random import randint

# the nodes are indexed 0 to n-1.
# For instance, the 2*2 grid is as follows:
# [0 1]
# [2 3]

def gridgraph(width, height): # method to create gridgraph node representation
    grid = []
    for row in range(0, width*height, width):
        rowarr = [i for i in range(row, row+width)]
        grid.append(rowarr)
    return grid

class AdjMatrix(): # Adjacenecy matrix class to model grid edges

    def __init__(self, num_nodes): # initialized with size. size is the number of nodes in the graph
        #self.empty = np.zeros((size, size))
        self.empty = [[0 for i in range(0, num_nodes)] for j in range(0, num_nodes)]

    def add_edge(self, i, j, weight = False): # i = columns, j = rows. weight = True gives randomly weighted graph.
        if not weight:
            node_weight = 1
        else:
            node_weight = randint(1, 100)
        self.empty[i][j] = node_weight
        self.empty[j][i] = node_weight

    def del_edge(self, i, j):
        self.empty[i][j] = 0
        self.empty[j][i] = 0

    def call_edge(self, i, j):
        #print(self.empty[i][j])
        return self.empty[i][j]

    def return_adj_matrix(self):
        #print("\nAdjacency matrix for "+str(dim)+"*"+str(dim)+" grid (radius="+str(radius)+"):")
        #print(self.empty)
        return self.empty

def make_grid_graph(grid_width, grid_height, radius = 1):
    """Returns node represenation of graph and adjacency matrix of graph in a tuple"""
    gra = gridgraph(grid_width, grid_height)
    adj = AdjMatrix(grid_width*grid_height)

    for rad in range(1, radius+1):
        for rownum in range(0, grid_height):
            for row in range(0, grid_width-rad):
                p1 = gra[rownum][row]
                p2 = gra[rownum][row+rad]
                adj.add_edge(p1, p2)
        
        for colnum in range(0, grid_width):
            for row in range(0, grid_height-rad):
                p1 = gra[row][colnum]
                p2 = gra[row+rad][colnum]
                adj.add_edge(p1, p2)

    return gra, adj.return_adj_matrix()

