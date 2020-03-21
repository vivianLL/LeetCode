'''
365. 水壶问题
Medium

https://leetcode-cn.com/problems/water-and-jug-problem/
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
你允许：
装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
'''
import math

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # # 数学解法 每次操作只会给水的总量带来 x 或者 y 的变化量。贝祖定理 存在一对整数a, b使ax+by=z有解当且仅当z是x,y的最大公约数的倍数。
        # if x + y < z:
        #     return False
        # if x == 0 or y == 0:
        #     return z == 0 or x + y == z
        # return z % math.gcd(x, y) == 0

        # 深度优先搜索
        stack = [(0, 0)]
        self.seen = set()   # 存储所有已经搜索过的 remain_x, remain_y 状态，保证每个状态至多只被搜索一次。
        while stack:
            remain_x, remain_y = stack.pop()     # X壶和Y壶中的水量
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False


sol = Solution()
ans = sol.canMeasureWater(3,5,4)
print(ans)

# 注意：在实际的代码编写中，由于深度优先搜索导致的递归远远超过了 Python 的默认递归层数（可以使用 sys 库更改递归层数，但不推荐这么做），
# 因此下面的代码使用栈来模拟递归，避免了真正使用递归而导致的问题。