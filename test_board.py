#!/usr/bin/env python

import unittest
import pygame

from board import Board
from settings import *
from settings import BLACK as b # makes life easier below
from settings import WHITE as w # ditto


class TestAllEqual(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_all_equal_true(self):
        """Lists with all equal values should return True"""
        l = [w, w, w,]
        self.assertTrue(self.board._all_equal(l))
        l = [w, w, w, w, w, w, w, w]
        self.assertTrue(self.board._all_equal(l))
        l = [b]
        self.assertTrue(self.board._all_equal(l))

    def test_all_equal_false(self):
        """Lists without all equal values should return False"""
        l = [w, b, w,]
        self.assertFalse(self.board._all_equal(l))
        l = [w, 0, w, b, w, w, w, 0]
        self.assertFalse(self.board._all_equal(l))
        l = [b, 0]
        self.assertFalse(self.board._all_equal(l))


class TestFiveInARow(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_five_in_a_row_white(self):
        """Lists with five+ whites in a row should return WHITE"""
        l = [0, w, w, w, w, w]
        self.assertEqual(self.board._five_in_a_row(l), w)
        l = [w, w, w, w, w, 0]
        self.assertEqual(self.board._five_in_a_row(l), w)
        l = [w, w, w, w, w, w]
        self.assertEqual(self.board._five_in_a_row(l), w)
        l = [w, w, w, w, w] # len 5 arr
        self.assertEqual(self.board._five_in_a_row(l), w)

    def test_five_in_a_row_black(self):
        """Lists with five+ blacks in a row should return BLACK"""
        l = [0, b, b, b, b, b]
        self.assertEqual(self.board._five_in_a_row(l), b)
        l = [b, b, b, b, b, 0]
        self.assertEqual(self.board._five_in_a_row(l), b)
        l = [b, b, b, b, b, b]
        self.assertEqual(self.board._five_in_a_row(l), b)
        l = [b, b, b, b, b] # len 5
        self.assertEqual(self.board._five_in_a_row(l), b)

    def test_no_five_in_a_row(self):
        """Lists without five in a row should return False"""
        l = [w, b, w, w, w, w]
        self.assertFalse(self.board._five_in_a_row(l))
        l = [w, b, w, w] # array too short
        self.assertFalse(self.board._five_in_a_row(l))
        l = [w, b, w, w, w, w, 0, 0] # too long
        self.assertFalse(self.board._five_in_a_row(l))
        l = [0, 0, 0, 0, 0, 0] # five 0s in a row
        self.assertFalse(self.board._five_in_a_row(l))


class TestRowWinner(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_empty_board(self):
        """Empty board should return False"""
        self.assertFalse(self.board._check_rows_for_winner())

    def test_winning_rows_white(self):
        """Various winning positions for white should return WHITE"""
        self.board._board[0] = [0, w, w, w, w, w]
        self.assertEqual(self.board._check_rows_for_winner(), w)
        self.board._board[0] = [w, w, w, w, w, 0]
        self.assertEqual(self.board._check_rows_for_winner(), w)
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[5] = [w, w, w, w, w, w]
        self.assertEqual(self.board._check_rows_for_winner(), w)

    def test_winning_rows_black(self):
        """Various winning positions for black should return BLACK"""
        self.board._board[0] = [0, b, b, b, b, b]
        self.assertEqual(self.board._check_rows_for_winner(), b)
        self.board._board[0] = [b, b, b, b, b, 0]
        self.assertEqual(self.board._check_rows_for_winner(), b)
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[5] = [b, b, b, b, b, b]
        self.assertEqual(self.board._check_rows_for_winner(), b)

    def test_non_winning_positions(self):
        """Various non-winning positions should return False"""
        self.board._board[0] = [w, b, w, w, w, w]
        self.board._board[1] = [b, w, w, b, b, b]
        self.board._board[2] = [b, w, b, b, b, b]
        self.board._board[3] = [0, 0, 0, w, 0, 0]
        self.board._board[4] = [w, w, 0, 0, 0, w]
        self.board._board[5] = [w, w, 0, w, 0, 0]
        self.assertFalse(self.board._check_rows_for_winner())


class TestColWinner(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_empty_board(self):
        "Empty board should return False"""
        self.assertFalse(self.board._check_cols_for_winner())

    def test_winning_cols_white(self):
        """Various winning positions for white should return WHITE"""
        for row in xrange(1, 6):
            self.board._board[row][0] = w
        self.assertEqual(self.board._check_cols_for_winner(), w)
        self.board.clear()
        for row in xrange(0, 5):
            self.board._board[row][5] = w
        self.assertEqual(self.board._check_cols_for_winner(), w)

    def test_winning_cols_black(self):
        """Various winning positions for black should return BLACK"""
        for row in xrange(1, 6):
            self.board._board[row][0] = b
        self.assertEqual(self.board._check_cols_for_winner(), b)
        self.board.clear()
        for row in xrange(0, 5):
            self.board._board[row][5] = b
        self.assertEqual(self.board._check_cols_for_winner(), b)

    def test_non_winning_positions(self):
        """Various non-winning positions should return False"""
        self.board._board[0] = [w, w, w, b, b, b]
        self.board._board[1] = [b, w, w, b, b, b]
        self.board._board[2] = [b, w, b, b, b, b]
        self.board._board[3] = [w, 0, w, w, 0, w]
        self.board._board[4] = [w, w, w, w, 0, w]
        self.board._board[5] = [w, w, w, w, 0, w]
        self.assertFalse(self.board._check_cols_for_winner())


class TestDiagWinner(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_empty_board(self):
        """Empty board should return False"""
        self.assertFalse(self.board._check_diags_for_winner())

    def test_main_diags_white(self):
        """Basic winning positions for white should return WHITE"""
        self.board._board[0] = [w, 0, 0, 0, 0, 0]
        self.board._board[1] = [0, w, 0, 0, 0, 0]
        self.board._board[2] = [0, 0, w, 0, 0, 0]
        self.board._board[3] = [0, 0, 0, w, 0, w]
        self.board._board[4] = [w, w, 0, 0, w, w]
        self.board._board[5] = [w, w, 0, w, 0, w]
        self.assertEqual(self.board._check_diags_for_winner(), w)
        self.board._board[0] = [w, 0, 0, 0, 0, w]
        self.board._board[1] = [0, 0, 0, 0, w, 0]
        self.board._board[2] = [0, 0, 0, w, 0, 0]
        self.board._board[3] = [0, 0, w, 0, 0, w]
        self.board._board[4] = [w, w, 0, 0, 0, w]
        self.board._board[5] = [w, w, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), w)

    def test_main_diags_black(self):
        """Basic winning positions for black should return BLACK"""
        self.board._board[0] = [b, 0, 0, 0, 0, 0]
        self.board._board[1] = [0, b, 0, 0, 0, 0]
        self.board._board[2] = [0, 0, b, 0, 0, 0]
        self.board._board[3] = [0, 0, 0, b, 0, w]
        self.board._board[4] = [w, w, 0, 0, b, w]
        self.board._board[5] = [w, w, 0, w, 0, b]
        self.assertEqual(self.board._check_diags_for_winner(), b)
        self.board._board[0] = [0, 0, 0, 0, 0, b]
        self.board._board[1] = [0, 0, 0, 0, b, 0]
        self.board._board[2] = [0, 0, 0, b, 0, 0]
        self.board._board[3] = [0, 0, b, 0, 0, w]
        self.board._board[4] = [w, b, 0, 0, b, w]
        self.board._board[5] = [b, w, 0, w, 0, b]
        self.assertEqual(self.board._check_diags_for_winner(), b)

    def test_minor_diags_white(self):
        """Basic winning positions for white should return WHITE"""
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[1] = [w, 0, 0, 0, 0, 0]
        self.board._board[2] = [0, w, 0, 0, 0, 0]
        self.board._board[3] = [0, 0, w, 0, 0, w]
        self.board._board[4] = [w, w, 0, w, 0, w]
        self.board._board[5] = [w, w, 0, w, w, 0]
        self.assertEqual(self.board._check_diags_for_winner(), w)
        self.board._board[0] = [0, w, 0, 0, 0, 0]
        self.board._board[1] = [0, 0, w, 0, 0, 0]
        self.board._board[2] = [0, 0, 0, w, 0, 0]
        self.board._board[3] = [0, 0, 0, 0, w, w]
        self.board._board[4] = [w, w, 0, 0, 0, w]
        self.board._board[5] = [w, w, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), w)
        self.board._board[0] = [0, 0, 0, 0, w, 0]
        self.board._board[1] = [0, 0, 0, w, 0, 0]
        self.board._board[2] = [0, 0, w, 0, 0, 0]
        self.board._board[3] = [0, w, 0, 0, 0, w]
        self.board._board[4] = [w, 0, 0, 0, 0, w]
        self.board._board[5] = [w, 0, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), w)
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[1] = [0, 0, 0, 0, 0, w]
        self.board._board[2] = [0, 0, 0, 0, w, 0]
        self.board._board[3] = [0, 0, 0, w, 0, w]
        self.board._board[4] = [0, 0, w, 0, 0, w]
        self.board._board[5] = [w, w, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), w)

    def test_minor_diags_black(self):
        """Basic winning positions for black should return BLACK"""
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[1] = [b, 0, 0, 0, 0, 0]
        self.board._board[2] = [0, b, 0, 0, 0, 0]
        self.board._board[3] = [0, 0, b, 0, 0, w]
        self.board._board[4] = [w, w, 0, b, 0, w]
        self.board._board[5] = [w, w, 0, w, b, 0]
        self.assertEqual(self.board._check_diags_for_winner(), b)
        self.board._board[0] = [0, b, 0, 0, 0, 0]
        self.board._board[1] = [0, 0, b, 0, 0, 0]
        self.board._board[2] = [0, 0, 0, b, 0, 0]
        self.board._board[3] = [0, 0, 0, 0, b, w]
        self.board._board[4] = [w, w, 0, 0, 0, b]
        self.board._board[5] = [w, w, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), b)
        self.board._board[0] = [0, 0, 0, 0, b, 0]
        self.board._board[1] = [0, 0, 0, b, 0, 0]
        self.board._board[2] = [0, 0, b, 0, 0, 0]
        self.board._board[3] = [0, b, 0, 0, 0, w]
        self.board._board[4] = [b, 0, 0, 0, 0, w]
        self.board._board[5] = [w, 0, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), b)
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[1] = [0, 0, 0, 0, 0, b]
        self.board._board[2] = [0, 0, 0, 0, b, 0]
        self.board._board[3] = [0, 0, 0, b, 0, w]
        self.board._board[4] = [0, 0, b, 0, 0, w]
        self.board._board[5] = [w, b, 0, w, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), b)


