'''
179. Largest Number
Medium

https://leetcode.com/problems/largest-number/
Given a list of non negative integers, arrange them such that they form the largest number.
'''
class Solution:
    def largestNumber(self, nums):
        # # 全排列的思想，复杂度高，超时
        # def permute(nums):
        #
        #     if len(nums) <= 1:
        #         return [nums]
        #     ans = []
        #     for i, num in enumerate(nums):
        #         n = nums[:i] + nums[i + 1:]
        #         for temp_list in permute(n):
        #             print([num],temp_list)
        #             ans.append([num] + temp_list)
        #     return ans
        #
        # output = []
        # ans = permute(nums)
        # for temp in ans:
        #     output.append(''.join(str(i) for i in temp))
        # return sorted(output)[-1]

        # # 快排思想 将简单比大小换为按位比大小（即将两个数字拼接后比大小） 时间复杂度O(nlogn)
        # if nums == [0 for _ in range(len(nums))]:return 0    # 包括空列表和列表全0的情况
        # if len(nums) <= 1:
        #     return str(nums[0])   # 注意返回字符串，而非字符串里是列表str(nums)
        #
        # def quicksort(nums,left,right):
        #     if left<right:
        #         partitionIndex = partition(nums,left,right)
        #         quicksort(nums,left,partitionIndex-1)
        #         quicksort(nums,partitionIndex+1,right)
        # def partition(nums,left,right):
        #     print(nums[left:right+1])
        #     pivot = left
        #     index = pivot+1
        #     i = index
        #     while i<=right:
        #         print(str(nums[i]),str(nums[pivot]))
        #         temp1 = ''.join([str(nums[i]),str(nums[pivot])])
        #         temp2 = ''.join([str(nums[pivot]),str(nums[i])])
        #         print(temp1,temp2)
        #         if temp1>temp2:
        #
        #             nums[i], nums[index] = nums[index], nums[i]
        #
        #             index = index+1
        #         i = i+1
        #     nums[index-1],nums[pivot] = nums[pivot],nums[index-1]
        #     return index-1
        # quicksort(nums,0,len(nums)-1)
        # print(nums)
        # numsstr = ''.join(str(num) for num in nums)
        # return numsstr

#         # 通过自定义比较器排序
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey)) # key用列表元素的某个属性或函数进行作为关键字，有默认值，迭代集合中的一项;
#         return '0' if largest_num[0] == '0' else largest_num
#
# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x+y > y+x

        # 最快
        from functools import cmp_to_key
        comp = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0
        return str(int(''.join(sorted([str(x) for x in nums], key=cmp_to_key(comp)))))  # 在python3.0中，cmp参数被彻底的移除了，可以用cmp_to_key转化成key

sol = Solution()
# ans = sol.largestNumber([10,2,0])
# ans = sol.largestNumber([0])
# ans = sol.largestNumber([0,0]) # []
ans = sol.largestNumber([1,2,3,4,5,6,7,8,9,0])
# ans = sol.largestNumber([3,30,34,5,9])
print(ans)