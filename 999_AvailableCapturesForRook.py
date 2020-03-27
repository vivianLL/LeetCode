'''
999. Available Captures for Rook
Easy

https://leetcode-cn.com/problems/available-captures-for-rook/
在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
返回车能够在一次移动中捕获到的卒的数量。
'''
class Solution:
    def numRookCaptures(self, board) -> int:
        # # 我的方法
        # count = 0
        # for i in range(8):
        #     for j in range(8):
        #         if board[i][j]=='R':
        #             q = i
        #             while q>0:
        #                 q -= 1
        #                 if board[q][j]=='B':
        #                     break
        #                 if board[q][j]=='p':
        #                     count += 1
        #                     break
        #             q = i
        #             while q<8-1:
        #                 q += 1
        #                 if board[q][j]=='B':
        #                     break
        #                 if board[q][j]=='p':
        #                     count += 1
        #                     break
        #             p = j
        #             while p>0:
        #                 p -= 1
        #                 if board[i][p]=='B':
        #                     break
        #                 if board[i][p]=='p':
        #                     count += 1
        #                     break
        #             p = j
        #             while p < 8-1:
        #                 p += 1
        #                 if board[i][p] == 'B':
        #                     break
        #                 if board[i][p] == 'p':
        #                     count += 1
        #                     break
        # return count

        # 方向数组
        cnt, st, ed = 0, 0, 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    st, ed = i, j
        for i in range(4):
            step = 0
            while True:
                tx = st + step * dx[i]
                ty = ed + step * dy[i]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                    break
                if board[tx][ty] == "p":
                    cnt += 1
                    break
                step += 1
        return cnt


l = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
l = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
l = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

sol = Solution()
ans = sol.numRookCaptures(l)
print(ans)

# 可以建立方向数组表示在这个方向上移动一步的增量，比如向北移动一步的时候，白色车的 x 轴坐标减 1，而 y 轴坐标不会变化，所以我们可以用 (-1, 0) 表示白色车向北移动一步的增量，其它三个方向同理。建立了方向数组，则白色车在某个方向移动 \textit{step}step 步的坐标增量就可以直接计算得到，比如向北移动 \textit{step}step 步的坐标增量即为 (-step, 0)。