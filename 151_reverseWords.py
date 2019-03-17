'''
151. Reverse Words in a String
Medium

https://leetcode.com/problems/reverse-words-in-a-string/
Given an input string, reverse the string word by word.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        # # 自写代码 空间复杂度O(n)
        # slist = list(s)[::-1]
        # temp = []
        # newlist = []
        # for i in range(len(slist)):
        #     if slist[i]!=' ':
        #         temp.append(slist[i])
        #     else:
        #         newlist.extend(temp[::-1])
        #         newlist.extend(' ')
        #         temp = []
        # newlist.extend(temp[::-1])    # 最后一个单词单独提出
        # s = ''.join(newlist).strip()  # 去除头尾空格
        # s = ' '.join(s.split())       # split里不可加参数，如为s = ' '.join(s.split(' '))则无法去除多个空格
        # return s

        # # 简单写法
        # return " ".join([t for t in s.strip().split()][::-1])

        # 剑指offer写法
        listofs = list(s)
        if len(listofs) == 0:
            return s

        def reverse(listofs):
            m = len(listofs)
            for i in range(m >> 1):
                listofs[i], listofs[m - 1 - i] = listofs[m - 1 - i], listofs[i]
            return listofs

        # 字符串整体翻转
        listofs = reverse(listofs)
        start = end = 0
        while end < len(listofs):
            # 对每个单词做翻转
            if listofs[end] == ' ':
                listofs[start:end] = reverse(listofs[start:end])
                start = end + 1
            end += 1
            # 最后一个单词单独提出
            if end == len(listofs) - 1:
                listofs[start:end + 1] = reverse(listofs[start:end + 1])
        listofs = ''.join(listofs).strip()  # 去除头尾空格
        return ' '.join(listofs.split())



sol = Solution()
s = "the sky is blue"
ans = sol.reverseWords(s)
print(ans)
s = "  hello world!  "
ans = sol.reverseWords(s)
print(ans)
s = "a good   example"
ans = sol.reverseWords(s)
print(ans)