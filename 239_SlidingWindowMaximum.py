'''
239. Sliding Window Maximum
Hard

https://leetcode.com/problems/sliding-window-maximum/
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
'''
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        # # 时间复杂度O(nk) 需要考虑较多特殊情况
        # if not nums or not k:
        #     return []
        # elif k > len(nums):
        #     return False
        # elif len(nums)==1:
        #     return nums
        # elif len(nums)==2:
        #     if k==2:
        #         return [max(nums)]   # 注意返回列表形式而非int
        #     if k==1:
        #         return nums
        # else:
        #     output = []
        #     for i in range(len(nums)-k+1):
        #         output.append(max(nums[i:i+k]))
        #     return output

        # 时间复杂度O(n)
        if len(nums) < k or len(nums) == 0:
            return []

        n = len(nums)
        maxid = -1
        res = [0] * (n - k + 1)
        for i in range(n - k + 1):
            if maxid < i:                 # 说明最大值不在当前滑动窗口内，本次需要重新在滑动窗口内计算最大值
                maxid = i
                for j in range(i, i + k):
                    if nums[j] > nums[maxid]:
                        maxid = j
            else:
                if nums[maxid] < nums[i + k - 1]:  # 当前最大值和滑动窗口最后一个元素比较
                    maxid = i + k - 1
            res[i] = nums[maxid]
        return res

sol = Solution()
ans = sol.maxSlidingWindow([2,3,4,2,6,2,5,1],3)
print(ans)
ans = sol.maxSlidingWindow([1,-1],2)
print(ans)
ans = sol.maxSlidingWindow([],0)
print(ans)