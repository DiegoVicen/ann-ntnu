from flatland import Flatland
from agents import Agent
import pygame
import sys


class Window():
    # Colors defined for convinience
    _black = (0, 0, 0)
    _white = (255, 255, 255)

    # Coordinates and other parameters of size
    _grid_o = (20, 20)
    _cell_size = 40

    def __init__(self, agent, env):
        self.agent = agent
        self.env = env
        # Compute window size
        self.height = (self.env.rows + 2) * self._cell_size + 2*self._grid_o[1]
        self.width = (self.env.cols + 2) * self._cell_size + 2*self._grid_o[0]
        # Populate grid centers dictionary
        self._grid = {}
        for i in range(-1, self.env.rows + 1):
            for j in range(-1, self.env.cols + 1):
                # Compute the corner of the cell
                self._grid[i, j] = (self._grid_o[0] + (j+1.5)*self._cell_size,
                                    self._grid_o[1] + (i+1.5)*self._cell_size)
                # Round to int
                self._grid[i, j] = (int(self._grid[i, j][0]),
                                    int(self._grid[i, j][1]))

    def start_simulation(self):
        # Create the screen
        self.screen = pygame.display.set_mode((self.height, self.width))
        # Call the draw function to start
        self._draw_window()
        # Intiate the GUI loop
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def _draw_window(self):

        # Draw a white background
        self.screen.fill(self._white)

        # Draw vertical lines of the grid
        for i in range(self.env.cols + 3):
            start = (self._grid_o[0] + i * self._cell_size,
                     self._grid_o[1])
            end = (self._grid_o[0] + i * self._cell_size,
                   self._grid_o[1] + (self.env.rows + 2) * self._cell_size)
            pygame.draw.lines(self.screen, self._black, False, [start, end], 1)

        # Draw horizontal lines of the grid
        for i in range(self.env.rows + 3):
            start = (self._grid_o[0],
                     self._grid_o[1] + i * self._cell_size)
            end = (self._grid_o[0] + (self.env.cols + 2) * self._cell_size,
                   self._grid_o[1] + i * self._cell_size)
            pygame.draw.lines(self.screen, self._black, False, [start, end], 1)

        # Draw each element in the grid
        for i in range(-1, self.env.rows + 1):
            for j in range(-1, self.env.cols + 1):
                pygame.draw.circle(self.screen, self._black, self._grid[i, j],
                                   10, 3)

        pygame.display.update()


def main():
    agent = Agent()
    env = Flatland(10, 10)
    window = Window(agent, env)
    window.start_simulation()


if __name__ == "__main__":
    main()