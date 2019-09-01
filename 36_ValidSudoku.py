'''
36. Valid Sudoku
Medium

https://leetcode.com/problems/valid-sudoku/
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''
class Solution:
    def isValidSudoku(self, board) -> bool:
        # # 自写程序 冗余多 较慢
        # if not board:
        #     return False
        # n = len(board)
        # m = len(board[0])
        # if n%3!=0 or m%3!=0:
        #     return False
        #
        # for i in range(n):
        #     listline = []
        #     listcol = []
        #     for j in range(m):
        #         if board[i][j] != '.':
        #             listline.append(board[i][j])
        #         if board[j][i] != '.':
        #             listcol.append(board[j][i])
        #         if board[i][j] not in '123456789.':
        #             return False
        #
        #         if i%3==0 and j%3==0:
        #             matrix = [x[j:j + 3] for x in board[i:i + 3]]
        #             listmatrix = [i for j in matrix for i in j if i!='.']
        #             if len(set(listmatrix)) != len(listmatrix):
        #                 return False
        #
        #     if len(set(listline))!=len(listline) or len(set(listcol))!=len(listcol):   # 长度相等而非直接相等
        #         return False
        #
        # return True

        # 快速方法 用三个矩阵分别检查三个规则是否有重复数字，比如用row, col, block分别检查行、列、块是否有重复数字
        row = {}
        col = {}
        block = {}
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y != ".":
                    if (i, y) in row or (j, y) in col or (i // 3, j // 3, y) in block:
                        return False
                    else:
                        row[i, y] = 1
                        col[j, y] = 1
                        block[i // 3, j // 3, y] = 1
        return True

sol = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# board = [
#     [".",".","4",".",".",".","6","3","."],
#     [".",".",".",".",".",".",".",".","."],
#     ["5",".",".",".",".",".",".","9","."],
#     [".",".",".","5","6",".",".",".","."],
#     ["4",".","3",".",".",".",".",".","1"],
#     [".",".",".","7",".",".",".",".","."],
#     [".",".",".","5",".",".",".",".","."],
#     [".",".",".",".",".",".",".",".","."],
#     [".",".",".",".",".",".",".",".","."]
# ]
# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
ans = sol.isValidSudoku(board)
print(ans)

# 注意：不考虑可解性，每一整行和每一整列（9个元素）都不能重复，而不仅是小的3x3矩阵里的行和列不能重复。