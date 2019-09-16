'''
76. Minimum Window Substring
Hard

https://leetcode.com/problems/minimum-window-substring/
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # 滑动窗口法 时间空间复杂度O(|S| + |T|)
        # if not t or not s:
        #     return ''
        # left = 0
        # right = 0
        # formed = 0   # form用于跟踪当前窗口中有多少个字符以其期望的频率出现在当前窗口中
        # ans = float('inf'),None,None
        # dictt = Counter(t)
        # required = len(dictt)
        # window_counts = {}
        # while right<len(s):
        #     cha = s[right]
        #     window_counts[cha] = window_counts.get(cha,0)+1
        #     if cha in dictt and window_counts[cha]==dictt[cha]:
        #         formed += 1
        #     while left <= right and formed==required:
        #         cha = s[left]
        #         if right - left + 1 < ans[0]:
        #             ans = (right-left+1,left,right)
        #         window_counts[cha] -= 1
        #         if cha in dictt and window_counts[cha] < dictt[cha]:  # 注意这个小于条件
        #             formed -= 1
        #         left += 1
        #     right += 1
        # return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

        # 优化的滑动窗口法
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        filtered_s = []   # 将s中的所有在t中的字符及其索引放到一个新列表中。
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:    # 此处与未优化前不同，不能直接用l，r
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1

            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


sol = Solution()
ans = sol.minWindow("ADOBECODEBANC","ABC")
print(ans)