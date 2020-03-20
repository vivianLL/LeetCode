'''
1013. Partition Array Into Three Parts With Equal Sum
Easy

https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
'''
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        # # 我的方法
        # s = sum(A)
        # if s%3 != 0:
        #     return False
        # else:
        #     temp = s//3
        #     for i in range(1,len(A)):   # 注意：应从1开始，下同
        #         if sum(A[:i])==temp:
        #             for j in range(1,len(A[i:])):
        #                 if sum(A[i:i+j])==temp and sum(A[i+j:])==temp:
        #                     return True
        #     return False

        # 官方写法 寻找切分点 不需要循环
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:  # 需要满足最后一个数组非空
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False

sol = Solution()
ans = sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
print(ans)
ans = sol.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
print(ans)
ans = sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
print(ans)
ans = sol.canThreePartsEqualSum([1,-1,1,-1])
print(ans)

# 注意：由于数组中的数有正有负，我们可能会得到若干个索引 i0, i1, i2, ...，从 A[0] 到这些索引的数之和均为 sum(A) / 3。
# 那么我们应该选取那个索引呢？直觉告诉我们，应该贪心地选择最小的那个索引。