'''
402. Remove K Digits
Medium

https://leetcode.com/problems/remove-k-digits/
Share
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # A_list = list(num)
        # flag = 0
        # for _ in range(k):
        #     for i in range(flag, len(A_list) - 1):
        #         print(A_list)
        #         # 循环比较当前一位大于后一位的时候删除当前位，然后将下次遍历从删除位开始
        #         if int(A_list[i]) > int(A_list[i + 1]):
        #             A_list.remove(A_list[i])
        #             flag = i - 1 if i - 1 > 0 else 0
        #             break
        #         # 有可能数组是不减的数组，所以在最后一次比较的时候也没有办法break这次循环，那么就直接删除最后一位即可，同样需要将下次循环以前一位开始
        #         elif i == len(A_list) - 2:
        #             A_list.remove(A_list[-1])
        #             flag -= 1
        #
        # print(A_list)
        # # 分成3种情况，因为首位为0必须将0删除，但是如果数组的长度只有1位那么就无需删除，如果最后数组的数据被全部删除，那么数组直接赋值为0
        # if len(A_list) > 1:
        #
        #     while A_list[0] == "0":
        #         if len(A_list) > 1:
        #             A_list.remove("0")
        #         else:
        #             break
        # elif not A_list:
        #     A_list = ["0"]
        # else:
        #     if k>0 and len(num)==1:
        #         return "0"
        #     else:
        #         pass
        #
        # # print("".join(A_list))
        # return "".join(A_list)

        # 快速写法
        cnt0 = num.count('0')
        if k >= len(num) - cnt0:
            return '0'

        i0 = 0
        while i0 < len(num) and k != 0:
            newi0 = num.find('0', i0)
            if newi0 != -1 and newi0 - i0 <= k:  # firstly, remove all digits before "0", if their count <= k
                k -= newi0 - i0
                i0 = newi0 + 1
            else:  # once we enter this "else", we are finishing
                part = num[i0:] if newi0 == -1 else num[i0:newi0]  # so, we can name this section and focus on it
                s, res = 0, ''
                while 0 < k < len(part) - s:  # make sure there is ENOUGH digits for k times deletion
                    for d in '123456789':
                        i = part.find(d, s)
                        if i != -1 and i - s <= k:
                            res += part[i]
                            k -= i - s  # all bigger digits before "i" are deleted, and part[i] is reserved, we put it in "res"
                            s = i + 1  # reset start to "i+1"
                            break  # once we hold some small part[i], we need to restart from "1" to "9"
                if k == 0:
                    res += part[
                           s:]  # k == 0 means we have run out of k times deletion, and s might NOT reach "part" end
                return res if newi0 == -1 else res + num[newi0:]  # this line echos the above part definition line
        while i0 < len(num) and num[i0] == '0':
            i0 += 1
        return num[i0:] if i0 < len(num) else '0'

sol = Solution()
ans = sol.removeKdigits("987132",4)
print(ans)
'''
"12",1
"9",1
# l1 = ["1000230","5"]
# l1 = ["987132","4"]
# l1 = ["54321","2"]
# l1 = ["1593121212","3"]
'''
# 参考网址：https://blog.csdn.net/hotpotbo/article/details/78477841