class TestTieGame(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_rows_tie(self):
        """Both players have won on rows should return TIE"""
        self.board._board[0] = [w, w, w, w, w, 0]
        self.board._board[1] = [0, 0, 0, 0, 0, 0]
        self.board._board[2] = [0, 0, 0, 0, 0, 0]
        self.board._board[3] = [0, 0, 0, 0, 0, 0]
        self.board._board[4] = [0, 0, 0, 0, 0, 0]
        self.board._board[5] = [0, b, b, b, b, b]
        self.assertEqual(self.board._check_rows_for_winner(), TIE)

    def test_cols_tie(self):
        """Both players have won on cols should return TIE"""
        self.board._board[0] = [w, 0, 0, 0, 0, 0]
        self.board._board[1] = [w, 0, 0, 0, 0, b]
        self.board._board[2] = [w, 0, 0, 0, 0, b]
        self.board._board[3] = [w, 0, 0, 0, 0, b]
        self.board._board[4] = [w, 0, 0, 0, 0, b]
        self.board._board[5] = [0, 0, 0, 0, 0, b]
        self.assertEqual(self.board._check_cols_for_winner(), TIE)

    def test_diag_tie(self):
        """Both players won on diags should return TIE"""
        self.board._board[0] = [w, 0, 0, 0, 0, 0]
        self.board._board[1] = [0, w, 0, 0, b, 0]
        self.board._board[2] = [0, 0, w, b, 0, 0]
        self.board._board[3] = [0, 0, b, w, 0, 0]
        self.board._board[4] = [0, b, 0, 0, w, 0]
        self.board._board[5] = [b, 0, 0, 0, 0, 0]
        self.assertEqual(self.board._check_diags_for_winner(), TIE)

    def test_mult_tie(self):
        """Both players win across multiple axes should return TIE"""
        self.board._board[0] = [w, 0, 0, 0, 0, 0]
        self.board._board[1] = [0, w, 0, 0, 0, 0]
        self.board._board[2] = [0, 0, w, 0, 0, 0]
        self.board._board[3] = [0, 0, 0, w, 0, 0]
        self.board._board[4] = [0, 0, 0, 0, w, 0]
        self.board._board[5] = [b, b, b, b, b, 0]
        self.assertEqual(self.board.winner(), TIE)


class QuadTest(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))
        self.board._board[0] = [0, 0, 0, b, b, b]
        self.board._board[1] = [0, 0, 0, b, b, b]
        self.board._board[2] = [0, 0, 0, b, b, b]
        self.board._board[3] = [w, w, w, w, b, b]
        self.board._board[4] = [w, w, w, b, 0, b]
        self.board._board[5] = [w, w, w, b, b, w]

    def test_get_quad(self):
        """get_quad should return the proper 3x3 array"""
        ret_quad = [ [b, b, b],
                     [b, b, b],
                     [b, b, b] ]
        self.assertEqual(self.board._get_quad(TOPRIGHT), ret_quad)
        ret_quad = [ [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0] ]
        self.assertEqual(self.board._get_quad(TOPLEFT), ret_quad)
        ret_quad = [ [w, w, w],
                     [w, w, w],
                     [w, w, w] ]
        self.assertEqual(self.board._get_quad(BOTLEFT), ret_quad)
        ret_quad = [ [w, b, b],
                     [b, 0, b],
                     [b, b, w] ]
        self.assertEqual(self.board._get_quad(BOTRIGHT), ret_quad)

    def test_set_quad(self):
        """set_quad should set the proper 3x3 subarray of the board"""
        target = [ [w, w, w, b, b, b],
                   [w, w, w, b, b, b],
                   [w, w, w, b, b, b],
                   [w, w, w, w, b, b],
                   [w, w, w, b, 0, b],
                   [w, w, w, b, b, w] ]
        set_quad = [ [w, w, w],
                     [w, w, w],
                     [w, w, w] ]
        self.board._set_quad(TOPLEFT, set_quad)
        self.assertEqual(self.board._board, target)
        target = [ [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, b, b],
                   [w, w, w, b, 0, b],
                   [w, w, w, b, b, w] ]
        self.board._set_quad(TOPRIGHT, set_quad)
        self.assertEqual(self.board._board, target)
        target = [ [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, w, w] ]
        self.board._set_quad(BOTRIGHT, set_quad)
        self.assertEqual(self.board._board, target)
        set_quad = [ [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0] ]
        target = [ [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [w, w, w, w, w, w],
                   [0, 0, 0, w, w, w],
                   [0, 0, 0, w, w, w],
                   [0, 0, 0, w, w, w] ]
        self.board._set_quad(BOTLEFT, set_quad)
        self.assertEqual(self.board._board, target)


class RotationTest(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))
        self.board._board = [ [w, 0, 0, 0, b, 0],
                              [0, w, 0, 0, 0, 0],
                              [0, 0, w, 0, b, 0],
                              [0, 0, 0, w, w, w],
                              [0, w, 0, w, w, 0],
                              [0, 0, 0, w, 0, 0] ]

    def test_rotate_clockwise(self):
        """rotate_quad should rotate the given quad clockwise"""
        target = [ [w, 0, 0, 0, 0, 0],
                   [0, w, 0, b, 0, b],
                   [0, 0, w, 0, 0, 0],
                   [0, 0, 0, w, w, w],
                   [0, w, 0, w, w, 0],
                   [0, 0, 0, w, 0, 0] ]
        self.board.rotate_quad(TOPRIGHT, CLOCKWISE)
        self.assertEqual(self.board._board, target)

    def test_rotate_counterclockwise(self):
        """rotate_quad should rotate the given quad clockwise"""
        target = [ [w, 0, 0, 0, b, 0],
                   [0, w, 0, 0, 0, 0],
                   [0, 0, w, 0, b, 0],
                   [0, 0, 0, w, 0, 0],
                   [0, w, 0, w, w, 0],
                   [0, 0, 0, w, w, w] ]
        self.board.rotate_quad(BOTRIGHT, COUNTERCLOCKWISE)
        self.assertEqual(self.board._board, target)


if __name__ == "__main__":
    # Have to init pygame or we can't create a Board object
    pygame.init()
    pygame.display.set_mode((1, 1))

    unittest.main()
