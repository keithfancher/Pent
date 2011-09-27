import pygame

from settings import *


class Board(pygame.sprite.Sprite):

    def __init__(self, position):
        """Construct..."""
        pygame.sprite.Sprite.__init__(self)

        # load images
        self.image = pygame.image.load("images/board.png").convert()
        self.rect = self.image.get_rect(center=position)
        self.marble_b = pygame.image.load("images/black.png").convert_alpha()
        self.marble_w = pygame.image.load("images/white.png").convert_alpha()

        # the board array
        self._board = [ [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0] ]

    def update(self):
        """Draws all the board's marbles, called every frame."""
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

    def clear(self):
        """Clears the board of marbles"""
        for row in xrange(0, 6):
            for col in xrange(0, 6):
                self._board[row][col] = 0

    def winner(self):
        """Returns BLACK, WHITE, TIE, or False"""
        white_wins = black_wins = False
        result = self._check_rows_for_winner()
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        elif result == TIE:
            return TIE # if we've already got two winners, no reason to go on

        result = self._check_cols_for_winner()
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        elif result == TIE:
            return TIE

        result = self._check_diags_for_winner()
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        elif result == TIE:
            return TIE

        if white_wins and black_wins:
            return TIE
        elif white_wins:
            return WHITE
        elif black_wins:
            return BLACK
        else:
            return False

    def _add_marble(self, color, row, col):
        """Attempts to add a marble to the board at the given row and column.
        Returns True if position is valid, False otherwise"""
        if row > 5 or row < 0 or col > 5 or col < 0: # out of bounds
            return False
        if self._board[row][col]: # already a piece there
            return False

        self._board[row][col] = color # add to board array
        return True

    def _draw_marble(self, color, row, col):
        """Blits a marble image onto the board's surface at given row and
        column. If color is 0, it just returns without doing anything."""
        if color:
            if color == WHITE:
                surface = self.marble_w
            elif color == BLACK:
                surface = self.marble_b
            position = (col * BLOCK_SIZE + 30, row * BLOCK_SIZE + 30)
            rect = surface.get_rect(topleft=position)
            self.image.blit(surface, rect)

    def _check_rows_for_winner(self):
        """Loops through each row checking for 5 in a row. Returns WHITE,
        BLACK, TIE, or False if nobody has won."""
        white_wins = black_wins = False
        for row in xrange(0, 6):
            result = self._five_in_a_row(self._board[row])
            if result == WHITE:
                white_wins = True
            elif result == BLACK:
                black_wins = True

        if white_wins and black_wins:
            return TIE
        elif white_wins:
            return WHITE
        elif black_wins:
            return BLACK
        else:
            return False

    def _check_cols_for_winner(self):
        """Loops through each column checking for 5 in a row. Returns WHITE or
        BLACK, or False if nobody has won."""
        white_wins = black_wins = False
        for col in xrange(0, 6):
            column = [] # build a list of each column for easy checking
            for row in xrange(0, 6):
                column.append(self._board[row][col])
            result = self._five_in_a_row(column)
            if result == WHITE:
                white_wins = True
            elif result == BLACK:
                black_wins = True

        if white_wins and black_wins:
            return TIE
        elif white_wins:
            return WHITE
        elif black_wins:
            return BLACK
        else:
            return False

    def _check_diags_for_winner(self):
        """Checks all six winning diagonal positions"""
        white_wins = black_wins = False

        # the two main diagonals
        diag1 = []
        diag2 = []
        for i in xrange(0, 6):
            diag1.append(self._board[i][i]) # left to right
            diag2.append(self._board[5 - i][i]) # right to left

        result = self._five_in_a_row(diag1)
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        result = self._five_in_a_row(diag2)
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True

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
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        result = self._five_in_a_row(diag2)
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        result = self._five_in_a_row(diag3)
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True
        result = self._five_in_a_row(diag4)
        if result == WHITE:
            white_wins = True
        elif result == BLACK:
            black_wins = True

        if white_wins and black_wins:
            return TIE
        elif white_wins:
            return WHITE
        elif black_wins:
            return BLACK
        else:
            return False

    def _five_in_a_row(self, in_list):
        """Takes a list, and returns WHITE or BLACK if it finds five in a row
        of that respective color. Returns False/0 otherwise. Note that this is
        a very Pentago-specific way of checking -- it only works for arrays of
        length 5 or 6, using array slicing."""
        if len(in_list) == 5:
            if self._all_equal(in_list):
                return in_list[0]

        if len(in_list) == 6:
            if self._all_equal(in_list[:4]):
                return in_list[0]
            if self._all_equal(in_list[1:]):
                return in_list[1]

        return False

    def _all_equal(self, in_list):
        """Li'l helper function that returns True if every element in a list is
        the same, False otherwise."""
        if in_list:
            filtered = filter(lambda x: x == in_list[0], in_list)
            if len(filtered) == len(in_list):
                return True
        return False
