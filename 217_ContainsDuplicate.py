'''
217. Contains Duplicate
Easy

https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums) -> bool:
        # # 简单写法
        # return len(nums) != len(set(nums))

        numset = set()  # 注意：创建空集合只能用set()
        for i in nums:
            if i not in numset:
                numset.add(i)
            else:
                return True
        return False

sol = Solution()
ans = sol.containsDuplicate([1,2,3,1])
print(ans)