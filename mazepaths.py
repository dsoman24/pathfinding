# Get all path distances in a maze from adjacency matrix representation. 
# Note: will only work if the maze has no loops. This is a very basic algorithm. Works for DFS mazes since every node will only have 1 path back to the root.
# Will work for disjointed graphs/mazes

from mazegenerator import maze_adj_matrix
from gridgenerator import gridgraph
from printarray import print_2d_array as printarr

def adjacent_nodes(node, adj_matrix, visited):
    adj_nodes = []
    for i in range(len(adj_matrix[node])):
        if adj_matrix[node][i] != 0 and i not in visited:
            adj_nodes.append(i)

    return adj_nodes

def find_paths(maze_adj, grid, root_row, root_col):
    """Use DFS to find paths and distances"""
    adj_matrix = maze_adj[0]
    edges = maze_adj[1]
    root = grid[root_row][root_col]
    distances = [float('inf') for i in range(len(adj_matrix))] # initializes all distances as infinity
    distances[root] = 0
    paths = []

    stack = [root]
    visited = [root]
    
    # compute distances using DFS
    while stack:
        current = stack.pop()
        adjacent = adjacent_nodes(current, adj_matrix, visited)
        if adjacent:
            for node in adjacent:
                if distances[node] == float('inf'):
                    distances[node] = adj_matrix[current][node] # If a node is adjacent and has not been visited its distance is changed from infinity to its weight in the adjacency matrix
                distances[node] += distances[current]
                stack.append(node)
        visited += adjacent
    
    # compute paths
    for node in range(len(adj_matrix)):
        current = node
        path = [current]
        while current != root:
            for edge in edges:
                if edge[1] == current:
                    next_node = edge[0]
                    path.append(next_node)
                    current = next_node
        paths.append(path)

    return distances, paths

def find_longest_path(distances):
    max_distance_idx = 0
    max_distance = 0
    for i in range(len(distances)):
        if distances[i] >= max_distance:
            max_distance = distances[i]
            max_distance_idx = i

    return max_distance_idx
