#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from gameboard.board import Board
from gameboard.coordinate import Coordinate

class ShipSinker:
    """This is the class where all the magic happens. Given a board you should decide on a position to shoot at."""
    def make_move(self, board):
        # You get a board-object.

        for y in range(board.size()):
            for x in range(board.size()):
                if (self.get(board, x, y) == None):
                    return Coordinate(x, y)

    def get(self, board, x, y):
        for shot in board.shots():
            if (shot["coordinates"]["x"] == x and shot["coordinates"]["y"] == y):
                return shot
        return None