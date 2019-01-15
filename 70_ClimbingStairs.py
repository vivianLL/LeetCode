'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划问题，与509题同理，多种解法不再赘述
        if n == 0 or n == 1:
            return n
        fbn1 = 0
        fbn2 = 1
        for i in range(0, n):
            tmp = fbn1 + fbn2;
            fbn1 = fbn2;
            fbn2 = tmp;
        return fbn2

sol = Solution()
ans = sol.climbStairs(6)
print(ans)

# 思路：我们把n级台阶的跳法看成是n的函数，记为f(n),当n>2时，第一次调的时候就有两种不同的选择，一是第一次跳一级，则此时的跳法数目等于后面剩下的n-1级台阶的跳法数目，即为f(n-1)；另一种选择是一次跳2级，此时跳法数目等于后面剩下的n-2级台阶跳法数目，即为f(n-2).因此n级台阶不同跳法总数f(n)=f(n-1)+f(n-2).分析到这里，我们不难看出这就是斐波拉契数列了。