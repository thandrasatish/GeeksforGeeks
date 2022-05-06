class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k-1:
                k_tmp = k 
                while stack and k_tmp > 1:
                    stack.pop()
                    k_tmp -= 1
            else:
                if stack and stack[-1][0] == c:
                    stack.append((c,stack[-1][1]+1))
                else:
                    stack.append((c,1))
        res = ""
        idx = 0
        while idx < len(stack):
            c = stack[idx][0]
            res += c
            idx += 1
        return res
