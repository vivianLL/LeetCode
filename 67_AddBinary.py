'''
67. Add Binary
Easy

https://leetcode.com/problems/add-binary/
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # # 简单写法一
        # return bin(int(a,2)+int(b,2)).split('b')[-1]
        #
        # # 简单写法二
        # return bin(int(a, 2) + int(b, 2))[2:]
        #
        # # 简单写法三
        # return format(int(a, 2) + int(b, 2), "b")

        # c++写法
        maxlen = max(len(a), len(b))
        a = (a.zfill(maxlen + 1))[::-1]   # zfill返回指定长度的字符串，原字符串右对齐，前面填充0
        b = (b.zfill(maxlen + 1))[::-1]
        sum = [0 for _ in range(len(a))]
        for i in range(maxlen):
            if int(a[i]) + int(b[i]) + sum[i] <= 1:
                sum[i] = int(a[i]) + int(b[i]) + int(sum[i])
            else:
                sum[i] = int(a[i]) + int(b[i]) + int(sum[i]) - 2
                sum[i + 1] = 1
        sum = sum[::-1]
        while sum[0] == 0 and len(sum) > 1:
            sum.remove(0)
        return ''.join(str(x) for x in sum)



sol = Solution()
ans = sol.addBinary("11","0")
print(ans)