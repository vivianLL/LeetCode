'''
79. Word Search
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Solution:
    # def exist(self, board, word):
    #     """
    #     :type board: List[List[str]]
    #     :type word: str
    #     :rtype: bool
    #     """
    #     if not board:
    #         return False
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if self.dfs(board, i, j, word):  # 判断从board[i][j]开始能否找到路径
    #                 return True
    #     return False
    #
    #
    # def dfs(self, board, i, j, word):
    #     if len(word) == 0:  # all the characters are checked
    #         return True
    #     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
    #         return False
    #     tmp = board[i][j]  # first character is found, check the remaining part 通过tmp临时替换的方式，避免重复访问
    #     board[i][j] = "#"  # avoid visit agian
    #     # check whether can find "word" along one direction
    #     res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
    #           or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
    #     board[i][j] = tmp
    #     return res

    def exist(self, board, word):
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True

        return False

    def getWords(self, board, word, i, j, visited, pos=0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True  #(i,j)未访问
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
              or self.getWords(board, word, i, j - 1, visited, pos + 1) \
              or self.getWords(board, word, i + 1, j, visited, pos + 1) \
              or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False  #(i,j)已访问
        print(visited)

        return res

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given_word = "ABCCED"

sol = Solution()
ans = sol.exist(board, Given_word)
print(ans)

# 思路：深度优先搜索 注意从哪一层哪一步开始递归，怎样搜索word的下一个字符，递归结束的标志，矩阵i,j越界在何处判断，怎样避免重复访问