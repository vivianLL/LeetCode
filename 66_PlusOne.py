class Solution:
    def plusOne(self, digits):
        # # 法一 自写 定义不同规则
        # if digits[-1] != 9:
        #     digits[-1] += 1
        #     return digits
        # else:
        #     i = len(digits)-1
        #     while i != 0:
        #         if digits[i] != 9:
        #             digits[i] += 1
        #             return digits
        #         else:
        #             digits[i] = 0
        #             i -= 1
        #     if digits[0] == 9:
        #         digits[0] = 0
        #         digits.insert(0,1)
        #
        #         return digits
        #     else:
        #         digits[i] += 1
        #     return digits

        # # 简单写法
        # for i in reversed(range(len(digits))):
        #     if digits[i] == 9:
        #         digits[i] = 0
        #     else:
        #         digits[i] += 1
        #         return digits
        # digits[0] = 1
        # digits.append(0)
        # return digits

        # 快速写法
        carry = False
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == True:
                digits[i] += 1
                carry = False
            if digits[i] >= 10:
                digits[i] -= 10
                carry = True
        if carry == True:
            digitnew = [1]
            for i in range(len(digits)):
                digitnew.append(digits[i])
            digits = digitnew
        return digits


sol = Solution()
ans = sol.plusOne([4,9,9,9,9])
print(ans)