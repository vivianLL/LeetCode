'''
6. ZigZag Conversion
Medium

https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # # 解法一：按行排序 从左到右遍历ss，将每个字符追加到适当的行。可以使用两个变量跟踪适当的行:当前行和当前方向。
        # # Time Complexity: O(n), where n == len(s)；Space Complexity: O(n)
        if numRows==1: return s
        rows = [[] for _ in range(min(numRows,len(s)))]
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow].append(c)
            print(rows)
            if curRow==0 or curRow == numRows-1:
                goingDown = not goingDown
            if goingDown==True:
                curRow += 1
            else:
                curRow += -1

        ans = ''
        for row in rows:
            ans += "".join(row)
        return ans

        # # 按行访问 按Zig-Zag型的顺序逐行阅读字母 因为我们所取的每一行字符串是有规律的写入的，,P A Y P A L 可以看作一个循环规律为2n-2,可以按2n-2来添加字符串
        # if numRows == 1: return s
        # ans = ""
        # n = len(s)
        # cycleLen = 2*numRows - 2
        # for i in range(numRows):
        #     j = 0
        #     while i+j < n:
        #         print(s[j+i])
        #         ans += s[j+i]        # 按行遍历Z字型斜的部分
        #         if i != 0 and i!=numRows-1 and j+cycleLen-i<n:  # Z字型斜的部分
        #             # print(s[j+cycleLen-i])
        #             ans += s[j+cycleLen-i]
        #         j += cycleLen
        # return ans

        # # 解法三： python下O(1)空间复杂度
        # if s == None:
        #     return s
        # if numRows == 0:
        #     return s
        # if numRows == 1:
        #     return s
        # rstr = ""
        # for i in range(numRows):
        #     if i == 0:
        #         rstr += s[::numRows + (numRows - 2)]
        #         print(s[::numRows + (numRows - 2)])
        #     elif i == numRows - 1:
        #         rstr += s[i::numRows + (numRows - 2)]
        #         print(s[i::numRows + (numRows - 2)])
        #     else:
        #         spacea = 2 * (numRows - i -1)
        #         spaceb = 2 * numRows - 2 - spacea
        #         counter = 0
        #         j = i
        #         while j < len(s):
        #             rstr += s[j]
        #             print(s[j],rstr)
        #             if counter % 2 == 0:
        #                 j += spacea
        #             else:
        #                 j += spaceb
        #             counter += 1
        # return rstr


sol = Solution()
ans = sol.convert("PAYPALISHIRING", 3)  # "PAHNAPLSIIGYIR"
print(ans)