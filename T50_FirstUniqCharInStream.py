'''
剑指offer面试题50 题目二：字符流中第一个不重复的字符

牛客网：链接：https://www.nowcoder.com/questionTerminal/00de97733b8e4f97a3fb5c680ee10720
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.string_all = {}
        self.ch = []
    def FirstAppearingOnce(self):
        # write code here
        if self.string_all is None:
            return '#'
        for i in self.ch:
            if self.string_all[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.ch.append(char)
        if char in self.string_all:
            self.string_all[char] = self.string_all[char] + 1
        else:
            self.string_all[char] = 1

# Insert函数用来接收字符，构成字符流。FirstAppearingOnce函数用来判断是否为第一个只出现一次的字符。
# 用了字典来记录字符以及出现的次数。
# 比如 google ：
# 先 插入 g，出现次数为 1，返回 g
# 再插入o，则字符流为 go，出现次数都为 1，但是第一个只出现一次的字符为 g ，返回 g
# 再插入 o，则字符流为 goo，出现次数为 1,2，第一个只出现一次的字符为 g ，返回 g
# 再插入g，则字符流为 goog，出现次数为 2,2，不存在第一个只出现一次的字符 ，返回 #
# 再插入 l，则字符流为googl，出现次数为2,2,1，第一个只出现一次的字符为 l，返回 l
# 以此类推
