'''
205. Isomorphic Strings
Easy

https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        mapval = [hashmap[k] for k in hashmap]
        return len(mapval) == len(set(mapval))


        # hashmap = {}
        # mapval = {}
        # for i in range(len(s)):
        #     print(hashmap, mapval)
        #     if s[i] in hashmap:
        #         if hashmap[s[i]] != t[i]:
        #             return False
        #     elif t[i] in mapval:
        #         return False
        #     else:
        #         hashmap[s[i]] = t[i]
        #         mapval[t[i]] = True
        #
        # return True

        # pos1, pos2 = [-1] * 256, [-1] * 256
        # for i in range(len(s)):
        #     if pos1[ord(s[i])] != pos2[ord(t[i])]:
        #         return False
        #     pos1[ord(s[i])] = pos2[ord(t[i])] = i
        # return True


sol = Solution()
ans = sol.isIsomorphic("paperig","titlegg")
print(ans)

# 思路一：先遍历一遍s和t，将s到t的字符映射存放在dict中，遍历过程中如果发现某个位置的映射与已经确定的映射冲突则可以直接返回false。
# 在遍历s和t的时候将已经经过映射的值保存在mapval这个dict中，这样在中途发现重复时也可以及时返回false。
# 思路二：对于s和t，分别用一个数组记录每个字符在该字符串中上一次出现的位置。当同时遍历s和t时，如果发现它们在某一位置的字符上次出现的位置不同，则返回false。
# 思路三：根据题目描述的映射要求，s有多少种不同的字符，t也有多少种不同的字符。如果我们将映射写成字符对的形式，比如 (‘a’,’c’) 表示s中字符’a’映射到t中’c’，那么映射的个数与s中字符的种类数相同。
# 用Python的内置函数zip，也可以一行实现判断同构。