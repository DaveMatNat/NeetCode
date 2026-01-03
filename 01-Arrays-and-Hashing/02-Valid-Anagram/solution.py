"""
Valid Anagram
LeetCode 242

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(26) => O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            idx_s = ord(s[i]) - ord('a')
            idx_t = ord(t[i]) - ord('a')
            count[idx_s] += 1
            count[idx_t] -= 1
        
        for i in count:
            if i !=0:
                return False
        return True
        


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.isAnagram("silent", "listen"))
    # TODO: Add test cases
    print(solution.isAnagram("speak", "spoke"))
    pass
