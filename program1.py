class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():  # If it's one of the opening brackets
                stack.append(char)
            elif char in bracket_map:  # If it's one of the closing brackets
                if not stack or stack[-1] != bracket_map[char]:  # Check for matching opening bracket
                    return False
                stack.pop()  # Pop the last opening bracket
        
        return len(stack) == 0  # If stack is empty, all brackets are matched

# Example usage:
# sol = Solution()
# print(sol.isValid("()"))        # Output: True
# print(sol.isValid("()[]{}"))    # Output: True
# print(sol.isValid("(]"))        # Output: False
