'''
17. Letter Combinations of a Phone Number
Medium

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
class Solution:
    # 自写程序
    # def letterCombinations(self, digits: str):
    #     if digits == "":
    #         return []
    #     dig2letter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    #     ans = [x for x in dig2letter[digits[0]]]
    #     i = 1
    #     while i < len(digits):
    #         temp = []
    #         for x in ans:
    #             temp.extend(self.help(x,dig2letter[digits[i]]))
    #         ans = temp
    #         i += 1
    #     return ans
    #
    #
    # def help(self,letter,digit):
    #     temp = []
    #     print(digit)
    #     for x in digit:
    #         temp.append(letter+x)
    #     print(temp)
    #     return temp

    # 回溯 优雅写法
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

sol = Solution()
ans = sol.letterCombinations("237")
print(ans)
print(len(ans))
# 思路：全排列 递归 BFS（广度优先搜索：对每一个数字可以添加的字符都添加到后面）