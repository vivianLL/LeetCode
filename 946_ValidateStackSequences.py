'''
946. Validate Stack Sequences
Medium

https://leetcode.com/problems/validate-stack-sequences/
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
'''
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # 贪婪算法 均为O(N)
        j = 0
        newstack = []  # 压入栈
        for x in pushed:
            newstack.append(x)
            while newstack and newstack[-1] == popped[j]:  # popped[j]为弹出序列当前最顶上元素
                newstack.pop()
                j += 1  # 计数 当前有多少数对应上

        return j == len(popped)  # 相当于 return not newstack



sol = Solution()
ans = sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2])
print(ans)
ans = sol.validateStackSequences([1,2,3,4,5], [5,4,3,2,1])
print(ans)

# 思路：
# 如果下一个弹出的数字刚好是栈顶数字，那么直接弹出。
# 如果下一个弹出的数字不在栈顶，我们把压栈序列中还没有入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止。
# 如果所有的数字都压入栈了仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列。