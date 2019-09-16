'''
68. Text Justification
Hard

https://leetcode.com/problems/text-justification/
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
'''
class Solution:
    def fullJustify(self, words, maxWidth: int):
        lines = []
        i = 0
        while i < len(words):
            line = []
            lenline = 0
            lenword = 0

            while i < len(words):
                w = words[i]
                nextl = lenline + len(w) + (1 if lenline else 0)
                if nextl > maxWidth:
                    break

                line.append(w)
                lenline = nextl
                lenword += len(w)

                i += 1

            if i == len(words) or len(line)==1:
                l = ' '.join(line) + ' '*(maxWidth - lenline)
                lines.append(l)
                # print(lines)
            else:
                space_len = maxWidth - lenword
                part_count = len(line) - 1
                base_space = space_len // part_count
                extra_space = space_len % part_count
                l = line[0]
                for j in range(1,len(line)):
                    l += ' '*base_space
                    if extra_space:
                        l += ' '
                        extra_space -= 1
                    l += line[j]
                lines.append(l)
        return lines

sol = Solution()
ans = sol.fullJustify(["What","must","be","acknowledgment","shall","be"],16)
print(ans)