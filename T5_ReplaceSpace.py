# -*- coding:utf-8 -*-
'''
剑指offer面试题5 牛客网[编程题]替换空格
https://www.nowcoder.com/questionTerminal/4060ac7e3e404ad1a894ef3e17650423
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # # 最简单的做法
        # res = s.replace(" ","%20") # 不能返回s
        #     return res

        # # 时间复杂度为O(n)，空间复杂度为O(n)的做法
        # res = ""
        # for i in s:
        #     if i == ' ':
        #         res += "%20"
        #     else:
        #         res += i
        # return res

        # 通用解法（C/C++/Java) 在原字符串上从后向前复制和替换 两个指针 替换后字符串长度等于原长度加2*空格数
        p1 = len(s)-1  # 列表从0开始计数
        # print(p1)
        res = list(s)
        n = s.count(' ')
        res += [0]*n*2  # 后面补零
        p2 = len(res)-1
        # print(p2)
        while p1 != p2:
            if res[p1]!=' ':
                res[p2] = res[p1]
                p2 = p2-1
            else:
                res[p2] = '0'
                res[p2-1] = '2'
                res[p2-2] = '%'
                p2 = p2-3
            p1 = p1-1
        return ''.join(res)  # 返回字符串


# s = "We are happy. "
s = '   '
sol = Solution()
newS = sol.replaceSpace(s)
print(newS)

# 思想：从尾到头比较可以减少重复移动字符的次数
