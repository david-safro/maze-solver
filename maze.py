# maze.py

import numpy as np
from constants import ROWS, COLS

class Maze:
    def __init__(self):
        self.maze = self.create_maze()

    def create_maze(self):
        # Start building the maze from a random cell
        stack = [(np.random.randint(0, ROWS - 1), np.random.randint(0, COLS - 1))]
        maze = np.zeros((ROWS, COLS), dtype=int)

        while stack:
            current_row, current_col = stack[-1]

            # Find unvisited neighbors
            neighbors = []
            if current_row > 1 and maze[current_row - 2, current_col] == 0:
                neighbors.append((current_row - 2, current_col))
            if current_col > 1 and maze[current_row, current_col - 2] == 0:
                neighbors.append((current_row, current_col - 2))
            if current_row < ROWS - 2 and maze[current_row + 2, current_col] == 0:
                neighbors.append((current_row + 2, current_col))
            if current_col < COLS - 2 and maze[current_row, current_col + 2] == 0:
                neighbors.append((current_row, current_col + 2))

            if neighbors:
                # Choose a random neighbor
                next_row, next_col = neighbors[np.random.randint(0, len(neighbors))]

                # Remove the wall between the current cell and the chosen neighbor
                maze[next_row, next_col] = 1
                maze[current_row + (next_row - current_row) // 2, current_col + (next_col - current_col) // 2] = 1

                # Move to the chosen neighbor
                stack.append((next_row, next_col))
            else:
                # Dead end, backtrack
                stack.pop()

        # Set the opening and exit
        maze[0, 1] = 1
        maze[ROWS - 1, COLS - 2] = 1

        return maze
#working
