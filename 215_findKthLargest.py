'''
215. Kth Largest Element in an Array
Medium

https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
class Solution:
    # 快排 O(nlogn)
    # def findKthLargest(self, nums, k: int) -> int:
    #     left = 0
    #     right = len(nums)-1
    #     nums = self.quickSort(left,right,nums)
    #     print(nums)
    #     return nums[k-1]
    #
    #
    # def quickSort(self,left,right,nums):
    #     if  left<right:
    #         partitionIndex = self.partition(left, right, nums)
    #         self.quickSort(left,partitionIndex - 1,nums)
    #         self.quickSort(partitionIndex + 1,right,nums)
    #     return nums
    #
    # def partition(self,left,right,nums):
    #     pivot = left
    #     index = pivot+1
    #     for i in range(index,right+1):
    #         if nums[i]>nums[pivot]:
    #             nums[i],nums[index] = nums[index],nums[i]
    #             index += 1
    #     nums[pivot],nums[index-1] = nums[index-1],nums[pivot]
    #     return index-1

    # 快排思想 O(n)
    def findKthLargest(self, nums, k: int) -> int:
        low =0
        high = len(nums)-1
        return self.findKth(nums,low,high,k)

    def findKth(self,nums,low,high,k):
        index = (self.partition(nums,low,high))[0]
        if index==k:
            return nums[index]
        if index<k:
            return self.findKth(nums,index+1,high,k)
        else:
            return self.findKth(nums,low,index-1,k)

    def partition(self,nums,low,high):
        pivot = nums[low]
        while low<high:
            while low<high and nums[high]>pivot:
                high-=1
            while low<high and nums[low]<pivot:
                low+=1
            nums[low],nums[high] = nums[high],nums[low]
        nums[high] = pivot
        return high,nums


sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
ans = sol.findKthLargest(nums,k)
print(ans)