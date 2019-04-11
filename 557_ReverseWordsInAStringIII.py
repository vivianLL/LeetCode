'''
557. Reverse Words in a String III
Easy

https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        # split 和 字符串+操作 时间O(n) 空间O(n)
        # slist = s.split(' ')
        # sstr = ''
        # for i in range(len(slist)):
        #     sstr += (slist[i][::-1]) + ' '
        # return sstr[:-1]

        # # split 和 字符串join操作 时间O(n) 空间O(n)
        # slist = s.split(' ')
        # sstr = []
        # for i in range(len(slist)):
        #     sstr.append(slist[i][::-1])
        # return ' '.join(sstr)
        #
        # # 简便写法
        # return   ' '.join([x[::-1]  for x in s.split(' ')])
        #
        # return ' '.join(s[::-1].split()[::-1])  # 或先对字符串反序，再对列表元素反序。进一步简化代码

        # 不用split
        res, cr = '', ''
        for i in s:
            if i == ' ':
                res += cr[::-1] + i
                cr = ''
            else:
                cr += i
        return res + cr[::-1]


sol = Solution()
ans = sol.reverseWords("Let's take LeetCode contest")
print(ans)