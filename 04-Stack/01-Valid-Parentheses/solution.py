"""
Valid Parentheses
LeetCode 20

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', ']':'[','}':'{'}
        for p in s:
            if p in pair.values():
                stack.append(p) # push
            elif p in pair:
                if stack and pair[p] == stack[-1]: # if p is close and compatible
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.isValid("([{}])"))
    print(solution.isValid("([{])"))
    # TODO: Add test cases
    pass
