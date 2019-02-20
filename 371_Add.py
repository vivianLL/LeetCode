'''
371. Sum of Two Integers(不用加减乘除做加法)

https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''

class Solution:
    def getSum(self, a: 'int', b: 'int'):
        # 修正的python按位加法
        while b != 0:              # 进位标志位
            temp = a ^ b           # 利用异或（半加）运算来计算不带进位的加法结果，注意负数按位与需要先算补码再求回原码
            b = (a & b) << 1       # 利用与运算计算进位的标志
            a = temp & 0xFFFFFFFF  # 每次都把num1规定成一个32位的数
        return a if a >> 31 == 0 else a - 4294967296  # 32个1也就是一个int可表示的无符号整数为4294967295，对应的有符号为-1。因此最后我们可以判断符号位是否为1做处理。


        # # python格式化输出 chr(43)对应+
        # return eval(f'a {chr(43)} b')  # use .format for legacy python

        # # 简单位运算（Python3.x之后整数只有一个可以放任意大数的int型，不会溢出，所以计算正数和负数异或时，Python就会长时间不出结果，进入死循环）
        # while b:
        #     sum = a ^ b
        #     carry = (a & b) << 1
        #     a = sum
        #     b = carry
        # return a

        # # 自己写的，太长了，只能计算正数==
        # a = str(bin(a)).split('0b')[-1]
        # b = str(bin(b)).split('0b')[-1]
        # la = len(a)
        # lb = len(b)
        # if la>lb:
        #     b = "".join(['0' * (la - lb), b])  # 注意不用+号如何用join拼接字符串
        # if lb>la:
        #     a = "".join(['0' * (lb - la),a])
        #
        # n = max(len(a),len(b))
        # flag = ['0']*(n)
        # carry = ['0']*(n)
        # for i in range(n-1,-1,-1):
        #     if i==n-1:
        #         add1bit = '%s%s0' % (a[i], b[i])
        #     else:
        #         add1bit = '%s%s%s'%(a[i],b[i],carry[i+1])
        #
        #     if add1bit == "110" or add1bit == "101" or add1bit == "011":
        #         carry[i] = '1'
        #         flag[i] = '0'
        #     if add1bit == "100" or add1bit == "001" or add1bit == "010":
        #         carry[i] = '0'
        #         flag[i] = '1'
        #     if add1bit == "000":
        #         carry[i] = '0'
        #         flag[i] = '0'
        #     if add1bit == "111":
        #         carry[i] = '1'
        #         flag[i] = '1'
        #     # print(flag,i,carry[i])
        #     flagstr = "".join(flag)
        # if carry[0]=='1':  # 注意最后的进位，且1为字符串，不为int数
        #     sum = "".join([carry[0],flagstr])
        # else:
        #     print(carry,carry[0])
        #     sum = flag
        # print("sum: ",sum)
        # sum = int(sum,2)
        # return sum




sol = Solution()
newS = sol.getSum(5,7)
print(newS)
newS = sol.getSum(-2,7)
print(newS)

# 注意：需要考虑负整数
