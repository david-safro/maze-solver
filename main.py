# main.py
#working
import pygame
from tkinter import messagebox
from constants import *
from maze import Maze
from bfs import BFS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation")
clock = pygame.time.Clock()

def draw_maze(maze):
    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            if maze[row, col] == 0:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[row, col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

def draw_path(path):
    for pos in path:
        row, col = pos
        pygame.draw.rect(screen, RED, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        pygame.time.wait(10)

def draw_start_end():
    start_pos = (0, 1)
    end_pos = (ROWS - 1, COLS - 2)

    pygame.draw.rect(screen, GREEN, (start_pos[1] * CELL_SIZE, start_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (end_pos[1] * CELL_SIZE, end_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

def show_alert(message):
    messagebox.showinfo("Success", message)

def main():
    maze = Maze().maze
    bfs = BFS(maze)

    running = True
    path_found = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_maze(maze)
        draw_start_end()

        if not path_found:
            path = bfs.search((0, 1), (ROWS - 1, COLS - 2))
            if path:
                draw_path(path)
                path_found = True
                show_alert("Path found!")
            else:
                show_alert("No path exists.")

    pygame.quit()

if __name__ == "__main__":
    main()
