'''
65. Valid Number

https://leetcode.com/problems/valid-number/
Validate if a given string can be interpreted as a decimal number.
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        # 简单做法
        # s = s.strip()
        # try:
        #     s = float(s)
        #     return True
        # except:
        #     return False

        # 常规做法
        s = s.strip()  # 去除首尾空格
        isDot, isDigit, isE = False, False, False  # 点，数字，e

        for i, x in enumerate(s):
            if x == "e":
                if not isDigit or isE:  # 前面没有数字，or 前面已经存在字符 e
                    return False

                isDigit = False  # 设置isDigit = false
                isE = True
            elif x in "+-":
                if i != 0 and s[i - 1] != "e":  # +- 只能出现首位，和 字符e的后面
                    return False
            elif x == ".":
                if isDot or isE:  # 字符 .（小数点）只能出现一次，而且是只能出现在 e 的前面
                    return False
                isDot = True
            elif x.isdecimal():  # 检查字符串是否只包含十进制字符
                isDigit = True
            else:
                return False

        return len(s) > 0 and isDigit

        # 确定有穷状态自动机(DFA)
        # 参考网址：https://www.cnblogs.com/zuoyuan/p/3703075.html
        INVALID = 0;
        SPACE = 1;
        SIGN = 2;
        DIGIT = 3;
        DOT = 4;
        EXPONENT = 5;
        # 0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable = [[-1, 0, 3, 1, 2, -1],  # 0 no input or just spaces
                           [-1, 8, -1, 1, 4, 5],  # 1 input is digits
                           [-1, -1, -1, 4, -1, -1],  # 2 no digits in front just Dot
                           [-1, -1, -1, 1, 2, -1],  # 3 sign
                           [-1, 8, -1, 4, -1, 5],  # 4 digits and dot in front
                           [-1, -1, 6, 7, -1, -1],  # 5 input 'e' or 'E'
                           [-1, -1, -1, 7, -1, -1],  # 6 after 'e' input sign
                           [-1, 8, -1, 7, -1, -1],  # 7 after 'e' input digits
                           [-1, 8, -1, -1, -1, -1]]  # 8 after valid input input space
        state = 0;
        i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputtype = SIGN
            elif s[i] in '0123456789':
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputtype = EXPONENT

            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 1 or state == 4 or state == 7 or state == 8




sol = Solution()
ans = sol.isNumber("1.2.3")
print(ans)
ans = sol.isNumber(".123")
print(ans)
ans = sol.isNumber("123.")
print(ans)  # True
ans = sol.isNumber(".")
print(ans)  # False
ans = sol.isNumber("e1")
print(ans)
ans = sol.isNumber("1 ") # " 0"
print(ans) # True
ans = sol.isNumber(" ")
print(ans) # False
ans = sol.isNumber("12e+5.4")
print(ans) # True
# ans = sol.isNumber("-12e-3")
# print(ans)
# ans = sol.isNumber("+-123e")
# print(ans)
# ans = sol.isNumber(".123")
# print(ans)
# ans = sol.isNumber("-2e-10")
# print(ans)