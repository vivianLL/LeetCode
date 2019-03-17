'''
215. Kth Largest Element in an Array
Medium

https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
import heapq
class Solution:
    # # nums的大小很小时
    # def findKthLargest(self, nums, k: int) -> int:
    #     nums.sort()
    #     return nums[-k]

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

    # # 随机快排思想 O(n)
    # def findKthLargest(self, nums, k: int) -> int:
    #     low =0
    #     high = len(nums)-1
    #     return self.findKth(nums,low,high,k)
    #
    # def findKth(self,nums,low,high,k):
    #     index = (self.partition(nums,low,high))[0]
    #     if index==k:
    #         return nums[index]
    #     if index<k:
    #         return self.findKth(nums,index+1,high,k)
    #     else:
    #         return self.findKth(nums,low,index-1,k)
    #
    # def partition(self,nums,low,high):
    #     pivot = nums[low]
    #     while low<high:
    #         while low<high and nums[high]>pivot:
    #             high-=1
    #         while low<high and nums[low]<pivot:
    #             low+=1
    #         nums[low],nums[high] = nums[high],nums[low]
    #     nums[high] = pivot
    #     return high,nums

    # # 大顶堆 Space: O(n) Time Complexity：Heapify用了O(N)，然后一共pop了k个元素，每个元素使用logn的时间复杂，所以一共是O(n + klog(n))
    # def findKthLargest(self, nums, k: int):
    #     nums = [-num for num in nums]  # Python的Standard Library里面调用heapify的时候，永远是一个min_heap，然后因为没有Max Heap的implementation，你要做的就是通过Min Heap来模拟Max Heap的运算，最简单的就是将所有的数变成-num
    #     heapq.heapify(nums)  # 把数组变成堆
    #     res = float('inf')
    #     for _ in range(k):
    #         res = heapq.heappop(nums)
    #     return -res

    # 小顶堆 Time: O(k) + O(n * logk) | Space: O(K)
    # 每次pop最小元素，然后push过程中，heap都会重新把内部的数据进行整合，然后当pop和push执行完后，heap里是nums最大的k个数，heap的顶端永远是最大的k个数里最小的值
    def findKthLargest(self, nums, k: int):
        # min_heap = [-float('inf')] * k
        min_heap = nums[:k]        # 在开辟数组的同时，放入input array里面前k个数的元素，这样我们的时间复杂度会有一定的提升
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
                print(min_heap)
        return min_heap[0]

sol = Solution()
nums = [3,2,3,1,2,4,0,5,6]
k = 4
ans = sol.findKthLargest(nums,k)
print(ans)

# 参考网址：https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/167837/Python-or-tm
