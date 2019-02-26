'''
剑指offer面试题21 牛客网[编程题]调整数组顺序使奇数位于偶数前面
https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        # # 简单写法
        # return sorted(array, key=lambda c: c % 2, reverse=True)

        # # 自己写的代码 时间复杂度O(n) 空间复杂度O(n)
        # odd = []
        # even = []
        # for i in range(len(array)):
        #     if array[i]%2==0:
        #         odd.append(array[i])
        #     else:
        #         even.append(array[i])
        # reorder = even+odd
        # return reorder

        # 时间复杂度O(n) 空间复杂度O(1) 但不保证相对位置不变
        n = len(array)
        head = 0
        tail = n - 1
        while head < tail:
            while array[head] % 2 != 0:
                head += 1
            while array[tail] % 2 == 0:
                tail -= 1
            array[head], array[tail] = array[tail], array[head]
            head += 1
            tail -= 1
        return array


sol = Solution()
ans = sol.reOrderArray([6,3,7,4,5])
print(ans)


# 如果为原地排序，则两种思路。
# 第一种：从头往尾扫描数组，遇到一个偶数就把它提出来，依次把其后的数字前移一格，最后将偶数插入末尾的空位。时间复杂度为O(n2)O(n2)
# 第二种：采用两指针分别从首尾出发，当头指针遇到一个偶数，并且尾指针遇到一个奇数时，交换两指针的数字，直到两指针相遇。时间复杂度为O(n)O(n)，(类似于快排)
# 若要求相对位置不变，以上两种方法不能使用了。解决方案没有太好的办法，一类是采用稳定的排序，例如冒泡，归并，二是开辟长度为n的数组，遍历原数组，依次把奇数偶数放入新数组，最后将新数组赋值给原数组。
