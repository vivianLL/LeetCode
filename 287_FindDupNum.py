'''
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''
import collections

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力法：复杂度O(n^2) 大列表（17万数据）时超时
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]!=nums[j]:
        #             j=j+1
        #         else:
        #             return nums[i]
        #     i+1


        # # 排序法：复杂度O(nlogn) 就地排序O(1)则改变了数组 否则空间复杂度O(n)
        #         # nums.sort()   # O(nlogn)
        #         # for i in range(1, len(nums)):
        #         #     if nums[i] == nums[i - 1]:
        #         #         return nums[i]


        # # 集合法 时间复杂度O(n) 空间复杂度O(n)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)     # 或seen[num]=1


        # # 二分法：时间复杂度O(nlgn) 88 ms, faster than 6.02%
        # 不能保证找出所有重复的数字 不能确定是每个数字各出现一次还是某个数字出现两次
        # length = len(nums)
        # start = 0
        # end = length-1
        #
        # while end>start:
        #     count = 0
        #     mid = int((end + start)/2)
        #     for i in range(0, length):
        #         if nums[i] <= mid:
        #             count=count+1
        #         i = i + 1
        #     if count>mid:
        #         end=mid
        #     else:
        #         start=mid+1
        #
        # print(start)
        # return start


        # '''从前往后遍历数组，将nums[nums[i]-1]设置为其相反数，当nums[nums[i]-1]已经是负数的时候，
        # 说明abs(nums[i])已经出现过了。返回其值。时间复杂度O(n). 空间复杂度O(1).'''
        # 68 ms, faster than 19.76%
        # for i in range(0,len(nums)):
        #     idx = abs(nums[i])-1
        #     if nums[idx]<0:
        #         print(idx+1)
        #         return (idx+1)
        #     nums[idx]=-nums[idx]
        #     i = i +1


        # # 循环链条法 时间复杂度O(n) 空间复杂度O(1) 52 ms, faster than 47.83%
        # slow = nums[0]
        # fast = nums[nums[0]]
        # # 找到快慢指针相遇的地方 相当于c++的do while
        # while(slow!=fast):
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]  # 比slow多走一步
        # find = 0
        # # 用一个新指针从头开始，直到和慢指针相遇，找到环的“入口”
        # while find!=slow:
        #     slow = nums[slow]
        #     find = nums[find]
        # print(find)
        # return find


        # # 使用python标准库
        # a = collections.Counter(nums)  # 计数函数 Counter({3: 2, 1: 1, 4: 1, 6: 1, 2: 1, 5: 1})
        # print(a.get)
        # # find = max(a.keys(), key=a.get) # Counter 其实是dict 的一个子类，可以使用get方法
        # find = max(a, key=lambda i: a[i])
        # print(find)
        # return find


        # 重排数组交换顺序 改变了数组 时间复杂度O(n) 空间复杂度O(1) from《剑指offer》
        for i in range(0,len(nums)):
            while nums[i]!=i:
                if nums[i] == nums[nums[i]]:
                    print(nums[i])
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
            i = i+1

sol = Solution()
list = [1,2,4,6,2,5,3]
num = sol.findDuplicate(list)
print(num)


# 二分法 鸽笼原理 递归怎么写 if和for谁在里层谁在外层 if的判断应以中点为划分，而不应以起点终点为划分 边界条件有没有等号 起始点是否需要加一 注意最后返回值是start不是mid
# 确定计数范围 起点终点变化的条件 不能单纯的length/2，而要start/2或end/2
# 映射找环/循环链条法 将数组的下标和数组值一对一映射，如果有重复，则会产生多对一的映射。实际上就是找环路起点的题 Floyd判圈法 如果从同一个起点同时开始以不同速度前进的2个指针最终相遇，那么可以判定存在一个环 http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
# 其他方法：哈希表：遍历数组时，用一个集合记录已经遍历过的数，如果集合中已经有了说明是重复。但这样要空间，不符合。排序法：要修改原数组，不符合。
