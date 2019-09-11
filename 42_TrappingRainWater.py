'''
42. Trapping Rain Water
Hard

https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''
class Solution:
    def trap(self, height) -> int:
        # # 方法一 左右扫描法 即 动态规划
        # if len(height) == 0 or len(height)==1:
        #     return 0
        #
        # n = len(height)
        #
        # left,right = [0]*n, [0]*n   # 每个位置都存放其左边最大值和右边最大值
        # temp = 0
        # for i in range(n):
        #     temp = max(temp,height[i])   # 找每个元素的左边最大值（含自身）
        #     left[i] = temp
        # temp = 0
        # for i in range(n-1,-1,-1):
        #     temp = max(temp,height[i])    # 找每个元素的右边最大值（含自身）
        #     right[i] = temp
        # res = 0
        # for i in range(n):
        #     res += min(left[i],right[i])-height[i]   # 最小的高度值-自身
        # return res

        # # 用栈法
        # if len(height) == 0 or len(height) == 1:
        #     return 0
        # ans = 0
        # current = 0
        # st = []
        # while current<len(height):
        #     while st!=[] and height[current]>height[st[-1]]:
        #         top = st[-1]
        #         st.pop()
        #         if st==[]:
        #             break
        #         distance = current - st[-1] - 1
        #         bounded_height = min(height[current],height[st[-1]]) - height[top]
        #         ans += distance * bounded_height
        #     st.append(current)
        #     current += 1
        # return ans

        # 双指针法
        if len(height) == 0 or len(height)==1:
            return 0
        left = 0
        right = len(height)-1
        area = 0
        leftwall, rightwall = 0, 0
        while left<right:
            if height[left]<height[right]:   # 右边高，则以右端为墙
                if leftwall>height[left]:    # 如果左墙也比当前位置高的话
                    area += min(leftwall,height[right])-height[left]    # 面积就是两墙最低者减去当前位置的高度
                else:
                    leftwall = height[left]   # 否则更新左墙
                left += 1
            else:
                if rightwall>height[right]:
                    area += min(rightwall,height[left])-height[right]
                else:
                    rightwall = height[right]
                right -= 1
        return area

sol = Solution()
ans = sol.trap([2,1,5,6,2,3])
print(ans)
# 左右扫描法思路：每个位置能接的雨水量是：当前位置左边最高的数与右边最高的数的最小值减去当前位置的数。
# 双指针法思路：当前位置需要左右两堵墙的最小值减去当前值。左右两端各设定一个指针，初始两堵墙。如果左端小于右端，则以右端为墙，当前值等于左墙和右墙的最小值减去当前值。
# 参考网址：https://www.cnblogs.com/king-lps/p/10789797.html