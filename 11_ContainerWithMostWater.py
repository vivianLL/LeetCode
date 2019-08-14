'''
11. Container With Most Water
Medium

https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
'''
class Solution:
    def maxArea(self, height) -> int:
        maxArea = 0
        left = 0
        right = len(height)-1
        while left < right:
            Area = min(height[left],height[right]) * (right-left)
            if Area > maxArea:
                maxArea = Area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

sol = Solution()
ans = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)

# 思路：双指针法 直线之间形成的面积总是受到较短直线高度的限制。线越长，得到的面积就越大。
# 我们取两个指针，一个在数组的开头，一个在数组的末尾，组成了行长度。