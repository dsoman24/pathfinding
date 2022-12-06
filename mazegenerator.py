# Generate adjacency matrix for a random maze
# Randomized DFS
# No loops

from gridgenerator import gridgraph, AdjMatrix
from printarray import print_2d_array as printarr
from random import randint

def get_node_pos(node, grid):
        rownum = 0
        colnum = 0
        width = len(grid[0])
        height = len(grid)
        # x is vertical, y is horizontal
        for i in range(height):
            for j in range(width):
                if grid[i][j] == node:
                    rownum = i
                    colnum = j
        
        return rownum, colnum

def available_neighbors(node, visited, grid):
        width = len(grid[0])
        height = len(grid)
        pos = get_node_pos(node, grid)
        neighbors = []
        direction = (-1, 1) # (-1 = up/left, 1 = down/right)
        # x direction neighbors
        for i in direction:
            step_idx = pos[0]+i
            if step_idx > -1 and step_idx < height:
                neighbor = grid[step_idx][pos[1]]
                if neighbor not in visited:
                    neighbors.append(neighbor)
        # y direction neighbors
        for i in direction:
            step_idx = pos[1]+i
            if step_idx > -1 and step_idx < width:
                neighbor = grid[pos[0]][step_idx]
                if neighbor not in visited:
                    neighbors.append(neighbor)
        return neighbors

def maze_adj_matrix(width, height, root_row = 0, root_col = 0):
    """Random maze generator with a given width and height, and starting node. 
    Starting node is node 0, (0, 0) on top left corner.
    Returns its adjacency matrix and array of edges."""
    num_nodes = width*height # number of nodes
    grid = gridgraph(width, height)
    adj = AdjMatrix(num_nodes)
    root = grid[root_row][root_col]
    stack = [root]
    visited = [root]
    edges = [(root, root)]

    while stack: 
        current = stack.pop()
        neighbors = available_neighbors(current, visited, grid)
        if neighbors:
            rand_idx = randint(0, len(neighbors)-1)
            chosen = neighbors[rand_idx]
            for i in range(len(neighbors)):
                visited.append(neighbors[i])
                adj.add_edge(current, neighbors[i])
                edges.append((current, neighbors[i]))
                if i != rand_idx:
                    stack.append(neighbors[i])
            stack.append(chosen)
    
    return adj.return_adj_matrix(), edges