'''
344. Reverse String
Easy

https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
'''
class Solution:
    def reverseString(self, s:[]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     s[i],s[-1-i] = s[-1-i],s[i]
        # print(s)  # 注意题目要求原地操作 无返回值

        # s.reverse() # 不能用s[::-1]因为非原地
        # print(s)

        # 类C++写法
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

sol = Solution()
ans = sol.reverseString(["H","a","n","n","a","h"])
print(ans)