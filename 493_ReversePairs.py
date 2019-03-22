'''
493. Reverse Pairs
Hard

https://leetcode.com/problems/reverse-pairs/
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.
'''
class Solution:
    def reversePairs(self, nums):
        # # 时间复杂度O(n^2) 超时
        # if not nums or len(nums)==1:
        #     return 0
        # pairs = []
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>2*nums[j]:
        #             pairs.append([nums[i], nums[j]])  # 若重复逆序对只算一个，则需加判断if [nums[i],nums[j]] not in pairs:
        # print(pairs)
        # return len(pairs)

        # 归并排序 时间复杂度O(nlogn) 时间复杂度O(n)
        if not nums:
            return 0
        res = self.merge_sort_count(nums, 0, len(nums) - 1)
        return res

    def merge_sort_count(self, nums, st, end):
        if st == end:
            return 0
        mid = (end + st) // 2
        cnt = 0
        cnt += self.merge_sort_count(nums, st, mid)
        cnt += self.merge_sort_count(nums, mid + 1, end)

        i, j = st, mid + 1
        while i <= mid and j <= end:
            if nums[i] > nums[j] * 2:
                cnt += mid + 1 - i      # nums[i]后面到nums[mid-1]的数都是大于nums[i]的，所以若nums[i] > nums[j] * 2，则mid + 1 - i个数都> nums[j] * 2
                j += 1
            else:
                i += 1
        nums[st:end + 1] = sorted(nums[st:end + 1])
        return cnt


sol = Solution()
ans = sol.reversePairs([2,4,3,5,1])
print(ans)
# ans = sol.reversePairs([1,3,2,3,1])
# print(ans)

# 思路：归并排序的改进版，把数据分成前后两个数组(递归分到每个数组仅有一个数据项)。合并数组，合并时，出现前面的数组值array[i]大于后面数组值array[j]时；则前面数组array[i]~array[mid]（因为前面的数组已经排序，array[i]后面到array[mid-1]的数都是大于array[i]的）都是大于array[j]的，count += mid+1 - i。这个思路来自牛客网中的一位
