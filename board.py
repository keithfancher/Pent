import pygame

from settings import *


class Board(pygame.sprite.Sprite):
    _board = [ [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0] ]

    def __init__(self, position):
        """Construct..."""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect(center=position)

    def update(self):
        """Draws all the board's marbles"""
        for row in xrange(0, 6):
            for col in xrange(0, 6):
                self._draw_marble(self._board[row][col], row, col)

    def make_move(self, color, mouse_coordinates):
        """Attempts to make a move at the given screen coordinates. Returns
        True if move is valid, False otherwise"""
        # adjust screen coordinates to board coordinates
        real_x, real_y = mouse_coordinates
        real_x -= self.rect.left
        real_y -= self.rect.top

        # then to block coords, not pixels
        col = real_x / BLOCK_SIZE
        row = real_y / BLOCK_SIZE
        return self._add_marble(color, row, col)

    def winner(self):
        """Returns BLACK or WHITE or False"""
        # TODO: also handle ties
        return self._check_rows_for_winner() or\
               self._check_cols_for_winner() or\
               self._check_diags_for_winner()

    def _add_marble(self, color, row, col):
        """Attempts to add a marble to the board at the given row and column.
        Returns True if position is valid, False otherwise"""
        if row > 5 or row < 0 or col > 5 or col < 0: # out of bounds
            return False
        if self._board[row][col]: # already a piece there
            return False

        self._board[row][col] = color # add to board array
        return True

    def _check_rows_for_winner(self):
        """Loops through each row checking for 5 in a row. Returns WHITE or
        BLACK, or False if nobody has won."""
        for row in xrange(0, 6):
            result = self._five_in_a_row(self._board[row])
            if result:
                return result
        return False

    def _check_cols_for_winner(self):
        """Loops through each column checking for 5 in a row. Returns WHITE or
        BLACK, or False if nobody has won."""
        for col in xrange(0, 6):
            column = [] # build a list of each column for easy checking
            for row in xrange(0, 6):
                column.append(self._board[row][col])
            result = self._five_in_a_row(column)
            if result:
                return result
        return False

    def _check_diags_for_winner(self):
        """Checks all six winning diagonal positions"""
        # the two main diagonals
        diag1 = []
        diag2 = []
        for i in xrange(0, 6):
            diag1.append(self._board[i][i]) # left to right
            diag2.append(self._board[5 - i][i]) # right to left
        result = self._five_in_a_row(diag1)
        if result:
            return result
        result = self._five_in_a_row(diag2)
        if result:
            return result

        # the four minor diagonals
        diag1 = []
        diag2 = []
        diag3 = []
        diag4 = []
        for i in xrange(0, 5):
            # left to right
            diag1.append(self._board[i + 1][i])
            diag2.append(self._board[i][i + 1])

            # right to left
            diag3.append(self._board[4 - i][i])
            diag4.append(self._board[5 - i][i + 1])
        result = self._five_in_a_row(diag1)
        if result:
            return result
        result = self._five_in_a_row(diag2)
        if result:
            return result
        result = self._five_in_a_row(diag3)
        if result:
            return result
        result = self._five_in_a_row(diag4)
        if result:
            return result

        return False

    def _draw_marble(self, color, row, col):
        """Blits a marble image onto the board's surface at given row and
        column. If color is 0, it just returns without doing anything."""
        if color:
            surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
            if color == WHITE:
                surface.fill(pygame.Color('white'))
            else:
                surface.fill(pygame.Color('black'))
            position = (col * BLOCK_SIZE, row * BLOCK_SIZE)
            rect = surface.get_rect(topleft=position)
            self.image.blit(surface, rect)

    def _five_in_a_row(self, in_list):
        """Takes a list, and returns WHITE or BLACK if it finds five in a row
        of that respective color. Returns False otherwise."""
        str_list = map(str, in_list) # so we can use join() and str functions
        joined = " ".join(str_list)
        white_win = "%d %d %d %d %d" % (WHITE, WHITE, WHITE, WHITE, WHITE)
        black_win = "%d %d %d %d %d" % (BLACK, BLACK, BLACK, BLACK, BLACK)
        if joined.find(white_win) != -1:
            return WHITE
        if joined.find(black_win) != -1:
            return BLACK
        return False
