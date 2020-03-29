'''
820. 单词的压缩编码
Medium

https://leetcode-cn.com/problems/short-encoding-of-words/
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
'''
class Solution:
    def minimumLengthEncoding(self, words) -> int:
        # # 我的方法 先按字符串长度从大到小排序 再遍历，查找当前字符串是否在s中，以及在s中的位置
        # words.sort(key=lambda x: len(x),reverse=True)
        # print(words)
        # s = ""
        # for x in words:
        #     if x not in s:
        #         s += x+'#'
        #     else:
        #         idx = s.find(x)
        #         print(idx)
        #         print(s[idx+len(x)])
        #         if s[idx+len(x)]!='#':
        #             s += x + '#'
        # print(s)
        # return len(s)

        # # 存储后缀
        # good = set(words)
        # for word in words:
        #     for k in range(1, len(word)):  # 枚举单词所有的后缀。对于每个后缀，如果其存在 words 列表中，我们就将其从列表中删除。（需先去重）
        #         print(word[k:])
        #         good.discard(word[k:])    # discard用于移除指定的集合元素，在移除一个不存在的元素时不会发生错误
        # return sum(len(word) + 1 for word in good)

        # 字典树
        import collections
        from functools import reduce
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]        # 找到是否不同的单词具有相同的后缀，我们可以将其反序之后插入字典树中。

        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)  # 字典树的叶子节点（没有孩子的节点）就代表没有后缀的单词，统计叶子节点代表的单词长度加一的和即为我们要的答案。

sol = Solution()
# ans = sol.minimumLengthEncoding(["time", "mel", "bell"])
# print(ans)
ans = sol.minimumLengthEncoding(["me", "time"])
print(ans)