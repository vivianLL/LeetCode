'''
204. 计数质数

https://leetcode-cn.com/problems/count-primes/
简单
统计所有小于非负整数 n 的质数的数量。
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        # # 自写方法 超时
        # if n<=2:
        #     return 0
        # l = [2]
        # x = 3
        # while x < n:
        #     flag = True
        #     for i in l:
        #         if x % i == 0:
        #             flag = False
        #             break
        #     if flag==True:
        #         l.append(x)
        #     x += 1
        # return len(l)

        if n<=2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            # [::i]取i的倍数
            primes[i * i:n:i] = [False] * len(primes[i * i:n:i])   # 注意此处索引要用i^2开始到n，步长为i，比[2 * i:n:i]要快

        return sum(primes)


sol = Solution()
ans = sol.countPrimes(12)
print(ans)
# 质数的性质：
# 对于一个数x，只需对[2,]的数进行整除，若能整除则不是素数，不能整除则为素数。（maybe超时）。
# 一个合数必然能分解成质因子之积。因此我们每当找到一个素数，设它为 i，那么2∗i,3∗i,4∗i,....,n这些数来说肯定都是合数。删掉！
# so 只需遍历[2,]，因为超过部分如果不是素数，则在前面的因子的倍数（cur_value）已经被删除了。