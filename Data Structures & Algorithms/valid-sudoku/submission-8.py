from collections import Counter

def is_valid_combination(combo: list[str]) -> bool:
    for item, count in Counter(combo).items():
        if item != '.' and count != 1:
            return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = all(is_valid_combination(row) for row in board)
        valid_cols = all(is_valid_combination(col) for col in zip(*board))

        flattened = [cell for row in board for cell in row]
        boxes = [
            [
                flattened[3*y + 27*x + 9*i + j]
                for i in range(3)
                for j in range(3)
            ]
            for x in range(3)
            for y in range(3)
        ]

        valid_boxes = all(is_valid_combination(box) for box in boxes)

        return valid_rows and valid_cols and valid_boxes
