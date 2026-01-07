"""
Longest Substring Without Repeating Characters
LeetCode 3

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(m)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
            
                


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    # TODO: Add test cases
    pass
