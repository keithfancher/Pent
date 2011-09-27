#!/usr/bin/env python

import unittest

from board import Board
from settings import BLACK as b # makes life easier below
from settings import WHITE as w # ditto
from settings import TIE


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
        for row in xrange(1, 6):
            self.board._board[row][0] = w
        self.assertEqual(self.board._check_cols_for_winner(), w)
        self.board._clear()
        for row in xrange(0, 5):
            self.board._board[row][5] = w
        self.assertEqual(self.board._check_cols_for_winner(), w)

    def test_winning_cols_black(self):
        """Various winning positions for black should return BLACK"""
        for row in xrange(1, 6):
            self.board._board[row][0] = b
        self.assertEqual(self.board._check_cols_for_winner(), b)
        self.board._clear()
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


if __name__ == "__main__":
    unittest.main()
