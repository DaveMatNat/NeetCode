"""
Longest Repeating Character Replacement
LeetCode 424

Problem: 

Approach:

Time Complexity: O(26 * n)
Space Complexity: O(26)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.characterReplacement("AAABABB",1))
    print(solution.characterReplacement("XYYX",2))
    # TODO: Add test cases
    pass
