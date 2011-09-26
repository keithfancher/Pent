#!/usr/bin/env python


import unittest

from board import Board, Marble
from settings import BLACK, WHITE


class TestRowWinner(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_empty_board(self):
        """Empty board should return False"""
        self.assertFalse(self.board._check_rows_for_winner())

    def test_winning_rows_white(self):
        """Various winning positions for white should return WHITE"""
        w = Marble(WHITE, (0, 0)) # position doesn't actually matter here
        self.board._board[0] = [0, w, w, w, w, w]
        self.assertEqual(self.board._check_rows_for_winner(), WHITE)
        self.board._board[0] = [w, w, w, w, w, 0]
        self.assertEqual(self.board._check_rows_for_winner(), WHITE)
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[5] = [w, w, w, w, w, w]
        self.assertEqual(self.board._check_rows_for_winner(), WHITE)

    def test_winning_rows_black(self):
        """Various winning positions for black should return BLACK"""
        b = Marble(BLACK, (0, 0)) # position doesn't actually matter here
        self.board._board[0] = [0, b, b, b, b, b]
        self.assertEqual(self.board._check_rows_for_winner(), BLACK)
        self.board._board[0] = [b, b, b, b, b, 0]
        self.assertEqual(self.board._check_rows_for_winner(), BLACK)
        self.board._board[0] = [0, 0, 0, 0, 0, 0]
        self.board._board[5] = [b, b, b, b, b, b]
        self.assertEqual(self.board._check_rows_for_winner(), BLACK)

    def test_non_winning_positions(self):
        """Various non-winning positions should return False"""
        w = Marble(WHITE, (0, 0))
        b = Marble(BLACK, (0, 0))
        self.board._board[0] = [w, w, w, b, b, b]
        self.board._board[1] = [b, w, w, b, b, b]
        self.board._board[2] = [b, w, b, b, b, b]
        self.board._board[3] = [w, w, w, w, 0, w]
        self.assertFalse(self.board._check_rows_for_winner())


class TestColWinner(unittest.TestCase):

    def setUp(self):
        self.board = Board((400, 400))

    def test_empty_board(self):
        "Empty board should return False"""
        self.assertFalse(self.board._check_cols_for_winner())

    def test_winning_cols_white(self):
        """Various winning positions for white should return WHITE"""
        w = Marble(WHITE, (0, 0))
        for row in xrange(1, 6):
            self.board._board[row][0] = w
        self.assertEqual(self.board._check_cols_for_winner(), WHITE)
        for row in xrange(1, 6): # clear out previous winner
            self.board._board[row][0] = 0
        for row in xrange(0, 5):
            self.board._board[row][5] = w
        self.assertEqual(self.board._check_cols_for_winner(), WHITE)

    def test_winning_cols_black(self):
        """Various winning positions for black should return BLACK"""
        b = Marble(BLACK, (0, 0))
        for row in xrange(1, 6):
            self.board._board[row][0] = b
        self.assertEqual(self.board._check_cols_for_winner(), BLACK)
        for row in xrange(1, 6): # clear out previous winner
            self.board._board[row][0] = 0
        for row in xrange(0, 5):
            self.board._board[row][5] = b
        self.assertEqual(self.board._check_cols_for_winner(), BLACK)

    def test_non_winning_positions(self):
        """Various non-winning positions should return False"""
        w = Marble(WHITE, (0, 0))
        b = Marble(BLACK, (0, 0))
        self.board._board[0] = [w, w, w, b, b, b]
        self.board._board[1] = [b, w, w, b, b, b]
        self.board._board[2] = [b, w, b, b, b, b]
        self.board._board[3] = [w, 0, w, w, 0, w]
        self.board._board[4] = [w, w, w, w, 0, w]
        self.board._board[5] = [w, w, w, w, 0, w]
        self.assertFalse(self.board._check_cols_for_winner())


class TestDiagWinner(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == "__main__":
    unittest.main()
