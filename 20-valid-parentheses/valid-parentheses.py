class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # If it's an opening bracket, push to stack
            if ch in '([{':
                stack.append(ch)
            # If it's a closing bracket
            elif ch in ')]}':
                # Stack empty or top not matching pair → invalid
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # Otherwise, valid pair → pop the stack
                stack.pop()

        # If stack empty → all brackets matched correctly
        return len(stack) == 0