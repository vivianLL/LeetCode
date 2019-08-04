'''
38. Count and Say
Easy

https://leetcode.com/problems/count-and-say/
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        # # 自己写的递归
        # if n<1:
        #     return ""
        # elif n==1:
        #     return "1"
        # else:
        #     ans = ""
        #     x = self.countAndSay(n-1)
        #     i = 0
        #     a = x[0]
        #     count = 0
        #     while x:
        #         while len(x)>i and a==x[i]:
        #             i += 1
        #             count += 1
        #         else:
        #             ans += str(count) + a
        #             x = x[i:]
        #             if x:
        #                 a = x[0]
        #                 count = 0
        #                 i = 0
        #             else:
        #                 return ans
        #     ans += str(count) + a
        #     return ans

        # # 简洁写法
        # if n==1 : return "1"
        # x = self.countAndSay(n-1)+"*"  # 为了x末尾的标记，方便循环读数
        # count = 1
        # ans = ""
        # for i in range(len(x)-1):
        #     if x[i]==x[i+1]:
        #         count += 1
        #     else:
        #         ans += str(count)+x[i]
        #         count = 1
        # return ans

        # 快速写法
        d = {
            1: '1', 2: '11', 3: '21', 4: '1211', 5: '111221'
        }
        if n <= 5:
            return d[n]
        else:
            s = self.countAndSay(n - 1)
            res = ''
            num = ''
            count = 0
            for char in s:
                if char != num:
                    if count != 0:
                        res += '{}{}'.format(count, num)
                    num = char
                    count = 1
                else:
                    count += 1
            if count != 0:
                res += '{}{}'.format(count, num)
            return res



sol = Solution()
# ans = sol.countAndSay(1)
# print(ans)
# ans = sol.countAndSay(2)
# print(ans)
# ans = sol.countAndSay(3)
# print(ans)
ans = sol.countAndSay(4)
print(ans)
# ans = sol.countAndSay(5)
# print(ans)
ans = sol.countAndSay(7)
print(ans)