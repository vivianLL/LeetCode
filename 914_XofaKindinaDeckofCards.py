'''
914. X of a Kind in a Deck of Cards
Easy

https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
'''
import collections
import collections
import math
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        # 我的方法 先创建计数字典，然后对字典里的元素找公约数
        # dic = {}
        # for x in deck:
        #     if x not in dic:
        #         dic[x]=1
        #     else:
        #         dic[x]+=1
        # lis = [x for x in dic.values()]
        # max_num = max(lis)
        # print(max_num)
        # i = 2
        # while i<=max_num:
        #     for j in range(len(lis)):
        #         if lis[j] % i !=0:
        #             i += 1
        #             break
        #         if j==len(lis)-1 and lis[j] % i ==0:
        #             return True
        # print(i)
        # if i>max_num:
        #     return False

        # 简洁的官方写法 注意python2和python3写法（库的导入）不一样
        vals = collections.Counter(deck).values()
        # reduce函数对参数序列中元素进行累积。函数function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
        return reduce(math.gcd, vals) >= 2

sol = Solution()
ans = sol.hasGroupsSizeX([1,2,3,3,3,4,4,3,2,1])
print(ans)