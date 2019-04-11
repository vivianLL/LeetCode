'''
20. Valid Parentheses
Easy

https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if s=='':
            return True
        stack = []
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            else:
                if s[i]==')':
                    if stack==[] or stack.pop()!='(':   # 注意栈是否为空
                        return False
                if s[i]==']':
                    if stack==[] or stack.pop()!='[':
                        return False
                if s[i]=='}':
                    if stack==[] or stack.pop()!='{':
                        return False
        if stack==[]:   # 注意最后栈应为空
            return True
        else:
            return False

sol = Solution()
ans = sol.isValid("((")  # "[}" "){"
print(ans)
#