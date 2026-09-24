from typing import List

# main section of intialization section 
class WordSearch:
    def __init__(self, board: List[List[str]]):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0]) if board else 0

    def exists(self, word: str) -> bool:
        if not self.board or not word:
            return False

        for row in range(self.rows):
            for col in range(self.cols):
                if self._search(row, col, word, 0, set()):
                    return True

        return False

    def _search(
        self,
        row: int,
        col: int,
        word: str,
        index: int,
        visited: set
    ) -> bool:
      

        # We found the complete word
        if index == len(word):
            return True

        # Check boundaries
        if (
            row < 0
            or row >= self.rows
            or col < 0
            or col >= self.cols
        ):
            return False

        # Don't use the same cell twice
        if (row, col) in visited:
            return False

        # Current cell doesn't match the required character
        if self.board[row][col] != word[index]:
            return False

        # Choose this cell
        visited.add((row, col))

        # Explore four possible directions
        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1)    # left
        ]

        for row_change, col_change in directions:
            next_row = row + row_change
            next_col = col + col_change

            if self._search(
                next_row,
                next_col,
                word,
                index + 1,
                visited
            ):
                return True

        # Backtrack:
        # remove this cell so another path can use it
        visited.remove((row, col))

        return False


# Example
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"

search = WordSearch(board)

result = search.exists(word)

print(result)
