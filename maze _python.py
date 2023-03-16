# Running time of Algorithms: Worst Case 
#Algorithms to use randomness 

from PIL import Image
import random

# Set maze dimensions
maze_width = 5000
maze_height = 5000

# Create a new image with the specified dimensions
maze_image = Image.new('RGB', (maze_width, maze_height), 'white')

# Set up the maze
maze = [[0 for _ in range(maze_width)] for _ in range(maze_height)]
start_x, start_y = 1, 1
maze[start_y][start_x] = 1
stack = [(start_x, start_y)]

# Generate the maze
while stack:
    x, y = stack.pop()
    neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
    random.shuffle(neighbors)
    for nx, ny in neighbors:
        if 0 < nx < maze_width - 1 and 0 < ny < maze_height - 1:
            if maze[ny][nx] == 0:
                maze[ny][nx] = 1
                maze[(ny+y)//2][(nx+x)//2] = 1
                stack.append((nx, ny))

# Draw the maze on the image
wall_color = (0, 0, 0)  # black
for y in range(maze_height):
    for x in range(maze_width):
        if maze[y][x] == 0:
            maze_image.putpixel((x, y), wall_color)

# Save the maze image to a file
maze_image.save('maze.png')        

    
# Set maze dimensions
maze_width = 5000
maze_height = 5000

# Create a new image with the specified dimensions
maze_image = Image.new('RGB', (maze_width, maze_height), 'white')

# Set up the maze
maze = [[0 for _ in range(maze_width)] for _ in range(maze_height)]
stack = []

# Set the start and end points randomly on the edges of the maze
start_x, start_y = random.choice([(0, random.randint(0, maze_height-1)), 
                                  (maze_width-1, random.randint(0, maze_height-1)), 
                                  (random.randint(0, maze_width-1), 0), 
                                  (random.randint(0, maze_width-1), maze_height-1)])
end_x, end_y = random.choice([(0, random.randint(0, maze_height-1)), 
                              (maze_width-1, random.randint(0, maze_height-1)), 
                              (random.randint(0, maze_width-1), 0), 
                              (random.randint(0, maze_width-1), maze_height-1)])
maze[start_y][start_x] = 1
maze[end_y][end_x] = 1

# Add the start point to the heap with a distance of 0
heap = [(0, start_x, start_y, [])]

# Dijkstra's algorithm to find the shortest path
while heap:
    dist, x, y, path = heapq.heappop(heap)
    if x == end_x and y == end_y:
        # Draw the path on the maze image
        path_color = (255, 0, 0)  # red
        for px, py in path:
            maze_image.putpixel((px, py), path_color)
        break
    if maze[y][x] == 0:
        maze[y][x] = 2
        path.append((x, y))
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < maze_width and 0 <= ny < maze_height:
                if maze[ny][nx] == 1 or maze[ny][nx] == 2:
                    heapq.heappush(heap, (dist+1, nx, ny, path[:]))

# Draw the maze on the image
wall_color = (0, 0, 0)  # black
for y in range(maze_height):
    for x in range(maze_width):
        if maze[y][x] == 0:
            maze_image.putpixel((x, y), wall_color)

# Save the maze image to a file
maze_image.save('maze02.png')