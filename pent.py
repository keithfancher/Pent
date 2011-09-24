#!/usr/bin/env python

import pygame

from util import shut_down


SCREEN_W = 600
SCREEN_H = 600
FPS = 40


class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((600, 600))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()


class Marble(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((80, 80))
        self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect()


def main():
    """ My main() man!"""
    pygame.init()
    pygame.display.set_caption('Pent')
    screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.RenderPlain()

    board = Board()
    test_marble = Marble()
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
