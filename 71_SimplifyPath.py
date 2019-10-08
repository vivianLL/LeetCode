'''
71. Simplify Path
Medium

https://leetcode.com/problems/simplify-path/
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_array = path.split("/")
        print(path_array)
        stack = []
        res_path = ""
        for item in path_array:
            if item not in ["", ".", ".."]:
                stack.append(item)
            if ".." == item and stack:
                stack.pop(-1)
        if [] == stack:
            return "/"
        for item in stack:
            res_path += "/" + item + ""   # ""加不加都行
        return res_path


sol = Solution()
ans = sol.simplifyPath("/a/.///b/../../c/d")
print(ans)
ans = sol.simplifyPath("/a//b////c/d//././/..")
print(ans)
# 思路：
# 字符串处理，由于"."返回当前目录，".."是返回上级目录（如果是根目录则不处理），因此可以考虑用栈记录路径名，以便于处理。需要注意几个细节：
# 重复连续出现的'/'，只按1个处理，即跳过重复连续出现的'/'；
# 如果路径名是"."，则不处理；
# 如果路径名是".."，则需要弹栈，如果栈为空，则不做处理；
# 如果路径名为其他字符串，入栈。
# 最后，再逐个取出栈中元素（即已保存的路径名），用'/'分隔并连接起来，不过要注意顺序呦。