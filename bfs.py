# bfs.py
#working
from queue import Queue
from constants import *
class BFS:
    def __init__(self, maze):
        self.maze = maze

    def search(self, start_pos, end_pos):
        queue = Queue()
        queue.enqueue((start_pos, []))
        visited = set()

        while not queue.is_empty():
            current_pos, path = queue.dequeue()

            if current_pos == end_pos:
                return path

            row, col = current_pos
            neighbors = []

            if row > 0 and self.maze[row - 1, col] == 1:
                neighbors.append((row - 1, col))
            if col > 0 and self.maze[row, col - 1] == 1:
                neighbors.append((row, col - 1))
            if row < ROWS - 1 and self.maze[row + 1, col] == 1:
                neighbors.append((row + 1, col))
            if col < COLS - 1 and self.maze[row, col + 1] == 1:
                neighbors.append((row, col + 1))

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.enqueue((neighbor, path + [neighbor]))
                    visited.add(neighbor)

        return None
