#!/usr/bin/env python

import pygame

from util import shut_down


# Pygame constants
SCREEN_W = 800
SCREEN_H = 800
FPS = 40

# Player constants
WHITE = 1
BLACK = -1

# In pixels, of course
BOARD_SIZE = 600
BLOCK_SIZE = BOARD_SIZE / 6


class Board(pygame.sprite.Sprite):
    _board = [ [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0] ]

    _marbles = pygame.sprite.RenderPlain()
    _block_width = BOARD_SIZE / 6

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self._marbles.draw(self.image) # blit marbles onto game board

    def make_move(self, color, mouse_coordinates):
        """returns True if move is valid, False otherwise"""

        # adjust screen coordinates to board coordinates
        real_x, real_y = mouse_coordinates
        real_x -= self.rect.left
        real_y -= self.rect.top

        # then to block coords, not pixels
        col = real_x / BLOCK_SIZE
        row = real_y / BLOCK_SIZE
        return self._add_marble(color, row, col)

    def winner(self):
        """returns BLACK or WHITE or False"""
        # TODO: also handle ties
        return self._check_rows_for_winner() or\
               self._check_cols_for_winner() or\
               self._check_diags_for_winner()

    def _add_marble(self, color, row, col):
        """returns True if position is valid, False otherwise"""
        if row > 5 or row < 0 or col > 5 or col < 0: # out of bounds
            return False
        if self._board[row][col]: # already a piece there
            return False

        topleft = (col * BLOCK_SIZE, row * BLOCK_SIZE)
        new_marble = Marble(color, topleft)
        self._marbles.add(new_marble) # add to sprite group
        self._board[row][col] = new_marble # add to board array
        return True

    def _check_rows_for_winner(self):
        """returns WHITE or BLACK or False"""
        for row in xrange(0, 6):
            in_a_row = 1
            for col in xrange(1, 6): # don't test first block
                if self._check_equality(row, col, row, col - 1):
                    in_a_row += 1
                else:
                    in_a_row = 1

                if in_a_row >= 5:
                    return self._board[row][col].color
        return False

    def _check_cols_for_winner(self):
        # TODO
        return False

    def _check_diags_for_winner(self):
        # TODO
        return False

    def _check_equality(self, row1, col1, row2, col2):
        """helper function that makes checking for winners a bit cleaner"""
        if self._board[row1][col1] and self._board[row2][col2]:
            if self._board[row1][col1].color == self._board[row2][col2].color:
                return True

        return False


class Marble(pygame.sprite.Sprite):
    def __init__(self, color, position):
        pygame.sprite.Sprite.__init__(self)

        # TODO: error checking
        self.color = color
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        if self.color == WHITE:
            self.image.fill(pygame.Color('white'))
        else:
            self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect(topleft=position)


def main():
    """ My main() man!"""
    pygame.init()
    pygame.display.set_caption('Pent')
    screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.RenderPlain()

    board = Board(screen.get_rect().center)
    all_sprites.add(board)

    # White goes first for now
    current_player = WHITE

    # Main event loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shut_down(screen)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shut_down(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.make_move(current_player, pygame.mouse.get_pos()):
                    winner = board.winner()
                    if winner:
                        print "Somebody won I guess"
                    current_player = -current_player

        # Clear screen
        screen.fill(pygame.Color('black'))

        all_sprites.update()
        all_sprites.draw(screen)

        # Flip screen
        pygame.display.flip()

        # Pause
        clock.tick(FPS)


if __name__ == "__main__":
    main()
