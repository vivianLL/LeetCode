'''
剑指offer面试题17 打印从1到最大的n位数
题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999.
（在LeetCode和牛客网上均没有）
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # def Print1ToMaxOfNDigits(self, n):
        # # 基础方法 未考虑大数问题
        # max = 9
        # i = 1
        # while i<n:
        #     max = max*10+9
        #     i=i+1
        #
        # for num in range(1,max+1):
        #     print(num)

    # # 考虑大数问题，看做是n个数(0-9)的全排列问题，递归实现
    # def Print1ToMaxOfNDigits(self,n):
    #     if n <= 0:
    #         return False
    #
    #     number = ['0'] * n
    #     for i in range(10):
    #         number[0] = str(i)
    #         self.Print1ToMaxOfNDigitsRecursively(number, n, 0)
    #
    # def PrintNumber(self,number):
    #     isBeginning0 = True
    #     nLength = len(number)
    #
    #     for i in range(nLength):
    #         if isBeginning0 and number[i] != '0':
    #             isBeginning0 = False
    #         if not isBeginning0:
    #             print('%c' % number[i],end='')  # end='' 不换行输出,end默认值为'\n'
    #     print('')
    #
    # def Print1ToMaxOfNDigitsRecursively(self,number, length, index):
    #     if index == length - 1:
    #         self.PrintNumber(number)
    #         return
    #     for i in range(10):
    #         number[index + 1] = str(i) # 最低位
    #         self.Print1ToMaxOfNDigitsRecursively(number, length, index + 1)

    # 考虑大数问题，在字符串/数组上模拟数字加法，较易理解
    def Print1ToMaxOfNDigits(self,n):
        if n <= 0:
            return
        list_num = ["0"] * n
        while self.Increament(list_num) is False:  # 判断时候已经去到最大值了，是的话停止
            self.PrintNumber(list_num)

    def PrintNumber(self,number):  # 打印单个数，前面的零不打印
        isBegin = False  # 找到最高非零位
        for i in range(len(number)):
            if number[i] != "0" and isBegin is False:
                isBegin = True
            if isBegin:
                tmp = ("".join(number[i:]))
                print(tmp)
                break

    def Increament(self,number):  # 在表示数字的数组上增加1
        isOverFlow = False
        isIncre = 0  # 是够归零进一
        len_num = len(number)
        n = len_num - 1  # 因为从最后一位开始而不是0位
        while n >= 0:
            nsum = int(number[n]) + isIncre
            if n == len_num - 1:
                nsum += 1 # 就是最后一位加一
            if nsum == 10:
                if n == 0:  # nsum在最高位上
                    isOverFlow = True  #  如果是最后的一个9999加一 那说明已经移除  例如 2位 的是 99 再加一就是溢出了
                else:  # 进位
                    isIncre = 1  # 如果不是那么就前面一位加一,自己变为0
                    number[n] = "0"
            else:
                number[n] = str(nsum)
            n -= 1
        return isOverFlow


sol = Solution()
sol.Print1ToMaxOfNDigits(2)