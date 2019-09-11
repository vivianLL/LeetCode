'''
453. Minimum Moves to Equal Array Elements
Easy

https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
'''
class Solution:
    def minMoves(self, nums) -> int:
        # ans = 0
        # nums = sorted(nums)
        # for i in range(1,len(nums)):
        #     ans += nums[i]-nums[0]
        # return ans

        target = min(nums)
        n = len(nums)

        return sum(nums) - target * n

sol = Solution()
ans = sol.minMoves([1,2,3])
print(ans)