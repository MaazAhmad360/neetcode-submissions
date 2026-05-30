class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = {}
        is_valid = True

        for i, r in enumerate(board):
            for j, c in enumerate(board[i]):
                if c != '.':
                    board_no = ((i // 3) * 3 + (j // 3))
                    if c not in sudoku:
                        sudoku[c] = [(i, j, board_no)]
                    else:
                        hit = any(
                            i == s[0] or 
                            j == s[1] or 
                            board_no == s[2] 
                            for s in sudoku[c]
                        )
                        if hit:
                            return False
                        sudoku[c].append((i, j, board_no))
        return True
            