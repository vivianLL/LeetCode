'''
400. Nth Digit
Easy

https://leetcode.com/problems/nth-digit/
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        # # 自写代码 超时
        # s = ''
        # i=0
        # while i<=n:
        #     print(str(i))
        #     s = s+str(i)
        #     print(s)
        #     i+=1
        #     return int(s[n])

        # 剑指offer思路
        if n < 0:
            return False
        elif n >= 0 and n <= 9:
            return n
        else:
            a = 9
            base = 1
            i = 1
            while a*i < n:     # 注意此处为a*i<n，而非 a<n
                print(a,base,i)   # （9,1,1）（90,10,2） （900,100,3）
                if a==9:
                    n=n-a-1       # 0~9有10个数字
                else:
                    n=n-a*i       # 10~99有90个两位数，100~999有900个三位数，所以a*i为90*2、900*3、9000*4···
                i = i + 1
                print(n)
                base *= 10        # 1、10、100、1000···
                a = 9*base
            x = n//i              # 第n位是某个i位数中的一位
            num = 10**(i-1)+x     # 第n位是从10**(i-1)开始的第x个数字中间的一位
            print(10**(i-1)+x)
            print(n%i)            # 第n位是某个数字中间的第几位
            return int(str(num)[n%i])




sol = Solution()
ans = sol.findNthDigit(1001)     # 7
# print(ans)
# ans = sol.findNthDigit(100000000)  # 8
# print(ans)
# ans = sol.findNthDigit(333333)
# print(ans)
# ans = sol.findNthDigit(3)     # 3
print(ans)
