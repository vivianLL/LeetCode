'''
91. Decode Ways
Medium

https://leetcode.com/problems/decode-ways/
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        # # 剑指offer思想 递归
        # length = len(s)
        # counts = [0]*length
        # count = 0
        # for i in s:
        #     if i not in {'1','2','3','4','5','6','7','8','9','0'}:
        #         return 0
        # if length==0 or s[0] == '0': return 0         # 若从0开始则无法编码，注意是s[0] == '0'，而不仅仅是s == '0'
        #
        # for i in range(length-1,-1,-1):
        #     if i<length-1:
        #         count = counts[i+1]      # counts列表记录从第i位开始的不同翻译的数目，每加一位则累加到count上
        #     else:                        # i是最后一位
        #         if s[i] != '0':
        #             count = 1
        #
        #     if i<length-1:
        #         digit1 = int(s[i])
        #         digit2 = int(s[i+1])
        #         converted = digit1*10+digit2
        #         if 10<=converted<=26:         # 注意此处为10-26，因为若小于10，如05，则无法编码
        #             if i<length-2:
        #                 count+=counts[i+2]
        #             else:
        #                 count+=1
        #         elif 0<converted<10:
        #             if count>0:
        #                 count-=1
        #         elif digit2==0:
        #             count=0
        #             return 0
        #     counts[i] = count
        # count = counts[0]
        # print(counts)
        # return count

        # # 最快
        # if len(s) == 0 or s[0] == '0': return 0
        # prev, cur = 1, 1
        # for i in range(1, len(s)):
        #     if s[i] == '0':
        #         cur = 0
        #     if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
        #         cur += prev
        #         prev = cur - prev
        #     else:
        #         prev = cur
        # return cur

        # 动态规划
        if len(s) == 0:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]

        dp[n] = 1
        dp[n-1] = 1 if s[n-1] != "0" else  0

        for i in range(n-2, -1, -1):
            if s[i] == "0":
                continue
            if int(s[i:i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]

sol = Solution()
count = sol.numDecodings('12258') # 5
print(count)
count = sol.numDecodings('226')   # 3
print(count)
count = sol.numDecodings('0')     # 0
print(count)
count = sol.numDecodings('110')   # 1
print(count)
count = sol.numDecodings('01')    # 0
print(count)
count = sol.numDecodings('101')    # 1
print(count)
count = sol.numDecodings('012')    # 0
print(count)
count = sol.numDecodings('550926')    # 0
print(count)
# 思路：使用循环从最小的问题自下而上解决问题，以消除重复的子问题
# 若用动态规划 第i位开始不同翻译的数目f(i)=f(i+1)+g(i,i+1)*f(i+2)，g(i,i+1)=1若i位和i+1位拼接在[10,25]，否则为0，有重复子问题