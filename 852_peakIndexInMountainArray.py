# def findPeak(nums):
#     线性搜索 Time Complexity: O(N) Space Complexity: O(1)
#     if nums:
#         if len(nums) == 1:
#             return 0
#         if nums[0] > nums[1]: #数组单调递减
#             return 0
#         index = len(nums)-1
#         if nums[index] > nums[index-1] : #数组单调递增
#             return index
#         #循环n-1次
#         for i in range(index):
#             if (nums[i] > nums[i+1]) :
#                 return i          #nums[i]
#
#     return -1

def findPeak(nums):
    # 二分搜索 Time Complexity: O(log N) Space Complexity: O(1).
    if nums:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]: #数组单调递减
            return 0
        index = len(nums)-1
        if nums[index] > nums[index-1] : #数组单调递增
            return index
        i = 0
        j = index
        while i<=j:
            mid = (i + j) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:     # 处于下坡段, 即递减段
                j = mid - 1
            elif nums[mid] > nums[mid - 1]:     # 处于上坡段, 即递增段
                i = mid + 1

    return -1



print(findPeak([1,2,11,9,6,5,2]))
