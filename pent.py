#!/usr/bin/env python

import pygame

from board import Board
from util import shut_down
from settings import *


def main():
    pygame.init()
    pygame.display.set_caption('Pent')
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
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
                    if winner == TIE:
                        print "Tie game..."
                    elif winner == WHITE:
                        print "White won..."
                    elif winner == BLACK:
                        print "Black won..."
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
