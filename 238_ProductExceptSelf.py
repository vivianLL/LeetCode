'''
238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Note: Please solve it without division and in O(n).
'''
from functools import reduce
class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        # # 自己写的方法，超时
        # product = []
        # for i in range(0,len(nums)):
        #     newlist = nums[i+1:] + nums[:i]
        #     product.append(reduce(lambda x,y:x*y,newlist)) # reduce() 函数会对参数序列中元素进行累积。
        # return product

        # # 依然超时
        # res_list = []
        # for i in range(len(nums)):
        #     tmp_list = nums[:]
        #     tmp_list.pop(i)
        #     res = 1
        #     for j in range(len(tmp_list)):
        #         res *= tmp_list[j]
        #     res_list.append(res)
        # return res_list

        # 通过测试
        # res = [1] * len(nums)
        # lprod = 1
        # rprod = 1
        # for i in range(len(nums)):
        #     res[i] *= lprod
        #     lprod *= nums[i]
        #     print(i,~i)
        #     res[~i] *= rprod
        #     rprod *= nums[~i]
        # return res

        # 通过测试且较快
        p = 1
        n = len(nums)
        output = []            # output的意义是nums数组不包括i位置的所有乘积，分为i左边的元素乘积和 i右边的所有元素乘积。
        for i in range(0, n):  # output装入下标小于i的值
            output.append(p)
            p = p * nums[i]
        print(output)
        p = 1
        for i in range(n - 1, -1, -1):  # output装入下标大于i的值
            output[i] = output[i] * p
            p = p * nums[i]
        return output



sol = Solution()
newlist = sol.productExceptSelf([1,2,3,4])
print(newlist)