# -*- coding:utf-8 -*-
'''
剑指offer面试题13 牛客网[编程题]机器人的运动范围
https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
class Solution:
    # 判断数位求和是否大于阈值
    def allow(self, threshold, row, col):
        n = 0
        while row != 0:
            n += row % 10
            row = row // 10
        while col != 0:
            n += col % 10
            col = col // 10

        if n > threshold:
            return False
        else:
            return True

    def find(self, threshold, visited_matrix, rows, cols, row, col):
        """
        本函数用于递归查找，并计算个数
        :param threshold:
        :param visited_matrix:
        :param rows:
        :param cols:
        :param row:
        :param col:
        :return:
        """
        count = 0
        if row >= 0 and col >= 0 and row < rows and col < cols and self.allow(threshold, row, col) and \
                visited_matrix[row][col] != 1:
            visited_matrix[row][col] = 1  # 如果访问过就设为1
            count += 1
            count += self.find(threshold, visited_matrix, rows, cols, row - 1, col) + \
                     self.find(threshold, visited_matrix, rows, cols, row + 1, col) + \
                     self.find(threshold, visited_matrix, rows, cols, row, col - 1) + \
                     self.find(threshold, visited_matrix, rows, cols, row, col + 1)
        return count

    def movingCount(self, threshold, rows, cols):
        # write code here
        if (rows < 0 or cols < 0 or threshold < 0):
            return 0
        visited_matrix = [[0] * cols for i in range(rows)]
        return self.find(threshold, visited_matrix, rows, cols, 0, 0)




# 这是一个典型的回溯法问题，我们从 (0, 0) 点开始，每次朝上下左右四个方向扩展新的节点即可。
#
# 扩展时需要注意新的节点需要满足如下条件：
#
# 之前没有遍历过，这个可以用个bool数组来判断；这个bool矩阵是DFS中的典型辅助矩阵
# 没有走出边界；
# 横纵坐标的各位数字之和小于 k；