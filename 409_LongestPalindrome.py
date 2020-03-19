'''
409. Longest Palindrome
Easy
https://leetcode.com/problems/longest-palindrome/

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
'''
import collections
class Solution:
    def longestPalindrome(self, s: str):
        # # 我的解法
        # dic = {}
        # for x in s:
        #     if x not in dic:
        #         dic[x] = 1
        #     else:
        #         dic[x] += 1
        # ans = 0
        # jishu = False
        # for y in dic:
        #     if dic[y]%2==0:
        #         ans += dic[y]
        #     else:
        #         jishu = True
        #         ans += dic[y]-1
        #
        # return ans+1 if jishu==True else ans

        # # 其他解法
        # a = set(s)
        # b = list(a)
        # oddc = 0
        # flag = 0
        # for i in range(len(b)):
        #     c = s.count(b[i])
        #     if c % 2 != 0:
        #         oddc += 1
        #         flag = 1
        # l = len(s) - (oddc - flag)
        # return l

        # 官方解法 由于在遍历字符时，ans 每次会增加 v / 2 * 2，因此 ans 一直为偶数。但在发现了第一个出现次数为奇数的字符后，我们将 ans 增加 1，这样 ans 变为奇数，在后面发现其它出现奇数次的字符时，我们就不改变 ans 的值了。
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

sol = Solution()
ans = sol.longestPalindrome("abccccdddddeeef")
print(ans)
ans = sol.longestPalindrome("abccccdd")
print(ans)
ans = sol.longestPalindrome("abcc")
print(ans)
ans = sol.longestPalindrome("cc")
print(ans)

# 注意：在一个回文串中，只有最多一个字符出现了奇数次，其余的字符都出现偶数次。
# 当字母出现奇数次时，不能只保留最大的奇数。注意所以字母都出现偶数次的情况。