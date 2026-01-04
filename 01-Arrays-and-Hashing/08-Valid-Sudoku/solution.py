"""
Valid Sudoku
LeetCode 36

Problem: 

Approach:

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        # Check row
        for r in board:
            seen = set()
            for num in r:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        # Check columns
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[c][r] == ".":
                    continue
                if board[c][r] in seen:
                    return False
                seen.add(board[c][r])
        
        # Check 3 x 3
        squares = defaultdict(set) # key = (r/3, c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                sq_idx = (r//3,c//3)
                if board[r][c] in squares[sq_idx]:
                    return False
                else:
                    squares[sq_idx].add(board[r][c])

        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    board1 = [["1","2",".",".","3",".",".",".","."],
              ["4",".",".","5",".",".",".",".","."],
              [".","9","8",".",".",".",".",".","3"],
              ["5",".",".",".","6",".",".",".","4"],
              [".",".",".","8",".","3",".",".","5"],
              ["7",".",".",".","2",".",".",".","6"],
              [".",".",".",".",".",".","2",".","."],
              [".",".",".","4","1","9",".",".","8"],
              [".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(board1))

    board2 = [["1","2",".",".","3",".",".",".","."],
              ["4",".",".","5",".",".",".",".","."],
              [".","9","1",".",".",".",".",".","3"],
              ["5",".",".",".","6",".",".",".","4"],
              [".",".",".","8",".","3",".",".","5"],
              ["7",".",".",".","2",".",".",".","6"],
              [".",".",".",".",".",".","2",".","."],
              [".",".",".","4","1","9",".",".","8"],
              [".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(board2))
    # TODO: Add test cases
    pass
