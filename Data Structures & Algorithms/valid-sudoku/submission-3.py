from collections import Counter

def is_valid_combination(combo: list[str]) -> bool:
    for item, count in Counter(combo).items():
        if item != '.' and count != 1:
            return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not is_valid_combination(row):
                print(f'{row=}')
                return False

        for col in list(zip(*board)):
            if not is_valid_combination(col):
                print(f'{col=}')
                return False

        flattened = [cell for row in board for cell in row]
        # 0 -> 0  1  2  9  10 11 18 19 20
        # 1 -> 3  4  5  12 13 14 21 22 23
        # 2 -> 6  7  8  15 16 17 24 25 26
        # 4 -> 27 28 29 36 37 38
        # 5 -> 30 31 32 39 40 41
        # 6 -> 33 34 35 42 43 44
        # 3n (+1) (+2) (+9) (+10) (+11) (+18) (+19) (+20)

        indices = [0, 1, 2, 9, 10, 11, 18, 19, 20]

        boxes = [
            [flattened[3 * y + 27 * x + j] for j in indices]
            for x in range(3)
            for y in range(3)
        ]

        for box in boxes:
            print(box)
            if not is_valid_combination(box):
                print(f'{box=}')
                return False

        return True
