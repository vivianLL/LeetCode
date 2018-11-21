'''
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN

input test: "+" "-" "+-1" "-2147483648" "1a" " 42" " +1" " -1a"

'''

# Runtime: 56 ms, faster than 99.97% of Python3 online submissions for String to Integer (atoi).
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()   # 去除左边首部的空格

        if str == None or str == " " or str == "":
            return 0

        if (str[0] is "+"):
            if len(str)==1:
                return 0
            if (str[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
                string = ""
                for i in range(1, len(str)):

                    if (str[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
                        string += str[i]
                    else:
                        break
                if int(string) > 2147483647:
                    return 2147483647
                return int(string)
            else:
                return 0

        if (str[0] is "-"):
            if len(str)==1:
                return 0
            if (str[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
                string = "-"
                for i in range(1, len(str)):

                    if (str[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
                        string += str[i]
                    else:
                        break
                if int(string) < -2147483648:
                    return -2147483648
                return int(string)
            else:
                return 0

        if (str[0] in ["1", "2","3", "4", "5", "6", "7", "8", "9", "0"]):
            string = ""
            for i in range(0,len(str)):
                if (str[i] in ["1", "2","3", "4", "5", "6", "7", "8", "9", "0"]):
                    string+=str[i]
                else:
                    break
            if int(string) > 2147483647:
                return 2147483647
            return int(string)
        return 0

# 36ms
# class Solution(object):
#     def myAtoi(self, string):
#         min = -2147483648
#         max = 2147483647
#         res = ""
#         str_list = list(string.strip())
#         print(string.strip())
#         for index, char in enumerate(str_list):
#             if len(res) > 0 and not char.isdigit():  # isdigit检测字符串是否只由数字组成
#                 break
#             elif index == 1 and not char.isdigit():
#                 return 0
#             elif char == '+':
#                 continue
#             elif char.isdigit() or char == '-':
#                 res += char
#             else:
#                 return 0
#         if res == '-' or len(res) == 0:
#             return 0
#         res = int(res)
#         if res > max:
#             return max
#         elif res < min:
#             return min
#         return res

sol = Solution()
num = sol.myAtoi(" +-2147483649 12")
print(num)
