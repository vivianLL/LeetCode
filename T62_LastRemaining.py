'''
剑指offer面试题62 圆圈中最后剩下的数字

https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
0, 1, … , n-1 这 n 个数字排成一个圈圈，从数字 0 开始每次从圆圏里删除第 m 个数字。求出这个圈圈里剩下的最后一个数字。
'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # # 常规算法 时间复杂度O(mn) 超时
        # if n<1 or m<1:
        #     return False
        # temp = m
        # mOvern = False
        # if m>n:
        #     m = m%n
        #     mOvern = True
        # leftCount = n
        # count = 0
        # index = 0
        # arr = [False]*n
        # while leftCount>1:
        #     count+=1
        #     if count==m:
        #         count = 0
        #         leftCount-=1
        #         arr[index]=True
        #         if mOvern:
        #             m = temp % leftCount
        #             m=leftCount if m==0 else m
        #     index = (index+1)%n
        #     while arr[index]:
        #         index = (index + 1) % n
        # return index

        # # 创新解法，递归实现
        if n < 0 or m < 1:
            return False
        if n==1:
            return 0
        if n>1:
            return (self.LastRemaining_Solution(n-1,m)+m)%n

        # 创新解法，循环实现
        # if n < 0 or m < 1:
        #     return False
        #
        # last = 0
        # for i in range(2,n+1):
        #     last = (last + m) % i
        #
        # return last

        # 另一种python解法
        # if n < 0 or m < 1:
        #     return False
        # s = [x for x in range(n)]  # 产生等差数列
        # p = m - 1
        # while len(s) != 1:
        #     # 这里用while而不是if  因为处理一次后的p可能仍>len(s)-1. 所以必须处理到p值满足list的index条件为止
        #     while p > len(s) - 1:  # 超过了尾数的index
        #         # 这个条件要放在最前面,为了防止p一上来就设置的大于len(s)-1, 如last_reaining_number(5, 8)
        #         p = p - (len(s) - 1) - 1  # -1 减1 是因为index从0计数..
        #     s.pop(p)
        #     p += (m - 1)
        # return s[0]



sol = Solution()
newS = sol.LastRemaining_Solution(4000,3)
print(newS)

# 约瑟夫环的公式是：
# f(n, m) = 0           (n = 1)
# f(n, m) = [f(n-1, m) +m] % n  (n > 1)
