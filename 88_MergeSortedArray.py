'''
88. Merge Sorted Array
Easy

https://leetcode.com/problems/merge-sorted-array/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 冒泡遍历 O(n^2)
        # count = 0
        # for i in range(len(nums2)):
        #     while (nums1[count] <= nums2[i] and count <= m + i - 1):    # 注意此处的m+i-1
        #         count = count + 1
        #     nums1.insert(count, nums2[i])
        #     count = count + 1
        #     del nums1[-1]
        # print(nums1)
        #
        # # 合并后排序 O(nlogn)
        # nums1[m:] = nums2
        # nums1.sort()

        #  分别定义i,j两个整形变量,作为指针, 指向当前A, B数组位置 循环比较A[i], B[j]位置上的值,小的则提取值放在结果数据, 同时对应的指针+1 另一个的指针不变.
        # 不是原地排序 报错
        result = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        result += nums1[i:m]
        result += nums2[j:]
        nums1 = result
        print(nums1)


sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1,m,nums2,n)