'''
969. Pancake Sorting
Medium

https://leetcode.com/problems/pancake-sorting/
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Note:
1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
'''
class Solution:
    def pancakeSort(self, A):
        # 法一 找最大 每一趟，将该趟中最大的元素反转到A[0]，然后反转A[0]到A[len]；重复这个过程直到序列被排好为止。（选择排序）
        ans = []
        n = len(A)
        while n>0 and len(A)!=1:

            i = A.index(max(A))
            tempA = A[:i+1][::-1]+A[i+1:]
            tempA = tempA[::-1]
            if i!=len(A):
                ans.extend([i+1,n])
            n -= 1
            A = tempA[:-1]
            print(tempA,A)
        return ans

        # 利用note给出的信息优化
        res = list()
        for i in range(len(A), 1, -1):  # i即为当前需要排序的最大的数
            idx = A.index(i) + 1
            A = A[:idx][::-1] + A[idx:]
            A = A[:i][::-1]
            res += [idx, i]

        return res



sol = Solution()
ans = sol.pancakeSort([3,2,4,1])
print(ans)
ans = sol.pancakeSort([])
print(ans)

# 难点在于怎么用最少的次数排好序