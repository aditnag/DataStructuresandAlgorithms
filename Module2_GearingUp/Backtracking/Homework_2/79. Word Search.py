from typing import List


class Solution:
    def __init__(self):
        self.board = None
        self.cols = None
        self.rows = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, word):
        if len(word) == 0:
            return True

        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.board[row][col] != word[0]:
            return False

        # res = False
        original_char = self.board[row][col]
        self.board[row][col] = "#"
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if self.backtrack(row + dr, col + dc, word[1:]):
                return True
        self.board[row][col] = original_char
        return False
