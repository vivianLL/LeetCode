'''
4. Median of Two Sorted Arrays
Hard

https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        a = nums1 if l1 <= l2 else nums2  # short
        b = nums1 if l1 > l2 else nums2  # long
        k = (l1 + l2 + 1) // 2
        left = 0
        right = len(a)
        while left <= right:
            mid = (left + right) // 2
            if mid < right and b[k - mid - 1] > a[mid]:
                left = mid + 1
            elif mid > left and b[k - mid] < a[mid - 1]:
                right = mid - 1
            else:
                if mid == 0:
                    maxL = b[k - mid - 1]
                elif k - mid == 0:  # nums1 nums2长度相等时才可能等于0
                    maxL = a[mid - 1]
                else:
                    maxL = max(a[mid - 1], b[k - mid - 1])

                if (l1 + l2) % 2 == 0:
                    if mid == len(a):
                        minR = b[k - mid]
                    elif k - mid == len(b):
                        minR = a[mid]
                    else:
                        minR = min(a[mid], b[k - mid])
                    return (maxL + minR) / 2
                else:
                    return maxL

# 思路：找中位数，因为要求log的时间复杂度，所以应在两个未合并的有序数组之间使用二分法
# 需要考虑两数组长度和的奇偶，和i,j的边界条件
# 详见LeetCode里的solution