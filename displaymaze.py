import pygame as pg
from mazegenerator import *
from gridgenerator import *
from mazepaths import *

# Initialize maze and grid
if __name__ == "__main__":
    grid_width, grid_height = 21, 21 # MANUAL INPUT
    root_row, root_col = 0, 0 # MANUAL INPUT

else:
    grid_width = int(input("Maze width?: "))
    grid_height = int(input("Maze height?: "))
    
    root_row = int(input("Root cell row number?: "))
    root_col = int(input("Root cell column number?: "))

maze = maze_adj_matrix(grid_width, grid_height, root_row, root_col)
grid = gridgraph(grid_width, grid_height)
paths = find_paths(maze, grid, root_row, root_col)
edges = maze[1]

### INPUTS ###
screen_width, screen_height = 800, 800
screen_fill_color = 0, 0, 0
wall_color = 0, 0, 255
cell_color = 255, 255, 255
start_marker_color = 0, 255, 0
end_marker_color = 255, 0, 0
path_marker_color = 0, 255, 255
show_solution = False
animation_delay = 20
# Cells are squares with equal cell width:
cell_size = 10


def animation_step(delay = animation_delay):
    pg.time.delay(delay)
    pg.display.update()

bg_width = (2*grid_width+1)*cell_size
bg_height = (2*grid_height+1)*cell_size

corner_x = round(screen_width/2 - bg_width/2)
corner_y = round(screen_height/2 - bg_height/2)

# Start/end/path marker radius:
marker_radius = 0.35*cell_size

# Initialize pygame
pg.init()

# Create screen
screen = pg.display.set_mode((screen_width, screen_height))
screen.fill(screen_fill_color)

# Window title
pg.display.set_caption('Randomized DFS Maze')

# Icon
icon = pg.image.load('maze.png')
pg.display.set_icon(icon)

#### DRAW MAZE: ###

# Draw background

maze_bg = pg.Rect(corner_x, corner_y, bg_width, bg_height)
pg.draw.rect(screen, wall_color, maze_bg)

# Get top left corner positions of each cell in grid
cell_x_pos = []
cell_y_pos = []

for x in range(corner_x+cell_size, corner_x+bg_width, 2*cell_size):
    cell_x_pos.append(x)

for y in range(corner_y+cell_size, corner_y+bg_height, 2*cell_size):
    cell_y_pos.append(y)

### PROGRAM RUN LOOP ###

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    # Draw grid cells
    for x_pos in cell_x_pos:
        for y_pos in cell_y_pos:
            cell = pg.Rect(x_pos, y_pos, cell_size, cell_size)
            pg.draw.rect(screen, cell_color, cell)
            #animation_step()

    # Draw edges
    for edge in edges:
        cell1_pos = get_node_pos(edge[0], grid)
        cell2_pos = get_node_pos(edge[1], grid)

        if cell1_pos[1] == cell2_pos[1]: # same column (same x position) - vertical edge
            edge_x = corner_x+cell_size*(2*cell1_pos[1]+1)
            edge_y = corner_y+cell_size*(2*min(cell1_pos[0], cell2_pos[0])+2)
        elif cell1_pos[0] == cell2_pos[0]: # same row (same y position) - horizontal edge
            edge_x = corner_x+cell_size*(2*min(cell1_pos[1], cell2_pos[1])+2)
            edge_y = corner_y+cell_size*(2*cell1_pos[0]+1)
        
        edge_disp = pg.Rect(edge_x, edge_y, cell_size, cell_size)
        pg.draw.rect(screen, cell_color, edge_disp)
        animation_step()

    # Draw start/end and solution path
    longest_path = paths[1][find_longest_path(paths[0])]

    for point in longest_path:
        
        point_pos = get_node_pos(point, grid)
        marker_x = corner_x+cell_size*(2*point_pos[1]+1)+cell_size/2
        marker_y = corner_y+cell_size*(2*point_pos[0]+1)+cell_size/2
        
        if point == longest_path[-1]:
            color = start_marker_color
        elif point == longest_path[0]:
            color = end_marker_color
        else:
            color = path_marker_color

        if show_solution == False:
            if point in longest_path[1:-1]:
                continue
        pg.draw.circle(screen, color, (marker_x, marker_y), marker_radius)
        animation_step()

    displaying = True
    while displaying:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                displaying = False
                running = False
            
pg.quit()