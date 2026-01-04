"""
Valid Palindrome
LeetCode 125

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -=1
                continue
            else:
                if s[l].lower() == s[r].lower():
                    l +=1
                    r -=1
                else:
                    return False
        return True



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.isPalindrome("Was it a car or a cat I saw?"))
    print(solution.isPalindrome("tab a cat"))
    # TODO: Add test cases
    pass
