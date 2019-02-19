# -*- coding:utf-8 -*-
'''
剑指offer面试题17 牛客网[编程题]求1+2+3+...+n
https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1?tpId=13&tqId=11200&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
题目描述：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
import numpy
class Solution:
    def Sum_Solution(self, n):
        # # 法一：通过数组计算n(n+1)/2，测试不通过
        # array = numpy.zeros((n, n+1), dtype=numpy.int)
        # sum = array.size//2 # python3中除法得到整数用//
        # return sum

        # # 法二，sum
        # return sum(list(range(0,n+1)))

        # 法三：利用逻辑与的短路特性实现递归终止
        result = n
        temp = n > 0 and self.Sum_Solution(n-1)
        result = result + temp
        return result


sol = Solution()
newS = sol.Sum_Solution(3)
print(newS)

# 注意：
# “or”运算符表示“或”，有一个为真则全部为真；前半部分判断出来是真的，后半部分就不再进行运算了。
# “and”运算符表示“与”，前一项为假则整个表达式为假，因此可以利用这个性质进行递归运算或者达到整洁代码的目的。