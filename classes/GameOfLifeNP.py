import numpy as np


class GameOfLife:
    """Represents a generalized Conway's Game of Life.
    The game is an n-dimensional array (n >= 2) of boolean values. Each cell is either alive (True) or dead (False).
    On each iteration the cells are updated as follows:
        - An alive cell stays alive if it has between `a` and `b` live neighbours
        - A dead cell becomes alive if it has between `c` and `d` live neighbours
        - Otherwise a cell dies
    The board has wraparound edges, so the neighbours of edge cell are located on the opposite edge.

    Fields:
        board: the current state of the game, n-dimensional array of type bool
        a: minimal number of live neighbours for a cell to stay alive
        b: maximal number of live neighbours for a cell to stay alive
        c: minimal number of live neighbours for a cell to become alive
        d: maximal number of live neighbours for a cell to become alive
    """

    def __init__(self, board: np.ndarray,
                 a: int = 2, b: int = 3,
                 c: int = 3, d: int = 3):
        """Initializes `board` and game rule fields. `board` must be stored as a copy"""
        self.board = board.copy()
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def next_iteration(self) -> None:
        """Computes the next iteration of the game. Invalidates `self.board`"""
        num_nei = np.zeros_like(self.board, int) + self.board
        num_nei += np.roll(self.board, 1, axis=0)
        num_nei += np.roll(self.board, -1, axis=0)
        for i in range(1, len(np.shape(self.board))):
            trans_ar = num_nei.copy()
            num_nei += np.roll(trans_ar, 1, axis=i)
            num_nei += np.roll(trans_ar, -1, axis=i)
        num_nei -= self.board
        stay_alive = np.logical_and(self.board, np.logical_and(num_nei >= self.a, num_nei <= self.b))
        revive = np.logical_and(np.logical_not(self.board), np.logical_and(num_nei >= self.c, num_nei <= self.d))
        self.board = np.logical_or(stay_alive, revive)


matrix = np.array([[True, False, True, True],
                   [False, False, False, False],
                   [True, True, False, False]])

game = GameOfLife(matrix, 3, 6, 5, 10)
game.next_iteration()
print(game.board)
