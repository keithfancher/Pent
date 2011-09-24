#!/usr/bin/env python

import pygame

from util import shut_down


# Pygame constants
SCREEN_W = 800
SCREEN_H = 800
FPS = 40

# Player constants
WHITE = 1
BLACK = 0


class Board(pygame.sprite.Sprite):
    _board = [ [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0] ]

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((600, 600))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect(center=position)

        # test...
        self._board[0][2] = Marble(WHITE)
        self._board[1][2] = Marble(BLACK)

    def update(self):
        for row in xrange(0, 6):
            for col in xrange(0, 6):
                if self._board[row][col]:
                    if self._board[row][col].color == WHITE:
                        pass
                    else:
                        pass


class Marble(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.image = pygame.Surface((80, 80))
        if self.color == WHITE:
            self.image.fill(pygame.Color('white'))
        else:
            self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect()


def main():
    """ My main() man!"""
    pygame.init()
    pygame.display.set_caption('Pent')
    screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.RenderPlain()

    board = Board(screen.get_rect().center)
    test_marble = Marble(WHITE)
    all_sprites.add(board)
    all_sprites.add(test_marble)

    # Main event loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shut_down(screen)

            # Set the speed based on the key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shut_down(screen)

            # Reset speed when key goes up
            if event.type == pygame.KEYUP:
                pass

            # Update the cursor position
            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

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
