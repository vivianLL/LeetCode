import heapq

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # 法一：递归 复杂度高
        # if len(word1)==0:
        #     return len(word2)
        # elif len(word2)==0:
        #     return len(word1)
        # elif word1[-1]==word2[-1]:
        #     return self.minDistance(word1[:-1], word2[:-1])
        # else:
        #     return min(self.minDistance(word1,word2[:-1])+1,self.minDistance(word1[:-1],word2)+1,self.minDistance(word1[:-1],word2[:-1])+1)

        # #法二：二重循环 建立二维矩阵 时间复杂度为 O(mn), 空间复杂度 O(mn)
        # if len(word1) == 0:
        #     return len(word2)
        # elif len(word2)==0:
        #     return len(word1)
        # M = len(word1)
        # N = len(word2)
        # output = [[0] * (N + 1) for _ in range(M + 1)]
        # for i in range(M + 1):
        #     for j in range(N + 1):
        #         if i == 0 and j == 0:
        #             output[i][j] = 0
        #         elif i == 0 and j != 0:
        #             output[i][j] = j
        #         elif i != 0 and j == 0:
        #             output[i][j] = i
        #         elif word1[i - 1] == word2[j - 1]:
        #             output[i][j] = output[i - 1][j - 1]
        #         else:
        #             output[i][j] = min(output[i - 1][j - 1] + 1, output[i - 1][j] + 1, output[i][j - 1] + 1)
        # return output[M][N]

        # #法三 时间复杂度为 O(mn), 空间复杂度 O(m)
        # if len(word1) == 0:
        #     return len(word2)
        # elif len(word2) == 0:
        #     return len(word1)
        # M = len(word1)
        # N = len(word2)
        # tmp = [i for i in range(N + 1)]
        # value = None
        #
        # for i in range(M):
        #     tmp[0] = i + 1
        #     last = i
        #     for j in range(N):
        #         if word1[i] == word2[j]:
        #             value = last
        #         else:
        #             value = 1 + min(last, tmp[j], tmp[j + 1])
        #         last = tmp[j + 1]
        #         tmp[j + 1] = value
        # return value

        # 法三
        heap = [(0, word1, word2)]
        seen = set()

        while len(heap) > 0:
            dist, w1, w2 = heapq.heappop(heap)
            if w1 == w2:
                return dist
            if (w1, w2) not in seen:
                seen.add((w1, w2))
                while w1 and w2 and w1[-1] == w2[-1]:
                    w1 = w1[:-1]
                    w2 = w2[:-1]
                else:
                    heapq.heappush(heap, (dist + 1, w1[:-1], w2))
                    heapq.heappush(heap, (dist + 1, w1, w2[:-1]))
                    heapq.heappush(heap, (dist + 1, w1[:-1], w2[:-1]))


sol = Solution()
ans = sol.minDistance("se","")
print(ans)
ans = sol.minDistance("intention","execution")
print(ans)
ans = sol.minDistance("dinitrophenylhydrazine","benzalphenylhydrazone")
print(ans)
