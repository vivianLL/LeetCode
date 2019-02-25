'''
剑指offer面试题61 扑克牌中的顺子

https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
从扑克牌中随机抽 5 张牌,判断是不是顺子,即这 5 张牌是不是连续的。 2-10 为数字本身,A 为 1,J 为 11,Q 为 12,K 为 13,而大小王可以看成任意的 数字。（大小王最多4张）
'''
class Solution:
    def IsContinuous(self, numbers):
        # # write code here
        # if numbers == []:
        #     return False
        # # numbers = sorted(numbers)  # 先对数组排序，sorted使用timsort，平均时间复杂度O(nlogn)
        # numbers.sort()
        # print(numbers)
        # count0 = 0
        # countmiss = 0
        # seen = set()  # 设置集合判断数组中是否有重复非零值
        # for i in range(0,len(numbers)):
        #     if numbers[i]==0:
        #         count0 = count0+1
        #     if numbers[i] not in seen:
        #         seen.add(numbers[i])
        #     else:
        #         if numbers[i]!=0:
        #             return False
        #     if i!=len(numbers)-1:
        #         if numbers[i]!=0 and numbers[i+1]-numbers[i]!=1:
        #             countmiss = countmiss+numbers[i+1]-numbers[i]-1
        # print(count0)
        # print(countmiss)
        # if count0>4 or count0<countmiss:
        #     return False
        # else:
        #     return True

        # 简洁写法
        if not numbers: return False
        numbers.sort()
        print(numbers)
        zeros = numbers.count(0)
        gaps = 0
        small = zeros
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            gaps += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return gaps <= zeros



sol = Solution()
newS = sol.IsContinuous([9,10,0,10,12])
print(newS)
newS = sol.IsContinuous([])
print(newS)

# 思路：首先将数组排序；其次统计0的个数和相邻数字之间的空缺总数。如果空缺总数小于或等于0的个数，那么这个数组就是连续的，反之不连续。
# 需注意数组中非0数字重复出现、0多余4个、空数组的情况。