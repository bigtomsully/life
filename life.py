import pygame
import numpy as np

# Game parameters
WIDTH, HEIGHT = 800, 800
RES = 20

# Color mapping
COLORS = [
    (0,0,0),
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (255,255,255)
]

def draw_grid():
    for x in range(0, WIDTH, RES):
        for y in range(0, HEIGHT, RES):
            pygame.draw.line(screen, (125, 125, 125), (x, 0), (x, HEIGHT))
            pygame.draw.line(screen, (125, 125, 125), (0, y), (WIDTH, y))

def draw_cells():
    for i in range(COLS):
        for j in range(ROWS):
            color = COLORS[0]
            if grid[i][j] == 1:
                alive_neighbors = count_alive_neighbors(i, j)
                if alive_neighbors < len(COLORS):
                    color = COLORS[alive_neighbors]
            pygame.draw.rect(screen, color, pygame.Rect(j*RES, i*RES, RES-1, RES-1))

def count_alive_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (x + i + COLS) % COLS
            row = (y + j + ROWS) % ROWS
            count += grid[col][row]
    count -= grid[x][y]
    return count

def update_grid():
    global grid
    new_grid = grid.copy()
    for i in range(COLS):
        for j in range(ROWS):
            alive_neighbors = count_alive_neighbors(i, j)
            if grid[i][j] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and alive_neighbors == 3:
                new_grid[i][j] = 1
    grid = new_grid

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Initialize grid
COLS, ROWS = WIDTH // RES, HEIGHT // RES
grid = np.random.choice([0, 1], COLS*ROWS, p=[0.5, 0.5]).reshape(COLS, ROWS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    # Drawing cells and grid
    draw_cells()
    draw_grid()

    # Updating grid
    update_grid()

    pygame.display.flip()
    clock.tick(1)
